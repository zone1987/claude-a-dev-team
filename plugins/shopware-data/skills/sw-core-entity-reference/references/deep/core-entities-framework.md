# Shopware 6 Core Entities — Framework

> Auto-generated from `src/` — 36 definitions


## Framework/App

### `app` [E]

**Class:** `AppDefinition` | **Entity:** `AppEntity` | **Collection:** `AppCollection`

**Defaults:** `active=false`, `configurable=false`, `allowDisable=true`, `modules="["`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | Required |
| `path` | `path` | StringField | Required |
| `author` | `author` | StringField |  |
| `copyright` | `copyright` | StringField |  |
| `license` | `license` | StringField |  |
| `active` | `active` | BoolField | Required |
| `configurable` | `configurable` | BoolField | Required |
| `privacy` | `privacy` | StringField |  |
| `version` | `version` | StringField | Required |
| `iconRaw` | `icon` | BlobField |  |
| `icon` | `icon` | StringField | WriteProtected |
| `appSecret` | `app_secret` | StringField | WriteProtected |
| `modules` | `modules` | ListField |  |
| `mainModule` | `main_module` | JsonField |  |
| `cookies` | `cookies` | ListField |  |
| `allowDisable` | `allow_disable` | BoolField | Required |
| `baseAppUrl` | `base_app_url` | StringField |  |
| `allowedHosts` | `allowed_hosts` | ListField |  |
| `templateLoadPriority` | `template_load_priority` | IntField |  |
| `checkoutGatewayUrl` | `checkout_gateway_url` | StringField |  |
| `contextGatewayUrl` | `context_gateway_url` | StringField |  |
| `inAppPurchasesGatewayUrl` | `in_app_purchases_gateway_url` | StringField |  |
| `sourceType` | `source_type` | StringField |  |
| `sourceConfig` | `source_config` | JsonField |  |
| `selfManaged` | `self_managed` | BoolField |  |
| `requestedPrivileges` | `requested_privileges` | ListField | Required |
| `label` | `` | TranslatedField |  |
| `description` | `` | TranslatedField |  |
| `privacyPolicyExtensions` | `` | TranslatedField |  |
| `customFields` | `` | TranslatedField | Since |
| `integrationId` | `integration_id` | FkField | Required |
| `aclRoleId` | `acl_role_id` | FkField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `AppTranslationDefinition::class` | OneToMany | `AppTranslationDefinition` |
| `integration` | OneToOne | `IntegrationDefinition` |
| `aclRole` | OneToOne | `AclRoleDefinition` |
| `customFieldSets` | OneToMany | `CustomFieldSetDefinition` |
| `actionButtons` | OneToMany | `ActionButtonDefinition` |
| `templates` | OneToMany | `TemplateDefinition` |
| `scripts` | OneToMany | `ScriptDefinition` |
| `webhooks` | OneToMany | `WebhookDefinition` |
| `paymentMethods` | OneToMany | `AppPaymentMethodDefinition` |
| `taxProviders` | OneToMany | `TaxProviderDefinition` |
| `scriptConditions` | OneToMany | `AppScriptConditionDefinition` |
| `cmsBlocks` | OneToMany | `AppCmsBlockDefinition` |
| `flowActions` | OneToMany | `AppFlowActionDefinition` |
| `flowEvents` | OneToMany | `AppFlowEventDefinition` |
| `appShippingMethods` | OneToMany | `AppShippingMethodDefinition` |
| `mcpTools` | OneToMany | `AppMcpToolDefinition` |
| `mcpPrompts` | OneToMany | `AppMcpPromptDefinition` |
| `mcpResources` | OneToMany | `AppMcpResourceDefinition` |

**Translated fields:** `label`, `description`, `privacyPolicyExtensions`, `customFields`

### `app_action_button` [E]

**Class:** `ActionButtonDefinition` | **Entity:** `ActionButtonEntity` | **Collection:** `ActionButtonCollection` | **Parent:** `AppDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `entity` | `entity` | StringField | Required |
| `view` | `view` | StringField | Required |
| `url` | `url` | StringField | Required |
| `action` | `action` | StringField | Required |
| `label` | `` | TranslatedField |  |
| `appId` | `app_id` | FkField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `ActionButtonTranslationDefinition::class` | OneToMany | `ActionButtonTranslationDefinition` |
| `app` | ManyToOne | `AppDefinition` |

**Translated fields:** `label`

### `app_action_button_translation` [T]

**Class:** `ActionButtonTranslationDefinition` | **Entity:** `ActionButtonTranslationEntity` | **Collection:** `ActionButtonTranslationCollection` | **Parent:** `ActionButtonDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `label` | `label` | StringField | Required |

