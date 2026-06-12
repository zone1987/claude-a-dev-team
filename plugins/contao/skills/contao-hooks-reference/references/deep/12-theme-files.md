# Contao Hooks – Theme / Dateien

Hooks für Theme-Import/-Export, XML-Generierung, Dateikombination, Downloads und Uploads.

---

## `compareThemeFiles`

**Zweck:** Wird während des Theme-Imports ausgelöst, wenn Contao einen Vergleich anzeigt (fehlende Datenbankfelder, zu überschreibende Template-Dateien etc.). Ermöglicht eigene Vergleichs-HTML-Ausgabe.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\DOMDocument` | `$xml` | XML-Objekt mit den Theme-Daten |
| 2 | `\Contao\ZipReader` | `$zip` | ZIP-Archiv mit den Theme-Dateien |

**Rückgabe:** `string` – Eigenes HTML für die Backend-Vergleichsanzeige, oder leerer String.

**Zeitpunkt:** Beim Theme-Import, wenn der Vergleich zwischen importiertem Theme und aktueller Installation angezeigt wird.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\ZipReader;

#[AsHook('compareThemeFiles')]
class CompareThemeFilesListener
{
    public function __invoke(\DOMDocument $xml, ZipReader $zip): string
    {
        if ($this->hasCustomData($xml)) {
            return '<div class="custom-comparison">Custom-Vergleich...</div>';
        }
        return '';
    }
}
```

---

## `exportTheme`

**Zweck:** Wird beim Theme-Export ausgelöst. Ermöglicht das Hinzufügen eigener Daten zur XML-Datei und zum ZIP-Archiv.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\DOMDocument` | `$xml` | XML-Objekt mit den Theme-Daten |
| 2 | `\Contao\ZipWriter` | `$zipArchive` | ZIP-Archiv mit den Theme-Dateien |
| 3 | `int` | `$themeId` | ID des exportierten Themes |

**Rückgabe:** `void`

**Zeitpunkt:** Bei Theme-Export-Operationen im Contao-Backend.

```php
use Contao\ZipWriter;

#[AsHook('exportTheme')]
class ExportThemeListener
{
    public function __invoke(\DOMDocument $xml, ZipWriter $zipArchive, int $themeId): void
    {
        // Eigene Dateien zum ZIP hinzufügen
        $zipArchive->addString('custom_data.json', json_encode(['themeId' => $themeId]));
        
        // XML-Daten ergänzen
        $element = $xml->createElement('customData', 'value');
        $xml->documentElement->appendChild($element);
    }
}
```

---

## `extractThemeFiles`

**Zweck:** Wird beim Theme-Import ausgelöst, wenn ein Theme extrahiert wird. Ermöglicht eigene Logik wie Datei-Platzierung oder Datenbankabfragen.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\DOMDocument` | `$xml` | XML-Objekt mit den Theme-Daten |
| 2 | `\Contao\ZipReader` | `$zipArchive` | ZIP-Archiv mit den Theme-Dateien |
| 3 | `int` | `$themeId` | ID des importierten Themes |
| 4 | `array` | `$mapper` | Datenbank-Mapping-Daten |

**Rückgabe:** `void`

**Zeitpunkt:** Beim Theme-Import, wenn das Archiv extrahiert wird.

```php
use Contao\ZipReader;

#[AsHook('extractThemeFiles')]
class ExtractThemeFilesListener
{
    public function __invoke(\DOMDocument $xml, ZipReader $zipArchive, int $themeId, array $mapper): void
    {
        // Eigene Theme-Dateien aus dem Archiv extrahieren und platzieren
    }
}
```

---

## `generateXmlFiles`

**Zweck:** Wird ausgelöst, wenn XML-Dateien (z.B. Sitemaps, Feeds) neu generiert werden (über Backend-Wartung "XML-Dateien neu erstellen" oder programmatisch).

**Parameter:** keine

**Rückgabe:** `void`

