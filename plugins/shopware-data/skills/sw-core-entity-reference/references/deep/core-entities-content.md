# Shopware 6 Core Entities — Content

> Auto-generated from `src/` — 89 definitions


## Content/CMS

### `cms_block` [E]

**Class:** `CmsBlockDefinition` | **Entity:** `CmsBlockEntity` | **Collection:** `CmsBlockCollection` | **Parent:** `CmsSectionDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `CmsSectionDefinition::class` | `CmsSectionDefinition::class` | ReferenceVersionField | Required |
| `position` | `position` | IntField | ApiAware |
| `type` | `type` | StringField | ApiAware |
| `` | `` | LockedField |  |
| `name` | `name` | StringField | ApiAware |
| `sectionPosition` | `section_position` | StringField | ApiAware |
| `marginTop` | `margin_top` | StringField | ApiAware |
| `marginBottom` | `margin_bottom` | StringField | ApiAware |
| `marginLeft` | `margin_left` | StringField | ApiAware |
| `marginRight` | `margin_right` | StringField | ApiAware |
| `backgroundColor` | `background_color` | StringField | ApiAware |
| `backgroundMediaId` | `background_media_id` | FkField | ApiAware |
| `backgroundMediaMode` | `background_media_mode` | StringField | ApiAware |
| `cssClass` | `css_class` | StringField | ApiAware |
| `visibility` | `visibility` | JsonField | ApiAware |
| `mobile` | `mobile` | BoolField | ApiAware |
| `desktop` | `desktop` | BoolField | ApiAware |
| `tablet` | `tablet` | BoolField | ApiAware |
| `sectionId` | `cms_section_id` | FkField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `section` | ManyToOne | `CmsSectionDefinition` |
| `backgroundMedia` | ManyToOne | `MediaDefinition` |
| `slots` | OneToMany | `CmsSlotDefinition` |

### `cms_page` [E]

**Class:** `CmsPageDefinition` | **Entity:** `CmsPageEntity` | **Collection:** `CmsPageCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `type` | `type` | StringField | ApiAware |
| `entity` | `entity` | StringField | ApiAware |
| `cssClass` | `css_class` | StringField | ApiAware |
| `config` | `config` | JsonField | ApiAware |
| `backgroundColor` | `background_color` | StringField | ApiAware |
| `previewMediaId` | `preview_media_id` | FkField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |
| `` | `` | LockedField |  |

| Association | Type | Target |
|-------------|------|--------|
| `sections` | OneToMany | `CmsSectionDefinition` |
| `CmsPageTranslationDefinition::class` | OneToMany | `CmsPageTranslationDefinition` |
| `previewMedia` | ManyToOne | `MediaDefinition` |
| `categories` | OneToMany | `CategoryDefinition` |
| `landingPages` | OneToMany | `LandingPageDefinition` |
| `homeSalesChannels` | OneToMany | `SalesChannelDefinition` |
| `products` | OneToMany | `ProductDefinition` |

**Translated fields:** `name`, `customFields`

### `cms_page_translation` [T]

**Class:** `CmsPageTranslationDefinition` | **Entity:** `CmsPageTranslationEntity` | **Parent:** `CmsPageDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField |  |
| `` | `` | CustomFields | ApiAware |

### `cms_section` [E]

**Class:** `CmsSectionDefinition` | **Entity:** `CmsSectionEntity` | **Collection:** `CmsSectionCollection` | **Parent:** `CmsPageDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField |  |
| `CmsPageDefinition::class` | `CmsPageDefinition::class` | ReferenceVersionField | Required |
| `position` | `position` | IntField | ApiAware |
| `type` | `type` | StringField | ApiAware |
| `` | `` | LockedField |  |
| `name` | `name` | StringField | ApiAware |
| `sizingMode` | `sizing_mode` | StringField | ApiAware |
| `mobileBehavior` | `mobile_behavior` | StringField | ApiAware |
| `backgroundColor` | `background_color` | StringField | ApiAware |
| `backgroundMediaId` | `background_media_id` | FkField | ApiAware |
| `backgroundMediaMode` | `background_media_mode` | StringField | ApiAware |
| `cssClass` | `css_class` | StringField | ApiAware |
| `pageId` | `cms_page_id` | FkField | ApiAware |
| `visibility` | `visibility` | JsonField | ApiAware |
| `mobile` | `mobile` | BoolField | ApiAware |
| `desktop` | `desktop` | BoolField | ApiAware |
| `tablet` | `tablet` | BoolField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `page` | ManyToOne | `CmsPageDefinition` |
| `backgroundMedia` | ManyToOne | `MediaDefinition` |
| `blocks` | OneToMany | `CmsBlockDefinition` |

### `cms_slot` [E]

**Class:** `CmsSlotDefinition` | **Entity:** `CmsSlotEntity` | **Collection:** `CmsSlotCollection` | **Parent:** `CmsBlockDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `CmsBlockDefinition::class` | `CmsBlockDefinition::class` | ReferenceVersionField | Required |
| `fieldConfig` | `fieldConfig` | JsonField | Runtime |
| `type` | `type` | StringField | ApiAware |
| `slot` | `slot` | StringField | ApiAware |
| `` | `` | LockedField | ApiAware |
| `config` | `` | TranslatedField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |
| `data` | `data` | JsonField | ApiAware |
| `blockId` | `cms_block_id` | FkField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `block` | ManyToOne | `CmsBlockDefinition` |
| `CmsSlotTranslationDefinition::class` | OneToMany | `CmsSlotTranslationDefinition` |

**Translated fields:** `config`, `customFields`

### `cms_slot_translation` [T]

**Class:** `CmsSlotTranslationDefinition` | **Entity:** `CmsSlotTranslationEntity` | **Parent:** `CmsSlotDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `config` | `config` | SlotConfigField | ApiAware |
| `` | `` | CustomFields | ApiAware |


## Content/Category

### `category` [E]

**Class:** `CategoryDefinition` | **Entity:** `CategoryEntity` | **Collection:** `CategoryCollection`

**Defaults:** `displayNestedProducts=true`, `type="page"`, `productAssignmentType="product"`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `self::class` | `self::class` | ParentFkField | ApiAware |
| `parent_version_id` | `self::class` | ReferenceVersionField | ApiAware |
| `afterCategoryId` | `after_category_id` | FkField | ApiAware |
| `after_category_version_id` | `self::class` | ReferenceVersionField | ApiAware |
| `mediaId` | `media_id` | FkField | ApiAware |
| `displayNestedProducts` | `display_nested_products` | BoolField | ApiAware |
| `` | `` | AutoIncrementField |  |
| `breadcrumb` | `` | TranslatedField | ApiAware |
| `level` | `level` | TreeLevelField | ApiAware |
| `path` | `path` | TreePathField | ApiAware |
| `` | `` | ChildCountField | ApiAware |
| `type` | `type` | StringField | ApiAware |
| `productAssignmentType` | `product_assignment_type` | StringField | ApiAware |
| `visible` | `visible` | BoolField | ApiAware |
| `active` | `active` | BoolField | ApiAware |
| `visibleChildCount` | `visible_child_count` | IntField | Runtime |
| `name` | `` | TranslatedField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |
| `slotConfig` | `` | TranslatedField |  |
| `linkType` | `` | TranslatedField | ApiAware |
| `internalLink` | `` | TranslatedField | ApiAware |
| `externalLink` | `` | TranslatedField | ApiAware |
| `linkNewTab` | `` | TranslatedField | ApiAware |
| `description` | `` | TranslatedField | ApiAware |
| `metaTitle` | `` | TranslatedField | ApiAware |
| `metaDescription` | `` | TranslatedField | ApiAware |
| `keywords` | `` | TranslatedField | ApiAware |
| `cmsPageId` | `cms_page_id` | FkField | ApiAware |
| `CmsPageDefinition::class` | `CmsPageDefinition::class` | ReferenceVersionField | Required |
| `productStreamId` | `product_stream_id` | FkField | ApiAware |
| `customEntityTypeId` | `custom_entity_type_id` | FkField | ApiAware |
| `cmsPageIdSwitched` | `cms_page_id_switched` | BoolField | Runtime |

