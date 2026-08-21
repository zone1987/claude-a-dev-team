# Digital Sales Rooms — configuration

Full reference: [DIGITAL-SALES-ROOMS-CONFIG-CONFIGURATION.md](DIGITAL-SALES-ROOMS-CONFIG-CONFIGURATION.md)

## Quick start via CLI

```bash
# all configuration steps in one command (in the plugin root directory):
composer dsr:config

# or individually:
composer dsr:domain-setup    # domain configuration
composer dsr:daily-setup     # Daily.co video setup
composer dsr:mercure-setup   # Mercure realtime setup
```

## Manual configuration

1. **Domain** → sales channel → Domains section → add the DSR domain
2. **Plugin** → Marketing › Digital Sales Rooms › Configuration
   - Appointments: select the available DSR domains
   - Video and Audio: Daily.co API key
   - Realtime Service: Mercure hub URLs + secrets
