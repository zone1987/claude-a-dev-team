# Shopware 6 Core Entities — System

> Auto-generated from `src/` — 64 definitions


## System/Country

### `country` [E]

**Class:** `CountryDefinition` | **Entity:** `CountryEntity` | **Collection:** `CountryCollection`

**Defaults:** `vatIdRequired=false`, `postalCodeRequired=false`, `checkPostalCodePattern=false`, `checkAdvancedPostalCodePattern=false`, `customerTax="$defaultTax"`, `companyTax="$defaultTax"`, `isEu=false`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `iso` | `iso` | StringField | ApiAware |
| `position` | `position` | IntField | ApiAware |
| `active` | `active` | BoolField | ApiAware |
| `shippingAvailable` | `shipping_available` | BoolField | ApiAware |
| `iso3` | `iso3` | StringField | ApiAware |
| `displayStateInRegistration` | `display_state_in_registration` | BoolField | ApiAware |
| `forceStateInRegistration` | `force_state_in_registration` | BoolField | ApiAware |
| `checkVatIdPattern` | `check_vat_id_pattern` | BoolField | ApiAware |
| `vatIdRequired` | `vat_id_required` | BoolField | ApiAware |
| `vatIdPattern` | `vat_id_pattern` | StringField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |
| `customerTax` | `customer_tax` | TaxFreeConfigField | ApiAware |
| `companyTax` | `company_tax` | TaxFreeConfigField | ApiAware |
| `postalCodeRequired` | `postal_code_required` | BoolField | ApiAware |
| `checkPostalCodePattern` | `check_postal_code_pattern` | BoolField | ApiAware |
| `checkAdvancedPostalCodePattern` | `check_advanced_postal_code_pattern` | BoolField | ApiAware |
| `advancedPostalCodePattern` | `advanced_postal_code_pattern` | StringField | ApiAware |
| `addressFormat` | `` | TranslatedField | ApiAware |
| `defaultPostalCodePattern` | `default_postal_code_pattern` | StringField | ApiAware |
| `isEu` | `is_eu` | BoolField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `states` | OneToMany | `CountryStateDefinition` |
| `CountryTranslationDefinition::class` | OneToMany | `CountryTranslationDefinition` |
| `customerAddresses` | OneToMany | `CustomerAddressDefinition` |
| `orderAddresses` | OneToMany | `OrderAddressDefinition` |
| `salesChannelDefaultAssignments` | OneToMany | `SalesChannelDefinition` |
| `salesChannels` | ManyToMany | `SalesChannelDefinition` |
| `taxRules` | OneToMany | `TaxRuleDefinition` |
| `currencyCountryRoundings` | OneToMany | `CurrencyCountryRoundingDefinition` |

**Translated fields:** `name`, `customFields`, `addressFormat`

### `country_state` [E]

**Class:** `CountryStateDefinition` | **Entity:** `CountryStateEntity` | **Collection:** `CountryStateCollection` | **Parent:** `CountryDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `countryId` | `country_id` | FkField | ApiAware |
| `shortCode` | `short_code` | StringField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `position` | `position` | IntField | ApiAware |
| `active` | `active` | BoolField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `country` | ManyToOne | `CountryDefinition` |
| `CountryStateTranslationDefinition::class` | OneToMany | `CountryStateTranslationDefinition` |
| `customerAddresses` | OneToMany | `CustomerAddressDefinition` |
| `orderAddresses` | OneToMany | `OrderAddressDefinition` |

**Translated fields:** `name`, `customFields`

### `country_state_translation` [T]

**Class:** `CountryStateTranslationDefinition` | **Entity:** `CountryStateTranslationEntity` | **Collection:** `CountryStateTranslationCollection` | **Parent:** `CountryStateDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |
| `` | `` | CustomFields | ApiAware |

### `country_translation` [T]

**Class:** `CountryTranslationDefinition` | **Entity:** `CountryTranslationEntity` | **Collection:** `CountryTranslationCollection` | **Parent:** `CountryDefinition`

**Defaults:** `addressFormat="CountryDefinition::DEFAULT_ADDRESS_FORMAT"`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |
| `addressFormat` | `address_format` | JsonField | ApiAware |
| `` | `` | CustomFields | ApiAware |

### `sales_channel_country` [E]

**Class:** `SalesChannelCountryDefinition`

### `sales_channel_country_state` [E]

**Class:** `SalesChannelCountryStateDefinition`


## System/Currency

### `currency` [E]

**Class:** `CurrencyDefinition` | **Entity:** `CurrencyEntity` | **Collection:** `CurrencyCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `factor` | `factor` | FloatField | ApiAware |
| `symbol` | `symbol` | StringField | ApiAware |
| `isoCode` | `iso_code` | StringField | ApiAware |
| `shortName` | `` | TranslatedField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `position` | `position` | IntField | ApiAware |
| `isSystemDefault` | `is_system_default` | BoolField | ApiAware |
| `taxFreeFrom` | `tax_free_from` | FloatField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |
| `itemRounding` | `item_rounding` | CashRoundingConfigField | ApiAware |
| `totalRounding` | `total_rounding` | CashRoundingConfigField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `CurrencyTranslationDefinition::class` | OneToMany | `CurrencyTranslationDefinition` |
| `salesChannelDefaultAssignments` | OneToMany | `SalesChannelDefinition` |
| `orders` | OneToMany | `OrderDefinition` |
| `salesChannels` | ManyToMany | `SalesChannelDefinition` |
| `salesChannelDomains` | OneToMany | `SalesChannelDomainDefinition` |
| `promotionDiscountPrices` | OneToMany | `PromotionDiscountPriceDefinition` |
| `productExports` | OneToMany | `ProductExportDefinition` |
| `countryRoundings` | OneToMany | `CurrencyCountryRoundingDefinition` |

**Translated fields:** `shortName`, `name`, `customFields`

### `currency_country_rounding` [E]

**Class:** `CurrencyCountryRoundingDefinition` | **Entity:** `CurrencyCountryRoundingEntity` | **Collection:** `CurrencyCountryRoundingCollection` | **Parent:** `CurrencyDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `currencyId` | `currency_id` | FkField | Required |
| `countryId` | `country_id` | FkField | Required |
| `itemRounding` | `item_rounding` | CashRoundingConfigField | Required |
| `totalRounding` | `total_rounding` | CashRoundingConfigField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `currency` | ManyToOne | `CurrencyDefinition` |
| `country` | ManyToOne | `CountryDefinition` |

