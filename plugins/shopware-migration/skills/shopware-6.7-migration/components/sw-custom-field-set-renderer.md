# sw-custom-field-set-renderer

> Renders a complete set of custom fields with their configured field types.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sets | `any` | — | yes |  |
| entity | `any` | — | yes |  |
| parentEntity | `any` | `null` | no |  |
| variant | `any` | `'tabs'` | no | Valid: `tabs`, `media-collapse` |
| disabled | `any` | `false` | no |  |
| isLoading | `any` | `false` | no |  |
| isSaveSuccessful | `any` | `false` | no |  |
| showCustomFieldSetSelection | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| process-finish | — | |
| save | — | |
| change-active-selection | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initializeCustomFields` | |
| `getInheritedCustomField` | |
| `getCustomFieldInformation` | |
| `getInheritValue` | |
| `getParentCustomFieldSetSelectionSwitchState` | |
| `supportsMapInheritance` | |
| `isMeteorComponent` | |
| `getBind` | |
| `getElementEventListeners` | |
| `getInheritWrapperBind` | |
| `customFieldSetCriteriaById` | |
| `loadCustomFieldSet` | |
| `resetTabs` | |
| `waitForTabComponent` | |
| `getTabLabel` | |
| `onChangeCustomFieldSets` | |
| `onChangeCustomFieldSetSelectionActive` | |
| `sortSets` | |
| `onUpdateActiveSelection` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `hasParent` | |
| `visibleCustomFieldSets` | |
| `customFieldSetRepository` | |
| `customFieldSetCriteria` | |
| `globalCustomFieldSets` | |
| `componentsWithMapInheritanceSupport` | |

## Examples

### Example 1
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
                    <sw-custom-field-set-renderer
                        :entity="country"
                        :disabled="!acl.can('country.editor')"
                        :sets="customFieldSets"
                    />
                </mt-card>
                {% endblock %}
            </template>
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

### Example 2
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
                    <sw-custom-field-set-renderer
                        :entity="salutation"
                        :disabled="!acl.can('salutation.editor') || undefined"
                        :sets="customFieldSets"
                    />
                </mt-card>
                {% endblock %}
            </template>
        </sw-card-view>
    </template>
    {% endblock %}

</sw-page>
{% endblock %}

```

### Example 3
Source: `sw-settings-units/page/sw-settings-units-detail/sw-settings-units-detail.html.twig`
```twig
                <sw-custom-field-set-renderer
                    :entity="unit"
                    :sets="customFieldSets"
                    :disabled="!acl.can('unit.editor')"
                />
            </mt-card>

            <sw-skeleton v-else />
        </sw-card-view>
    </template>
</sw-page>
{% endblock %}

```

### Example 4
Source: `sw-settings-number-range/page/sw-settings-number-range-detail/sw-settings-number-range-detail.html.twig`
```twig
                    <sw-custom-field-set-renderer
                        :entity="numberRange"
                        :disabled="!acl.can('number_ranges.editor')"
                        :sets="customFieldSets"
                    />
                </mt-card>
                {% endblock %}
            </template>
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

### Example 5
Source: `sw-property/page/sw-property-detail/sw-property-detail.html.twig`
```twig
                    <sw-custom-field-set-renderer
                        :entity="propertyGroup"
                        :disabled="!acl.can('property.editor') || undefined"
                        :sets="customFieldSets"
                    />
                </mt-card>
                {% endblock %}
            </div>
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```
