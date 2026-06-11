---
name: sw-store-api-route
description: Scaffold einer Shopware-6 Store-API-Route (Abstract + Route + Response-Struct) mit _routeScope store-api und Registrierung.
argument-hint: <name> [--plugin <PluginName>] [--path /store-api/ff/example]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-store-api-route

Erzeuge eine Store-API-Route. Skill: `sw-store-api-route`.

## Ablauf
1. Name + Ziel-Plugin + Pfad (`/store-api/...`); Route-Name `store-api.<owner>.<name>`.
2. `Abstract<Name>Route` (abstrakte Basis, `getDecorated`), `<Name>Route` (extends Abstract, `#[Route]` mit
   `_routeScope: ['store-api']`, `load(Request, SalesChannelContext)`), `<Name>RouteResponse` (extends `StoreApiResponse`).
3. services.xml-Registrierung.
4. Hinweis: Auth via `sw-access-key`; für Frontends Typen neu generieren (`@shopware/api-gen`).

Für das Ändern einer bestehenden Core-Route stattdessen Decoration (`sw-store-api-override`). Admin-API-Aktion → `sw-admin-api-controller`.
