---
name: sw-api-map
description: Gewinnt die vollständige API-Endpunktliste eines Shopware-Projekts aus der OpenAPI-Spec (Admin + Store, inkl. Plugin-Routen) und schreibt .shopware-catalog/admin-api.md und .shopware-catalog/store-api.md (Pfad, Methode, Tag, Parameter, Auth).
argument-hint: [--store-only|--admin-only]
allowed-tools: Read, Glob, Grep, Bash, Write, Task
model: haiku
---

# /sw-api-map

Erzeuge/aktualisiere die API-Kataloge. Delegiere an den Agent `shopware-api-mapper` (Skill `sw-api-catalog`).

## Ablauf
1. OpenAPI-Spec beschaffen (in Reihenfolge): lokale Spec-Datei im Projekt → laufender Shop
   (`/store-api/_info/openapi3.json` mit `sw-access-key`; `/api/_info/openapi3.json` mit Bearer-Token, APP_ENV=dev)
   → lokale Referenz-Repos (`storeapi.json`/`adminapi.json`).
2. Spec parsen (python3/jq, nicht „ganz lesen"): `info.version`, `servers`, `securitySchemes`, je `paths.<p>.<m>`
   Tag/Summary/Parameter/Body/Responses.
3. Schreiben: `.shopware-catalog/store-api.md` und/oder `.shopware-catalog/admin-api.md`, gruppiert nach Tag,
   mit Auth-Hinweis je Endpoint. `--store-only`/`--admin-only` begrenzt.
4. Kopf mit Quelle/API-Version/Server/Anzahl; Kurzzusammenfassung ausgeben.

Keine Spec erreichbar → vermerken und auf statische Liste (`sw-store-api-endpoints`) verweisen. Nichts erfinden.
