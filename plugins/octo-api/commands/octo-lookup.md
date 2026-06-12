---
name: octo-lookup
description: Schlägt eine OCTO-API-Capability oder einen Endpunkt nach (Ventrata oder Go-City) und gibt Request/Response/Parameter/Required/Auth aus.
argument-hint: <capability-oder-endpoint> [--api ventrata|gocity]
allowed-tools: Read, Glob, Grep
model: haiku
---

# /octo-lookup

Schlage eine OCTO-Capability oder einen Endpunkt nach. Delegiere an `octo-api-expert`.

## Ablauf
1. Aus `$ARGUMENTS` die Capability (z.B. `pricing`, `redemption`, `cart`) oder den Endpunkt (z.B. `POST /octo/bookings`) bestimmen.
2. Quelle wählen: `--api gocity` → `octo-gocity-*` (+ `gocity-openapi.json`); sonst Ventrata → passendes `octo-<name>`-Skill
   bzw. `octo-endpoints` für die Gesamtübersicht.
3. Ausgeben: Capability-Identifier, Endpunkt(e) (Methode/Pfad), Parameter (Pfad/Query/Body, **required** markiert),
   Response-Schema, nötige Header/Auth, ein curl-Beispiel.
4. Bei „Unterschied/Vergleich" → `octo-ventrata-vs-gocity`.

Nur belegte Inhalte aus den Skills/Spec — nichts erfinden. Keine echten Credentials ausgeben.
