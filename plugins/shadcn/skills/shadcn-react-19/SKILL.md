---
name: shadcn-react-19
description: >
  shadcn/ui with React 19 and Next.js 15 — peer dependency issues, npm flags
  --force and --legacy-peer-deps, React 19 upgrade status table, recharts
  react-is override. Use when asked about React 19 shadcn, npm peer dependency
  error, ERESOLVE, next.js 15 shadcn, react 19 compatibility.
---

# shadcn/ui — React 19 + Next.js 15

> Note: Full React 19 + Tailwind v4 support is in the `latest` release.
> This primarily covers npm peer dependency resolution for older packages.

## The problem

React 19 may not yet be listed as a peer dependency in some packages, causing
npm install errors:

```
npm error ERESOLVE unable to resolve dependency tree
npm error Found: react@19.0.0-rc-...
```

Note: This is npm only. pnpm and bun show only a silent warning.

## Solutions

### Solution 1: --force or --legacy-peer-deps

```bash
npm i <package> --force
npm i <package> --legacy-peer-deps
```

The shadcn CLI prompts you to choose:
```
? How would you like to proceed?
❯   Use --force
    Use --legacy-peer-deps
```

- `--force`: ignores and overrides dependency conflicts
- `--legacy-peer-deps`: skips strict peer dependency checks

### Solution 2: Downgrade to React 18

```bash
npm i react@18 react-dom@18
```

## React 19 support status

| Package | Status | Note |
|---------|--------|------|
| radix-ui | Works | |
| lucide-react | Works | |
| class-variance-authority | Works | Does not list React 19 as peer dep |
| tailwindcss-animate | Works | Does not list React 19 as peer dep |
| embla-carousel-react | Works | |
| recharts | Works | See note below |
| react-hook-form | Works | |
| react-resizable-panels | Works | |
| sonner | Works | |
| react-day-picker | Works | With flag for npm |
| input-otp | Works | |
| vaul | Works | |
| @radix-ui/react-icons | Works | |
| cmdk | Works | |

## Recharts + React 19 override

```json
// package.json
{
  "overrides": {
    "react-is": "^19.0.0-rc-..."
  }
}
```
Then run: `npm install --legacy-peer-deps`

Note: `react-is` version must match the React 19 version you are using.

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/react-19.mdx`
