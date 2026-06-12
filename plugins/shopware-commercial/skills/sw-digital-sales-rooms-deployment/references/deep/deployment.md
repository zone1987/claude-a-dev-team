# Digital Sales Rooms — Deployment (vollständig)

Die DSR-Frontend-App ist eine Nuxt-3-Anwendung und kann überall deployed werden,
wo Node.js läuft. Details zur Nuxt-Deployment-Optionen:
[Nuxt Deploy-Dokumentation](https://nuxt.com/deploy).

---

## Option 1: AWS Amplify

### Voraussetzungen

- AWS-Account registriert
- Frontend-Quellcode in eigenem Git-Repository (z.B. GitHub)
  - Plugin-ZIP herunterladen → `/templates/dsr-frontends/` extrahieren → pushen

### Deployment-Schritte

1. AWS Amplify Hosting Console öffnen
2. Neue App erstellen
3. Git-Repository und Main-Branch autorisieren (Auto-Deploy bei Push)
4. App-Name wählen — Build-Settings werden automatisch erkannt
5. Unter **Advanced Settings → Environment variables** folgende Variables setzen:
   - `SHOPWARE_STORE_API`
   - `SHOPWARE_ADMIN_API`
   - `SHOPWARE_STORE_API_ACCESS_TOKEN`
   - `SHOPWARE_STOREFRONT_URL`
   - `ORIGIN`
6. Konfiguration bestätigen → **Save and Deploy**

### Custom Domain

Nach dem Deployment: Custom Domain/Subdomain zuweisen.
[AWS-Anleitung](https://docs.aws.amazon.com/amplify/latest/userguide/custom-domains.html)

### Sales-Channel-Domain konfigurieren

Erhaltene App-Domain in den Shopware Sales Channel eintragen →
`sw-digital-sales-rooms-config`.

---

## Option 2: Cloudflare Pages

### Voraussetzungen

- Cloudflare-Account
- Frontend-Quellcode in eigenem GitHub-Repository

### Deployment vom lokalen Rechner

Bekannter `.npmrc`-Fix für Nuxt/Cloudflare:

```bash
# .npmrc
shamefully-hoist=true
strict-peer-dependencies=false
```

```bash
pnpm install wrangler --save-dev

# .env-Datei generieren (siehe Installation-Skill)

# Build für Cloudflare Pages:
npx nuxi build --preset=cloudflare_pages

# Beim ersten Mal: Projekt erstellen
wrangler pages deploy dist/
```

### Automatisierung mit GitHub Actions

#### GitHub Secrets & Variables einrichten

- **Secret:** `CLOUDFLARE_API_TOKEN` — API-Token mit "Cloudflare Pages — Edit"-Berechtigung
  ([Token erstellen](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/))
- **Environment** `production` anlegen mit diesen Variables:
  - `SHOPWARE_STORE_API`, `SHOPWARE_ADMIN_API`, `SHOPWARE_STORE_API_ACCESS_TOKEN`
  - `SHOPWARE_STOREFRONT_URL`, `ORIGIN`
- Optional weitere Environments: `development`, `staging`

#### Pipeline `.github/workflows/publish.yml`

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
        name: Install pnpm
        with:
          version: 8
          run_install: false

      - name: Install dependencies
        run: pnpm install

      - name: Build env file
        run: |
          touch .env
          echo SHOPWARE_STORE_API=${{ vars.SHOPWARE_STORE_API }} >> .env
          echo SHOPWARE_ADMIN_API=${{ vars.SHOPWARE_ADMIN_API }} >> .env
          echo SHOPWARE_STORE_API_ACCESS_TOKEN=${{ vars.SHOPWARE_STORE_API_ACCESS_TOKEN }} >> .env
          echo SHOPWARE_STOREFRONT_URL=${{ vars.SHOPWARE_STOREFRONT_URL }} >> .env
          echo ORIGIN=${{ vars.ORIGIN }} >> .env

      - name: Build code
        run: npx nuxi build --preset=cloudflare_pages

      - name: Publish to Cloudflare Pages
        uses: cloudflare/pages-action@v1.5.0
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: YOUR_ACCOUNT_ID       # aus Dashboard-URL
          projectName: YOUR_PROJECT_NAME
          directory: dist
          wranglerVersion: '3'
```

### Custom Domain

[Cloudflare-Anleitung](https://developers.cloudflare.com/pages/configuration/custom-domains/)

---

## Option 3: Ubuntu Server mit PM2

PM2 ist ein Node.js-Process-Manager, der die App im Hintergrund laufen lässt
und bei Abstürzen automatisch neu startet.

### Voraussetzungen

```bash
# Node.js + npm (Ubuntu)
sudo apt update && sudo apt install nodejs npm

# PM2 global installieren
npm install -g pm2

# pnpm global installieren
npm install -g pnpm
```

### Build

Quellcode auf dem Server klonen und gemäß `sw-digital-sales-rooms-installation`
`.env` generieren und `pnpm build` ausführen.

### App mit PM2 starten

`ecosystem.config.cjs` im Projekt-Root anlegen:

```js
module.exports = {
  apps: [
    {
      name: 'DSRNuxtApp',
      port: '3000',
      exec_mode: 'cluster',
      instances: 'max',
      script: './.output/server/index.mjs'
    }
  ]
}
```

```bash
pm2 start ecosystem.config.cjs
```

---

## SaaS (Shopware Beyond)

Im SaaS-Betrieb ist das SwagDigitalSalesRooms-Plugin bereits installiert
(sichtbar unter Marketing-Menüpunkt). Folgende Schritte sind dennoch nötig:

1. **Frontend-App deployen** — eine der Optionen oben
2. **3rd-Party-Setup** → `sw-digital-sales-rooms-3rdparty`
3. **Plugin-Konfiguration** → `sw-digital-sales-rooms-config`
