---
name: sw-hosting
description: Shopware self-hosted operations: requirements, installation, webserver, database, search, HTTP caching, S3, env config, worker and cron, performance, observability, updates, deployment.
---

# Shopware self-hosting

Running Shopware on your own infrastructure. Ordered as you would set a server up: requirements first, deployment last.

## Reference map

- **[CACHING-HTTP.md](CACHING-HTTP.md)**: Refer to `CACHING-HTTP-DETAIL.md` for full YAML examples. [CACHING-HTTP-DETAIL](CACHING-HTTP-DETAIL.md).
- **[DATABASE.md](DATABASE.md)**: Refer to `DATABASE-DETAIL.md` for full MySQL and Redis configuration details. [DATABASE-DETAIL](DATABASE-DETAIL.md).
- **[DEPLOYMENT.md](DEPLOYMENT.md)**: Refer to `DEPLOYMENT-DETAIL.md` for full deploy.php, GitLab CI, and GitHub Actions examples. [DEPLOYMENT-DETAIL](DEPLOYMENT-DETAIL.md).
- **[ENV-CONFIG.md](ENV-CONFIG.md)**: Refer to `ENV-CONFIG-DETAIL.md` for the complete environment variables table. [ENV-CONFIG-DETAIL](ENV-CONFIG-DETAIL.md).
- **[FILESYSTEM-S3.md](FILESYSTEM-S3.md)**: Refer to `FILESYSTEM-S3-DETAIL.md` for full adapter configs. [FILESYSTEM-S3-DETAIL](FILESYSTEM-S3-DETAIL.md).
- **[INSTALLATION.md](INSTALLATION.md)**: Refer to `INSTALLATION-DETAIL.md` for full Docker Compose examples, Dockerfile, and extension management deta…. [INSTALLATION-DETAIL](INSTALLATION-DETAIL.md).
- **[OBSERVABILITY.md](OBSERVABILITY.md)**: Refer to `OBSERVABILITY-DETAIL.md` for full configuration examples and Grafana stack setup. [OBSERVABILITY-DETAIL](OBSERVABILITY-DETAIL.md).
- **[PERFORMANCE.md](PERFORMANCE.md)**: Refer to `PERFORMANCE-DETAIL.md` for the full list of all tweaks. [PERFORMANCE-DETAIL](PERFORMANCE-DETAIL.md).
- **[REQUIREMENTS.md](REQUIREMENTS.md)**: Refer to the deep reference for the full recommended stack table and version details. [REQUIREMENTS-DETAIL](REQUIREMENTS-DETAIL.md).
- **[SEARCH.md](SEARCH.md)**: Refer to `SEARCH-DETAIL.md` for cluster architecture details, shard config, and debugging. [SEARCH-DETAIL](SEARCH-DETAIL.md).
- **[UPDATES.md](UPDATES.md)**: Refer to `UPDATES-DETAIL.md` for full CLI sequences and staging configuration. [UPDATES-DETAIL](UPDATES-DETAIL.md).
- **[WEBSERVER.md](WEBSERVER.md)**: Refer to `WEBSERVER-DETAIL.md` for full VCL examples and Fastly configs. [WEBSERVER-DETAIL](WEBSERVER-DETAIL.md).
- **[WORKER-CRON.md](WORKER-CRON.md)**: Refer to `WORKER-CRON-DETAIL.md` for full systemd unit files and supervisord config. [WORKER-CRON-DETAIL](WORKER-CRON-DETAIL.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (hosting, deployment, PaaS, shopware-cli) and the shopware-cli reference, retrieved 2026-08-20.
