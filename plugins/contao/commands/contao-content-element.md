---
name: contao-content-element
description: Scaffold eines Contao-Content-Elements als Fragment-Controller (#[AsContentElement]) inkl. Twig-Template, DCA-Palette und Übersetzungen.
argument-hint: <name> [--bundle <Bundle>] [--category <category>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /contao-content-element

Erzeuge ein Content-Element (modernes Fragment-Controller-Muster). Skills: `contao-content-elements`,
`contao-fragment-controllers`, `contao-templates`.

## Ablauf
1. Name (z.B. `my_element`) + Ziel-Bundle + Kategorie.
2. Controller `src/Controller/ContentElement/<Name>Controller.php` mit `#[AsContentElement(category: '...')]`,
   `getResponse()`/`__invoke` (Template-Daten setzen).
3. Twig-Template `contao/templates/content_element/<name>.html.twig` (bzw. modernes `@Contao`-Namespace-Template).
4. DCA/Palette für das Element + Übersetzungen (`contao/languages/.../default.xlf` bzw. PHP).
5. Hinweis: Cache leeren; Element erscheint im Backend unter der Kategorie.

Front-End-Modul stattdessen → `/contao-module`. Bestehende Dateien nicht überschreiben.
