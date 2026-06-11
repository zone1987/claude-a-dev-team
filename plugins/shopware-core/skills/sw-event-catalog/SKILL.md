---
name: sw-event-catalog
description: >
  Den projektspezifischen Event-Katalog von Shopware nutzen — welche Events es im KONKRETEN Projekt gibt (Core +
  custom), ihre Event-Klasse, der Event-Name/Konstante, wo sie dispatcht werden und welche Argumente/Payload sie
  tragen (Getter/Constructor). Damit findet man das passende Event für einen Subscriber. Trigger: "welches Event",
  "welche Events gibt es", "Event-Katalog", "Event-Argumente", "auf welches Event hören", "event payload", "event map",
  "ProductEvents Konstante". Shopware 6.7. Erzeuger: /sw-event-map.
---

# Shopware 6 — Event-Katalog (Projekt-Introspektion)

Beantwortet: **„welche Events existieren in DIESEM Projekt und was tragen sie?"** — aus einem gecachten Katalog.
Grundlage für jeden Subscriber (`sw-events-subscriber`).

## Nutzung
1. Katalog liegt unter `.shopware-catalog/events.md` im Projekt-Root.
2. **Fehlt/veraltet** → mit `/sw-event-map` (Agent `shopware-event-mapper`, haiku) neu erzeugen.
3. Nachschlagen: Event-Name/Konstante → Event-Klasse, Dispatch-Ort, **Argumente/Payload** (Getter) → passenden
   Subscriber bauen.

## Event-Arten im Katalog
- **Business-Events** (Klassen, oft `implements ShopwareEvent`/`FlowEventAware`), inkl. `*Events`-Konstantenklassen.
- **Entity-Events** (`{entity}.written/.deleted/.loaded` etc.) je Entity.
- **Page-/Pagelet-LoadedEvents** (Storefront), **Kernel-/Symfony-Events**, **Flow-Events**.

## Wann neu erzeugen
- Nach `git pull` / Plugin-Install/-Update, nach Anlegen eigener Events.

Zum **Erstellen** eines Subscribers/Events: `sw-events-subscriber`, `sw-extension-points`. Der Katalog ist die
Quelle der Wahrheit über vorhandene Events.
