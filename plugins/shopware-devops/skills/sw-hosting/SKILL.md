---
name: sw-hosting
description: Shopware self-hosted operations: requirements, webserver, database, search, HTTP caching, S3, env config, worker and cron, observability, updates. Use when hosting or deploying Shopware 6.
---

# Shopware self-hosting

Running Shopware on your own infrastructure. Ordered as you would set a server up: requirements first, deployment last.

## Reference map

- **[CACHING-HTTP.md](references/CACHING-HTTP.md)**: Refer to `CACHING-HTTP-DETAIL.md` for full YAML examples.
- **[DATABASE.md](references/DATABASE.md)**: Refer to `DATABASE-DETAIL.md` for full MySQL and Redis configuration details.
- **[DEPLOYMENT.md](references/DEPLOYMENT.md)**: Refer to `DEPLOYMENT-DETAIL.md` for full deploy.php, GitLab CI, and GitHub Actions examples.
- **[ENV-CONFIG.md](references/ENV-CONFIG.md)**: Refer to `ENV-CONFIG-DETAIL.md` for the complete environment variables table.
- **[FILESYSTEM-S3.md](references/FILESYSTEM-S3.md)**: Refer to `FILESYSTEM-S3-DETAIL.md` for full adapter configs.
- **[INSTALLATION.md](references/INSTALLATION.md)**: Refer to `INSTALLATION-DETAIL.md` for full Docker Compose examples, Dockerfile, and extension management deta….
- **[OBSERVABILITY.md](references/OBSERVABILITY.md)**: Refer to `OBSERVABILITY-DETAIL.md` for full configuration examples and Grafana stack setup.
- **[PERFORMANCE.md](references/PERFORMANCE.md)**: Refer to `PERFORMANCE-DETAIL.md` for the full list of all tweaks.
- **[REQUIREMENTS.md](references/REQUIREMENTS.md)**: Refer to the deep reference for the full recommended stack table and version details.
- **[SEARCH.md](references/SEARCH.md)**: Refer to `SEARCH-DETAIL.md` for cluster architecture details, shard config, and debugging.
- **[UPDATES.md](references/UPDATES.md)**: Refer to `UPDATES-DETAIL.md` for full CLI sequences and staging configuration.
- **[WEBSERVER.md](references/WEBSERVER.md)**: Refer to `WEBSERVER-DETAIL.md` for full VCL examples and Fastly configs.
- **[WORKER-CRON.md](references/WORKER-CRON.md)**: Refer to `WORKER-CRON-DETAIL.md` for full systemd unit files and supervisord config.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (hosting, deployment, PaaS, shopware-cli) and the shopware-cli reference, retrieved 2026-08-20.
