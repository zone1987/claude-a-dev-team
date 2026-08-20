# sw-settings-measurement-default-units

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| measurementSystems | `any` | — | yes |  |
| measurementSystem | `any` | — | yes |  |
| measurementUnits | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| measurement-system-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onChangeMeasurementSystem` | |
| `labelUnitCallback` | |
| `getUnitOptionsByType` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `lengthUnitOptions` | |
| `weightUnitOptions` | |
| `measurementSystemOptions` | |
| `measurementUnitSystemError` | |
| `measurementLengthUnitError` | |
| `measurementWeightUnitError` | |

## Examples

### Example 1
Source: `sw-settings-measurement/page/sw-settings-measurement/sw-settings-measurement.html.twig`
```twig
            <sw-settings-measurement-default-units
                :measurement-systems="measurementSystems"
                :measurement-system="measurementSystem"
                :measurement-units="measurementUnits"
                @measurement-system-change="onChangeMeasurementSystem"
            />
        </sw-card-view>
    </template>
</sw-page>

```
