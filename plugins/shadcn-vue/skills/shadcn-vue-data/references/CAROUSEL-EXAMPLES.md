# Carousel — Examples

Source: `registry/bases/reka/examples/carousel/`

---

## Contents

- [Basic Carousel](#basic-carousel)
- [Multiple Slides Visible](#multiple-slides-visible)
- [With Custom Gap](#with-custom-gap)
- [Vertical Orientation](#vertical-orientation)
- [Loop + Align Options](#loop-align-options)
- [Accessing the Embla API via `@init-api`](#accessing-the-embla-api-via-init-api)
- [Accessing the API via Template Ref](#accessing-the-api-via-template-ref)
- [Autoplay Plugin](#autoplay-plugin)
- [Using Slot Props](#using-slot-props)
- [Item Sizing Reference](#item-sizing-reference)

## Basic Carousel

```vue
<script setup lang="ts">
import { Card, CardContent } from "@/registry/bases/reka/ui/card"
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/registry/bases/reka/ui/carousel"
import { Example } from "~/registry/bases/reka/components/example"
</script>

<template>
  <Example title="Basic">
    <Carousel class="mx-auto max-w-xs sm:max-w-sm">
      <CarouselContent>
        <CarouselItem v-for="index in 5" :key="index">
          <div class="p-1">
            <Card>
              <CardContent class="flex aspect-square items-center justify-center p-6">
                <span class="text-4xl font-semibold">{{ index }}</span>
              </CardContent>
            </Card>
          </div>
        </CarouselItem>
      </CarouselContent>
      <CarouselPrevious class="hidden sm:inline-flex" />
      <CarouselNext class="hidden sm:inline-flex" />
    </Carousel>
  </Example>
</template>
```

---

## Multiple Slides Visible

Use `:opts="{ align: 'start' }"` and `basis-1/2` / `basis-1/3` on `CarouselItem`:

```vue
<script setup lang="ts">
import { Card, CardContent } from "@/registry/bases/reka/ui/card"
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/registry/bases/reka/ui/carousel"
import { Example } from "~/registry/bases/reka/components/example"
</script>

<template>
  <Example title="Multiple">
    <Carousel
      class="mx-auto max-w-xs sm:max-w-sm"
      :opts="{
        align: 'start',
      }"
    >
      <CarouselContent>
        <CarouselItem v-for="index in 5" :key="index" class="sm:basis-1/2 lg:basis-1/3">
          <div class="p-1">
            <Card>
              <CardContent class="flex aspect-square items-center justify-center p-6">
                <span class="text-3xl font-semibold">{{ index }}</span>
              </CardContent>
            </Card>
          </div>
        </CarouselItem>
      </CarouselContent>
      <CarouselPrevious class="hidden sm:inline-flex" />
      <CarouselNext class="hidden sm:inline-flex" />
    </Carousel>
  </Example>
</template>
```

---

## With Custom Gap

Override the default `-ml-4` / `pl-4` spacing with `-ml-1` / `pl-1`:

```vue
<script setup lang="ts">
import { Card, CardContent } from "@/registry/bases/reka/ui/card"
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/registry/bases/reka/ui/carousel"
import { Example } from "~/registry/bases/reka/components/example"
</script>

<template>
  <Example title="With Gap">
    <Carousel class="mx-auto max-w-xs sm:max-w-sm">
      <CarouselContent class="-ml-1">
        <CarouselItem v-for="index in 5" :key="index" class="pl-1 md:basis-1/2">
          <div class="p-1">
            <Card>
              <CardContent class="flex aspect-square items-center justify-center p-6">
                <span class="text-2xl font-semibold">{{ index }}</span>
              </CardContent>
            </Card>
          </div>
        </CarouselItem>
      </CarouselContent>
      <CarouselPrevious class="hidden sm:inline-flex" />
      <CarouselNext class="hidden sm:inline-flex" />
    </Carousel>
  </Example>
</template>
```

---

## Vertical Orientation

```vue
<Carousel orientation="vertical" class="mx-auto max-w-xs">
  <CarouselContent class="h-[200px]">
    <CarouselItem v-for="index in 5" :key="index">
      <div class="p-1">Slide {{ index }}</div>
    </CarouselItem>
  </CarouselContent>
  <CarouselPrevious />
  <CarouselNext />
</Carousel>
```

---

## Loop + Align Options

```vue
<Carousel :opts="{ align: 'start', loop: true }">
  <CarouselContent>
    <CarouselItem v-for="i in 5" :key="i" class="basis-1/3">
      Slide {{ i }}
    </CarouselItem>
  </CarouselContent>
</Carousel>
```

---

## Accessing the Embla API via `@init-api`

```vue
<script setup lang="ts">
import type { CarouselApi } from "@/components/ui/carousel"
import { ref, watch } from "vue"

const api = ref<CarouselApi>()
const current = ref(0)
const total = ref(0)

function onInitApi(val: CarouselApi) {
  api.value = val
}

watch(api, (val) => {
  if (!val) return
  total.value = val.scrollSnapList().length
  current.value = val.selectedScrollSnap() + 1
  val.on("select", () => {
    current.value = val.selectedScrollSnap() + 1
  })
})
</script>

<template>
  <Carousel @init-api="onInitApi">
    <CarouselContent>
      <CarouselItem v-for="i in 5" :key="i">Slide {{ i }}</CarouselItem>
    </CarouselContent>
  </Carousel>
  <p>Slide {{ current }} of {{ total }}</p>
</template>
```

---

## Accessing the API via Template Ref

```vue
<script setup lang="ts">
import { ref } from "vue"

const carouselRef = ref()

function goToFirst() {
  carouselRef.value?.carouselApi?.scrollTo(0)
}
</script>

<template>
  <Carousel ref="carouselRef">
    <CarouselContent>
      <CarouselItem v-for="i in 5" :key="i">Slide {{ i }}</CarouselItem>
    </CarouselContent>
  </Carousel>
  <button @click="goToFirst">Go to first</button>
</template>
```

---

## Autoplay Plugin

```bash
npm install embla-carousel-autoplay
```

```vue
<script setup lang="ts">
import Autoplay from "embla-carousel-autoplay"
</script>

<template>
  <Carousel :plugins="[Autoplay({ delay: 2000 })]">
    <CarouselContent>
      <CarouselItem v-for="i in 5" :key="i">Slide {{ i }}</CarouselItem>
    </CarouselContent>
  </Carousel>
</template>
```

---

## Using Slot Props

Access navigation state directly from the default slot without a template ref:

```vue
<Carousel v-slot="{ canScrollNext, canScrollPrev, scrollNext, scrollPrev }">
  <CarouselContent>
    <CarouselItem v-for="i in 5" :key="i">Slide {{ i }}</CarouselItem>
  </CarouselContent>
  <button :disabled="!canScrollPrev" @click="scrollPrev">Prev</button>
  <button :disabled="!canScrollNext" @click="scrollNext">Next</button>
</Carousel>
```

---

## Item Sizing Reference

| Class on CarouselItem | Visible slides (approx.) |
|-----------------------|--------------------------|
| `basis-full` (default) | 1 |
| `basis-1/2` | 2 |
| `basis-1/3` | 3 |
| `basis-1/4` | 4 |

Spacing convention: negate on `CarouselContent`, apply on `CarouselItem`:

```
CarouselContent class="-ml-4"   →   CarouselItem class="pl-4"   (default)
CarouselContent class="-ml-2"   →   CarouselItem class="pl-2"
CarouselContent class="-ml-1"   →   CarouselItem class="pl-1"
```
