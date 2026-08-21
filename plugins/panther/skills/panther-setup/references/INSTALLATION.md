# Symfony Panther — installation

```bash
composer require --dev symfony/panther
vendor/bin/bdi detect drivers   # recommended: automatic driver detection
```

## PHPUnit extension (required for full functionality)

```xml
<!-- phpunit.dist.xml (PHPUnit 10+) or phpunit.xml.dist (old) -->
<extensions>
    <bootstrap class="Symfony\Component\Panther\ServerExtension"/>
</extensions>
```

## Environment variables (short list)

| Variable                   | Description                               | Default     |
|----------------------------|-------------------------------------------|-------------|
| `PANTHER_NO_HEADLESS`      | Make the browser visible                  | —           |
| `PANTHER_WEB_SERVER_PORT`  | Port of the built-in PHP server           | `9080`      |
| `PANTHER_ERROR_SCREENSHOT_DIR` | Screenshot path on test failures      | —           |
| `PANTHER_NO_SANDBOX`       | Disable the sandbox (Docker/CI)           | —           |

## Deep dive

- [INSTALLATION-DETAIL.md](INSTALLATION-DETAIL.md) — complete driver options, all env vars, Docker, GitHub Actions, GitLab CI, SSL
