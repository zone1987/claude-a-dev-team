---
name: panther-testcase
description: >
  PantherTestCase und PantherTestCaseTrait: createPantherClient/createAdditionalPantherClient/
  createHttpBrowserClient mit allen Optionen, Integration mit WebTestCase, vollstandige Liste
  aller 22 assertSelector*/assertPageTitle*-Assertions (sofort + waitFor-Varianten).
  PantherTestCase trait, client factory methods, all assertion methods, options arrays.
  Trigger: "panthertest case", "panther test class", "createpantherclient optionen",
  "createpantherclient options", "panther assertions", "assertselectortext", "assertpagetitle",
  "assertselectorisvisible", "assertselectorwillexist", "panther trait", "panther webtest",
  "panther phpunit", "assertselectorattribute", "panther assert", "panther additional client".
---

# PantherTestCase — TestCase & Assertions

```php
use Symfony\Component\Panther\PantherTestCase;

class MyTest extends PantherTestCase
{
    public function testFeature(): void
    {
        $client = static::createPantherClient(['browser' => static::FIREFOX]);
        $client->request('GET', '/');
        $this->assertSelectorWillExist('.dynamic-content');
        $this->assertSelectorTextContains('h1', 'Hallo');
    }
}
```

## createPantherClient — Optionen

```php
static::createPantherClient(
    array $options = [],         // webServerDir, hostname, port, router, external_base_uri,
                                 // readinessPath, env, browser (chrome|firefox|selenium)
    array $kernelOptions = [],   // Symfony-Kernel-Optionen
    array $managerOptions = []   // capabilities, chromedriver_arguments, host (Selenium), ...
): PantherClient
```

## Alle Assertions (22)

Direkte (sofort): `assertPageTitleSame`, `assertPageTitleContains`, `assertSelectorExists`,
`assertSelectorNotExists`, `assertSelectorTextContains`, `assertSelectorTextNotContains`,
`assertSelectorIsVisible`, `assertSelectorIsNotVisible`, `assertSelectorIsEnabled`,
`assertSelectorIsDisabled`, `assertSelectorAttributeContains`, `assertSelectorAttributeNotContains`

waitFor-Varianten: `assertSelectorWillExist`, `assertSelectorWillNotExist`,
`assertSelectorWillContain`, `assertSelectorWillNotContain`, `assertSelectorWillBeVisible`,
`assertSelectorWillNotBeVisible`, `assertSelectorWillBeEnabled`, `assertSelectorWillBeDisabled`,
`assertSelectorAttributeWillContain`, `assertSelectorAttributeWillNotContain`

## Vertiefung

- [references/deep/testcase.md](references/deep/testcase.md) — Vollstandige Methoden-Signaturen, alle Options-Schlussel, Trait-Nutzung, Real-Time-Tests, Multi-Domain
