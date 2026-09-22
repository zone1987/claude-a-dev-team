---
name: sw-document-type
description: Scaffolds a Shopware 6 document type with its renderer, template and migration.
argument-hint: <Name> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-document-type

Creates a document type. Skill: `sw-document`.

## Steps

1. Type name in snake_case, prefixed with the plugin's own prefix (e.g.
   `{table-prefix}packing_list`), plus the target plugin.
2. `src/Core/Checkout/Document/Renderer/<Name>Renderer.php` extending
   `AbstractDocumentRenderer` (`supports`, `render`), registered in
   `src/Resources/config/services/documents.php` — **PHP, not XML** — with the
   `document.renderer` tag set by hand:

   ```php
   $services->set(MyRenderer::class)
       ->args([service('document_type.repository')])
       ->tag('document.renderer');
   ```

3. Twig template under `Resources/views/documents/<type>.html.twig`.
4. Migration creating the `document_type` and `document_base_config` rows.
5. Generation runs through `DocumentGenerator`; document numbers come from a
   `NumberRange`, never from a counter of your own.

**Never overwrite an existing document type.** An invoice a shop has already issued must
keep rendering the way it did.

## Before it counts as done

`composer gate` green, and the rendered document checked in the browser — a template is
proved end-to-end, never by an integration test.
→ `shopware-testing` → `sw-testing-standard`
