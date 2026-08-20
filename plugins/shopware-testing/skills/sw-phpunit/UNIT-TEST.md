# Shopware 6 — Unit-Test

Testet isolierte Logik (Services, Value-Objects, Berechnungen) **ohne** Kernel/DB — Abhängigkeiten werden gemockt.
Schnellste Stufe der Test-Pyramide.

```php
final class PriceCalculatorTest extends TestCase
{
    public function testRounds(): void
    {
        $sut = new FfPriceCalculator();
        static::assertSame(19.99, $sut->normalize(19.994));
    }
}
```

Kein `IntegrationTestBehaviour`. Repositories/Config über statische Mocks (`sw-mock-repository`, `sw-mock-system-config`).
`assertSame` statt `assertEquals` (strikte Gleichheit, ADR). Exceptions über `expectExceptionObject` testen.
Für DAL/DB-Verhalten → `sw-integration-test`.
