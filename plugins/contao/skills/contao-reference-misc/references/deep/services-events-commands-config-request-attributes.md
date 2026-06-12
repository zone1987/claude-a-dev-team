# Contao 5.x — Services, Events, Commands, Config, Request-Attributes

---

## 1. Core Services

### ContaoFramework

Initialisiert das Legacy-Contao-Framework und stellt Adapter für statische Klassen bereit.

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

Generiert und validiert Request-Tokens für eigene Formulare (notwendig für POST-Requests auf Contao-Routen).

**Service-ID:** `@contao.csrf.token_manager`  
**Token-Name:** aus `contao.csrf_token_name` (Standard: `contao_csrf_token`)

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
        // In Formular einbetten: <input type="hidden" name="REQUEST_TOKEN" value="{{ token }}">
    }
}
```

---

### Database Connection

Zugriff auf konfigurierte Datenbankverbindungen via Doctrine DBAL.

**Service:** `database_connection`  
**Typ:** `Doctrine\DBAL\Connection`

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

Ermöglicht Cache-Tagging und -Invalidierung basierend auf Entity-/Model-Klassen nach der Namenskonvention `contao.db.tl_content.5`.

```php
use Contao\CoreBundle\Cache\EntityCacheTags;

class MyController
{
    public function __construct(private readonly EntityCacheTags $cacheTags) {}

    public function show(int $id): Response
    {
        $response = new Response(…);
        $this->cacheTags->tagWith('tl_example');
        // oder: $this->cacheTags->tagWith($model);
        return $response;
    }
}
```

---

### OptIn

Zentrales Opt-In-Tracking mit automatischer Bereinigung nach der gesetzlich erforderlichen Dauer.

**Präfix-Beschränkung:** 6 Zeichen vor dem Bindestrich.

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

Symfony-Routing-Service für URL-Generierung zu Routen innerhalb von Services.

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

Erkennt ob ein Request zum Contao Backend oder Frontend gehört.

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
            // Backend-Logik
        }
        
        if ($this->scopeMatcher->isFrontendRequest($request)) {
            // Frontend-Logik
        }
    }
}
```

---

### Security Helper

Ruft aktuellen Backend- oder Frontend-Benutzer ab und prüft Autorisierungs-Rollen.

```php
use Symfony\Bundle\SecurityBundle\Security;

class MyService
{
    public function __construct(private readonly Security $security) {}

    public function checkAccess(): void
    {
        $user = $this->security->getUser(); // BackendUser | FrontendUser | null

        if ($this->security->isGranted('ROLE_ADMIN')) {
            // Admin-Logik
        }

        if ($this->security->isGranted('ROLE_USER')) {
            // Backend-Benutzer
        }

        if ($this->security->isGranted('ROLE_MEMBER')) {
            // Frontend-Mitglied
        }
    }
}
```

---

### SimpleTokenParser

Parst einfache Tokens mit Ersetzung und bedingten Ausdrücken, erweiterbar über `contao.simple_token_extension`-Tags.

```php
use Contao\CoreBundle\String\SimpleTokenParser;

class MyService
{
    public function __construct(private readonly SimpleTokenParser $parser) {}

    public function parse(string $text, array $tokens): string
    {
        return $this->parser->parse($text, $tokens);
        // Beispiel: $text = 'Hallo ##firstname##!'
        // $tokens = ['firstname' => 'Max']
        // Ergebnis: 'Hallo Max!'
    }
}
```

---

### Slug

Generiert menschenlesbare eindeutige Identifikatoren aus Strings.

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

Fragt Contao-Sicherheitstoken-Informationen ab.

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

Ersetzt Insert-Tags in Strings.

```php
use Contao\CoreBundle\InsertTag\InsertTagParser;

class MyService
{
    public function __construct(private readonly InsertTagParser $parser) {}

    public function process(string $text): string
    {
        // Für Text-Kontext (HTML-sicher)
        $plain = $this->parser->replace($text);

        // Für inline-Text (kein vollständiges HTML)
        $inline = $this->parser->replaceInline($text);

        // Chunked für selektives Escaping
        $chunked = $this->parser->replaceChunked($text); // ChunkedText
        
        return $plain;
    }
}
```

---

### RequestStack

Zugriff auf den aktuellen HTTP-Request aus dem Service-Container.

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

Zugriff auf oder Setzen des Response-Kontexts für Contao-Requests.

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
        // z. B. für CSP-Tags, JSON-LD, etc.
        return '';
    }
}
```

---

### Locales

Locale-/Sprachinformationen mit Übersetzungen.

```php
use Contao\CoreBundle\Intl\Locales;

class LocaleService
{
    public function __construct(private readonly Locales $locales) {}

    public function getAll(): array
    {
        // Alle konfigurierten Locales ['de' => 'Deutsch', 'en' => 'English', …]
        return $this->locales->getLocales();
    }

