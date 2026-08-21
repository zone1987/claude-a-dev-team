---
name: contao-content-element
description: Scaffolds a Contao content element as a fragment controller with #[AsContentElement], a Twig template, a DCA palette and translations.
argument-hint: <name> [--bundle <Bundle>] [--category <category>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /contao-content-element

Create the content element named in $ARGUMENTS, using the fragment-controller pattern.

Call the Skill tool with "contao-frontend" first: it carries the service-tag options, both
registration methods and the Twig naming rules.

## Steps (one question at a time, skip what the arguments settle)

1. **The name** (`my_element`), the target bundle, and the backend category.
2. **The controller** at `src/Controller/ContentElement/<Name>Controller.php`, carrying
   `#[AsContentElement(category: '...')]` and a `__invoke` or `getResponse` that fills the template
   data.
3. **The template** at `contao/templates/content_element/<name>.html.twig`, or the `@Contao`
   namespace form for a modern element.
4. **The DCA palette** for the element, plus translations in
   `contao/languages/<lang>/default.xlf` or their PHP equivalent.
5. **Clear the cache**, after which the element appears in the backend under its category.

## Output

Every file written, and the cache command still to run.

For a front-end module use `/contao-module` instead. Never overwrite an existing file. Invent nothing.
