# Examples

Source: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/radio-group/`

---

## Basic

`RadioGroupBasic.vue` — three mutually exclusive options with horizontal
`Field` / `FieldLabel` layout.

```vue
<script setup lang="ts">
import { Field, FieldLabel } from "@/registry/bases/reka/ui/field"
import { RadioGroup, RadioGroupItem } from "@/registry/bases/reka/ui/radio-group"
</script>

<template>
  <RadioGroup default-value="comfortable">
    <Field orientation="horizontal">
      <RadioGroupItem id="r1" value="default" />
      <FieldLabel html-for="r1" class="font-normal">
        Default
      </FieldLabel>
    </Field>
    <Field orientation="horizontal">
      <RadioGroupItem id="r2" value="comfortable" />
      <FieldLabel html-for="r2" class="font-normal">
        Comfortable
      </FieldLabel>
    </Field>
    <Field orientation="horizontal">
      <RadioGroupItem id="r3" value="compact" />
      <FieldLabel html-for="r3" class="font-normal">
        Compact
      </FieldLabel>
    </Field>
  </RadioGroup>
</template>
```

---

## With Descriptions

`RadioGroupWithDescriptions.vue` — each option shows a title and a
`FieldDescription` subtitle. The entire `Field` is wrapped in `FieldLabel`
so clicking anywhere selects the option.

```vue
<script setup lang="ts">
import {
  Field,
  FieldContent,
  FieldDescription,
  FieldLabel,
} from "@/registry/bases/reka/ui/field"
import { RadioGroup, RadioGroupItem } from "@/registry/bases/reka/ui/radio-group"
</script>

<template>
  <RadioGroup default-value="plus">
    <FieldLabel html-for="plus-plan">
      <Field orientation="horizontal">
        <FieldContent>
          <div class="font-medium">
            Plus
          </div>
          <FieldDescription>
            For individuals and small teams
          </FieldDescription>
        </FieldContent>
        <RadioGroupItem id="plus-plan" value="plus" />
      </Field>
    </FieldLabel>
    <FieldLabel html-for="pro-plan">
      <Field orientation="horizontal">
        <FieldContent>
          <div class="font-medium">
            Pro
          </div>
          <FieldDescription>For growing businesses</FieldDescription>
        </FieldContent>
        <RadioGroupItem id="pro-plan" value="pro" />
      </Field>
    </FieldLabel>
    <FieldLabel html-for="enterprise-plan">
      <Field orientation="horizontal">
        <FieldContent>
          <div class="font-medium">
            Enterprise
          </div>
          <FieldDescription>
            For large teams and enterprises
          </FieldDescription>
        </FieldContent>
        <RadioGroupItem id="enterprise-plan" value="enterprise" />
      </Field>
    </FieldLabel>
  </RadioGroup>
</template>
```

---

## With FieldSet

`RadioGroupWithFieldSet.vue` — wraps the group in a `FieldSet` /
`FieldLegend` for a proper accessible group label with description.

```vue
<script setup lang="ts">
import {
  Field,
  FieldDescription,
  FieldLabel,
  FieldLegend,
  FieldSet,
} from "@/registry/bases/reka/ui/field"
import { RadioGroup, RadioGroupItem } from "@/registry/bases/reka/ui/radio-group"
</script>

<template>
  <FieldSet>
    <FieldLegend>Battery Level</FieldLegend>
    <FieldDescription>
      Choose your preferred battery level.
    </FieldDescription>
    <RadioGroup default-value="medium">
      <Field orientation="horizontal">
        <RadioGroupItem id="battery-high" value="high" />
        <FieldLabel html-for="battery-high" class="font-normal">
          High
        </FieldLabel>
      </Field>
      <Field orientation="horizontal">
        <RadioGroupItem id="battery-medium" value="medium" />
        <FieldLabel html-for="battery-medium" class="font-normal">
          Medium
        </FieldLabel>
      </Field>
      <Field orientation="horizontal">
        <RadioGroupItem id="battery-low" value="low" />
        <FieldLabel html-for="battery-low" class="font-normal">
          Low
        </FieldLabel>
      </Field>
    </RadioGroup>
  </FieldSet>
