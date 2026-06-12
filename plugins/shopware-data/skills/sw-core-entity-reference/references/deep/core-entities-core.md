# Shopware 6 Core Entities — Core

> Auto-generated from `src/` — 65 definitions


## Core/Checkout

### `document` [E]

**Class:** `DocumentDefinition` | **Entity:** `DocumentEntity` | **Collection:** `DocumentCollection` | **Parent:** `OrderDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `documentTypeId` | `document_type_id` | FkField | ApiAware |
| `referencedDocumentId` | `referenced_document_id` | FkField | ApiAware |
| `orderId` | `order_id` | FkField | ApiAware |
| `documentMediaFileId` | `document_media_file_id` | FkField | ApiAware |
| `documentA11yMediaFileId` | `document_a11y_media_file_id` | FkField | ApiAware |
| `order_version_id` | `OrderDefinition::class` | ReferenceVersionField | ApiAware |
| `config` | `config` | JsonField | ApiAware |
| `sent` | `sent` | BoolField | ApiAware |
| `static` | `static` | BoolField | ApiAware |
| `deepLinkCode` | `deep_link_code` | StringField | ApiAware |
| `documentNumber` | `document_number` | NumberRangeField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `documentType` | ManyToOne | `DocumentTypeDefinition` |
| `order` | ManyToOne | `OrderDefinition` |
| `referencedDocument` | ManyToOne | `` |
| `dependentDocuments` | OneToMany | `` |
| `documentMediaFile` | ManyToOne | `MediaDefinition` |
| `documentA11yMediaFile` | ManyToOne | `MediaDefinition` |
| `documentFiles` | OneToMany | `DocumentFileDefinition` |

### `document_base_config` [E]

**Class:** `DocumentBaseConfigDefinition` | **Entity:** `DocumentBaseConfigEntity` | **Collection:** `DocumentBaseConfigCollection` | **Parent:** `DocumentTypeDefinition`

**Defaults:** `global=false`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `documentTypeId` | `document_type_id` | FkField | ApiAware |
| `logoId` | `logo_id` | FkField | ApiAware |
| `name` | `name` | StringField | ApiAware |
| `filenamePrefix` | `filename_prefix` | StringField | ApiAware |
| `filenameSuffix` | `filename_suffix` | StringField | ApiAware |
| `global` | `global` | BoolField | ApiAware |
| `documentNumber` | `document_number` | NumberRangeField | ApiAware |
| `pageSize` | `page_size` | StringField |  |
| `pageOrientation` | `page_orientation` | StringField |  |
| `itemsPerPage` | `items_per_page` | IntField |  |
| `displayHeader` | `display_header` | BoolField |  |
| `displayFooter` | `display_footer` | BoolField |  |
| `displayPageCount` | `display_page_count` | BoolField |  |
| `displayCompanyAddress` | `display_company_address` | BoolField |  |
| `displayReturnAddress` | `display_return_address` | BoolField |  |
| `displayCustomerVatId` | `display_customer_vat_id` | BoolField |  |
| `` | `` | CustomFields | ApiAware |
| `` | `` | CreatedAtField | ApiAware |
| `config` | `config` | JsonField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `documentType` | ManyToOne | `DocumentTypeDefinition` |
| `logo` | ManyToOne | `MediaDefinition` |
| `salesChannels` | OneToMany | `DocumentBaseConfigSalesChannelDefinition` |

### `document_base_config_sales_channel` [E]

**Class:** `DocumentBaseConfigSalesChannelDefinition` | **Entity:** `DocumentBaseConfigSalesChannelEntity` | **Collection:** `DocumentBaseConfigSalesChannelCollection` | **Parent:** `DocumentBaseConfigDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `documentBaseConfigId` | `document_base_config_id` | FkField | ApiAware |
| `salesChannelId` | `sales_channel_id` | FkField | ApiAware |
| `documentTypeId` | `document_type_id` | FkField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `documentType` | ManyToOne | `DocumentTypeDefinition` |
| `documentBaseConfig` | ManyToOne | `DocumentBaseConfigDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |

### `document_file` [E]

**Class:** `DocumentFileDefinition` | **Entity:** `DocumentFileEntity` | **Collection:** `DocumentFileCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `documentId` | `document_id` | FkField | Required |
| `mediaId` | `media_id` | FkField | Required |
| `documentFormat` | `document_format` | StringField | Required |
| `` | `` | CreatedAtField |  |
| `` | `` | UpdatedAtField |  |

