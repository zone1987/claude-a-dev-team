# sw-cms-visibility-config

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| visibility | `any` | — | yes |  |

## Methods

| Method | Description |
|--------|-------------|
| `onVisibilityChange` | |

## Examples

### Example 1
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
                <sw-cms-visibility-config
                    class="sw-cms-sidebar__visibility-config-block"
                    :visibility="selectedBlock.visibility"
                    @visibility-change="(viewport, isVisible) => onVisibilityChange(selectedBlock, viewport, isVisible)"
                />
            </template>
        </sw-sidebar-collapse>
    </template>
</div>
{% endblock %}

{% block sw_cms_sidebar_section_settings %}
<div class="sw-cms-sidebar__section-settings">
    <template v-if="selectedSection !== null">

```

### Example 2
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
                    <sw-cms-visibility-config
                        class="sw-cms-sidebar__visibility-config-section"
                        :visibility="selectedSection.visibility"
                        @visibility-change="(viewport, isVisible) => onVisibilityChange(selectedSection, viewport, isVisible)"
                    />
                </template>
            </sw-sidebar-collapse>
            {% endblock %}
        </template>
    </div>
    {% endblock %}
</sw-sidebar-item>
{% endblock %}

{% block sw_cms_sidebar_navigator %}
```