### `currency_translation` [T]

**Class:** `CurrencyTranslationDefinition` | **Entity:** `CurrencyTranslationEntity` | **Collection:** `CurrencyTranslationCollection` | **Parent:** `CurrencyDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `shortName` | `short_name` | StringField | ApiAware |
| `name` | `name` | StringField | ApiAware |
| `` | `` | CustomFields | ApiAware |

### `sales_channel_currency` [E]

**Class:** `SalesChannelCurrencyDefinition`


## System/CustomEntity

### `custom_entity` [E]

**Class:** `CustomEntityDefinition` | **Entity:** `CustomEntityEntity` | **Collection:** `CustomEntityCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | Required |
| `fields` | `fields` | JsonField | Required |
| `flags` | `flags` | JsonField |  |
| `appId` | `app_id` | FkField |  |
| `pluginId` | `plugin_id` | FkField |  |
| `cmsAware` | `cms_aware` | BoolField | Runtime |
| `storeApiAware` | `store_api_aware` | BoolField | Runtime |
| `customFieldsAware` | `custom_fields_aware` | BoolField |  |
| `labelProperty` | `label_property` | StringField |  |
| `deletedAt` | `deleted_at` | DateTimeField |  |

### `dynamic_entity` [E]

**Class:** `DynamicEntityDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |

### `dynamic_mapping_entity` [M]

**Class:** `DynamicMappingEntityDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `self::kebabCaseToCamelCase($this->source) . 'Id` | `$this->source . '_id` | FkField | Required |
| `self::kebabCaseToCamelCase($this->reference) . 'Id` | `$this->reference . '_id` | FkField | Required |
| `$definition->getEntityName()` | `$definition->getEntityName()` | ReferenceVersionField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `self::kebabCaseToCamelCase($this->reference)` | ManyToOne | `` |
| `self::kebabCaseToCamelCase($this->source)` | ManyToOne | `` |

### `dynamic_translation_entity` [T]

**Class:** `DynamicTranslationEntityDefinition`


## System/CustomField

### `custom_field` [E]

**Class:** `CustomFieldDefinition` | **Entity:** `CustomFieldEntity` | **Collection:** `CustomFieldCollection`

**Defaults:** `allowCustomerWrites=false`, `allowCartExpose=false`, `storeApiAware=true`, `includeInSearch=false`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | Required |
| `type` | `type` | StringField | Required |
| `config` | `config` | JsonField |  |
| `active` | `active` | BoolField |  |
| `customFieldSetId` | `set_id` | FkField |  |
| `allowCustomerWrite` | `allow_customer_write` | BoolField |  |
| `allowCartExpose` | `allow_cart_expose` | BoolField |  |
| `storeApiAware` | `store_api_aware` | BoolField |  |
| `includeInSearch` | `include_in_search` | BoolField |  |

| Association | Type | Target |
|-------------|------|--------|
| `customFieldSet` | ManyToOne | `CustomFieldSetDefinition` |
| `productSearchConfigFields` | OneToMany | `ProductSearchConfigFieldDefinition` |

### `custom_field_set` [E]

**Class:** `CustomFieldSetDefinition` | **Entity:** `CustomFieldSetEntity` | **Collection:** `CustomFieldSetCollection`

**Defaults:** `position=1`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | Required |
| `config` | `config` | JsonField |  |
| `active` | `active` | BoolField |  |
| `global` | `global` | BoolField |  |
| `position` | `position` | IntField |  |
| `appId` | `app_id` | FkField |  |

| Association | Type | Target |
|-------------|------|--------|
| `customFields` | OneToMany | `CustomFieldDefinition` |
| `relations` | OneToMany | `CustomFieldSetRelationDefinition` |
| `products` | ManyToMany | `ProductDefinition` |
| `app` | ManyToOne | `AppDefinition` |

### `custom_field_set_relation` [E]

**Class:** `CustomFieldSetRelationDefinition` | **Entity:** `CustomFieldSetRelationEntity` | **Collection:** `CustomFieldSetRelationCollection` | **Parent:** `CustomFieldSetDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `customFieldSetId` | `set_id` | FkField | Required |
| `entityName` | `entity_name` | StringField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `customFieldSet` | ManyToOne | `CustomFieldSetDefinition` |


## System/DeliveryTime

### `delivery_time` [E]

**Class:** `DeliveryTimeDefinition` | **Entity:** `DeliveryTimeEntity` | **Collection:** `DeliveryTimeCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `min` | `min` | IntField | ApiAware |
| `max` | `max` | IntField | ApiAware |
| `unit` | `unit` | StringField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `shippingMethods` | OneToMany | `ShippingMethodDefinition` |
| `products` | OneToMany | `ProductDefinition` |
| `DeliveryTimeTranslationDefinition::class` | OneToMany | `DeliveryTimeTranslationDefinition` |

**Translated fields:** `name`, `customFields`

### `delivery_time_translation` [T]

