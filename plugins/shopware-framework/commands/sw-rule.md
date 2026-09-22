---
name: sw-rule
description: Scaffolds a Shopware 6 custom rule (a PHP rule plus an admin condition component) for the rule builder, including registration.
argument-hint: <name> [--plugin <PluginName>] [--scope cart|checkout|lineItem]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-rule

Produce a custom rule. Skill: `sw-automation`.

## Steps
1. Settle the rule name (camelCase, e.g. `ffMinAge`), the target plugin and the scope (cart,
   checkout, lineItem).
2. PHP: `src/Core/Rule/<Name>Rule.php` (extends `Rule`, with `RULE_NAME`, `match(RuleScope)`,
   `getConstraints` and `getName`), registered through the `shopware.rule.definition` tag.
3. The admin condition component `sw-condition-<name>` (using the `sw-condition-base` mixin),
   registered with `ruleConditionDataProviderService` (scopes and operators).
4. Where `match()` needs extra data, supply it through the scope or a collector.

Never overwrite an existing rule. Keep the fields of the PHP constraints and the admin component
consistent — they describe the same condition.

## Before it counts as done

`composer gate` green, unit tests for `match()` covering both outcomes, and the rule proved
end-to-end: selectable in the rule builder and taking effect in the cart.
→ `shopware-testing` → `sw-testing-standard`
