# sw-landing-page-tree

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| landingPageId | `any` | `null` | no |  |
| currentLanguageId | `any` | — | yes |  |
| allowEdit | `any` | `true` | no |  |
| allowCreate | `any` | `true` | no |  |
| allowDelete | `any` | `true` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| landing-page-checked-elements-count | — | |
| unsaved-changes | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadLandingPages` | |
| `checkedElementsCount` | |
| `deleteCheckedItems` | |
| `onDeleteLandingPage` | |
| `changeLandingPage` | |
| `duplicateElement` | |
| `createNewElement` | |
| `syncLandingPages` | |
| `createNewLandingPage` | |
| `addLandingPage` | |
| `addLandingPages` | |
| `removeFromStore` | |
| `getLandingPageUrl` | |
| `newLandingPageUrl` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `landingPagesToDelete` | |
| `cmsLandingPageCriteria` | |
| `landingPage` | |
| `landingPageRepository` | |
| `landingPages` | |
| `disableContextMenu` | |
| `contextMenuTooltipText` | |

## Examples

### Example 1
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
            <sw-landing-page-tree
                ref="landingPageTree"
                :landing-page-id="landingPageId"
                :current-language-id="currentLanguageId"
                :allow-edit="acl.can('landing_page.editor')"
                :allow-create="acl.can('landing_page.creator')"
                :allow-delete="acl.can('landing_page.deleter')"
                @unsaved-changes="openChangeModal"
                @landing-page-checked-elements-count="landingPageCheckedElementsCount"
            />
            {% endblock %}

        </template>
    </sw-sidebar-collapse>
    {% endblock %}
```
