# B2B Employee Management — Developer reference

## Contents

- [Core concept](#core-concept)
- [Database schema](#database-schema)
- [Creating / inviting employees](#creating--inviting-employees)
- [Permission system](#permission-system)
- [Route Restriction (Denylist)](#route-restriction-denylist)
- [Organization Unit](#organization-unit)
- [Subscription integration](#subscription-integration)

## Core concept

Employee Management enables B2B merchants to build a buyer platform for business
partners. Employees are separate logins within a company customer
(business partner) and act on behalf of the company.

**Core entities:**
- **Business Partner** (`swag_b2b_business_partner`): extension of a regular storefront customer
- **Employee** (`swag_b2b_employee`): separate login instance with its own password and role
- **Role** (`swag_b2b_role`): permission set assigned to an employee

## Database schema

```sql
swag_b2b_business_partner:
  id, customer_id (FK), default_role_id (FK), custom_fields

swag_b2b_employee:
  id, business_partner_customer_id (FK), role_id (FK), active,
  first_name, last_name, email, password, recovery_time, recovery_hash

swag_b2b_role:
  id, business_partner_customer_id (FK), name, permissions (JSON)
```

Employees are unique by email. Uniqueness is checked when inviting.

## Creating / inviting employees

### Via storefront
The business partner navigates to `/account` → employee page → add new employee.

### Via Store API
`POST /store-api/employee/create` (as a logged-in customer).

### Via Administration
The merchant selects the business partner customer → "Company" tab → add employee.

**Invitation URL (default):** `/account/business-partner/employee/invite/%%RECOVERHASH%%`

**Customize the URL via system config:**
```php
// Key: b2b.employee.invitationURL
```

## Permission system

Roles contain a list of permissions as JSON. The business partner defines a
default role that is preselected when creating new employees.

### Custom permissions via plugin

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

Twig check: `{% if isB2bAllowed(constant('...::OWN_ENTITY_READ')) %}`

PHP check: `$context->getCustomer()->getEmployee()->getRole()->can('own_entity.read')`

### Custom permissions via app

Via Store API `POST /store-api/permission` with a permission name (must be unique).
Snippet key: `b2b.role-edit.permissions.[name]`, e.g. `b2b.role-edit.permissions.order.delete`.

## Route Restriction (Denylist)

Employees share the customer account with the business partner. To prevent
unauthorized data changes, there is a denylist:

Configuration: `Resources/config/employee_route_access.xml`

```xml
<routes>
    <denied>store-api.account.change-profile</denied>
    <denied>store-api.account.change-email</denied>
    <allowed>store-api.account.login</allowed>
</routes>
```

The `B2bRouteBlocker` subscriber checks routes before the controller is reached.

### Extending the denylist (decoration)

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

Enables differentiated access rights within complex company structures.
Requires Employee Management.

### Entities

```sql
b2b_components_organization:
  id, name, customer_id (FK), default_shipping_address_id (FK),
  default_billing_address_id (FK), custom_fields

b2b_components_organization_customer_address:
  id, organization_id (FK), customer_address_id (FK), type
```

### Reading the organization from the context

```php
$employee = $context->getCustomer()?->getExtension(SalesChannelContextFactoryDecorator::CUSTOMER_EMPLOYEE_EXTENSION);
if ($employee instanceof EmployeeEntity) {
    $organizationId = $employee->get('organizationId');
}
```

### Store API endpoints

```http
POST /store-api/organization-unit           # Create
POST /store-api/organization-unit/{id}      # Update
GET|POST /store-api/organization-unit/{id}  # Load single
GET|POST /store-api/organization-units      # Load list
DELETE /store-api/organization-unit         # Delete (ids: array)
```

### Extending the Organization entity

The Organization entity is an attribute entity (not a classic EntityDefinition).
Entity name: `b2b_components_organization`

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

## Subscription integration

B2B employees can create and manage subscriptions. The integration uses the
decorator pattern and event subscribers without core modification.

### Permissions for subscription access

| Permission                              | Access                               |
|-----------------------------------------|--------------------------------------|
| `subscription.read.all`                 | See all subscriptions                |
| `organization_unit.subscription.read`   | Own + department subscriptions       |
| (none)                                  | Only own subscriptions               |

### Tracking

The table `b2b_components_subscription_employee` links a subscription to the creating employee.

### Core artifacts

- `SubscriptionRouteDecorator` — permission-based filtering
- `SalesChannelContextServiceDecorator` — employee context in subscription contexts
- `SubscriptionTransformedSubscriber` — add employee data on creation
- `SubscriptionCartConvertedSubscriber` — employee data in the initial order
- `SubscriptionOrderPlacedSubscriber` — employee context in follow-up orders
- `SubscriptionExtension` + `SubscriptionEmployeeDefinition` — entity extension

### Loading the employee from a subscription

```php
$criteria = new Criteria();
$criteria->addAssociation('subscriptionEmployee.employee');
$subscription = $subscriptionRepository->search($criteria, $context)->first();
$employee = $subscription->getSubscriptionEmployee()->getEmployee();
```
