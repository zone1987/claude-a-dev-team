# shopware-cli extension

Commands for building, validating and packaging Shopware extensions.

```bash
shopware-cli extension build path/to/MyPlugin
shopware-cli extension validate --full path/to/MyPlugin
shopware-cli extension zip path/to/MyPlugin --disable-git
shopware-cli extension admin-watch path/to/MyPlugin http://localhost
```

## Command overview

| Command | Summary |
|---------|---------|
| `build` | Build admin/storefront assets (ESBuild/Webpack) |
| `validate` | Check the extension (fast or `--full` with PHPStan/ESLint) |
| `zip` | Create a release zip (git export or `--disable-git`) |
| `admin-watch` | Start the ESBuild dev proxy |
| `fix` | Run code fixers (PHPCSFixer, ESLint) |
| `format` | Run formatters (Prettier, PHP-CS-Fixer) |
| `get-name` | Print the technical name |
| `get-version` | Print the version |
| `get-changelog` | Print the changelog |
| `prepare` | Install Composer deps, clean up before zipping |
| `config-schema` | JSON schema for `.shopware-extension.yml` |

## Deep dive

- [EXTENSION-COMMANDS.md](EXTENSION-COMMANDS.md) — All flags, examples, edge cases
