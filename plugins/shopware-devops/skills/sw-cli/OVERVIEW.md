# shopware-cli — Überblick

`shopware-cli` ist ein in Go geschriebenes CLI für alle Shopware-DevOps-Aufgaben:
Extension-Build, Projekt-Management, Account-Upload, CI-Pipelines.

```bash
# Installation
curl -1sLf https://dl.cloudsmith.io/public/friendsofshopware/stable/setup.deb.sh | sudo bash
sudo apt install shopware-cli          # Debian/Ubuntu

brew install shopware/homebrew-tap/shopware-cli  # macOS

go install github.com/shopware/shopware-cli@latest  # Go
npm install -g @shopware-ag/shopware-cli            # npm
# Docker: shopware/shopware-cli:latest
```

## Globale Flags

| Flag | Kurz | Default | Beschreibung |
|------|------|---------|--------------|
| `--verbose` | | false | Debug-Ausgabe |
| `--no-interaction` | `-n` | false | Kein interaktiver Input (CI-safe) |
| `--version` | | | Version ausgeben |

## Command-Gruppen

| Gruppe | Beschreibung |
|--------|--------------|
| `account` | Shopware Account: Login, Logout, Producer/Store-Aktionen |
| `extension` | Extension Build, Validate, Zip, Watch, Fix, Format |
| `project` | Projekt-Management: Create, CI-Build, DB-Dump, Worker, Admin-API |

## Vertiefung

- [ALL-COMMANDS.md](ALL-COMMANDS.md) — Alle Commands mit Flags und Zweck (erschöpfend)
- [INTERNAL-PACKAGES.md](INTERNAL-PACKAGES.md) — Wichtige interne Go-Packages
