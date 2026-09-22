# `ResetInterface` and `kernel.reset`

## The problem

A service that caches something keeps that cache — across request boundaries, whenever the
kernel outlives the request.

| Environment | Why it matters |
|---|---|
| Message consumers (`messenger:consume`) | one long-running process, many messages |
| Tests | many tests in one kernel |
| RoadRunner, FrankenPHP, Swoole | the worker lives across many requests |

**The consequence:** request two sees request one's cache. A service that caches per
category shows the first page's data on the second page view.

## The fix

```php
use Symfony\Contracts\Service\ResetInterface;

class MyLoader implements ResetInterface
{
    /** @var array<string, MyCollection> */
    private array $cache = [];

    #[\Override]
    public function reset(): void
    {
        $this->cache = [];
    }
}
```

Plus the tag in the service definition:

```php
->tag('kernel.reset', ['method' => 'reset']);
```

## Why the tag is set by hand

Symfony normally wires `ResetInterface` to the tag through
`registerForAutoconfiguration`. A plugin that registers its services **explicitly**, as
the standard requires ([DEPENDENCY-INJECTION.md](DEPENDENCY-INJECTION.md)), does not use
`autoconfigure` — so the mechanism never runs and **the interface alone does nothing.**

This is a silent trap: the interface is implemented, the method exists, the code looks
complete, and `reset()` is never called. Whoever turns autoconfigure off takes on
responsibility for every tag.

## Which services need it

**Any service holding state beyond a single call:**

- a property that caches
- a remembered query result
- a built index
- a counter

**Not needed** for stateless services — which should be the majority. A service with no
mutable properties needs no `reset()`.

**The check:** does the class have a non-`readonly` property written after construction?
Then it needs `ResetInterface` and the tag.

## How it is tested

```php
public function testItForgetsItsCacheOnReset(): void
{
    $subject = new MyLoader($repository);

    $subject->load('some-id', $context);
    $subject->reset();
    $subject->load('some-id', $context);

    // The repository was asked twice, not once: the cache did not survive the reset.
    static::assertCount(2, $repository->searches());
}
```

**Assert the effect, not the property.** A test reading the private `$cache` through
reflection passes even when the tag is missing — and the tag is the part that actually
breaks.