| Association | Type | Target |
|-------------|------|--------|
| `document` | ManyToOne | `DocumentDefinition` |
| `media` | OneToOne | `MediaDefinition` |

### `document_type` [E]

**Class:** `DocumentTypeDefinition` | **Entity:** `DocumentTypeEntity` | **Collection:** `DocumentTypeCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `technicalName` | `technical_name` | StringField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `DocumentTypeTranslationDefinition::class` | OneToMany | `DocumentTypeTranslationDefinition` |
| `documents` | OneToMany | `DocumentDefinition` |
| `documentBaseConfigs` | OneToMany | `DocumentBaseConfigDefinition` |
| `documentBaseConfigSalesChannels` | OneToMany | `DocumentBaseConfigSalesChannelDefinition` |

**Translated fields:** `name`, `customFields`

### `document_type_translation` [T]

**Class:** `DocumentTypeTranslationDefinition` | **Entity:** `DocumentTypeTranslationEntity` | **Parent:** `DocumentTypeDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | Required |
| `` | `` | CustomFields | ApiAware |


## Core/DevOps

### `name_constant_entity` [E]

**Class:** `NameConstantEntityDefinition`


## Core/Framework

### `_date_field_test` [E]

**Class:** `DateDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `date` | `date` | DateField | ApiAware |
| `dateNullable` | `date_nullable` | DateField | ApiAware |

### `_test_country` [E]

**Class:** `SingleEntityDependencyTestDependencySubDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | Required |
| `iso` | `iso` | StringField | Required |

### `_test_lock` [E]

**Class:** `TestDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `description` | `description` | StringField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `` | `` | LockedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `TestTranslationDefinition::class` | OneToMany | `TestTranslationDefinition` |

**Translated fields:** `name`

### `_test_lock_translation` [T]

**Class:** `TestTranslationDefinition` | **Parent:** `TestDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |

### `_test_nullable` [E]

**Class:** `ConfigJsonDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `data` | `data` | ConfigJsonField | ApiAware |

### `_test_nullable` [E]

**Class:** `JsonDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `data` | `data` | JsonField | ApiAware |
| `root` | `root` | JsonField |  |
| `child` | `child` | JsonField |  |
| `childDateTime` | `childDateTime` | DateTimeField | ApiAware |
| `childDate` | `childDate` | DateField | ApiAware |

### `_test_nullable` [E]

**Class:** `ListDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `data` | `data` | ListField | ApiAware |

### `_test_nullable` [E]

**Class:** `NestedDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `data` | `data` | JsonField |  |
| `gross` | `gross` | FloatField | ApiAware |
| `net` | `net` | FloatField | ApiAware |
| `foo` | `foo` | JsonField |  |
| `bar` | `bar` | StringField | ApiAware |
| `baz` | `baz` | JsonField |  |
| `deep` | `deep` | BoolField | ApiAware |

### `_test_nullable` [E]

**Class:** `PriceFieldDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `data` | `data` | PriceField | ApiAware |

### `_test_nullable` [E]

**Class:** `WriteProtectedDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `protected` | `protected` | StringField | ApiAware |
| `systemProtected` | `system_protected` | StringField | ApiAware |
| `relationId` | `relation_id` | FkField |  |
| `systemRelationId` | `system_relation_id` | FkField |  |

| Association | Type | Target |
|-------------|------|--------|
| `relation` | ManyToOne | `WriteProtectedRelationDefinition` |
| `relations` | ManyToMany | `WriteProtectedRelationDefinition` |
| `systemRelation` | ManyToOne | `WriteProtectedRelationDefinition` |
| `systemRelations` | ManyToMany | `WriteProtectedRelationDefinition` |

### `_test_nullable` [E]

**Class:** `WriteProtectedTranslatedDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `protected` | `` | TranslatedField | ApiAware |
| `systemProtected` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `WriteProtectedTranslationDefinition::class` | OneToMany | `WriteProtectedTranslationDefinition` |

**Translated fields:** `protected`, `systemProtected`

### `_test_nullable_reference` [M]

**Class:** `WriteProtectedReferenceDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `wpId` | `wp_id` | FkField | ApiAware |
| `relationId` | `relation_id` | FkField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `wp` | ManyToOne | `WriteProtectedDefinition` |
| `relation` | ManyToOne | `WriteProtectedRelationDefinition` |

### `_test_nullable_translation` [T]

