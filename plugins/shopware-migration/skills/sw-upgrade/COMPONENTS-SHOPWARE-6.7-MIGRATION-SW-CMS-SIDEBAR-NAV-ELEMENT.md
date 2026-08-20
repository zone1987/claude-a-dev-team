# sw-cms-sidebar-nav-element

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| block | `any` | — | yes |  |
| removable | `any` | — | no |  |
| duplicable | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| block-duplicate | — | |
| block-delete | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onBlockDuplicate` | |
| `onBlockDelete` | |

## Examples

### Example 1
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

### Example 2
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