    public function getEnabled(): array
    {
        // Backend-aktivierte Locales
        return $this->locales->getEnabledLocales();
    }
}
```

Konfiguration: `contao.intl.locales`, `contao.intl.enabled_locales`

---

### Countries

Ländercodes und übersetzte Ländernamen.

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

Konfiguration: `contao.intl.countries`

---

### Mailer

Symfony-Mailer-Service für E-Mail-Versand.

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

### PageFinder (ab 5.3)

Findet Seiten aus der Seitenstruktur nach Hostname oder Request.

```php
use Contao\CoreBundle\Routing\PageFinder;

class MyService
{
    public function __construct(private readonly PageFinder $pageFinder) {}

    public function findRoot(string $host): ?\Contao\PageModel
    {
        return $this->pageFinder->findRootPageForHostAndLanguage($host, 'de');
    }

    // Ab 5.4:
    public function getCurrent(): ?\Contao\PageModel
    {
        return $this->pageFinder->getCurrentPage();
    }
}
```

---

### ContentUrlGenerator (ab 5.3)

Generiert URLs für Content-Objekte wie Seiten und News-Einträge.

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

Contao implementiert Events über den Symfony Event Dispatcher.

### contao.backend_menu_build

Wird beim Aufbau des Backend-Menüs ausgeführt. Ermöglicht die Änderung der Menüstruktur.

**Event-Klasse:** `\Contao\CoreBundle\Event\MenuEvent`

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
            ->setLabel('Mein Menüpunkt')
            ->setUri('/contao?do=my_module');

        $tree->addChild($item);
    }
}
```

---

### contao.generate_symlinks

Ausgelöst nach Contaos Symlink-Generierung. Erlaubt Registrierung eigener Symlinks.

**Event-Klasse:** `\Contao\CoreBundle\Event\GenerateSymlinksEvent`

---

### contao.image_sizes_all

Ausgelöst beim Sammeln verfügbarer Bildgrößen für Backend-Auswahl. Erlaubt eigene Definitionen.

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

Wie `contao.image_sizes_all`, aber gefiltert nach Berechtigungen des aktuellen Backend-Benutzers.

**Event-Klasse:** `\Contao\CoreBundle\Event\ImageSizesEvent`

---

### contao.preview_url_create

Ausgelöst beim Generieren von Vorschau-URLs für Frontend-Zugriff im Backend.

**Event-Klasse:** `\Contao\CoreBundle\Event\PreviewUrlCreateEvent`

---

### contao.preview_url_convert

Konvertiert Preview-Controller-Anfragen zu spezifischen Frontend-URLs im Vorschau-Modus.

**Event-Klasse:** `\Contao\CoreBundle\Event\PreviewUrlConvertEvent`

---

### contao.robots_txt

Aktiviert bei Zugriff auf `/robots.txt`. Erlaubt programmatisches Hinzufügen eigener Einträge.

**Event-Klasse:** `\Contao\CoreBundle\Event\RobotsTxtEvent`

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

Ausgelöst beim Generieren gültiger Slug-Zeichen-Optionen im Backend.

**Event-Klasse:** `\Contao\CoreBundle\Event\SlugValidCharactersEvent`

---

### FilterPageTypeEvent

Wird ausgelöst wenn verfügbare Seitentypen für den `tl_page`-Typ-Select gesammelt werden.

**Event-Klasse:** `\Contao\CoreBundle\Event\FilterPageTypeEvent`

---

### contao.sitemap

Ausgelöst im `SitemapController` während der Sitemap-Konstruktion.

**Event-Klasse:** `\Contao\CoreBundle\Event\SitemapEvent`

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

### SendNewsletterEvent (Newsletter-Bundle)

Ausgelöst für jede Newsletter-Übertragung. Erlaubt Inhalts-Anpassung, Verhinderung des Versands oder Logging.

**Event-Klasse:** `\Contao\NewsletterBundle\Event\SendNewsletterEvent`

---

### FetchArticlesForFeedEvent (News-Bundle)

Ausgelöst bei News-Feed-Erstellung zum Sammeln von Artikeln.

**Event-Klasse:** `\Contao\NewsBundle\Event\FetchArticlesForFeedEvent`

---

### TransformArticleForFeedEvent (News-Bundle)

Ausgelöst beim Konvertieren von News-Artikeln zu Feed-Item-Knoten.

**Event-Klasse:** `\Contao\NewsBundle\Event\TransformArticleForFeedEvent`

---

### LayoutEvent (ab 5.7.1)

Ausgelöst beim Layout-Aufbau für moderne Twig-Layouts mit Slots.

**Event-Klasse:** `\Contao\CoreBundle\Event\LayoutEvent`

---

## 3. Commands

Contao-Konsole: `php vendor/bin/contao-console <befehl>`

```bash
# Alle verfügbaren Befehle auflisten
php vendor/bin/contao-console list

# Hilfe zu einem Befehl anzeigen
php vendor/bin/contao-console contao:user:password --help
```

### Wichtige Contao-Befehle

