# API Reference

vue-sonner docs: https://vue-sonner.vercel.app/

## Toaster Props

Extends `ToasterProps` from `vue-sonner`:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `theme` | `'light' \| 'dark' \| 'system'` | `'system'` | Color theme |
| `position` | `'top-left' \| 'top-center' \| 'top-right' \| 'bottom-left' \| 'bottom-center' \| 'bottom-right'` | `'bottom-right'` | Toast position |
| `richColors` | `boolean` | `false` | Use rich semantic colors |
| `expand` | `boolean` | `false` | Expand toasts by default |
| `duration` | `number` | `4000` | Auto-dismiss duration (ms) |
| `visibleToasts` | `number` | `3` | Max visible toasts |
| `closeButton` | `boolean` | `false` | Show close button |
| `offset` | `string \| number` | — | Offset from screen edge |
| `dir` | `'ltr' \| 'rtl' \| 'auto'` | `'auto'` | Text direction |
| `class` | `string` | — | Additional CSS classes |

## Slots (icon overrides)

| Slot | Description |
|------|-------------|
| `#success-icon` | Custom success icon |
| `#info-icon` | Custom info icon |
| `#warning-icon` | Custom warning icon |
| `#error-icon` | Custom error icon |
| `#loading-icon` | Custom loading icon |
| `#close-icon` | Custom close icon |

## toast() Function

Import from `vue-sonner` directly:

```ts
import { toast } from 'vue-sonner'

toast('Message')
toast.success('Success!')
toast.error('Error!')
toast.info('Info')
toast.warning('Warning')
toast.loading('Loading...')
toast.promise(promise, { loading: '...', success: 'Done', error: 'Failed' })
toast.dismiss(id)
toast.dismiss() // dismiss all
```

### toast() Options

| Option | Type | Description |
|--------|------|-------------|
| `description` | `string` | Secondary text below title |
| `action` | `{ label: string, onClick: () => void }` | Action button |
| `cancel` | `{ label: string, onClick?: () => void }` | Cancel button |
| `id` | `string \| number` | Custom toast ID for deduplication |
| `duration` | `number` | Override auto-dismiss duration |
| `onDismiss` | `(t) => void` | Callback on dismiss |
| `onAutoClose` | `(t) => void` | Callback on auto-close |
