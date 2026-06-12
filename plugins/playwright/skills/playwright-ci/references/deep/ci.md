# Playwright in CI/CD

## Grundprinzipien

Drei Pflichtschritte fuer CI-Umgebungen:

1. **Browser-Ausfuehrung**: Entweder Docker-Image nutzen oder System-Abhaengigkeiten installieren
2. **Installation**: `npm ci` + `npx playwright install --with-deps`
3. **Ausfuehrung**: `npx playwright test`

### Worker-Empfehlung fuer CI

```typescript
// playwright.config.ts
export default defineConfig({
  workers: process.env.CI ? 1 : undefined,
  // CI: Sequenziell fuer Stabilitaet; Sharding fuer Parallelisierung
});
```

---

## GitHub Actions

### Standard-Workflow (`.github/workflows/playwright.yml`)

```yaml
name: Playwright Tests
on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]
jobs:
  test:
    timeout-minutes: 60
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v5
    - uses: actions/setup-node@v5
      with:
        node-version: lts/*
    - name: Install dependencies
      run: npm ci
    - name: Install Playwright Browsers
      run: npx playwright install --with-deps
    - name: Run Playwright tests
      run: npx playwright test
    - uses: actions/upload-artifact@v4
      if: ${{ !cancelled() }}
      with:
        name: playwright-report
        path: playwright-report/
        retention-days: 30
```

### Per Docker-Container

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    container:
      image: mcr.microsoft.com/playwright:v1.60.0-noble
    steps:
    - uses: actions/checkout@v5
    - name: Install dependencies
      run: npm ci
    - name: Run Playwright tests
      run: npx playwright test
      env:
        HOME: /root
```

Hinweis: Beim Container-Ansatz `--user 1001` ergaenzen fuer konsistente Cross-Platform-Umgebungen.

### Deployment-Trigger

```yaml
on:
  deployment_status:
jobs:
  test:
    if: github.event.deployment_status.state == 'success'
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v5
    - uses: actions/setup-node@v5
    - run: npm ci
    - run: npx playwright install --with-deps
    - run: npx playwright test
      env:
        PLAYWRIGHT_TEST_BASE_URL: ${{ github.event.deployment_status.target_url }}
```

### Fail-Fast / Only-Changed

```bash
# Nur geaenderte Tests ausfuehren (Dependency-Graph-Analyse)
npx playwright test --only-changed=origin/$GITHUB_BASE_REF
```

### Sharding in GitHub Actions

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        shardIndex: [1, 2, 3, 4]
        shardTotal: [4]
    steps:
    - uses: actions/checkout@v5
    - uses: actions/setup-node@v5
    - run: npm ci
    - run: npx playwright install --with-deps
    - run: npx playwright test --shard=${{ matrix.shardIndex }}/${{ matrix.shardTotal }}
    - uses: actions/upload-artifact@v4
      if: ${{ !cancelled() }}
      with:
        name: blob-report-${{ matrix.shardIndex }}
        path: blob-report/
        retention-days: 1

  merge-reports:
    needs: test
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v5
    - uses: actions/setup-node@v5
    - run: npm ci
    - uses: actions/download-artifact@v4
      with:
        path: all-blob-reports
        pattern: blob-report-*
        merge-multiple: true
    - run: npx playwright merge-reports --reporter html ./all-blob-reports
    - uses: actions/upload-artifact@v4
      with:
        name: playwright-report
        path: playwright-report/
        retention-days: 30
```

---

## Azure Pipelines

```yaml
trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:
- task: NodeTool@0
  inputs:
    versionSpec: '22'

- script: npm ci
  displayName: 'Install dependencies'

- script: npx playwright install --with-deps
  displayName: 'Install Playwright browsers'

- script: npx playwright test
  displayName: 'Run Playwright tests'

- task: PublishTestResults@2
  displayName: 'Publish test results'
  inputs:
    testResultsFormat: JUnit
    testResultsFiles: 'test-results/results.xml'
  condition: always()

- task: PublishPipelineArtifact@1
  inputs:
    targetPath: playwright-report
    artifact: playwright-report
    publishLocation: pipeline
  condition: always()
```

