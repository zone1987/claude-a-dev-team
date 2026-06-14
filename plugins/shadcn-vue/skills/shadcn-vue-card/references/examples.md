# Card — Examples

## 1. CardDefault

Basic card with the default size.

```vue
<script setup lang="ts">
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
</script>

<template>
  <Card class="w-[350px]">
    <CardHeader>
      <CardTitle>Create project</CardTitle>
      <CardDescription>Deploy your new project in one-click.</CardDescription>
    </CardHeader>
    <CardContent>
      <div class="grid w-full items-center gap-4">
        <div class="flex flex-col space-y-1.5">
          <Label for="name">Name</Label>
          <Input id="name" placeholder="Name of your project" />
        </div>
        <div class="flex flex-col space-y-1.5">
          <Label for="framework">Framework</Label>
          <Select>
            <SelectTrigger id="framework">
              <SelectValue placeholder="Select" />
            </SelectTrigger>
            <SelectContent position="popper">
              <SelectItem value="next">Next.js</SelectItem>
              <SelectItem value="sveltekit">SvelteKit</SelectItem>
              <SelectItem value="astro">Astro</SelectItem>
              <SelectItem value="nuxt">Nuxt.js</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </div>
    </CardContent>
    <CardFooter class="flex justify-between">
      <Button variant="outline">Cancel</Button>
      <Button>Deploy</Button>
    </CardFooter>
  </Card>
</template>
```

---

## 2. CardSmall

Card using a smaller size variant (reduced padding via `py-4`).

```vue
<script setup lang="ts">
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
</script>

<template>
  <Card class="w-[350px] py-4">
    <CardHeader>
      <CardTitle>Create project</CardTitle>
      <CardDescription>Deploy your new project in one-click.</CardDescription>
    </CardHeader>
    <CardContent>
      <div class="grid w-full items-center gap-4">
        <div class="flex flex-col space-y-1.5">
          <Label for="name-sm">Name</Label>
          <Input id="name-sm" placeholder="Name of your project" />
        </div>
        <div class="flex flex-col space-y-1.5">
          <Label for="framework-sm">Framework</Label>
          <Select>
            <SelectTrigger id="framework-sm">
              <SelectValue placeholder="Select" />
            </SelectTrigger>
            <SelectContent position="popper">
              <SelectItem value="next">Next.js</SelectItem>
              <SelectItem value="sveltekit">SvelteKit</SelectItem>
              <SelectItem value="astro">Astro</SelectItem>
              <SelectItem value="nuxt">Nuxt.js</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </div>
    </CardContent>
    <CardFooter class="flex justify-between">
      <Button variant="outline">Cancel</Button>
      <Button>Deploy</Button>
    </CardFooter>
  </Card>
</template>
```

---

## 3. CardHeaderWithBorder

Card where the header has a bottom border. `CardHeader` applies `pb-6`
automatically when it carries the `border-b` class.

```vue
<script setup lang="ts">
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
</script>

<template>
  <Card class="w-[350px]">
    <CardHeader class="border-b">
      <CardTitle>Create project</CardTitle>
      <CardDescription>Deploy your new project in one-click.</CardDescription>
    </CardHeader>
    <CardContent class="pt-6">
      <div class="grid w-full items-center gap-4">
        <div class="flex flex-col space-y-1.5">
          <Label for="name-hb">Name</Label>
          <Input id="name-hb" placeholder="Name of your project" />
        </div>
        <div class="flex flex-col space-y-1.5">
          <Label for="framework-hb">Framework</Label>
          <Select>
            <SelectTrigger id="framework-hb">
              <SelectValue placeholder="Select" />
            </SelectTrigger>
            <SelectContent position="popper">
              <SelectItem value="next">Next.js</SelectItem>
              <SelectItem value="sveltekit">SvelteKit</SelectItem>
              <SelectItem value="astro">Astro</SelectItem>
              <SelectItem value="nuxt">Nuxt.js</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </div>
    </CardContent>
    <CardFooter class="flex justify-between">
      <Button variant="outline">Cancel</Button>
      <Button>Deploy</Button>
    </CardFooter>
  </Card>
</template>
```

---

## 4. CardFooterWithBorder

Card where the footer has a top border. `CardFooter` applies `pt-6`
automatically when it carries the `border-t` class.

