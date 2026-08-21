# B2B Suite migration to B2B Components — Developer reference

> **Important:** the B2B Suite is no longer supported as of Shopware 6.8.
> The migration should be planned soon.

## Contents

- [Purpose](#purpose)
- [Prerequisites](#prerequisites)
- [Migration tables](#migration-tables)
- [Migration process](#migration-process)
- [Configuration via XML](#configuration-via-xml)
- [Handlers (custom transformations)](#handlers-custom-transformations)
- [Component migration order](#component-migration-order)
- [Error handling](#error-handling)
- [Post-migration actions](#post-migration-actions)

## Purpose

The B2B Suite Migration extension migrates data from the B2B Suite into B2B Components
(part of the Commercial plugin). The migration adds data to B2B Components without
deleting B2B Suite data.

## Prerequisites

- B2B Suite version 4.9.3 or higher
- The queue worker must be running (`bin/console messenger:consume`)
- Create a database backup before the migration (especially if B2B Commercial already has data)
- Budget Management: requires B2B Commercial version 7.6.0 or higher

## Migration tables

Three tracking tables are created:

| Table                            | Purpose                                       |
|----------------------------------|-----------------------------------------------|
| `b2b_components_migration_state` | State of the migration process per entity     |
| `b2b_components_migration_map`   | Mapping between Suite and Components IDs      |
| `b2b_components_migration_errors`| Error log for debugging                       |

## Migration process

1. The **message queue** processes the migration (scalable for large data volumes)
2. **Sequential processing** respects the dependencies:
   - Employee → Budget (Budget needs Employee)
   - Employee → Quote → Shopping List
3. **Entity sequencing** within each component

## Configuration via XML

All field mappings are defined in XML configuration files:

```xml
<entity>
  <name>migration_b2b_component_employee</name>
  <source>b2b_debtor_contact</source>      <!-- Source table -->
  <target>b2b_employee</target>            <!-- Target table -->
  <fields>
    <field source="first_name" target="first_name"/>
    <field source="last_name" target="last_name"/>
    <field source="active" target="status" handler="b2b.employee.employee_status_transformer"/>
  </fields>
</entity>
```

## Handlers (custom transformations)

Handlers enable complex data transformations before the mapping.

### Registering a handler

```php
$services->set(MyCustomTransformer::class)
    ->lazy()  // Best practice: lazy loading
    ->args([service(ExtensionDispatcher::class)])
    ->tag('b2b.migration.transformer');
```

### Implementing a handler

```php
class MyStatusTransformer extends AbstractFieldTransformer
{
    public function __construct(ExtensionDispatcher $extensions)
    {
        parent::__construct($extensions);
    }

    public function getName(): string
    {
        return 'b2b.my.status_transformer';  // Unique name, referenced in the XML
    }

    protected function requiredSourceFields(): array
    {
        return ['active'];  // Required fields from the source table
    }

    protected function _transform(Field $field, array $sourceRecord): mixed
    {
        $active = $sourceRecord[$field->getSource()] ?? 0;
        return $active ? 'active' : 'inactive';
    }
}
```

### Handler options in the XML

**Single source → single target:**
```xml
<field source="active" target="status" handler="b2b.my.status_transformer"/>
```

**Several sources → single target:**
```xml
<field target="quote_number" handler="b2b.my.transformer">
    <source>currency_factor</source>
    <source>auth_id.b2b_store_front_auth.customer_id.customer.sales_channel_id</source>
</field>
```

**Several sources → several targets:**
```xml
<field handler="b2b.my.transformer">
    <source>source_field_a</source>
    <source>source_field_b</source>
    <target>target_field_x</target>
    <target>target_field_y</target>
</field>
```

**Single source → several targets:**
```xml
<field source="converted_at" handler="b2b.my.transformer">
    <target>order_version_id</target>
    <target>order_id</target>
</field>
```

### Relational paths in source fields

Dot-separated paths traverse relations (e.g. `auth_id.b2b_store_front_auth.customer_id`).

### Return values of the _transform method

- Single target: single value (string, int, JSON)
- Several targets: associative array `['target_field' => value, ...]`

### Extending handler logic

Handlers dispatch a `B2BMigrationFieldTransformerExtension` event via the `ExtensionDispatcher`
carrying the technical name of the handler. Subscribers can add their own logic without
changing the original handler.

## Component migration order

1. Business Partner (Debtor) → `swag_b2b_business_partner` → `swag_b2b_business_partner`
2. Employees (Contacts) → `b2b_debtor_contact` → `b2b_employee`
3. Roles → `b2b_acl_route` → `swag_b2b_role`
4. Quotes → `b2b_offer` → `quote`
5. Shopping Lists → `b2b_order_list` → `b2b_components_shopping_list`
6. Budgets → separate migration (requires Commercial 7.6.0+)

## Error handling

Errors are logged in `b2b_components_migration_errors`.
Migrations can be re-run after fixing errors (idempotent thanks to the mapping table).

## Post-migration actions

Budget Management: the organizational unit of a budget must be
**assigned manually in B2B Commercial** after the migration (it cannot be migrated automatically).
