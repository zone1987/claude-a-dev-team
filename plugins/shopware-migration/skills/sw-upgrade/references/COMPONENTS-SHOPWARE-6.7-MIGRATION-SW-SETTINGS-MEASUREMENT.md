# sw-settings-measurement

> Shopware Administration component.

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getMeasurementUnits` | |
| `getDefaultMeasurementSystems` | |
| `onSave` | |
| `onChangeLanguage` | |
| `onChangeMeasurementSystem` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `measurementSystemRepository` | |
| `measurementSystemCriteria` | |
| `defaultLengthUnit` | |
| `defaultWeightUnit` | |
| `requiredFields` | |

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
