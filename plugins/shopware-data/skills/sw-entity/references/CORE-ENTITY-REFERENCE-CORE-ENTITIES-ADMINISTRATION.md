# Shopware 6 Core Entities — Administration

> Auto-generated from `src/` — 2 definitions


## Administration

### `app_administration_snippet` [E]

**Class:** `AppAdministrationSnippetDefinition` | **Entity:** `AppAdministrationSnippetEntity` | **Collection:** `AppAdministrationSnippetCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `value` | `value` | LongTextField | ApiAware |
| `appId` | `app_id` | FkField | ApiAware |
| `localeId` | `locale_id` | FkField | ApiAware |

### `notification` [E]

**Class:** `NotificationDefinition` | **Entity:** `NotificationEntity` | **Collection:** `NotificationCollection`

**Defaults:** `requiredPrivileges="["`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `status` | `status` | StringField | Required |
| `message` | `message` | LongTextField | Required |
| `adminOnly` | `admin_only` | BoolField |  |
| `requiredPrivileges` | `required_privileges` | ListField |  |
| `createdByIntegrationId` | `created_by_integration_id` | FkField |  |
| `createdByUserId` | `created_by_user_id` | FkField |  |

| Association | Type | Target |
|-------------|------|--------|
| `createdByIntegration` | ManyToOne | `IntegrationDefinition` |
| `createdByUser` | ManyToOne | `UserDefinition` |
