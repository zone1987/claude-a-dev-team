# B2B Suite Migration zu B2B Components — Entwickler-Referenz

> **Wichtig:** B2B Suite wird ab Shopware 6.8 nicht mehr unterstuetzt.
> Migration sollte zeitnah geplant werden.

## Zweck

Das B2B Suite Migration Extension migriert Daten aus der B2B Suite in B2B Components
(Teil des Commercial Plugins). Die Migration ergaenzt Daten in B2B Components ohne
B2B Suite-Daten zu loeschen.

## Voraussetzungen

- B2B Suite Version 4.9.3 oder hoeher
- Queue Worker muss laufen (`bin/console messenger:consume`)
- Datenbank-Backup vor Migration erstellen (besonders wenn B2B Commercial bereits Daten hat)
- Budget Management: benoetigt B2B Commercial Version 7.6.0 oder hoeher

## Migrationstabellen

Drei Tracking-Tabellen werden angelegt:

| Tabelle                          | Zweck                                         |
|----------------------------------|-----------------------------------------------|
| `b2b_components_migration_state` | Status des Migrationsprozesses pro Entitaet   |
| `b2b_components_migration_map`   | Mapping zwischen Suite- und Components-IDs    |
| `b2b_components_migration_errors`| Fehlerprotokoll fuer Debugging                |

## Migrationsablauf

1. **Message Queue** verarbeitet die Migration (skalierbar fuer grosse Datenmengen)
2. **Sequentielle Verarbeitung** respektiert Abhaengigkeiten:
   - Employee → Budget (Budget braucht Employee)
   - Employee → Quote → Shopping List
3. **Entity-Sequencing** innerhalb jeder Komponente

## Konfiguration via XML

Alle Feld-Mappings sind in XML-Konfigurationsdateien definiert:

```xml
<entity>
  <name>migration_b2b_component_employee</name>
  <source>b2b_debtor_contact</source>      <!-- Quell-Tabelle -->
  <target>b2b_employee</target>            <!-- Ziel-Tabelle -->
  <fields>
    <field source="first_name" target="first_name"/>
    <field source="last_name" target="last_name"/>
    <field source="active" target="status" handler="b2b.employee.employee_status_transformer"/>
  </fields>
</entity>
```

## Handler (Custom Transformations)

Handler ermöglichen komplexe Datentransformationen vor dem Mapping.

### Handler registrieren

```php
$services->set(MyCustomTransformer::class)
    ->lazy()  // Best Practice: lazy loading
    ->args([service(ExtensionDispatcher::class)])
    ->tag('b2b.migration.transformer');
```

### Handler implementieren

```php
class MyStatusTransformer extends AbstractFieldTransformer
{
    public function __construct(ExtensionDispatcher $extensions)
    {
        parent::__construct($extensions);
    }

    public function getName(): string
    {
        return 'b2b.my.status_transformer';  // Eindeutiger Name, referenziert in XML
    }

    protected function requiredSourceFields(): array
    {
        return ['active'];  // Pflichtfelder aus Quell-Tabelle
    }

    protected function _transform(Field $field, array $sourceRecord): mixed
    {
        $active = $sourceRecord[$field->getSource()] ?? 0;
        return $active ? 'active' : 'inactive';
    }
}
```

### Handler-Optionen im XML

**Einzel-Quelle → Einzel-Ziel:**
```xml
<field source="active" target="status" handler="b2b.my.status_transformer"/>
```

**Mehrere Quellen → Einzel-Ziel:**
```xml
<field target="quote_number" handler="b2b.my.transformer">
    <source>currency_factor</source>
    <source>auth_id.b2b_store_front_auth.customer_id.customer.sales_channel_id</source>
</field>
```

**Mehrere Quellen → Mehrere Ziele:**
```xml
<field handler="b2b.my.transformer">
    <source>source_field_a</source>
    <source>source_field_b</source>
    <target>target_field_x</target>
    <target>target_field_y</target>
</field>
```

**Einzel-Quelle → Mehrere Ziele:**
```xml
<field source="converted_at" handler="b2b.my.transformer">
    <target>order_version_id</target>
    <target>order_id</target>
</field>
```

### Relational-Pfade in Source-Feldern

Punktgetrennte Pfade traversieren Relationen (z.B. `auth_id.b2b_store_front_auth.customer_id`).

### Rueckgabewerte des _transform-Methode

- Einzel-Ziel: Einzelwert (string, int, JSON)
- Mehrere Ziele: Assoziatives Array `['target_field' => value, ...]`

### Handler-Logik erweitern

Handler dispatchen via `ExtensionDispatcher` ein `B2BMigrationFieldTransformerExtension`-Event
mit dem technischen Namen des Handlers. Subscriber koennen eigene Logik hinzufuegen ohne
den Original-Handler zu aendern.

## Komponenten-Migration-Reihenfolge

1. Business Partner (Debtor) → `swag_b2b_business_partner` → `swag_b2b_business_partner`
2. Employees (Contacts) → `b2b_debtor_contact` → `b2b_employee`
3. Roles → `b2b_acl_route` → `swag_b2b_role`
4. Quotes → `b2b_offer` → `quote`
5. Shopping Lists → `b2b_order_list` → `b2b_components_shopping_list`
6. Budgets → Eigene Migration (benoetigt Commercial 7.6.0+)

## Fehlerbehandlung

Fehler werden in `b2b_components_migration_errors` protokolliert.
Migrationen koennen nach Fehlerbehebung erneut ausgefuehrt werden (idempotent dank Mapping-Tabelle).

## Nachmigrations-Aktionen

Budget Management: Organisations-Einheit des Budgets muss nach Migration
**manuell in B2B Commercial zugewiesen** werden (kann nicht automatisch migriert werden).
