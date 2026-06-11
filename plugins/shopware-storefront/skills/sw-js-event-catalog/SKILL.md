---
name: sw-js-event-catalog
description: >
  Den projektspezifischen Katalog der JavaScript-Storefront-Events von Shopware nutzen — welche JS-Events es im
  KONKRETEN Projekt gibt (Core + custom), WO sie published werden ($emitter.publish), WO subscribed wird
  (document.$emitter.subscribe), welche Argumente/`detail` sie tragen, plus native DOM-/PluginManager-Events.
  Trigger: "welche JS-Events gibt es", "Storefront JS Event Katalog", "wo wird Event published/subscribed",
  "$emitter publish subscribe", "JS event argumente", "js event map". Shopware 6.7. Erzeuger: /sw-js-plugin-map.
---

# Shopware 6 — JS-Storefront-Event-Katalog (Projekt-Introspektion)

Beantwortet: **„welche JS-Events existieren, wo werden sie gefeuert/abonniert, was tragen sie?"** — aus einem
gecachten Katalog. Grundlage für plugin-übergreifende JS-Kommunikation (`sw-js-events`).

## Nutzung
1. Katalog liegt unter `.shopware-catalog/js-events.md` im Projekt-Root.
2. **Fehlt/veraltet** → mit `/sw-js-plugin-map` (Agent `shopware-js-plugin-mapper`, haiku) neu erzeugen — der
   Mapper schreibt sowohl `js-plugins.md` als auch `js-events.md`.
3. Nachschlagen: Event-Name → Publish-Ort(e), Subscribe-Ort(e), Argumente (`event.detail`-Felder), Typ
   (Emitter / nativ / PluginManager-Lifecycle).

## Erfasste Event-Arten
- **$emitter-Events**: `this.$emitter.publish('name', detail)` ↔ `document.$emitter.subscribe('name', cb)`.
- **Native DOM-Events**: `dispatchEvent(new CustomEvent('name', { detail }))` / `addEventListener`.
- **PluginManager-Lifecycle**: Initialisierungs-/Update-Events.

## Wann neu erzeugen
- Nach `git pull` / Plugin-Install/-Update, nach Anlegen eigener JS-Events.

Zum **Auslösen/Abonnieren** im Code: `sw-js-events`. Der Katalog ist die Quelle der Wahrheit über vorhandene JS-Events.