**Class:** `DeliveryTimeTranslationDefinition` | **Entity:** `DeliveryTimeTranslationEntity` | **Collection:** `DeliveryTimeTranslationCollection` | **Parent:** `DeliveryTimeDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |
| `` | `` | CustomFields | ApiAware |


## System/Integration

### `integration` [E]

**Class:** `IntegrationDefinition` | **Entity:** `IntegrationEntity` | **Collection:** `IntegrationCollection`

**Defaults:** `admin=false`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `label` | `label` | StringField | Required |
| `accessKey` | `access_key` | StringField | Required |
| `secretAccessKey` | `secret_access_key` | PasswordField | Required |
| `lastUsageAt` | `last_usage_at` | DateTimeField |  |
| `admin` | `admin` | BoolField | WriteProtected |
| `mcpAllowlist` | `mcp_allowlist` | JsonField |  |
| `` | `` | CustomFields |  |
| `deletedAt` | `deleted_at` | DateTimeField |  |

| Association | Type | Target |
|-------------|------|--------|
| `app` | OneToOne | `AppDefinition` |
| `stateMachineHistoryEntries` | OneToMany | `StateMachineHistoryDefinition` |
| `aclRoles` | ManyToMany | `AclRoleDefinition` |

### `integration_role` [M]

**Class:** `IntegrationRoleDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `integrationId` | `integration_id` | FkField | PrimaryKey |
| `aclRoleId` | `acl_role_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `integration` | ManyToOne | `IntegrationDefinition` |
| `role` | ManyToOne | `AclRoleDefinition` |


## System/Language

### `language` [E]

**Class:** `LanguageDefinition` | **Entity:** `LanguageEntity` | **Collection:** `LanguageCollection`

**Defaults:** `active=true`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `self::class` | `self::class` | ParentFkField | ApiAware |
| `localeId` | `locale_id` | FkField | ApiAware |
| `translationCodeId` | `translation_code_id` | FkField | ApiAware |
| `name` | `name` | StringField | ApiAware |
| `active` | `active` | BoolField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `self::class` | ManyToOne | `` |
| `locale` | ManyToOne | `LocaleDefinition` |
| `translationCode` | ManyToOne | `LocaleDefinition` |
| `self::class` | OneToMany | `` |
| `salesChannels` | ManyToMany | `SalesChannelDefinition` |
| `salesChannelDefaultAssignments` | OneToMany | `SalesChannelDefinition` |
| `salesChannelDomains` | OneToMany | `SalesChannelDomainDefinition` |
| `customers` | OneToMany | `CustomerDefinition` |
| `newsletterRecipients` | OneToMany | `NewsletterRecipientDefinition` |
| `orders` | OneToMany | `OrderDefinition` |
| `categoryTranslations` | OneToMany | `CategoryTranslationDefinition` |
| `countryStateTranslations` | OneToMany | `CountryStateTranslationDefinition` |
| `countryTranslations` | OneToMany | `CountryTranslationDefinition` |
| `currencyTranslations` | OneToMany | `CurrencyTranslationDefinition` |
| `customerGroupTranslations` | OneToMany | `CustomerGroupTranslationDefinition` |
| `localeTranslations` | OneToMany | `LocaleTranslationDefinition` |
| `mediaTranslations` | OneToMany | `MediaTranslationDefinition` |
| `paymentMethodTranslations` | OneToMany | `PaymentMethodTranslationDefinition` |
| `productManufacturerTranslations` | OneToMany | `ProductManufacturerTranslationDefinition` |
| `productTranslations` | OneToMany | `ProductTranslationDefinition` |
| `shippingMethodTranslations` | OneToMany | `ShippingMethodTranslationDefinition` |
| `unitTranslations` | OneToMany | `UnitTranslationDefinition` |
| `propertyGroupTranslations` | OneToMany | `PropertyGroupTranslationDefinition` |
| `propertyGroupOptionTranslations` | OneToMany | `PropertyGroupOptionTranslationDefinition` |
| `salesChannelTranslations` | OneToMany | `SalesChannelTranslationDefinition` |
| `salesChannelTypeTranslations` | OneToMany | `SalesChannelTypeTranslationDefinition` |
| `salutationTranslations` | OneToMany | `SalutationTranslationDefinition` |
| `pluginTranslations` | OneToMany | `PluginTranslationDefinition` |
| `productStreamTranslations` | OneToMany | `ProductStreamTranslationDefinition` |
| `stateMachineTranslations` | OneToMany | `StateMachineTranslationDefinition` |
| `stateMachineStateTranslations` | OneToMany | `StateMachineStateTranslationDefinition` |
| `cmsPageTranslations` | OneToMany | `CmsPageTranslationDefinition` |
| `cmsSlotTranslations` | OneToMany | `CmsSlotTranslationDefinition` |
| `mailTemplateTranslations` | OneToMany | `MailTemplateTranslationDefinition` |
| `mailHeaderFooterTranslations` | OneToMany | `MailHeaderFooterTranslationDefinition` |
| `documentTypeTranslations` | OneToMany | `DocumentTypeTranslationDefinition` |
| `numberRangeTypeTranslations` | OneToMany | `NumberRangeTypeTranslationDefinition` |
| `deliveryTimeTranslations` | OneToMany | `DeliveryTimeTranslationDefinition` |
| `productSearchKeywords` | OneToMany | `ProductSearchKeywordDefinition` |
| `productKeywordDictionaries` | OneToMany | `ProductKeywordDictionaryDefinition` |
| `mailTemplateTypeTranslations` | OneToMany | `MailTemplateTypeTranslationDefinition` |
| `promotionTranslations` | OneToMany | `PromotionTranslationDefinition` |
| `numberRangeTranslations` | OneToMany | `NumberRangeTranslationDefinition` |
| `productReviews` | OneToMany | `ProductReviewDefinition` |
| `seoUrlTranslations` | OneToMany | `SeoUrlDefinition` |
| `taxRuleTypeTranslations` | OneToMany | `TaxRuleTypeTranslationDefinition` |
| `productCrossSellingTranslations` | OneToMany | `ProductCrossSellingTranslationDefinition` |
| `importExportProfileTranslations` | OneToMany | `ImportExportProfileTranslationDefinition` |
| `productSortingTranslations` | OneToMany | `ProductSortingTranslationDefinition` |
| `productFeatureSetTranslations` | OneToMany | `ProductFeatureSetTranslationDefinition` |
| `appTranslations` | OneToMany | `AppTranslationDefinition` |
| `actionButtonTranslations` | OneToMany | `ActionButtonTranslationDefinition` |
| `landingPageTranslations` | OneToMany | `LandingPageTranslationDefinition` |
| `appCmsBlockTranslations` | OneToMany | `AppCmsBlockTranslationDefinition` |
| `appScriptConditionTranslations` | OneToMany | `AppScriptConditionTranslationDefinition` |
| `appMcpToolTranslations` | OneToMany | `AppMcpToolTranslationDefinition` |
| `appMcpPromptTranslations` | OneToMany | `AppMcpPromptTranslationDefinition` |
| `appMcpResourceTranslations` | OneToMany | `AppMcpResourceTranslationDefinition` |
| `productSearchConfig` | OneToOne | `ProductSearchConfigDefinition` |
| `appFlowActionTranslations` | OneToMany | `AppFlowActionTranslationDefinition` |
| `taxProviderTranslations` | OneToMany | `TaxProviderTranslationDefinition` |

### `sales_channel_language` [E]

**Class:** `SalesChannelLanguageDefinition`


## System/Locale

### `locale` [E]

**Class:** `LocaleDefinition` | **Entity:** `LocaleEntity` | **Collection:** `LocaleCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `code` | `code` | StringField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `territory` | `` | TranslatedField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `languages` | OneToMany | `LanguageDefinition` |
| `LocaleTranslationDefinition::class` | OneToMany | `LocaleTranslationDefinition` |
| `users` | OneToMany | `UserDefinition` |

