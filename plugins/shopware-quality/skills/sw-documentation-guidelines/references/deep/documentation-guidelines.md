# Shopware Dokumentations-Guidelines: Vollständige Referenz

Quellen: `resources/guidelines/documentation-guidelines/` (alle Dateien)

---

## Zielgruppen

| Zielgruppe | Aufgaben |
|-----------|---------|
| Fullstack Developer | Plugin-Entwicklung, Templates, Routes/Controller |
| Frontend Developer | Admin, Themes, PWA |
| Backend Developer | DI/Service-Architektur, Message Queues, DAL, ElasticSearch |
| API Developer | API konsumieren, erweitern, Paradigmen |
| DevOps | Hosting, Deployment, Performance |
| Solution Architect | Hosting, Architektur, Extension-System, Paradigmen |
| Designer | Component Library, Design System |

---

## Dokumentationsstruktur

### Concepts

Erklärt Core-Konzepte von Shopware. Entry Point um zu verstehen wie die Plattform organisiert ist.
- **Erklärt** (nicht zeigt), was etwas ist und warum es so ist
- Kein Code; keine Schritt-für-Schritt-Anleitungen
- Pseudo-Code nur zur Illustration akzeptabel (keine Shopware-Source)
- Cross-Links zu verwandten Konzepten pflegen

**Aufbau eines Concept-Artikels:**
1. **Introduction**: Was ist das Konzept? Was kann es enthalten? Wie verhält es sich zu anderen Teilen? Was erwartet der Leser in verwandten Artikeln?
2. **Comprehensive explanation**: Details mit Beispielen, Tabellen, Grafiken
3. **Conclusions**: Überleitung zum nächsten Artikel

### Guides

Home für How-tos, Tutorials, Cookbooks, Beispiele.
- Enthält Code; gibt konkrete Beispiele; Schritt-für-Schritt-Anweisungen
- Cross-Links zurück zur Concepts-Section für verwandte Konzepte
- Erklärt Shopware-spezifische Begriffe und verlinkt zu Definitionen

### Resources

- API-Referenzen, Code-Referenzen, Testing-Referenzen
- Tooling-Dokumentation
- Links, SDKs, Libraries
- Guidelines für Contributions (dieses Dokument)

---

## Sprache und Grammatik

### Stimme und Ton

**Friendly** — weniger formal, menschlicher als ein Roboter; gelegentlich Humor wenn passend.

**Direct and clear** — auf den Punkt; Skim-lesbar; so einfach wie möglich.

**Customer focussed** — Leser als kompetent aber mit variablem Niveau annehmen.

### Aktiv- vs. Passivstimme

Aktiv bevorzugen:
```
Gut:    The user passes the access-key.
Schlecht: The access-key is passed by the user.
```

Passiv akzeptabel bei: Objektbetonung, De-Emphase des Subjekts, unbekannter Handelnder.

### Person

- Zweite Person ("you") statt erste ("we", "I")
- Imperativform: "Create a PDF file." statt "You need to create a PDF file."
- "our" vermeiden

### Tense

- Einfaches Präsens (simple present)
- Kein Futur oder Vergangenheit

### Abkürzungen

- Beim ersten Auftreten ausschreiben + Kürzel in Klammern: "JSON Web Token (JWT)"
- Bekannte Abkürzungen (API, HTTPS, PDF) müssen nicht erklärt werden
- Keine eigenen Abkürzungen erfinden
- Plural: "APIs", "IDEs" (bei Endung s/sh/ch/x: "OSes")

### Konjunktionen und Satzzeichen

- Kein Schrägstrich als Konjunktion (nicht "blue/red" — stattdessen "blue or red")
- Kein Ampersand als Konjunktion (nicht "&" — stattdessen "and")
- Oxford-Komma bei Aufzählungen: "assets, controllers, services, or tests"
- Em-Dash (—) für Gedankenpause; Hyphen (-) für Komposita, Zahlenbereiche, Präfix-Wörter

### Verbotenes

