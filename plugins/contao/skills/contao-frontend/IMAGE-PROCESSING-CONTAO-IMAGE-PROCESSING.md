# Contao Image Processing (5.x)

## Contents

- [Architecture overview](#architecture-overview)
- [ImageFactory](#imagefactory)
- [PictureFactory](#picturefactory)
- [Size Array Format](#size-array-format)
- [Image Sizes (config.yaml)](#image-sizes-configyaml)
- [Image Studio](#image-studio)

## Architecture overview

| Use case | Component | Abstraction level |
|----------------|-----------|-------------------|
| Image output in templates | Image Studio | High |
| Controlled resize | ImageFactory / PictureFactory | Medium |
| Outside of Contao | contao/image | Low to medium |
| Direct manipulation | imagine/imagine, contao/imagine-svg | Low |

**Processing chain:** Contao → Imagine → PHP extensions (GD / ImageMagick / GraphicsMagick)

**Integrated templates:** `image.html5`, `picture_default.html5`, `figure.html.twig`

---

## ImageFactory

Service: `contao.image.factory` → implements `ImageFactoryInterface`

### Method `create($path, $size, $options)`

| Parameter | Types |
|-----------|-------|
| `$path` | `string` or `ImageInterface` |
| `$size` | `array` (size array), `int` (DB ID), `ResizeConfiguration` |
| `$options` | `string` (target path) or `ResizeOptions` |

**Returns:** `ImageInterface` (or `DeferredImageInterface` if there is no target path and it does not exist yet)

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

### With a target path

```php
$image = $this->imageFactory->create(
    '/path/to/source/image.jpg',
    [100, 100, ResizeConfiguration::MODE_CROP],
    '/path/to/target/image.jpg',
);
```

---

## PictureFactory

Service: `contao.image.picture_factory` → implements `PictureFactoryInterface`

Generates responsive images with multiple variants for `<picture>`, `srcset`, `sizes`.

```php
use Contao\CoreBundle\Image\PictureFactoryInterface;

public function __construct(private readonly PictureFactoryInterface $pictureFactory) {}

$picture = $this->pictureFactory->create(
    '/path/to/image.jpg',
    [100, 100, ResizeConfiguration::MODE_CROP]
);
```

`$size` accepts: `array`, `int`, `string` or `PictureConfiguration`.

---

## Size Array Format

```php
// Static resize mode
$size = [256, 128, 'crop'];
$size = [256, 128, ResizeConfiguration::MODE_BOX];
// Valid modes: crop | box | proportional

// Configuration stored in the database (tl_image_size ID)
$size = [0, 0, 8];

// config.yaml reference (note the underscore prefix!)
$size = [0, 0, '_example'];
```

---

## Image Sizes (config.yaml)

### Simple configuration

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

### Advanced configuration

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

### Media queries / responsive `<picture>`

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

### Format conversion (WebP fallback)

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

### Backend translation

```yaml
# translations/image_sizes.en.yaml
example: Image with 512 Pixel width
```

---

## Image Studio

### Studio classes

| Class | Purpose |
|--------|-------|
| `FigureBuilder` | Fluent API for creating `Figure` objects |
| `Figure` | Data container for all image data |
| `ImageResult` | Lazily loaded image/source data |
| `LightboxResult` | Lightbox group + optional resize |

Service: `Contao\CoreBundle\Image\Studio\Studio`

### FigureBuilder – basics

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

### Resource methods

| Method | Source |
|---------|--------|
| `fromFilesModel($model)` | FilesModel instance |
| `fromUuid($uuid)` | UUID from tl_files |
| `fromId($id)` | ID from tl_files |
| `fromPath($path)` | File path (auto-detects FilesModel) |
| `fromImage($image)` | ImageInterface |
| `from($resource)` | Auto-detection |

### Configuration methods

| Method | Purpose |
|---------|-------|
| `setSize($size)` | Resize (array / PictureConfiguration / reference) |
| `setMetadata($meta)` | Override or disable metadata |
| `setLocale($locale)` | Locale for metadata |
| `setLinkHref($href)` | Link URL |
| `setLinkAttribute($key, $val)` | Link attribute |
| `enableLightbox()` | Enable the lightbox |
| `setLightboxSize($size)` | Lightbox image size |
| `setLightboxGroupIdentifier($id)` | Lightbox group (`data-lightbox`) |
| `setOptions($options)` | Template-specific options |

### Twig output

```twig
{{ figure(id, '_my_size') }}

{% set special_size = picture_config({
    width: 400,
    height: 400,
    resizeMode: 'proportional'
}) %}
{{ figure(uuid, special_size) }}
```

### PHP template (legacy)

```php
$template = new FrontendTemplate('image');
$figure->applyLegacyTemplateData($template);

// Or inline
echo $this->figure('path/to/image.png', '_my_size');
```

---

*Sources:*
- *https://docs.contao.org/5.x/dev/framework/image-processing/*
- *https://docs.contao.org/5.x/dev/framework/image-processing/image-picture-factory/*
- *https://docs.contao.org/5.x/dev/framework/image-processing/image-sizes/*
- *https://docs.contao.org/5.x/dev/framework/image-processing/image-studio/*
