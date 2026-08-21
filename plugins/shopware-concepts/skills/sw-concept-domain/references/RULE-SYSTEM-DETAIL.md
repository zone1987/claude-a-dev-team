# Shopware rule system — complete concept documentation

Sources: `concepts/framework/rule-system/index.md`, `rule-concepts.md`, `rule-evaluation.md`

---

## Contents

- [Rule system overview (index.md)](#rule-system-overview-indexmd)
- [Rule Concepts (rule-concepts.md)](#rule-concepts-rule-conceptsmd)
- [Rule Evaluation (rule-evaluation.md)](#rule-evaluation-rule-evaluationmd)

## Rule system overview (index.md)

A generic system for describing business conditions as **composable rules**.
Evaluated against a specific context (cart, order, customer).

The **Rule Builder** = an administration feature for visually configuring and combining rules.

### Areas of use

- **Checkout / cart** — availability and behaviour of shipping/payment methods, product prices
- **Promotions** — applying/restricting based on customer, cart content, other criteria
- **Flow Builder** — rule conditions for flows

### Example scenario

"If a customer buys a car, they get a pair of sunglasses for free in the same order."

The rule system sits between the cart state (a car is in the cart) and the desired action
(the sunglasses are free), without embedding that logic directly into the cart.

---

## Rule Concepts (rule-concepts.md)

### Rule

- Single condition → `true` or `false`
- Answers specific questions: "Does the customer belong to the default group?", "Is the cart > €50?"
- **No data fetching** — receives all data via the RuleScope
- **No side effects** — changes nothing in the cart, orders or other state (pure function)

### RuleScope (context carrier)

Defines the context for rule evaluation and provides the data.

| Scope | Content |
|---|---|
| `CheckoutRuleScope` | SalesChannelContext (customer, sales channel, currency, etc.) |
| `CartRuleScope` | CheckoutRuleScope + cart data |
| `FlowRuleScope` | Checkout info + order data |
| `LineItemScope` | A single line item |

Rules depend only on what the scope exposes → reusable across features.

### Container rules (tree structure)

Combine the results of other rules via logical operators. No condition evaluation of their own.

| Container | Meaning |
|---|---|
| `AndRule` | All children must match |
| `OrRule` | At least one child must match |
| `NotRule` | This child must not match |

A complete rule definition = a **tree** of container nodes (AND/OR/NOT) and leaf nodes
(concrete conditions).

Example tree:
```
OrRule
├── LineItemsInCartCountRule (operator: ">=", count: 40)
└── GoodsPriceRule (operator: ">=", amount: 500)
```

### Operators and comparisons

- Equality/inequality: `=`, `!=`
- Ranges: `<`, `<=`, `>`, `>=`
- Emptiness checks: `empty`

Consistent semantics via `RuleComparison` for comparable value types.

### Rule Config (UI contract)

`RuleConfig` defines which fields and operators are shown in the admin UI:

- **Operator set** — which operators are valid for this rule
- **Field definitions** — `name` (identifier), `type` (UI representation: number/text/date), additional config
  (options for select fields, unit for number fields)

### Rule Constraints (validation)

`RuleConstraints` describe what a valid configuration for a rule is.

- **Value constraints** — fields must have certain types/values (not empty, numeric, etc.)
- **Operator constraints** — only certain operators allowed

---

## Rule Evaluation (rule-evaluation.md)

### Lifecycle overview

```
Rule Builder → Validation → Database → Runtime scope → Match / Evaluate
```

1. The Rule Builder lets the user create a rule tree (containers + conditions)
2. The rule system validates each condition against the corresponding rule class in the registry
3. Valid rules are persisted in the DB
4. At runtime: the domain builds the matching RuleScope, computes the matching rules
5. Features filter by rule IDs in the context or evaluate the rule tree directly

### 1. From Rule Builder to a stored rule definition

**Database structure:**
- `rule` — represents the entire rule
- `rule_condition` — container nodes and leaf conditions
  - `parent_id` — for the tree structure
  - `type` — maps to a rule class
  - `value` — JSON with the configured values (operator, thresholds, IDs)

**Validation**: `RuleValidator` subscribes to write events and checks the `RuleConditionEntity`:
- Resolve the type → rule class via `RuleConditionRegistry`
- Check the constraints of the rule class
- Invalid payloads are rejected

### 2. Preparing the evaluation

**Scope owners** (who builds which scope):

- **Cart/checkout**: `CartRuleLoader` — main entry point; builds scopes and evaluates rules
- **Flows**: `FlowRuleScopeBuilder` — builds the `FlowRuleScope`; reconstructs a cart-like context from the order
- **Line items**: `AnyRuleLineItemMatcher` — builds the `LineItemScope` for single-line tests

Rules are **pure functions** — dependent only on the scope passed in, no global state.

### 3. Matching rules (checkout)

**Iterative process** (during checkout):

```
Load candidate rules
→ Build scope from cart
→ Filter matching rules (RuleCollection::filterMatchingRules)
→ Cart changed? → Recalculate cart → (repeat)
→ Expose matching rule IDs on SalesChannelContext
```

Result: a consistent pair (cart, matching rule IDs).

### 4. Using rules at runtime

#### ID-based decisions (the performance path)

Entities such as `shipping_method`, `payment_method`, `tax_provider` have an `availability_rule_id`.
Allowed if the rule ID is in `SalesChannelContext::getRuleIds()` → no direct call needed.

#### Direct evaluation (the flexibility path)

Features fetch the rule tree from the DB, build the corresponding scope, and call `Rule::match(RuleScope $scope)`.

Delegation with container rules:
```
Feature → OrRule::match(scope)
OrRule → Rule1::match(scope) → false
OrRule → Rule2::match(scope) → false
OrRule → Feature: false
```
