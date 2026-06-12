# Contao Hooks – Templates

Hooks für Backend- und Frontend-Template-Parsing und Widget-Ausgabe.

---

## `outputBackendTemplate`

**Zweck:** Wird ausgelöst, wenn ein Backend-Template auf dem Bildschirm ausgegeben wird. Ermöglicht Modifikation des gerenderten Template-Inhalts.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$buffer` | Gerenderter Backend-Template-Inhalt |
| 2 | `string` | `$template` | Template-Name ohne Extension (z.B. `be_main`) |

**Rückgabe:** `string` – Originaler oder modifizierter `$buffer`.

**Zeitpunkt:** Nach dem Rendern, vor der Ausgabe an den Browser.

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;

#[AsHook('outputBackendTemplate')]
class OutputBackendTemplateListener
{
    public function __invoke(string $buffer, string $template): string
    {
        if ('be_main' === $template) {
            $buffer = str_replace('</head>', '<style>.custom{color:red}</style></head>', $buffer);
        }
        return $buffer;
    }
}
```

---

## `parseBackendTemplate`

**Zweck:** Wird ausgelöst, wenn ein Backend-Template geparsed wird. Ähnlich wie `outputBackendTemplate`, feuert aber beim Parsen (früher im Prozess).

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$buffer` | Geparster Backend-Template-Inhalt |
| 2 | `string` | `$template` | Template-Name ohne Extension (z.B. `be_widget`) |

**Rückgabe:** `string` – Originaler oder modifizierter `$buffer`.

**Zeitpunkt:** Beim Parsen von Backend-Templates im Admin-Interface.

```php
#[AsHook('parseBackendTemplate')]
class ParseBackendTemplateListener
{
    public function __invoke(string $buffer, string $template): string
    {
        if ('be_main' === $template) {
            // Custom-Inhalte einfügen
        }
        return $buffer;
    }
}
```

---

## `parseFrontendTemplate`

**Zweck:** Wird ausgelöst, wenn ein Frontend-Template geparsed wird.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$buffer` | Geparster Frontend-Template-Inhalt |
| 2 | `string` | `$templateName` | Template-Name ohne Extension (z.B. `nav_default`) |
| 3 | `\Contao\FrontendTemplate` | `$template` | Die Template-Instanz |

**Rückgabe:** `string` – Originaler oder modifizierter `$buffer`.

**Zeitpunkt:** Nach dem Parsen eines Frontend-Templates, vor der Ausgabe.

```php
#[AsHook('parseFrontendTemplate')]
class ParseFrontendTemplateListener
{
    public function __invoke(string $buffer, string $templateName, FrontendTemplate $template): string
    {
        if ('ce_text' === $templateName) {
            // Inhalt eines Textelements modifizieren
        }
        return $buffer;
    }
}
```

---

## `parseTemplate`

**Zweck:** Wird **vor** dem Parsen eines Templates ausgelöst. Übergibt das Template-Objekt – ideal für das Hinzufügen eigener Template-Variablen.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `\Contao\Template` | `$template` | Frontend- oder Backend-Template-Instanz |

**Rückgabe:** `void`

**Zeitpunkt:** Vor dem Parsen des Templates. Template-Variablen können hier gesetzt werden.

```php
#[AsHook('parseTemplate')]
class ParseTemplateListener
{
    public function __invoke(Template $template): void
    {
        if ('fe_page' === $template->getName() || str_starts_with($template->getName(), 'fe_page_')) {
            $template->customVar = 'meinWert';
        }
    }
}
```

**Tipp:** Mit Closures können auch Hilfsfunktionen injiziert werden:

```php
$template->isMemberOf = fn(int $groupId): bool =>
    $this->authorizationChecker->isGranted(
        ContaoCorePermissions::MEMBER_IN_GROUPS,
        $groupId
    );
```

---

## `parseWidget`

**Zweck:** Erlaubt die Anpassung der Ausgabe eines `\Contao\Widget` beim Parsen.

**Parameter:**

| # | Typ | Name | Beschreibung |
|---|-----|------|-------------|
| 1 | `string` | `$buffer` | Ausgabe-Puffer des Widgets |
| 2 | `\Contao\Widget` | `$widget` | Die Widget-Instanz |

**Rückgabe:** `string` – Modifizierter Ausgabe-Puffer.

**Zeitpunkt:** Beim Parsen eines Widgets, bevor das HTML gerendert wird.

```php
use Contao\Widget;

#[AsHook('parseWidget')]
class ParseWidgetListener
{
    public function __invoke(string $buffer, Widget $widget): string
    {
        if ('myFieldName' === $widget->name) {
            $buffer = '<div class="custom-wrapper">' . $buffer . '</div>';
        }
        return $buffer;
    }
}
```

---

_Quelle: https://docs.contao.org/5.x/dev/reference/hooks/ (Stand 2025-06)_
