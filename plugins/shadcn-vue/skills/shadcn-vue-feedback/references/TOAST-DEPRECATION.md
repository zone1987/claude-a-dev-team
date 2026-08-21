# Toast — Deprecation Notice

## Status

The `toast` component has been removed from shadcn-vue v4 and is **deprecated**.

From the official docs:

> "The toast component has been deprecated. See the sonner documentation
> for more information."

Source: `content/docs/components/toast.md` (reka base)

## Replacement

Use **sonner** (`vue-sonner`) instead. See:

- Skill: `shadcn-vue-sonner`
- Official docs: https://www.shadcn-vue.com/docs/components/sonner
- vue-sonner: https://vue-sonner.vercel.app/

## Old Documentation

The v3 toast component (with `useToast` hook, `Toaster`, `Toast`,
`ToastAction`, `ToastClose`, `ToastDescription`, `ToastProvider`,
`ToastTitle`, `ToastViewport`) is documented at:

https://v3.shadcn-vue.com/docs/components/toast

## Comparison

| Feature | Old toast (v3) | Sonner (v4) |
|---------|---------------|-------------|
| API | `useToast()` hook | `toast()` function |
| Setup | `<ToastProvider>` + `<Toaster>` | `<Toaster>` only |
| CSS | included in component | `import 'vue-sonner/style.css'` |
| Types | success/destructive | success/error/info/warning/loading |
| Promise | no | `toast.promise()` |
| Stacking | no | yes (stackable) |

Source: `content/docs/components/toast.md`
