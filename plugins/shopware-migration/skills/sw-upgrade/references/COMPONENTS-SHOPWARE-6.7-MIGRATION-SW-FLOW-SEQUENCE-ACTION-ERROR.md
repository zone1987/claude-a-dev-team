# sw-flow-sequence-action-error

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| content | — | |

## Methods

| Method | Description |
|--------|-------------|
| `removeWarning` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `sequences` | |

## Examples

### Example 1
Source: `sw-flow/component/sw-flow-sequence-action/sw-flow-sequence-action.html.twig`
```twig
<sw-flow-sequence-action-error
    v-if="!isValidAction(item.actionName)"
    :sequence="item"
>
    <template #content>
        <div class="sw-flow-sequence-action__error-action">
            <div class="sw-flow-sequence-action__error-action-title">
                <mt-icon
                    name="regular-question-circle-s"
                    size="14px"
                    class="mt-icon-action"
                />

                <span>{{ $tc('sw-flow.actions.unknownLabel') }}</span>
            </div>
```
