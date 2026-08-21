# Shopware 6 — Unit Test

Tests isolated logic (services, value objects, calculations) **without** kernel or DB — dependencies are mocked.
The fastest tier of the test pyramid.

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

No `IntegrationTestBehaviour`. Use static mocks for repositories/config (`sw-mock-repository`, `sw-mock-system-config`).
Prefer `assertSame` over `assertEquals` (strict equality, ADR). Test exceptions with `expectExceptionObject`.
For DAL/DB behaviour → `sw-integration-test`.
