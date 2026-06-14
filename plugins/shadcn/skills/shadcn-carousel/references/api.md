# Carousel — API Reference

## Composition

```text
Carousel
├── CarouselContent
│   ├── CarouselItem
│   └── CarouselItem
├── CarouselPrevious
└── CarouselNext
```

## Usage

```tsx
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel"
```

```tsx
<Carousel>
  <CarouselContent>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
    <CarouselItem>...</CarouselItem>
  </CarouselContent>
  <CarouselPrevious />
  <CarouselNext />
</Carousel>
```

## Sub-Component Props

### Carousel

| Prop          | Type                          | Default        | Description                              |
| ------------- | ----------------------------- | -------------- | ---------------------------------------- |
| `opts`        | `CarouselOptions`             | -              | Embla Carousel options object            |
| `plugins`     | `CarouselPlugin`              | -              | Array of Embla plugins                   |
| `orientation` | `"horizontal" \| "vertical"`  | `"horizontal"` | Scroll axis direction                    |
| `setApi`      | `(api: CarouselApi) => void`  | -              | Callback to receive the Embla API instance |
| `className`   | `string`                      | -              |                                          |

### CarouselContent

The scrollable list container. Forwards the `ref` to Embla.

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CarouselItem

An individual slide. Default `basis-full` (one slide at a time).

| Prop        | Type     | Default |
| ----------- | -------- | ------- |
| `className` | `string` | -       |

### CarouselPrevious / CarouselNext

Navigation buttons. Accept all `Button` props.

| Prop        | Type     | Default     |
| ----------- | -------- | ----------- |
| `variant`   | string   | `"outline"` |
| `size`      | string   | `"icon"`    |
| `className` | `string` | -           |

## `CarouselApi` Type

```ts
import { type CarouselApi } from "@/components/ui/carousel"
```

The type is `UseEmblaCarouselType[1]`. Key methods:

| Method                  | Description                              |
| ----------------------- | ---------------------------------------- |
| `scrollSnapList()`      | Returns array of scroll snap positions   |
| `selectedScrollSnap()`  | Returns current snap index (0-based)     |
| `canScrollPrev()`       | Whether the carousel can scroll back     |
| `canScrollNext()`       | Whether the carousel can scroll forward  |
| `scrollPrev()`          | Scroll to previous slide                 |
| `scrollNext()`          | Scroll to next slide                     |
| `on(event, callback)`   | Subscribe to an Embla event              |
| `off(event, callback)`  | Unsubscribe from an Embla event          |

## Sizes

Use the `basis` utility on `CarouselItem`:

```tsx
// 33% of carousel width
<CarouselItem className="basis-1/3">...</CarouselItem>

// Responsive: 50% on md, 33% on lg
<CarouselItem className="md:basis-1/2 lg:basis-1/3">...</CarouselItem>
```

## Spacing

Use negative margin on `CarouselContent` and matching padding on `CarouselItem`:

```tsx
<CarouselContent className="-ml-4">
  <CarouselItem className="pl-4">...</CarouselItem>
</CarouselContent>
```

## Embla Options

```tsx
<Carousel opts={{ align: "start", loop: true }}>
```

See https://www.embla-carousel.com/api/options/ for all options.

## Events

```tsx
import { type CarouselApi } from "@/components/ui/carousel"

const [api, setApi] = React.useState<CarouselApi>()

React.useEffect(() => {
  if (!api) return
  api.on("select", () => {
    // Do something on slide change
  })
}, [api])
```

See https://www.embla-carousel.com/api/events/ for all events.

## RTL

```tsx
<Carousel dir={dir} opts={{ direction: dir }}>
  ...
  <CarouselPrevious className="rtl:rotate-180" />
  <CarouselNext className="rtl:rotate-180" />
</Carousel>
```

---

_Source: `/tmp/shadcn-repo/apps/v4/content/docs/components/radix/carousel.mdx`_
