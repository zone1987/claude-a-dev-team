# Contao Hooks – Theme / Files

Hooks for theme import/export, XML generation, file combining, downloads and uploads.

---

## Contents

- [`compareThemeFiles`](#comparethemefiles)
- [`exportTheme`](#exporttheme)
- [`extractThemeFiles`](#extractthemefiles)
- [`generateXmlFiles`](#generatexmlfiles)
- [`getCombinedFile`](#getcombinedfile)
- [`postDownload`](#postdownload)
- [`postUpload`](#postupload)
- [`removeOldFeeds`](#removeoldfeeds)

## `compareThemeFiles`

**Purpose:** Triggered during the theme import when Contao shows a comparison (missing database fields, template files to be overwritten etc.). Allows your own comparison HTML output.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\DOMDocument` | `$xml` | XML object with the theme data |
| 2 | `\Contao\ZipReader` | `$zip` | ZIP archive with the theme files |

**Returns:** `string` – Your own HTML for the back end comparison view, or an empty string.

**Timing:** During the theme import, when the comparison between the imported theme and the current installation is displayed.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;
use Contao\ZipReader;

#[AsHook('compareThemeFiles')]
class CompareThemeFilesListener
{
    public function __invoke(\DOMDocument $xml, ZipReader $zip): string
    {
        if ($this->hasCustomData($xml)) {
            return '<div class="custom-comparison">Custom comparison...</div>';
        }
        return '';
    }
}
```

---

## `exportTheme`

**Purpose:** Triggered during the theme export. Allows adding your own data to the XML file and to the ZIP archive.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\DOMDocument` | `$xml` | XML object with the theme data |
| 2 | `\Contao\ZipWriter` | `$zipArchive` | ZIP archive with the theme files |
| 3 | `int` | `$themeId` | ID of the exported theme |

**Returns:** `void`

**Timing:** During theme export operations in the Contao back end.

```php
use Contao\ZipWriter;

#[AsHook('exportTheme')]
class ExportThemeListener
{
    public function __invoke(\DOMDocument $xml, ZipWriter $zipArchive, int $themeId): void
    {
        // Add your own files to the ZIP
        $zipArchive->addString('custom_data.json', json_encode(['themeId' => $themeId]));
        
        // Extend the XML data
        $element = $xml->createElement('customData', 'value');
        $xml->documentElement->appendChild($element);
    }
}
```

---

## `extractThemeFiles`

**Purpose:** Triggered during the theme import when a theme is extracted. Allows your own logic such as file placement or database queries.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `\DOMDocument` | `$xml` | XML object with the theme data |
| 2 | `\Contao\ZipReader` | `$zipArchive` | ZIP archive with the theme files |
| 3 | `int` | `$themeId` | ID of the imported theme |
| 4 | `array` | `$mapper` | Database mapping data |

**Returns:** `void`

**Timing:** During the theme import, when the archive is extracted.

```php
use Contao\ZipReader;

#[AsHook('extractThemeFiles')]
class ExtractThemeFilesListener
{
    public function __invoke(\DOMDocument $xml, ZipReader $zipArchive, int $themeId, array $mapper): void
    {
        // Extract and place your own theme files from the archive
    }
}
```

---

## `generateXmlFiles`

**Purpose:** Triggered when XML files (e.g. sitemaps, feeds) are regenerated (through the back end maintenance task "Regenerate the XML files" or programmatically).

**Parameters:** none

**Returns:** `void`

**Timing:** While the XML files are regenerated.

```php
#[AsHook('generateXmlFiles')]
class GenerateXmlFilesListener
{
    public function __invoke(): void
    {
        // Generate or update your own XML file(s)
        $this->generateMyCustomXmlFeed();
    }
}
```

---

## `getCombinedFile`

**Purpose:** Triggered when CSS or JavaScript files are combined. Allows modifying the combined file content before it is stored.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$content` | Content of the file that is added to the combiner |
| 2 | `string` | `$key` | Unique identifier of the temporary file in `system/scripts/` |
| 3 | `string` | `$mode` | Combiner mode: `Combiner::CSS` or `Combiner::JS` |
| 4 | `array` | `$file` | Detailed information about the combined file |

**Returns:** `string` – The modified combined file content.

**Timing:** During the file combining process for CSS or JS resources.

```php
use Contao\Combiner;

#[AsHook('getCombinedFile')]
class GetCombinedFileListener
{
    public function __invoke(string $content, string $key, string $mode, array $file): string
    {
        if (Combiner::CSS === $mode) {
            // Post-process the CSS content, e.g. replace variables
            $content = str_replace('var(--my-var)', '#ff0000', $content);
        }
        return $content;
    }
}
```

---

## `postDownload`

**Purpose:** Triggered after a file has been downloaded by the browser (e.g. through download content elements or attachments in news/events).

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `string` | `$file` | Downloaded file (path relative to `TL_ROOT`) |

**Returns:** `void`

**Timing:** After a file has been sent to the browser.

> **Note:** For modern Contao 5 applications, a `kernel.response` listener is recommended, because newer components no longer use this hook.

```php
#[AsHook('postDownload')]
class PostDownloadListener
{
    public function __invoke(string $file): void
    {
        // Record download statistics
        $this->trackDownload($file);
    }
}
```

---

## `postUpload`

**Purpose:** Triggered after a user has uploaded one or more files in the back end.

**Parameters:**

| # | Type | Name | Description |
|---|-----|------|-------------|
| 1 | `array` | `$files` | List of uploaded files (paths relative to the Contao root) |

**Returns:** `void`

**Timing:** After file uploads in the back end have finished.

```php
#[AsHook('postUpload')]
class PostUploadListener
{
    public function __invoke(array $files): void
    {
        foreach ($files as $file) {
            // e.g. generate thumbnails, upload to a CDN
            $this->processUploadedFile($file);
        }
    }
}
```

---

## `removeOldFeeds`

**Purpose:** Triggered when outdated XML files are removed from the Contao root directory. Allows protecting your own feed files from deletion.

**Parameters:** none

**Returns:** `array` – Array of XML file names (without the extension) that should be kept.

**Timing:** During the automatic clean-up process for outdated XML feed files.

```php
#[AsHook('removeOldFeeds')]
class RemoveOldFeedsListener
{
    public function __invoke(): array
    {
        // Do not delete these XML files
        return ['my-custom-feed', 'other-feed'];
    }
}
```

---

_Source: https://docs.contao.org/5.x/dev/reference/hooks/ (as of 2025-06)_
