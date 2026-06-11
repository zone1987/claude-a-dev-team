---
name: sw-event-map
description: Scannt das aktuelle Shopware-Projekt (Core + custom) und erzeugt/aktualisiert den Event-Katalog .shopware-catalog/events.md (Event-Name/Konstante, Event-Klasse, Dispatch-Ort, Argumente/Payload) als Grundlage für Subscriber.
argument-hint: [--custom-only]
allowed-tools: Read, Glob, Grep, Bash, Write, Task
model: haiku
---

# /sw-event-map

Erzeuge/aktualisiere den Event-Katalog. Delegiere an den Agent `shopware-event-mapper` (Skill `sw-event-catalog`).

## Ablauf
1. Scan-Bereich: `vendor/shopware/**` (Core) + `custom/plugins/*`, `custom/static-plugins/*`. Bei `--custom-only` nur custom.
2. Erfasse: Event-Klassen (`*Event.php`) mit Gettern/Constructor-Args, Konstanten-Klassen (`*Events.php`),
   Dispatch-Stellen (`->dispatch(`), Entity-Events je Definition, Flow-Events (`FlowEventAware`).
3. Schreibe `.shopware-catalog/events.md`, gruppiert (Business/Entity/Storefront-Page/Flow), je Event Name, Klasse,
   Dispatch-Ort und **Payload/Argumente**.
4. Kopf mit Scan-Datum/Bereich/Anzahl; Kurzzusammenfassung ausgeben.

Effizient via grep (`class .*Event`, `_EVENT =`, `->dispatch(`, `implements .*ShopwareEvent|FlowEventAware`).
Nur real vorhandene Events — nichts erfinden.