| Association | Type | Target |
|-------------|------|--------|
| `self::class` | ManyToOne | `` |
| `self::class` | OneToMany | `` |
| `media` | ManyToOne | `MediaDefinition` |
| `CategoryTranslationDefinition::class` | OneToMany | `CategoryTranslationDefinition` |
| `products` | ManyToMany | `ProductDefinition` |
| `nestedProducts` | ManyToMany | `ProductDefinition` |
| `tags` | ManyToMany | `TagDefinition` |
| `cmsPage` | ManyToOne | `CmsPageDefinition` |
| `productStream` | ManyToOne | `ProductStreamDefinition` |
| `navigationSalesChannels` | OneToMany | `SalesChannelDefinition` |
| `footerSalesChannels` | OneToMany | `SalesChannelDefinition` |
| `serviceSalesChannels` | OneToMany | `SalesChannelDefinition` |
| `mainCategories` | OneToMany | `MainCategoryDefinition` |
| `seoUrls` | OneToMany | `SeoUrlDefinition` |

**Translated fields:** `breadcrumb`, `name`, `customFields`, `slotConfig`, `linkType`, `internalLink`, `externalLink`, `linkNewTab`, `description`, `metaTitle`, `metaDescription`, `keywords`

### `category_tag` [M]

**Class:** `CategoryTagDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `categoryId` | `category_id` | FkField | PrimaryKey |
| `CategoryDefinition::class` | `CategoryDefinition::class` | ReferenceVersionField | PrimaryKey |
| `tagId` | `tag_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `category` | ManyToOne | `CategoryDefinition` |
| `tag` | ManyToOne | `TagDefinition` |

### `category_translation` [T]

**Class:** `CategoryTranslationDefinition` | **Entity:** `CategoryTranslationEntity` | **Collection:** `CategoryTranslationCollection` | **Parent:** `CategoryDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |
| `` | `` | BreadcrumbField | ApiAware |
| `slotConfig` | `slot_config` | JsonField |  |
| `linkType` | `link_type` | StringField | ApiAware |
| `internalLink` | `internal_link` | IdField | ApiAware |
| `externalLink` | `external_link` | StringField | ApiAware |
| `linkNewTab` | `link_new_tab` | BoolField | ApiAware |
| `description` | `description` | LongTextField | ApiAware |
| `metaTitle` | `meta_title` | LongTextField | ApiAware |
| `metaDescription` | `meta_description` | LongTextField | ApiAware |
| `keywords` | `keywords` | LongTextField | ApiAware |
| `` | `` | CustomFields | ApiAware |

### `sales_channel_category` [E]

**Class:** `SalesChannelCategoryDefinition` | **Entity:** `SalesChannelCategoryEntity`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `seoUrl` | `seo_url` | StringField | ApiAware |


## Content/Flow

### `flow` [E]

**Class:** `FlowDefinition` | **Entity:** `FlowEntity` | **Collection:** `FlowCollection`

**Defaults:** `active=false`, `priority=1`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | Required |
| `eventName` | `event_name` | StringField | Required |
| `priority` | `priority` | IntField |  |
| `payload` | `payload` | BlobField | WriteProtected |
| `invalid` | `invalid` | BoolField | WriteProtected |
| `active` | `active` | BoolField |  |
| `description` | `description` | StringField |  |
| `` | `` | CustomFields |  |
| `appFlowEventId` | `app_flow_event_id` | FkField |  |

| Association | Type | Target |
|-------------|------|--------|
| `sequences` | OneToMany | `FlowSequenceDefinition` |
| `appFlowEvent` | ManyToOne | `AppFlowEventDefinition` |

### `flow_action` [E]

**Class:** `FlowActionDefinition`

### `flow_sequence` [E]

**Class:** `FlowSequenceDefinition` | **Entity:** `FlowSequenceEntity` | **Collection:** `FlowSequenceCollection` | **Parent:** `FlowDefinition`

**Defaults:** `trueCase=false`, `position=1`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `flowId` | `flow_id` | FkField | Required |
| `ruleId` | `rule_id` | FkField |  |
| `actionName` | `action_name` | StringField | SearchRanking |
| `config` | `config` | JsonField |  |
| `position` | `position` | IntField |  |
| `displayGroup` | `display_group` | IntField |  |
| `trueCase` | `true_case` | BoolField |  |
| `self::class` | `self::class` | ParentFkField |  |
| `` | `` | CustomFields |  |
| `appFlowActionId` | `app_flow_action_id` | FkField |  |

| Association | Type | Target |
|-------------|------|--------|
| `flow` | ManyToOne | `FlowDefinition` |
| `rule` | ManyToOne | `RuleDefinition` |
| `self::class` | ManyToOne | `` |
| `self::class` | OneToMany | `` |
| `appFlowAction` | ManyToOne | `AppFlowActionDefinition` |

### `flow_template` [E]

**Class:** `FlowTemplateDefinition` | **Entity:** `FlowTemplateEntity` | **Collection:** `FlowTemplateCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | Required |
| `config` | `config` | FlowTemplateConfigField |  |


## Content/ImportExport

### `6.2.0.0` [T]

**Class:** `ImportExportProfileTranslationDefinition` | **Entity:** `ImportExportProfileTranslationEntity` | **Collection:** `ImportExportProfileTranslationCollection` | **Parent:** `ImportExportProfileDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `label` | `label` | StringField |  |

### `import_export_file` [E]

**Class:** `ImportExportFileDefinition` | **Entity:** `ImportExportFileEntity`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `originalName` | `original_name` | StringField | Required |
| `path` | `path` | StringField | Required |
| `expireDate` | `expire_date` | DateTimeField | Required |
| `size` | `size` | IntField |  |
| `accessToken` | `access_token` | StringField |  |

| Association | Type | Target |
|-------------|------|--------|
| `log` | OneToOne | `ImportExportLogDefinition` |

### `import_export_log` [E]

**Class:** `ImportExportLogDefinition` | **Entity:** `ImportExportLogEntity`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `activity` | `activity` | StringField | Required |
| `state` | `state` | StringField | Required |
| `records` | `records` | IntField | Required |
| `userId` | `user_id` | FkField |  |
| `profileId` | `profile_id` | FkField |  |
| `fileId` | `file_id` | FkField |  |
| `invalidRecordsLogId` | `invalid_records_log_id` | FkField |  |
| `username` | `username` | StringField |  |
| `profileName` | `profile_name` | StringField |  |
| `config` | `config` | JsonField | Required |
| `result` | `result` | JsonField |  |

| Association | Type | Target |
|-------------|------|--------|
| `user` | ManyToOne | `UserDefinition` |
| `profile` | ManyToOne | `ImportExportProfileDefinition` |
| `file` | OneToOne | `ImportExportFileDefinition` |
| `invalidRecordsLog` | OneToOne | `ImportExportLogDefinition` |
| `failedImportLog` | OneToOne | `ImportExportLogDefinition` |

### `import_export_profile` [E]

**Class:** `ImportExportProfileDefinition` | **Entity:** `ImportExportProfileEntity`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `technicalName` | `technical_name` | StringField | Required |
| `label` | `` | TranslatedField | Required |
| `type` | `type` | StringField |  |
| `systemDefault` | `system_default` | BoolField |  |
| `sourceEntity` | `source_entity` | StringField | Required |
| `fileType` | `file_type` | StringField | Required |
| `delimiter` | `delimiter` | StringField | Required |
| `enclosure` | `enclosure` | StringField | Required |
| `mapping` | `mapping` | JsonField |  |
| `updateBy` | `update_by` | JsonField |  |
| `config` | `config` | JsonField |  |

| Association | Type | Target |
|-------------|------|--------|
| `importExportLogs` | OneToMany | `ImportExportLogDefinition` |
| `ImportExportProfileTranslationDefinition::class` | OneToMany | `ImportExportProfileTranslationDefinition` |

**Translated fields:** `label`


## Content/LandingPage

### `landing_page` [E]

**Class:** `LandingPageDefinition` | **Entity:** `LandingPageEntity` | **Collection:** `LandingPageCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `active` | `active` | BoolField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |
| `slotConfig` | `` | TranslatedField | ApiAware |
| `metaTitle` | `` | TranslatedField | ApiAware |
| `metaDescription` | `` | TranslatedField | ApiAware |
| `keywords` | `` | TranslatedField | ApiAware |
| `url` | `` | TranslatedField | ApiAware |
| `cmsPageId` | `cms_page_id` | FkField | ApiAware |
| `CmsPageDefinition::class` | `CmsPageDefinition::class` | ReferenceVersionField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `LandingPageTranslationDefinition::class` | OneToMany | `LandingPageTranslationDefinition` |
| `tags` | ManyToMany | `TagDefinition` |
| `cmsPage` | ManyToOne | `CmsPageDefinition` |
| `salesChannels` | ManyToMany | `SalesChannelDefinition` |
| `seoUrls` | OneToMany | `SeoUrlDefinition` |

**Translated fields:** `name`, `customFields`, `slotConfig`, `metaTitle`, `metaDescription`, `keywords`, `url`

