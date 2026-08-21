---
name: sw-hosting
description: Shopware self-hosted operations: requirements, installation, webserver, database, search, HTTP caching, S3, env config, worker and cron, performance, observability, updates, deployment.
---

# Shopware self-hosting

Running Shopware on your own infrastructure. Ordered as you would set a server up: requirements first, deployment last.

## Reference map

- **[CACHING-HTTP.md](references/CACHING-HTTP.md)**: Refer to `CACHING-HTTP-DETAIL.md` for full YAML examples. [CACHING-HTTP-DETAIL](references/CACHING-HTTP-DETAIL.md).
- **[DATABASE.md](references/DATABASE.md)**: Refer to `DATABASE-DETAIL.md` for full MySQL and Redis configuration details. [DATABASE-DETAIL](references/DATABASE-DETAIL.md).
- **[DEPLOYMENT.md](references/DEPLOYMENT.md)**: Refer to `DEPLOYMENT-DETAIL.md` for full deploy.php, GitLab CI, and GitHub Actions examples. [DEPLOYMENT-DETAIL](references/DEPLOYMENT-DETAIL.md).
- **[ENV-CONFIG.md](references/ENV-CONFIG.md)**: Refer to `ENV-CONFIG-DETAIL.md` for the complete environment variables table. [ENV-CONFIG-DETAIL](references/ENV-CONFIG-DETAIL.md).
- **[FILESYSTEM-S3.md](references/FILESYSTEM-S3.md)**: Refer to `FILESYSTEM-S3-DETAIL.md` for full adapter configs. [FILESYSTEM-S3-DETAIL](references/FILESYSTEM-S3-DETAIL.md).
- **[INSTALLATION.md](references/INSTALLATION.md)**: Refer to `INSTALLATION-DETAIL.md` for full Docker Compose examples, Dockerfile, and extension management deta…. [INSTALLATION-DETAIL](references/INSTALLATION-DETAIL.md).
- **[OBSERVABILITY.md](references/OBSERVABILITY.md)**: Refer to `OBSERVABILITY-DETAIL.md` for full configuration examples and Grafana stack setup. [OBSERVABILITY-DETAIL](references/OBSERVABILITY-DETAIL.md).
- **[PERFORMANCE.md](references/PERFORMANCE.md)**: Refer to `PERFORMANCE-DETAIL.md` for the full list of all tweaks. [PERFORMANCE-DETAIL](references/PERFORMANCE-DETAIL.md).
- **[REQUIREMENTS.md](references/REQUIREMENTS.md)**: Refer to the deep reference for the full recommended stack table and version details. [REQUIREMENTS-DETAIL](references/REQUIREMENTS-DETAIL.md).
- **[SEARCH.md](references/SEARCH.md)**: Refer to `SEARCH-DETAIL.md` for cluster architecture details, shard config, and debugging. [SEARCH-DETAIL](references/SEARCH-DETAIL.md).
- **[UPDATES.md](references/UPDATES.md)**: Refer to `UPDATES-DETAIL.md` for full CLI sequences and staging configuration. [UPDATES-DETAIL](references/UPDATES-DETAIL.md).
- **[WEBSERVER.md](references/WEBSERVER.md)**: Refer to `WEBSERVER-DETAIL.md` for full VCL examples and Fastly configs. [WEBSERVER-DETAIL](references/WEBSERVER-DETAIL.md).
- **[WORKER-CRON.md](references/WORKER-CRON.md)**: Refer to `WORKER-CRON-DETAIL.md` for full systemd unit files and supervisord config. [WORKER-CRON-DETAIL](references/WORKER-CRON-DETAIL.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (hosting, deployment, PaaS, shopware-cli) and the shopware-cli reference, retrieved 2026-08-20.
