---
name: shadcn-cli
description: >
  shadcn/ui CLI — all commands and options: init, add, apply, preset,
  view, search, build, docs, info, migrate, eject. Use when asked about
  shadcn CLI, npx shadcn, shadcn init flags, shadcn add, shadcn migrate,
  shadcn build registry, shadcn eject, CLI options.
---

# shadcn/ui — CLI Reference

## init

Initialise configuration and dependencies. Can also create new projects.

```bash
npx shadcn@latest init
npx shadcn@latest create   # alias for init
```

**All options:**
```
Usage: shadcn init [options] [components...]

Options:
  -t, --template <template>  template: next, vite, start, react-router, laravel, astro
  -b, --base <base>          component library: radix, base
  -p, --preset [name]        use a preset configuration
  -y, --yes                  skip confirmation prompt (default: true)
  -d, --defaults             use defaults: --template=next --preset=nova
  -f, --force                force overwrite of existing configuration
  -c, --cwd <cwd>            working directory (default: current)
  -n, --name <name>          name for new project
  -s, --silent               mute output
  --css-variables            use CSS variables for theming (default: true)
  --no-css-variables         do not use CSS variables
  --monorepo                 scaffold monorepo project
  --no-monorepo              skip monorepo prompt
  --rtl                      enable RTL support
  --no-rtl                   disable RTL support
  --pointer                  enable pointer cursor for buttons
  --no-pointer               disable pointer cursor
  --reinstall                re-install existing UI components
  --no-reinstall             do not re-install existing UI components
```

## add

Add components and dependencies.

```bash
npx shadcn@latest add button
npx shadcn@latest add button card dialog
npx shadcn@latest add @acme/auth @v0/dashboard
```

**Options:**
```
Usage: shadcn add [options] [components...]

Options:
  -y, --yes            skip confirmation (default: false)
  -o, --overwrite      overwrite existing files (default: false)
  -c, --cwd <cwd>      working directory
  -a, --all            add all available components
  -p, --path <path>    path to add the component to
  -s, --silent         mute output
  --dry-run            preview changes without writing files
  --diff [path]        show diff for a file
  --view [path]        show file contents
```

## Reference files

- [references/commands.md](references/commands.md)

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/cli.mdx`
