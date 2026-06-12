# Contao 5.x — Seitenstruktur

Quellen:
- https://docs.contao.org/5.x/manual/de/seitenstruktur/
- https://docs.contao.org/5.x/manual/de/seitenstruktur/seiten-als-zentrale-elemente/
- https://docs.contao.org/5.x/manual/de/seitenstruktur/mehrsprachige-webseiten/
- https://docs.contao.org/5.x/manual/de/seitenstruktur/multidomain-betrieb/

---

## Seiten als zentrale Elemente

Contao ist ein **seitenbasiertes CMS**. Die Seitenstruktur ist das zentrale Element:

- Besucher rufen Seiten auf, keine einzelnen Beiträge
- Seiten werden über ihren **Alias** im Frontend aufgerufen
- Hierarchische Verschachtelung möglich (Eltern-/Kindseiten)
- Navigationsmenüs werden automatisch generiert
- Eigenschaften werden an Unterseiten **vererbt** (Layout, Zugriffsrechte)

### Analogie

Eine Seite funktioniert wie eine Fernsehsendung: Redakteure erstellen Beiträge (Inhalte), ein Chefredakteur entscheidet über die Veröffentlichung (Seitenstruktur und Zugriffsrechte). Inhalte erscheinen erst im Frontend, wenn sie einer Seite zugeordnet sind.

### Bestandteile einer Seite

Jede Seite weiß:
- Welche Artikel mit ihr verknüpft sind
- Welches **Seitenlayout** zur Darstellung verwendet wird
- Ob sie gecacht werden darf
- Welche Benutzer auf sie zugreifen dürfen

Das Seitenlayout unterteilt die Seite in Layoutbereiche. Darin befinden sich Frontend-Module, die der Reihe nach HTML generieren. CSS ist im Seitenlayout eingebettet (Theme-Manager).

---

## Seitentypen

### Übersicht aller Seitentypen

| Seitentyp | Funktion |
|-----------|---------|
| **Website-Startseite** | Startpunkt einer Webseite; ermöglicht Multidomain-Betrieb und Mehrsprachigkeit |
| **Reguläre Seite** | Normale Inhaltsseite, vergleichbar mit einer statischen HTML-Datei |
| **Interne Weiterleitung** | Leitet zu einer anderen Seite innerhalb derselben Installation weiter |
| **Externe Weiterleitung** | Leitet zu einer externen URL oder einer anderen Domain weiter |
| **Abmelden** | Erstellt einen Abmelde-Link für geschützte Bereiche (mit optionaler Weiterleitung) |
| **401 Nicht authentifiziert** | Erscheint für nicht eingeloggte Besucher ohne Zugriff auf geschützte Seiten |
| **403 Zugriff verweigert** | Erscheint für eingeloggte Besucher ohne ausreichende Rechte |
| **404 Seite nicht gefunden** | Erscheint bei Aufruf nicht existierender Seiten |
| **503 Dienst nicht verfügbar** | Erscheint wenn eine Root-Seite im Wartungsmodus ist |
| **News-Feed** | Erstellt RSS-, Atom- oder JSON-Feeds aus Nachrichtenarchiven |

### Website-Startseite (Root-Seite)

Die Startseite kennzeichnet den Einstiegspunkt einer Webseite. Sie definiert:
- Domain-Zuordnung (für Multidomain-Betrieb)
- Sprache der Webseite
- Sprachfallback (ja/nein)
- URL-Präfix (z. B. `/de/` für mehrsprachige Sites)

Eine Contao-Installation kann mehrere Website-Startseiten haben (Multidomain, Mehrsprachigkeit).

---

## Multidomain-Betrieb

### Grundprinzip

Multidomain-Betrieb = eine Contao-Installation ist unter **mehreren Domains** erreichbar und liefert je nach Domain **unterschiedliche Inhalte**.

