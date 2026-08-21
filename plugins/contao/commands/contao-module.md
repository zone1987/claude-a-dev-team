---
name: contao-module
description: Scaffolds a Contao front-end module as a fragment controller with #[AsFrontendModule], a Twig template, a DCA palette and translations.
argument-hint: <name> [--bundle <Bundle>] [--category <category>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /contao-module

Create the front-end module named in $ARGUMENTS, using the fragment-controller pattern.

Call the Skill tool with "contao-frontend" first: it carries the service-tag options and where a
module differs from a content element.

## Steps (one question at a time, skip what the arguments settle)

1. **The name** (`my_module`), the target bundle, and the backend category.
2. **The controller** at `src/Controller/FrontendModule/<Name>Controller.php`, carrying
   `#[AsFrontendModule(category: '...')]`.
3. **The template** at `contao/templates/frontend_module/<name>.html.twig`.
4. **The DCA palette** in `tl_module`, plus translations.
5. **Clear the cache**, after which the module is selectable in the module configuration.

## Output

Every file written, and the cache command still to run.

For a content element use `/contao-content-element` instead. Never overwrite an existing file.
Invent nothing.
