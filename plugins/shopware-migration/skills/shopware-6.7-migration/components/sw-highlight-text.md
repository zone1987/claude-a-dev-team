# sw-highlight-text

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| searchTerm | `any` | `null` | no |  |
| text | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `searchAndReplace` | |
| `escapeRegExp` | |

## Examples

### Example 1
Source: `sw-import-export/component/sw-import-export-edit-profile-general/sw-import-export-edit-profile-general.html.twig`
```twig
                <sw-highlight-text
                    v-if="highlightSearchTerm && !isSelected(item)"
                    :text="getKey(item, labelProperty)"
                    :search-term="searchTerm"
                />
                {% endblock %}

                {% block sw_import_export_edit_profile_general_container_object_type_select_result_text %}
                <template v-else>
                    {{ getKey(item, labelProperty) }}
                </template>
                {% endblock %}
            </sw-select-result>
            {% endblock %}
        </template>
```

### Example 2
Source: `sw-import-export/component/sw-import-export-edit-profile-general/sw-import-export-edit-profile-general.html.twig`
```twig
                    <sw-highlight-text
                        v-if="highlightSearchTerm && !isSelected(item)"
                        :text="getKey(item, labelProperty)"
                        :search-term="searchTerm"
                    />
                    {% endblock %}

                    {% block sw_import_export_edit_profile_general_container_type_result_text %}
                    <template v-else>
                        {{ getKey(item, labelProperty) }}
                    </template>
                    {% endblock %}
                </sw-select-result>
                {% endblock %}
            </template>
```

### Example 3
Source: `sw-import-export/component/sw-import-export-entity-path-select/sw-import-export-entity-path-select.html.twig`
```twig
                    <sw-highlight-text
                        v-if="highlightSearchTerm"
                        :text="getKey(item, labelProperty)"
                        :search-term="searchTerm"
                    />

                    <template v-else>
                        {{ getKey(item, labelProperty) }}
                    </template>

                    <mt-icon
                        v-if="item.relation && item.relation !== 'many_to_many'"
                        name="regular-chevron-right-xs"
                        size="10px"
                    />
```

### Example 4
Source: `sw-cms/component/sw-cms-product-assignment/sw-cms-product-assignment.html.twig`
```twig
                                <sw-highlight-text
                                    v-if="highlightSearchTerm"
                                    :text="getKey(item, `translated.${labelProperty}`)"
                                    :search-term="searchTerm"
                                />

                                <template v-else>
                                    {{ getKey(item, `translated.${labelProperty}`) }}
                                </template>
                            </slot>
                        {% endblock %}
                        </sw-select-result>
                    {% endblock %}
                    </slot>
                {% endblock %}
```

### Example 5
Source: `sw-cms/elements/product-listing/config/sw-cms-el-config-product-listing.html.twig`
```twig
                                <sw-highlight-text
                                    v-if="highlightSearchTerm"
                                    :text="getKey(item,labelProperty) || getKey(item, `translated.${labelProperty}`)"
                                    :search-term="searchTerm"
                                />
                                <template v-else>
                                    {{ getKey(item,labelProperty) || getKey(item, `translated.${labelProperty}`) }}
                                </template>
                            </slot>
                            {% endblock %}
                        </sw-select-result>
                    </slot>
                </template>
            </sw-entity-multi-select>
            {% endblock %}
```