**Translated fields:** `name`, `territory`, `customFields`

### `locale_translation` [T]

**Class:** `LocaleTranslationDefinition` | **Entity:** `LocaleTranslationEntity` | **Collection:** `LocaleTranslationCollection` | **Parent:** `LocaleDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |
| `territory` | `territory` | StringField | ApiAware |
| `` | `` | CustomFields | ApiAware |


## System/NumberRange

### `number_range` [E]

**Class:** `NumberRangeDefinition` | **Entity:** `NumberRangeEntity` | **Collection:** `NumberRangeCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `typeId` | `type_id` | FkField | Required |
| `global` | `global` | BoolField | Required |
| `name` | `` | TranslatedField |  |
| `description` | `` | TranslatedField |  |
| `pattern` | `pattern` | StringField | Required |
| `start` | `start` | IntField | Required |
| `customFields` | `` | TranslatedField |  |

| Association | Type | Target |
|-------------|------|--------|
| `type` | ManyToOne | `NumberRangeTypeDefinition` |
| `numberRangeSalesChannels` | OneToMany | `NumberRangeSalesChannelDefinition` |
| `state` | OneToOne | `NumberRangeStateDefinition` |
| `NumberRangeTranslationDefinition::class` | OneToMany | `NumberRangeTranslationDefinition` |

**Translated fields:** `name`, `description`, `customFields`

### `number_range_sales_channel` [E]

**Class:** `NumberRangeSalesChannelDefinition` | **Entity:** `NumberRangeSalesChannelEntity` | **Collection:** `NumberRangeSalesChannelCollection` | **Parent:** `NumberRangeDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `numberRangeId` | `number_range_id` | FkField | Required |
| `salesChannelId` | `sales_channel_id` | FkField | Required |
| `numberRangeTypeId` | `number_range_type_id` | FkField |  |

| Association | Type | Target |
|-------------|------|--------|
| `numberRange` | ManyToOne | `NumberRangeDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |
| `numberRangeType` | ManyToOne | `NumberRangeTypeDefinition` |

### `number_range_state` [E]

**Class:** `NumberRangeStateDefinition` | **Entity:** `NumberRangeStateEntity` | **Collection:** `NumberRangeStateCollection` | **Parent:** `NumberRangeDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | Required |
| `numberRangeId` | `number_range_id` | FkField | PrimaryKey |
| `lastValue` | `last_value` | IntField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `numberRange` | OneToOne | `NumberRangeDefinition` |

### `number_range_translation` [T]

**Class:** `NumberRangeTranslationDefinition` | **Entity:** `NumberRangeTranslationEntity` | **Collection:** `NumberRangeTranslationCollection` | **Parent:** `NumberRangeDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | Required |
| `description` | `description` | StringField |  |
| `` | `` | CustomFields |  |

### `number_range_type` [E]

**Class:** `NumberRangeTypeDefinition` | **Entity:** `NumberRangeTypeEntity` | **Collection:** `NumberRangeTypeCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `technicalName` | `technical_name` | StringField | SearchRanking |
| `typeName` | `` | TranslatedField | SearchRanking |
| `global` | `global` | BoolField | Required |
| `customFields` | `` | TranslatedField |  |

| Association | Type | Target |
|-------------|------|--------|
| `numberRanges` | OneToMany | `NumberRangeDefinition` |
| `numberRangeSalesChannels` | OneToMany | `NumberRangeSalesChannelDefinition` |
| `NumberRangeTypeTranslationDefinition::class` | OneToMany | `NumberRangeTypeTranslationDefinition` |

**Translated fields:** `typeName`, `customFields`

### `number_range_type_translation` [T]

**Class:** `NumberRangeTypeTranslationDefinition` | **Entity:** `NumberRangeTypeTranslationEntity` | **Collection:** `NumberRangeTypeTranslationCollection` | **Parent:** `NumberRangeTypeDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `typeName` | `type_name` | StringField | Required |
| `` | `` | CustomFields |  |


## System/SalesChannel

### `sales_channel` [E]

**Class:** `SalesChannelDefinition` | **Entity:** `SalesChannelEntity` | **Collection:** `SalesChannelCollection`

