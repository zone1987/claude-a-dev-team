---
name: contao-hook
description: Scaffold eines Contao-Hook-Listeners (#[AsHook('hookName')]) mit korrekter Methoden-Signatur des gewählten Hooks.
argument-hint: <hookName> [--bundle <Bundle>] [--priority <int>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /contao-hook

Erzeuge einen Hook-Listener. Skills: `contao-hooks`, `contao-hooks-reference`.

## Ablauf
1. Hook-Name aus `$ARGUMENTS` (z.B. `parseTemplate`, `generatePage`, `getContentElement`). Die **exakte Signatur**
   (Parameter-Typen + Rückgabewert) aus `contao-hooks-reference` ermitteln.
2. Listener-Klasse `src/EventListener/<Name>Listener.php` mit `#[AsHook('<hookName>')]` (optional `priority:`) und der
   korrekten `__invoke(...)`-Signatur des Hooks.
3. Hinweis: Service wird per Attribut automatisch registriert (Autoconfigure); Cache leeren.

Nur dokumentierte Hooks verwenden; Signatur nicht erfinden — aus der Referenz übernehmen.
