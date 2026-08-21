# Contao 5.x — Services, Events, Commands, Config, Request Attributes

---

## Contents

- [1. Core Services](#1-core-services)
- [2. Events](#2-events)
- [3. Commands](#3-commands)
- [4. Bundle Configuration (contao.yaml)](#4-bundle-configuration-contaoyaml)
- [5. Environment Variables](#5-environment-variables)
- [6. Request Attributes](#6-request-attributes)

## 1. Core Services

### ContaoFramework

Initializes the legacy Contao framework and provides adapters for static classes.

```php
use Contao\CoreBundle\Framework\ContaoFramework;

class MyService
{
    public function __construct(private readonly ContaoFramework $framework) {}

    public function doSomething(): void
    {
        $this->framework->initialize();
        $adapter = $this->framework->getAdapter(\Contao\Config::class);
        $value = $adapter->get('uploadPath');
    }
}
```

---

### CsrfTokenManager

Generates and validates request tokens for your own forms (required for POST requests on Contao routes).

**Service-ID:** `@contao.csrf.token_manager`  
**Token name:** from `contao.csrf_token_name` (default: `contao_csrf_token`)

```php
use Symfony\Component\Security\Csrf\CsrfTokenManagerInterface;

class MyController
{
    public function __construct(
        private readonly CsrfTokenManagerInterface $csrfTokenManager
    ) {}

    public function form(): Response
    {
        $token = $this->csrfTokenManager->getToken('contao_csrf_token')->getValue();
        // Embed in the form: <input type="hidden" name="REQUEST_TOKEN" value="{{ token }}">
    }
}
```

---

### Database Connection

Access to configured database connections via Doctrine DBAL.

**Service:** `database_connection`  
**Type:** `Doctrine\DBAL\Connection`

```php
use Doctrine\DBAL\Connection;

class MyRepository
{
    public function __construct(private readonly Connection $db) {}

    public function findAll(): array
    {
        return $this->db->fetchAllAssociative('SELECT * FROM tl_example');
    }
}
```

---

### EntityCacheTags

Enables cache tagging and invalidation based on entity/model classes following the naming convention `contao.db.tl_content.5`.

```php
use Contao\CoreBundle\Cache\EntityCacheTags;

class MyController
{
    public function __construct(private readonly EntityCacheTags $cacheTags) {}

    public function show(int $id): Response
    {
        $response = new Response(…);
        $this->cacheTags->tagWith('tl_example');
        // or: $this->cacheTags->tagWith($model);
        return $response;
    }
}
```

---

### OptIn

Central opt-in tracking with automatic cleanup after the legally required period.

**Prefix restriction:** 6 characters before the hyphen.

```php
use Contao\CoreBundle\OptIn\OptIn;

class RegistrationService
{
    public function __construct(private readonly OptIn $optIn) {}

    public function createToken(string $email): string
    {
        $token = $this->optIn->create('reg-', $email, ['tl_member' => [0]]);
        return $token->getIdentifier();
    }
}
```

---

### Router

Symfony routing service for URL generation to routes inside services.

```php
use Symfony\Component\Routing\Generator\UrlGeneratorInterface;

class MyService
{
    public function __construct(private readonly UrlGeneratorInterface $router) {}

    public function getUrl(): string
    {
        return $this->router->generate('my_route', ['id' => 42]);
    }
}
```

---

### ScopeMatcher

Detects whether a request belongs to the Contao back end or front end.

**Service:** `contao.routing.scope_matcher`

```php
use Contao\CoreBundle\Routing\ScopeMatcher;
use Symfony\Component\HttpFoundation\RequestStack;

class MyEventListener
{
    public function __construct(
        private readonly RequestStack $requestStack,
        private readonly ScopeMatcher $scopeMatcher,
    ) {}

    public function onKernelRequest(): void
    {
        $request = $this->requestStack->getCurrentRequest();
        
        if ($this->scopeMatcher->isBackendRequest($request)) {
            // Back end logic
        }
        
        if ($this->scopeMatcher->isFrontendRequest($request)) {
            // Front end logic
        }
    }
}
```

---

### Security Helper

Retrieves the current back end or front end user and checks authorization roles.

```php
use Symfony\Bundle\SecurityBundle\Security;

class MyService
{
    public function __construct(private readonly Security $security) {}

    public function checkAccess(): void
    {
        $user = $this->security->getUser(); // BackendUser | FrontendUser | null

        if ($this->security->isGranted('ROLE_ADMIN')) {
            // Admin logic
        }

        if ($this->security->isGranted('ROLE_USER')) {
            // Back end user
        }

        if ($this->security->isGranted('ROLE_MEMBER')) {
            // Front end member
        }
    }
}
```

---

### SimpleTokenParser

Parses simple tokens with replacement and conditional expressions, extensible via `contao.simple_token_extension` tags.

```php
use Contao\CoreBundle\String\SimpleTokenParser;

class MyService
{
    public function __construct(private readonly SimpleTokenParser $parser) {}

    public function parse(string $text, array $tokens): string
    {
        return $this->parser->parse($text, $tokens);
        // Example: $text = 'Hallo ##firstname##!'
        // $tokens = ['firstname' => 'Max']
        // Result: 'Hallo Max!'
    }
}
```

---

### Slug

Generates human-readable unique identifiers from strings.

```php
use Contao\CoreBundle\Slug\Slug;

class AliasGenerator
{
    public function __construct(private readonly Slug $slug) {}

    public function generate(string $title, int $id): string
    {
        return $this->slug->generate(
            $title,
            $id,
            fn(string $alias) => null !== \Contao\NewsModel::findByAlias($alias)
        );
    }
}
```

---

### TokenChecker

Queries Contao security token information.

```php
use Contao\CoreBundle\Security\Authentication\Token\TokenChecker;

class MyService
{
    public function __construct(private readonly TokenChecker $tokenChecker) {}

    public function check(): void
    {
        $hasFrontendUser  = $this->tokenChecker->hasFrontendUser();
        $hasBackendUser   = $this->tokenChecker->hasBackendUser();
        $isPreviewMode    = $this->tokenChecker->isPreviewMode();
        $frontendUsername = $this->tokenChecker->getFrontendUsername();
        $backendUsername  = $this->tokenChecker->getBackendUsername();
    }
}
```

---

### InsertTagParser

Replaces insert tags in strings.

```php
use Contao\CoreBundle\InsertTag\InsertTagParser;

class MyService
{
    public function __construct(private readonly InsertTagParser $parser) {}

    public function process(string $text): string
    {
        // For text context (HTML-safe)
        $plain = $this->parser->replace($text);

        // For inline text (not full HTML)
        $inline = $this->parser->replaceInline($text);

        // Chunked for selective escaping
        $chunked = $this->parser->replaceChunked($text); // ChunkedText
        
        return $plain;
    }
}
```

---

### RequestStack

Access to the current HTTP request from the service container.

```php
use Symfony\Component\HttpFoundation\RequestStack;

class MyService
{
    public function __construct(private readonly RequestStack $requestStack) {}

    public function getLocale(): string
    {
        return $this->requestStack->getCurrentRequest()?->getLocale() ?? 'de';
    }
}
```

---

### ResponseContextAccessor

Access to or setting of the response context for Contao requests.

```php
use Contao\CoreBundle\Routing\ResponseContext\ResponseContextAccessor;

class MyContentElement
{
    public function __construct(
        private readonly ResponseContextAccessor $responseContextAccessor
    ) {}

    public function generate(): string
    {
        $context = $this->responseContextAccessor->getResponseContext();
        // e.g. for CSP tags, JSON-LD, etc.
        return '';
    }
}
```

---

### Locales

Locale/language information with translations.

```php
use Contao\CoreBundle\Intl\Locales;

class LocaleService
{
    public function __construct(private readonly Locales $locales) {}

    public function getAll(): array
    {
        // All configured locales ['de' => 'Deutsch', 'en' => 'English', …]
        return $this->locales->getLocales();
    }

    public function getEnabled(): array
    {
        // Locales enabled in the back end
        return $this->locales->getEnabledLocales();
    }
}
```

Configuration: `contao.intl.locales`, `contao.intl.enabled_locales`

---

### Countries

Country codes and translated country names.

```php
use Contao\CoreBundle\Intl\Countries;

class CountryService
{
    public function __construct(private readonly Countries $countries) {}

    public function getAll(): array
    {
        // ['DE' => 'Deutschland', 'AT' => 'Österreich', …]
        return $this->countries->getCountries();
    }
}
```

Configuration: `contao.intl.countries`

---

### Mailer

Symfony mailer service for sending e-mail.

```php
use Symfony\Component\Mailer\MailerInterface;
use Symfony\Component\Mime\Email;

class NotificationService
{
    public function __construct(private readonly MailerInterface $mailer) {}

    public function sendMail(string $to, string $subject, string $body): void
    {
        $email = (new Email())
            ->from('noreply@example.com')
            ->to($to)
            ->subject($subject)
            ->text($body);

        $this->mailer->send($email);
    }
}
```

---

### PageFinder (as of 5.3)

Finds pages from the page structure by hostname or request.

```php
use Contao\CoreBundle\Routing\PageFinder;

class MyService
{
    public function __construct(private readonly PageFinder $pageFinder) {}

    public function findRoot(string $host): ?\Contao\PageModel
    {
        return $this->pageFinder->findRootPageForHostAndLanguage($host, 'de');
    }

    // As of 5.4:
    public function getCurrent(): ?\Contao\PageModel
    {
        return $this->pageFinder->getCurrentPage();
    }
}
```

---

### ContentUrlGenerator (as of 5.3)

Generates URLs for content objects such as pages and news entries.

```php
use Contao\CoreBundle\Routing\ContentUrlGenerator;

class MyService
{
    public function __construct(private readonly ContentUrlGenerator $urlGenerator) {}

    public function getUrl(\Contao\PageModel $page): string
    {
        return $this->urlGenerator->generate($page);
    }
}
```

---

## 2. Events

Contao implements events via the Symfony event dispatcher.

### contao.backend_menu_build

Executed while the back end menu is being built. Allows modification of the menu structure.

**Event class:** `\Contao\CoreBundle\Event\MenuEvent`

```php
use Contao\CoreBundle\Event\MenuEvent;
use Symfony\Component\EventDispatcher\Attribute\AsEventListener;

#[AsEventListener]
class BackendMenuListener
{
    public function __invoke(MenuEvent $event): void
    {
        $factory = $event->getFactory();
        $tree = $event->getTree();

        if ('mainMenu' !== $tree->getName()) {
            return;
        }

        $item = $factory->createItem('my_item')
            ->setLabel('My menu item')
            ->setUri('/contao?do=my_module');

        $tree->addChild($item);
    }
}
```

---

### contao.generate_symlinks

Dispatched after Contao's symlink generation. Allows registration of your own symlinks.

**Event class:** `\Contao\CoreBundle\Event\GenerateSymlinksEvent`

---

### contao.image_sizes_all

Dispatched while collecting available image sizes for the back end selection. Allows your own definitions.

**Event-Klasse:** `\Contao\CoreBundle\Event\ImageSizesEvent`

```php
use Contao\CoreBundle\Event\ImageSizesEvent;
use Symfony\Component\EventDispatcher\Attribute\AsEventListener;

#[AsEventListener('contao.image_sizes_all')]
class ImageSizesListener
{
    public function __invoke(ImageSizesEvent $event): void
    {
        $sizes = $event->getImageSizes();
        $sizes['My Group'][] = '_my_custom_size';
        $event->setImageSizes($sizes);
    }
}
```

---

### contao.image_sizes_user

Like `contao.image_sizes_all`, but filtered by the permissions of the current back end user.

**Event-Klasse:** `\Contao\CoreBundle\Event\ImageSizesEvent`

---

### contao.preview_url_create

Dispatched when generating preview URLs for front end access from the back end.

**Event class:** `\Contao\CoreBundle\Event\PreviewUrlCreateEvent`

---

### contao.preview_url_convert

Converts preview controller requests into specific front end URLs in preview mode.

**Event class:** `\Contao\CoreBundle\Event\PreviewUrlConvertEvent`

---

### contao.robots_txt

Activated when `/robots.txt` is accessed. Allows programmatic addition of your own entries.

**Event class:** `\Contao\CoreBundle\Event\RobotsTxtEvent`

```php
use Contao\CoreBundle\Event\RobotsTxtEvent;
use Symfony\Component\EventDispatcher\Attribute\AsEventListener;

#[AsEventListener]
class RobotsTxtListener
{
    public function __invoke(RobotsTxtEvent $event): void
    {
        $event->getFileObject()->addSitemap('https://example.com/sitemap.xml');
    }
}
```

---

### contao.slug_valid_characters

Dispatched when generating valid slug character options in the back end.

**Event class:** `\Contao\CoreBundle\Event\SlugValidCharactersEvent`

---

### FilterPageTypeEvent

Dispatched when the available page types for the `tl_page` type select are collected.

**Event class:** `\Contao\CoreBundle\Event\FilterPageTypeEvent`

---

### contao.sitemap

Dispatched in the `SitemapController` while the sitemap is being constructed.

**Event class:** `\Contao\CoreBundle\Event\SitemapEvent`

```php
use Contao\CoreBundle\Event\SitemapEvent;
use Symfony\Component\EventDispatcher\Attribute\AsEventListener;

#[AsEventListener]
class SitemapListener
{
    public function __invoke(SitemapEvent $event): void
    {
        $xml = $event->getDocument();
        $urlSet = $xml->documentElement;
        
        $urlElement = $xml->createElement('url');
        $locElement = $xml->createElement('loc', 'https://example.com/custom-page');
        $urlElement->appendChild($locElement);
        $urlSet->appendChild($urlElement);
    }
}
```

---

### SendNewsletterEvent (Newsletter bundle)

Dispatched for every newsletter transmission. Allows content adjustment, prevention of sending, or logging.

**Event class:** `\Contao\NewsletterBundle\Event\SendNewsletterEvent`

---

### FetchArticlesForFeedEvent (News bundle)

Dispatched during news feed creation to collect articles.

**Event class:** `\Contao\NewsBundle\Event\FetchArticlesForFeedEvent`

---

### TransformArticleForFeedEvent (News bundle)

Dispatched when converting news articles into feed item nodes.

**Event class:** `\Contao\NewsBundle\Event\TransformArticleForFeedEvent`

---

### LayoutEvent (as of 5.7.1)

Dispatched during layout construction for modern Twig layouts with slots.

**Event class:** `\Contao\CoreBundle\Event\LayoutEvent`

---

## 3. Commands

Contao console: `php vendor/bin/contao-console <command>`

```bash
# List all available commands
php vendor/bin/contao-console list

# Show help for a command
php vendor/bin/contao-console contao:user:password --help
```

### Important Contao commands

| Command | Description |
|--------|--------------|
| `contao:migrate` | Run database migrations |
| `contao:user:create` | Create a back end user |
| `contao:user:password` | Change the password of a back end user |
| `contao:user:list` | List back end users |
| `contao:cache:warmup` | Warm up the cache |
| `contao:generate-symlinks` | Generate symlinks |
| `contao:crawl` | Crawl pages (for search/sitemap) |
| `contao:backup:create` | Create a database backup |
| `contao:backup:restore` | Restore a database backup |
| `contao:backup:list` | List available backups |
| `contao:install` | Run the Contao installation routine |
| `contao:version` | Show the installed Contao version |

---

## 4. Bundle Configuration (contao.yaml)

Full configuration overview via:
```bash
vendor/bin/contao-console config:dump-reference contao
```

### Core settings

```yaml
# config/packages/contao.yaml
contao:
    csrf_cookie_prefix: csrf_
    csrf_token_name: contao_csrf_token
    error_level: 6135               # E_ALL & ~E_NOTICE & ~E_DEPRECATED & ~E_USER_DEPRECATED
    pretty_error_screens: false
    preview_script: ''
    upload_path: files
    editable_files: 'css,csv,html,ini,js,json,less,md,scss,svg,svgz,ts,txt,xliff,xml,yml,yaml'
    console_path: '%kernel.project_dir%/bin/console'
    localconfig: ~                  # Override TL_CONFIG variables
```

### Internationalization

```yaml
contao:
    intl:
        locales: []                 # List of ICU locale IDs
        enabled_locales: []        # Back end locale IDs
        countries: []              # ISO 3166-1 alpha-2 codes
```

### Messenger configuration

```yaml
contao:
    messenger:
        web_worker:
            transports: []
            grace_period: PT10M
        workers:
            - transports: ['async']
              options: {}
              autoscale:
                  enabled: false
                  min: 1
                  max: 5           # required when autoscale is enabled
```

### Image processing

```yaml
contao:
    image:
        bypass_cache: false
        target_dir: '%kernel.project_dir%/assets/images'
        valid_extensions: [jpg, jpeg, gif, png, tif, tiff, bmp, svg, svgz, webp, avif]
        reject_large_uploads: false
        imagine_options:
            jpeg_quality: 80
            jpeg_sampling_factors: [2, 1, 1]
            webp_quality: ~
            webp_lossless: ~
            avif_quality: ~
            avif_lossless: ~
            interlace: plane
        preview:
            target_dir: '%kernel.project_dir%/assets/previews'
            default_size: 512
            max_size: 1024
            enable_fallback_images: true
```

### Image size definition

```yaml
contao:
    image:
        sizes:
            _my_size:
                width: 800
                height: 600
                resize_mode: crop         # crop | box | proportional
                zoom: 100
                css_class: my-image
                lazy_loading: true
                densities: '1x, 2x'
                sizes: '(max-width: 768px) 100vw, 800px'
                skip_if_dimensions_match: false
                formats:
                    jpg: [webp, jpg]      # Conversion specifications
                items:
                    -
                        width: 400
                        height: 300
                        media: '(max-width: 768px)'
```

### Security

```yaml
contao:
    security:
        two_factor:
            enforce_backend: false
        hsts:
            enabled: true
            ttl: 31536000
```

### Search

```yaml
contao:
    search:
        default_indexer:
            enable: true
        index_protected: false
        listener:
            index: true
            delete: true
        backend_search:
            enabled: false
            dsn: ~
            index_name: contao_backend
```

### Back end

```yaml
contao:
    backend:
        attributes: {}            # HTML body tag attributes
        custom_css: []
        custom_js: []
        badge_title: ''
        route_prefix: /contao
```

### Backup

```yaml
contao:
    backup:
        ignore_tables: [tl_crawl_queue, tl_log, tl_search, tl_search_index, tl_search_term]
        keep_max: 5
        keep_intervals: [1D, 7D, 14D, 1M]
```

### Content Security Policy

```yaml
contao:
    csp:
        allowed_inline_styles: {}
        max_header_size: 3072
```

---

## 5. Environment Variables

### APP_ENV
`prod` (default) or `dev`. Development mode enables additional logging.

### APP_SECRET
For CSRF token generation (~32 random characters).

### DATABASE_URL
```
DATABASE_URL="mysql://user:password@127.0.0.1:3306/dbname"
```

### MAILER_DSN
```
MAILER_DSN=smtp://username:password@smtp.example.com:587
```
(as of Contao 5.0; `MAILER_URL` is no longer supported)

### DISABLE_HTTP_CACHE
`true` disables the default caching proxy.

### COOKIE_ALLOW_LIST
Cookies that count as authentication-relevant (cache bypass).
```
PHPSESSID,csrf_https-contao_csrf_token,csrf_contao_csrf_token,trusted_device,REMEMBERME
```

### COOKIE_REMOVE_FROM_DENY_LIST
Remove entries from the default deny list:
```
COOKIE_REMOVE_FROM_DENY_LIST=__utm.+,AMP_TOKEN
```

### QUERY_PARAMS_ALLOW_LIST
Query parameters that are retained; all others are removed.

### QUERY_PARAMS_REMOVE_FROM_DENY_LIST
Remove parameters from the default deny list.

### TRUSTED_PROXIES
```
TRUSTED_PROXIES=192.0.2.1
TRUSTED_PROXIES=192.0.2.0/24
```

### DNS_MAPPING (as of 5.3)
Automatically redirect domains across environments:
```json
DNS_MAPPING='{"www.example.com": "example.local", "www.foobar.org": "foobar.local"}'
```

Via `parameters.yaml`:
```yaml
parameters:
    contao.dns_mapping:
        www.example.com: http://example.local
        www.foobar.org: http://foobar.local
```
Run `contao:migrate` after configuring this.

---

## 6. Request Attributes

Request attributes that can be set or queried in Contao controllers.

| Attribute | Type | Description |
|----------|-----|--------------|
| `_contao_referer_id` | `string` | Current referer ID for back end request URLs (back end scope only) |
| `_locale` | `string` | Locale of the current request; set by Contao in front end/back end scope |
| `_scope` | `string` | Contao request scope: `frontend` or `backend` |
| `_token_check` | `bool` | Enable/disable CSRF protection for POST requests; default: enabled for routes with Contao scope |
| `_store_referrer` | `bool` | Store the URL as referrer in the back end session history (no longer used as of 5.7) |
| `pageModel` | `\Contao\PageModel\|int` | PageModel instance or ID in Contao requests; do not use directly — use argument value resolving in page controllers or `$this->getPageModel()` in content elements/front end modules instead |

### Checking the scope in services

```php
use Contao\CoreBundle\Routing\ScopeMatcher;
use Symfony\Component\HttpFoundation\RequestStack;

class MyListener
{
    public function __construct(
        private readonly RequestStack $requestStack,
        private readonly ScopeMatcher $scopeMatcher,
    ) {}

    public function onRequest(): void
    {
        $request = $this->requestStack->getCurrentRequest();
        if (null === $request) {
            return;
        }

        $scope = $request->attributes->get('_scope');     // 'frontend' | 'backend' | null
        $isBackend = $this->scopeMatcher->isBackendRequest($request);
        $isFrontend = $this->scopeMatcher->isFrontendRequest($request);
    }
}
```

### Locale from the request

```php
$locale = $request->attributes->get('_locale');    // e.g. 'de', 'de_CH'
$locale = $request->getLocale();                    // Symfony default
```

---

*Sources:*
- https://docs.contao.org/5.x/dev/reference/services/
- https://docs.contao.org/5.x/dev/reference/events/
- https://docs.contao.org/5.x/dev/reference/commands/
- https://docs.contao.org/5.x/dev/reference/config/
- https://docs.contao.org/5.x/dev/reference/request-attributes/
