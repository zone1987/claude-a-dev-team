# Finding out why a test fails

A failing test is information. The cost is in guessing instead of reading — and every
expensive detour in this workspace has had the same shape: an assumption about an API that
thirty seconds of source-reading would have settled.

## First, name which of the three it is

A failing test has exactly one of three causes. **Naming it before touching anything** is
the single highest-value habit here:

| Cause | What it looks like | What to do |
|---|---|---|
| **The code is wrong** | the test states a rule the code breaks | fix the code |
| **The expectation is wrong** | the test asserts something the domain does not promise | fix the test — **after** proving it, by reading the source |
| **The setup is wrong** | the test never reaches the thing it means to test | fix the setup |

**Case 2 is where damage happens.** A passing test "corrected" into a failing one because a
constructor's argument order was assumed rather than read costs more than the original bug,
and it can end with production code changed to match a wrong belief.

The guard is mechanical: **before flipping an assertion, open the class.**

```bash
grep -n "public function __construct" -A 10 \
  /path/to/shopware/src/Core/Framework/DataAbstractionLayer/Pricing/Price.php
```

A real example. `Price` takes **net before gross**:

```php
public function __construct(
    protected string $currencyId,
    protected float $net,      // ← second
    protected float $gross,    // ← third
    protected bool $linked,
)
```

Assuming the opposite produced a failing test, a "correction" that made it fail
differently, and three rounds of confusion. The grep above ends it.

## A throwaway console command beats every other tool

When a unit test passes and the shop behaves differently, the gap is between the test's
fixture and reality. A temporary Symfony command runs inside the real container, with the
real services, against the real database:

```php
<?php declare(strict_types=1);

namespace YourPlugin\Command;

use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

final class DebugCommand extends Command
{
    public function __construct(
        private readonly AbstractSalesChannelContextFactory $factory,
        private readonly YourService $service,
    ) {
        parent::__construct('yourplugin:debug');
    }

    protected function configure(): void
    {
        $this->addArgument('salesChannelId', InputArgument::REQUIRED);
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $context = $this->factory->create('dbg' . uniqid(), $input->getArgument('salesChannelId'));

        // Print every input the service sees, not just the answer. The answer you can
        // already infer; the inputs are what you are wrong about.
        $output->writeln('currency: ' . $context->getCurrencyId());
        $output->writeln('tax state: ' . $context->getTaxState());
        $output->writeln('prices: ' . $context->getShippingMethod()->getPrices()->count());

        return Command::SUCCESS;
    }
}
```

**This is what found the defect that a day of guessing had not**: the shipping method on
the `SalesChannelContext` arrives with an *empty* price collection, while the one on the
cart's delivery carries it fully loaded. `prices: 0` in the output settled it in seconds.

Wire it in `services.xml` with a `console.command` tag, run it, **then delete it**. It is a
probe, not a feature — and the code that replaces it is a test.

```bash
ddev exec bin/console yourplugin:debug <sales-channel-id>
```

If the output does not change after an edit, the container cached the old definition:

```bash
ddev exec bin/console cache:clear
```

## Print the inputs, not the conclusion

A probe that prints `Schwelle: NULL` tells you the answer is wrong. A probe that prints
every condition tells you *which* one failed:

```php
foreach ($prices as $price) {
    $output->writeln(sprintf(
        '  calc=%s end=%s start=%s currencies=[%s] gross=%s',
        var_export($price->getCalculation(), true),
        var_export($price->getQuantityEnd(), true),
        var_export($price->getQuantityStart(), true),
        $currencyPrice === null ? '-' : implode(',', $currencyPrice->getKeys()),
        $resolved === null ? 'NULL' : var_export($resolved->getGross(), true),
    ));
}
```

The line `currencies=[b7d2554b…] ` against a context currency of `019a74a9…` is what
revealed that the resolver needed the core's currency **fallback**, not an exact match.

## Uncovered lines: clover.xml, not the HTML report

The text summary says *how much*. `clover.xml` says *where*:

```bash
python3 -c "
import xml.etree.ElementTree as ET, pathlib
t = ET.parse('var/coverage/unit/clover.xml')
for f in t.iter('file'):
    src = pathlib.Path(f.get('name')).read_text().splitlines()
    for l in f.iter('line'):
        if l.get('count') == '0':
            n = int(l.get('num')); print(f'{f.get(\"name\")}:{n}: {src[n-1].strip()}')
"
```

**Then ask why no test went there.** In this workspace the answer was once "because every
fixture builds a cart without a delivery, and the delivery branch is the one real shops
take" — the uncovered line was the normal path, and the gap was in the fixtures.

## Surviving mutants: compute the value, do not guess it

A rounding mutant survives because the test used a value where `round`, `floor` and `ceil`
agree. Find one where they do not:

```php
foreach ([1.15, 4.35, 0.07, 0.10, 3.33] as $v) {
    $x = $v * 100;
    printf("%.2f -> %.20f round=%d floor=%d ceil=%d\n",
        $v, $x, (int)round($x), (int)floor($x), (int)ceil($x));
}
```

