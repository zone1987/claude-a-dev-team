# Shopware 6 — Code-Struktur: Vollständige Referenz

Quellen: `guides/development/extensions/code-structure.md`, `guides/development/extensions/index.md`

---

## Extension-Typen im Vergleich

Shopware bietet zwei primäre Extension-Typen:

- **Plugins**: Vollständiger System-Zugriff, nur Self-hosted
- **Apps**: API-basiert, Cloud-kompatibel

Themes sind kein eigener Extension-Typ, sondern reduzierte Plugins (nur Storefront-UI); in Cloud-Umgebungen via Apps geliefert.

### Entscheidungs-Tabelle

| Task | Plugin (inkl. Theme) | App | Hinweis |
|------|---------------------|-----|---------|
| Storefront-Optik ändern | ✅ | ✅ | Themes sind Storefront-Plugins; in Cloud via Apps |
| Admin-Module hinzufügen | ✅ | ✅ | Themes können keine Admin-Module |
| Webhooks ausführen | ✅ | ✅ | Apps sind webhook-first |
| Custom Entities | ✅ | ✅ | |
| Datenbankstruktur ändern | ✅ | ❌ | Apps können kein DB-Schema ändern |
| Payment-Provider integrieren | ✅ | ✅ | |
| Im Shopware Store publizieren | ✅ | ✅ | |
| In Shopware Cloud installieren | ❌ | ✅ | Plugins laufen nicht in Cloud |
| In Self-hosted installieren | ✅ | ✅ | Apps seit 6.4.0.0 auch Self-hosted |
| Custom Logic/Routes/Commands | ✅ | ⚠️ | Apps implementieren Logik extern via Webhooks |
| Style/Template-Vererbung | ✅ | ✅ | Nur Theme-Plugins |

---

## Shared Patterns (alle Extension-Typen)

### Namespaces und Autoloading

- PSR-4 zu Ordnernamen mappen; tiefes Nesting vermeiden, das Ownership verbirgt
- Namespace-Stamm muss zum Bundle-Namen passen

```json
{
  "autoload": {
    "psr-4": {
      "MyVendor\\MyPlugin\\": "src/"
    }
  }
}
```

### Konfiguration

- Defaults zentralisieren und Override-Points dokumentieren
- Environment-Variablen nur in der Projekt-Schicht verwenden — NICHT in Store-Plugins

### Dokumentation

- Jede Extension sollte ein README mit: Zweck, Install/Update-Schritten, bekannten Einschränkungen

---

## Project/Bundle-Struktur

Bundles für bespoke Installationen mit vollem Kontrollanspruch.

```
src/
├── Bundle/
│   └── MyFeatureBundle.php     # Symfony Bundle Klasse
├── Service/
│   └── MyFeatureService.php    # Domain-Logik
├── Event/
│   └── MyFeatureEvent.php
├── Migration/
│   └── V6_7/
│       └── Migration*.php
└── Resources/
    └── config/
        └── services.xml
```

**Konventionen:**
- Domain-Logik in Bundles, NICHT in Templates oder Controllern
- Services via Dependency Injection exponieren
- `composer.json` type: `shopware-bundle`
- Namespaces mit Bundle-Namen ausrichten
- Integration-Points (Events, DAL Extensions) hinter Service-Klassen kapseln

---

## Plugin-Struktur (Static/Custom + Managed/Store)

### Pflicht-Verzeichnisstruktur

```
MyPlugin/
├── composer.json
├── src/
│   ├── MyPlugin.php              # Plugin-Klasse (extends Plugin)
│   ├── Migration/
│   │   └── V6_7/
│   │       └── Migration*.php
│   ├── Resources/
│   │   ├── config/
│   │   │   ├── services.xml
│   │   │   └── config.xml       # Plugin-Konfiguration
│   │   ├── views/               # Twig-Templates (Overrides)
│   │   ├── storefront/          # Storefront JS/SCSS Assets
│   │   └── administration/      # Admin-Module (wenn vorhanden)
│   └── [Domain]/               # Domain-spezifische Klassen
└── tests/
```

### Regeln

- Standard-Plugin-Skeleton verwenden — keine eigenen Auto-Loader oder Custom-Entrypoints
- Konfiguration, Migrations, Administration, Storefront-Assets in Default-Ordnern lassen
- Kein Cross-Wiring zwischen Plugins
- DB-Schema-Änderungen ausschließlich via Migrations; install/update-Code idempotent
- Für Store-Plugins: Keine Projekt-Annahmen (Hostnamen, Queues, Cron-Timing, Dateizugriff); Requirements dokumentieren + sichere Fallbacks

### composer.json Pflicht-Felder

```json
{
  "type": "shopware-platform-plugin",
  "extra": {
    "shopware-plugin-class": "MyVendor\\MyPlugin\\MyPlugin",
    "label": {
      "de-DE": "Mein Plugin",
      "en-GB": "My Plugin"
    }
  }
}
```

---

## App-Struktur

Apps implementieren Logik auf einem externen Server; Shopware kommuniziert via Webhooks/HTTP.

```
my-app/
├── manifest.xml           # App-Manifest (Pflicht)
├── Resources/
│   ├── views/             # Twig-Templates (Admin-Module)
│   └── app/
│       └── storefront/
│           └── src/       # Storefront-Overrides
└── src/
    └── (App-Backend-Code — separat gehostet)
```

**Regeln:**
- Manifest minimal und explizit: Permissions, Webhooks, Actions exakt dokumentieren
- App-Backend (API/Webhook-Handler) von UI-Assets trennen
- Kein stateful Coupling an Shop-Runtime; multi-tenant-tauglich designen
- Keine direkten PHP-Erweiterungen möglich (kein Schema-Änderung via DB-Migrations)

---

## Upgrade-orientierte Struktur

Je weniger Surface Area dem Platform-Core ausgesetzt wird, desto weniger Upgrade-Aufwand.

**Dos:**
- Integration-Points (Events, Decorators, DAL Extensions) hinter Service-Klassen isolieren
- Zusammengehörige Logik in einem Repository
- Konsistentes Tooling im gesamten Repository
- Minimale Cross-Plugin-Abhängigkeiten

**Don'ts:**
- Verwandte Logik auf mehrere unabhängige Plugins aufteilen
- Direkte Abhängigkeiten auf andere Plugins (ohne klare API-Verträge)
- Core-Klassen ohne Decoration-Pattern erweitern

---

## MCP-Server Erweiterbarkeit

Sowohl Plugins als auch Apps können dem Shopware Built-in MCP-Server eigene Tools, Prompts und Resources hinzufügen:

- Plugins: `guides/plugins/plugins/mcp-server.md`
- Apps: `guides/plugins/apps/mcp-server.md`

---

## Referenzen

- `guides/development/extensions/code-structure.md`
- `guides/development/extensions/index.md`
- Plugin Base Guide: `guides/plugins/plugins/plugin-base-guide.md`
- Bundle Guide: `guides/plugins/plugins/bundle.md`
- App Base Guide: `guides/plugins/apps/app-base-guide.md`
- Theme Base Guide: `guides/plugins/themes/theme-base-guide.md`
