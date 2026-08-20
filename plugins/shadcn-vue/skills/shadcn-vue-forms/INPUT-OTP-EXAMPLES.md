# InputOTP — Beispiele

Quelle: `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/input-otp/InputOTPExample.vue`

## Contents

- [Einfach — 6 Ziffern mit Separator](#einfach-6-ziffern-mit-separator)
- [Kontrollierter Wert (v-model)](#kontrollierter-wert-v-model)
- [Deaktiviert](#deaktiviert)
- [4-stellige PIN](#4-stellige-pin)
- [Fehlerzustand](#fehlerzustand)
- [Formular mit Verifizierungskarte](#formular-mit-verifizierungskarte)

## Einfach — 6 Ziffern mit Separator

```vue
<script setup lang="ts">
import { Field, FieldLabel } from "@/registry/bases/reka/ui/field"
import {
  InputOTP,
  InputOTPGroup,
  InputOTPSeparator,
  InputOTPSlot,
} from "@/registry/bases/reka/ui/input-otp"
</script>

<template>
  <Field>
    <FieldLabel html-for="simple">Simple</FieldLabel>
    <InputOTP id="simple" :maxlength="6">
      <InputOTPGroup>
        <InputOTPSlot :index="0" />
        <InputOTPSlot :index="1" />
        <InputOTPSlot :index="2" />
      </InputOTPGroup>
      <InputOTPSeparator />
      <InputOTPGroup>
        <InputOTPSlot :index="3" />
        <InputOTPSlot :index="4" />
        <InputOTPSlot :index="5" />
      </InputOTPGroup>
    </InputOTP>
  </Field>
</template>
```

## Kontrollierter Wert (v-model)

```vue
<script setup lang="ts">
import { ref } from "vue"
import {
  InputOTP,
  InputOTPGroup,
  InputOTPSeparator,
  InputOTPSlot,
} from "@/registry/bases/reka/ui/input-otp"

const value = ref("123456")
</script>

<template>
  <InputOTP v-model="value" :maxlength="6">
    <InputOTPGroup>
      <InputOTPSlot :index="0" />
      <InputOTPSlot :index="1" />
    </InputOTPGroup>
    <InputOTPSeparator />
    <InputOTPGroup>
      <InputOTPSlot :index="2" />
      <InputOTPSlot :index="3" />
    </InputOTPGroup>
    <InputOTPSeparator />
    <InputOTPGroup>
      <InputOTPSlot :index="4" />
      <InputOTPSlot :index="5" />
    </InputOTPGroup>
  </InputOTP>
</template>
```

## Deaktiviert

```vue
<template>
  <InputOTP :maxlength="6" :disabled="true" value="123456">
    <InputOTPGroup>
      <InputOTPSlot :index="0" />
      <InputOTPSlot :index="1" />
      <InputOTPSlot :index="2" />
    </InputOTPGroup>
    <InputOTPSeparator />
    <InputOTPGroup>
      <InputOTPSlot :index="3" />
      <InputOTPSlot :index="4" />
      <InputOTPSlot :index="5" />
    </InputOTPGroup>
  </InputOTP>
</template>
```

## 4-stellige PIN

```vue
<template>
  <Field>
    <FieldLabel html-for="four-digits">4 Digits</FieldLabel>
    <FieldDescription>Common pattern for PIN codes.</FieldDescription>
    <InputOTP id="four-digits" :maxlength="4">
      <InputOTPGroup>
        <InputOTPSlot :index="0" />
        <InputOTPSlot :index="1" />
        <InputOTPSlot :index="2" />
        <InputOTPSlot :index="3" />
      </InputOTPGroup>
    </InputOTP>
  </Field>
</template>
```

## Fehlerzustand

```vue
<script setup lang="ts">
import { ref } from "vue"
import {
  Field, FieldDescription, FieldError, FieldLabel,
} from "@/registry/bases/reka/ui/field"
import {
  InputOTP, InputOTPGroup, InputOTPSeparator, InputOTPSlot,
} from "@/registry/bases/reka/ui/input-otp"

const value = ref("000000")
</script>

<template>
  <Field>
    <FieldLabel html-for="invalid">Invalid State</FieldLabel>
    <FieldDescription>Example showing the invalid error state.</FieldDescription>
    <InputOTP id="invalid" v-model="value" :maxlength="6">
      <InputOTPGroup>
        <InputOTPSlot :index="0" :aria-invalid="true" />
        <InputOTPSlot :index="1" :aria-invalid="true" />
      </InputOTPGroup>
      <InputOTPSeparator />
      <InputOTPGroup>
        <InputOTPSlot :index="2" :aria-invalid="true" />
        <InputOTPSlot :index="3" :aria-invalid="true" />
      </InputOTPGroup>
      <InputOTPSeparator />
      <InputOTPGroup>
        <InputOTPSlot :index="4" :aria-invalid="true" />
        <InputOTPSlot :index="5" :aria-invalid="true" />
      </InputOTPGroup>
    </InputOTP>
    <FieldError :errors="[{ message: 'Invalid code. Please try again.' }]" />
  </Field>
</template>
```

## Formular mit Verifizierungskarte

```vue
<script setup lang="ts">
import { Button } from "@/registry/bases/reka/ui/button"
import {
  Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle,
} from "@/registry/bases/reka/ui/card"
import {
  Field, FieldDescription, FieldLabel,
} from "@/registry/bases/reka/ui/field"
import {
  InputOTP, InputOTPGroup, InputOTPSeparator, InputOTPSlot,
} from "@/registry/bases/reka/ui/input-otp"
</script>

<template>
  <Card class="mx-auto max-w-md">
    <CardHeader>
      <CardTitle>Verify your login</CardTitle>
      <CardDescription>
        Enter the verification code sent to m@example.com.
      </CardDescription>
    </CardHeader>
    <CardContent>
      <form>
        <Field>
          <div class="flex items-center justify-between">
            <FieldLabel html-for="otp-verification">Verification code</FieldLabel>
            <Button variant="outline" size="xs">Resend Code</Button>
          </div>
          <InputOTP id="otp-verification" :maxlength="6" :required="true">
            <InputOTPGroup>
              <InputOTPSlot :index="0" />
              <InputOTPSlot :index="1" />
              <InputOTPSlot :index="2" />
            </InputOTPGroup>
            <InputOTPSeparator />
            <InputOTPGroup>
              <InputOTPSlot :index="3" />
              <InputOTPSlot :index="4" />
              <InputOTPSlot :index="5" />
            </InputOTPGroup>
          </InputOTP>
          <FieldDescription>
            <a href="#">I no longer have access to this email address.</a>
          </FieldDescription>
        </Field>
      </form>
    </CardContent>
    <CardFooter class="flex-col gap-2">
      <Button type="submit" class="w-full">Verify</Button>
    </CardFooter>
  </Card>
</template>
```

Quellen:
- `/tmp/shadcn-vue-repo/apps/v4/registry/bases/reka/examples/input-otp/InputOTPExample.vue`
- `/tmp/shadcn-vue-repo/apps/v4/content/docs/components/input-otp.md`
