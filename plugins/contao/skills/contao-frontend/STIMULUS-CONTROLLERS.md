# Turbo-compatible Stimulus controllers

How to write a Stimulus controller that survives Turbo's cache. The whole difficulty is one fact: a
cache snapshot is taken **before** the DOM is removed, so cleanup in `disconnect()` has no effect on
what gets cached.

## Lifecycle callbacks

| Callback | When it runs |
|---|---|
| `afterLoad()` | once, when the controller class is registered. Rarely needed. |
| `initialize()` | once, when the controller instance is created |
| `connect()` | each time the controller element is added to the DOM |
| `disconnect()` | each time the controller element is removed from the DOM |
| `beforeCache()` | before Turbo creates a cache snapshot. **Contao only.** |

## 1. Make transformations idempotent

A DOM modification has to be safe to apply more than once, because the cached snapshot may already
carry the previous run's changes. Four strategies:

1. Detect whether the change was already applied.
2. Set a `data-initialized` attribute and check it.
3. Restore the element to its original state in `beforeCache()`.
4. Remove the element entirely in `beforeCache()`.

**The trap in the first two**: the DOM you are inspecting is restored from cache and therefore dead.
It carries no event listeners and no live objects, so a check that looks at behaviour rather than
markup gives the wrong answer.

## 2. Clean up resources

`disconnect()` can run at any moment, so assume it will. Clean up CSS classes on parent elements,
sibling elements the controller created, and anything else that outlives the element itself.

Three cases to survive:

- the resource may not exist, so check before removing it
- `beforeCache()` may already have run and undone part of the work
- another controller may have altered the DOM in between

## 3. Conventions

- **Prefix internal methods with an underscore**, to separate them from the public API.
- **Avoid `addEventListener`.** Use the `data-action` notation instead.
- Where a listener is registered by hand, remove it in `disconnect()`, unless it targets the
  controller element itself or one of its children.

## Source

Distilled from
[docs.contao.org/5.x/dev/internals/_stimulus-backend](https://docs.contao.org/5.x/dev/internals/_stimulus-backend/),
retrieved 2026-08-21. The leading underscore marks it an internal page in the documentation's own
navigation; `beforeCache()` is a Contao addition rather than part of Stimulus.