### `landing_page_sales_channel` [M]

**Class:** `LandingPageSalesChannelDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `landingPageId` | `landing_page_id` | FkField | PrimaryKey |
| `LandingPageDefinition::class` | `LandingPageDefinition::class` | ReferenceVersionField | PrimaryKey |
| `salesChannelId` | `sales_channel_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `landingPage` | ManyToOne | `LandingPageDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |

### `landing_page_tag` [M]

**Class:** `LandingPageTagDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `landingPageId` | `landing_page_id` | FkField | PrimaryKey |
| `LandingPageDefinition::class` | `LandingPageDefinition::class` | ReferenceVersionField | PrimaryKey |
| `tagId` | `tag_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `landingPage` | ManyToOne | `LandingPageDefinition` |
| `tag` | ManyToOne | `TagDefinition` |

### `landing_page_translation` [T]

**Class:** `LandingPageTranslationDefinition` | **Entity:** `LandingPageTranslationEntity` | **Collection:** `LandingPageTranslationCollection` | **Parent:** `LandingPageDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |
| `url` | `url` | StringField | ApiAware |
| `slotConfig` | `slot_config` | JsonField | ApiAware |
| `metaTitle` | `meta_title` | LongTextField | ApiAware |
| `metaDescription` | `meta_description` | LongTextField | ApiAware |
| `keywords` | `keywords` | LongTextField | ApiAware |
| `` | `` | CustomFields | ApiAware |

### `sales_channel_landing_page` [E]

**Class:** `SalesChannelLandingPageDefinition`


## Content/MailTemplate

### `mail_header_footer` [E]

**Class:** `MailHeaderFooterDefinition` | **Entity:** `MailHeaderFooterEntity`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `systemDefault` | `system_default` | BoolField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `description` | `` | TranslatedField | ApiAware |
| `headerHtml` | `` | TranslatedField | ApiAware |
| `headerPlain` | `` | TranslatedField | ApiAware |
| `footerHtml` | `` | TranslatedField | ApiAware |
| `footerPlain` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `MailHeaderFooterTranslationDefinition::class` | OneToMany | `MailHeaderFooterTranslationDefinition` |
| `salesChannels` | OneToMany | `SalesChannelDefinition` |

**Translated fields:** `name`, `description`, `headerHtml`, `headerPlain`, `footerHtml`, `footerPlain`

### `mail_header_footer_translation` [T]

**Class:** `MailHeaderFooterTranslationDefinition` | **Entity:** `MailHeaderFooterTranslationEntity` | **Collection:** `MailHeaderFooterTranslationCollection` | **Parent:** `MailHeaderFooterDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | Required |
| `description` | `description` | StringField | ApiAware |
| `headerHtml` | `header_html` | LongTextField | ApiAware |
| `headerPlain` | `header_plain` | LongTextField | ApiAware |
| `footerHtml` | `footer_html` | LongTextField | ApiAware |
| `footerPlain` | `footer_plain` | LongTextField | ApiAware |

### `mail_template` [E]

**Class:** `MailTemplateDefinition` | **Entity:** `MailTemplateEntity` | **Collection:** `MailTemplateCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `mailTemplateTypeId` | `mail_template_type_id` | FkField | Required |
| `systemDefault` | `system_default` | BoolField | ApiAware |
| `` | `` | WasModifiedByUserField | ApiAware |
| `senderName` | `` | TranslatedField | ApiAware |
| `description` | `` | TranslatedField | SearchRanking |
| `subject` | `` | TranslatedField | SearchRanking |
| `contentHtml` | `` | TranslatedField | ApiAware |
| `contentPlain` | `` | TranslatedField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `MailTemplateTranslationDefinition::class` | OneToMany | `MailTemplateTranslationDefinition` |
| `mailTemplateType` | ManyToOne | `MailTemplateTypeDefinition` |
| `media` | OneToMany | `MailTemplateMediaDefinition` |

**Translated fields:** `senderName`, `description`, `subject`, `contentHtml`, `contentPlain`, `customFields`

### `mail_template_media` [M]

**Class:** `MailTemplateMediaDefinition` | **Entity:** `MailTemplateMediaEntity` | **Collection:** `MailTemplateMediaCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `mailTemplateId` | `mail_template_id` | FkField | ApiAware |
| `languageId` | `language_id` | FkField | ApiAware |
| `mediaId` | `media_id` | FkField | ApiAware |
| `position` | `position` | IntField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `mailTemplate` | ManyToOne | `MailTemplateDefinition` |
| `media` | ManyToOne | `MediaDefinition` |

### `mail_template_translation` [T]

**Class:** `MailTemplateTranslationDefinition` | **Entity:** `MailTemplateTranslationEntity` | **Collection:** `MailTemplateTranslationCollection` | **Parent:** `MailTemplateDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `senderName` | `sender_name` | StringField | ApiAware |
| `description` | `description` | LongTextField | ApiAware |
| `subject` | `subject` | StringField | Required |
| `contentHtml` | `content_html` | LongTextField | Required |
| `contentPlain` | `content_plain` | LongTextField | Required |
| `` | `` | CustomFields | ApiAware |

### `mail_template_type` [E]

**Class:** `MailTemplateTypeDefinition` | **Entity:** `MailTemplateTypeEntity` | **Collection:** `MailTemplateTypeCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `technicalName` | `technical_name` | StringField | ApiAware |
| `availableEntities` | `available_entities` | JsonField |  |
| `customFields` | `` | TranslatedField | ApiAware |
| `templateData` | `template_data` | JsonField | Deprecated |

| Association | Type | Target |
|-------------|------|--------|
| `MailTemplateTypeTranslationDefinition::class` | OneToMany | `MailTemplateTypeTranslationDefinition` |
| `mailTemplates` | OneToMany | `MailTemplateDefinition` |

**Translated fields:** `name`, `customFields`

### `mail_template_type_translation` [T]

**Class:** `MailTemplateTypeTranslationDefinition` | **Entity:** `MailTemplateTypeTranslationEntity` | **Collection:** `MailTemplateTypeTranslationCollection` | **Parent:** `MailTemplateTypeDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | Required |
| `` | `` | CustomFields | ApiAware |


## Content/Media

### `media` [E]

**Class:** `MediaDefinition` | **Entity:** `MediaEntity` | **Collection:** `MediaCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `userId` | `user_id` | FkField |  |
| `mediaFolderId` | `media_folder_id` | FkField |  |
| `mimeType` | `mime_type` | StringField | ApiAware |
| `fileExtension` | `file_extension` | StringField | ApiAware |
| `uploadedAt` | `uploaded_at` | DateTimeField | ApiAware |
| `fileName` | `file_name` | LongTextField | ApiAware |
| `fileSize` | `file_size` | IntField | ApiAware |
| `mediaTypeRaw` | `media_type` | BlobField | WriteProtected |
| `metaData` | `meta_data` | JsonField | ApiAware |
| `mediaType` | `media_type` | JsonField | WriteProtected |
| `config` | `config` | JsonField | ApiAware |
| `alt` | `` | TranslatedField | ApiAware |
| `title` | `` | TranslatedField | ApiAware |
| `url` | `url` | StringField | ApiAware |
| `path` | `path` | StringField | ApiAware |
| `hasFile` | `has_file` | BoolField | ApiAware |
| `private` | `private` | BoolField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |
| `thumbnailsRo` | `thumbnails_ro` | BlobField | Computed |
| `fileHash` | `file_hash` | StringField | Computed |

| Association | Type | Target |
|-------------|------|--------|
| `MediaTranslationDefinition::class` | OneToMany | `MediaTranslationDefinition` |
| `tags` | ManyToMany | `TagDefinition` |
| `thumbnails` | OneToMany | `MediaThumbnailDefinition` |
| `user` | ManyToOne | `UserDefinition` |
| `categories` | OneToMany | `CategoryDefinition` |
| `productManufacturers` | OneToMany | `ProductManufacturerDefinition` |
| `productMedia` | OneToMany | `ProductMediaDefinition` |
| `productDownloads` | OneToMany | `ProductDownloadDefinition` |
| `orderLineItemDownloads` | OneToMany | `OrderLineItemDownloadDefinition` |
| `avatarUsers` | OneToMany | `UserDefinition` |
| `mediaFolder` | ManyToOne | `MediaFolderDefinition` |
| `propertyGroupOptions` | OneToMany | `PropertyGroupOptionDefinition` |
| `mailTemplateMedia` | OneToMany | `MailTemplateMediaDefinition` |
| `documentBaseConfigs` | OneToMany | `DocumentBaseConfigDefinition` |
| `shippingMethods` | OneToMany | `ShippingMethodDefinition` |
| `paymentMethods` | OneToMany | `PaymentMethodDefinition` |
| `productConfiguratorSettings` | OneToMany | `ProductConfiguratorSettingDefinition` |
| `productOpenGraphImages` | OneToMany | `ProductDefinition` |
| `orderLineItems` | OneToMany | `OrderLineItemDefinition` |
| `cmsBlocks` | OneToMany | `CmsBlockDefinition` |
| `cmsSections` | OneToMany | `CmsSectionDefinition` |
| `cmsPages` | OneToMany | `CmsPageDefinition` |
| `documents` | OneToMany | `DocumentDefinition` |
| `a11yDocuments` | OneToMany | `DocumentDefinition` |
| `appPaymentMethods` | OneToMany | `AppPaymentMethodDefinition` |
| `appShippingMethods` | OneToMany | `AppShippingMethodDefinition` |
| `documentFile` | OneToOne | `DocumentFileDefinition` |

**Translated fields:** `alt`, `title`, `customFields`

### `media_default_folder` [E]

**Class:** `MediaDefaultFolderDefinition` | **Entity:** `MediaDefaultFolderEntity` | **Collection:** `MediaDefaultFolderCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `entity` | `entity` | StringField | Required |
| `` | `` | CustomFields |  |

