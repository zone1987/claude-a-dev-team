---
name: sw-hosting-filesystem-s3
description: >
  Shopware 6 Filesystem — S3, GCS, lokaler Adapter, CDN, private/public Dateien, Cluster-Shared-Dirs.
  Triggers: "filesystem s3", "s3 adapter", "google cloud storage", "flysystem", "cdn configuration",
  "media storage", "file storage", "private files", "public files", "theme files",
  "Dateisystem", "S3 einrichten", "externe Dateiablage", "CDN", "shared filesystem cluster",
  "x-sendfile", "x-accel nginx", "var/services shared"
---

# Shopware Hosting — Filesystem & S3

Refer to `references/deep/filesystem-s3.md` for full adapter configs.

## Basic structure

```yaml
# config/packages/shopware.yaml
shopware:
    filesystem:
        public:
            url: "https://cdn.example.com"
            type: "amazon-s3"
            config:
                bucket: "my-bucket"
                region: "eu-central-1"
                endpoint: "https://s3.example.com"
                credentials:
                    key: '...'
                    secret: '...'
        private:
            visibility: "private"
            type: "amazon-s3"
            config: ...
        theme: ...
        sitemap: ...
        asset: ...
```

Use YAML anchors to avoid duplication:
```yaml
shopware:
    filesystem:
        public: &s3_config
            type: "amazon-s3"
            url: "{{S3_URL}}"
            config:
                bucket: "{{AWS_BUCKET}}"
                region: "{{AWS_REGION}}"
        theme: *s3_config
        sitemap: *s3_config
```

## Install S3 adapter

```bash
composer require league/flysystem-async-aws-s3
```

## Google Cloud Storage

```bash
composer require league/flysystem-google-cloud-storage
```

```yaml
type: "google-storage"
config:
    bucket: "my-bucket"
    projectId: "my-project"
    keyFilePath: "/path/to/key.json"
```

## Private file download strategies
- `php` (default) – streamed response
- `x-sendfile` (Apache) – requires `mod_xsendfile`
- `x-accel` (Nginx) – internal redirect

## Cluster: shared directories
Besides S3, share `var/services/` across app servers (installed service source files).

## CDN (public files only)

```yaml
# config/packages/prod/shopware.yaml
shopware:
    filesystem:
        public:
            url: "https://cdn.example.com"
            type: "local"
            config:
                root: "%kernel.project_dir%/public"
```

See also: `sw-hosting-installation` (Docker volumes), `sw-hosting-deployment` (build without DB).

Full reference: `references/deep/filesystem-s3.md`
