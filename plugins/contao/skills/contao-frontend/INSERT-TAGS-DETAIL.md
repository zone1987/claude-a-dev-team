# Contao 5 — Insert Tags

## Contents

- [Overview](#overview)
- [Registration (as of Contao 5.2)](#registration-as-of-contao-52)
- [Simple insert tag](#simple-insert-tag)
- [Block insert tags](#block-insert-tags)
- [Insert tag flags](#insert-tag-flags)
- [Legacy implementation (before Contao 5.2)](#legacy-implementation-before-contao-52)
- [Formal syntax (EBNF)](#formal-syntax-ebnf)
- [Caching behavior](#caching-behavior)
- [Built-in insert tags (selection)](#built-in-insert-tags-selection)

## Overview

Insert tags are Contao's mechanism for replacing tokens in templates and database fields
with dynamic content. Format: `{{TAG_NAME}}` or
`{{TAG_NAME::PARAMETER}}`.

---

## Registration (as of Contao 5.2)

Since version 5.2, custom insert tags can be registered via PHP attributes or
service tags.

### Configuration options

| Option | Description |
|--------|-------------|
| `name` | Insert tag name (must be lower case) |
| `resolveNestedTags` | Resolve nested tags before processing |
| `priority` | Execution priority when names are identical |
| `method` | Method name (default: `__invoke`) |
| `asFragment` | Deprecated as of 5.3; renders via an ESI tag |
| `endTag` | End tag name for block insert tags |

---

## Simple insert tag

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

**Usage:** `{{rot13::Contao}}` → `Pbagnb`

---

## Block insert tags

Block insert tags wrap content. They receive the enclosed content
as a `ParsedSequence` object and return a modified sequence:

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

**Usage:**
```
{{ifmembergroup::1}}
    Only visible to members of group 1.
{{endifmembergroup}}
```

---

## Insert tag flags

Flags post-process the output of an insert tag:

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

**Usage:** `{{label::MSC:reset|rot13}}` → `Erfrg`

---

## Legacy implementation (before Contao 5.2)

For older versions, use the `replaceInsertTags` hook:

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
            return false; // not handled → try the next listener
        }

        return str_rot13($chunks[1]);
    }
}
```

---

## Formal syntax (EBNF)

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

## Caching behavior

Tags beginning with `cache_` or carrying the `uncached` flag bypass the
public cache:

```
{{rot13::Payload|uncached}}
```

---

## Built-in insert tags (selection)

| Tag | Description |
|-----|-------------|
| `{{link::*}}` | Link to Contao pages |
| `{{env::host}}` | Host name |
| `{{env::url}}` | Current URL |
| `{{date::*}}` | Formatted date |
| `{{asset::*::*}}` | Asset URL (file, package) |
| `{{request_token}}` | CSRF token |
| `{{user::*}}` | Attributes of the current user |

---

*Source: https://docs.contao.org/5.x/dev/framework/insert-tags/*