| Association | Type | Target |
|-------------|------|--------|
| `folder` | OneToOne | `MediaFolderDefinition` |

### `media_folder` [E]

**Class:** `MediaFolderDefinition` | **Entity:** `MediaFolderEntity` | **Collection:** `MediaFolderCollection`

**Defaults:** `useParentConfiguration=true`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `useParentConfiguration` | `use_parent_configuration` | BoolField |  |
| `configurationId` | `media_folder_configuration_id` | FkField | Required |
| `defaultFolderId` | `default_folder_id` | FkField |  |
| `self::class` | `self::class` | ParentFkField |  |
| `` | `` | ChildCountField |  |
| `path` | `path` | TreePathField |  |
| `name` | `name` | StringField | SearchRanking |
| `` | `` | CustomFields |  |

| Association | Type | Target |
|-------------|------|--------|
| `self::class` | ManyToOne | `` |
| `self::class` | OneToMany | `` |
| `media` | OneToMany | `MediaDefinition` |
| `defaultFolder` | OneToOne | `MediaDefaultFolderDefinition` |
| `configuration` | ManyToOne | `MediaFolderConfigurationDefinition` |

### `media_folder_configuration` [E]

**Class:** `MediaFolderConfigurationDefinition` | **Entity:** `MediaFolderConfigurationEntity` | **Collection:** `MediaFolderConfigurationCollection`

**Defaults:** `createThumbnails=true`, `keepAspectRatio=true`, `thumbnailQuality=80`, `private=false`, `noAssociation=false`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `createThumbnails` | `create_thumbnails` | BoolField |  |
| `keepAspectRatio` | `keep_aspect_ratio` | BoolField |  |
| `thumbnailQuality` | `thumbnail_quality` | IntField |  |
| `private` | `private` | BoolField |  |
| `noAssociation` | `no_association` | BoolField |  |
| `mediaThumbnailSizesRo` | `media_thumbnail_sizes_ro` | BlobField | Computed |
| `` | `` | CustomFields |  |

| Association | Type | Target |
|-------------|------|--------|
| `mediaFolders` | OneToMany | `MediaFolderDefinition` |
| `mediaThumbnailSizes` | ManyToMany | `MediaThumbnailSizeDefinition` |

### `media_folder_configuration_media_thumbnail_size` [M]

**Class:** `MediaFolderConfigurationMediaThumbnailSizeDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `mediaFolderConfigurationId` | `media_folder_configuration_id` | FkField | PrimaryKey |
| `mediaThumbnailSizeId` | `media_thumbnail_size_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `mediaFolderConfiguration` | ManyToOne | `MediaFolderConfigurationDefinition` |
| `mediaThumbnailSize` | ManyToOne | `MediaThumbnailSizeDefinition` |

### `media_tag` [M]

**Class:** `MediaTagDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `mediaId` | `media_id` | FkField | ApiAware |
| `tagId` | `tag_id` | FkField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `media` | ManyToOne | `MediaDefinition` |
| `tag` | ManyToOne | `TagDefinition` |

### `media_thumbnail` [E]

**Class:** `MediaThumbnailDefinition` | **Entity:** `MediaThumbnailEntity` | **Collection:** `MediaThumbnailCollection` | **Parent:** `MediaDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `mediaId` | `media_id` | FkField | ApiAware |
| `mediaThumbnailSizeId` | `media_thumbnail_size_id` | FkField | ApiAware |
| `width` | `width` | IntField | ApiAware |
| `height` | `height` | IntField | ApiAware |
| `url` | `url` | StringField | ApiAware |
| `path` | `path` | StringField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `media` | ManyToOne | `MediaDefinition` |
| `mediaThumbnailSize` | ManyToOne | `MediaThumbnailSizeDefinition` |

### `media_thumbnail_size` [E]

**Class:** `MediaThumbnailSizeDefinition` | **Entity:** `MediaThumbnailSizeEntity` | **Collection:** `MediaThumbnailSizeCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `width` | `width` | IntField | ApiAware |
| `height` | `height` | IntField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `mediaFolderConfigurations` | ManyToMany | `MediaFolderConfigurationDefinition` |
| `mediaThumbnails` | OneToMany | `MediaThumbnailDefinition` |

### `media_translation` [T]

**Class:** `MediaTranslationDefinition` | **Entity:** `MediaTranslationEntity` | **Collection:** `MediaTranslationCollection` | **Parent:** `MediaDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `title` | `title` | StringField | ApiAware |
| `alt` | `alt` | LongTextField | ApiAware |
| `` | `` | CustomFields | ApiAware |


## Content/Newsletter

### `newsletter_recipient` [E]

**Class:** `NewsletterRecipientDefinition` | **Entity:** `NewsletterRecipientEntity` | **Collection:** `NewsletterRecipientCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `email` | `email` | StringField | Required |
| `title` | `title` | StringField |  |
| `firstName` | `first_name` | StringField |  |
| `lastName` | `last_name` | StringField |  |
| `zipCode` | `zip_code` | StringField |  |
| `city` | `city` | StringField |  |
| `street` | `street` | StringField |  |
| `status` | `status` | StringField | Required |
| `hash` | `hash` | StringField | Required |
| `` | `` | CustomFields |  |
| `confirmedAt` | `confirmed_at` | DateTimeField |  |
| `salutationId` | `salutation_id` | FkField |  |
| `languageId` | `language_id` | FkField | Required |
| `salesChannelId` | `sales_channel_id` | FkField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `tags` | ManyToMany | `TagDefinition` |
| `salutation` | ManyToOne | `SalutationDefinition` |
| `language` | ManyToOne | `LanguageDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |

### `newsletter_recipient_tag` [M]

**Class:** `NewsletterRecipientTagDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `newsletterRecipientId` | `newsletter_recipient_id` | FkField | PrimaryKey |
| `tagId` | `tag_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `newsletterRecipient` | ManyToOne | `NewsletterRecipientDefinition` |
| `tag` | ManyToOne | `TagDefinition` |

### `sales_channel_newsletter_recipient` [E]

**Class:** `SalesChannelNewsletterRecipientDefinition`


## Content/Product

### `6.3.0.0` [T]