**Class:** `WriteProtectedTranslationDefinition` | **Parent:** `WriteProtectedTranslatedDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `protected` | `protected` | StringField | ApiAware |
| `systemProtected` | `system_protected` | StringField | ApiAware |

### `_test_pickup_point` [E]

**Class:** `SingleEntityDependencyTestRootDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | Required |
| `name` | `name` | StringField | Required |
| `warehouseId` | `warehouse_id` | FkField | Required |
| `zipcodeId` | `zipcode_id` | FkField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `warehouse` | ManyToOne | `SingleEntityDependencyTestSubDefinition` |
| `zipcode` | ManyToOne | `SingleEntityDependencyTestDependencyDefinition` |

### `_test_relation` [E]

**Class:** `WriteProtectedRelationDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `wp` | OneToMany | `WriteProtectedDefinition` |
| `wps` | ManyToMany | `WriteProtectedDefinition` |
| `systemWp` | OneToMany | `WriteProtectedDefinition` |
| `systemWps` | ManyToMany | `WriteProtectedDefinition` |

### `_test_to_many_association` [E]

**Class:** `ToManyAssociationDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `toMany` | ManyToMany | `ToManyAssociationDependencyDefinition` |

### `_test_to_many_association_dependency` [E]

**Class:** `ToManyAssociationDependencyDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `toManyDependency` | ManyToMany | `ToManyAssociationDefinition` |

### `_test_to_many_association_mapping` [M]

**Class:** `ToManyAssociationMappingDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `toManyId` | `to_many_id` | FkField | PrimaryKey |
| `toManyDependencyId` | `to_many_dependency_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `toMany` | ManyToOne | `ToManyAssociationDefinition` |
| `toManyDependency` | ManyToOne | `ToManyAssociationDependencyDefinition` |

### `_test_warehouse` [E]

**Class:** `SingleEntityDependencyTestSubDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | Required |
| `name` | `name` | StringField | Required |
| `zipcodeId` | `zipcode_id` | FkField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `zipcode` | ManyToOne | `SingleEntityDependencyTestDependencyDefinition` |

### `_test_was_modified_by_user` [E]

**Class:** `WasModifiedByUserFieldDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `name` | StringField |  |
| `` | `` | WasModifiedByUserField |  |

### `_test_zipcode` [E]

**Class:** `SingleEntityDependencyTestDependencyDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | Required |
| `zipcode` | `zipcode` | StringField | Required |
| `countryId` | `country_id` | FkField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `country` | ManyToOne | `SingleEntityDependencyTestDependencySubDefinition` |

### `acl_role` [E]

**Class:** `AclRoleDefinition` | **Entity:** `AclRoleEntity` | **Collection:** `AclRoleCollection`

**Defaults:** `privileges="["`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | Required |
| `description` | `description` | LongTextField |  |
| `privileges` | `privileges` | ListField | Required |
| `deletedAt` | `deleted_at` | DateTimeField |  |

| Association | Type | Target |
|-------------|------|--------|
| `users` | ManyToMany | `UserDefinition` |
| `app` | OneToOne | `AppDefinition` |
| `integrations` | ManyToMany | `IntegrationDefinition` |

### `acl_user_role` [M]

**Class:** `AclUserRoleDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `userId` | `user_id` | FkField | PrimaryKey |
| `aclRoleId` | `acl_role_id` | FkField | PrimaryKey |
| `` | `` | CreatedAtField |  |
| `` | `` | UpdatedAtField |  |

| Association | Type | Target |
|-------------|------|--------|
| `user` | ManyToOne | `UserDefinition` |
| `aclRole` | ManyToOne | `AclRoleDefinition` |

### `acme_consists_of_mapping` [M]

**Class:** `ConsistsOfManyToManyDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `productId` | `product_id` | FkField | PrimaryKey |
| `productIdTo` | `product_id_to` | FkField | PrimaryKey |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `productTo` | ManyToOne | `ProductDefinition` |

### `attribute_test` [E]

**Class:** `CustomFieldTestDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `parentId` | `parent_id` | IdField | ApiAware |
| `self::class` | `self::class` | ParentFkField | ApiAware |
| `name` | `name` | StringField | Inherited |
| `customTranslated` | `` | TranslatedField | Inherited |
| `custom` | `custom` | CustomFields | Inherited |

| Association | Type | Target |
|-------------|------|--------|
| `CustomFieldTestTranslationDefinition::class` | OneToMany | `CustomFieldTestTranslationDefinition` |
| `self::class` | ManyToOne | `` |
| `self::class` | OneToMany | `` |

**Translated fields:** `customTranslated`

### `attribute_test_translation` [T]

**Class:** `CustomFieldTestTranslationDefinition` | **Parent:** `CustomFieldTestDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `customTranslated` | `custom_translated` | CustomFields |  |

