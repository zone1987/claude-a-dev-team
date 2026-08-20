# Contao 5 — Initial Setup

## Installation: Managed Edition

```bash
composer create-project contao/managed-edition
# Spezifische Version:
composer create-project contao/managed-edition . 5.7
```

Die **Managed Edition** ist für Projekte gedacht, bei denen Contao der zentrale
Bestandteil der Anwendung ist. Sie ermöglicht automatische Konfiguration durch
Drittanbieter-Bundles.

---

## Managed Edition Internals

### Kernkomponenten

1. **Manager Bundle** (`contao/manager-bundle`)  
   Stellt das Anwendungs-Skelett bereit: Einstiegspunkte und Konfigurationsdateien.
   
2. **Manager Plugin** (`contao/manager-plugin`)  
   Ein Composer-Plugin, das nach jeder `composer install`/`composer update` automatisch
   den `contao-setup`-Script ausführt.

### Was `contao-setup` tut

- Erstellt Anwendungsstruktur und benötigte Verzeichnisse
- Baut den Cache neu
- Generiert erforderliche Symlinks

**composer.json (Managed Edition):**

```json
{
    "scripts": {
        "post-install-cmd": ["@php vendor/bin/contao-setup"],
        "post-update-cmd": ["@php vendor/bin/contao-setup"]
    }
}
```

Der spezialisierte Kernel der Managed Edition fragt installierte Packages nach
Konfigurationsdaten durch Interfaces des Manager Plugins ab — vollständige
Autokonfiguration ist das Ergebnis.

---

## Integration in bestehende Symfony Application

Contao kann als eigenständiges Symfony-Bundle in bestehende Symfony-Anwendungen
integriert werden. Diese Option ist sinnvoll, wenn Contao nur ergänzende CMS-Features
liefert, während die Symfony-App der Kern ist.

### Contao 5.3 in Symfony Application

Die Installationsanleitung für Contao 5.3 LTS als Symfony-Bundle ist unter
`https://docs.contao.org/5.x/dev/getting-started/initial-setup/symfony-application/contao-5.3/`
dokumentiert.

**Grundsatz:** Da Contao ein Symfony-Bundle ist, gelten alle Standard-Symfony-Bundles-
Konventionen. Die Integration erfordert:
- Bundle-Registrierung im Kernel
- Routing-Konfiguration
- Datenbank-Migrationen

---

## Wann welche Variante?

| Kriterium | Managed Edition | Symfony Application |
|-----------|----------------|---------------------|
| Contao ist Hauptkomponente | ✅ | ❌ |
| Automatische Bundle-Konfiguration | ✅ | Manuell |
| Bestehende Symfony-App | ❌ | ✅ |
| Einfachste Updates | ✅ | ❌ |

---

## Entwicklung starten

Nach der Installation mit der Managed Edition:

1. `composer install` (ohne `--optimize-autoloader` in der Entwicklung)
2. Neue Klassen sind sofort verfügbar ohne Cache-Neubau
3. Eigener Code in `src/`, Contao-spezifisches in `contao/`

**Empfehlung:** `.env`-Dateien statt `parameters.yaml` für sensible Daten verwenden.

---

*Quelle: https://docs.contao.org/5.x/dev/getting-started/initial-setup/*  
*https://docs.contao.org/5.x/dev/getting-started/initial-setup/managed-edition/*  
*https://docs.contao.org/5.x/dev/getting-started/initial-setup/symfony-application/*
