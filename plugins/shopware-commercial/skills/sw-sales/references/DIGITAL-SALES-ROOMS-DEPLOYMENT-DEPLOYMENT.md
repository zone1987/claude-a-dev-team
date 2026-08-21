# Digital Sales Rooms — deployment (complete)

The DSR frontend app is a Nuxt 3 application and can be deployed anywhere
Node.js runs. Details on the Nuxt deployment options:
[Nuxt deployment documentation](https://nuxt.com/deploy).

---

## Contents

- [Option 1: AWS Amplify](#option-1-aws-amplify)
- [Option 2: Cloudflare Pages](#option-2-cloudflare-pages)
- [Option 3: Ubuntu server with PM2](#option-3-ubuntu-server-with-pm2)
- [SaaS (Shopware Beyond)](#saas-shopware-beyond)

## Option 1: AWS Amplify

### Prerequisites

- A registered AWS account
- Frontend source code in your own Git repository (e.g. GitHub)
  - Download the plugin ZIP → extract `/templates/dsr-frontends/` → push

### Deployment steps

1. Open the AWS Amplify hosting console
2. Create a new app
3. Authorize the Git repository and main branch (auto-deploy on push)
4. Choose an app name — the build settings are detected automatically
5. Under **Advanced Settings → Environment variables**, set the following variables:
   - `SHOPWARE_STORE_API`
   - `SHOPWARE_ADMIN_API`
   - `SHOPWARE_STORE_API_ACCESS_TOKEN`
   - `SHOPWARE_STOREFRONT_URL`
   - `ORIGIN`
6. Confirm the configuration → **Save and Deploy**

### Custom Domain

After deployment: assign a custom domain/subdomain.
[AWS guide](https://docs.aws.amazon.com/amplify/latest/userguide/custom-domains.html)

### Configuring the sales channel domain

Enter the app domain you received into the Shopware sales channel →
`sw-digital-sales-rooms-config`.

---

## Option 2: Cloudflare Pages

### Prerequisites

- A Cloudflare account
- Frontend source code in your own GitHub repository

### Deployment from a local machine

Known `.npmrc` fix for Nuxt/Cloudflare:

```bash
# .npmrc
shamefully-hoist=true
strict-peer-dependencies=false
```

```bash
pnpm install wrangler --save-dev

# generate the .env file (see the installation skill)

# build for Cloudflare Pages:
npx nuxi build --preset=cloudflare_pages

# on the first run: create the project
wrangler pages deploy dist/
```

### Automation with GitHub Actions

#### Setting up GitHub secrets & variables

- **Secret:** `CLOUDFLARE_API_TOKEN` — API token with the "Cloudflare Pages — Edit" permission
  ([create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/))
- Create an **environment** `production` with these variables:
  - `SHOPWARE_STORE_API`, `SHOPWARE_ADMIN_API`, `SHOPWARE_STORE_API_ACCESS_TOKEN`
  - `SHOPWARE_STOREFRONT_URL`, `ORIGIN`
- Optionally further environments: `development`, `staging`

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
          accountId: YOUR_ACCOUNT_ID       # from the dashboard URL
          projectName: YOUR_PROJECT_NAME
          directory: dist
          wranglerVersion: '3'
```

### Custom Domain

[Cloudflare guide](https://developers.cloudflare.com/pages/configuration/custom-domains/)

---

## Option 3: Ubuntu server with PM2

PM2 is a Node.js process manager that keeps the app running in the background
and restarts it automatically on crashes.

### Prerequisites

```bash
# Node.js + npm (Ubuntu)
sudo apt update && sudo apt install nodejs npm

# install PM2 globally
npm install -g pm2

# install pnpm globally
npm install -g pnpm
```

### Build

Clone the source code on the server, generate `.env` according to
`sw-digital-sales-rooms-installation`, and run `pnpm build`.

### Starting the app with PM2

Create `ecosystem.config.cjs` in the project root:

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

In SaaS operation the SwagDigitalSalesRooms plugin is already installed
(visible under the Marketing menu item). The following steps are still required:

1. **Deploy the frontend app** — one of the options above
2. **Third-party setup** → `sw-digital-sales-rooms-3rdparty`
3. **Plugin configuration** → `sw-digital-sales-rooms-config`