### `app_cms_block` [E]

**Class:** `AppCmsBlockDefinition` | **Entity:** `AppCmsBlockEntity` | **Collection:** `AppCmsBlockCollection` | **Parent:** `AppDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | Required |
| `block` | `block` | JsonField | Required |
| `template` | `template` | LongTextField | Required |
| `styles` | `styles` | LongTextField | Required |
| `label` | `` | TranslatedField |  |
| `appId` | `app_id` | FkField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `AppCmsBlockTranslationDefinition::class` | OneToMany | `AppCmsBlockTranslationDefinition` |
| `app` | ManyToOne | `AppDefinition` |

**Translated fields:** `label`

### `app_cms_block_translation` [T]

**Class:** `AppCmsBlockTranslationDefinition` | **Entity:** `AppCmsBlockTranslationEntity` | **Collection:** `AppCmsBlockTranslationCollection` | **Parent:** `AppCmsBlockDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `label` | `label` | StringField | Required |

### `app_flow_action` [E]

**Class:** `AppFlowActionDefinition` | **Entity:** `AppFlowActionEntity` | **Collection:** `AppFlowActionCollection` | **Parent:** `AppDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `appId` | `app_id` | FkField | Required |
| `name` | `name` | StringField | Required |
| `badge` | `badge` | StringField |  |
| `parameters` | `parameters` | JsonField |  |
| `config` | `config` | JsonField |  |
| `headers` | `headers` | JsonField |  |
| `requirements` | `requirements` | ListField |  |
| `iconRaw` | `icon` | BlobField |  |
| `icon` | `icon` | StringField | WriteProtected |
| `swIcon` | `sw_icon` | StringField |  |
| `url` | `url` | StringField | Required |
| `delayable` | `delayable` | BoolField |  |
| `label` | `` | TranslatedField |  |
| `description` | `` | TranslatedField |  |
| `headline` | `` | TranslatedField |  |
| `customFields` | `` | TranslatedField |  |

| Association | Type | Target |
|-------------|------|--------|
| `AppFlowActionTranslationDefinition::class` | OneToMany | `AppFlowActionTranslationDefinition` |
| `app` | ManyToOne | `AppDefinition` |
| `flowSequences` | OneToMany | `FlowSequenceDefinition` |

**Translated fields:** `label`, `description`, `headline`, `customFields`

### `app_flow_action_translation` [T]

**Class:** `AppFlowActionTranslationDefinition` | **Entity:** `AppFlowActionTranslationEntity` | **Collection:** `AppFlowActionTranslationCollection` | **Parent:** `AppFlowActionDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `label` | `label` | StringField | Required |
| `description` | `description` | LongTextField |  |
| `headline` | `headline` | StringField |  |
| `` | `` | CustomFields |  |

### `app_flow_event` [E]

**Class:** `AppFlowEventDefinition` | **Entity:** `AppFlowEventEntity` | **Collection:** `AppFlowEventCollection` | **Parent:** `AppDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `appId` | `app_id` | FkField | Required |
| `name` | `name` | StringField | Required |
| `aware` | `aware` | ListField | Required |
| `` | `` | CustomFields |  |

| Association | Type | Target |
|-------------|------|--------|
| `app` | ManyToOne | `AppDefinition` |
| `flows` | OneToMany | `FlowDefinition` |

### `app_mcp_prompt` [E]

**Class:** `AppMcpPromptDefinition` | **Entity:** `AppMcpPromptEntity` | **Collection:** `AppMcpPromptCollection` | **Parent:** `AppDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | Required |
| `url` | `url` | StringField | Required |
| `appId` | `app_id` | FkField | Required |
| `label` | `` | TranslatedField |  |
| `description` | `` | TranslatedField |  |

| Association | Type | Target |
|-------------|------|--------|
| `app` | ManyToOne | `AppDefinition` |
| `AppMcpPromptTranslationDefinition::class` | OneToMany | `AppMcpPromptTranslationDefinition` |

**Translated fields:** `label`, `description`

### `app_mcp_prompt_translation` [T]