</template>
```

---

## Grid Layout

`RadioGroupGrid.vue` — uses a two-column grid class on `RadioGroup` to
lay out the options side by side.

```vue
<script setup lang="ts">
import { Field, FieldLabel } from "@/registry/bases/reka/ui/field"
import { RadioGroup, RadioGroupItem } from "@/registry/bases/reka/ui/radio-group"
</script>

<template>
  <RadioGroup default-value="medium" class="grid grid-cols-2 gap-2">
    <FieldLabel html-for="size-small">
      <Field orientation="horizontal">
        <RadioGroupItem id="size-small" value="small" />
        <div class="font-medium">
          Small
        </div>
      </Field>
    </FieldLabel>
    <FieldLabel html-for="size-medium">
      <Field orientation="horizontal">
        <RadioGroupItem id="size-medium" value="medium" />
        <div class="font-medium">
          Medium
        </div>
      </Field>
    </FieldLabel>
    <FieldLabel html-for="size-large">
      <Field orientation="horizontal">
        <RadioGroupItem id="size-large" value="large" />
        <div class="font-medium">
          Large
        </div>
      </Field>
    </FieldLabel>
    <FieldLabel html-for="size-xlarge">
      <Field orientation="horizontal">
        <RadioGroupItem id="size-xlarge" value="xlarge" />
        <div class="font-medium">
          X-Large
        </div>
      </Field>
    </FieldLabel>
  </RadioGroup>
</template>
```

---

## Disabled

`RadioGroupDisabled.vue` — the entire group is disabled via `:disabled="true"`
on the `RadioGroup` root.

```vue
<script setup lang="ts">
import { Field, FieldLabel } from "@/registry/bases/reka/ui/field"
import { RadioGroup, RadioGroupItem } from "@/registry/bases/reka/ui/radio-group"
</script>

<template>
  <RadioGroup default-value="option2" :disabled="true">
    <Field orientation="horizontal">
      <RadioGroupItem id="disabled-1" value="option1" />
      <FieldLabel html-for="disabled-1" class="font-normal">
        Option 1
      </FieldLabel>
    </Field>
    <Field orientation="horizontal">
      <RadioGroupItem id="disabled-2" value="option2" />
      <FieldLabel html-for="disabled-2" class="font-normal">
        Option 2
      </FieldLabel>
    </Field>
    <Field orientation="horizontal">
      <RadioGroupItem id="disabled-3" value="option3" />
      <FieldLabel html-for="disabled-3" class="font-normal">
        Option 3
      </FieldLabel>
    </Field>
  </RadioGroup>
</template>
```

---

## Invalid State

`RadioGroupInvalid.vue` — demonstrates the error/invalid visual state by
setting `data-invalid` on each `Field` and `aria-invalid="true"` on each
`RadioGroupItem`.

```vue
<script setup lang="ts">
import {
  Field,
  FieldDescription,
  FieldLabel,
  FieldLegend,
  FieldSet,
} from "@/registry/bases/reka/ui/field"
import { RadioGroup, RadioGroupItem } from "@/registry/bases/reka/ui/radio-group"
</script>

<template>
  <FieldSet>
    <FieldLegend>Notification Preferences</FieldLegend>
    <FieldDescription>
      Choose how you want to receive notifications.
    </FieldDescription>
    <RadioGroup default-value="email">
      <Field orientation="horizontal" data-invalid>
        <RadioGroupItem id="invalid-email" value="email" :aria-invalid="true" />
        <FieldLabel html-for="invalid-email" class="font-normal">
          Email only
        </FieldLabel>
      </Field>
      <Field orientation="horizontal" data-invalid>
        <RadioGroupItem id="invalid-sms" value="sms" :aria-invalid="true" />
        <FieldLabel html-for="invalid-sms" class="font-normal">
          SMS only
        </FieldLabel>
      </Field>
      <Field orientation="horizontal" data-invalid>
        <RadioGroupItem id="invalid-both" value="both" :aria-invalid="true" />
        <FieldLabel html-for="invalid-both" class="font-normal">
          Both Email &amp; SMS
        </FieldLabel>
      </Field>
    </RadioGroup>
  </FieldSet>
</template>
```
