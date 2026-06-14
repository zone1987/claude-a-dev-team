# Aspect Ratio — Examples

## Demo (16:9 image)

```tsx
import Image from "next/image"
import { AspectRatio } from "@/registry/new-york-v4/ui/aspect-ratio"

export default function AspectRatioDemo() {
  return (
    <AspectRatio ratio={16 / 9} className="rounded-lg bg-muted">
      <Image
        src="https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd?w=800&dpr=2&q=80"
        alt="Photo by Drew Beamer"
        fill
        className="h-full w-full rounded-lg object-cover dark:brightness-[0.2] dark:grayscale"
      />
    </AspectRatio>
  )
}
```

## Square (1:1)

```tsx
<AspectRatio ratio={1 / 1}>
  <Image src="..." alt="Square image" fill className="object-cover" />
</AspectRatio>
```

## Portrait (9:16)

```tsx
<AspectRatio ratio={9 / 16}>
  <Image src="..." alt="Portrait image" fill className="object-cover" />
</AspectRatio>
```

## With video

```tsx
<AspectRatio ratio={16 / 9}>
  <video src="..." className="size-full object-cover" controls />
</AspectRatio>
```

---
Source: `/tmp/shadcn-repo/apps/v4/registry/new-york-v4/examples/aspect-ratio-demo.tsx`
