# Carousel — Source Files

Source location: `registry/new-york-v4/ui/carousel/`

---

## Contents

- [Carousel.vue](#carouselvue)
- [CarouselContent.vue](#carouselcontentvue)
- [CarouselItem.vue](#carouselitemvue)
- [CarouselNext.vue](#carouselnextvue)
- [CarouselPrevious.vue](#carouselpreviousvue)
- [interface.ts](#interfacets)
- [useCarousel.ts](#usecarouselts)
- [index.ts](#indexts)

## Carousel.vue

```vue
<script setup lang="ts">
import type { CarouselEmits, CarouselProps, WithClassAsProps } from "./interface"
import { cn } from "@/lib/utils"
import { useProvideCarousel } from "./useCarousel"

const props = withDefaults(defineProps<CarouselProps & WithClassAsProps>(), {
  orientation: "horizontal",
})

const emits = defineEmits<CarouselEmits>()

const { canScrollNext, canScrollPrev, carouselApi, carouselRef, orientation, scrollNext, scrollPrev } = useProvideCarousel(props, emits)

defineExpose({
  canScrollNext,
  canScrollPrev,
  carouselApi,
  carouselRef,
  orientation,
  scrollNext,
  scrollPrev,
})

function onKeyDown(event: KeyboardEvent) {
  const prevKey = props.orientation === "vertical" ? "ArrowUp" : "ArrowLeft"
  const nextKey = props.orientation === "vertical" ? "ArrowDown" : "ArrowRight"

  if (event.key === prevKey) {
    event.preventDefault()
    scrollPrev()
    return
  }

  if (event.key === nextKey) {
    event.preventDefault()
    scrollNext()
  }
}
</script>

<template>
  <div
    data-slot="carousel"
    :class="cn('relative', props.class)"
    role="region"
    aria-roledescription="carousel"
    tabindex="0"
    @keydown="onKeyDown"
  >
    <slot :can-scroll-next :can-scroll-prev :carousel-api :carousel-ref :orientation :scroll-next :scroll-prev />
  </div>
</template>
```

---

## CarouselContent.vue

```vue
<script setup lang="ts">
import type { WithClassAsProps } from "./interface"
import { cn } from "@/lib/utils"
import { useCarousel } from "./useCarousel"

defineOptions({
  inheritAttrs: false,
})

const props = defineProps<WithClassAsProps>()

const { carouselRef, orientation } = useCarousel()
</script>

<template>
  <div
    ref="carouselRef"
    data-slot="carousel-content"
    class="overflow-hidden"
  >
    <div
      :class="
        cn(
          'flex',
          orientation === 'horizontal' ? '-ml-4' : '-mt-4 flex-col',
          props.class,
        )"
      v-bind="$attrs"
    >
      <slot />
    </div>
  </div>
</template>
```

---

## CarouselItem.vue

```vue
<script setup lang="ts">
import type { WithClassAsProps } from "./interface"
import { cn } from "@/lib/utils"
import { useCarousel } from "./useCarousel"

const props = defineProps<WithClassAsProps>()

const { orientation } = useCarousel()
</script>

<template>
  <div
    data-slot="carousel-item"
    role="group"
    aria-roledescription="slide"
    :class="cn(
      'min-w-0 shrink-0 grow-0 basis-full',
      orientation === 'horizontal' ? 'pl-4' : 'pt-4',
      props.class,
    )"
  >
    <slot />
  </div>
</template>
```

---

## CarouselNext.vue

```vue
<script setup lang="ts">
import type { WithClassAsProps } from "./interface"
import type { ButtonVariants } from "@/registry/new-york-v4/ui/button"
import { ArrowRight } from "@lucide/vue"
import { cn } from "@/lib/utils"
import { Button } from "@/registry/new-york-v4/ui/button"
import { useCarousel } from "./useCarousel"

const props = withDefaults(defineProps<{
  variant?: ButtonVariants["variant"]
  size?: ButtonVariants["size"]
}
& WithClassAsProps>(), {
  variant: "outline",
  size: "icon",
})

const { orientation, canScrollNext, scrollNext } = useCarousel()
</script>

<template>
  <Button
    data-slot="carousel-next"
    :disabled="!canScrollNext"
    :class="cn(
      'absolute size-8 rounded-full',
      orientation === 'horizontal'
        ? 'top-1/2 -right-12 -translate-y-1/2'
        : '-bottom-12 left-1/2 -translate-x-1/2 rotate-90',
      props.class,
    )"
    :variant="variant"
    :size="size"
    @click="scrollNext"
  >
    <slot>
      <ArrowRight />
      <span class="sr-only">Next Slide</span>
    </slot>
  </Button>
</template>
```

---

## CarouselPrevious.vue

```vue
<script setup lang="ts">
import type { WithClassAsProps } from "./interface"
import type { ButtonVariants } from "@/registry/new-york-v4/ui/button"
import { ArrowLeft } from "@lucide/vue"
import { cn } from "@/lib/utils"
import { Button } from "@/registry/new-york-v4/ui/button"
import { useCarousel } from "./useCarousel"

const props = withDefaults(defineProps<{
  variant?: ButtonVariants["variant"]
  size?: ButtonVariants["size"]
}
& WithClassAsProps>(), {
  variant: "outline",
  size: "icon",
})

const { orientation, canScrollPrev, scrollPrev } = useCarousel()
</script>

<template>
  <Button
    data-slot="carousel-previous"
    :disabled="!canScrollPrev"
    :class="cn(
      'absolute size-8 rounded-full',
      orientation === 'horizontal'
        ? 'top-1/2 -left-12 -translate-y-1/2'
        : '-top-12 left-1/2 -translate-x-1/2 rotate-90',
      props.class,
    )"
    :variant="variant"
    :size="size"
    @click="scrollPrev"
  >
    <slot>
      <ArrowLeft />
      <span class="sr-only">Previous Slide</span>
    </slot>
  </Button>
</template>
```

---

## interface.ts

```ts
import type useEmblaCarousel from "embla-carousel-vue"
import type {
  EmblaCarouselVueType,
} from "embla-carousel-vue"
import type { HTMLAttributes, UnwrapRef } from "vue"

type CarouselApi = EmblaCarouselVueType[1]
type UseCarouselParameters = Parameters<typeof useEmblaCarousel>
type CarouselOptions = UseCarouselParameters[0]
type CarouselPlugin = UseCarouselParameters[1]

export type UnwrapRefCarouselApi = UnwrapRef<CarouselApi>

export interface CarouselProps {
  opts?: CarouselOptions
  plugins?: CarouselPlugin
  orientation?: "horizontal" | "vertical"
}

export interface CarouselEmits {
  (e: "init-api", payload: UnwrapRefCarouselApi): void
}

export interface WithClassAsProps {
  class?: HTMLAttributes["class"]
}
```

---

## useCarousel.ts

```ts
import type { UnwrapRefCarouselApi as CarouselApi, CarouselEmits, CarouselProps } from "./interface"
import { createInjectionState } from "@vueuse/core"
import emblaCarouselVue from "embla-carousel-vue"
import { onMounted, ref } from "vue"

const [useProvideCarousel, useInjectCarousel] = createInjectionState(
  ({
    opts,
    orientation,
    plugins,
  }: CarouselProps, emits: CarouselEmits) => {
    const [emblaNode, emblaApi] = emblaCarouselVue({
      ...opts,
      axis: orientation === "horizontal" ? "x" : "y",
    }, plugins)

    function scrollPrev() {
      emblaApi.value?.scrollPrev()
    }
    function scrollNext() {
      emblaApi.value?.scrollNext()
    }

    const canScrollNext = ref(false)
    const canScrollPrev = ref(false)

    function onSelect(api: CarouselApi) {
      canScrollNext.value = api?.canScrollNext() || false
      canScrollPrev.value = api?.canScrollPrev() || false
    }

    onMounted(() => {
      if (!emblaApi.value)
        return

      emblaApi.value?.on("init", onSelect)
      emblaApi.value?.on("reInit", onSelect)
      emblaApi.value?.on("select", onSelect)

      emits("init-api", emblaApi.value)
    })

    return { carouselRef: emblaNode, carouselApi: emblaApi, canScrollPrev, canScrollNext, scrollPrev, scrollNext, orientation }
  },
)

function useCarousel() {
  const carouselState = useInjectCarousel()

  if (!carouselState)
    throw new Error("useCarousel must be used within a <Carousel />")

  return carouselState
}

export { useCarousel, useProvideCarousel }
```

---

## index.ts

```ts
export { default as Carousel } from "./Carousel.vue"
export { default as CarouselContent } from "./CarouselContent.vue"
export { default as CarouselItem } from "./CarouselItem.vue"
export { default as CarouselNext } from "./CarouselNext.vue"
export { default as CarouselPrevious } from "./CarouselPrevious.vue"
export type {
  UnwrapRefCarouselApi as CarouselApi,
} from "./interface"

export { useCarousel } from "./useCarousel"
```
