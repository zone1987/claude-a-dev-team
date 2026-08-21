# Accordion — Examples

## Contents

- [Basic](#basic)
- [Multiple (allow multiple open at once)](#multiple-allow-multiple-open-at-once)
- [With Disabled Item](#with-disabled-item)
- [In Card (FAQ layout)](#in-card-faq-layout)

## Basic

Three-item single-open accordion.

```vue
<script setup lang="ts">
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"

const items = [
  { value: "item-1", trigger: "Is it accessible?", content: "Yes. It adheres to the WAI-ARIA design pattern." },
  { value: "item-2", trigger: "Is it styled?", content: "Yes. It comes with default styles that matches the other components' aesthetic." },
  { value: "item-3", trigger: "Is it animated?", content: "Yes. It's animated by default, but you can disable it if you prefer." },
]
</script>

<template>
  <Accordion type="single" collapsible class="mx-auto max-w-lg">
    <AccordionItem v-for="item in items" :key="item.value" :value="item.value">
      <AccordionTrigger>{{ item.trigger }}</AccordionTrigger>
      <AccordionContent>{{ item.content }}</AccordionContent>
    </AccordionItem>
  </Accordion>
</template>
```

## Multiple (allow multiple open at once)

```vue
<template>
  <Accordion type="multiple" class="mx-auto max-w-lg">
    <AccordionItem value="item-1">
      <AccordionTrigger>What are the key considerations for enterprise authentication?</AccordionTrigger>
      <AccordionContent>Implementing a robust enterprise authentication system requires careful consideration of multiple factors...</AccordionContent>
    </AccordionItem>
    <AccordionItem value="item-2">
      <AccordionTrigger>How does distributed system architecture handle eventual consistency?</AccordionTrigger>
      <AccordionContent>Modern distributed systems employ various strategies to maintain data consistency...</AccordionContent>
    </AccordionItem>
  </Accordion>
</template>
```

## With Disabled Item

```vue
<template>
  <Accordion type="single" collapsible class="mx-auto max-w-lg overflow-hidden border">
    <AccordionItem value="item-1" class="p-1">
      <AccordionTrigger>Can I access my account history?</AccordionTrigger>
      <AccordionContent>Yes, you can view your complete account history...</AccordionContent>
    </AccordionItem>
    <AccordionItem value="item-2" :disabled="true" class="p-1">
      <AccordionTrigger>Premium feature information</AccordionTrigger>
      <AccordionContent>This section contains information about premium features.</AccordionContent>
    </AccordionItem>
    <AccordionItem value="item-3" class="p-1">
      <AccordionTrigger>How do I update my email address?</AccordionTrigger>
      <AccordionContent>You can update your email address in your account settings.</AccordionContent>
    </AccordionItem>
  </Accordion>
</template>
```

## In Card (FAQ layout)

```vue
<script setup lang="ts">
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"

const items = [
  { value: "plans", trigger: "What subscription plans do you offer?" },
  { value: "billing", trigger: "How does billing work?" },
  { value: "cancel", trigger: "How do I cancel my subscription?" },
]
</script>

<template>
  <Card class="mx-auto w-full max-w-lg gap-4">
    <CardHeader>
      <CardTitle>Subscription & Billing</CardTitle>
      <CardDescription>Common questions about your account</CardDescription>
    </CardHeader>
    <CardContent>
      <Accordion type="single" collapsible default-value="plans">
        <AccordionItem v-for="item in items" :key="item.value" :value="item.value">
          <AccordionTrigger>{{ item.trigger }}</AccordionTrigger>
          <AccordionContent>
            Answer to {{ item.trigger }}
          </AccordionContent>
        </AccordionItem>
      </Accordion>
    </CardContent>
  </Card>
</template>
```

---
Source: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/accordion/`
