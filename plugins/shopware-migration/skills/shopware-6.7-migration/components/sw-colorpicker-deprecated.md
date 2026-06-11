# sw-colorpicker-deprecated

> **Deprecated in 6.7** — Use `mt-colorpicker` instead. Will be removed in 6.8.
> See [mt-colorpicker](mt-colorpicker.md) for the replacement.

## Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-colorpicker>` | `<mt-colorpicker>` |

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `''` | no |  |
| colorOutput | `any` | `'auto'` | no | Valid: `auto`, `hex`, `hsl`, `rgb` |
| alpha | `any` | `true` | no |  |
| disabled | `any` | `false` | no |  |
| readonly | `any` | `false` | no |  |
| colorLabels | `any` | `true` | no |  |
| zIndex | `null \| null` | `null` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

## Methods

| Method | Description |
|--------|-------------|
| `componentBeforeDestroy` | |
| `debounceEmitColorValue` | |
| `outsideClick` | |
| `setOutsideClickEvent` | |
| `removeOutsideClickEvent` | |
| `toggleColorPicker` | |
| `moveSelector` | |
| `setDragging` | |
| `removeDragging` | |
| `setSingleRGBValue` | |
| `setHslaValues` | |
| `splitRGBValues` | |
| `splitHSLValues` | |
| `convertHSLtoRGB` | |
| `convertHSLtoHEX` | |
| `convertHSL` | |
| `convertRGBtoHSL` | |
| `convertHEXtoHSL` | |
| `onClickInput` | |
| `roundingFloat` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `colorValue` | |
| `integerAlpha` | |
| `sliderBackground` | |
| `isColorValid` | |
| `previewColorValue` | |
| `selectorBackground` | |
| `redValue` | |
| `greenValue` | |
| `blueValue` | |
| `rgbValue` | |
| `hslValue` | |
| `hexValue` | |
| `convertedValue` | |
| `selectorPositionX` | |
| `selectorPositionY` | |
| `selectorStyles` | |

## Examples

### Basic Usage
```twig
<sw-colorpicker-deprecated>
    <!-- content -->
</sw-colorpicker-deprecated>
```
