---
name: playwright-ci
description: Scaffolds a CI pipeline for Playwright — GitHub Actions, GitLab CI, Jenkins or Azure with browser installation (--with-deps), caching, optional sharding across machines, HTML and blob reports, and artefact upload (trace, screenshot, video).
argument-hint: [--provider github|gitlab|jenkins|azure] [--docker] [--shards N]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /playwright-ci

Produce a ready-to-use CI configuration for Playwright. Skills: `playwright-tooling`,
`playwright-runner`.

## Steps
1. Provider and options from `$ARGUMENTS` (default GitHub Actions).
2. **Workflow** — documented steps only (`playwright-tooling`):
   - Node setup plus `npm ci`
   - `npx playwright install --with-deps`, or the official Docker image
     `mcr.microsoft.com/playwright:vX.Y.Z-noble`
   - `npx playwright test`
   - report and artefact upload (HTML report; with sharding, `blob` plus `merge-reports`)
3. **`--shards N`:** a matrix with `--shard=i/N` and the blob reporter, then a merge job.
4. **`--docker`:** the official image instead of installing browsers by hand.
5. Caching and worker notes (CI typically `workers: 1` and `retries: 2`, via config or flags).

Use documented flags and images only (source: `playwright-tooling`, `playwright-runner`). No secrets
in the YAML — reference them as CI secrets or variables.
