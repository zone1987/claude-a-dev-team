---
name: sw-event-map
description: Scans the current Shopware project (core + custom) and writes or updates the event catalogue .shopware-catalog/events.md (event name/constant, event class, dispatch site, arguments/payload) as the basis for subscribers.
argument-hint: [--custom-only]
allowed-tools: Read, Glob, Grep, Bash, Write, Task
model: haiku
---

# /sw-event-map

Create or update the event catalogue. Delegate to the `shopware-event-mapper` agent (skill `sw-services`).

## Steps
1. Scan area: `vendor/shopware/**` (core) plus `custom/plugins/*`, `custom/static-plugins/*`. With `--custom-only`, custom only.
2. Record: event classes (`*Event.php`) with their getters and constructor arguments, constant classes (`*Events.php`),
   dispatch sites (`->dispatch(`), the entity events per definition, and flow events (`FlowEventAware`).
3. Write `.shopware-catalog/events.md`, grouped (business / entity / storefront page / flow), and for each event its name, class,
   dispatch site and **payload or arguments**.
4. Add a header with the scan date, area and count; print a short summary.

Scan efficiently with grep (`class .*Event`, `_EVENT =`, `->dispatch(`, `implements .*ShopwareEvent|FlowEventAware`).
Only events that really exist — invent nothing.
