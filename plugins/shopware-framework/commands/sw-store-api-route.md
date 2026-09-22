---
name: sw-store-api-route
description: Scaffolds a Shopware 6 Store API route (abstract base, route and response struct) with _routeScope store-api and its registration.
argument-hint: <Name> [--plugin <PluginName>] [--path /store-api/example]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-store-api-route

Produce a Store API route. Skill: `sw-api`.

## Steps
1. Settle the name, target plugin and path (`/store-api/…`); the route name is
   `store-api.<owner>.<name>`.
2. Create `Abstract<Name>Route` (the abstract base, with `getDecorated`), `<Name>Route` (extends the
   abstract, `#[Route]` with `_routeScope: ['store-api']`, `load(Request, SalesChannelContext)`) and
   `<Name>RouteResponse` (extends `StoreApiResponse`).
3. Register them in `src/Resources/config/services/routes.php` — PHP, not XML (`XmlFileLoader` is
   `@deprecated tag:v6.8.0`), explicitly and without autowiring
   (→ `shopware-core` → `sw-services` → `DEPENDENCY-INJECTION.md`).
4. Note the follow-up: auth goes through `sw-access-key`, and a frontend needs its types regenerated
   (`@shopware/api-gen`).

To change an existing core route, decorate it instead (`sw-api`). For an Admin API action, see
`sw-api`.

## Before it counts as done

`composer gate` green, unit tests for the route's logic, and the route proved end-to-end:
called with a valid `sw-access-key`, returning the expected response.
→ `shopware-testing` → `sw-testing-standard`
