# Contao 5.x — Dateiverwaltung

Quellen:
- https://docs.contao.org/5.x/manual/de/dateiverwaltung/
- https://docs.contao.org/5.x/manual/de/dateiverwaltung/dateien-und-ordner-verwalten/
- https://docs.contao.org/5.x/manual/de/dateiverwaltung/metadaten/
- https://docs.contao.org/5.x/manual/de/dateiverwaltung/downloads-kontrollieren/

---

## Überblick

Mit der Dateiverwaltung (auch "Dateimanager") kannst du Dateien und Ordner auf dem Server verwalten. Alle Benutzerdateien werden standardmäßig im Verzeichnis `files/` gespeichert.

Contao speichert alle Dateiinformationen in der Datenbank und vergibt jedem Eintrag eine eindeutige **UUID** (Universally Unique Identifier). Diese ID ist systemweit einzigartig und ermöglicht die Zuordnung von Dateien in Inhaltselementen auch nach Umbenennung oder Verschiebung.

Die Dateiverwaltung stellt die Verzeichnisstruktur als **hierarchischen Baum** dar. Ordner können per Plus-/Minus-Icon auf- und zugeklappt werden.

---

## 1. Dateien und Ordner verwalten

### Navigationssymbole

| Icon | Funktion | Beschreibung |
|------|----------|-------------|
| Stift | Bearbeiten | Umbenennen + Metadaten verwalten |
| Kopieren | Duplizieren | Datei oder Ordner kopieren |
| Pfeil | Verschieben | An andere Position verlagern |
| Mülleimer | Löschen | Dauerhaft entfernen |
| i | Informationen | Detailansicht (UUID, Größe, Pfad) |
| Pfeil hoch | Hochladen | Dateien in diesen Ordner laden |
| Bleistift | Datei bearbeiten | Texteditor für kompatible Dateitypen |
| Griff | Drag & Drop | Intuitive Verschiebung per Maus |

### Neue Ordner erstellen

Über die Schaltfläche **„Neuer Ordner"** mit zwei Optionen:
- **Öffentlich**: Ordner über HTTP erreichbar (Symlink in `web/files/`)
- **Nicht synchronisieren**: Verhindert Datenbankabgleich

#### Verschachtelte Ordner erstellen

Durch Eingabe eines Pfades wie `OrdnerA/OrdnerB` können direkt Unterordner erzeugt werden.

**Wichtig**: Bei verschachtelten Ordnern mit öffentlichem Zugang erhält lediglich der **letzte** (innerste) Ordner den öffentlichen Status.

### Dateien hochladen

**Standardlimits:**
- Dateigröße: bis 2 MB
- Bildgröße: bis 3000 × 3000 Pixel
- Bilder werden bei Überschreitung automatisch verkleinert

**DropZone**: In den Systemeinstellungen aktivierbar für komfortables Drag & Drop beim Upload.

**Gleichnamige Datei hochladen**: Die bestehende Datei wird aktualisiert, die **UUID bleibt erhalten** — alle Referenzen in Inhaltselementen bleiben gültig.

### FTP-Upload und Synchronisation

Bei FTP-Uploads müssen Dateinamen **ASCII-konform** sein. Sonderzeichen können zu Problemen führen.

| Problematisch | Optimal |
|--------------|---------|
| `Wies'n-Festzug München.jpg` | `Wiesn-Festzug-Muenchen.jpg` |
| `Foto 2024 (1).png` | `foto-2024-1.png` |

Nach einem FTP-Upload muss die Datenbank synchronisiert werden:
- Über den **Synchronisierungs-Button** in der Dateiverwaltung, oder
- Via CLI: `vendor/bin/contao-console contao:automator generateSymlinks`

---

## 2. Metadaten

Metadaten können für **alle Dateitypen** erfasst werden. Sie werden primär in Bildergalerien und Download-Elementen genutzt.

### Unterstützte Metadaten

| Feld | Beschreibung |
|------|-------------|
| **Titel** | Dateititel (z.B. für Bildbeschriftungen) |
| **Alternativer Text** | Alt-Attribut für Bilder (Barrierefreiheit) |
| **Link** | Verlinkung auf externe URL oder Seite |
| **Bildunterschrift** | Caption unter Bildern |
| **Lizenz-URL** | Lizenzhinweis (als JSON-LD Schema ausgegeben) |

### Mehrsprachige Metadaten

In mehrsprachigen Projekten können für jede Sprache **separate Metadaten** angelegt werden. Contao wählt automatisch die passende Sprache für den Besucher.

### HTML-Ausgabe-Beispiel (Bild-Inhaltselement)

```html
<div class="ce_image first block">
  <figure class="image_container">
    <a href="https://contao.org/de/" title="Contao CMS">
      <img src="…" width="…" height="…" alt="Contao CMS" itemprop="image">
    </a>
    <figcaption class="caption">Contao CMS</figcaption>
  </figure>
</div>
```

### Lizenz-URL (JSON-LD)

Die Lizenz-URL wird als `schema.org/ImageObject` im JSON-LD-Format ausgegeben:

```json
{
  "@type": "ImageObject",
  "contentUrl": "…",
  "license": "https://creativecommons.org/licenses/by/4.0/"
}
```

---

## 3. Downloads kontrollieren

### Verzeichnisschutz

Neue Ordner sind standardmäßig **öffentlich** (über HTTP erreichbar). Beim Anlegen die Option **„Öffentlich"** deaktivieren, um einen Ordner zu schützen.

**Wichtig**: Wenn ein übergeordneter Ordner öffentlich ist, können darin enthaltene Unterordner und Dateien **nicht** separat geschützt werden.

#### Technischer Hintergrund

Öffentliche Ordner werden als **Symlinks** unter `web/files/` erzeugt. Ohne Symlink sind Dateien für Browser nicht erreichbar.

Nicht-öffentliche Ordner sind per Browser **nicht direkt zugänglich**, aber über Contao-Inhaltselemente (Download, Downloads) weiterhin auslieferbar.

### Download-Element schützen

Der Zugriff auf Download-Elemente wird über **geschützte Seiten** oder **geschützte Inhaltselemente** beschränkt:

1. Schützendes Inhaltselement / Seite auf bestimmte Mitgliedergruppen beschränken
2. Downloads sind ausschließlich über diese Inhaltselemente zugänglich
3. Nur autorisierte Mitglieder können die Dateien herunterladen

### HTML-Ausgabe des Download-Elements

```html
<ul class="download_list">
  <li>
    <a href="?file=files/dokument.pdf" title="Herunterladen">
      dokument.pdf <span class="size">(124 KiB)</span>
    </a>
  </li>
</ul>
```

Der Pfad `?file=files/…` wird von Contao verarbeitet und gibt die Datei nur bei entsprechenden Rechten aus.

---

## Praxis-Tipps

### Datei-UUID finden

Im Informations-Dialog einer Datei (i-Icon) wird die UUID angezeigt. Diese kann in Entwicklungsszenarien für direkte Datenbankabfragen genutzt werden.

### Bild nicht im Frontend sichtbar?

Häufige Ursache: Der Ordner ist **nicht öffentlich** markiert. Lösung:
1. Ordner bearbeiten (Stift-Icon)
2. Option „Öffentlich" aktivieren
3. Symlink wird automatisch erstellt

### Suche ausblenden

Um den Suchbereich in der Dateiverwaltung auszublenden, kann ein DCA-Eintrag verwendet werden:

```php
// contao/dca/tl_files.php
$GLOBALS['TL_DCA']['tl_files']['config']['notSearchable'] = true;
```