**Zeitpunkt:** Beim Regenerieren der XML-Dateien.

```php
#[AsHook('generateXmlFiles')]
class GenerateXmlFilesListener
{
    public function __invoke(): void
    {
        // Eigene XML-Datei(en) generieren oder aktualisieren
        $this->generateMyCustomXmlFeed();
    }
}
```

---

## `getCombinedFile`

**Zweck:** Wird beim Zusammenführen von CSS- oder JavaScript-Dateien ausgelöst. Erlaubt Modifikation des kombinierten Dateiinhalts vor dem Speichern.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$content` | Inhalt der Datei, die zum Kombinierer hinzugefügt wird |
| 2 | `string` | `$key` | Eindeutiger Bezeichner für die temporäre Datei in `system/scripts/` |
| 3 | `string` | `$mode` | Kombinierer-Modus: `Combiner::CSS` oder `Combiner::JS` |
| 4 | `array` | `$file` | Detaillierte Informationen über die kombinierte Datei |

**Rückgabe:** `string` – Modifizierter kombinierter Dateiinhalt.

**Zeitpunkt:** Beim Dateikombinierungsprozess für CSS- oder JS-Ressourcen.

```php
use Contao\Combiner;

#[AsHook('getCombinedFile')]
class GetCombinedFileListener
{
    public function __invoke(string $content, string $key, string $mode, array $file): string
    {
        if (Combiner::CSS === $mode) {
            // CSS-Inhalte nachbearbeiten, z.B. Variablen ersetzen
            $content = str_replace('var(--my-var)', '#ff0000', $content);
        }
        return $content;
    }
}
```

---

## `postDownload`

**Zweck:** Wird ausgelöst, nachdem eine Datei vom Browser heruntergeladen wurde (z.B. über Download(s)-Content-Elemente oder Anhänge in News/Events).

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$file` | Heruntergeladene Datei (relativer Pfad von `TL_ROOT`) |

**Rückgabe:** `void`

**Zeitpunkt:** Nach dem Senden einer Datei an den Browser.

> **Hinweis:** Für moderne Contao-5-Anwendungen wird ein `kernel.response`-Listener empfohlen, da neuere Komponenten diesen Hook nicht mehr verwenden.

```php
#[AsHook('postDownload')]
class PostDownloadListener
{
    public function __invoke(string $file): void
    {
        // Download-Statistik erfassen
        $this->trackDownload($file);
    }
}
```

---

## `postUpload`

**Zweck:** Wird ausgelöst, nachdem ein Benutzer eine oder mehrere Dateien im Backend hochgeladen hat.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `array` | `$files` | Liste hochgeladener Dateien (Pfade relativ zum Contao-Root) |

**Rückgabe:** `void`

**Zeitpunkt:** Nach dem Abschluss von Datei-Uploads im Backend.

```php
#[AsHook('postUpload')]
class PostUploadListener
{
    public function __invoke(array $files): void
    {
        foreach ($files as $file) {
            // z.B. Thumbnails generieren, CDN hochladen
            $this->processUploadedFile($file);
        }
    }
}
```

---

## `removeOldFeeds`

**Zweck:** Wird ausgelöst, wenn veraltete XML-Dateien aus dem Contao-Root-Verzeichnis entfernt werden. Ermöglicht das Schützen eigener Feed-Dateien vor der Löschung.

**Parameter:** keine

**Rückgabe:** `array` – Array von XML-Dateinamen (ohne Extension), die erhalten werden sollen.

**Zeitpunkt:** Beim automatischen Bereinigungsprozess veralteter XML-Feed-Dateien.

```php
#[AsHook('removeOldFeeds')]
class RemoveOldFeedsListener
{
    public function __invoke(): array
    {
        // Diese XML-Dateien nicht löschen
        return ['mein-custom-feed', 'anderer-feed'];
    }
}
```

---

_Quelle: https://docs.contao.org/5.x/dev/reference/hooks/ (Stand 2025-06)_