- Kein Internet-Slang
- Keine Buzzwords und Jargon
- Keine Idiome und Phrasen
- Kein "In order to" am Satzanfang wiederholen
- Kein "please", "request" (zu höflich/um etwas bitten)
- Nicht so schreiben wie man spricht

---

## Formatierung: Text

### Schriftauszeichnung

- **Bold** (`**bold**`): UI-Elemente, Notices (Warning/Important), API Status-Codes, Titel in Description-Lists
- *Italic* (`*italic*`): Spezifische Wörter/Phrasen, Parameter-Werte, Klassen, Methoden, Produktversionen, Key Terms
- Unterstrichen: NIE verwenden

### Listen

- **Nummerierte Liste**: sequentielle Schritte oder fixe Anzahl von Elementen
- **Bulleted List**: allgemeine Aufzählung mit `*` (nicht `-`)
- **Description List**: Titel (bold) + Beschreibung; kann nummeriert oder bulleted sein
- Sentence Case für alle Listen-Items

### Headings

- `#` (H1): Camel Case — z.B. "Flow Sequence Evaluation"
- `##` und tiefer: Sentence Case — z.B. "Flow sequence evaluation"
- Keine Heading-Hierarchie überspringen (kein H3 direkt unter H1)
- Keine Punkte am Ende von Headings

### Hyperlinks

- Bedeutungsvoller Link-Text; nicht "click here" oder "read this document"
- Kompletter Satz mit Kontext: "For more information, see [XY]"
- Link-Text kurz halten; wichtige Wörter an den Anfang
- Nicht dieselbe Link-Formulierung für unterschiedliche Ziele

### Tabellen

- Nicht in Sätze einbetten
- Nur wenn mehr als eine Zeile und Spalte vorhanden
- Sentence Case für alle Inhalte
- Keine Punkte am Satz-Ende in Tabellen-Zellen
- Tabelle einleiten mit vollständigem Satz + "the following table"

---

## Formatierung: Code

### Inline Code

Backticks für: Attribute, CLI-Namen, Klassen/Methoden/Funktions-Namen, Enum-Namen, Dateipfade, Verzeichnisse, HTTP-Methoden, Parameter-Werte, Environment-Variablen, Command-Output.

### Code Blocks

- Fenced Code Blocks (drei Backticks) für mehrzeiligen Code oder Terminal-Ausgaben
- Immer Sprach-Identifier angeben: ` ```php `, ` ```bash `, ` ```twig ` etc.
- In Listen: korrekte Einrückung um Liste nicht zu brechen
- Zwei Spaces als Indentation, keine Tabs
- Drei Punkte (`...`) auf eigener Zeile für ausgelassene Ausgabe

### Platzhalter

- In Großbuchstaben und kursiv: `*`PLACEHOLDER_NAME`*`
- Informative Namen verwenden; kein "X" als Platzhalter

### HTTP Status Codes

- Code-Font: `400 Bad Request`
- Range: `HTTP 2xx`
- Explizite Range: `400-499`

### CLI-Befehle

- `$`-Prompt am Anfang jeder Eingabezeile
- Kein Verzeichnispfad vor Prompt

### API-Referenz

- Jede Klasse, Interface, Konstante, Methode beschreiben
- HTTP-Methoden in Großbuchstaben: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- Parameter beschreiben inkl. Valid Values und Default
- Method-Namen mit Klammern: `getProduct()`

### Deprecations

```markdown
::: warning
**Deprecated** - Access it using this getProd() method instead.
:::
```

---

## Asset-Management

### Bilder

| Attribut | Vorgabe |
|----------|---------|
| Format | `.png` (Screenshots), `.svg` (Diagramme, Logos, Vektoren), `.gif` (Animationen) |
| Größe | max. 5 MB |
| Dimensionen | max. 768×576px (4:3) |
| Alt-Text | Pflicht für jedes Bild |
| Rand | Kein Border |
| PII | Maskieren: Passwörter, Logins, Account-Details |

**Naming:**
```
<topicName>-<meaningfulImageName>.svg
storefront-pages.svg

<topicName>-<subtopicName>-<meaningfulImageName>.svg
storefront-dataHandling-pages.svg