### Azure mit Sharding und Matrix

```yaml
strategy:
  matrix:
    chromium-1:
      project: chromium
      shard: 1/3
    chromium-2:
      project: chromium
      shard: 2/3
    chromium-3:
      project: chromium
      shard: 3/3
    firefox-1:
      project: firefox
      shard: 1/3

steps:
- script: npx playwright test --project=$(project) --shard=$(shard)
```

---

## CircleCI

```yaml
version: 2.1
orbs:
  node: circleci/node@5

jobs:
  playwright-tests:
    parallelism: 4
    docker:
      - image: mcr.microsoft.com/playwright:v1.60.0-noble
    resource_class: medium
    steps:
      - checkout
      - node/install-packages:
          pkg-manager: npm
      - run:
          name: Run Playwright tests
          command: |
            SHARD="$((${CIRCLE_NODE_INDEX}+1))"
            npx playwright test --shard=${SHARD}/${CIRCLE_NODE_TOTAL}

workflows:
  build:
    jobs:
      - playwright-tests
```

Hinweis: CircleCI verwendet 0-basierte Indizierung (`CIRCLE_NODE_INDEX`), daher `+1` fuer den `--shard`-Parameter.

---

## GitLab CI

### Sequenziell (parallel jobs)

```yaml
stages:
  - test

playwright-tests:
  stage: test
  image: mcr.microsoft.com/playwright:v1.60.0-noble
  parallel: 7
  script:
    - npm ci
    - npx playwright test --shard=$CI_NODE_INDEX/$CI_NODE_TOTAL
  artifacts:
    when: always
    paths:
      - blob-report/
    expire_in: 1 week
```

### Matrix-basiert

```yaml
playwright-tests:
  stage: test
  image: mcr.microsoft.com/playwright:v1.60.0-noble
  parallel:
    matrix:
      - PROJECT: [chromium, firefox, webkit]
        SHARD: ['1/3', '2/3', '3/3']
  script:
    - npm ci
    - npx playwright test --project=$PROJECT --shard=$SHARD
```

---

## Jenkins

```groovy
pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright:v1.60.0-noble' } }
   stages {
      stage('e2e-tests') {
         steps {
            sh 'npm ci'
            sh 'npx playwright test'
         }
      }
   }
   post {
      always {
         archiveArtifacts artifacts: 'playwright-report/**', allowEmptyArchive: true
      }
   }
}
```

---

## Bitbucket Pipelines

```yaml
image: mcr.microsoft.com/playwright:v1.60.0-noble

pipelines:
  default:
    - step:
        name: Run Playwright tests
        script:
          - npm ci
          - npx playwright test
        artifacts:
          - playwright-report/**
```

---

## Google Cloud Build

```yaml
steps:
- name: mcr.microsoft.com/playwright:v1.60.0-noble
  entrypoint: bash
  args:
    - -c
    - npm ci && npx playwright test
artifacts:
  objects:
    location: 'gs://your-bucket/playwright-reports/$BUILD_ID'
    paths: ['playwright-report/**']
```

---

## Docker-Images

### Verfuegbare Images (Microsoft Artifact Registry)

| Image | Ubuntu-Version |
|-------|---------------|
| `mcr.microsoft.com/playwright:v1.60.0-noble` | Ubuntu 24.04 LTS |
| `mcr.microsoft.com/playwright:v1.60.0-jammy` | Ubuntu 22.04 LTS |
| `mcr.microsoft.com/playwright:v1.60.0` | Standard (noble) |

### Empfohlene Docker-Flags

| Flag | Zweck |
|------|-------|
| `--ipc=host` | Verhindert Chromium-Speicherabsturz |
| `--init` | Verhindert Zombie-Prozesse (PID=1) |
| `--cap-add=SYS_ADMIN` | Lokal bei Launch-Fehlern |

