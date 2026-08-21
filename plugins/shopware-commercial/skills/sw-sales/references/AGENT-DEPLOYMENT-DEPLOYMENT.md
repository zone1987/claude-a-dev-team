# Sales Agent — Deployment (complete)

Sales Agent is a Nuxt 3 application with MySQL and Redis. Deployment options are
analogous to DSR, but with a **mandatory Redis cache**.

---

## Contents

- [Option 1: AWS Amplify](#option-1-aws-amplify)
- [Option 2: Cloudflare Pages](#option-2-cloudflare-pages)
- [Option 3: Ubuntu Server with PM2](#option-3-ubuntu-server-with-pm2)

## Option 1: AWS Amplify

### Prerequisites

- AWS account
- Frontend source code in a Git repository

### Setting Up Redis with Amazon ElastiCache

AWS Amplify does not include Redis. Options:

**Option A: Amazon ElastiCache**

1. [ElastiCache Console](https://console.aws.amazon.com/elasticache/) → "Create"
2. Engine: Redis OSS
3. Configure the cluster (node type, replicas)
4. Security groups: allow access from Amplify
5. Note the primary endpoint

> **Note:** ElastiCache runs inside a VPC. Connecting from Amplify requires
> VPC peering or a public endpoint.

**Option B: Serverless Redis (recommended for Amplify)**

- [Upstash](https://upstash.com/) — serverless Redis with REST API
- [Redis Cloud](https://redis.com/cloud/overview/) — managed Redis

### Redis Environment Variables

```bash
REDIS_CACHE=true
REDIS_HOST=your-redis-endpoint.cache.amazonaws.com
REDIS_PORT=6379
REDIS_PASSWORD=your_redis_password
REDIS_TLS=true   # Recommended for production
```

### Deployment Steps

1. AWS Amplify Hosting Console → create a new app
2. Authorize the Git repository and main branch
3. Build settings are detected automatically
4. Under **Advanced Settings → Environment variables**, set all variables from
   `.env.template` (including the Redis variables)
5. **Save and Deploy**

### Custom Domain

[AWS guide](https://docs.aws.amazon.com/amplify/latest/userguide/custom-domains.html)

---

## Option 2: Cloudflare Pages

### Redis with Upstash

Cloudflare Pages/Workers does not include Redis.
[Upstash](https://upstash.com/) is the recommended solution.

**Setting up Upstash:**

1. [Upstash Console](https://console.upstash.com/) → "Create Database"
2. Choose a region (close to your users)
3. Copy the connection details:
   - `REDIS_HOST`, `REDIS_PORT`, `REDIS_PASSWORD`

**Alternative: Cloudflare integration**

1. Cloudflare Dashboard → Workers & Pages → project
2. Settings → Integrations → add the Upstash integration

### Environment Variables `.env`

```bash
REDIS_CACHE=true
REDIS_HOST=your-database.upstash.io
REDIS_PORT=6379
REDIS_PASSWORD=your_upstash_password
REDIS_TLS=true
```

### Deployment from Your Local Machine

`.npmrc` fix:

```bash
shamefully-hoist=true
strict-peer-dependencies=false
```

```bash
pnpm install wrangler --save-dev

# Prepare the .env file (setup skill)

# Build for Cloudflare Pages:
npx nuxi build --preset=cloudflare_pages

# Deploy (first time: create the project):
wrangler pages deploy dist/
```

### Automation with GitHub Actions

#### Secrets & Variables

- **Secret:** `CLOUDFLARE_API_TOKEN` (permission: "Cloudflare Pages — Edit")
- **Environment** `production` with all variables from `.env.template`

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

## Option 3: Ubuntu Server with PM2

### Setting Up Redis

**Option A: Install locally**

```bash
sudo apt update
sudo apt install redis-server
sudo nano /etc/redis/redis.conf
```

Important settings:
- `supervised systemd` — systemd integration
- `bind 127.0.0.1` — local access only
- `requirepass your_secure_password` — set a password

```bash
sudo systemctl enable redis-server
sudo systemctl start redis-server

# Test:
redis-cli -a your_secure_password ping   # → PONG
```

**Option B: Managed Redis (Upstash, Redis Cloud)**

Enter the provider's connection details in `.env`.

### Redis Environment Variables (local)

```bash
REDIS_CACHE=true
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
REDIS_PASSWORD=your_secure_password
REDIS_TLS=false   # true for managed services
```

### Building the Code

As per `sw-sales-agent-setup`: configure `.env`, `pnpm install`, `pnpm build`.

### PM2 Configuration

`ecosystem.config.cjs` in the project root:

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