Serialisiert bei mehreren Bildern:
storefront-dataHandling-pages_01.svg
```

Alle Assets in `assets/`-Verzeichnis.

### Diagramme

Einsetzen bei:
- Architektur darstellen
- Komplexe Beziehungen zeigen
- Komplexe Workflows definieren

Tools:
- **Mermaid**: Flowcharts, Sequence Diagrams, State Machine Diagrams, Class Diagrams (als `mermaid`-Code-Block eingebettet)
- **Meteor Diagram Kit** (Figma): andere Diagramm-Typen; folgt Shopware-Design-Standards

### Screenshots

Einsetzen bei:
- Visualisierungen/Beispiele zeigen
- Panels mit Query/Einstellungen
- Neue Features hervorheben

Regeln:
- Neuestes OS-Versionen
- Fokussiertes aktives Fenster
- Kein unnötiger Whitespace/Scrollbalken
- Reale oder realitätsnahe Daten
- Kein Code in Screenshots (→ Code Blocks)
- Kein Screenshot für sich häufig ändernde Seiten

### Videos und GIFs

Einsetzen für: Ablauf von Prozeduren, visuelle Feature-Demonstration, Setup-Anleitungen.

- Captions und Transkripte für Videos
- Naming analog zu Bildern

### Datei-Naming

```
<two_digit_number>-<meaningful-name>.md
01-doc-process.md
```

---

## Dokumentationsprozess

### 1. Ideate

Vor dem Schreiben klären:
- Wer ist die Zielgruppe?
- Was wird dokumentiert?
- Was sind die Voraussetzungen?
- Welche Fragen werden beantwortet?
- Welche anderen Themen sind relevant?

### 2. Write — 30/90 Rule

- Bei **30% fertig**: Erster Draft + erstes Feedback auf High Level
- Bei **90% fertig**: Steady Review für In-depth-Validierung

Erster Draft:
- Dokumentstruktur (Themen-Fluss) vorbereiten
- Alle Punkte kurz skizzieren
- Gemeinsamen roten Faden beibehalten
- Platzhalter für Bilder und Code
- Cross-Referenzen einbauen
- Nicht-Shopware-spezifische Sprache bevorzugen oder verlinken

### 3. Review

Reviewer prüft: Allgemeinen Ansatz, Ton, Formulierung gem. Guidelines.

Mehrere Reviewer können vorteilhaft sein. Wiederholbarer Prozess bis Finalversion.

### 4. Publish

Vor Veröffentlichung prüfen ob alle ursprünglichen Fragen und Ziele erfüllt.

### 5. Versionen pflegen

Inhalte sind auf Shopware Major-Versionen basiert (6.3, 6.4, ...). Aktuell = `main`-Branch; ältere Versionen = eigene Branches.

Versions-Hinweis:
```markdown
::: info
This functionality is available starting with Shopware 6.4.3.0.
:::
```

---

## Embedding in Developer Portal

Repositories können Content via Docs CLI (`developer-portal`) einbetten:

```bash
# portal.json anpassen, dann:
./docs-cli manage
```

Nach Konfiguration in `.vitepress/navigation.ts` für Sidebar und in `.github/scripts/mount.sh` für Production Build.

Shortcuts in `package.json`:
- `docs:env` — Portal klonen/aktualisieren
- `docs:link` — Docs symlinken
- `docs:preview` — Vitepress Dev Server

---

## Referenzen

- `resources/guidelines/documentation-guidelines/01-general.md`
- `resources/guidelines/documentation-guidelines/02-conceptual-structure.md`
- `resources/guidelines/documentation-guidelines/03-language-and-grammar.md`
- `resources/guidelines/documentation-guidelines/04-fonts-and-formats/01-text.md`
- `resources/guidelines/documentation-guidelines/04-fonts-and-formats/02-code.md`
- `resources/guidelines/documentation-guidelines/05-methodize-assets.md`
- `resources/guidelines/documentation-guidelines/06-doc-process.md`
- `resources/guidelines/documentation-guidelines/07-embedding-external-repositories.md`
