# sw-cms-sidebar

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| page | `any` | — | yes |  |
| demoEntity | `any` | `null` | no |  |
| demoEntityIdProp | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| isDefaultLayout | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| page-type-change | — | |
| demo-entity-change | — | |
| page-save | — | |
| block-stage-drop | — | |
| current-block-change | — | |
| section-duplicate | — | |
| block-duplicate | — | |
| page-update | — | |
| open-layout-assignment | — | |
| open-layout-set-as-default | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onPageTypeChange` | |
| `onDemoEntityChange` | |
| `onCloseBlockConfig` | |
| `isDisabledPageType` | |
| `openSectionSettings` | |
| `blockIsRemovable` | |
| `blockIsUnique` | |
| `blockIsDuplicable` | |
| `sectionIsDuplicable` | |
| `onBlockDragSort` | |
| `refreshPosition` | |
| `onSidebarNavigatorClick` | |
| `onSidebarNavigationConfirm` | |
| `onSidebarNavigationCancel` | |
| `getDragData` | |
| `getDropData` | |
| `onBlockDragStop` | |
| `onBlockDropAbort` | |
| `onBlockStageDrop` | |
| `moveSectionUp` | |
| `moveSectionDown` | |
| `onSectionDuplicate` | |
| `onSectionDelete` | |
| `onBlockDelete` | |
| `onBlockDuplicate` | |
| `onRemoveSectionBackgroundMedia` | |
| `onSetSectionBackgroundMedia` | |
| `onToggleBlockFavorite` | |
| `successfulUpload` | |
| `uploadTag` | |
| `getMainContentBlocks` | |
| `getSidebarContentBlocks` | |
| `pageUpdate` | |
| `onOpenLayoutAssignment` | |
| `onOpenLayoutSetAsDefault` | |
| `blockTypeExists` | |
| `onVisibilityChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `pageTypes` | |
| `pageTypesOptions` | |
| `blockRepository` | |
| `slotRepository` | |
| `cmsBlocks` | |
| `cmsBlockCategories` | |
| `cmsBlockCategoriesOptions` | |
| `mediaRepository` | |
| `addBlockTitle` | |
| `pageSections` | |
| `sidebarItemSettings` | |
| `tooltipDisabled` | |
| `demoCriteria` | |
| `demoContext` | |
| `blockTypes` | |
| `pageConfigErrors` | |
| `hasPageConfigErrors` | |
| `showDefaultLayoutSelection` | |
| `cmsBlocksBySelectedBlockCategory` | |
| `isLayoutAssignmentDisabled` | |
| `pageNameError` | |

## Examples

### Example 1
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
<sw-cms-sidebar
    ref="cmsSidebar"
    :page="page"
    :demo-entity="currentMappingEntity"
    :demo-entity-id-prop="demoEntityId"
    :disabled="!acl.can('cms.editor') || undefined"
    :is-default-layout="isDefaultLayout"
    @demo-entity-change="onDemoEntityChange"
    @block-duplicate="onBlockDuplicate"
    @section-duplicate="onSectionDuplicate"
    @block-stage-drop="onPageUpdate"
    @page-type-change="onPageTypeChange"
    @page-update="onPageUpdate"
    @page-save="onPageSave"
    @open-layout-assignment="onOpenLayoutAssignment"
```

### Example 2
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
        <sw-cms-sidebar-nav-element
            v-draggable="getDragData(block, sectionIndex)"
            v-droppable="getDropData(block, sectionIndex)"
            :block="block"
            class="sw-cms-sidebar__navigator-block"
            :removable="blockIsRemovable(block)"
            :duplicable="blockIsDuplicable(block)"
            :class="{ 'is--dragging': block.isDragging }"
            @block-delete="onBlockDelete($event, section)"
            @block-duplicate="onBlockDuplicate($event, section)"
        />
    </template>
    {% endblock %}
</template>

```

### Example 3
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
                    <sw-cms-sidebar-nav-element
                        v-draggable="getDragData(block, sectionIndex)"
                        v-droppable="getDropData(block, sectionIndex)"
                        :block="block"
                        :removable="blockIsRemovable(block)"
                        class="sw-cms-sidebar__navigator-block is--sidebar"
                        :class="{ 'is--dragging': block.isDragging }"
                        @block-delete="onBlockDelete($event, section)"
                        @block-duplicate="onBlockDuplicate($event, section)"
                    />
                </template>
                {% endblock %}
            </template>

            <template v-else>
```
