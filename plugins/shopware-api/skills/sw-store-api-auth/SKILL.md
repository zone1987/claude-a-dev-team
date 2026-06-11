---
name: sw-store-api-auth
description: >
  Authentifizierung/Kontext der Shopware-6 Store API: sw-access-key (Sales-Channel-Access-Key) als Pflicht-Header,
  sw-context-token (Kontext-/Warenkorb-/Login-Token) Lebenszyklus, Kunden-Login. Trigger: "Store API auth", "sw-access-key",
  "sw-context-token", "Store API token", "contextToken", "sales channel access key", "store api login". Shopware 6.7.
---

# Shopware 6 — Store-API-Auth & Kontext

Die Store API ist kundenseitig und nutzt **keine OAuth-Tokens**, sondern Header.

- **`sw-access-key`** (Pflicht): Access-Key des Sales Channels (Admin → Verkaufskanal → API-Zugang). Identifiziert den Channel.
- **`sw-context-token`** (zustandsbehaftet): identifiziert den aktuellen Kontext (Warenkorb, eingeloggter Kunde,
  gewählte Währung/Sprache). Wird vom Server zurückgegeben (Header/Body) und bei Folge-Requests **mitgeschickt**.

```bash
# erster Request: Access-Key reicht; Server liefert ggf. einen sw-context-token zurück
curl "$BASE/store-api/context" -H "sw-access-key: $KEY"

# Login: Token wird im Response-Header zurückgegeben und danach wiederverwendet
curl -X POST "$BASE/store-api/account/login" -H "sw-access-key: $KEY" -H "Content-Type: application/json" \
     -d '{ "username": "kunde@example.com", "password": "..." }'   # -> sw-context-token
```

Den `sw-context-token` über die ganze Session/Warenkorb-Strecke konstant halten. Sprache/Währung über Kontext
bzw. Header (`sw-api-headers`). Endpunkte: `sw-store-api-endpoints`.
