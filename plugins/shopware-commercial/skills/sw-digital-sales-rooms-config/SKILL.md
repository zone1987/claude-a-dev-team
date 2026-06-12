---
name: sw-digital-sales-rooms-config
description: >
  Konfiguration von Digital Sales Rooms: Domain-Setup im Sales Channel,
  CLI-Konfiguration (composer dsr:config) und Plugin-Einstellungsseite.
  Triggers: "DSR konfigurieren", "configure digital sales rooms",
  "composer dsr:config", "dsr domain setup", "dsr plugin config",
  "DSR domain sales channel", "dsr daily api key", "dsr mercure setup config"
---

# Digital Sales Rooms — Konfiguration

Vollständige Referenz: [references/deep/configuration.md](references/deep/configuration.md)

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