### Docker-Kommandos

```bash
# Image pullen
docker pull mcr.microsoft.com/playwright:v1.60.0-noble

# E2E-Testing (vertrauenswuerdiger Code)
docker run -it --rm --ipc=host mcr.microsoft.com/playwright:v1.60.0-noble /bin/bash

# Web-Scraping (nicht-vertrauenswuerdige Seiten)
docker run -it --rm --ipc=host \
  --user pwuser \
  --security-opt seccomp=seccomp_profile.json \
  mcr.microsoft.com/playwright:v1.60.0-noble /bin/bash
```

### Remote-Server in Docker

```bash
docker run -p 3000:3000 --rm --init -it \
  --workdir /home/pwuser \
  --user pwuser \
  mcr.microsoft.com/playwright:v1.60.0-noble \
  /bin/sh -c "npx -y playwright@1.60.0 run-server --port 3000 --host 0.0.0.0"
```

Verbindung: `PW_TEST_CONNECT_WS_ENDPOINT=ws://127.0.0.1:3000/`

### Eigenes Dockerfile

```dockerfile
FROM node:20-bookworm
RUN npx -y playwright@1.60.0 install --with-deps
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
```

### Wichtige Hinweise

- Alpine Linux wird **nicht** unterstuetzt (benoetigt glibc; Alpine nutzt musl)
- Image-Versionen immer pinnen (passend zur Playwright-Version des Projekts)
- Images enthalten Browser + System-Abhaengigkeiten; Playwright-Package separat installieren

---

## Browser-Caching

Browser-Caching wird **nicht empfohlen**: Wiederherstellungszeit entspricht der Download-Zeit.

Falls dennoch gewuenscht:
```yaml
- uses: actions/cache@v4
  id: playwright-cache
  with:
    path: ~/.cache/ms-playwright
    key: playwright-${{ hashFiles('package-lock.json') }}
- run: npx playwright install --with-deps
  if: steps.playwright-cache.outputs.cache-hit != 'true'
- run: npx playwright install-deps
  if: steps.playwright-cache.outputs.cache-hit == 'true'
```

---

## HTML-Report in Azure Storage veroeffentlichen

```yaml
- script: |
    azcopy cp ./playwright-report \
      "https://$AZURE_ACCOUNT.blob.core.windows.net/\$web" \
      --recursive
  env:
    AZCOPY_SPA_APPLICATION_ID: $(AZCOPY_SPA_APPLICATION_ID)
    AZCOPY_SPA_CLIENT_SECRET: $(AZCOPY_SPA_CLIENT_SECRET)
    AZCOPY_TENANT_ID: $(AZCOPY_TENANT_ID)
```

Voraussetzungen:
- Azure Storage Account mit aktiviertem "Static website hosting"
- Service Principal mit "Storage Blob Data Contributor"-Rolle
- Drei GitHub Secrets: `AZCOPY_SPA_APPLICATION_ID`, `AZCOPY_SPA_CLIENT_SECRET`, `AZCOPY_TENANT_ID`

---

## Headed-Modus unter Linux (Xvfb)

```bash
# Xvfb manuell starten
xvfb-run npx playwright test

# Oder als Schritt in CI
- run: xvfb-run --auto-servernum --server-args="-screen 0 1280x960x24" npx playwright test
```

---

## Debugging in CI

```bash
# Browser-Start-Fehler debuggen
DEBUG=pw:browser npx playwright test

# Alle API-Aufrufe loggen
DEBUG=pw:api npx playwright test
```

---

## Sicherheitshinweise

Artefakte (Traces, Reports, Logs) koennen sensible Daten enthalten:
- Test-Credentials und Access-Tokens
- Quellcode-Fragmente
- Nur in vertrauenswuerdige Artifact-Stores hochladen oder vor dem Teilen verschluesseln

---

## Quellen

- https://playwright.dev/docs/ci
- https://playwright.dev/docs/ci-intro
- https://playwright.dev/docs/docker
