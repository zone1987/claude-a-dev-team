# Digital Sales Rooms — 3rd-Party Setup

Vollständige Referenz: [DIGITAL-SALES-ROOMS-3RDPARTY-3RDPARTY.md](DIGITAL-SALES-ROOMS-3RDPARTY-3RDPARTY.md)

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
