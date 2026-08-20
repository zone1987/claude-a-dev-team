# shadcn/ui — Laravel Installation

The shadcn CLI does NOT scaffold a new Laravel app. Create one first, then
configure shadcn/ui.

## Step 1 — Create Laravel app with React starter kit
```bash
laravel new my-app
# Select the React starter kit when prompted
cd my-app
```

## Option A: Use shadcn/create

1. Open https://ui.shadcn.com/create?template=laravel
2. Build preset, copy command:
   ```bash
   npx shadcn@latest init --preset [CODE] --template laravel
   ```
3. When asked to overwrite `components.json` and components, choose Yes.

## Option B: Use the CLI directly

```bash
npx shadcn@latest init
# When asked to overwrite, choose Yes
```

## Add components
```bash
npx shadcn@latest add switch
```

Components are placed in `resources/js/components/ui/`.

```tsx
// resources/js/pages/index.tsx
import { Switch } from "@/components/ui/switch"

const MyPage = () => {
  return (
    <div>
      <Switch />
    </div>
  )
}

export default MyPage
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/installation/laravel.mdx`