```vue
<script setup lang="ts">
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
</script>

<template>
  <Card class="w-[350px]">
    <CardHeader>
      <CardTitle>Create project</CardTitle>
      <CardDescription>Deploy your new project in one-click.</CardDescription>
    </CardHeader>
    <CardContent>
      <div class="grid w-full items-center gap-4">
        <div class="flex flex-col space-y-1.5">
          <Label for="name-fb">Name</Label>
          <Input id="name-fb" placeholder="Name of your project" />
        </div>
        <div class="flex flex-col space-y-1.5">
          <Label for="framework-fb">Framework</Label>
          <Select>
            <SelectTrigger id="framework-fb">
              <SelectValue placeholder="Select" />
            </SelectTrigger>
            <SelectContent position="popper">
              <SelectItem value="next">Next.js</SelectItem>
              <SelectItem value="sveltekit">SvelteKit</SelectItem>
              <SelectItem value="astro">Astro</SelectItem>
              <SelectItem value="nuxt">Nuxt.js</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </div>
    </CardContent>
    <CardFooter class="border-t flex justify-between">
      <Button variant="outline">Cancel</Button>
      <Button>Deploy</Button>
    </CardFooter>
  </Card>
</template>
```

---

## 5. CardHeaderWithBorderSmall

Small card (reduced padding) with a bordered header.

```vue
<script setup lang="ts">
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
</script>

<template>
  <Card class="w-[350px] py-4">
    <CardHeader class="border-b">
      <CardTitle>Create project</CardTitle>
      <CardDescription>Deploy your new project in one-click.</CardDescription>
    </CardHeader>
    <CardContent class="pt-6">
      <div class="grid w-full items-center gap-4">
        <div class="flex flex-col space-y-1.5">
          <Label for="name-hbs">Name</Label>
          <Input id="name-hbs" placeholder="Name of your project" />
        </div>
        <div class="flex flex-col space-y-1.5">
          <Label for="framework-hbs">Framework</Label>
          <Select>
            <SelectTrigger id="framework-hbs">
              <SelectValue placeholder="Select" />
            </SelectTrigger>
            <SelectContent position="popper">
              <SelectItem value="next">Next.js</SelectItem>
              <SelectItem value="sveltekit">SvelteKit</SelectItem>
              <SelectItem value="astro">Astro</SelectItem>
              <SelectItem value="nuxt">Nuxt.js</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </div>
    </CardContent>
    <CardFooter class="flex justify-between">
      <Button variant="outline">Cancel</Button>
      <Button>Deploy</Button>
    </CardFooter>
  </Card>
</template>
```

---

## 6. CardFooterWithBorderSmall

Small card with a bordered footer.

```vue
<script setup lang="ts">
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
</script>

<template>
  <Card class="w-[350px] py-4">
    <CardHeader>
      <CardTitle>Create project</CardTitle>
      <CardDescription>Deploy your new project in one-click.</CardDescription>
    </CardHeader>
    <CardContent>
      <div class="grid w-full items-center gap-4">
        <div class="flex flex-col space-y-1.5">
          <Label for="name-fbs">Name</Label>
          <Input id="name-fbs" placeholder="Name of your project" />
        </div>
        <div class="flex flex-col space-y-1.5">
          <Label for="framework-fbs">Framework</Label>
          <Select>
            <SelectTrigger id="framework-fbs">
              <SelectValue placeholder="Select" />
            </SelectTrigger>
            <SelectContent position="popper">
              <SelectItem value="next">Next.js</SelectItem>
              <SelectItem value="sveltekit">SvelteKit</SelectItem>
              <SelectItem value="astro">Astro</SelectItem>
              <SelectItem value="nuxt">Nuxt.js</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </div>
    </CardContent>
    <CardFooter class="border-t flex justify-between">
      <Button variant="outline">Cancel</Button>
      <Button>Deploy</Button>
    </CardFooter>
  </Card>
</template>
```

---

## 7. CardWithImage

Card containing an overlay image. The image is placed inside `CardContent`
using z-index layering so text can sit on top of it.

