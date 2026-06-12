# Contao 5 — Core Concepts

## Übersicht

Contao bietet ein breites Set an Erweiterungs- und Anpassungsmechanismen. Die acht
zentralen Konzepte bilden das Fundament jeder Contao-Entwicklung.

---

## 1. Data Container Arrays (DCA) & Models

**DCA** (Data Container Arrays) sind ein Kernkonzept des Contao Frameworks. Sie
beschreiben, wie Datensätze verwaltet werden — Felder, Paletten, Listenansichten,
Operationen und Datenbankschema.

**Models** sind objektorientierte Repräsentationen von DCA-Datensätzen. Sie ermöglichen
das Erstellen, Laden und Verändern von Daten über eine saubere API.

Beispiel: `NewsModel::findByPk(5)` — lädt einen News-Datensatz als Model-Objekt.

**Schlüsselpunkte:**
- Eine DCA-Datei pro Tabelle in `contao/dca/<tabellenname>.php`
- Felder definieren: `inputType`, `eval`, `sql`
- Paletten steuern die Backend-Formularansicht
- `PaletteManipulator` für nicht-destruktive Erweiterungen bestehender Paletten

---

## 2. Front-End-Module

Front-End-Module behandeln komplexe Funktionalitäten auf bestimmten Seiten oder
an bestimmten Stellen der Website. Beispiele: Navigationslisten, News-Listen,
Mitglieder-Formulare.

- Implementiert als Fragment-Controller (`AbstractFrontendModuleController`)
- Registrierung via `#[AsFrontendModule]`-Attribut
- DCA-Konfiguration in `tl_module`
- Template: `frontend_module/<type>.html.twig`

---

## 3. Content Elements

Content Elements verwalten beliebige und komplexe Inhalte innerhalb der
Seitenstruktur — statische Seiteninhalte, News-Detailansichten etc.

- Implementiert als Fragment-Controller (`AbstractContentElementController`)
- Registrierung via `#[AsContentElement]`-Attribut
- DCA-Konfiguration in `tl_content` (Paletten)
- Template: `content_element/<type>.html.twig`
- Ab Contao 5.3: Nested Fragments (verschachtelte Kind-Elemente)

---

## 4. Templating

Contao verwendet seit Version 4.12 nativ das **Twig-Template-System** von Symfony.
Ab Contao 5 sind die meisten Content Elements ausschließlich Twig-basiert.
PHP-Templates (Legacy) werden bis Contao 5 noch unterstützt, ab Contao 6 entfallen.

**Kernmechanismus:** Managed Namespace `@Contao` ermöglicht Template-Vererbung ohne
gegenseitiges Wissen der beteiligten Bundles. Mehrere Bundles können dasselbe Template
unabhängig voneinander erweitern.

---

## 5. Assets & Images

Contao unterstützt responsive Bildverarbeitung via GD lib, Imagick und Gmagick.

Assets werden über globale Arrays (`$GLOBALS['TL_CSS']`, `$GLOBALS['TL_JAVASCRIPT']`)
oder im Twig-Template via `{% use %}` und den `add`-Tag eingebunden.

---

## 6. Hooks

Hooks erlauben die Modifikation interner Prozesse an definierten Ausführungspunkten.

**Registrierung** via PHP-Attribut `#[AsHook('hookName')]` — bei aktiviertem Autowiring
und Autoconfigure reicht eine einzige PHP-Datei.

Beispiel-Hooks: `parseArticles`, `updatePersonalData`, `loadDataContainer`,
`replaceInsertTags`, `generatePage`, `initializeFrontend` etc.

---

## 7. Extensions (Bundles)

Erweiterungen sind Symfony-Bundles, die sich automatisch (via Manager Plugin) oder
manuell in Contao-Anwendungen integrieren.

**Verzeichnisstruktur eines Bundles:**
```
src/
├── ContaoExampleBundle.php       # Bundle-Klasse
├── ContaoManager/
│   └── Plugin.php                # Manager Plugin
├── Controller/                   # Controller-Klassen
├── EventListener/                # Hook- und Event-Listener
config/
├── services.yaml
└── routes.yaml
contao/
├── config/config.php
├── dca/
├── languages/
└── templates/
```

**composer.json:**
```json
{
    "type": "contao-bundle",
    "extra": {
        "contao-manager-plugin": "Vendor\\Bundle\\ContaoManager\\Plugin"
    }
}
```

---

## 8. Insert Tags

Insert Tags sind spezielle Token im Format `{{TAG_NAME}}` oder `{{TAG_NAME::PARAMETER}}`,
die vor der Frontend-Auslieferung durch dynamische Inhalte ersetzt werden.

- Eingebaut: `{{link::*}}`, `{{env::*}}`, `{{date::*}}`, `{{asset::*::*}}` etc.
- Eigene Tags: `#[AsInsertTag('name')]`-Attribut
- Block-Tags: `#[AsBlockInsertTag('name', endTag: 'endname')]`
- Flags für Ausgabe-Transformation: `#[AsInsertTagFlag('flag')]`

---

## Framework-Übersicht (weitere Konzepte)

Das Contao Framework enthält darüber hinaus:

| Bereich | Beschreibung |
|---------|-------------|
| Caching | HTTP-Caching-Integration |
| Cron | Contao-Cron-Funktionalität |
| Data Container Array | Vollständige DCA-Konfiguration |
| Filesystem | Dateiarbeit in Contao |
| Form Widgets | Eigene Input-Widgets |
| Image Processing | Bildverarbeitung und responsive Images |
| Models | ORM-ähnliche Datenbankabstraktion |
| Page Controllers | Seitentypen in der Seitenstruktur |
| Routing | Custom Routes und Request-Attribute |
| Search Indexing | Suchindex-Integration |
| Security | Symfony Security Integration |
| Translations | Übersetzungssystem |

---

*Quelle: https://docs.contao.org/5.x/dev/getting-started/core-concepts/*  
*https://docs.contao.org/5.x/dev/framework/*