**Echter Multidomain-Betrieb erfordert:**
- Mehrere Domains UND
- Mehrere Website-Startseiten in der Seitenstruktur (je eine pro Domain)

**Kein echter Multidomain-Betrieb**: Dieselbe Webseite unter mehreren Domains erreichbar → Problem: Duplicate Content für Suchmaschinen. Lösung: eine primäre Domain wählen, andere per Redirect weiterleiten.

### Redirect-Beispiel (`.htaccess`)

```apache
RewriteEngine On
RewriteCond %{HTTP_HOST} ^www\.example\.com [NC]
RewriteRule (.*) http://www.example.org/$1 [R=301,L]
```

### Anwendungsbeispiel: Agentur mit mehreren Kunden-Domains

Domains: `firma.at`, `firma.ch`, `firma.de` — alle zeigen auf eine Contao-Installation.

In der Seitenstruktur drei Website-Startseiten mit je eingetragener Domain:

| Startpunkt | Domain | Aufgerufene Website |
|-----------|--------|-------------------|
| Österreich | firma.at | Nur österreichische Seite |
| Schweiz | firma.ch | Nur schweizerische Seite |
| Deutschland | firma.de | Nur deutsche Seite |

**Wichtig**: `www.firma.at/produkte.html` gibt 404, wenn „Produkte" nur in der Schweizer Webseite existiert.

---

## Mehrsprachige Webseiten

### Contaos Ansatz

Contao unterstützt ausschließlich den Ansatz **separate Webseiten pro Sprache** in der Seitenstruktur. Jede Sprache = eigene Website-Startseite.

Die Strukturen können sich unterscheiden (deutsche und englische Version müssen nicht identische Seiten haben).

### URL-Präfix für Sprachen

Um die Sprache in die URL einzubinden (z. B. `www.example.com/de/`):

Website-Startseite bearbeiten → **URL-Präfix** eintragen (z. B. `de`).

Ergebnis:
- `www.example.com/` = Englisch (ohne Präfix)
- `www.example.com/de/` = Deutsch
- `www.example.com/fr/` = Französisch

### Cache nach Änderungen leeren

```bash
vendor/bin/contao-console cache:clear --env=prod --no-warmup
vendor/bin/contao-console cache:warmup --env=prod
```

### Den richtigen Startpunkt finden

Contao prüft beim Seitenaufruf vier Möglichkeiten (in dieser Reihenfolge):

1. Gibt es eine Seite, die zur **Domain UND Sprache** des Besuchers passt?
2. Gibt es eine Seite, die zur **Domain passt** und **Sprachfallback** aktiviert hat?
3. Gibt es eine Seite **ohne Domain**, die zur **Sprache** des Besuchers passt?
4. Gibt es eine Seite **ohne Domain** mit **Sprachfallback**?

### Praxisbeispiel: Zwei-Domains-Szenario

Domains: `www.example.com` (Firmenseite), `www.example.org` (Privatseite)

Benötigte Startpunkte:

| Seite | Domain | Sprache | Fallback |
|-------|--------|---------|---------|
| Firma deutsch | – | de | – |
| Firma englisch | – | en | ja |
| Privat | example.org | de | ja |

**Routing-Tabelle**:

| Domain | Browser-Sprache | Ziel | Treffer-Typ |
|--------|----------------|------|------------|
| www.example.com | Deutsch | Firma deutsch | Sprache |
| www.example.com | Englisch | Firma englisch | Sprache |
| www.example.com | Spanisch | Firma englisch | Fallback |
| www.example.org | beliebig | Privat | Domain |

**Ohne Sprachfallback** wäre die Privatseite nur für deutschsprachige Besucher zugänglich. Spanischsprachige Besucher würden „Keine Seiten gefunden" sehen.

### Wichtiger Hinweis

Drittanbieter-Erweiterungen können alternative Mehrsprachigkeitsansätze bieten (z. B. Inhalte in einer einzigen Webseite mit automatischer Übersetzung).
