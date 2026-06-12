# Sales Agent — Deployment (vollständig)

Sales Agent ist eine Nuxt-3-Anwendung mit MySQL und Redis. Deployment-Optionen
analog zu DSR, aber mit **zwingend erforderlichem Redis-Cache**.

---

## Option 1: AWS Amplify

### Voraussetzungen

- AWS-Account
- Frontend-Quellcode in Git-Repository

### Redis mit Amazon ElastiCache einrichten

AWS Amplify enthält kein Redis. Optionen:

**Option A: Amazon ElastiCache**

1. [ElastiCache Console](https://console.aws.amazon.com/elasticache/) → "Create"
2. Engine: Redis OSS
3. Cluster konfigurieren (Node-Type, Replikas)
4. Security Groups: Zugriff von Amplify erlauben
5. Primary Endpoint notieren

> **Hinweis:** ElastiCache läuft in einem VPC. Verbindung von Amplify erfordert
> VPC Peering oder öffentlichen Endpoint.

**Option B: Serverless Redis (empfohlen für Amplify)**

- [Upstash](https://upstash.com/) — Serverless Redis mit REST API
- [Redis Cloud](https://redis.com/cloud/overview/) — Managed Redis

### Redis-Umgebungsvariablen

```bash
REDIS_CACHE=true
REDIS_HOST=your-redis-endpoint.cache.amazonaws.com
REDIS_PORT=6379
REDIS_PASSWORD=your_redis_password
REDIS_TLS=true   # Empfohlen für Produktion
```

### Deployment-Schritte

1. AWS Amplify Hosting Console → Neue App erstellen
2. Git-Repository und Main-Branch autorisieren
3. Build-Settings werden automatisch erkannt
4. Unter **Advanced Settings → Environment variables** alle Variables aus
   `.env.template` setzen (inkl. Redis-Variables)
5. **Save and Deploy**

### Custom Domain

[AWS-Anleitung](https://docs.aws.amazon.com/amplify/latest/userguide/custom-domains.html)

---

## Option 2: Cloudflare Pages

### Redis mit Upstash

Cloudflare Pages/Workers enthält kein Redis.
[Upstash](https://upstash.com/) ist die empfohlene Lösung.

**Upstash einrichten:**

1. [Upstash Console](https://console.upstash.com/) → "Create Database"
2. Region wählen (nah an Usern)
3. Connection Details kopieren:
   - `REDIS_HOST`, `REDIS_PORT`, `REDIS_PASSWORD`

**Alternative: Cloudflare-Integration**

1. Cloudflare Dashboard → Workers & Pages → Projekt
2. Settings → Integrations → Upstash-Integration hinzufügen

### Umgebungsvariablen `.env`

```bash
REDIS_CACHE=true
REDIS_HOST=your-database.upstash.io
REDIS_PORT=6379
REDIS_PASSWORD=your_upstash_password
REDIS_TLS=true
```

### Deployment vom lokalen Rechner

`.npmrc` fix:

```bash
shamefully-hoist=true
strict-peer-dependencies=false
```

```bash
pnpm install wrangler --save-dev

# .env-Datei vorbereiten (Setup-Skill)

# Build für Cloudflare Pages:
npx nuxi build --preset=cloudflare_pages

# Deployen (erstmalig: Projekt erstellen):
wrangler pages deploy dist/
```

### Automatisierung mit GitHub Actions

#### Secrets & Variables

- **Secret:** `CLOUDFLARE_API_TOKEN` (Berechtigung: "Cloudflare Pages — Edit")
- **Environment** `production` mit allen Variables aus `.env.template`

#### `.github/workflows/publish.yml`

```yml
on:
  push:
    branches:
      - main

jobs:
  publish:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      deployments: write
    name: Cloudflare Pages Deployment
    environment: production
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - uses: pnpm/action-setup@v4
        with:
          version: 8
          run_install: false

      - name: Install dependencies
        run: pnpm install

      - name: Build env file
        run: |
          touch .env
          echo COMPANY_NAME=${{ vars.COMPANY_NAME }} >> .env
          echo ORIGIN=${{ vars.ORIGIN }} >> .env
          echo REDIS_CACHE=${{ vars.REDIS_CACHE }} >> .env
          echo REDIS_HOST=${{ vars.REDIS_HOST }} >> .env
          echo REDIS_PORT=${{ vars.REDIS_PORT }} >> .env
          echo REDIS_PASSWORD=${{ vars.REDIS_PASSWORD }} >> .env
          echo REDIS_TLS=${{ vars.REDIS_TLS }} >> .env
          echo APP_NAME=${{ vars.APP_NAME }} >> .env
          echo APP_SECRET=${{ vars.APP_SECRET }} >> .env
          echo DATABASE_URL=${{ vars.DATABASE_URL }} >> .env

      - name: Build code
        run: npx nuxi build --preset=cloudflare_pages

      - name: Publish to Cloudflare Pages
        uses: cloudflare/pages-action@v1.5.0
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: YOUR_ACCOUNT_ID
          projectName: YOUR_PROJECT_NAME
          directory: dist
          wranglerVersion: "3"
```

---

## Option 3: Ubuntu Server mit PM2

### Redis einrichten

**Option A: Lokal installieren**

```bash
sudo apt update
sudo apt install redis-server
sudo nano /etc/redis/redis.conf
```

Wichtige Einstellungen:
- `supervised systemd` — systemd-Integration
- `bind 127.0.0.1` — nur lokaler Zugriff
- `requirepass your_secure_password` — Passwort setzen

```bash
sudo systemctl enable redis-server
sudo systemctl start redis-server

# Test:
redis-cli -a your_secure_password ping   # → PONG
```

**Option B: Managed Redis (Upstash, Redis Cloud)**

Connection-Details des Providers in `.env` eintragen.

### Redis-Umgebungsvariablen (lokal)

```bash
REDIS_CACHE=true
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
REDIS_PASSWORD=your_secure_password
REDIS_TLS=false   # true für managed services
```

### Code bauen

Gemäß `sw-sales-agent-setup`: `.env` konfigurieren, `pnpm install`, `pnpm build`.

### PM2-Konfiguration

`ecosystem.config.cjs` im Projekt-Root:

```js
module.exports = {
  apps: [
    {
      name: "SalesAgentApp",
      port: "3000",
      exec_mode: "cluster",
      instances: "max",
      script: "./.output/server/index.mjs",
    },
  ],
};
```

```bash
pm2 start ecosystem.config.cjs
```
