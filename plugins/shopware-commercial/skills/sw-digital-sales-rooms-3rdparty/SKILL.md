---
name: sw-digital-sales-rooms-3rdparty
description: >
  Einrichtung der Drittanbieter-Dienste für Digital Sales Rooms:
  Mercure Hub (Stackhero oder Docker) und Daily.co (Video/Audio API).
  Triggers: "DSR Mercure", "DSR Daily.co", "mercure digital sales rooms",
  "daily.co setup DSR", "mercure hub einrichten", "stackhero mercure",
  "dsr realtime service", "dsr video api", "mercure CORS setup"
---

# Digital Sales Rooms — 3rd-Party Setup

Vollständige Referenz: [references/deep/3rdparty.md](references/deep/3rdparty.md)

## Daily.co (Video/Audio)

1. Dashboard: [dashboard.daily.co](https://dashboard.daily.co/)
2. Sektion "Developers" → API KEY kopieren
3. In DSR Plugin-Config eintragen: Video and Audio → API key

## Mercure (Realtime)

**Schnellstart via Stackhero (empfohlen):**

1. [stackhero.io](https://www.stackhero.io) → Neuen Stack mit "Mercure Hub" erstellen
2. Hub url, public url, subscriber secret + publisher secret kopieren
3. CORS: Frontend-Domain und Backend-Domain in "publish allowed origins" eintragen
4. Werte in DSR Plugin-Config → Realtime service eintragen

**Alternativ: Docker**

```bash
git clone https://github.com/shopware/local-mercure-sample
docker-compose up
```
