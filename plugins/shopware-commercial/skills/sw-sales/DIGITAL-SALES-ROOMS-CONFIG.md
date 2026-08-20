# Digital Sales Rooms — Konfiguration

Vollständige Referenz: [DIGITAL-SALES-ROOMS-CONFIG-CONFIGURATION.md](DIGITAL-SALES-ROOMS-CONFIG-CONFIGURATION.md)

## Schnellstart via CLI

```bash
# Alle Konfigurationsschritte in einem Befehl (im Plugin-Root-Verzeichnis):
composer dsr:config

# Oder einzeln:
composer dsr:domain-setup    # Domain-Konfiguration
composer dsr:daily-setup     # Daily.co Video-Setup
composer dsr:mercure-setup   # Mercure Realtime-Setup
```

## Manuelle Konfiguration

1. **Domain** → Sales Channel → Domains-Sektion → DSR-Domain hinzufügen
2. **Plugin** → Marketing › Digital Sales Rooms › Configuration
   - Appointments: verfügbare DSR-Domains auswählen
   - Video and Audio: Daily.co API-Key
   - Realtime Service: Mercure Hub-URLs + Secrets