**Class:** `AppMcpPromptTranslationDefinition` | **Entity:** `AppMcpPromptTranslationEntity` | **Collection:** `AppMcpPromptTranslationCollection` | **Parent:** `AppMcpPromptDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `label` | `label` | StringField | Required |
| `description` | `description` | LongTextField |  |

### `app_mcp_resource` [E]

**Class:** `AppMcpResourceDefinition` | **Entity:** `AppMcpResourceEntity` | **Collection:** `AppMcpResourceCollection` | **Parent:** `AppDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | Required |
| `uri` | `uri` | StringField | Required |
| `url` | `url` | StringField | Required |
| `mimeType` | `mime_type` | StringField |  |
| `appId` | `app_id` | FkField | Required |
| `label` | `` | TranslatedField |  |
| `description` | `` | TranslatedField |  |

| Association | Type | Target |
|-------------|------|--------|
| `app` | ManyToOne | `AppDefinition` |
| `AppMcpResourceTranslationDefinition::class` | OneToMany | `AppMcpResourceTranslationDefinition` |

**Translated fields:** `label`, `description`

### `app_mcp_resource_translation` [T]

**Class:** `AppMcpResourceTranslationDefinition` | **Entity:** `AppMcpResourceTranslationEntity` | **Collection:** `AppMcpResourceTranslationCollection` | **Parent:** `AppMcpResourceDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `label` | `label` | StringField | Required |
| `description` | `description` | LongTextField |  |

### `app_mcp_tool` [E]

**Class:** `AppMcpToolDefinition` | **Entity:** `AppMcpToolEntity` | **Collection:** `AppMcpToolCollection` | **Parent:** `AppDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | Required |
| `url` | `url` | StringField | Required |
| `inputSchema` | `input_schema` | JsonField |  |
| `requiredPrivileges` | `required_privileges` | JsonField |  |
| `appId` | `app_id` | FkField | Required |
| `label` | `` | TranslatedField |  |
| `description` | `` | TranslatedField |  |

| Association | Type | Target |
|-------------|------|--------|
| `app` | ManyToOne | `AppDefinition` |
| `AppMcpToolTranslationDefinition::class` | OneToMany | `AppMcpToolTranslationDefinition` |

**Translated fields:** `label`, `description`

### `app_mcp_tool_translation` [T]

**Class:** `AppMcpToolTranslationDefinition` | **Entity:** `AppMcpToolTranslationEntity` | **Collection:** `AppMcpToolTranslationCollection` | **Parent:** `AppMcpToolDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `label` | `label` | StringField | Required |
| `description` | `description` | LongTextField |  |

### `app_payment_method` [E]

**Class:** `AppPaymentMethodDefinition` | **Entity:** `AppPaymentMethodEntity` | **Collection:** `AppPaymentMethodCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `appName` | `app_name` | StringField | Required |
| `identifier` | `identifier` | StringField | Required |
| `payUrl` | `pay_url` | StringField |  |
| `finalizeUrl` | `finalize_url` | StringField |  |
| `validateUrl` | `validate_url` | StringField |  |
| `captureUrl` | `capture_url` | StringField |  |
| `refundUrl` | `refund_url` | StringField |  |
| `recurringUrl` | `recurring_url` | StringField |  |
| `appId` | `app_id` | FkField |  |
| `originalMediaId` | `original_media_id` | FkField |  |
| `paymentMethodId` | `payment_method_id` | FkField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `app` | ManyToOne | `AppDefinition` |
| `originalMedia` | ManyToOne | `MediaDefinition` |
| `paymentMethod` | OneToOne | `PaymentMethodDefinition` |

### `app_script_condition` [E]

**Class:** `AppScriptConditionDefinition` | **Entity:** `AppScriptConditionEntity` | **Collection:** `AppScriptConditionCollection` | **Parent:** `AppDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `identifier` | `identifier` | StringField | Required |
| `name` | `` | TranslatedField |  |
| `active` | `active` | BoolField | Required |
| `group` | `group` | StringField |  |
| `script` | `script` | LongTextField | AllowHtml |
| `constraints` | `constraints` | BlobField | WriteProtected |
| `config` | `config` | JsonField |  |
| `appId` | `app_id` | FkField | CascadeDelete |

| Association | Type | Target |
|-------------|------|--------|
| `app` | ManyToOne | `AppDefinition` |
| `ruleConditions` | OneToMany | `RuleConditionDefinition` |
| `AppScriptConditionTranslationDefinition::class` | OneToMany | `AppScriptConditionTranslationDefinition` |

**Translated fields:** `name`

### `app_script_condition_translation` [T]

**Class:** `AppScriptConditionTranslationDefinition` | **Entity:** `AppScriptConditionTranslationEntity` | **Collection:** `AppScriptConditionTranslationCollection` | **Parent:** `AppScriptConditionDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |

### `app_shipping_method` [E]

