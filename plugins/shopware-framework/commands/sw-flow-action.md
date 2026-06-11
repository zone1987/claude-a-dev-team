---
name: sw-flow-action
description: Scaffold einer Shopware-6 Flow-Builder-Action (PHP + Admin-Komponente) inkl. requirements und Registrierung.
argument-hint: <action.name> [--plugin <PluginName>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-flow-action

Erzeuge eine Flow-Action. Skills: `sw-flow-action`, `sw-flow-trigger`, `sw-flow-transaction`.

## Ablauf
1. Action-Name (`action.<owner>.<verb>`, z.B. `action.ff.notify`) + Ziel-Plugin + benötigte Aware-Daten (z.B. OrderAware).
2. PHP `src/Core/Content/Flow/Dispatching/Action/<Name>Action.php` (`getName`, `requirements`, `handleFlow(StorableFlow)`),
   Registrierung via `flow.action`-Tag.
3. Admin-Komponente (`sw-flow-action-...`) für Konfiguration + Registrierung beim Flow-Action-Service.
4. Hinweis: transaktional nach Business-Prozess; externe Calls fehlertolerant/idempotent.

Eigener Trigger nötig? → `sw-flow-trigger`. Bestehende Actions nicht überschreiben.
