# Shopware 6 — Filesystem & S3 (Deep Reference)

Sources: `guides/hosting/infrastructure/filesystem.md`

## Overview

Shopware uses [Flysystem](https://flysystem.thephpleague.com/docs/) for all file operations.

Filesystem types:
- `public` — product images, media, theme, assets
- `private` — invoices, delivery notes, plugin private files
- `theme` — compiled theme files
- `sitemap` — sitemap XML files
- `asset` — bundle assets (JS, CSS)

Default: falls back to `public` config for `theme`, `asset`, `sitemap` if not explicitly set.

## Config location

```
config/packages/shopware.yaml
```

## Adapter types

### Local

```yaml
shopware:
    filesystem:
        public:
            type: "local"
            url: "https://your.domain/public"
            config:
                root: "%kernel.project_dir%/public"
```

### Amazon S3 (and compatible: MinIO, Wasabi, etc.)

```bash
composer require league/flysystem-async-aws-s3
```

```yaml
shopware:
    filesystem:
        public:
            type: "amazon-s3"
            url: "https://your-cloudfront-url"
            config:
                bucket: "my-public-bucket"
                region: "eu-central-1"
                endpoint: "https://s3.example.com"    # custom endpoint (MinIO etc.)
                root: "media"                          # subfolder in bucket
                use_path_style_endpoint: true          # required for non-AWS providers
                credentials:
                    key: 'ACCESS_KEY'
                    secret: 'SECRET_KEY'
```

### Google Cloud Storage

```bash
composer require league/flysystem-google-cloud-storage
```

```yaml
shopware:
    filesystem:
        public:
            type: "google-storage"
            url: "https://storage.googleapis.com/my-bucket"
            config:
                bucket: "my-bucket"
                projectId: "my-project"
                keyFilePath: "/path/to/service-account.json"
```

**Note:** Bucket must use "Fine-grained" ACL mode (not uniform access).

## Environment variable usage

```yaml
shopware:
    filesystem:
        public:
            type: "amazon-s3"
            url: "{{S3_URL}}"
            config:
                bucket: "{{AWS_BUCKET}}"
                region: "{{AWS_REGION}}"
                endpoint: "{{AWS_ENDPOINT}}"
                use_path_style_endpoint: true
                credentials:
                    key: "{{AWS_ACCESS_KEY_ID}}"
                    secret: "{{AWS_SECRET_ACCESS_KEY}}"
```

## YAML anchors to avoid duplication

```yaml
shopware:
    filesystem:
        public: &s3_config
            type: "amazon-s3"
            url: "{{S3_URL}}"
            config:
                bucket: "{{AWS_BUCKET}}"
                region: "{{AWS_REGION}}"
                endpoint: "{{AWS_ENDPOINT}}"
                use_path_style_endpoint: true
                credentials:
                    key: "{{AWS_ACCESS_KEY_ID}}"
                    secret: "{{AWS_SECRET_ACCESS_KEY}}"
        theme: *s3_config
        sitemap: *s3_config
        asset: *s3_config
```

## Private files

```yaml
shopware:
    filesystem:
        private:
            visibility: "private"
            type: "amazon-s3"
            config: ...
```

## Private file download strategies

```yaml
shopware:
    filesystem:
        private_local_download_strategy: x-accel  # php | x-sendfile | x-accel
```

| Strategy | Server | Description |
|---|---|---|
| `php` | Any | Streams file via PHP (default) |
| `x-sendfile` | Apache only | Requires `mod_xsendfile` |
| `x-accel` | Nginx only | Internal redirect (fastest) |

## Allowed file extensions

```yaml
shopware:
    filesystem:
        allowed_extensions:           # public filesystem
            - jpg
            - png
            - pdf
        private_allowed_extensions:   # private filesystem
            - pdf
            - xml
```

## CDN configuration

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

The `url` field changes where Shopware generates URLs for assets — the files stay local but URLs point to CDN.

## Fallback behavior

`theme`, `asset`, `sitemap` inherit `public` config if not explicitly configured. When changing `public` to S3 but wanting `theme` to stay local, explicitly configure `theme`:

```yaml
shopware:
    filesystem:
        public:
            type: "amazon-s3"
            ...
        theme:
            type: "local"
            url: "https://your.domain/public"
            config:
                root: "%kernel.project_dir%/public"
```

## Custom S3 HTTP client (since 6.7.9.0)

Register `shopware.filesystem.s3.client` service for custom timeouts/retries:

```yaml
# config/packages/framework.yaml
framework:
    http_client:
        scoped_clients:
            s3.http_client:
                base_uri: '{your-s3-endpoint}'
                timeout: 30.0
                http_version: '1.1'
```

```php
// config/services.php
use AsyncAws\Core\HttpClient\AwsRetryStrategy;
use Symfony\Component\HttpClient\RetryableHttpClient;

$services->set(AwsRetryStrategy::class);
$services->set('shopware.filesystem.s3.client', RetryableHttpClient::class)
    ->args([service('s3.http_client'), service(AwsRetryStrategy::class), 3]);
```

## Custom Flysystem adapter

```php
class MyFlysystemAdapterFactory implements AdapterFactoryInterface
{
    public function getType(): string
    {
        return 'my-adapter-prefix';
    }

    public function create(array $config): AdapterInterface
    {
        return new MyFlysystemAdapter($config);
    }
}
```

Register with tag `shopware.filesystem.factory`.

## Cluster: shared directories

Besides S3, share `var/services/` across app servers. This directory holds installed service source files. If not shared, each node re-downloads on first use (harmless but redundant).
