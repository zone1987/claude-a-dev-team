---
name: contao-module
description: Scaffold eines Contao-Frontend-Moduls als Fragment-Controller (#[AsFrontendModule]) inkl. Twig-Template, DCA-Palette und Übersetzungen.
argument-hint: <name> [--bundle <Bundle>] [--category <category>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /contao-module

Erzeuge ein Front-End-Modul (Fragment-Controller). Skills: `contao-frontend-modules`, `contao-fragment-controllers`, `contao-templates`.

## Ablauf
1. Name (z.B. `my_module`) + Ziel-Bundle + Kategorie.
2. Controller `src/Controller/FrontendModule/<Name>Controller.php` mit `#[AsFrontendModule(category: '...')]`.
3. Twig-Template `contao/templates/frontend_module/<name>.html.twig`.
4. DCA/Palette (`tl_module`) + Übersetzungen.
5. Hinweis: Cache leeren.

Content-Element stattdessen → `/contao-content-element`. Backend-Modul → DCA + `contao-backend-modules`.