```
3.33 -> 333.00000000000000000000 round=333 floor=333 ceil=333   ← useless as a test value
1.15 -> 114.99999999999998578915 round=115 floor=114 ceil=115   ← kills the floor mutant
0.07 ->   7.00000000000000088818 round=7   floor=7   ceil=8     ← kills the ceil mutant
```

`3.33 × 3` is exactly `9.99` in floating point, which is why a test built on it proves
nothing about rounding.

## Browser tests: read the artifacts, then reduce

Playwright writes three things on failure, and the second is the one people skip:

| Artifact | What it answers |
|---|---|
| `test-failed-1.png` | what the page looked like |
| `error-context.md` | **the accessibility tree** — every element, by role and name |
| `trace.zip` | every step, request and DOM snapshot |

The `error-context.md` snapshot settled a whole afternoon: it showed
`link "Shopping cart contains one item"` — proving the click *had* worked and the cart
*was* filled, so the problem was the off-canvas not opening, not the add-to-cart failing.

**Then reduce to a probe spec.** A throwaway spec that prints instead of asserting narrows
faster than a debugger:

```typescript
test('probe: what does the page actually have', async ({ StorefrontPage, ShopCustomer }) => {
    await ShopCustomer.goesTo('checkout/cart');

    console.log('URL:', StorefrontPage.url());
    console.log('line items:', await StorefrontPage.locator('.line-item-label').count());
    console.log('our container:', await StorefrontPage.locator('.up-to-free-shipping').count());
    console.log('router keys:', await StorefrontPage.evaluate(() => Object.keys(window.router ?? {})));

    expect(true).toBe(true);
});
```

Delete it when it has answered. Name it `_probe.spec.ts` so a leftover is obvious.

## Server-side first, browser second

Before blaming the browser, ask the server. `curl` with a cookie jar cuts out JavaScript,
rendering and timing at once:

```bash
cat > shopware/public/_probe.sh <<'SH'
#!/bin/sh
J=/tmp/c.txt; rm -f $J
B=https://your-shop.ddev.site/<sales-channel-path>
curl -sk -c $J -b $J "$B/" -o /dev/null
curl -sk -c $J -b $J "$B/checkout/offcanvas" > /tmp/oc.html
grep -oE 'up-to-free-shipping[a-z-]*' /tmp/oc.html | sort | uniq -c
SH
ddev exec -s playwright sh /var/www/html/shopware/public/_probe.sh
rm -f shopware/public/_probe.sh
```

This proved the plugin rendered correctly while the Playwright test said otherwise —
turning the question from "is the plugin broken" into "why does the test session differ",
which is a much smaller question.

## Cleaning up: count, never read

Whether a suite leaves data behind is a measurement:

```bash
count() { ddev mysql -uroot -proot db -e "
SELECT (SELECT COUNT(*) FROM shipping_method_translation WHERE name LIKE 'Test-%') AS shipping,
       (SELECT COUNT(*) FROM product_translation WHERE name LIKE 'Test-%')         AS products,
       (SELECT COUNT(*) FROM sales_channel_translation WHERE name LIKE '%acceptance%') AS channels,
       (SELECT COUNT(*) FROM customer)                                             AS customers;" -N; }

count; ddev playwright test; count; ddev playwright test; count
```

**Two runs**, because a clean-up that works once can still leave the second run's data.
Reading the clean-up code proves nothing — it looked correct while failing silently on
every single run.

## When the container serves stale code

Symptoms: an edit has no effect, a new console command shows its old output, a service
argument is not injected.

```bash
ddev exec bin/console cache:clear
ddev exec bash -c "cd /var/www/html/shopware && rm -rf var/cache/dev* && bin/console cache:warmup"
```

For the storefront, the theme is a second cache — and a sales channel the acceptance suite
just created has **no compiled theme at all**:

```bash
ddev exec bin/console theme:compile
```

## Checking a string replacement actually landed

Scripted edits fail silently when the target text moved — a style fixer reformatting
`$this->` to `static::` between two runs is enough. **Always verify:**

```bash
grep -n "the new text" path/to/file || echo "replacement did not land"
```

A whole round of confusion in this workspace came from a `pageFor()` helper that was never
changed, because a fixer had rewritten the line the replacement was anchored to.

## Where to look it up

`https://github.com/shopware/shopware/tree/v<INSTALLED VERSION>`, or a local checkout at
that version. Constructor argument order, feature flag defaults, nullability, how the core
tests this kind of class — all of it, and all of it has been got wrong by assuming.
→ [STANDARD-SOURCE-OF-TRUTH.md](STANDARD-SOURCE-OF-TRUTH.md)

## What to write down afterwards

Every diagnosis that took more than a few minutes goes into `CONTEXT.md`, in the shape that
saves the next person the same hour:

> **The context's shipping method has no price matrix; the delivery's does.**
> `$context->getShippingMethod()->getPrices()` returns an empty collection. The shipping
> method on `$cart->getDeliveries()` carries it loaded. Found with a throwaway console
> command printing `prices: 0`.

Write the mistakes too, not only the conclusions. A record that only lists what worked is a
record that will not stop the next person from repeating what did not.
