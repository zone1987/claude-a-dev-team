# Shopware rule system — concept

Complete concept documentation: `RULE-SYSTEM-DETAIL.md`

## Quick overview

The rule system describes business conditions as **composable rules** that are evaluated against a
context (cart, order, customer). Used in: checkout, promotions, Flow Builder.

### Rule

- Single condition → `true` or `false`
- No side effects, no data fetching (pure function)
- Receives all data via the **RuleScope**

### RuleScope (context carrier)

- `CheckoutRuleScope` — SalesChannelContext (customer, currency, etc.)
- `CartRuleScope` — checkout + cart data
- `FlowRuleScope` — checkout + order data
- `LineItemScope` — a single line item

### Container rules (tree structure)

- `AndRule` — all children must match
- `OrRule` — at least one child must match
- `NotRule` — the child must not match
- Nestable to any depth

### Evaluation lifecycle

1. Rule Builder → visual configuration
2. Validation via `RuleConstraints` and `RuleConfig`
3. Persistence in the DB (`rule` + `rule_condition` with `parent_id`)
4. Runtime: `CartRuleLoader` builds the scope, filters candidates, iterates until stable
5. ID-based (payment method availability) or direct evaluation (Flow Builder)

Technical implementation: `shopware-framework` (dev plugin)