**Class:** `ProductFeatureSetTranslationDefinition` | **Entity:** `ProductFeatureSetTranslationEntity` | **Collection:** `ProductFeatureSetTranslationCollection` | **Parent:** `ProductFeatureSetDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | Required |
| `description` | `description` | StringField | ApiAware |

### `product` [E]

**Class:** `ProductDefinition` | **Entity:** `ProductEntity` | **Collection:** `ProductCollection`

**Defaults:** `isCloseout=false`, `minPurchase=1`, `purchaseSteps=1`, `shippingFree=false`, `restockTime=null`, `active=true`, `markAsTopseller=false`, `type="physical"`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `self::class` | `self::class` | ParentFkField | ApiAware |
| `parent_version_id` | `self::class` | ReferenceVersionField | ApiAware |
| `manufacturerId` | `product_manufacturer_id` | FkField | ApiAware |
| `ProductManufacturerDefinition::class` | `ProductManufacturerDefinition::class` | ReferenceVersionField | ApiAware |
| `unitId` | `unit_id` | FkField | ApiAware |
| `taxId` | `tax_id` | FkField | ApiAware |
| `coverId` | `product_media_id` | FkField | ApiAware |
| `ProductMediaDefinition::class` | `ProductMediaDefinition::class` | ReferenceVersionField | ApiAware |
| `deliveryTimeId` | `delivery_time_id` | FkField | ApiAware |
| `featureSetId` | `product_feature_set_id` | FkField | Inherited |
| `canonicalProductId` | `canonical_product_id` | FkField | ApiAware |
| `canonical_product_version_id` | `self::class` | ReferenceVersionField | ApiAware |
| `cmsPageId` | `cms_page_id` | FkField | ApiAware |
| `CmsPageDefinition::class` | `CmsPageDefinition::class` | ReferenceVersionField | Inherited |
| `openGraphMediaId` | `open_graph_media_id` | FkField | ApiAware |
| `price` | `price` | PriceField | Inherited |
| `productNumber` | `product_number` | NumberRangeField | ApiAware |
| `restockTime` | `restock_time` | IntField | ApiAware |
| `` | `` | AutoIncrementField |  |
| `active` | `active` | BoolField | ApiAware |
| `available` | `available` | BoolField | ApiAware |
| `isCloseout` | `is_closeout` | BoolField | ApiAware |
| `availableStock` | `available_stock` | IntField | ApiAware |
| `stock` | `stock` | IntField | ApiAware |
| `variation` | `variation` | ListField | Runtime |
| `displayGroup` | `display_group` | StringField | ApiAware |
| `variantListingConfig` | `variant_listing_config` | VariantListingConfigField | Inherited |
| `variantRestrictions` | `variant_restrictions` | JsonField |  |
| `manufacturerNumber` | `manufacturer_number` | StringField | ApiAware |
| `ean` | `ean` | StringField | ApiAware |
| `purchaseSteps` | `purchase_steps` | IntField | ApiAware |
| `maxPurchase` | `max_purchase` | IntField | ApiAware |
| `minPurchase` | `min_purchase` | IntField | ApiAware |
| `purchaseUnit` | `purchase_unit` | FloatField | ApiAware |
| `referenceUnit` | `reference_unit` | FloatField | ApiAware |
| `shippingFree` | `shipping_free` | BoolField | ApiAware |
| `purchasePrices` | `purchase_prices` | PriceField | Inherited |
| `markAsTopseller` | `mark_as_topseller` | BoolField | ApiAware |
| `weight` | `weight` | FloatField | ApiAware |
| `width` | `width` | FloatField | ApiAware |
| `height` | `height` | FloatField | ApiAware |
| `length` | `length` | FloatField | ApiAware |
| `releaseDate` | `release_date` | DateTimeField | ApiAware |
| `ratingAverage` | `rating_average` | FloatField | ApiAware |
| `categoryTree` | `category_tree` | ListField | ApiAware |
| `propertyIds` | `property_ids` | ManyToManyIdField | ApiAware |
| `optionIds` | `option_ids` | ManyToManyIdField | ApiAware |
| `streamIds` | `stream_ids` | ManyToManyIdField | ApiAware |
| `tagIds` | `tag_ids` | ManyToManyIdField | Inherited |
| `categoryIds` | `category_ids` | ManyToManyIdField | ApiAware |
| `` | `` | ChildCountField | ApiAware |
| `customFieldSetSelectionActive` | `custom_field_set_selection_active` | BoolField | Inherited |
| `sales` | `sales` | IntField | ApiAware |
| `metaDescription` | `` | TranslatedField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `keywords` | `` | TranslatedField | ApiAware |
| `description` | `` | TranslatedField | ApiAware |
| `descriptionTeaser` | `` | TranslatedField | ApiAware |
| `metaTitle` | `` | TranslatedField | ApiAware |
| `packUnit` | `` | TranslatedField | ApiAware |
| `packUnitPlural` | `` | TranslatedField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |
| `slotConfig` | `` | TranslatedField | Inherited |
| `customSearchKeywords` | `` | TranslatedField | Inherited |
| `ogTitle` | `` | TranslatedField | ApiAware |
| `ogDescription` | `` | TranslatedField | ApiAware |
| `type` | `type` | StringField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `downloads` | OneToMany | `ProductDownloadDefinition` |
| `self::class` | ManyToOne | `` |
| `self::class` | OneToMany | `` |
| `deliveryTime` | ManyToOne | `DeliveryTimeDefinition` |
| `tax` | ManyToOne | `TaxDefinition` |
| `manufacturer` | ManyToOne | `ProductManufacturerDefinition` |
| `unit` | ManyToOne | `UnitDefinition` |
| `cover` | ManyToOne | `ProductMediaDefinition` |
| `openGraphMedia` | ManyToOne | `MediaDefinition` |
| `featureSet` | ManyToOne | `ProductFeatureSetDefinition` |
| `cmsPage` | ManyToOne | `CmsPageDefinition` |
| `canonicalProduct` | ManyToOne | `ProductDefinition` |
| `prices` | OneToMany | `ProductPriceDefinition` |
| `media` | OneToMany | `ProductMediaDefinition` |
| `crossSellings` | OneToMany | `ProductCrossSellingDefinition` |
| `crossSellingAssignedProducts` | OneToMany | `ProductCrossSellingAssignedProductsDefinition` |
| `configuratorSettings` | OneToMany | `ProductConfiguratorSettingDefinition` |
| `visibilities` | OneToMany | `ProductVisibilityDefinition` |
| `searchKeywords` | OneToMany | `ProductSearchKeywordDefinition` |
| `productReviews` | OneToMany | `ProductReviewDefinition` |
| `mainCategories` | OneToMany | `MainCategoryDefinition` |
| `seoUrls` | OneToMany | `SeoUrlDefinition` |
| `orderLineItems` | OneToMany | `OrderLineItemDefinition` |
| `wishlists` | OneToMany | `CustomerWishlistProductDefinition` |
| `options` | ManyToMany | `PropertyGroupOptionDefinition` |
| `properties` | ManyToMany | `PropertyGroupOptionDefinition` |
| `categories` | ManyToMany | `CategoryDefinition` |
| `streams` | ManyToMany | `ProductStreamDefinition` |
| `categoriesRo` | ManyToMany | `CategoryDefinition` |
| `tags` | ManyToMany | `TagDefinition` |
| `customFieldSets` | ManyToMany | `CustomFieldSetDefinition` |
| `ProductTranslationDefinition::class` | OneToMany | `ProductTranslationDefinition` |

**Translated fields:** `metaDescription`, `name`, `keywords`, `description`, `descriptionTeaser`, `metaTitle`, `packUnit`, `packUnitPlural`, `customFields`, `slotConfig`, `customSearchKeywords`, `ogTitle`, `ogDescription`

### `product_category` [M]

**Class:** `ProductCategoryDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `productId` | `product_id` | FkField | PrimaryKey |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | PrimaryKey |
| `categoryId` | `category_id` | FkField | PrimaryKey |
| `CategoryDefinition::class` | `CategoryDefinition::class` | ReferenceVersionField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `category` | ManyToOne | `CategoryDefinition` |

### `product_category_tree` [M]

**Class:** `ProductCategoryTreeDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `productId` | `product_id` | FkField | PrimaryKey |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | PrimaryKey |
| `categoryId` | `category_id` | FkField | PrimaryKey |
| `CategoryDefinition::class` | `CategoryDefinition::class` | ReferenceVersionField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `category` | ManyToOne | `CategoryDefinition` |

### `product_configurator_setting` [E]

**Class:** `ProductConfiguratorSettingDefinition` | **Entity:** `ProductConfiguratorSettingEntity` | **Collection:** `ProductConfiguratorSettingCollection` | **Parent:** `ProductDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `productId` | `product_id` | FkField | ApiAware |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | ApiAware |
| `mediaId` | `media_id` | FkField | ApiAware |
| `optionId` | `property_group_option_id` | FkField | ApiAware |
| `price` | `price` | JsonField |  |
| `position` | `position` | IntField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `media` | ManyToOne | `MediaDefinition` |
| `option` | ManyToOne | `PropertyGroupOptionDefinition` |

### `product_cross_selling` [E]

**Class:** `ProductCrossSellingDefinition` | **Entity:** `ProductCrossSellingEntity` | **Collection:** `ProductCrossSellingCollection` | **Parent:** `ProductDefinition`