### `custom_field_plain_test` [E]

**Class:** `CustomFieldPlainTestDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `name` | StringField | Inherited |
| `` | `` | CustomFields | ApiAware |

### `date_time_test` [E]

**Class:** `DateTimeDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `name` | StringField |  |

### `defaults` [E]

**Class:** `DefaultsDefinition`

**Defaults:** `active=true`, `children="["`, `foo="Default foo"`, `name="Default name"`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `active` | `active` | BoolField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `children` | OneToMany | `DefaultsChildDefinition` |

### `defaults_child` [E]

**Class:** `DefaultsChildDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `defaultsId` | `defaults_id` | FkField |  |
| `foo` | `foo` | StringField | Required |
| `name` | `` | TranslatedField |  |

| Association | Type | Target |
|-------------|------|--------|
| `DefaultsChildTranslationDefinition::class` | OneToMany | `DefaultsChildTranslationDefinition` |
| `defaults` | ManyToOne | `DefaultsDefinition` |

**Translated fields:** `name`

### `defaults_child_translation` [T]

**Class:** `DefaultsChildTranslationDefinition` | **Parent:** `DefaultsChildDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | Required |

### `email` [E]

**Class:** `EmailDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `email` | `email` | EmailField | ApiAware |

### `extendable` [E]

**Class:** `ExtendableDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `apiAwareTest` | `api_aware_test` | BoolField | ApiAware |

### `extended` [E]

**Class:** `ExtendedDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `name` | StringField | ApiAware |
| `extendableId` | `extendable_id` | FkField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `toOne` | OneToOne | `ExtendableDefinition` |
| `toMany` | ManyToOne | `ExtendableDefinition` |

### `extended_product` [E]

**Class:** `ExtendedProductDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `name` | StringField |  |
| `productId` | `product_id` | FkField |  |
| `languageId` | `language_id` | FkField |  |

| Association | Type | Target |
|-------------|------|--------|
| `language` | ManyToOne | `LanguageDefinition` |
| `toOne` | OneToOne | `ProductDefinition` |
| `manyToOne` | ManyToOne | `ProductDefinition` |

### `extended_product_manufacturer` [E]

**Class:** `ExtendedProductManufacturerDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `name` | StringField | ApiAware |
| `manufacturerId` | `manufacturer_id` | FkField | ApiAware |
| `languageId` | `language_id` | FkField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `language` | ManyToOne | `LanguageDefinition` |
| `toOne` | OneToOne | `ProductManufacturerDefinition` |
| `manyToOne` | ManyToOne | `ProductManufacturerDefinition` |

### `fk_field_primary` [E]

**Class:** `FkFieldPrimaryTestDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `productId` | `product_id` | FkField | ApiAware |
| `name` | `name` | StringField | ApiAware |

### `group_by_test` [E]

**Class:** `GroupByTestDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `name` | StringField | ApiAware |
| `field1` | `field1` | IntField | ApiAware |
| `field2` | `field2` | IntField | ApiAware |

### `many_to_one_product` [E]

**Class:** `ManyToOneProductDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `products` | OneToMany | `ProductDefinition` |

### `multi_fk_field_primary` [E]

**Class:** `MultiFkFieldPrimaryTestDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `firstId` | `first_id` | IdField | ApiAware |
| `secondId` | `second_id` | IdField | ApiAware |

### `named` [E]

**Class:** `NamedDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `name` | StringField | ApiAware |
| `optionalGroupId` | `optional_group_id` | FkField |  |

| Association | Type | Target |
|-------------|------|--------|
| `optionalGroup` | ManyToOne | `NamedOptionalGroupDefinition` |

### `named_optional_group` [E]

**Class:** `NamedOptionalGroupDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `name` | StringField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `nameds` | OneToMany | `NamedDefinition` |

### `non_id_primary_key_test` [E]

**Class:** `NonIdFieldNamePrimaryKeyTestDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `testField` | `test_field` | IdField | ApiAware |
| `nonPk` | `non_pk` | IdField |  |
| `name` | `name` | StringField |  |

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

### `product_one_to_one_inherited` [E]

