---
name: sw-document-type
description: Scaffold eines eigenen Shopware-6 Dokumenttyps (Renderer + Twig-Template + document_type-Migration) inkl. Registrierung.
argument-hint: <typeName> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-document-type

Erzeuge einen Dokumenttyp. Skill: `sw-document-type` (+ `sw-document`).

## Ablauf
1. Typ-Name (snake_case, z.B. `ff_packing_list`) + Ziel-Plugin.
2. `src/Core/Checkout/Document/Renderer/<Name>Renderer.php` extends `AbstractDocumentRenderer` (`supports`, `render`),
   Registrierung via `document.renderer`-Tag.
3. Twig-Template `Resources/views/documents/<type>.html.twig`.
4. Migration: `document_type` + `document_base_config` anlegen.
5. Hinweis: Erzeugung über `DocumentGenerator`; Belegnummern via NumberRange.

Bestehende Dokumenttypen nicht überschreiben.