**Defaults:** `position=0`, `sortBy="cheapestPrice"`, `sortDirection="FieldSorting::ASCENDING"`, `type="productStream"`, `active=false`, `limit=24`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `position` | `position` | IntField | ApiAware |
| `sortBy` | `sort_by` | StringField | ApiAware |
| `sortDirection` | `sort_direction` | StringField | ApiAware |
| `type` | `type` | StringField | ApiAware |
| `active` | `active` | BoolField | ApiAware |
| `limit` | `limit` | IntField | ApiAware |
| `productId` | `product_id` | FkField | Required |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | Required |
| `productStreamId` | `product_stream_id` | FkField |  |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `productStream` | ManyToOne | `ProductStreamDefinition` |
| `assignedProducts` | OneToMany | `ProductCrossSellingAssignedProductsDefinition` |
| `ProductCrossSellingTranslationDefinition::class` | OneToMany | `ProductCrossSellingTranslationDefinition` |

**Translated fields:** `name`

### `product_cross_selling_assigned_products` [E]

**Class:** `ProductCrossSellingAssignedProductsDefinition` | **Entity:** `ProductCrossSellingAssignedProductsEntity` | **Collection:** `ProductCrossSellingAssignedProductsCollection` | **Parent:** `ProductCrossSellingDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `crossSellingId` | `cross_selling_id` | FkField | Required |
| `productId` | `product_id` | FkField | Required |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | Required |
| `position` | `position` | IntField |  |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `crossSelling` | ManyToOne | `ProductCrossSellingDefinition` |

### `product_cross_selling_translation` [T]

**Class:** `ProductCrossSellingTranslationDefinition` | **Entity:** `ProductCrossSellingTranslationEntity` | **Collection:** `ProductCrossSellingTranslationCollection` | **Parent:** `ProductCrossSellingDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |

### `product_custom_field_set` [M]

**Class:** `ProductCustomFieldSetDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `productId` | `product_id` | FkField | PrimaryKey |
| `customFieldSetId` | `custom_field_set_id` | FkField | PrimaryKey |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `customFieldSet` | ManyToOne | `CustomFieldSetDefinition` |

### `product_download` [E]

**Class:** `ProductDownloadDefinition` | **Entity:** `ProductDownloadEntity` | **Collection:** `ProductDownloadCollection` | **Parent:** `ProductDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `productId` | `product_id` | FkField | ApiAware |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | ApiAware |
| `mediaId` | `media_id` | FkField | ApiAware |
| `position` | `position` | IntField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `media` | ManyToOne | `MediaDefinition` |

### `product_export` [E]

**Class:** `ProductExportDefinition` | **Entity:** `ProductExportEntity` | **Collection:** `ProductExportCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `productStreamId` | `product_stream_id` | FkField | Required |
| `storefrontSalesChannelId` | `storefront_sales_channel_id` | FkField | Required |
| `salesChannelId` | `sales_channel_id` | FkField | Required |
| `salesChannelDomainId` | `sales_channel_domain_id` | FkField | Required |
| `currencyId` | `currency_id` | FkField | Required |
| `fileName` | `file_name` | StringField | Required |
| `accessKey` | `access_key` | StringField | Required |
| `encoding` | `encoding` | StringField | Required |
| `fileFormat` | `file_format` | StringField | Required |
| `provider` | `provider` | StringField |  |
| `feedLabel` | `feed_label` | StringField |  |
| `includeVariants` | `include_variants` | BoolField |  |
| `generateByCronjob` | `generate_by_cronjob` | BoolField | Required |
| `generatedAt` | `generated_at` | DateTimeField |  |
| `interval` | `interval` | IntField | Required |
| `headerTemplate` | `header_template` | LongTextField | AllowHtml |
| `bodyTemplate` | `body_template` | LongTextField | AllowHtml |
| `footerTemplate` | `footer_template` | LongTextField | AllowHtml |
| `pausedSchedule` | `paused_schedule` | BoolField |  |
| `isRunning` | `is_running` | BoolField |  |

| Association | Type | Target |
|-------------|------|--------|
| `productStream` | ManyToOne | `ProductStreamDefinition` |
| `storefrontSalesChannel` | ManyToOne | `SalesChannelDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |
| `salesChannelDomain` | ManyToOne | `SalesChannelDomainDefinition` |
| `currency` | ManyToOne | `CurrencyDefinition` |

### `product_feature_set` [E]

**Class:** `ProductFeatureSetDefinition` | **Entity:** `ProductFeatureSetEntity` | **Collection:** `ProductFeatureSetCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `` | TranslatedField |  |
| `description` | `` | TranslatedField |  |
| `features` | `features` | JsonField |  |

| Association | Type | Target |
|-------------|------|--------|
| `products` | OneToMany | `ProductDefinition` |
| `ProductFeatureSetTranslationDefinition::class` | OneToMany | `ProductFeatureSetTranslationDefinition` |

**Translated fields:** `name`, `description`

### `product_keyword_dictionary` [E]

**Class:** `ProductKeywordDictionaryDefinition` | **Entity:** `ProductKeywordDictionaryEntity` | **Collection:** `ProductKeywordDictionaryCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `languageId` | `language_id` | FkField | PrimaryKey |
| `keyword` | `keyword` | StringField | ApiAware |
| `reversed` | `reversed` | StringField | Computed |

| Association | Type | Target |
|-------------|------|--------|
| `language` | ManyToOne | `LanguageDefinition` |

### `product_manufacturer` [E]

**Class:** `ProductManufacturerDefinition` | **Entity:** `ProductManufacturerEntity` | **Collection:** `ProductManufacturerCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `mediaId` | `media_id` | FkField | ApiAware |
| `link` | `` | TranslatedField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `description` | `` | TranslatedField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `media` | ManyToOne | `MediaDefinition` |
| `products` | OneToMany | `ProductDefinition` |
| `ProductManufacturerTranslationDefinition::class` | OneToMany | `ProductManufacturerTranslationDefinition` |

**Translated fields:** `link`, `name`, `description`, `customFields`

### `product_manufacturer_translation` [T]

**Class:** `ProductManufacturerTranslationDefinition` | **Entity:** `ProductManufacturerTranslationEntity` | **Collection:** `ProductManufacturerTranslationCollection` | **Parent:** `ProductManufacturerDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |
| `link` | `link` | LongTextField | ApiAware |
| `description` | `description` | LongTextField | ApiAware |
| `` | `` | CustomFields | ApiAware |

### `product_media` [E]

**Class:** `ProductMediaDefinition` | **Entity:** `ProductMediaEntity` | **Collection:** `ProductMediaCollection` | **Parent:** `ProductDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `productId` | `product_id` | FkField | ApiAware |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | ApiAware |
| `mediaId` | `media_id` | FkField | ApiAware |
| `position` | `position` | IntField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `media` | ManyToOne | `MediaDefinition` |
| `coverProducts` | OneToMany | `ProductDefinition` |

### `product_option` [M]

**Class:** `ProductOptionDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `productId` | `product_id` | FkField | PrimaryKey |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | PrimaryKey |
| `optionId` | `property_group_option_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `option` | ManyToOne | `PropertyGroupOptionDefinition` |

### `product_price` [E]

**Class:** `ProductPriceDefinition` | **Entity:** `ProductPriceEntity` | **Collection:** `ProductPriceCollection` | **Parent:** `ProductDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `` | `` | VersionField |  |
| `productId` | `product_id` | FkField | Required |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | Required |
| `ruleId` | `rule_id` | FkField | Required |
| `price` | `price` | PriceField | Required |
| `` | `` | CustomFields |  |
| `quantityStart` | `quantity_start` | IntField | Required |
| `quantityEnd` | `quantity_end` | IntField |  |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `rule` | ManyToOne | `RuleDefinition` |

### `product_property` [M]

**Class:** `ProductPropertyDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `productId` | `product_id` | FkField | PrimaryKey |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | PrimaryKey |
| `optionId` | `property_group_option_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `option` | ManyToOne | `PropertyGroupOptionDefinition` |

### `product_review` [E]

**Class:** `ProductReviewDefinition` | **Entity:** `ProductReviewEntity` | **Collection:** `ProductReviewCollection` | **Parent:** `ProductDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `productId` | `product_id` | FkField | ApiAware |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | ApiAware |
| `customerId` | `customer_id` | FkField |  |
| `salesChannelId` | `sales_channel_id` | FkField | ApiAware |
| `languageId` | `language_id` | FkField | ApiAware |
| `externalUser` | `external_user` | StringField | ApiAware |
| `externalEmail` | `external_email` | StringField | SearchRanking |
| `title` | `title` | StringField | ApiAware |
| `content` | `content` | LongTextField | ApiAware |
| `points` | `points` | FloatField | ApiAware |
| `status` | `status` | BoolField | ApiAware |
| `comment` | `comment` | LongTextField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `customer` | ManyToOne | `CustomerDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |
| `language` | ManyToOne | `LanguageDefinition` |