**Defaults:** `taxCalculationType="horizontal"`, `homeEnabled=true`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `typeId` | `type_id` | FkField | Required |
| `languageId` | `language_id` | FkField | ApiAware |
| `customerGroupId` | `customer_group_id` | FkField | ApiAware |
| `currencyId` | `currency_id` | FkField | ApiAware |
| `paymentMethodId` | `payment_method_id` | FkField | ApiAware |
| `shippingMethodId` | `shipping_method_id` | FkField | ApiAware |
| `countryId` | `country_id` | FkField | ApiAware |
| `analyticsId` | `analytics_id` | FkField |  |
| `navigationCategoryId` | `navigation_category_id` | FkField | ApiAware |
| `navigation_category_version_id` | `CategoryDefinition::class` | ReferenceVersionField | ApiAware |
| `navigationCategoryDepth` | `navigation_category_depth` | IntField | ApiAware |
| `footerCategoryId` | `footer_category_id` | FkField | ApiAware |
| `footer_category_version_id` | `CategoryDefinition::class` | ReferenceVersionField | ApiAware |
| `serviceCategoryId` | `service_category_id` | FkField | ApiAware |
| `service_category_version_id` | `CategoryDefinition::class` | ReferenceVersionField | ApiAware |
| `mailHeaderFooterId` | `mail_header_footer_id` | FkField | ApiAware |
| `hreflangDefaultDomainId` | `hreflang_default_domain_id` | FkField | ApiAware |
| `measurementUnits` | `measurement_units` | MeasurementUnitsField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `shortName` | `short_name` | StringField | ApiAware |
| `taxCalculationType` | `tax_calculation_type` | StringField | ApiAware |
| `accessKey` | `access_key` | StringField | Required |
| `configuration` | `configuration` | JsonField | ApiAware |
| `active` | `active` | BoolField | ApiAware |
| `hreflangActive` | `hreflang_active` | BoolField | ApiAware |
| `maintenance` | `maintenance` | BoolField | ApiAware |
| `maintenanceIpWhitelist` | `maintenance_ip_whitelist` | ListField |  |
| `customFields` | `` | TranslatedField | ApiAware |
| `paymentMethodIds` | `payment_method_ids` | ManyToManyIdField |  |
| `homeCmsPageId` | `home_cms_page_id` | FkField |  |
| `home_cms_page_version_id` | `CmsPageDefinition::class` | ReferenceVersionField | Required |
| `homeSlotConfig` | `` | TranslatedField |  |
| `homeEnabled` | `` | TranslatedField |  |
| `homeName` | `` | TranslatedField |  |
| `homeMetaTitle` | `` | TranslatedField |  |
| `homeMetaDescription` | `` | TranslatedField |  |
| `homeKeywords` | `` | TranslatedField |  |

| Association | Type | Target |
|-------------|------|--------|
| `SalesChannelTranslationDefinition::class` | OneToMany | `SalesChannelTranslationDefinition` |
| `currencies` | ManyToMany | `CurrencyDefinition` |
| `languages` | ManyToMany | `LanguageDefinition` |
| `countries` | ManyToMany | `CountryDefinition` |
| `paymentMethods` | ManyToMany | `PaymentMethodDefinition` |
| `shippingMethods` | ManyToMany | `ShippingMethodDefinition` |
| `type` | ManyToOne | `SalesChannelTypeDefinition` |
| `language` | ManyToOne | `LanguageDefinition` |
| `customerGroup` | ManyToOne | `CustomerGroupDefinition` |
| `currency` | ManyToOne | `CurrencyDefinition` |
| `paymentMethod` | ManyToOne | `PaymentMethodDefinition` |
| `shippingMethod` | ManyToOne | `ShippingMethodDefinition` |
| `country` | ManyToOne | `CountryDefinition` |
| `orders` | OneToMany | `OrderDefinition` |
| `customers` | OneToMany | `CustomerDefinition` |
| `homeCmsPage` | ManyToOne | `CmsPageDefinition` |
| `domains` | OneToMany | `SalesChannelDomainDefinition` |
| `systemConfigs` | OneToMany | `SystemConfigDefinition` |
| `navigationCategory` | ManyToOne | `CategoryDefinition` |
| `footerCategory` | ManyToOne | `CategoryDefinition` |
| `serviceCategory` | ManyToOne | `CategoryDefinition` |
| `productVisibilities` | OneToMany | `ProductVisibilityDefinition` |
| `hreflangDefaultDomain` | OneToOne | `SalesChannelDomainDefinition` |
| `mailHeaderFooter` | ManyToOne | `MailHeaderFooterDefinition` |
| `newsletterRecipients` | OneToMany | `NewsletterRecipientDefinition` |
| `numberRangeSalesChannels` | OneToMany | `NumberRangeSalesChannelDefinition` |
| `promotionSalesChannels` | OneToMany | `PromotionSalesChannelDefinition` |
| `documentBaseConfigSalesChannels` | OneToMany | `DocumentBaseConfigSalesChannelDefinition` |
| `productReviews` | OneToMany | `ProductReviewDefinition` |
| `seoUrls` | OneToMany | `SeoUrlDefinition` |
| `seoUrlTemplates` | OneToMany | `SeoUrlTemplateDefinition` |
| `mainCategories` | OneToMany | `MainCategoryDefinition` |
| `productExports` | OneToMany | `ProductExportDefinition` |
| `analytics` | OneToOne | `SalesChannelAnalyticsDefinition` |
| `customerGroupsRegistrations` | ManyToMany | `CustomerGroupDefinition` |
| `landingPages` | ManyToMany | `LandingPageDefinition` |
| `boundCustomers` | OneToMany | `CustomerDefinition` |
| `wishlists` | OneToMany | `CustomerWishlistDefinition` |

**Translated fields:** `name`, `customFields`, `homeSlotConfig`, `homeEnabled`, `homeName`, `homeMetaTitle`, `homeMetaDescription`, `homeKeywords`

### `sales_channel_analytics` [E]

**Class:** `SalesChannelAnalyticsDefinition` | **Entity:** `SalesChannelAnalyticsEntity` | **Collection:** `SalesChannelAnalyticsCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `trackingId` | `tracking_id` | StringField |  |
| `active` | `active` | BoolField |  |
| `trackOrders` | `track_orders` | BoolField |  |
| `anonymizeIp` | `anonymize_ip` | BoolField |  |
| `trackOffcanvasCart` | `track_offcanvas_cart` | BoolField |  |
| `enhancedConversions` | `enhanced_conversions` | BoolField |  |

| Association | Type | Target |
|-------------|------|--------|
| `salesChannel` | OneToOne | `SalesChannelDefinition` |

### `sales_channel_country` [M]

**Class:** `SalesChannelCountryDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `salesChannelId` | `sales_channel_id` | FkField | PrimaryKey |
| `countryId` | `country_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |
| `country` | ManyToOne | `CountryDefinition` |

### `sales_channel_currency` [M]

**Class:** `SalesChannelCurrencyDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `salesChannelId` | `sales_channel_id` | FkField | PrimaryKey |
| `currencyId` | `currency_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |
| `currency` | ManyToOne | `CurrencyDefinition` |

### `sales_channel_domain` [E]

**Class:** `SalesChannelDomainDefinition` | **Entity:** `SalesChannelDomainEntity` | **Collection:** `SalesChannelDomainCollection` | **Parent:** `SalesChannelDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `url` | `url` | StringField | ApiAware |
| `salesChannelId` | `sales_channel_id` | FkField | ApiAware |
| `languageId` | `language_id` | FkField | ApiAware |
| `currencyId` | `currency_id` | FkField | ApiAware |
| `snippetSetId` | `snippet_set_id` | FkField | ApiAware |
| `measurementUnits` | `measurement_units` | MeasurementUnitsField | ApiAware |
| `hreflangUseOnlyLocale` | `hreflang_use_only_locale` | BoolField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |
| `language` | ManyToOne | `LanguageDefinition` |
| `currency` | ManyToOne | `CurrencyDefinition` |
| `snippetSet` | ManyToOne | `SnippetSetDefinition` |
| `salesChannelDefaultHreflang` | OneToOne | `SalesChannelDefinition` |
| `productExports` | OneToMany | `ProductExportDefinition` |

