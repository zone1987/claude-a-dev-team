# shopware-cli account

Commands for Shopware Account management and store publishing.

```bash
shopware-cli account login           # OIDC browser flow
shopware-cli account logout
shopware-cli account producer extension list
shopware-cli account producer extension info pull path/to/MyPlugin
shopware-cli account producer extension info push path/to/MyPlugin
shopware-cli account producer extension upload MyPlugin-6.7.0.zip
```

## Command overview

| Command | Description |
|---------|-------------|
| `account login` | OIDC/OAuth2 browser login |
| `account logout` | Invalidate the local token |
| `account producer extension list` | List all of your own extensions (`--search`) |
| `account producer extension info pull` | Pull store info + assets into `.shopware-extension.yml` |
| `account producer extension info push` | Upload local store info |
| `account producer extension upload` | Upload extension zip + trigger code review |

## Deep dive

- [ACCOUNT-COMMANDS.md](ACCOUNT-COMMANDS.md) — All flags, upload flow, `.shopware-extension.yml` format
