# Shopware 6 Core Entities — Storefront

> Auto-generated from `src/` — 5 definitions


## Storefront

### `theme` [E]

**Class:** `ThemeDefinition` | **Entity:** `ThemeEntity` | **Collection:** `ThemeCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `technicalName` | `technical_name` | StringField | ApiAware |
| `name` | `name` | StringField | ApiAware |
| `author` | `author` | StringField | ApiAware |
| `description` | `` | TranslatedField | ApiAware |
| `labels` | `` | TranslatedField | ApiAware |
| `helpTexts` | `` | TranslatedField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |
| `previewMediaId` | `preview_media_id` | FkField | ApiAware |
| `parentThemeId` | `parent_theme_id` | FkField | ApiAware |
| `themeJson` | `theme_json` | JsonField |  |
| `baseConfig` | `base_config` | JsonField | ApiAware |
| `configValues` | `config_values` | JsonField | ApiAware |
| `active` | `active` | BoolField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `ThemeTranslationDefinition::class` | OneToMany | `ThemeTranslationDefinition` |
| `salesChannels` | ManyToMany | `SalesChannelDefinition` |
| `media` | ManyToMany | `MediaDefinition` |
| `previewMedia` | ManyToOne | `MediaDefinition` |
| `dependentThemes` | ManyToMany | `ThemeChildDefinition` |

**Translated fields:** `description`, `labels`, `helpTexts`, `customFields`

### `theme_child` [M]

**Class:** `ThemeChildDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `parentId` | `parent_id` | FkField | PrimaryKey |
| `childId` | `child_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `parentTheme` | ManyToOne | `ThemeDefinition` |
| `childTheme` | ManyToOne | `ThemeDefinition` |

### `theme_media` [M]

**Class:** `ThemeMediaDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `themeId` | `theme_id` | FkField | PrimaryKey |
| `mediaId` | `media_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `theme` | ManyToOne | `ThemeDefinition` |
| `media` | ManyToOne | `MediaDefinition` |

### `theme_sales_channel` [M]

**Class:** `ThemeSalesChannelDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `salesChannelId` | `sales_channel_id` | FkField | PrimaryKey |
| `themeId` | `theme_id` | FkField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `theme` | ManyToOne | `ThemeDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |

### `theme_translation` [T]

**Class:** `ThemeTranslationDefinition` | **Entity:** `ThemeTranslationEntity` | **Collection:** `ThemeTranslationCollection` | **Parent:** `ThemeDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `description` | `description` | StringField | ApiAware |
| `labels` | `labels` | JsonField | ApiAware |
| `helpTexts` | `help_texts` | JsonField | ApiAware |
| `` | `` | CustomFields | ApiAware |
