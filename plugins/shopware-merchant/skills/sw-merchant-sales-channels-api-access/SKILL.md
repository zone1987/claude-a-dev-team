name: sw-merchant-sales-channels-api-access
description: >
  Shopware API Zugang Verkaufskanal, Sales Channel Access Key generieren, Store API Key,
  Shopware API Zugangs-ID, API Schlüssel Kanal, Sales Channel API Token, Headless API Key,
  Shopware Store API Authentifizierung, Access Token generieren Verkaufskanal
---

# Shopware 6 – API-Zugang (Access Key)

Pro Verkaufskanal wird ein API-Zugangsschlüssel (Access Key) generiert.

## Wo

**Verkaufskanal > Abschnitt "API-Zugang"**

## Funktion

- Eindeutiger API-Schlüssel für die Sales Channel (Store) API
- Erlaubt Zugriff von Fremdsystemen (Apps, PWA, Mobile) auf Shop-Daten
- Jeder Kanal hat einen eigenen Schlüssel → Anfragen sind kanalspezifisch

## Wichtig

- Schlüssel nur einmal sichtbar → sofort sichern
- Bei Kompromittierung: neuen Schlüssel generieren (alter wird ungültig)
- Headless-Kanal: API-Zugang wird von Erweiterungen intern genutzt

## Quelle

https://docs.shopware.com/de/shopware-6-de/einstellungen/Verkaufskanaele
