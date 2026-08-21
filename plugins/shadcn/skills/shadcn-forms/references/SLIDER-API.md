# Slider — API Reference

Full API:
- Radix: https://www.radix-ui.com/docs/primitives/components/slider#api-reference
- Base UI: https://base-ui.com/react/components/slider#api-reference

## Slider (Root)

| Prop              | Type                               | Default        | Description                                   |
| ----------------- | ---------------------------------- | -------------- | --------------------------------------------- |
| `defaultValue`    | `number[]`                         | —              | Uncontrolled initial value(s)                 |
| `value`           | `number[]`                         | —              | Controlled value(s)                           |
| `onValueChange`   | `(value: number[]) => void`        | —              | Called while dragging                         |
| `onValueCommit`   | `(value: number[]) => void`        | —              | Called when drag ends                         |
| `min`             | `number`                           | `0`            | Minimum value                                 |
| `max`             | `number`                           | `100`          | Maximum value                                 |
| `step`            | `number`                           | `1`            | Step increment                                |
| `orientation`     | `"horizontal" \| "vertical"`      | `"horizontal"` | Slider orientation                            |
| `disabled`        | `boolean`                          | `false`        | Disables interaction                          |
| `inverted`        | `boolean`                          | `false`        | Invert the slider direction                   |
| `name`            | `string`                           | —              | Form field name                               |
| `className`       | `string`                           | —              | Additional CSS classes                        |

`data-slot="slider"`

### Value array rules

- Single thumb: `defaultValue={[50]}`
- Range (two thumbs): `defaultValue={[20, 80]}`
- Multiple thumbs: `defaultValue={[10, 50, 90]}`

The component determines the number of thumbs from the length of the value array.

## Internal sub-components (data slots)

| Slot              | Element                       | Description                      |
| ----------------- | ----------------------------- | -------------------------------- |
| `slider-track`    | `SliderPrimitive.Track`       | The background track bar         |
| `slider-range`    | `SliderPrimitive.Range`       | The filled range indicator       |
| `slider-thumb`    | `SliderPrimitive.Thumb`       | Draggable thumb (one per value)  |

## Keyboard support

| Key         | Action                      |
| ----------- | --------------------------- |
| `ArrowRight` / `ArrowUp`  | Increase value by step |
| `ArrowLeft` / `ArrowDown` | Decrease value by step |
| `Home`      | Set to minimum value        |
| `End`       | Set to maximum value        |
| `PageUp`    | Increase by 10x step        |
| `PageDown`  | Decrease by 10x step        |

## Base UI specific: thumbAlignment

The base variant uses `thumbAlignment="edge"` which aligns the thumb to the edge of the track (not centered).

## Source files

- `registry/new-york-v4/ui/slider.tsx`
