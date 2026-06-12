# Contao 5 — Insert Tags

## Übersicht

Insert Tags sind Contaos Mechanismus, um Token in Templates und Datenbankfeldern
durch dynamische Inhalte zu ersetzen. Format: `{{TAG_NAME}}` oder
`{{TAG_NAME::PARAMETER}}`.

---

## Registrierung (ab Contao 5.2)

Seit Version 5.2 können eigene Insert Tags über PHP-Attribute oder Service-Tags
registriert werden.

### Konfigurationsoptionen

| Option | Beschreibung |
|--------|-------------|
| `name` | Insert-Tag-Name (muss Kleinschreibung sein) |
| `resolveNestedTags` | Verschachtelte Tags vor der Verarbeitung auflösen |
| `priority` | Ausführungspriorität bei gleichem Namen |
| `method` | Methoden-Name (Standard: `__invoke`) |
| `asFragment` | Veraltet ab 5.3; rendert via ESI-Tag |
| `endTag` | End-Tag-Name für Block-Insert-Tags |

---

## Einfacher Insert Tag

```php
// src/InsertTag/Rot13InsertTag.php
namespace App\InsertTag;

use Contao\CoreBundle\DependencyInjection\Attribute\AsInsertTag;
use Contao\CoreBundle\InsertTag\InsertTagResult;
use Contao\CoreBundle\InsertTag\OutputType;
use Contao\CoreBundle\InsertTag\ParsedInsertTag;
use Contao\CoreBundle\InsertTag\ResolvedInsertTag;
use Contao\CoreBundle\InsertTag\Resolver\InsertTagResolverNestedResolvedInterface;

#[AsInsertTag('rot13')]
class Rot13InsertTag implements InsertTagResolverNestedResolvedInterface
{
    public function __invoke(ResolvedInsertTag $insertTag): InsertTagResult
    {
        if (null === $insertTag->getParameters()->get(0)) {
            throw new \InvalidArgumentException('Missing parameters.');
        }

        return new InsertTagResult(
            str_rot13($insertTag->getParameters()->get(0)),
            OutputType::text
        );
    }
}
```

**Verwendung:** `{{rot13::Contao}}` → `Pbagnb`

---

## Block Insert Tags

Block-Insert-Tags umschließen Inhalt. Sie empfangen den eingeschlossenen Inhalt
als `ParsedSequence`-Objekt und geben eine modifizierte Sequenz zurück:

```php
// src/InsertTag/IfMemberGroupInsertTag.php
namespace App\InsertTag;

use Contao\CoreBundle\DependencyInjection\Attribute\AsBlockInsertTag;
use Contao\CoreBundle\InsertTag\InsertTagResult;
use Contao\CoreBundle\InsertTag\ParsedSequence;
use Contao\CoreBundle\InsertTag\ResolvedInsertTag;
use Contao\CoreBundle\InsertTag\Resolver\BlockInsertTagResolverNestedResolvedInterface;
use Symfony\Component\Security\Core\Authorization\AuthorizationCheckerInterface;

#[AsBlockInsertTag('ifmembergroup', endTag: 'endifmembergroup')]
class IfMemberGroupInsertTag implements BlockInsertTagResolverNestedResolvedInterface
{
    public function __construct(
        private readonly AuthorizationCheckerInterface $auth
    ) {}

    public function __invoke(ResolvedInsertTag $insertTag, ParsedSequence $wrappedContent): ParsedSequence
    {
        if (!$groups = $insertTag->getParameters()->all()) {
            throw new \InvalidArgumentException('Missing parameters.');
        }

        if ($this->auth->isGranted(ContaoCorePermissions::MEMBER_IN_GROUPS, $groups)) {
            return $wrappedContent;
        }

        return new ParsedSequence([]);
    }
}
```

**Verwendung:**
```
{{ifmembergroup::1}}
    Nur für Mitglieder der Gruppe 1 sichtbar.
{{endifmembergroup}}
```

---

## Insert-Tag-Flags

Flags verarbeiten die Ausgabe eines Insert Tags:

```php
// src/InsertTag/Rot13InsertTagFlag.php
namespace App\InsertTag;

use Contao\CoreBundle\DependencyInjection\Attribute\AsInsertTagFlag;
use Contao\CoreBundle\InsertTag\Flag\InsertTagFlagInterface;
use Contao\CoreBundle\InsertTag\InsertTagFlag;
use Contao\CoreBundle\InsertTag\InsertTagResult;
use Contao\CoreBundle\InsertTag\OutputType;

#[AsInsertTagFlag('rot13')]
class Rot13InsertTagFlag implements InsertTagFlagInterface
{
    public function __invoke(InsertTagFlag $flag, InsertTagResult $result): InsertTagResult
    {
        return $result
            ->withValue(str_rot13($result->getValue()))
            ->withOutputType(OutputType::text);
    }
}
```

**Verwendung:** `{{label::MSC:reset|rot13}}` → `Erfrg`

---

## Legacy-Implementierung (vor Contao 5.2)

Für ältere Versionen den `replaceInsertTags`-Hook nutzen:

```php
use Contao\CoreBundle\DependencyInjection\Attribute\AsHook;

#[AsHook('replaceInsertTags')]
class Rot13InsertTagListener
{
    public const TAG = 'rot13';

    public function __invoke(string $tag): string|false
    {
        $chunks = explode('::', $tag);

        if (self::TAG !== $chunks[0]) {
            return false; // nicht behandelt → nächsten Listener probieren
        }

        return str_rot13($chunks[1]);
    }
}
```

---

## Formale Syntax (EBNF)

```
InsertTag  ::= "{{" Name Parameter* Flag* "}}"
Name       ::= [a-z#x80-#xFF][a-z0-9_#x80-#xFF]*
Parameter  ::= "::" ( KeyValuePair | Value )
Flag       ::= "|" [^{}|]*
KeyValuePair ::= Key "=" Value
Key        ::= [^{}|=]*
Value      ::= ( [^{}|] | InsertTag )*
```

---

## Caching-Verhalten

Tags, die mit `cache_` beginnen oder das `uncached`-Flag haben, umgehen den
öffentlichen Cache:

```
{{rot13::Payload|uncached}}
```

---

## Eingebaute Insert Tags (Auswahl)

| Tag | Beschreibung |
|-----|-------------|
| `{{link::*}}` | Link zu Contao-Seiten |
| `{{env::host}}` | Hostname |
| `{{env::url}}` | Aktuelle URL |
| `{{date::*}}` | Datum formatiert |
| `{{asset::*::*}}` | Asset-URL (Datei, Paket) |
| `{{request_token}}` | CSRF-Token |
| `{{user::*}}` | Aktueller Benutzer-Attribute |

---

*Quelle: https://docs.contao.org/5.x/dev/framework/insert-tags/*
