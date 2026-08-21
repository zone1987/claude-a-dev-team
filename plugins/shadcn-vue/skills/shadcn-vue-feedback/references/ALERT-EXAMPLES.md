# Alert — Examples

## Basic (title only / title + description / description only)

```vue
<script setup lang="ts">
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
</script>

<template>
  <div class="flex flex-col gap-4">
    <Alert>
      <AlertTitle>Success! Your changes have been saved.</AlertTitle>
    </Alert>
    <Alert>
      <AlertTitle>Success! Your changes have been saved.</AlertTitle>
      <AlertDescription>This is an alert with title and description.</AlertDescription>
    </Alert>
    <Alert>
      <AlertDescription>This one has a description only. No title. No icon.</AlertDescription>
    </Alert>
  </div>
</template>
```

## With Icons

Place an SVG directly as the first child — the grid layout adjusts automatically.

```vue
<template>
  <div class="flex flex-col gap-4">
    <Alert>
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
        fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10" />
        <line x1="12" x2="12" y1="8" y2="12" />
        <line x1="12" x2="12.01" y1="16" y2="16" />
      </svg>
      <AlertTitle>Let's try one with icon, title and a <a href="#">link</a>.</AlertTitle>
    </Alert>
    <Alert>
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
        fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10" />
        <line x1="12" x2="12" y1="8" y2="12" />
        <line x1="12" x2="12.01" y1="16" y2="16" />
      </svg>
      <AlertTitle>Success! Your changes have been saved</AlertTitle>
      <AlertDescription>This is an alert with icon, title and description.</AlertDescription>
    </Alert>
  </div>
</template>
```

## Destructive Variant

```vue
<template>
  <div class="flex flex-col gap-4">
    <Alert variant="destructive">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
        fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10" />
        <line x1="12" x2="12" y1="8" y2="12" />
        <line x1="12" x2="12.01" y1="16" y2="16" />
      </svg>
      <AlertTitle>Something went wrong!</AlertTitle>
      <AlertDescription>Your session has expired. Please log in again.</AlertDescription>
    </Alert>
    <Alert variant="destructive">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
        fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10" />
        <line x1="12" x2="12" y1="8" y2="12" />
        <line x1="12" x2="12.01" y1="16" y2="16" />
      </svg>
      <AlertTitle>Unable to process your payment.</AlertTitle>
      <AlertDescription>
        <p>Please verify your <a href="#">billing information</a> and try again.</p>
        <ul class="list-inside list-disc">
          <li>Check your card details</li>
          <li>Ensure sufficient funds</li>
          <li>Verify billing address</li>
        </ul>
      </AlertDescription>
    </Alert>
  </div>
</template>
```

---
Source: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/alert/`
