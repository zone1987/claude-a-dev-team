# shopware-cli account

Commands für Shopware Account-Verwaltung und Store-Publishing.

```bash
shopware-cli account login           # OIDC Browser-Flow
shopware-cli account logout
shopware-cli account producer extension list
shopware-cli account producer extension info pull path/to/MyPlugin
shopware-cli account producer extension info push path/to/MyPlugin
shopware-cli account producer extension upload MyPlugin-6.7.0.zip
```

## Command-Übersicht

| Command | Beschreibung |
|---------|--------------|
| `account login` | OIDC/OAuth2 Browser-Login |
| `account logout` | Lokalen Token invalidieren |
| `account producer extension list` | Alle eigenen Extensions listen (`--search`) |
| `account producer extension info pull` | Store-Infos + Assets in `.shopware-extension.yml` ziehen |
| `account producer extension info push` | Lokale Store-Infos hochladen |
| `account producer extension upload` | Extension-Zip hochladen + Code-Review triggern |

## Vertiefung

- [ACCOUNT-COMMANDS.md](ACCOUNT-COMMANDS.md) — Alle Flags, Upload-Flow, `.shopware-extension.yml`-Format
