---
name: sw-rule
description: Scaffold einer Shopware-6 Custom Rule (PHP Rule + Admin-Bedingungs-Komponente) für den Rule Builder, inkl. Registrierung.
argument-hint: <ruleName> [--plugin <PluginName>] [--scope cart|checkout]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-rule

Erzeuge eine Custom Rule. Skills: `sw-custom-rule`, `sw-rule-condition`.

## Ablauf
1. Rule-Name (camelCase, z.B. `ffMinAge`) + Ziel-Plugin + Scope (Cart/Checkout/LineItem).
2. PHP `src/Core/Rule/<Name>Rule.php` (extends `Rule`, `RULE_NAME`, `match(RuleScope)`, `getConstraints`, `getName`),
   Registrierung via `shopware.rule.definition`-Tag.
3. Admin-Bedingungs-Komponente `sw-condition-<name>` (`sw-condition-base`-Mixin) + Registrierung beim
   `ruleConditionDataProviderService` (Scopes, Operatoren).
4. Falls `match()` Zusatzdaten braucht: Daten über Scope/Collector bereitstellen.

Bestehende Rules nicht überschreiben; Felder von PHP-Constraints und Admin-Komponente konsistent halten.
