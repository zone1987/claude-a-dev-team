# B2B Employee Management — Entwickler-Referenz

## Grundkonzept

Employee Management ermoeglicht B2B-Haendlern, eine Kaeuferplattform fuer Geschaeftspartner
aufzubauen. Mitarbeiter (Employees) sind separate Logins innerhalb eines Unternehmens-Kunden
(Business Partner) und agieren im Namen des Unternehmens.

**Kernentitaeten:**
- **Business Partner** (`swag_b2b_business_partner`): Erweiterung eines regulaeren Storefront-Kunden
- **Employee** (`swag_b2b_employee`): Separate Login-Instanz mit eigenem Passwort und Rolle
- **Role** (`swag_b2b_role`): Berechtigungs-Set, das einem Mitarbeiter zugewiesen wird

## Datenbankschema

```sql
swag_b2b_business_partner:
  id, customer_id (FK), default_role_id (FK), custom_fields

swag_b2b_employee:
  id, business_partner_customer_id (FK), role_id (FK), active,
  first_name, last_name, email, password, recovery_time, recovery_hash

swag_b2b_role:
  id, business_partner_customer_id (FK), name, permissions (JSON)
```

Employees sind ueber E-Mail eindeutig. Beim Einladen wird auf Eindeutigkeit geprueft.

## Mitarbeiter anlegen / einladen

### Via Storefront
Business Partner navigiert zu `/account` → Employee-Seite → Neuen Mitarbeiter hinzufuegen.

### Via Store API
`POST /store-api/employee/create` (als eingeloggter Kunde).

### Via Administration
Merchant waehlt Business-Partner-Kunden → Tab "Company" → Mitarbeiter hinzufuegen.

**Einladungs-URL (Standard):** `/account/business-partner/employee/invite/%%RECOVERHASH%%`

**URL anpassen via System Config:**
```php
// Schluessel: b2b.employee.invitationURL
```

## Berechtigungssystem

Roles enthalten eine Liste von Permissions als JSON. Business Partner definiert eine
Default-Rolle, die beim Erstellen neuer Mitarbeiter vorausgewaehlt wird.

### Eigene Permissions via Plugin

```php
class PermissionCollectorSubscriber implements EventSubscriberInterface
{
    public const OWN_ENTITY_READ = 'own_entity.read';
    public const OWN_ENTITY_EDIT = 'own_entity.edit';

    public static function getSubscribedEvents(): array
    {
        return [PermissionCollectorEvent::NAME => ['onAddOwnPermissions', 1000]];
    }

    public function onAddOwnPermissions(PermissionCollectorEvent $event): void
    {
        $collection = $event->getCollection();
        $collection->addPermission(self::OWN_ENTITY_READ, 'own_entity', []);
        $collection->addPermission(self::OWN_ENTITY_EDIT, 'own_entity', [self::OWN_ENTITY_READ]);
    }
}
```

Twig-Pruefung: `{% if isB2bAllowed(constant('...::OWN_ENTITY_READ')) %}`

PHP-Pruefung: `$context->getCustomer()->getEmployee()->getRole()->can('own_entity.read')`

### Eigene Permissions via App

Via Store API `POST /store-api/permission` mit Berechtigungsnamen (muss eindeutig sein).
Snippet-Key: `b2b.role-edit.permissions.[name]` z.B. `b2b.role-edit.permissions.order.delete`.

## Route Restriction (Denylist)

Mitarbeiter teilen den Kunden-Account mit dem Business Partner. Um unerlaubte
Daten-Aenderungen zu verhindern, gibt es eine Denylist:

Konfiguration: `Resources/config/employee_route_access.xml`

```xml
<routes>
    <denied>store-api.account.change-profile</denied>
    <denied>store-api.account.change-email</denied>
    <allowed>store-api.account.login</allowed>
</routes>
```

Der `B2bRouteBlocker` subscriber prueft Routen vor Erreichen des Controllers.

### Denylist erweitern (Decoration)

```php
class DecoratedEmployeeRouteAccessLoader extends AbstractEmployeeRouteAccessLoader
{
    private const CONFIG = __DIR__ . '/new-custom-employee_route_access.xml';

    public function load(): array
    {
        $oldConfig = $this->decorated->load();
        $customConfig = (array) @simplexml_load_file(self::CONFIG);
        return array_merge_recursive($oldConfig, $customConfig);
    }
}
```

## Organization Unit

Ermoeglicht differenzierte Zugriffsrechte innerhalb komplexer Unternehmensstrukturen.
Setzt Employee Management voraus.

### Entitaeten

```sql
b2b_components_organization:
  id, name, customer_id (FK), default_shipping_address_id (FK),
  default_billing_address_id (FK), custom_fields

b2b_components_organization_customer_address:
  id, organization_id (FK), customer_address_id (FK), type
```

### Organization aus Context auslesen

```php
$employee = $context->getCustomer()?->getExtension(SalesChannelContextFactoryDecorator::CUSTOMER_EMPLOYEE_EXTENSION);
if ($employee instanceof EmployeeEntity) {
    $organizationId = $employee->get('organizationId');
}
```

### Store API Endpoints

```http
POST /store-api/organization-unit           # Anlegen
POST /store-api/organization-unit/{id}      # Aktualisieren
GET|POST /store-api/organization-unit/{id}  # Einzeln laden
GET|POST /store-api/organization-units      # Liste laden
DELETE /store-api/organization-unit         # Loeschen (ids: array)
```

### Organization Entity erweitern

Organization Entity ist eine Attribute Entity (kein klassisches EntityDefinition).
Entity-Name: `b2b_components_organization`

```php
class OrganizationExtension extends EntityExtension
{
    public function extendFields(FieldCollection $collection): void
    {
        $collection->add(
            (new OneToManyAssociationField('yourEntities', YourEntityDefinition::class, 'organization_id'))
                ->addFlags(new CascadeDelete())
        );
    }

    public function getEntityName(): string
    {
        return 'b2b_components_organization';
    }
}
```

Services: `b2b_components_organization.definition`, `b2b_components_organization.repository`

## Subscription-Integration

B2B Employees koennen Abonnements erstellen und verwalten. Die Integration nutzt
Decorator-Pattern und Event-Subscriber ohne Core-Modifikation.

### Berechtigungen fuer Subscription-Zugriff

| Permission                              | Zugriff                              |
|-----------------------------------------|--------------------------------------|
| `subscription.read.all`                 | Alle Abonnements sehen               |
| `organization_unit.subscription.read`   | Eigene + Abteilungs-Abonnements      |
| (keine)                                 | Nur eigene Abonnements               |

### Tracking

Tabelle `b2b_components_subscription_employee` verknuepft Subscription mit erstellendem Employee.

### Kernartefakte

- `SubscriptionRouteDecorator` — permission-basiertes Filtern
- `SalesChannelContextServiceDecorator` — Employee-Context in Subscription-Kontexten
- `SubscriptionTransformedSubscriber` — Employee-Daten beim Erstellen hinzufuegen
- `SubscriptionCartConvertedSubscriber` — Employee-Daten in Erstbestellung
- `SubscriptionOrderPlacedSubscriber` — Employee-Context in Folgebestellungen
- `SubscriptionExtension` + `SubscriptionEmployeeDefinition` — Entity-Extension

### Employee aus Subscription laden

```php
$criteria = new Criteria();
$criteria->addAssociation('subscriptionEmployee.employee');
$subscription = $subscriptionRepository->search($criteria, $context)->first();
$employee = $subscription->getSubscriptionEmployee()->getEmployee();
```