**Class:** `OneToOneInheritedProductDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | Required |
| `` | `` | VersionField |  |
| `myDate` | `my_date` | DateTimeField | Inherited |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | Required |
| `productId` | `product_id` | FkField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `product` | OneToOne | `ProductDefinition` |

### `root` [E]

**Class:** `RootDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField |  |
| `name` | `name` | StringField |  |

| Association | Type | Target |
|-------------|------|--------|
| `sub` | OneToOne | `SubDefinition` |
| `subCascade` | OneToOne | `SubCascadeDefinition` |

### `root_sub` [E]

**Class:** `SubDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField |  |
| `name` | `name` | StringField |  |
| `stock` | `stock` | IntField |  |
| `rootId` | `root_id` | FkField |  |
| `RootDefinition::class` | `RootDefinition::class` | ReferenceVersionField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `root` | OneToOne | `RootDefinition` |
| `manies` | OneToMany | `SubManyDefinition` |

### `root_sub_cascade` [E]

**Class:** `SubCascadeDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField |  |
| `name` | `name` | StringField |  |
| `stock` | `stock` | IntField |  |
| `rootId` | `root_id` | FkField |  |
| `RootDefinition::class` | `RootDefinition::class` | ReferenceVersionField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `root` | OneToOne | `RootDefinition` |

### `root_sub_many` [E]

**Class:** `SubManyDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField |  |
| `name` | `name` | StringField |  |
| `subId` | `root_sub_id` | FkField | ApiAware |
| `SubDefinition::class` | `SubDefinition::class` | ReferenceVersionField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `sub` | ManyToOne | `SubDefinition` |

### `script` [E]

**Class:** `ScriptDefinition` | **Entity:** `ScriptEntity` | **Collection:** `ScriptCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `script` | `script` | LongTextField | Required |
| `hook` | `hook` | StringField | Required |
| `name` | `name` | StringField | Required |
| `active` | `active` | BoolField | Required |
| `appId` | `app_id` | FkField |  |

| Association | Type | Target |
|-------------|------|--------|
| `app` | ManyToOne | `AppDefinition` |

### `test_entity_one` [E]

**Class:** `TestEntityOneDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `technicalName` | `technical_name` | StringField | PrimaryKey |

### `test_entity_two` [E]

**Class:** `TestEntityTwoDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `testEntityOneTechnicalName` | `test_entity_one_technical_name` | NonUuidFkField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `testEntityOne` | ManyToOne | `TestEntityOneDefinition` |

### `translatable_test` [E]

**Class:** `TranslatableTestDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `TranslatableTestTranslationDefinition::class` | OneToMany | `TranslatableTestTranslationDefinition` |

**Translated fields:** `name`

### `translatable_test_translation` [T]

**Class:** `TranslatableTestTranslationDefinition` | **Parent:** `CustomFieldTestDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |


## Core/System

### `sales_channel_salutation` [E]

**Class:** `SalesChannelSalutationDefinition`

### `salutation` [E]

**Class:** `SalutationDefinition` | **Entity:** `SalutationEntity` | **Collection:** `SalutationCollection`

**Defaults:** `position="self::DEFAULT_POSITION"`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `salutationKey` | `salutation_key` | StringField | ApiAware |
| `displayName` | `` | TranslatedField | ApiAware |
| `letterName` | `` | TranslatedField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |
| `position` | `position` | IntField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `SalutationTranslationDefinition::class` | OneToMany | `SalutationTranslationDefinition` |
| `customers` | OneToMany | `CustomerDefinition` |
| `customerAddresses` | OneToMany | `CustomerAddressDefinition` |
| `orderCustomers` | OneToMany | `OrderCustomerDefinition` |
| `orderAddresses` | OneToMany | `OrderAddressDefinition` |
| `newsletterRecipients` | OneToMany | `NewsletterRecipientDefinition` |

**Translated fields:** `displayName`, `letterName`, `customFields`

### `salutation_translation` [T]

**Class:** `SalutationTranslationDefinition` | **Entity:** `SalutationTranslationEntity` | **Collection:** `SalutationTranslationCollection` | **Parent:** `SalutationDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `displayName` | `display_name` | StringField | ApiAware |
| `letterName` | `letter_name` | StringField | ApiAware |
| `` | `` | CustomFields | ApiAware |


## Core/Test

### `test_entity` [E]

**Class:** `TestEntityDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `idAllowHtml` | `idAllowHtml` | IdField | AllowHtml |
| `idAllowHtmlSanitized` | `idAllowHtmlSanitized` | IdField | AllowHtml |
