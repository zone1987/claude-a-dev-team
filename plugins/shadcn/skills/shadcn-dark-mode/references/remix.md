# Dark Mode — Remix

Uses `remix-themes` for server-side theme storage in a session cookie.

## Step 1 — Modify tailwind.css

Add `:root[class~="dark"]` to support the `dark` class on `<html>`:

```css
.dark,
:root[class~="dark"] {
  /* dark mode variables */
}
```

## Step 2 — Install remix-themes

```bash
npm install remix-themes
```

## Step 3 — Create session storage and resolver

```tsx
// app/sessions.server.tsx
import { createThemeSessionResolver } from "remix-themes"

const isProduction = process.env.NODE_ENV === "production"

const sessionStorage = createCookieSessionStorage({
  cookie: {
    name: "theme",
    path: "/",
    httpOnly: true,
    sameSite: "lax",
    secrets: ["s3cr3t"],
    ...(isProduction
      ? { domain: "your-production-domain.com", secure: true }
      : {}),
  },
})

export const themeSessionResolver = createThemeSessionResolver(sessionStorage)
```

## Step 4 — Set up Remix Themes in root.tsx

```tsx
// app/root.tsx
import clsx from "clsx"
import { PreventFlashOnWrongTheme, ThemeProvider, useTheme } from "remix-themes"
import { themeSessionResolver } from "./sessions.server"

export async function loader({ request }: LoaderFunctionArgs) {
  const { getTheme } = await themeSessionResolver(request)
  return { theme: getTheme() }
}

export default function AppWithProviders() {
  const data = useLoaderData<typeof loader>()
  return (
    <ThemeProvider specifiedTheme={data.theme} themeAction="/action/set-theme">
      <App />
    </ThemeProvider>
  )
}

export function App() {
  const data = useLoaderData<typeof loader>()
  const [theme] = useTheme()
  return (
    <html lang="en" className={clsx(theme)}>
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <Meta />
        <PreventFlashOnWrongTheme ssrTheme={Boolean(data.theme)} />
        <Links />
      </head>
      <body>
        <Outlet />
        <ScrollRestoration />
        <Scripts />
        <LiveReload />
      </body>
    </html>
  )
}
```

## Step 5 — Create action route

```tsx
// app/routes/action.set-theme.ts
import { createThemeAction } from "remix-themes"
import { themeSessionResolver } from "./sessions.server"

export const action = createThemeAction(themeSessionResolver)
```

## Step 6 — Mode toggle

```tsx
// components/mode-toggle.tsx
import { Moon, Sun } from "lucide-react"
import { Theme, useTheme } from "remix-themes"
import { Button } from "./ui/button"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "./ui/dropdown-menu"

export function ModeToggle() {
  const [, setTheme] = useTheme()

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" size="icon">
          <Sun className="h-[1.2rem] w-[1.2rem] scale-100 rotate-0 transition-all dark:scale-0 dark:-rotate-90" />
          <Moon className="absolute h-[1.2rem] w-[1.2rem] scale-0 rotate-90 transition-all dark:scale-100 dark:rotate-0" />
          <span className="sr-only">Toggle theme</span>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <DropdownMenuItem onClick={() => setTheme(Theme.LIGHT)}>Light</DropdownMenuItem>
        <DropdownMenuItem onClick={() => setTheme(Theme.DARK)}>Dark</DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
```

Source: `/tmp/shadcn-repo/apps/v4/content/docs/dark-mode/remix.mdx`