```vue
<script setup lang="ts">
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
</script>

<template>
  <Card class="w-[350px] gap-0 overflow-hidden py-0">
    <div class="relative h-48 w-full">
      <img
        src="https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd?w=800&dpr=2&q=80"
        alt="Card image"
        class="h-full w-full object-cover"
      />
    </div>
    <CardHeader>
      <CardTitle>Card title</CardTitle>
      <CardDescription>Card description</CardDescription>
    </CardHeader>
    <CardContent>
      <p class="text-sm">
        Some quick example text to build on the card title and make up the bulk
        of the card's content.
      </p>
    </CardContent>
    <CardFooter>
      <Button>Go somewhere</Button>
    </CardFooter>
  </Card>
</template>
```

---

## 8. CardWithImageSmall

Same image card in the small (reduced padding) variant.

```vue
<script setup lang="ts">
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
</script>

<template>
  <Card class="w-[350px] gap-0 overflow-hidden py-0">
    <div class="relative h-36 w-full">
      <img
        src="https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd?w=800&dpr=2&q=80"
        alt="Card image"
        class="h-full w-full object-cover"
      />
    </div>
    <CardHeader class="py-4">
      <CardTitle>Card title</CardTitle>
      <CardDescription>Card description</CardDescription>
    </CardHeader>
    <CardContent class="py-0 pb-4">
      <p class="text-sm">
        Some quick example text to build on the card title and make up the bulk
        of the card's content.
      </p>
    </CardContent>
    <CardFooter class="pb-4">
      <Button>Go somewhere</Button>
    </CardFooter>
  </Card>
</template>
```

---

## 9. CardLogin

A login form inside a card.

```vue
<script setup lang="ts">
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
</script>

<template>
  <Card class="w-[350px]">
    <CardHeader>
      <CardTitle>Login</CardTitle>
      <CardDescription>
        Enter your credentials to access your account.
      </CardDescription>
    </CardHeader>
    <CardContent>
      <div class="grid gap-4">
        <div class="grid gap-2">
          <Label for="email">Email</Label>
          <Input id="email" type="email" placeholder="m@example.com" />
        </div>
        <div class="grid gap-2">
          <div class="flex items-center">
            <Label for="password">Password</Label>
            <a
              href="#"
              class="ml-auto inline-block text-sm underline-offset-4 hover:underline"
            >
              Forgot your password?
            </a>
          </div>
          <Input id="password" type="password" />
        </div>
      </div>
    </CardContent>
    <CardFooter class="flex-col gap-2">
      <Button class="w-full">Login</Button>
      <Button variant="outline" class="w-full">Login with Google</Button>
      <div class="mt-4 text-center text-sm">
        Don't have an account?
        <a href="#" class="underline underline-offset-4">Sign up</a>
      </div>
    </CardFooter>
  </Card>
</template>
```

---

## 10. CardMeetingNotes

Card using `CardAction` to place an avatar group in the top-right corner of
the header. Demonstrates the two-column CSS grid layout of `CardHeader`.

```vue
<script setup lang="ts">
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Badge } from "@/components/ui/badge"
</script>

<template>
  <Card class="w-[380px]">
    <CardHeader>
      <CardTitle>Meeting Notes</CardTitle>
      <CardDescription>Product sync — June 12, 2025</CardDescription>
      <CardAction>
        <div class="flex -space-x-2">
          <Avatar class="h-7 w-7 border-2 border-background">
            <AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" />
            <AvatarFallback>SC</AvatarFallback>
          </Avatar>
          <Avatar class="h-7 w-7 border-2 border-background">
            <AvatarImage src="https://github.com/leerob.png" alt="@leerob" />
            <AvatarFallback>LR</AvatarFallback>
          </Avatar>
          <Avatar class="h-7 w-7 border-2 border-background">
            <AvatarFallback>+3</AvatarFallback>
          </Avatar>
        </div>
      </CardAction>
    </CardHeader>
    <CardContent class="grid gap-3">
      <div class="flex items-start gap-2">
        <Badge variant="outline">Action</Badge>
        <p class="text-sm">
          Finalize design tokens for the new component library.
        </p>
      </div>
      <div class="flex items-start gap-2">
        <Badge variant="outline">Decision</Badge>
        <p class="text-sm">
          Adopt shadcn-vue as the primary UI component source.
        </p>
      </div>
      <div class="flex items-start gap-2">
        <Badge variant="outline">Note</Badge>
        <p class="text-sm">
          Follow up with the accessibility audit results next sprint.
        </p>
      </div>
    </CardContent>
  </Card>
</template>
```

---
Source: `registry/bases/reka/examples/card/`