### `sales_channel_language` [M]

**Class:** `SalesChannelLanguageDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `salesChannelId` | `sales_channel_id` | FkField | PrimaryKey |
| `languageId` | `language_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |
| `language` | ManyToOne | `LanguageDefinition` |

### `sales_channel_payment_method` [M]

**Class:** `SalesChannelPaymentMethodDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `salesChannelId` | `sales_channel_id` | FkField | PrimaryKey |
| `paymentMethodId` | `payment_method_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |
| `paymentMethod` | ManyToOne | `PaymentMethodDefinition` |

### `sales_channel_shipping_method` [M]

**Class:** `SalesChannelShippingMethodDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `salesChannelId` | `sales_channel_id` | FkField | PrimaryKey |
| `shippingMethodId` | `shipping_method_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |
| `shippingMethod` | ManyToOne | `ShippingMethodDefinition` |

### `sales_channel_translation` [T]

**Class:** `SalesChannelTranslationDefinition` | **Entity:** `SalesChannelTranslationEntity` | **Collection:** `SalesChannelTranslationCollection` | **Parent:** `SalesChannelDefinition`

**Defaults:** `homeEnabled=true`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |
| `homeSlotConfig` | `home_slot_config` | JsonField |  |
| `homeEnabled` | `home_enabled` | BoolField | Required |
| `homeName` | `home_name` | StringField |  |
| `homeMetaTitle` | `home_meta_title` | StringField |  |
| `homeMetaDescription` | `home_meta_description` | StringField |  |
| `homeKeywords` | `home_keywords` | StringField |  |
| `` | `` | CustomFields | ApiAware |

### `sales_channel_type` [E]

**Class:** `SalesChannelTypeDefinition` | **Entity:** `SalesChannelTypeEntity` | **Collection:** `SalesChannelTypeCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `coverUrl` | `cover_url` | StringField |  |
| `iconName` | `icon_name` | StringField |  |
| `screenshotUrls` | `screenshot_urls` | ListField |  |
| `name` | `` | TranslatedField |  |
| `manufacturer` | `` | TranslatedField |  |
| `description` | `` | TranslatedField |  |
| `descriptionLong` | `` | TranslatedField |  |
| `customFields` | `` | TranslatedField |  |

| Association | Type | Target |
|-------------|------|--------|
| `SalesChannelTypeTranslationDefinition::class` | OneToMany | `SalesChannelTypeTranslationDefinition` |
| `salesChannels` | OneToMany | `SalesChannelDefinition` |

**Translated fields:** `name`, `manufacturer`, `description`, `descriptionLong`, `customFields`

### `sales_channel_type_translation` [T]

**Class:** `SalesChannelTypeTranslationDefinition` | **Entity:** `SalesChannelTypeTranslationEntity` | **Collection:** `SalesChannelTypeTranslationCollection` | **Parent:** `SalesChannelTypeDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | Required |
| `manufacturer` | `manufacturer` | StringField |  |
| `description` | `description` | StringField |  |
| `descriptionLong` | `description_long` | LongTextField | ApiAware |
| `` | `` | CustomFields |  |


## System/Snippet

### `snippet` [E]

**Class:** `SnippetDefinition` | **Entity:** `SnippetEntity` | **Collection:** `SnippetCollection` | **Parent:** `SnippetSetDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `setId` | `snippet_set_id` | FkField | ApiAware |
| `translationKey` | `translation_key` | StringField | ApiAware |
| `value` | `value` | LongTextField | ApiAware |
| `author` | `author` | StringField | Required |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `set` | ManyToOne | `SnippetSetDefinition` |

### `snippet_set` [E]

**Class:** `SnippetSetDefinition` | **Entity:** `SnippetSetEntity` | **Collection:** `SnippetSetCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | ApiAware |
| `baseFile` | `base_file` | StringField | Required |
| `iso` | `iso` | StringField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `snippets` | OneToMany | `SnippetDefinition` |
| `salesChannelDomains` | OneToMany | `SalesChannelDomainDefinition` |


## System/StateMachine

### `state_machine` [E]

**Class:** `StateMachineDefinition` | **Entity:** `StateMachineEntity` | **Collection:** `StateMachineCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `technicalName` | `technical_name` | StringField | Required |
| `name` | `` | TranslatedField | SearchRanking |
| `customFields` | `` | TranslatedField |  |
| `initialStateId` | `initial_state_id` | FkField |  |

| Association | Type | Target |
|-------------|------|--------|
| `states` | OneToMany | `StateMachineStateDefinition` |
| `transitions` | OneToMany | `StateMachineTransitionDefinition` |
| `StateMachineTranslationDefinition::class` | OneToMany | `StateMachineTranslationDefinition` |
| `historyEntries` | OneToMany | `StateMachineHistoryDefinition` |

**Translated fields:** `name`, `customFields`

### `state_machine_history` [E]

**Class:** `StateMachineHistoryDefinition` | **Entity:** `StateMachineHistoryEntity` | **Collection:** `StateMachineHistoryCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `referencedId` | `referenced_id` | IdField | Required |
| `referencedVersionId` | `referenced_version_id` | IdField | Required |
| `stateMachineId` | `state_machine_id` | FkField | Required |
| `entityName` | `entity_name` | StringField | Required |
| `fromStateId` | `from_state_id` | FkField | Required |
| `toStateId` | `to_state_id` | FkField | Required |
| `transitionActionName` | `action_name` | StringField |  |
| `userId` | `user_id` | FkField |  |
| `integrationId` | `integration_id` | FkField |  |
| `internalComment` | `internal_comment` | LongTextField |  |

