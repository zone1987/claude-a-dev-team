---
name: sw-plugin-create
description: Scaffold eines neuen Shopware-6-Plugins mit korrekten Owner-/Namens-/Namespace-Konventionen, composer.json, Plugin-Klasse und Grundstruktur.
argument-hint: <PluginName> [--owner Ff|Adt|Ag|Pb] [--sw 6.7|6.8|6.9|7.0]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-plugin-create

Lege ein neues Shopware-6-Plugin an. Nutze das Skill `sw-plugin-base` für die Detailregeln.

## Ablauf (eine Frage pro Schritt, überspringe Beantwortetes)
1. **Plugin-Name** (PascalCase, kein Theme). Aus `$ARGUMENTS` falls vorhanden.
2. **Owner** aus Präfix ableiten (`Ff`→forty-four, `Adt`→A-Dev-Team, `Ag`→Andreas Gerhardt, `Pb`→Pfötchenbuddies);
   sonst fragen und Präfix voranstellen.
3. **Zweck** ("Was soll das Plugin machen?") → DE- + EN-`label` für composer.json.
4. **Lizenz** (MIT oder proprietary).
5. **Ziel-Version** → `conflict`-Range (6.7 → `<6.7 || >=6.8`, 6.8 → `<6.8 || >=6.9`, …).

## Erzeugte Struktur
```
<PluginName>/
├── composer.json          # type: shopware-platform-plugin, extra.shopware-plugin-class, extra.label (de/en),
│                          # autoload psr-4 "{PluginName}\\": "src/", conflict-Range
├── src/
│   ├── <PluginName>.php    # extends Shopware\Core\Framework\Plugin
│   └── Resources/config/services.xml
├── README.md
└── CHANGELOG.md
```

Namespace = `{PluginName}\{PluginName}`, PSR-4-Root `src/`. Plugin-Klasse minimal (Logik via DI).
Nach dem Anlegen: Hinweis auf `bin/console plugin:refresh && plugin:install --activate <PluginName>` und auf
`/sw-entity`, `/sw-controller`, `/sw-admin-module` für nächste Bausteine. Keine erfundenen composer-Felder.