### `product_search_config` [E]

**Class:** `ProductSearchConfigDefinition` | **Entity:** `ProductSearchConfigEntity` | **Collection:** `ProductSearchConfigCollection`

**Defaults:** `andLogic=true`, `minSearchLength=2`, `excludedTerms="["`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `languageId` | `language_id` | FkField | Required |
| `andLogic` | `and_logic` | BoolField | Required |
| `minSearchLength` | `min_search_length` | IntField | Required |
| `excludedTerms` | `excluded_terms` | ListField |  |

| Association | Type | Target |
|-------------|------|--------|
| `language` | OneToOne | `LanguageDefinition` |
| `configFields` | OneToMany | `ProductSearchConfigFieldDefinition` |

### `product_search_config_field` [E]

**Class:** `ProductSearchConfigFieldDefinition` | **Entity:** `ProductSearchConfigFieldEntity` | **Collection:** `ProductSearchConfigFieldCollection` | **Parent:** `ProductSearchConfigDefinition`

**Defaults:** `tokenize=false`, `searchable=false`, `useExactSubfield=false`, `ranking=0`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `searchConfigId` | `product_search_config_id` | FkField | Required |
| `customFieldId` | `custom_field_id` | FkField |  |
| `field` | `field` | StringField | Required |
| `tokenize` | `tokenize` | BoolField | Required |
| `searchable` | `searchable` | BoolField | Required |
| `useExactSubfield` | `use_exact_subfield` | BoolField | Required |
| `ranking` | `ranking` | IntField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `searchConfig` | ManyToOne | `ProductSearchConfigDefinition` |
| `customField` | ManyToOne | `CustomFieldDefinition` |

### `product_search_keyword` [E]

**Class:** `ProductSearchKeywordDefinition` | **Entity:** `ProductSearchKeywordEntity` | **Collection:** `ProductSearchKeywordCollection` | **Parent:** `ProductDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `` | `` | VersionField |  |
| `languageId` | `language_id` | FkField | PrimaryKey |
| `productId` | `product_id` | FkField | Required |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | Required |
| `keyword` | `keyword` | StringField | Required |
| `ranking` | `ranking` | FloatField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `language` | ManyToOne | `LanguageDefinition` |

### `product_sorting` [E]

**Class:** `ProductSortingDefinition` | **Entity:** `ProductSortingEntity` | **Collection:** `ProductSortingCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `` | `` | LockedField |  |
| `key` | `url_key` | StringField | ApiAware |
| `priority` | `priority` | IntField | ApiAware |
| `active` | `active` | BoolField | Required |
| `fields` | `fields` | JsonField | Required |
| `label` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `ProductSortingTranslationDefinition::class` | OneToMany | `ProductSortingTranslationDefinition` |

**Translated fields:** `label`

### `product_sorting_translation` [T]

**Class:** `ProductSortingTranslationDefinition` | **Entity:** `ProductSortingTranslationEntity` | **Collection:** `ProductSortingTranslationCollection` | **Parent:** `ProductSortingDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `label` | `label` | StringField | ApiAware |

### `product_stream` [E]

**Class:** `ProductStreamDefinition` | **Entity:** `ProductStreamEntity` | **Collection:** `ProductStreamCollection`

**Defaults:** `internal=false`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `apiFilter` | `api_filter` | JsonField | WriteProtected |
| `invalid` | `invalid` | BoolField | WriteProtected |
| `name` | `` | TranslatedField | ApiAware |
| `description` | `` | TranslatedField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |
| `internal` | `internal` | BoolField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `ProductStreamTranslationDefinition::class` | OneToMany | `ProductStreamTranslationDefinition` |
| `filters` | OneToMany | `ProductStreamFilterDefinition` |
| `productCrossSellings` | OneToMany | `ProductCrossSellingDefinition` |
| `productExports` | OneToMany | `ProductExportDefinition` |
| `categories` | OneToMany | `CategoryDefinition` |
| `products` | ManyToMany | `ProductDefinition` |

**Translated fields:** `name`, `description`, `customFields`

### `product_stream_filter` [E]

**Class:** `ProductStreamFilterDefinition` | **Entity:** `ProductStreamFilterEntity` | **Collection:** `ProductStreamFilterCollection` | **Parent:** `ProductStreamDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `productStreamId` | `product_stream_id` | FkField | Required |
| `self::class` | `self::class` | ParentFkField |  |
| `type` | `type` | StringField | Required |
| `field` | `field` | StringField |  |
| `operator` | `operator` | StringField |  |
| `value` | `value` | LongTextField |  |
| `parameters` | `parameters` | JsonField |  |
| `position` | `position` | IntField |  |
| `` | `` | CustomFields |  |

| Association | Type | Target |
|-------------|------|--------|
| `productStream` | ManyToOne | `ProductStreamDefinition` |
| `self::class` | ManyToOne | `` |
| `self::class` | OneToMany | `` |

### `product_stream_mapping` [M]

**Class:** `ProductStreamMappingDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `productId` | `product_id` | FkField | PrimaryKey |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | PrimaryKey |
| `productStreamId` | `product_stream_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `productStream` | ManyToOne | `ProductStreamDefinition` |

### `product_stream_translation` [T]

**Class:** `ProductStreamTranslationDefinition` | **Entity:** `ProductStreamTranslationEntity` | **Collection:** `ProductStreamTranslationCollection` | **Parent:** `ProductStreamDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |
| `description` | `description` | LongTextField | ApiAware |
| `` | `` | CustomFields | ApiAware |

### `product_tag` [M]

**Class:** `ProductTagDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `productId` | `product_id` | FkField | PrimaryKey |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | PrimaryKey |
| `tagId` | `tag_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `tag` | ManyToOne | `TagDefinition` |

### `product_translation` [T]

**Class:** `ProductTranslationDefinition` | **Entity:** `ProductTranslationEntity` | **Collection:** `ProductTranslationCollection` | **Parent:** `ProductDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `metaDescription` | `meta_description` | StringField | ApiAware |
| `name` | `name` | StringField | ApiAware |
| `keywords` | `keywords` | LongTextField | ApiAware |
| `description` | `description` | LongTextField | ApiAware |
| `descriptionTeaser` | `description_teaser` | StringField | ApiAware |
| `metaTitle` | `meta_title` | StringField | ApiAware |
| `packUnit` | `pack_unit` | StringField | ApiAware |
| `packUnitPlural` | `pack_unit_plural` | StringField | ApiAware |
| `customSearchKeywords` | `custom_search_keywords` | ListField |  |
| `slotConfig` | `slot_config` | JsonField | ApiAware |
| `ogTitle` | `og_title` | StringField | ApiAware |
| `ogDescription` | `og_description` | StringField | ApiAware |
| `` | `` | CustomFields | ApiAware |

### `product_visibility` [E]

**Class:** `ProductVisibilityDefinition` | **Entity:** `ProductVisibilityEntity` | **Collection:** `ProductVisibilityCollection` | **Parent:** `ProductDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | Required |
| `productId` | `product_id` | FkField | Required |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | Required |
| `salesChannelId` | `sales_channel_id` | FkField | Required |
| `visibility` | `visibility` | IntField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |
| `product` | ManyToOne | `ProductDefinition` |

### `sales_channel_product` [E]

**Class:** `SalesChannelProductDefinition` | **Entity:** `SalesChannelProductEntity` | **Collection:** `SalesChannelProductCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `calculatedPrice` | `calculated_price` | JsonField | ApiAware |
| `calculatedPrices` | `calculated_prices` | ListField | ApiAware |
| `calculatedMaxPurchase` | `calculated_max_purchase` | IntField | ApiAware |
| `calculatedCheapestPrice` | `calculated_cheapest_price` | JsonField | ApiAware |
| `isNew` | `is_new` | BoolField | ApiAware |
| `cheapestPrice` | `cheapest_price` | CheapestPriceField | WriteProtected |
| `cheapestPriceContainer` | `cheapest_price_container` | ObjectField | Runtime |
| `sortedProperties` | `sortedProperties` | ObjectField | Runtime |
| `measurements` | `measurements` | ObjectField | Runtime |

| Association | Type | Target |
|-------------|------|--------|
| `seoCategory` | OneToOne | `CategoryDefinition` |

### `sales_channel_tracking_customer` [E]

**Class:** `SalesChannelTrackingCustomerDefinition` | **Entity:** `SalesChannelTrackingCustomerEntity` | **Collection:** `SalesChannelTrackingCustomerCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `customerId` | `customer_id` | FkField | Required |
| `salesChannelId` | `sales_channel_id` | FkField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `customer` | OneToOne | `CustomerDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |

