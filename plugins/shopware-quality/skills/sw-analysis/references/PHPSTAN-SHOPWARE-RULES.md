# PHPStan-Shopware: Complete Rule List

Source: `shopwarelabs/phpstan-shopware`, as of 2025.
All rules are enabled in `rules.neon`. Identifiers follow the `shopware.*` scheme.

---

## Contents

- [1. DALDefinitionRule (`BestPractise\DALDefinitionRule`)](#1-daldefinitionrule-bestpractisedaldefinitionrule)
- [2. PreferRouteEventRule (`BestPractise\PreferRouteEventRule`)](#2-preferrouteeventrule-bestpractisepreferrouteeventrule)
- [3. ClassExtendUsesAbstractClassWhenExisting (`ClassExtendUsesAbstractClassWhenExisting`)](#3-classextendusesabstractclasswhenexisting-classextendusesabstractclasswhenexisting)
- [4. DisallowDefaultContextCreation (`DisallowDefaultContextCreation`)](#4-disallowdefaultcontextcreation-disallowdefaultcontextcreation)
- [5. DisallowFunctionsRule (`DisallowFunctionsRule`)](#5-disallowfunctionsrule-disallowfunctionsrule)
- [6. DisallowSessionFunctionsRule (`DisallowSessionFunctionsRule`)](#6-disallowsessionfunctionsrule-disallowsessionfunctionsrule)
- [7. ForbidGlobBraceRule (`ForbidGlobBraceRule`)](#7-forbidglobbracerule-forbidglobbracerule)
- [8. InternalClassExtendsRule (`InternalClassExtendsRule`)](#8-internalclassextendsrule-internalclassextendsrule)
- [9. InternalFunctionCallRule (`InternalFunctionCallRule`)](#9-internalfunctioncallrule-internalfunctioncallrule)
- [10. InternalMethodCallRule (`InternalMethodCallRule`)](#10-internalmethodcallrule-internalmethodcallrule)
- [11. MethodBecomesAbstractRule (`MethodBecomesAbstractRule`)](#11-methodbecomesabstractrule-methodbecomesabstractrule)
- [12. NoDALFilterByID (`NoDALFilterByID`)](#12-nodalfilterbyid-nodalfilterbyid)
- [13. NoSessionInPaymentHandlerAndStoreApiRule (`NoSessionInPaymentHandlerAndStoreApiRule`)](#13-nosessioninpaymenthandlerandstoreapirule-nosessioninpaymenthandlerandstoreapirule)
- [14. NoSuperglobalsRule (`NoSuperglobalsRule`)](#14-nosuperglobalsrule-nosuperglobalsrule)
- [15. NoSymfonySessionInConstructorRule (`NoSymfonySessionInConstructorRule`)](#15-nosymfonysessioninconstructorrule-nosymfonysessioninconstructorrule)
- [16. NoUserEntityGetStoreTokenRule (`NoUserEntityGetStoreTokenRule`)](#16-nouserentitygetstoretokenrule-nouserentitygetstoretokenrule)
- [17. ScheduledTaskTooLowIntervalRule (`ScheduledTaskTooLowIntervalRule`)](#17-scheduledtasktoolowintervalrule-scheduledtasktoolowintervalrule)
- [18. SetForeignKeyRule (`SetForeignKeyRule`)](#18-setforeignkeyrule-setforeignkeyrule)
- [19. NoEntityRepositoryInLoopRule (`NoEntityRepositoryInLoopRule`)](#19-noentityrepositoryinlooprule-noentityrepositoryinlooprule)
- [20. ForbidLocalDiskWriteRule (`ForbidLocalDiskWriteRule`)](#20-forbidlocaldiskwriterule-forbidlocaldiskwriterule)
- [21. ForwardSalesChannelContextToSystemConfigServiceRule (`ForwardSalesChannelContextToSystemConfigServiceRule`)](#21-forwardsaleschannelcontexttosystemconfigservicerule-forwardsaleschannelcontexttosystemconfigservicerule)
- [22. ForbidPredictableSaltRule (`ForbidPredictableSaltRule`)](#22-forbidpredictablesaltrule-forbidpredictablesaltrule)
- [23. ForbidWeakCryptoKeyRule (`ForbidWeakCryptoKeyRule`)](#23-forbidweakcryptokeyrule-forbidweakcryptokeyrule)
- [24. ForbidInsecureCookieRule (`ForbidInsecureCookieRule`)](#24-forbidinsecurecookierule-forbidinsecurecookierule)
- [25. ForbidInsecureSymfonyCookieRule (`ForbidInsecureSymfonyCookieRule`)](#25-forbidinsecuresymfonycookierule-forbidinsecuresymfonycookierule)
- [26. ForbidDisabledSslVerificationRule (`ForbidDisabledSslVerificationRule`)](#26-forbiddisabledsslverificationrule-forbiddisabledsslverificationrule)
- [27. NoEmptyResponseRule (`NoEmptyResponseRule`)](#27-noemptyresponserule-noemptyresponserule)
- [Type Extension](#type-extension)
- [Collectors](#collectors)

## 1. DALDefinitionRule (`BestPractise\DALDefinitionRule`)

**Identifier:** `shopware.bestPractise.dal.propertyMissing` / `.propertyReadonly` / `.propertyPrivate` / `.noGetter` / `.noSetter`

**Checks:** consistency between the DAL `EntityDefinition` (fields) and the corresponding `Entity` class (properties).

- Field in the definition but property missing in the entity → `propertyMissing`
- Property is `readonly` → `propertyReadonly`
- Property is `private` (the EntityHydrator cannot populate private properties) → `propertyPrivate`
- Property is `protected` without a matching getter method (`get…`, `is…`, `has…`) → `noGetter`
- Property is `protected` without a setter (except for `runtime`/`computed` fields) → `noSetter`

**Violation:**
```php
class ProductEntity extends Entity {
    private string $name; // private → phpstan error
}
```

---

## 2. PreferRouteEventRule (`BestPractise\PreferRouteEventRule`)

**Identifier:** `shopware.bestPractise.preferRouteEventListener`

**Checks:** event listeners on `kernel.request`, `kernel.response`, `kernel.controller` that internally filter for a specific route (`$request->attributes->get('_route') !== 'my.route'`).

Recommends using the route-specific event instead (for example `my.route.request`), which is only dispatched on a match.

**Violation:**
```php
#[AsEventListener(event: 'kernel.request')]
public function onRequest(RequestEvent $event): void {
    if ($event->getRequest()->attributes->get('_route') !== 'frontend.home.page') {
        return; // ← the rule triggers here
    }
    // ...
}
```

**Fix:** listen to `frontend.home.page.request`.

---

## 3. ClassExtendUsesAbstractClassWhenExisting (`ClassExtendUsesAbstractClassWhenExisting`)

**Identifier:** `shopware.class.extends.abstract`

**Checks:** if a class extends a Shopware class that has a `getDecorated()` method (decoration pattern) and an abstract class exists in the inheritance chain, that abstract class must be extended (not the concrete implementation).

**Violation:**
```php
// Wrong: extending the concrete class directly
class MyProductRoute extends ProductRoute { ... }

// Correct:
class MyProductRoute extends AbstractProductRoute { ... }
```

---

## 4. DisallowDefaultContextCreation (`DisallowDefaultContextCreation`)

**Identifier:** `shopware.disallow.default.context.creation`

**Checks:** calls to `Context::createDefaultContext()` when `Context::createCLIContext()` is available.

**Violation:**
```php
$context = Context::createDefaultContext(); // ← error
```

**Fix:**
- CLI: `Context::createCLIContext()`
- Web: pass the context through from the controller parameter

---

## 5. DisallowFunctionsRule (`DisallowFunctionsRule`)

**Identifier:** `shopware.disallowFunctions`

**Checks:** forbidden debug/termination functions in production code.

**Forbidden functions:** `var_dump`, `exit`, `die`, `dd`, `dump`

**Violation:**
```php
var_dump($data); // ← error
dd($product);   // ← error
```

---

## 6. DisallowSessionFunctionsRule (`DisallowSessionFunctionsRule`)

**Identifier:** `shopware.disallowSessionFunctions`

**Checks:** direct PHP session functions instead of the Symfony session component.

**Forbidden functions:** `session_write_close`, `session_start`, `session_destroy`

**Violation:**
```php
session_start(); // ← error
```

**Fix:** use `$request->getSession()` from the Symfony request object.

---

## 7. ForbidGlobBraceRule (`ForbidGlobBraceRule`)

**Identifier:** `shopware.forbidGlobBrace`

**Checks:** use of the `GLOB_BRACE` constant, which is not supported on some platforms (Alpine Linux / musl libc).

**Violation:**
```php
glob('/path/**', GLOB_BRACE); // ← error
```

---

## 8. InternalClassExtendsRule (`InternalClassExtendsRule`)

**Identifier:** `shopware.internalClassExtends`

**Checks:** extending a Shopware class marked as `@internal`.

**Violation:**
```php
// FooService is @internal in Shopware
class MyService extends FooService { } // ← error
```

---

## 9. InternalFunctionCallRule (`InternalFunctionCallRule`)

**Identifier:** `shopware.internalFunctionCall`

**Checks:** calling a Shopware function marked as `@internal` from another package namespace.

Namespace check: calling from within the same Shopware package (`NamespaceChecker::arePartOfTheSamePackage`) is allowed.

---

## 10. InternalMethodCallRule (`InternalMethodCallRule`)

**Identifier:** `shopware.internalMethodCall`

**Checks:** calling a method of a Shopware class marked as `@internal` from a foreign namespace.

**Violation:**
```php
// The method doInternalStuff() is @internal
$service->doInternalStuff(); // ← error (when outside the same package)
```

---

## 11. MethodBecomesAbstractRule (`MethodBecomesAbstractRule`)

**Identifier:** `shopware.method.becomes.abstract`

**Checks:** methods in parent classes marked with `@abstract` in the doc comment (but not yet PHP-abstract) that the child class does not implement.

This prepares breaking changes: a method will be declared `abstract` in the next major, so plugins should implement it already.

**Violation:**
```php
class MyRoute extends AbstractProductRoute {
    // getDecorated() is missing, but the parent has @abstract getDecorated()
}
```

---

## 12. NoDALFilterByID (`NoDALFilterByID`)

**Identifier:** `shopware.dal.filterById`

**Checks:** direct use of `EqualsFilter('id', ...)` or `EqualsAnyFilter('id', ...)`.

Pass IDs directly via the `Criteria` constructor or `$criteria->setIds()`.

Exception: inside a `MultiFilter` or `NotFilter` it is allowed.

**Violation:**
```php
$criteria->addFilter(new EqualsFilter('id', $id));       // ← error
$criteria->addFilter(new EqualsAnyFilter('id', $ids));   // ← error
```

**Fix:**
```php
$criteria = new Criteria([$id]);
// or
$criteria->setIds($ids);
```

---

## 13. NoSessionInPaymentHandlerAndStoreApiRule (`NoSessionInPaymentHandlerAndStoreApiRule`)

**Identifier:** `shopware.sessionUsageInPaymentHandler` / `shopware.sessionUsageInStoreApi`

**Checks:** use of `SessionInterface` methods inside:
- classes extending `AbstractPaymentHandler`
- Store API controllers (`_routeScope: store-api`)

Sessions are not allowed in these contexts (headless/API compatibility).

---

## 14. NoSuperglobalsRule (`NoSuperglobalsRule`)

**Identifier:** `shopware.noSuperGlobals`

**Checks:** direct access to the superglobals `$_GET`, `$_POST`, `$_FILES`, `$_REQUEST`.

**Violation:**
```php
$data = $_POST['name']; // ← error
```

**Fix:** use the Symfony `Request` object.

---

## 15. NoSymfonySessionInConstructorRule (`NoSymfonySessionInConstructorRule`)

**Identifier:** `shopware.sessionUsageInConstructor`

**Checks:** method calls on `SessionInterface` inside the constructor (`__construct`).

The session must not be used in the constructor, because it may not be initialized at that point.

**Violation:**
```php
public function __construct(SessionInterface $session) {
    $value = $session->get('key'); // ← error
}
```

---

## 16. NoUserEntityGetStoreTokenRule (`NoUserEntityGetStoreTokenRule`)

**Identifier:** `shopware.noUserEntityGetStoreToken`

**Checks:** calls to `UserEntity::getStoreToken()`.

The store token is an internal security feature and must not be read in plugins.

**Violation:**
```php
$token = $userEntity->getStoreToken(); // ← error
```

---

## 17. ScheduledTaskTooLowIntervalRule (`ScheduledTaskTooLowIntervalRule`)

**Identifier:** `shopware.scheduledTaskLowInterval`

**Checks:** `getDefaultInterval()` in classes extending `ScheduledTask`. Minimum interval: **300 seconds** (5 minutes).

**Violation:**
```php
class MyTask extends ScheduledTask {
    public static function getDefaultInterval(): int {
        return 60; // ← error: below 300 seconds
    }
}
```

---

## 18. SetForeignKeyRule (`SetForeignKeyRule`)

**Identifier:** `shopware.foreign.key.checks`

**Checks:** disabling `FOREIGN_KEY_CHECKS` in SQL strings inside `update()` methods of `MigrationStep` or `Plugin`.

Disabling foreign key checks in migrations is forbidden. Delete data in the correct order instead.

**Violation:**
```php
$connection->executeStatement('SET FOREIGN_KEY_CHECKS=0'); // ← error
```

---

## 19. NoEntityRepositoryInLoopRule (`NoEntityRepositoryInLoopRule`)

**Identifier:** `shopware.noEntityRepositoryInLoop`

**Checks:** method calls on an `EntityRepository` inside `for` or `foreach` loops.

Prevents N+1 queries.

**Violation:**
```php
foreach ($productIds as $id) {
    $this->productRepository->search(new Criteria([$id]), $context); // ← error
}
```

**Fix:** collect all IDs in a single `Criteria` and query once.

---

## 20. ForbidLocalDiskWriteRule (`ForbidLocalDiskWriteRule`)

**Identifier:** `shopware.forbidLocalDiskWrite`

**Checks:** writing directly to the local disk outside the temp directory.

**Monitored functions/methods:**
- `file_put_contents`, `fopen` (write modes), `symlink`, `mkdir`, `rmdir`, `unlink`, `rename`
- `ZipArchive::open` with the `CREATE`/`OVERWRITE` flags
- `Symfony\Component\Filesystem\Filesystem` methods: `dumpFile`, `mkdir`, `touch`, `remove`, `chmod`, `chown`, `chgrp`, `rename`, `symlink`, `hardlink`, `mirror`, `copy`, `tempnam`, `appendToFile`

Exceptions: paths under `sys_get_temp_dir()`, `php://stdin/stdout/stderr`, `STDIN/STDOUT/STDERR`.

**Violation:**
```php
file_put_contents('/var/www/html/data.txt', $content); // ← error
```

**Fix:** use Flysystem: https://developer.shopware.com/docs/guides/plugins/plugins/framework/filesystem/filesystem.html

---

## 21. ForwardSalesChannelContextToSystemConfigServiceRule (`ForwardSalesChannelContextToSystemConfigServiceRule`)

**Identifier:** `shopware.forwardSalesChannelContext`

**Checks:** calls to `SystemConfigService::get()`, `getString()`, `getInt()`, `getFloat()`, `getBool()` when a `SalesChannelContext` variable is available in scope but no `salesChannelId` parameter is passed.

**Violation:**
```php
public function handle(SalesChannelContext $context): void {
    $value = $this->systemConfig->get('MyPlugin.config.key'); // ← error, salesChannelId missing
}
```

**Fix:**
```php
$value = $this->systemConfig->get('MyPlugin.config.key', $context->getSalesChannelId());
```

---

## 22. ForbidPredictableSaltRule (`ForbidPredictableSaltRule`)

**Identifier:** `shopware.forbidPredictableSalt`

**Checks:** hardcoded salts in password hashing:
- `crypt($password, $salt)` with a literal string as the second argument
- `password_hash($password, $algo, ['salt' => '...'])` with an explicit `salt` key

**Violation:**
```php
crypt($password, 'mysecret'); // ← error
password_hash($pw, PASSWORD_BCRYPT, ['salt' => 'abc']); // ← error
```

---

## 23. ForbidWeakCryptoKeyRule (`ForbidWeakCryptoKeyRule`)

**Identifier:** `shopware.forbidWeakCryptoKey`

**Checks:** `openssl_pkey_new(['private_key_bits' => N])` with N < 2048.

**Violation:**
```php
openssl_pkey_new(['private_key_bits' => 1024]); // ← error
```

---

## 24. ForbidInsecureCookieRule (`ForbidInsecureCookieRule`)

**Identifier:** `shopware.forbidInsecureCookie`

**Checks:** `setcookie()` / `setrawcookie()` without `secure=true`.

Both signatures are checked:
- Legacy: the 6th argument must be `true`
- Array options: `['secure' => true]` must be set

**Violation:**
```php
setcookie('session', $value, 0, '/', ''); // ← error: no secure
setcookie('session', $value, ['httponly' => true]); // ← error: secure missing
```

---

## 25. ForbidInsecureSymfonyCookieRule (`ForbidInsecureSymfonyCookieRule`)

**Identifier:** `shopware.forbidInsecureSymfonyCookie`

**Checks:** `new Cookie(...)`, `Cookie::create(...)` and `->withSecure(...)` without an explicit `secure=true`.

All three creation paths are covered. `withSecure()` without an argument counts as secure (defaults to true).

**Violation:**
```php
new Cookie('name', 'value'); // ← error: secure parameter missing
Cookie::create('name')->withSecure(false); // ← error
```

**Fix:**
```php
new Cookie('name', 'value', secure: true);
Cookie::create('name')->withSecure(); // withSecure() without an arg = true
```

---

## 26. ForbidDisabledSslVerificationRule (`ForbidDisabledSslVerificationRule`)

**Identifier:** `shopware.forbidDisabledSslVerification`

**Checks:** disabling SSL/TLS certificate verification:
- `stream_context_create(['ssl' => ['verify_peer' => false]])` or `verify_peer_name`
- `curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false)`
- `curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0)` or `1` (< 2 counts as disabled)

**Violation:**
```php
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false); // ← error (MITM risk)
```

---

## 27. NoEmptyResponseRule (`NoEmptyResponseRule`)

**Identifier:** `shopware.noEmptyResponse`

**Checks:** `new Response('')` or `new Response(null)` without an appropriate status code.

Allowed status codes for empty body responses: `204`, `301`, `302`, `303`, `304`, `307`, `308`.

**Violation:**
```php
return new Response(''); // ← error: no content without a matching status
```

**Fix:**
```php
return new Response('', Response::HTTP_NO_CONTENT); // 204 is allowed
// or
return new JsonResponse(['data' => $result]); // provide content
```

---

## Type Extension

### CollectionHasSpecifyingExtension

**Tag:** `phpstan.typeSpecifier.methodTypeSpecifyingExtension`

Improves type inference for `Collection::has($key)`. After a successful `has()` check, PHPStan narrows the return type of `Collection::get($key)` to non-null.

```php
if ($collection->has($id)) {
    $item = $collection->get($id); // PHPStan knows: not null
}
```

---

## Collectors

- **DALDefinitionCollector:** collects the fields of all `EntityDefinition` subclasses (name, `runtime`, `computed` flags)
- **DALEntityCollector:** collects the properties and methods of all `Entity` subclasses (visibility, `readonly`, getters/setters)

Both collectors work together with `DALDefinitionRule`.
