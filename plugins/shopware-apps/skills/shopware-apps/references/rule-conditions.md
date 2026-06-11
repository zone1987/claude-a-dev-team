---
title: Custom Rule Conditions
impact: LOW
impactDescription: Apps define custom rule conditions via manifest and Twig scripts
tags: rule, conditions, rule-builder, twig, scripts
---

## Custom Rule Conditions

Since Shopware 6.4.12.0, apps can add custom conditions to the Rule Builder via manifest.xml and Twig scripts.

### Manifest Definition

```xml
<rule-conditions>
    <rule-condition>
        <identifier>my_custom_condition</identifier>
        <name>Customer first name check</name>
        <name lang="de-DE">Kunden-Vorname prüfen</name>
        <group>customer</group>
        <script>custom-condition.twig</script>
        <constraints>
            <single-select name="operator">
                <label>Operator</label>
                <options>
                    <option value="="><name>Is equal to</name></option>
                    <option value="!="><name>Is not equal to</name></option>
                </options>
                <required>true</required>
            </single-select>
            <text name="firstName">
                <label>First Name</label>
                <required>true</required>
            </text>
        </constraints>
    </rule-condition>
</rule-conditions>
```

### Groups

`general`, `customer`, `cart`, `item`, `promotion`, `misc`

### Script Implementation

Place in `Resources/scripts/rule-conditions/custom-condition.twig`:

```twig
{% if scope.salesChannelContext.customer is not defined %}
    {% return false %}
{% endif %}

{% return compare(operator, scope.salesChannelContext.customer.firstName, firstName) %}
```

### Available in Scripts

- `scope` — RuleScope with access to SalesChannelContext and cart
- Constraint values as named variables (e.g., `operator`, `firstName`)
- `compare(operator, value, comparable)` — Helper for comparisons

### Compare Operators

`=`, `!=`, `>`, `>=`, `<`, `<=`, `empty`

### Important Notes

- Scripts must return boolean values
- The `identifier` must not change after creation
- Constraint names become script variables
- Scripts execute in a sandboxed environment
