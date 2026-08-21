# shadcn-vue CLI Reference

```bash
npx shadcn-vue@latest <command>
```

---

## Contents

- [init](#init)
- [add](#add)
- [apply](#apply)
- [view](#view)
- [search / list](#search-list)
- [build](#build)
- [docs](#docs)
- [info](#info)
- [migrate](#migrate)

## init

Initialize configuration and dependencies for a new project. Installs dependencies,
adds the `cn` util, and configures CSS variables.

```bash
npx shadcn-vue@latest init
```

Alias: `create`

```bash
npx shadcn-vue@latest create
```

**All Options:**

```
Usage: shadcn-vue init [options] [components...]

initialize your project and install dependencies

Arguments:
  components                     names, url or local path to component

Options:
  -p, --preset <preset>          use a preset configuration or URL.
                                 (reka-vega, reka-nova, reka-maia, reka-lyra,
                                  reka-mira, reka-luma, reka-sera)
  -t, --template <template>      the template to use.
                                 (nuxt, vite, astro, laravel)
  --base <base>                  the component library base to use. (reka)
  --style <style>                the visual style to use.
                                 (vega, nova, maia, lyra, mira, luma, sera)
  --icon-library <icon-library>  the icon library to use.
                                 (lucide, tabler, hugeicons, phosphor, remixicon)
  --font <font>                  the font to use.
                                 (inter, figtree, jetbrains-mono, geist, geist-mono)
  -b, --base-color <base-color>  the base color to use.
                                 (neutral, gray, zinc, stone, slate)
  -n, --name <name>              the name for the new project.
  -d, --defaults                 use default configuration. (default: false)
  -y, --yes                      skip confirmation prompt. (default: true)
  -f, --force                    force overwrite of existing configuration. (default: false)
  -c, --cwd <cwd>                the working directory. defaults to the current directory.
  -s, --silent                   mute output. (default: false)
  --src-dir                      use the src directory when creating a new project.
                                 (default: false)
  --no-src-dir                   do not use the src directory when creating a new project.
  --reinstall                    re-install existing UI components.
  --no-reinstall                 do not re-install existing UI components.
  --rtl                          enable RTL support.
  --no-rtl                       disable RTL support.
  --pointer                      enable pointer cursor for buttons.
  --no-pointer                   disable pointer cursor for buttons.
  --css-variables                use css variables for theming. (default: true)
  --no-css-variables             do not use css variables for theming.
  --no-base-style                do not install the base shadcn style.
  -h, --help                     display help for command
```

Example with components:

```bash
npx shadcn-vue@latest init Sidebar01 Login01
```

---

## add

Add components and dependencies to your project.

```bash
npx shadcn-vue@latest add [component]
```

**All Options:**

```
Usage: shadcn-vue add [options] [components...]

add a component to your project

Arguments:
  components           names, url or local path to component

Options:
  -y, --yes            skip confirmation prompt. (default: false)
  -o, --overwrite      overwrite existing files. (default: false)
  -c, --cwd <cwd>      the working directory. defaults to the current directory.
  -a, --all            add all available components (default: false)
  -p, --path <path>    the path to add the component to.
  -s, --silent         mute output. (default: false)
  -h, --help           display help for command
```

Add via URL:

```bash
npx shadcn-vue add https://acme.com/registry/navbar.json
```

---

## apply

Apply a preset to an existing project.

```bash
npx shadcn-vue@latest apply --preset nova
```

**All Options:**

```
Usage: shadcn-vue apply [options] [preset]

apply a preset to an existing project

Arguments:
  preset             the preset to apply

Options:
  --preset <preset>  preset configuration to apply
  -y, --yes          skip confirmation prompt. (default: false)
  -c, --cwd <cwd>    the working directory. defaults to the current directory.
  -s, --silent       mute output. (default: false)
  -h, --help         display help for command
```

---

## view

View items from the registry before installing them.

```bash
npx shadcn-vue@latest view [item]
```

Multiple items:

```bash
npx shadcn-vue@latest view button card dialog
```

Namespaced registries:

```bash
npx shadcn-vue@latest view @acme/auth @v0/dashboard
```

**All Options:**

```
Usage: shadcn-vue view [options] <items...>

view items from the registry

Arguments:
  items            the item names or URLs to view

Options:
  -c, --cwd <cwd>  the working directory. defaults to the current directory.
  -h, --help       display help for command
```

---

## search / list

Search for items from registries. `list` is an alias for `search`.

```bash
npx shadcn-vue@latest search [registry]
```

With query:

```bash
npx shadcn-vue@latest search @shadcn-vue -q "button"
```

Multiple registries:

```bash
npx shadcn-vue@latest search @shadcn-vue @v0 @acme
```

List alias:

```bash
npx shadcn-vue@latest list @acme
```

**All Options:**

```
Usage: shadcn-vue search|list [options] <registries...>

search items from registries

Arguments:
  registries             the registry names or urls to search items from.
                         Names must be prefixed with @.

Options:
  -c, --cwd <cwd>        the working directory. defaults to the current directory.
  -q, --query <query>    query string
  -l, --limit <number>   maximum number of items to display per registry (default: "100")
  -o, --offset <number>  number of items to skip (default: "0")
  -h, --help             display help for command
```

---

## build

Generate registry JSON files from `registry.json`. Outputs to `public/r/` by default.

```bash
npx shadcn-vue@latest build
```

Custom output:

```bash
npx shadcn-vue@latest build --output ./public/registry
```

**All Options:**

```
Usage: shadcn-vue build [options] [registry]

build components for a shadcn-vue registry

Arguments:
  registry             path to registry.json file (default: "./registry.json")

Options:
  -o, --output <path>  destination directory for json files (default: "./public/r")
  -c, --cwd <cwd>      the working directory. defaults to the current directory.
  -h, --help           display help for command
```

---

## docs

Fetch documentation and API references for components.

```bash
npx shadcn-vue@latest docs [component]
```

**All Options:**

```
Usage: shadcn-vue docs [options] <components...>

get docs, api references and usage examples for components

Arguments:
  components         component names

Options:
  -c, --cwd <cwd>    the working directory. defaults to the current directory.
  -b, --base <base>  the base to use (reka). defaults to project base.
  --json             output as JSON. (default: false)
  -h, --help         display help for command
```

---

## info

Get information about your project.

```bash
npx shadcn-vue@latest info
```

**All Options:**

```
Usage: shadcn-vue info [options]

get information about your project

Options:
  -c, --cwd <cwd>  the working directory. defaults to the current directory.
  --json            output as JSON. (default: false)
  -h, --help        display help for command
```

---

## migrate

Run migrations on your project.

```bash
npx shadcn-vue@latest migrate [migration]
```

**Available Migrations:**

| Migration | Description |
|---|---|
| `icons` | Migrate UI components to a different icon library |
| `rtl` | Migrate components to support RTL (right-to-left) |

**All Options:**

```
Usage: shadcn-vue migrate [options] [migration] [path]

run a migration.

Arguments:
  migration        the migration to run.
  path             optional path or glob pattern to migrate.

Options:
  -c, --cwd <cwd>  the working directory. defaults to the current directory.
  -l, --list       list all migrations. (default: false)
  -y, --yes        skip confirmation prompt. (default: false)
  -h, --help       display help for command
```

### migrate rtl

Transforms components to support RTL (right-to-left) languages.

```bash
npx shadcn-vue@latest migrate rtl
```

What it does:

1. Updates `components.json` to set `rtl: true`
2. Transforms physical CSS properties to logical equivalents
   (e.g. `ml-4` to `ms-4`, `text-left` to `text-start`)
3. Adds `rtl:` variants where needed
   (e.g. `space-x-4` to `space-x-4 rtl:space-x-reverse`)

Specific files:

```bash
# Single file
npx shadcn-vue@latest migrate rtl src/components/ui/button/Button.vue

# Glob pattern
npx shadcn-vue@latest migrate rtl "src/components/ui/**"
```

If no path is provided, transforms all files in the `ui` directory from `components.json`.

Source: `/tmp/shadcn-vue-repo/apps/v4/content/docs/06.cli.md`
