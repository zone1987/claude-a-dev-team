# Shopware 6 — architecture concept

Complete concept documentation: `OVERVIEW-DETAIL.md`

## Brief overview

Shopware follows a modular, API-first architecture built on Symfony with three primary domains:

- **Core** — backend foundation: business logic, DAL, APIs, extension mechanism
- **Storefront** — PHP frontend: Twig templates, pages/pagelets, themes, JS plugins
- **Administration** — Vue.js SPA: communicates exclusively via the Admin API

All three share a common API layer. Storefront and admin have no business logic of their own.

## Core principles

- API-first: all functionality reachable via APIs (headless possible)
- Separation of concerns: presentation separated from business logic
- Extensibility via events, services and extension points
- Asynchronous processing via Symfony Messenger

Technical implementation: `shopware-core`, `shopware-storefront`, `shopware-admin` (dev plugins)
