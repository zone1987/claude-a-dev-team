# Avatar — API Reference

Full reka-ui primitive docs: https://reka-ui.com/docs/components/avatar#api-reference

---

## Avatar

Wraps `AvatarRoot` from reka-ui. Default size is `size-8` (32 × 32 px) with `rounded-full`.

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `HTMLAttributes['class']` | — | Tailwind / CSS classes merged with the default `size-8 rounded-full` styles. Pass e.g. `"size-12"` to change the size. |

**Slots:** default — place `AvatarImage` and `AvatarFallback` here.

**Data attribute:** `data-slot="avatar"` (on the root element).

---

## AvatarImage

Wraps `AvatarImage` from reka-ui. The image is rendered with `aspect-square size-full`. It stays hidden until the browser has fully loaded the image; `AvatarFallback` is shown in the meantime.

Accepts all props from `AvatarImageProps` (reka-ui):

| Prop | Type | Required | Description |
|---|---|---|---|
| `src` | `string` | yes | URL of the avatar image |
| `alt` | `string` | recommended | Accessible alt text for the image |

Additional native `<img>` attributes can be passed via `v-bind`.

**Data attribute:** `data-slot="avatar-image"`.

---

## AvatarFallback

Wraps `AvatarFallback` from reka-ui. Shown while the image loads or when it fails. Background defaults to `bg-muted`, content is centred.

Accepts all props from `AvatarFallbackProps` (reka-ui) plus:

| Prop | Type | Default | Description |
|---|---|---|---|
| `class` | `HTMLAttributes['class']` | — | Tailwind / CSS classes merged with the default `bg-muted flex size-full items-center justify-center rounded-full` styles. |
| `delayMs` | `number` | `0` | Milliseconds to wait before showing the fallback. Avoids a flash on fast connections. |

The `class` prop is stripped from the delegated props via `reactiveOmit` so it is not forwarded to the underlying element twice.

**Slots:** default — place text initials, an icon, or any content.

**Data attribute:** `data-slot="avatar-fallback"`.
