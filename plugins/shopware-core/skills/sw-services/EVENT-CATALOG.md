# Shopware 6 — Event Catalogue (Project Introspection)

Answers: **"which events exist in THIS project and what do they carry?"** — from a cached catalogue.
The basis for every subscriber (`sw-events-subscriber`).

## Usage
1. The catalogue lives at `.shopware-catalog/events.md` in the project root.
2. **Missing/outdated** → regenerate it with `/sw-event-map` (agent `shopware-event-mapper`, haiku).
3. Look up: event name/constant → event class, dispatch location, **arguments/payload** (getters) → then build the
   matching subscriber.

## Event kinds in the catalogue
- **Business events** (classes, often `implements ShopwareEvent`/`FlowEventAware`), including `*Events` constant classes.
- **Entity events** (`{entity}.written/.deleted/.loaded` etc.) per entity.
- **Page/pagelet loaded events** (storefront), **kernel/Symfony events**, **flow events**.

## When to regenerate
- After `git pull` / plugin install or update, and after adding your own events.

To **create** a subscriber/event: `sw-events-subscriber`, `sw-extension-points`. The catalogue is the
source of truth about existing events.
