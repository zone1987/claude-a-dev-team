# Entity Protection

Scope-based access control at the entity level, complementing field-level `WriteProtected` flags.

## EntityProtection (abstract base)

- `parse(): \Generator` - yields protection identifiers
- `isAllowed(string $scope): bool` - default returns `true`

## WriteProtection

**Constructor:** `(string ...$allowedScopes)`

Prevents write operations unless context scope is allowed. `isAllowed()` checks scope against allow-list.

## ReadProtection

Same structure as WriteProtection. **Experimental** - scope may not be consistently guaranteed.

## EntityProtectionCollection

Extends `Collection<EntityProtection>`. Keys by FQCN (one instance per type).

## EntityProtectionValidator

Event subscriber enforcing protections at runtime.

**Subscribed events:**
- `PreWriteValidationEvent` -> validates write commands against `WriteProtection`
- `EntitySearchedEvent` -> validates search against `ReadProtection`, recursively checks nested associations

Usage in definitions:
```php
protected function defineProtections(): EntityProtectionCollection
{
    return new EntityProtectionCollection([
        new WriteProtection(Context::SYSTEM_SCOPE),
    ]);
}
```
