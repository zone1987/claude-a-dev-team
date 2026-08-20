# Alert Dialog — Examples

## Demo

```tsx
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/registry/new-york-v4/ui/alert-dialog"
import { Button } from "@/registry/new-york-v4/ui/button"

export default function AlertDialogDemo() {
  return (
    <AlertDialog>
      <AlertDialogTrigger asChild>
        <Button variant="outline">Show Dialog</Button>
      </AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
          <AlertDialogDescription>
            This action cannot be undone. This will permanently delete your
            account and remove your data from our servers.
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Cancel</AlertDialogCancel>
          <AlertDialogAction>Continue</AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  )
}
```

## Small dialog

```tsx
<AlertDialogContent size="sm">
  {/* ... */}
</AlertDialogContent>
```

## With media icon

```tsx
<AlertDialogContent>
  <AlertDialogHeader>
    <AlertDialogMedia>
      <TrashIcon className="size-8" />
    </AlertDialogMedia>
    <AlertDialogTitle>Delete account?</AlertDialogTitle>
    <AlertDialogDescription>
      This action is permanent.
    </AlertDialogDescription>
  </AlertDialogHeader>
  <AlertDialogFooter>
    <AlertDialogCancel>Cancel</AlertDialogCancel>
    <AlertDialogAction variant="destructive">Delete</AlertDialogAction>
  </AlertDialogFooter>
</AlertDialogContent>
```

---
Source: `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/alert-dialog-demo.tsx`
