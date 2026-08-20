# Examples

## Basic (Horizontal)

Controlled stepper with icon indicators.

```vue
<!-- StepperBasic.vue -->
<script setup lang="ts">
import { ref } from "vue"
import {
  Stepper,
  StepperDescription,
  StepperIndicator,
  StepperItem,
  StepperSeparator,
  StepperTitle,
  StepperTrigger,
} from "@/components/ui/stepper"

const currentStep = ref(1)
</script>

<template>
  <Stepper v-model="currentStep" class="w-full">
    <StepperItem :step="1">
      <StepperTrigger>
        <StepperIndicator>1</StepperIndicator>
        <div class="flex flex-col text-left">
          <StepperTitle>Account</StepperTitle>
          <StepperDescription>Create your account</StepperDescription>
        </div>
      </StepperTrigger>
      <StepperSeparator />
    </StepperItem>

    <StepperItem :step="2">
      <StepperTrigger>
        <StepperIndicator>2</StepperIndicator>
        <div class="flex flex-col text-left">
          <StepperTitle>Profile</StepperTitle>
          <StepperDescription>Set up your profile</StepperDescription>
        </div>
      </StepperTrigger>
      <StepperSeparator />
    </StepperItem>

    <StepperItem :step="3">
      <StepperTrigger>
        <StepperIndicator>3</StepperIndicator>
        <div class="flex flex-col text-left">
          <StepperTitle>Complete</StepperTitle>
          <StepperDescription>Finish setup</StepperDescription>
        </div>
      </StepperTrigger>
    </StepperItem>
  </Stepper>
</template>
```

## Vertical

Same stepper with `orientation="vertical"`.

```vue
<!-- StepperVertical.vue -->
<script setup lang="ts">
import { ref } from "vue"
import {
  Stepper,
  StepperDescription,
  StepperIndicator,
  StepperItem,
  StepperSeparator,
  StepperTitle,
  StepperTrigger,
} from "@/components/ui/stepper"

const currentStep = ref(1)
</script>

<template>
  <Stepper v-model="currentStep" orientation="vertical" class="w-full">
    <StepperItem :step="1">
      <StepperTrigger>
        <StepperIndicator>1</StepperIndicator>
        <div class="flex flex-col text-left">
          <StepperTitle>Account</StepperTitle>
          <StepperDescription>Create your account</StepperDescription>
        </div>
      </StepperTrigger>
      <StepperSeparator />
    </StepperItem>

    <StepperItem :step="2">
      <StepperTrigger>
        <StepperIndicator>2</StepperIndicator>
        <div class="flex flex-col text-left">
          <StepperTitle>Profile</StepperTitle>
          <StepperDescription>Set up your profile</StepperDescription>
        </div>
      </StepperTrigger>
      <StepperSeparator />
    </StepperItem>

    <StepperItem :step="3">
      <StepperTrigger>
        <StepperIndicator>3</StepperIndicator>
        <div class="flex flex-col text-left">
          <StepperTitle>Complete</StepperTitle>
          <StepperDescription>Finish setup</StepperDescription>
        </div>
      </StepperTrigger>
    </StepperItem>
  </Stepper>
</template>
```

Sources:
- `registry/bases/reka/examples/stepper/StepperBasic.vue`
- `registry/bases/reka/examples/stepper/StepperVertical.vue`