**Class:** `AppShippingMethodDefinition` | **Entity:** `AppShippingMethodEntity`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `appName` | `app_name` | StringField | Required |
| `identifier` | `identifier` | StringField | Required |
| `appId` | `app_id` | FkField |  |
| `shippingMethodId` | `shipping_method_id` | FkField | Required |
| `originalMediaId` | `original_media_id` | FkField |  |

| Association | Type | Target |
|-------------|------|--------|
| `app` | ManyToOne | `AppDefinition` |
| `shippingMethod` | OneToOne | `ShippingMethodDefinition` |
| `originalMedia` | ManyToOne | `MediaDefinition` |

### `app_template` [E]

**Class:** `TemplateDefinition` | **Entity:** `TemplateEntity` | **Collection:** `TemplateCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `template` | `template` | LongTextField | Required |
| `path` | `path` | StringField | Required |
| `active` | `active` | BoolField | Required |
| `appId` | `app_id` | FkField | Required |
| `hash` | `hash` | StringField |  |

| Association | Type | Target |
|-------------|------|--------|
| `app` | ManyToOne | `AppDefinition` |

### `app_translation` [T]

**Class:** `AppTranslationDefinition` | **Entity:** `AppTranslationEntity` | **Collection:** `AppTranslationCollection` | **Parent:** `AppDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `label` | `label` | StringField | Required |
| `description` | `description` | LongTextField |  |
| `privacyPolicyExtensions` | `privacy_policy_extensions` | LongTextField |  |
| `` | `` | CustomFields | Since |


## Framework/DAL

### `attribute_entity` [E]

**Class:** `AttributeEntityDefinition`

### `attribute_mapping` [M]

**Class:** `AttributeMappingDefinition`

### `attribute_translation` [T]

**Class:** `AttributeTranslationDefinition`

### `entity` [E]

**Class:** `EntityDefinition` | **Entity:** `ArrayEntity` | **Collection:** `EntityCollection`

### `entity_translation` [E]

**Class:** `EntityTranslationDefinition`

### `mapping_entity` [E]

**Class:** `MappingEntityDefinition`

### `version` [E]

**Class:** `VersionDefinition` | **Entity:** `VersionEntity` | **Collection:** `VersionCollection`

**Defaults:** `name="\\sprintf('Draft %s'"`, `createdAt="$dateTime"`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `commits` | OneToMany | `VersionCommitDefinition` |

### `version_commit` [E]

**Class:** `VersionCommitDefinition` | **Entity:** `VersionCommitEntity` | **Collection:** `VersionCommitCollection` | **Parent:** `VersionDefinition`

**Defaults:** `name="auto-save"`, `createdAt="Clock::get()->now()->format(Defaults::STORAGE_DATE_TIME_FORMAT)"`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `versionId` | `version_id` | FkField | Required |
| `userId` | `user_id` | IdField |  |
| `integrationId` | `integration_id` | IdField |  |
| `` | `` | AutoIncrementField |  |
| `isMerge` | `is_merge` | BoolField |  |
| `message` | `message` | StringField | SearchRanking |

| Association | Type | Target |
|-------------|------|--------|
| `data` | OneToMany | `VersionCommitDataDefinition` |
| `version` | ManyToOne | `VersionDefinition` |

### `version_commit_data` [E]

**Class:** `VersionCommitDataDefinition` | **Entity:** `VersionCommitDataEntity` | **Collection:** `VersionCommitDataCollection` | **Parent:** `VersionCommitDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `versionCommitId` | `version_commit_id` | FkField | Required |
| `userId` | `user_id` | IdField |  |
| `integrationId` | `integration_id` | IdField |  |
| `` | `` | AutoIncrementField |  |
| `entityName` | `entity_name` | StringField | Required |
| `entityId` | `entity_id` | JsonField | Required |
| `action` | `action` | StringField | Required |
| `payload` | `payload` | VersionDataPayloadField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `commit` | ManyToOne | `VersionCommitDefinition` |


## Framework/Event

### `business_event` [E]

**Class:** `BusinessEventDefinition`


## Framework/Log

### `log_entry` [E]

**Class:** `LogEntryDefinition` | **Entity:** `LogEntryEntity` | **Collection:** `LogEntryCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `message` | `message` | LongTextField | SearchRanking |
| `level` | `level` | IntField |  |
| `channel` | `channel` | StringField |  |
| `context` | `context` | JsonField | SearchRanking |
| `extra` | `extra` | JsonField | SearchRanking |


## Framework/MessageQueue

### `scheduled_task` [E]