| Association | Type | Target |
|-------------|------|--------|
| `stateMachine` | ManyToOne | `StateMachineDefinition` |
| `fromStateMachineState` | ManyToOne | `StateMachineStateDefinition` |
| `toStateMachineState` | ManyToOne | `StateMachineStateDefinition` |
| `user` | ManyToOne | `UserDefinition` |
| `integration` | ManyToOne | `IntegrationDefinition` |

### `state_machine_state` [E]

**Class:** `StateMachineStateDefinition` | **Entity:** `StateMachineStateEntity` | **Collection:** `StateMachineStateCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `technicalName` | `technical_name` | StringField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `stateMachineId` | `state_machine_id` | FkField | Required |
| `customFields` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `stateMachine` | ManyToOne | `StateMachineDefinition` |
| `fromStateMachineTransitions` | OneToMany | `StateMachineTransitionDefinition` |
| `toStateMachineTransitions` | OneToMany | `StateMachineTransitionDefinition` |
| `StateMachineStateTranslationDefinition::class` | OneToMany | `StateMachineStateTranslationDefinition` |
| `orderTransactions` | OneToMany | `OrderTransactionDefinition` |
| `orderDeliveries` | OneToMany | `OrderDeliveryDefinition` |
| `orders` | OneToMany | `OrderDefinition` |
| `orderTransactionCaptures` | OneToMany | `OrderTransactionCaptureDefinition` |
| `orderTransactionCaptureRefunds` | OneToMany | `OrderTransactionCaptureRefundDefinition` |
| `toStateMachineHistoryEntries` | OneToMany | `StateMachineHistoryDefinition` |
| `fromStateMachineHistoryEntries` | OneToMany | `StateMachineHistoryDefinition` |

**Translated fields:** `name`, `customFields`

### `state_machine_state_translation` [T]

**Class:** `StateMachineStateTranslationDefinition` | **Entity:** `StateMachineStateTranslationEntity` | **Collection:** `StateMachineStateTranslationCollection` | **Parent:** `StateMachineStateDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | Required |
| `` | `` | CustomFields |  |

### `state_machine_transition` [E]

**Class:** `StateMachineTransitionDefinition` | **Entity:** `StateMachineTransitionEntity` | **Collection:** `StateMachineTransitionCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `actionName` | `action_name` | StringField | Required |
| `stateMachineId` | `state_machine_id` | FkField | Required |
| `fromStateId` | `from_state_id` | FkField | Required |
| `toStateId` | `to_state_id` | FkField | Required |
| `` | `` | CustomFields |  |

| Association | Type | Target |
|-------------|------|--------|
| `stateMachine` | ManyToOne | `StateMachineDefinition` |
| `fromStateMachineState` | ManyToOne | `StateMachineStateDefinition` |
| `toStateMachineState` | ManyToOne | `StateMachineStateDefinition` |

### `state_machine_translation` [T]

**Class:** `StateMachineTranslationDefinition` | **Entity:** `StateMachineTranslationEntity` | **Collection:** `StateMachineTranslationCollection` | **Parent:** `StateMachineDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | Required |
| `` | `` | CustomFields | ApiAware |


## System/SystemConfig

### `system_config` [E]

**Class:** `SystemConfigDefinition` | **Entity:** `SystemConfigEntity` | **Collection:** `SystemConfigCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `configurationKey` | `configuration_key` | StringField | ApiAware |
| `configurationValue` | `configuration_value` | ConfigJsonField | ApiAware |
| `salesChannelId` | `sales_channel_id` | FkField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |


## System/Tag

### `tag` [E]

**Class:** `TagDefinition` | **Entity:** `TagEntity` | **Collection:** `TagCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `products` | ManyToMany | `ProductDefinition` |
| `media` | ManyToMany | `MediaDefinition` |
| `categories` | ManyToMany | `CategoryDefinition` |
| `customers` | ManyToMany | `CustomerDefinition` |
| `orders` | ManyToMany | `OrderDefinition` |
| `shippingMethods` | ManyToMany | `ShippingMethodDefinition` |
| `newsletterRecipients` | ManyToMany | `NewsletterRecipientDefinition` |
| `landingPages` | ManyToMany | `LandingPageDefinition` |
| `rules` | ManyToMany | `RuleDefinition` |


## System/Tax

### `tax` [E]

**Class:** `TaxDefinition` | **Entity:** `TaxEntity` | **Collection:** `TaxCollection`

**Defaults:** `position=0`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `taxRate` | `tax_rate` | FloatField | ApiAware |
| `name` | `name` | StringField | ApiAware |
| `position` | `position` | IntField | Required |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `products` | OneToMany | `ProductDefinition` |
| `rules` | OneToMany | `TaxRuleDefinition` |
| `shippingMethods` | OneToMany | `ShippingMethodDefinition` |

### `tax_provider` [E]

**Class:** `TaxProviderDefinition` | **Entity:** `TaxProviderEntity` | **Collection:** `TaxProviderCollection`

**Defaults:** `position=1`, `active=true`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `identifier` | `identifier` | StringField | Required |
| `active` | `active` | BoolField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `active` | `active` | BoolField | ApiAware |
| `priority` | `priority` | IntField | Required |
| `processUrl` | `process_url` | StringField | ApiAware |
| `availabilityRuleId` | `availability_rule_id` | FkField |  |
| `appId` | `app_id` | FkField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `TaxProviderTranslationDefinition::class` | OneToMany | `TaxProviderTranslationDefinition` |
| `availabilityRule` | ManyToOne | `RuleDefinition` |
| `app` | ManyToOne | `AppDefinition` |

**Translated fields:** `name`, `customFields`

### `tax_provider_translation` [T]

