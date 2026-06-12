---
name: playwright-ci
description: Scaffold einer CI-Pipeline für Playwright — GitHub Actions / GitLab CI / Jenkins / Azure mit Browser-Installation (--with-deps), Caching, optionalem Sharding über mehrere Maschinen, HTML-/Blob-Report und Artefakt-Upload (Trace/Screenshot/Video).
argument-hint: [--provider github|gitlab|jenkins|azure] [--docker] [--shards N]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /playwright-ci

Erzeuge eine einsatzfertige CI-Konfiguration für Playwright. Skills: `playwright-ci`, `playwright-test-execution`.

## Ablauf
1. Provider/Optionen aus `$ARGUMENTS` (Default GitHub Actions).
2. **Workflow** erzeugen — nur dokumentierte Schritte (`playwright-ci`):
   - Node-Setup + `npm ci`
   - `npx playwright install --with-deps` (oder offizielles Docker-Image `mcr.microsoft.com/playwright:vX.Y.Z-noble`)
   - `npx playwright test`
   - Report-/Artefakt-Upload (HTML-Report, bei Sharding `blob` + `merge-reports`)
3. **`--shards N`:** Matrix mit `--shard=i/N` + Blob-Reporter, danach Merge-Job.
4. **`--docker`:** offizielles Image statt manueller Browser-Installation.
5. Caching-/Worker-Hinweise (CI-typisch `workers: 1`/`retries: 2` via Config oder Flags).

Nur dokumentierte Flags/Images (Quelle: `playwright-ci`/`playwright-test-execution`). Keine Secrets im YAML — als CI-Secrets/Variablen referenzieren.