**Class:** `ScheduledTaskDefinition` | **Entity:** `ScheduledTaskEntity` | **Collection:** `ScheduledTaskCollection`

**Defaults:** `nextExecutionTime="Clock::get()->now()"`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | Required |
| `scheduledTaskClass` | `scheduled_task_class` | StringField | Required |
| `runInterval` | `run_interval` | IntField | Required |
| `defaultRunInterval` | `default_run_interval` | IntField | Required |
| `status` | `status` | StringField | Required |
| `lastExecutionTime` | `last_execution_time` | DateTimeField |  |
| `nextExecutionTime` | `next_execution_time` | DateTimeField | Required |


## Framework/Plugin

### `plugin` [E]

**Class:** `PluginDefinition` | **Entity:** `PluginEntity` | **Collection:** `PluginCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `baseClass` | `base_class` | StringField | Required |
| `name` | `name` | StringField | Required |
| `composerName` | `composer_name` | StringField |  |
| `autoload` | `autoload` | JsonField | Required |
| `active` | `active` | BoolField |  |
| `managedByComposer` | `managed_by_composer` | BoolField |  |
| `path` | `path` | StringField |  |
| `author` | `author` | StringField |  |
| `copyright` | `copyright` | StringField |  |
| `license` | `license` | StringField |  |
| `version` | `version` | StringField | Required |
| `upgradeVersion` | `upgrade_version` | StringField |  |
| `installedAt` | `installed_at` | DateTimeField |  |
| `upgradedAt` | `upgraded_at` | DateTimeField |  |
| `iconRaw` | `icon` | BlobField |  |
| `icon` | `icon` | StringField | WriteProtected |
| `label` | `` | TranslatedField |  |
| `description` | `` | TranslatedField |  |
| `manufacturerLink` | `` | TranslatedField |  |
| `supportLink` | `` | TranslatedField |  |
| `customFields` | `` | TranslatedField |  |

| Association | Type | Target |
|-------------|------|--------|
| `PluginTranslationDefinition::class` | OneToMany | `PluginTranslationDefinition` |
| `paymentMethods` | OneToMany | `PaymentMethodDefinition` |

**Translated fields:** `label`, `description`, `manufacturerLink`, `supportLink`, `customFields`

### `plugin_translation` [T]

**Class:** `PluginTranslationDefinition` | **Entity:** `PluginTranslationEntity` | **Collection:** `PluginTranslationCollection` | **Parent:** `PluginDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `label` | `label` | StringField | Required |
| `description` | `description` | LongTextField | AllowHtml |
| `manufacturerLink` | `manufacturer_link` | StringField |  |
| `supportLink` | `support_link` | StringField |  |
| `` | `` | CustomFields |  |


## Framework/Webhook

### `webhook` [E]

**Class:** `WebhookDefinition` | **Entity:** `WebhookEntity` | **Collection:** `WebhookCollection`

**Defaults:** `active=true`, `errorCount=0`, `onlyLiveVersion=false`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | Required |
| `eventName` | `event_name` | StringField | Required |
| `url` | `url` | StringField | Required |
| `onlyLiveVersion` | `only_live_version` | BoolField |  |
| `errorCount` | `error_count` | IntField | Required |
| `active` | `active` | BoolField |  |
| `appId` | `app_id` | FkField |  |

| Association | Type | Target |
|-------------|------|--------|
| `app` | ManyToOne | `AppDefinition` |

### `webhook_event_log` [E]

**Class:** `WebhookEventLogDefinition` | **Entity:** `WebhookEventLogEntity` | **Collection:** `WebhookEventLogCollection`

**Defaults:** `onlyLiveVersion=false`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `appName` | `app_name` | StringField |  |
| `webhookName` | `webhook_name` | StringField | Required |
| `eventName` | `event_name` | StringField | Required |
| `deliveryStatus` | `delivery_status` | StringField | Required |
| `timestamp` | `timestamp` | IntField |  |
| `processingTime` | `processing_time` | IntField |  |
| `appVersion` | `app_version` | StringField |  |
| `requestContent` | `request_content` | JsonField |  |
| `responseContent` | `response_content` | JsonField |  |
| `responseStatusCode` | `response_status_code` | IntField |  |
| `responseReasonPhrase` | `response_reason_phrase` | StringField |  |
| `url` | `url` | StringField | Required |
| `onlyLiveVersion` | `only_live_version` | BoolField |  |
| `serializedWebhookMessage` | `serialized_webhook_message` | BlobField | Required |
| `` | `` | CustomFields |  |
| `sequence` | `sequence` | IntField | WriteProtected |