**Class:** `TaxProviderTranslationDefinition` | **Entity:** `TaxProviderTranslationEntity` | **Collection:** `TaxProviderTranslationCollection` | **Parent:** `TaxProviderDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | Required |
| `` | `` | CustomFields | ApiAware |

### `tax_rule` [E]

**Class:** `TaxRuleDefinition` | **Entity:** `TaxRuleEntity` | **Collection:** `TaxRuleCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `taxRuleTypeId` | `tax_rule_type_id` | FkField | Required |
| `countryId` | `country_id` | FkField | Required |
| `taxRate` | `tax_rate` | FloatField | Required |
| `data` | `data` | JsonField |  |
| `states` | `states` | ListField |  |
| `zipCode` | `zipCode` | StringField |  |
| `fromZipCode` | `fromZipCode` | StringField |  |
| `toZipCode` | `toZipCode` | StringField |  |
| `taxId` | `tax_id` | FkField | Required |
| `activeFrom` | `active_from` | DateTimeField |  |

| Association | Type | Target |
|-------------|------|--------|
| `type` | ManyToOne | `TaxRuleTypeDefinition` |
| `country` | ManyToOne | `CountryDefinition` |
| `tax` | ManyToOne | `TaxDefinition` |

### `tax_rule_type` [E]

**Class:** `TaxRuleTypeDefinition` | **Entity:** `TaxRuleTypeEntity` | **Collection:** `TaxRuleTypeCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `technicalName` | `technical_name` | StringField | Required |
| `position` | `position` | IntField | Required |
| `typeName` | `` | TranslatedField | SearchRanking |

| Association | Type | Target |
|-------------|------|--------|
| `rules` | OneToMany | `TaxRuleDefinition` |
| `TaxRuleTypeTranslationDefinition::class` | OneToMany | `TaxRuleTypeTranslationDefinition` |

**Translated fields:** `typeName`

### `tax_rule_type_translation` [T]

**Class:** `TaxRuleTypeTranslationDefinition` | **Entity:** `TaxRuleTypeTranslationEntity` | **Collection:** `TaxRuleTypeTranslationCollection` | **Parent:** `TaxRuleTypeDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `typeName` | `type_name` | StringField | Required |


## System/Unit

### `unit` [E]

**Class:** `UnitDefinition` | **Entity:** `UnitEntity` | **Collection:** `UnitCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `shortCode` | `` | TranslatedField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `products` | OneToMany | `ProductDefinition` |
| `UnitTranslationDefinition::class` | OneToMany | `UnitTranslationDefinition` |

**Translated fields:** `shortCode`, `name`, `customFields`

### `unit_translation` [T]

**Class:** `UnitTranslationDefinition` | **Entity:** `UnitTranslationEntity` | **Collection:** `UnitTranslationCollection` | **Parent:** `UnitDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `shortCode` | `short_code` | StringField | ApiAware |
| `name` | `name` | StringField | ApiAware |
| `` | `` | CustomFields | ApiAware |


## System/User

### `user` [E]

**Class:** `UserDefinition` | **Entity:** `UserEntity` | **Collection:** `UserCollection`

**Defaults:** `timeZone="UTC"`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `localeId` | `locale_id` | FkField | Required |
| `username` | `username` | StringField | Required |
| `password` | `password` | PasswordField | Required |
| `firstName` | `first_name` | StringField | Required |
| `lastName` | `last_name` | StringField | Required |
| `title` | `title` | StringField | SearchRanking |
| `email` | `email` | EmailField | Required |
| `active` | `active` | BoolField |  |
| `admin` | `admin` | BoolField |  |
| `mcpAllowlist` | `mcp_allowlist` | JsonField |  |
| `lastUpdatedPasswordAt` | `last_updated_password_at` | DateTimeField |  |
| `timeZone` | `time_zone` | TimeZoneField | Required |
| `` | `` | CustomFields |  |
| `avatarId` | `avatar_id` | FkField |  |
| `storeToken` | `store_token` | StringField |  |

| Association | Type | Target |
|-------------|------|--------|
| `locale` | ManyToOne | `LocaleDefinition` |
| `avatarMedia` | ManyToOne | `MediaDefinition` |
| `media` | OneToMany | `MediaDefinition` |
| `accessKeys` | OneToMany | `UserAccessKeyDefinition` |
| `configs` | OneToMany | `UserConfigDefinition` |
| `stateMachineHistoryEntries` | OneToMany | `StateMachineHistoryDefinition` |
| `importExportLogEntries` | OneToMany | `ImportExportLogDefinition` |
| `aclRoles` | ManyToMany | `AclRoleDefinition` |
| `recoveryUser` | OneToOne | `UserRecoveryDefinition` |
| `createdOrders` | OneToMany | `OrderDefinition` |
| `updatedOrders` | OneToMany | `OrderDefinition` |
| `createdCustomers` | OneToMany | `CustomerDefinition` |
| `updatedCustomers` | OneToMany | `CustomerDefinition` |

### `user_access_key` [E]

**Class:** `UserAccessKeyDefinition` | **Entity:** `UserAccessKeyEntity` | **Collection:** `UserAccessKeyCollection` | **Parent:** `UserDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `userId` | `user_id` | FkField | Required |
| `accessKey` | `access_key` | StringField | Required |
| `secretAccessKey` | `secret_access_key` | PasswordField | Required |
| `lastUsageAt` | `last_usage_at` | DateTimeField |  |
| `` | `` | CustomFields |  |

| Association | Type | Target |
|-------------|------|--------|
| `user` | ManyToOne | `UserDefinition` |

### `user_config` [E]

**Class:** `UserConfigDefinition` | **Entity:** `UserConfigEntity` | **Collection:** `UserConfigCollection` | **Parent:** `UserDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `userId` | `user_id` | FkField | Required |
| `key` | `key` | StringField | Required |
| `value` | `value` | JsonField |  |

| Association | Type | Target |
|-------------|------|--------|
| `user` | ManyToOne | `UserDefinition` |

### `user_recovery` [E]

**Class:** `UserRecoveryDefinition` | **Entity:** `UserRecoveryEntity` | **Collection:** `UserRecoveryCollection` | **Parent:** `UserDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `hash` | `hash` | StringField | Required |
| `userId` | `user_id` | FkField | Required |
| `` | `` | CreatedAtField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `user` | OneToOne | `UserDefinition` |
