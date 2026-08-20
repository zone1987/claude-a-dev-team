# sw-cms-slot

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| element | `any` | — | yes |  |
| active | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `onSettingsButtonClick` | |
| `onCloseSettingsModal` | |
| `onElementButtonClick` | |
| `onCloseElementModal` | |
| `onSelectElement` | |
| `onToggleElementFavorite` | |
| `toggleHoverElement` | |
| `getFavoriteIconToggleState` | |
| `elementInElementGroup` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `slotElementId` | |
| `cmsServiceState` | |
| `elementConfig` | |
| `elementModalTitle` | |
| `cmsElements` | |
| `groupedCmsElements` | |
| `componentClasses` | |
| `cmsSlotSettingsClasses` | |
| `tooltipDisabled` | |
| `modalVariant` | |

## Examples

### Example 1
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
                        <sw-cms-slot
                            :element="el"
                            :disabled="disabled || undefined"
                            :active="selectedBlock !== null && selectedBlock.id === block.id"
                        />
                    </template>
                    {% endblock %}
                </component>
                {% endblock %}
            </sw-cms-block>
            {% endblock %}

            {% block sw_cms_section_add_sidebar_block %}
            <sw-cms-stage-add-block
                v-if="isSystemDefaultLanguage && !disabled"
```

### Example 2
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
                                <sw-cms-slot
                                    :element="el"
                                    :disabled="disabled || undefined"
                                    :active="selectedBlock !== null && selectedBlock.id === block.id"
                                />
                            </template>
                            {% endblock %}
                        </component>
                        {% endblock %}
                    </sw-cms-block>
                    {% endblock %}

                    {% block sw_cms_section_add_content_block %}
                    <sw-cms-stage-add-block
                        v-if="isSystemDefaultLanguage && !disabled"
```
