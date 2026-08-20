# Digital Sales Rooms — third-party setup

Full reference: [DIGITAL-SALES-ROOMS-3RDPARTY-3RDPARTY.md](DIGITAL-SALES-ROOMS-3RDPARTY-3RDPARTY.md)

## Daily.co (Video/Audio)

1. Dashboard: [dashboard.daily.co](https://dashboard.daily.co/)
2. "Developers" section → copy the API KEY
3. Enter it in the DSR plugin config: Video and Audio → API key

## Mercure (Realtime)

**Quick start via Stackhero (recommended):**

1. [stackhero.io](https://www.stackhero.io) → create a new stack with "Mercure Hub"
2. Copy hub url, public url, subscriber secret + publisher secret
3. CORS: enter the frontend domain and backend domain in "publish allowed origins"
4. Enter the values in the DSR plugin config → Realtime service

**Alternative: Docker**

```bash
git clone https://github.com/shopware/local-mercure-sample
docker-compose up
```
