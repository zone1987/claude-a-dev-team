# sw-cms-section

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| page | `any` | — | yes |  |
| section | `any` | — | yes |  |
| active | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| page-config-open | — | |
| block-duplicate | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `openBlockBar` | |
| `emitPageConfigOpen` | |
| `onAddSectionBlock` | |
| `onBlockSelection` | |
| `onBlockDuplicate` | |
| `onBlockDelete` | |
| `updateBlockPositions` | |
| `getDropData` | |
| `blockTypeExists` | |
| `hasBlockErrors` | |
| `hasUniqueBlockErrors` | |
| `hasSlotConfigErrors` | |
| `toggleVisibility` | |
| `getBlockComponent` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `blockRepository` | |
| `slotRepository` | |
| `sectionClasses` | |
| `sectionTypeClass` | |
| `customSectionClass` | |
| `sectionStyles` | |
| `sectionSidebarClasses` | |
| `sectionMobileAndHidden` | |
| `isSideBarType` | |
| `sideBarEmpty` | |
| `blockCount` | |
| `mainContentEmpty` | |
| `sideBarBlocks` | |
| `mainContentBlocks` | |
| `assetFilter` | |
| `blockTypes` | |
| `isVisible` | |
| `toggleButtonText` | |
| `expandedClass` | |
| `sectionContentClasses` | |
| `pageSlotsError` | |
| `pageSlotConfigError` | |

## Examples

### Example 1
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
                <sw-cms-section
                    class="sw-cms-stage-section"
                    :page="page"
                    :section="section"
                    :active="selectedSection !== null && selectedSection.id === section.id"
                    :disabled="!acl.can('cms.editor') || undefined"
                    @page-config-open="pageConfigOpen"
                    @block-duplicate="onBlockDuplicate"
                />
                {% endblock %}
            </template>
        </template>
        {% endblock %}

        {% block sw_cms_detail_stage_add_last_section %}
```

### Example 2
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
<sw-cms-section-actions
    :section="section"
    :disabled="disabled || undefined"
/>
{% endblock %}

<div
    class="sw-cms-section__wrapper"
    :style="sectionStyles"
>
    <sw-cms-visibility-toggle
        v-if="isVisible"
        :text="toggleButtonText"
        :is-collapsed="isCollapsed"
        :class="expandedClass"
```

### Example 3
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