| Befehl | Beschreibung |
|--------|--------------|
| `contao:migrate` | Datenbankmigrationen ausführen |
| `contao:user:create` | Backend-Benutzer anlegen |
| `contao:user:password` | Passwort eines Backend-Benutzers ändern |
| `contao:user:list` | Backend-Benutzer auflisten |
| `contao:cache:warmup` | Cache aufwärmen |
| `contao:generate-symlinks` | Symlinks generieren |
| `contao:crawl` | Seiten crawlen (für Suche/Sitemap) |
| `contao:backup:create` | Datenbank-Backup erstellen |
| `contao:backup:restore` | Datenbank-Backup wiederherstellen |
| `contao:backup:list` | Verfügbare Backups auflisten |
| `contao:install` | Contao-Installationsroutine ausführen |
| `contao:version` | Installierte Contao-Version anzeigen |

---

## 4. Bundle-Konfiguration (contao.yaml)

Vollständige Konfigurationsübersicht via:
```bash
vendor/bin/contao-console config:dump-reference contao
```

### Kern-Einstellungen

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
    localconfig: ~                  # TL_CONFIG-Variablen überschreiben
```

### Internationalisierung

```yaml
contao:
    intl:
        locales: []                 # ICU Locale-IDs Liste
        enabled_locales: []        # Backend-Locale-IDs
        countries: []              # ISO 3166-1 alpha-2 Codes
```

### Messenger-Konfiguration

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
                  max: 5           # required wenn autoscale aktiviert
```

### Bildverarbeitung

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

### Bildgrößen-Definition

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
                    jpg: [webp, jpg]      # Konvertierungsspezifikationen
                items:
                    -
                        width: 400
                        height: 300
                        media: '(max-width: 768px)'
```

### Sicherheit

```yaml
contao:
    security:
        two_factor:
            enforce_backend: false
        hsts:
            enabled: true
            ttl: 31536000
```

### Suche

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

### Backend

```yaml
contao:
    backend:
        attributes: {}            # HTML body-Tag-Attribute
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

## 5. Umgebungsvariablen

### APP_ENV
`prod` (Standard) oder `dev`. Entwicklungsmodus aktiviert zusätzliches Logging.

### APP_SECRET
Für CSRF-Token-Generierung (~32 zufällige Zeichen).

### DATABASE_URL
```
DATABASE_URL="mysql://user:password@127.0.0.1:3306/dbname"
```

### MAILER_DSN
```
MAILER_DSN=smtp://username:password@smtp.example.com:587
```
(ab Contao 5.0; `MAILER_URL` nicht mehr unterstützt)

### DISABLE_HTTP_CACHE
`true` deaktiviert Standard-Caching-Proxy.

### COOKIE_ALLOW_LIST
Cookies die als authentifizierungsrelevant gelten (Cache-Bypass).
```
PHPSESSID,csrf_https-contao_csrf_token,csrf_contao_csrf_token,trusted_device,REMEMBERME
```

### COOKIE_REMOVE_FROM_DENY_LIST
Einträge aus Standard-Deny-Liste entfernen:
```
COOKIE_REMOVE_FROM_DENY_LIST=__utm.+,AMP_TOKEN
```

### QUERY_PARAMS_ALLOW_LIST
Query-Parameter die erhalten bleiben; alle anderen werden entfernt.

### QUERY_PARAMS_REMOVE_FROM_DENY_LIST
Parameter aus Standard-Deny-Liste entfernen.

### TRUSTED_PROXIES
```
TRUSTED_PROXIES=192.0.2.1
TRUSTED_PROXIES=192.0.2.0/24
```

### DNS_MAPPING (ab 5.3)
Domänen automatisch über Umgebungen hinweg umleiten:
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
Nach Konfiguration `contao:migrate` ausführen.

---

## 6. Request-Attributes

Request-Attribute die in Contao-Controllern gesetzt oder abgefragt werden können.

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `_contao_referer_id` | `string` | Aktueller Referer-ID für Backend-Request-URLs (nur Backend-Scope) |
| `_locale` | `string` | Locale des aktuellen Requests; gesetzt durch Contao im Frontend/Backend-Scope |
| `_scope` | `string` | Contao-Request-Scope: `frontend` oder `backend` |
| `_token_check` | `bool` | CSRF-Schutz für POST-Requests aktivieren/deaktivieren; Standard: aktiviert für Routen mit Contao-Scope |
| `_store_referrer` | `bool` | URL in Backend-Session-History als Referrer speichern (ab 5.7 nicht mehr verwendet) |
| `pageModel` | `\Contao\PageModel\|int` | PageModel-Instanz oder ID in Contao-Requests; nicht direkt verwenden — stattdessen Argument-Value-Resolving in Page-Controllern oder `$this->getPageModel()` in Inhaltselementen/Frontend-Modulen nutzen |

### Scope in Services prüfen

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

### Locale aus Request

```php
$locale = $request->attributes->get('_locale');    // z. B. 'de', 'de_CH'
$locale = $request->getLocale();                    // Symfony-Standard
```

---

*Quellen:*
- https://docs.contao.org/5.x/dev/reference/services/
- https://docs.contao.org/5.x/dev/reference/events/
- https://docs.contao.org/5.x/dev/reference/commands/
- https://docs.contao.org/5.x/dev/reference/config/
- https://docs.contao.org/5.x/dev/reference/request-attributes/
