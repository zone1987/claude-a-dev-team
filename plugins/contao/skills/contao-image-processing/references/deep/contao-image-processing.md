# Contao Image Processing (5.x)

## Architektur-Überblick

| Anwendungsfall | Komponente | Abstraktionslevel |
|----------------|-----------|-------------------|
| Template-Bildausgabe | Image Studio | Hoch |
| Kontrolliertes Resize | ImageFactory / PictureFactory | Mittel |
| Außerhalb Contao | contao/image | Niedrig-mittel |
| Direkte Manipulation | imagine/imagine, contao/imagine-svg | Niedrig |

**Verarbeitungskette:** Contao → Imagine → PHP-Extensions (GD / ImageMagick / GraphicsMagick)

**Integrierte Templates:** `image.html5`, `picture_default.html5`, `figure.html.twig`

---

## ImageFactory

Dienst: `contao.image.factory` → implements `ImageFactoryInterface`

### Methode `create($path, $size, $options)`

| Parameter | Typen |
|-----------|-------|
| `$path` | `string` oder `ImageInterface` |
| `$size` | `array` (Size Array), `int` (DB-ID), `ResizeConfiguration` |
| `$options` | `string` (Zielpfad) oder `ResizeOptions` |

**Rückgabe:** `ImageInterface` (oder `DeferredImageInterface` wenn kein Zielpfad + noch nicht vorhanden)

```php
use Contao\CoreBundle\Image\ImageFactoryInterface;

public function __construct(private readonly ImageFactoryInterface $imageFactory) {}

$image = $this->imageFactory->create(
    '/path/to/image.jpg',
    [100, 100, ResizeConfiguration::MODE_CROP],
);

$image->getPath();                          // /root/assets/images/9/image-6dc4b466.jpg
$image->getUrl('/root');                    // assets/images/9/image-6dc4b466.jpg
$image->getDimensions()->getSize()->getWidth(); // 100
```

### Mit Zielpfad

```php
$image = $this->imageFactory->create(
    '/path/to/source/image.jpg',
    [100, 100, ResizeConfiguration::MODE_CROP],
    '/path/to/target/image.jpg',
);
```

---

## PictureFactory

Dienst: `contao.image.picture_factory` → implements `PictureFactoryInterface`

Erzeugt responsive Bilder mit mehreren Varianten für `<picture>`, `srcset`, `sizes`.

```php
use Contao\CoreBundle\Image\PictureFactoryInterface;

public function __construct(private readonly PictureFactoryInterface $pictureFactory) {}

$picture = $this->pictureFactory->create(
    '/path/to/image.jpg',
    [100, 100, ResizeConfiguration::MODE_CROP]
);
```

`$size` akzeptiert: `array`, `int`, `string` oder `PictureConfiguration`.

---

## Size Array Format

```php
// Statischer Resize-Modus
$size = [256, 128, 'crop'];
$size = [256, 128, ResizeConfiguration::MODE_BOX];
// Gültige Modi: crop | box | proportional

// Datenbankgespeicherte Konfiguration (tl_image_size ID)
$size = [0, 0, 8];

// config.yaml-Referenz (Unterstrich-Präfix!)
$size = [0, 0, '_example'];
```

---

## Image Sizes (config.yaml)

### Einfache Konfiguration

```yaml
# config/config.yaml
contao:
    image:
        sizes:
            example:
                width: 512
            foobar:
                width: 1024
```

### Erweiterte Konfiguration

```yaml
contao:
    image:
        sizes:
            example:
                width: 128
                height: 128
                resize_mode: crop    # crop | box | proportional
                zoom: 100
                css_class: example
                lazy_loading: true
                densities: 1.5x, 2x
```

### Media Queries / Responsive `<picture>`

```yaml
contao:
    image:
        sizes:
            example:
                width: 1024
                height: 512
                resize_mode: box
                densities: 1.25x
                items:
                    -
                        media: '(max-width: 512px)'
                        width: 128
                        height: 64
                        resize_mode: box
                        densities: 2x
                    -
                        media: '(max-width: 1024px)'
                        width: 512
                        height: 256
                        resize_mode: box
                        densities: 1.5x
```

### Format-Konvertierung (WebP-Fallback)

```yaml
contao:
    image:
        sizes:
            example:
                width: 256
                height: 256
                resize_mode: crop
                formats:
                    jpg: [webp, jpg]
                    webp: [webp, jpg]
                    png: [webp, png]
```

### Defaults

```yaml
contao:
    image:
        sizes:
            _defaults:
                formats:
                    jpg: [webp, jpg]
                densities: 0.75x, 2x
                lazy_loading: true
                resize_mode: crop
            large_photo:
                width: 1000
                height: 500
```

### Backend-Übersetzung

```yaml
# translations/image_sizes.en.yaml
example: Image with 512 Pixel width
```

---

## Image Studio

### Studio-Klassen

| Klasse | Zweck |
|--------|-------|
| `FigureBuilder` | Fluent API zum Erstellen von `Figure`-Objekten |
| `Figure` | Datenbehälter für alle Bilddaten |
| `ImageResult` | Lazy-geladene Bild-/Source-Daten |
| `LightboxResult` | Lightbox-Gruppe + optionales Resize |

Dienst: `Contao\CoreBundle\Image\Studio\Studio`

### FigureBuilder – Basis

```php
use Contao\CoreBundle\Image\Studio\Studio;

public function __construct(private readonly Studio $studio) {}

$figure = $this->studio
    ->createFigureBuilder()
    ->fromUuid($myUuid)
    ->setSize([800, 600, 'crop'])
    ->enableLightbox()
    ->build();
```

### Resource-Methoden

| Methode | Quelle |
|---------|--------|
| `fromFilesModel($model)` | FilesModel-Instanz |
| `fromUuid($uuid)` | UUID aus tl_files |
| `fromId($id)` | ID aus tl_files |
| `fromPath($path)` | Dateipfad (auto-erkennt FilesModel) |
| `fromImage($image)` | ImageInterface |
| `from($resource)` | Auto-Erkennung |

### Konfigurations-Methoden

| Methode | Zweck |
|---------|-------|
| `setSize($size)` | Resize (Array / PictureConfiguration / Referenz) |
| `setMetadata($meta)` | Metadaten überschreiben oder deaktivieren |
| `setLocale($locale)` | Locale für Metadaten |
| `setLinkHref($href)` | Link-URL |
| `setLinkAttribute($key, $val)` | Link-Attribut |
| `enableLightbox()` | Lightbox aktivieren |
| `setLightboxSize($size)` | Lightbox-Bildgröße |
| `setLightboxGroupIdentifier($id)` | Lightbox-Gruppe (`data-lightbox`) |
| `setOptions($options)` | Template-spezifische Optionen |

### Twig-Ausgabe

```twig
{{ figure(id, '_my_size') }}

{% set special_size = picture_config({
    width: 400,
    height: 400,
    resizeMode: 'proportional'
}) %}
{{ figure(uuid, special_size) }}
```

### PHP-Template (Legacy)

```php
$template = new FrontendTemplate('image');
$figure->applyLegacyTemplateData($template);

// Oder inline
echo $this->figure('path/to/image.png', '_my_size');
```

---

*Quellen:*
- *https://docs.contao.org/5.x/dev/framework/image-processing/*
- *https://docs.contao.org/5.x/dev/framework/image-processing/image-picture-factory/*
- *https://docs.contao.org/5.x/dev/framework/image-processing/image-sizes/*
- *https://docs.contao.org/5.x/dev/framework/image-processing/image-studio/*