### `sales_channel_tracking_order` [E]

**Class:** `SalesChannelTrackingOrderDefinition` | **Entity:** `SalesChannelTrackingOrderEntity` | **Collection:** `SalesChannelTrackingOrderCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `orderId` | `order_id` | FkField | Required |
| `order_version_id` | `OrderDefinition::class` | ReferenceVersionField | Required |
| `salesChannelId` | `sales_channel_id` | FkField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `order` | OneToOne | `OrderDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |


## Content/Property

### `property_group` [E]

**Class:** `PropertyGroupDefinition` | **Entity:** `PropertyGroupEntity` | **Collection:** `PropertyGroupCollection`

**Defaults:** `displayType="text"`, `sortingType="alphanumeric"`, `filterable="self::FILTERABLE"`, `visibleOnProductDetailPage="self::VISIBLE_ON_PRODUCT_DETAIL_PAGE"`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `description` | `` | TranslatedField | ApiAware |
| `displayType` | `display_type` | StringField | ApiAware |
| `sortingType` | `sorting_type` | StringField | ApiAware |
| `filterable` | `filterable` | BoolField | ApiAware |
| `visibleOnProductDetailPage` | `visible_on_product_detail_page` | BoolField | ApiAware |
| `position` | `` | TranslatedField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `options` | OneToMany | `PropertyGroupOptionDefinition` |
| `PropertyGroupTranslationDefinition::class` | OneToMany | `PropertyGroupTranslationDefinition` |

**Translated fields:** `name`, `description`, `position`, `customFields`

### `property_group_option` [E]

**Class:** `PropertyGroupOptionDefinition` | **Entity:** `PropertyGroupOptionEntity` | **Collection:** `PropertyGroupOptionCollection` | **Parent:** `PropertyGroupDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `groupId` | `property_group_id` | FkField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `position` | `` | TranslatedField | ApiAware |
| `colorHexCode` | `color_hex_code` | StringField | ApiAware |
| `mediaId` | `media_id` | FkField | ApiAware |
| `combinable` | `combinable` | BoolField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `media` | ManyToOne | `MediaDefinition` |
| `group` | ManyToOne | `PropertyGroupDefinition` |
| `PropertyGroupOptionTranslationDefinition::class` | OneToMany | `PropertyGroupOptionTranslationDefinition` |
| `productConfiguratorSettings` | OneToMany | `ProductConfiguratorSettingDefinition` |
| `productProperties` | ManyToMany | `ProductDefinition` |
| `productOptions` | ManyToMany | `ProductDefinition` |

**Translated fields:** `name`, `position`, `customFields`

### `property_group_option_translation` [T]

**Class:** `PropertyGroupOptionTranslationDefinition` | **Entity:** `PropertyGroupOptionTranslationEntity` | **Collection:** `PropertyGroupOptionTranslationCollection` | **Parent:** `PropertyGroupOptionDefinition`

**Defaults:** `position=1`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |
| `position` | `position` | IntField | ApiAware |
| `` | `` | CustomFields | ApiAware |

### `property_group_translation` [T]

**Class:** `PropertyGroupTranslationDefinition` | **Entity:** `PropertyGroupTranslationEntity` | **Collection:** `PropertyGroupTranslationCollection` | **Parent:** `PropertyGroupDefinition`

**Defaults:** `position=1`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |
| `description` | `description` | LongTextField | ApiAware |
| `position` | `position` | IntField | ApiAware |
| `` | `` | CustomFields | ApiAware |


## Content/Rule

### `rule` [E]

**Class:** `RuleDefinition` | **Entity:** `RuleEntity` | **Collection:** `RuleCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `name` | StringField | ApiAware |
| `priority` | `priority` | IntField | Required |
| `description` | `description` | LongTextField | ApiAware |
| `payload` | `payload` | BlobField | WriteProtected |
| `invalid` | `invalid` | BoolField | WriteProtected |
| `areas` | `areas` | ListField | WriteProtected |
| `` | `` | CustomFields | ApiAware |
| `moduleTypes` | `module_types` | JsonField |  |

| Association | Type | Target |
|-------------|------|--------|
| `conditions` | OneToMany | `RuleConditionDefinition` |
| `productPrices` | OneToMany | `ProductPriceDefinition` |
| `shippingMethodPrices` | OneToMany | `ShippingMethodPriceDefinition` |
| `shippingMethodPriceCalculations` | OneToMany | `ShippingMethodPriceDefinition` |
| `shippingMethods` | OneToMany | `ShippingMethodDefinition` |
| `paymentMethods` | OneToMany | `PaymentMethodDefinition` |
| `personaPromotions` | OneToMany | `PromotionDefinition` |
| `flowSequences` | OneToMany | `FlowSequenceDefinition` |
| `taxProviders` | OneToMany | `TaxProviderDefinition` |
| `tags` | ManyToMany | `TagDefinition` |
| `personaPromotions` | ManyToMany | `PromotionDefinition` |
| `orderPromotions` | ManyToMany | `PromotionDefinition` |
| `cartPromotions` | ManyToMany | `PromotionDefinition` |
| `promotionDiscounts` | ManyToMany | `PromotionDiscountDefinition` |
| `promotionSetGroups` | ManyToMany | `PromotionSetGroupDefinition` |

### `rule_condition` [E]

**Class:** `RuleConditionDefinition` | **Entity:** `RuleConditionEntity` | **Collection:** `RuleConditionCollection` | **Parent:** `RuleDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `type` | `type` | StringField | Required |
| `ruleId` | `rule_id` | FkField | Required |
| `scriptId` | `script_id` | FkField |  |
| `self::class` | `self::class` | ParentFkField |  |
| `value` | `value` | JsonField |  |
| `position` | `position` | IntField |  |
| `` | `` | CustomFields |  |

| Association | Type | Target |
|-------------|------|--------|
| `rule` | ManyToOne | `RuleDefinition` |
| `appScriptCondition` | ManyToOne | `AppScriptConditionDefinition` |
| `self::class` | ManyToOne | `` |
| `self::class` | OneToMany | `` |

### `rule_tag` [M]

**Class:** `RuleTagDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `ruleId` | `rule_id` | FkField | PrimaryKey |
| `tagId` | `tag_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `rule` | ManyToOne | `RuleDefinition` |
| `tag` | ManyToOne | `TagDefinition` |


## Content/SEO

### `main_category` [E]

**Class:** `MainCategoryDefinition` | **Entity:** `MainCategoryEntity` | **Collection:** `MainCategoryCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `productId` | `product_id` | FkField | ApiAware |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | ApiAware |
| `categoryId` | `category_id` | FkField | ApiAware |
| `CategoryDefinition::class` | `CategoryDefinition::class` | ReferenceVersionField | ApiAware |
| `salesChannelId` | `sales_channel_id` | FkField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `product` | ManyToOne | `ProductDefinition` |
| `category` | ManyToOne | `CategoryDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |

### `sales_channel_main_category` [E]

**Class:** `SalesChannelMainCategoryDefinition`

### `sales_channel_seo_url` [E]

**Class:** `SalesChannelSeoUrlDefinition`

### `seo_url` [E]

**Class:** `SeoUrlDefinition` | **Entity:** `SeoUrlEntity` | **Collection:** `SeoUrlCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `salesChannelId` | `sales_channel_id` | FkField | ApiAware |
| `languageId` | `language_id` | FkField | ApiAware |
| `foreignKey` | `foreign_key` | IdField | ApiAware |
| `routeName` | `route_name` | StringField | ApiAware |
| `pathInfo` | `path_info` | StringField | ApiAware |
| `seoPathInfo` | `seo_path_info` | StringField | ApiAware |
| `isCanonical` | `is_canonical` | BoolField | ApiAware |
| `isModified` | `is_modified` | BoolField | ApiAware |
| `isDeleted` | `is_deleted` | BoolField | ApiAware |
| `error` | `error` | StringField | Runtime |
| `url` | `url` | StringField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `language` | ManyToOne | `LanguageDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |

### `seo_url_template` [E]

**Class:** `SeoUrlTemplateDefinition` | **Entity:** `SeoUrlTemplateEntity` | **Collection:** `SeoUrlTemplateCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `salesChannelId` | `sales_channel_id` | FkField | ApiAware |
| `entityName` | `entity_name` | StringField | Required |
| `routeName` | `route_name` | StringField | Required |
| `template` | `template` | StringField | AllowEmptyString |
| `isValid` | `is_valid` | BoolField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |
