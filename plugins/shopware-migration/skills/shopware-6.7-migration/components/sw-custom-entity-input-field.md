# sw-custom-entity-input-field

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `null \| null \| null \| null` | `null` | no |  |
| type | `any` | — | yes |  |
| label | `any` | `''` | no |  |
| placeholder | `any` | `''` | no |  |
| helpText | `any` | `''` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `onChange` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `currentValue` | |

## Examples

### Example 1
Source: `sw-custom-entity/page/sw-generic-custom-entity-detail/sw-generic-custom-entity-detail.html.twig`
```twig
                <sw-custom-entity-input-field
                    v-for="field in card.fields"
                    :key="field.ref"
                    v-model:value="customEntityData[field.ref]"
                    class="sw-generic-custom-entity-detail__field"
                    :type="getType(field.ref)"
                    :label="getLabel('fields', field.ref)"
                    :placeholder="getPlaceholder('fields', field.ref)"
                    :help-text="getHelpText('fields', field.ref)"
                />
            </template>
        </mt-card>
    </div>
</template>

```
