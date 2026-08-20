# sw-cms-section-config

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| section | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| section-delete | — | |
| section-duplicate | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onSetBackgroundMedia` | |
| `successfulUpload` | |
| `removeMedia` | |
| `onSectionDelete` | |
| `onSectionDuplicate` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `uploadTag` | |
| `mediaRepository` | |
| `cmsPageState` | |
| `quickactionsDisabled` | |
| `quickactionClasses` | |
| `sizingModeOptions` | |
| `mobileBehaviorOptions` | |
| `backgroundMediaModeOptions` | |

## Examples

### Example 1
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
                    <sw-cms-section-config
                        :section="selectedSection"
                        @section-duplicate="onSectionDuplicate"
                        @section-delete="onSectionDelete"
                    />
                </template>
                {% endblock %}
            </sw-sidebar-collapse>

            <sw-sidebar-collapse :expand-on-loading="false">
                <template #header>
                    <span>{{ $tc('sw-cms.sidebar.contentMenu.visibilitySettings') }}</span>
                </template>
                <template #content>
                    <sw-cms-visibility-config
```
