# PHPStan-Shopware: Vollständige Regelliste

Quelle: `shopwarelabs/phpstan-shopware`, Stand 2025.
Alle Regeln sind in `rules.neon` aktiviert. Identifier folgen dem Schema `shopware.*`.

---

## 1. DALDefinitionRule (`BestPractise\DALDefinitionRule`)

**Identifier:** `shopware.bestPractise.dal.propertyMissing` / `.propertyReadonly` / `.propertyPrivate` / `.noGetter` / `.noSetter`

**Prüft:** Konsistenz zwischen DAL `EntityDefinition` (Felder) und der zugehörigen `Entity`-Klasse (Properties).

- Feld in Definition, aber Property fehlt im Entity → `propertyMissing`
- Property ist `readonly` → `propertyReadonly`
- Property ist `private` (EntityHydrator kann private Properties nicht befüllen) → `propertyPrivate`
- Property ist `protected` ohne passende Getter-Methode (`get…`, `is…`, `has…`) → `noGetter`
- Property ist `protected` ohne Setter (außer bei `runtime`/`computed` Feldern) → `noSetter`

**Verstoß:**
```php
class ProductEntity extends Entity {
    private string $name; // private → phpstan error
}
```

---

## 2. PreferRouteEventRule (`BestPractise\PreferRouteEventRule`)

**Identifier:** `shopware.bestPractise.preferRouteEventListener`

**Prüft:** Event-Listener auf `kernel.request`, `kernel.response`, `kernel.controller`, die intern auf eine bestimmte Route filtern (`$request->attributes->get('_route') !== 'meine.route'`).

Empfiehlt stattdessen, den route-spezifischen Event (z.B. `meine.route.request`) zu verwenden, der nur bei Match aufgerufen wird.

**Verstoß:**
```php
#[AsEventListener(event: 'kernel.request')]
public function onRequest(RequestEvent $event): void {
    if ($event->getRequest()->attributes->get('_route') !== 'frontend.home.page') {
        return; // ← Regel schlägt an
    }
    // ...
}
```

**Fix:** Auf `frontend.home.page.request` lauschen.

---

## 3. ClassExtendUsesAbstractClassWhenExisting (`ClassExtendUsesAbstractClassWhenExisting`)

**Identifier:** `shopware.class.extends.abstract`

**Prüft:** Wenn eine Klasse eine Shopware-Klasse extends, die eine `getDecorated()`-Methode besitzt (Decoration-Pattern), und in der Vererbungskette eine abstrakte Klasse existiert, muss diese abstrakte Klasse extended werden (nicht die konkrete Implementierung).

**Verstoß:**
```php
// Falsch: Direkt konkrete Klasse extends
class MyProductRoute extends ProductRoute { ... }

// Richtig:
class MyProductRoute extends AbstractProductRoute { ... }
```

---

## 4. DisallowDefaultContextCreation (`DisallowDefaultContextCreation`)

**Identifier:** `shopware.disallow.default.context.creation`

**Prüft:** Aufruf von `Context::createDefaultContext()` wenn `Context::createCLIContext()` vorhanden ist.

**Verstoß:**
```php
$context = Context::createDefaultContext(); // ← Fehler
```

**Fix:**
- CLI: `Context::createCLIContext()`
- Web: Context aus Controller-Parameter durchreichen

---

## 5. DisallowFunctionsRule (`DisallowFunctionsRule`)

**Identifier:** `shopware.disallowFunctions`

**Prüft:** Verbotene Debug-/Terminierungsfunktionen im produktiven Code.

**Verbotene Funktionen:** `var_dump`, `exit`, `die`, `dd`, `dump`

**Verstoß:**
```php
var_dump($data); // ← Fehler
dd($product);   // ← Fehler
```

---

## 6. DisallowSessionFunctionsRule (`DisallowSessionFunctionsRule`)

**Identifier:** `shopware.disallowSessionFunctions`

**Prüft:** Direkte PHP-Session-Funktionen statt Symfony-Session-Komponente.

**Verbotene Funktionen:** `session_write_close`, `session_start`, `session_destroy`

**Verstoß:**
```php
session_start(); // ← Fehler
```

**Fix:** `$request->getSession()` aus dem Symfony Request-Objekt verwenden.

---

## 7. ForbidGlobBraceRule (`ForbidGlobBraceRule`)

**Identifier:** `shopware.forbidGlobBrace`

**Prüft:** Verwendung der Konstante `GLOB_BRACE`, die auf manchen Plattformen (Alpine Linux / musl libc) nicht unterstützt wird.

**Verstoß:**
```php
glob('/path/**', GLOB_BRACE); // ← Fehler
```

---

## 8. InternalClassExtendsRule (`InternalClassExtendsRule`)

**Identifier:** `shopware.internalClassExtends`

**Prüft:** Extends einer als `@internal` markierten Shopware-Klasse.

**Verstoß:**
```php
// FooService ist @internal in Shopware
class MyService extends FooService { } // ← Fehler
```

---

## 9. InternalFunctionCallRule (`InternalFunctionCallRule`)

**Identifier:** `shopware.internalFunctionCall`

**Prüft:** Aufruf einer als `@internal` markierten Shopware-Funktion aus einem anderen Package-Namespace heraus.

Namespace-Prüfung: Aufruf innerhalb desselben Shopware-Packages (`NamespaceChecker::arePartOfTheSamePackage`) ist erlaubt.

---

## 10. InternalMethodCallRule (`InternalMethodCallRule`)

**Identifier:** `shopware.internalMethodCall`

**Prüft:** Aufruf einer als `@internal` markierten Methode einer Shopware-Klasse aus einem fremden Namespace.

**Verstoß:**
```php
// Methode doInternalStuff() ist @internal
$service->doInternalStuff(); // ← Fehler (wenn außerhalb des gleichen Packages)
```

---

## 11. MethodBecomesAbstractRule (`MethodBecomesAbstractRule`)

**Identifier:** `shopware.method.becomes.abstract`

**Prüft:** Methoden in Parent-Klassen, die mit `@abstract` im DocComment markiert sind (aber noch nicht PHP-abstract sind) und in der Kindklasse nicht implementiert wurden.

Dient zur Vorbereitung von Breaking Changes: Eine Methode wird im nächsten Major als `abstract` deklariert, Plugins sollen sie bereits jetzt implementieren.

**Verstoß:**
```php
class MyRoute extends AbstractProductRoute {
    // getDecorated() fehlt, aber Parent hat @abstract getDecorated()
}
```

---

## 12. NoDALFilterByID (`NoDALFilterByID`)

**Identifier:** `shopware.dal.filterById`

**Prüft:** Direkte Verwendung von `EqualsFilter('id', ...)` oder `EqualsAnyFilter('id', ...)`.

IDs sollen direkt über `Criteria`-Konstruktor oder `$criteria->setIds()` übergeben werden.

Ausnahme: Innerhalb eines `MultiFilter` oder `NotFilter` ist es erlaubt.

**Verstoß:**
```php
$criteria->addFilter(new EqualsFilter('id', $id));       // ← Fehler
$criteria->addFilter(new EqualsAnyFilter('id', $ids));   // ← Fehler
```

**Fix:**
```php
$criteria = new Criteria([$id]);
// oder
$criteria->setIds($ids);
```

---

## 13. NoSessionInPaymentHandlerAndStoreApiRule (`NoSessionInPaymentHandlerAndStoreApiRule`)

**Identifier:** `shopware.sessionUsageInPaymentHandler` / `shopware.sessionUsageInStoreApi`

**Prüft:** Nutzung von `SessionInterface`-Methoden innerhalb von:
- Klassen, die `AbstractPaymentHandler` erweitern
- Store-API-Controllern (`_routeScope: store-api`)

Sessions sind in diesen Kontexten nicht erlaubt (headless/API-Kompatibilität).

---

## 14. NoSuperglobalsRule (`NoSuperglobalsRule`)

**Identifier:** `shopware.noSuperGlobals`

**Prüft:** Direkter Zugriff auf Superglobals `$_GET`, `$_POST`, `$_FILES`, `$_REQUEST`.

**Verstoß:**
```php
$data = $_POST['name']; // ← Fehler
```

**Fix:** Symfony `Request`-Objekt verwenden.

---

## 15. NoSymfonySessionInConstructorRule (`NoSymfonySessionInConstructorRule`)

**Identifier:** `shopware.sessionUsageInConstructor`

**Prüft:** Methodenaufrufe auf `SessionInterface` innerhalb des Konstruktors (`__construct`).

Die Session darf im Konstruktor nicht verwendet werden, da sie dort ggf. noch nicht initialisiert ist.

**Verstoß:**
```php
public function __construct(SessionInterface $session) {
    $value = $session->get('key'); // ← Fehler
}
```

---

## 16. NoUserEntityGetStoreTokenRule (`NoUserEntityGetStoreTokenRule`)

**Identifier:** `shopware.noUserEntityGetStoreToken`

**Prüft:** Aufruf von `UserEntity::getStoreToken()`.

Das Store-Token ist ein internes Sicherheitsmerkmal und darf in Plugins nicht ausgelesen werden.

**Verstoß:**
```php
$token = $userEntity->getStoreToken(); // ← Fehler
```

---

## 17. ScheduledTaskTooLowIntervalRule (`ScheduledTaskTooLowIntervalRule`)

**Identifier:** `shopware.scheduledTaskLowInterval`

**Prüft:** `getDefaultInterval()` in Klassen, die `ScheduledTask` erweitern. Minimum-Intervall: **300 Sekunden** (5 Minuten).

**Verstoß:**
```php
class MyTask extends ScheduledTask {
    public static function getDefaultInterval(): int {
        return 60; // ← Fehler: unter 300 Sekunden
    }
}
```

---

## 18. SetForeignKeyRule (`SetForeignKeyRule`)

**Identifier:** `shopware.foreign.key.checks`

**Prüft:** `FOREIGN_KEY_CHECKS`-Deaktivierung in SQL-Strings innerhalb von `update()`-Methoden von `MigrationStep` oder `Plugin`.

Das Deaktivieren von Foreign-Key-Checks in Migrationen ist verboten. Stattdessen sollen Daten in der richtigen Reihenfolge gelöscht werden.

**Verstoß:**
```php
$connection->executeStatement('SET FOREIGN_KEY_CHECKS=0'); // ← Fehler
```

---

## 19. NoEntityRepositoryInLoopRule (`NoEntityRepositoryInLoopRule`)

**Identifier:** `shopware.noEntityRepositoryInLoop`

**Prüft:** Methodenaufrufe auf `EntityRepository` innerhalb von `for`- oder `foreach`-Schleifen.

Verhindert N+1-Queries.

**Verstoß:**
```php
foreach ($productIds as $id) {
    $this->productRepository->search(new Criteria([$id]), $context); // ← Fehler
}
```

**Fix:** Alle IDs in einer `Criteria` sammeln und einmalig abfragen.

---

## 20. ForbidLocalDiskWriteRule (`ForbidLocalDiskWriteRule`)

**Identifier:** `shopware.forbidLocalDiskWrite`

**Prüft:** Direktes Schreiben auf die lokale Festplatte außerhalb des temp-Verzeichnisses.

**Überwachte Funktionen/Methoden:**
- `file_put_contents`, `fopen` (Schreib-Modi), `symlink`, `mkdir`, `rmdir`, `unlink`, `rename`
- `ZipArchive::open` mit `CREATE`/`OVERWRITE`-Flags
- `Symfony\Component\Filesystem\Filesystem`-Methoden: `dumpFile`, `mkdir`, `touch`, `remove`, `chmod`, `chown`, `chgrp`, `rename`, `symlink`, `hardlink`, `mirror`, `copy`, `tempnam`, `appendToFile`

Ausnahmen: Pfade unter `sys_get_temp_dir()`, `php://stdin/stdout/stderr`, `STDIN/STDOUT/STDERR`.

**Verstoß:**
```php
file_put_contents('/var/www/html/data.txt', $content); // ← Fehler
```

**Fix:** Flysystem verwenden: https://developer.shopware.com/docs/guides/plugins/plugins/framework/filesystem/filesystem.html

---

## 21. ForwardSalesChannelContextToSystemConfigServiceRule (`ForwardSalesChannelContextToSystemConfigServiceRule`)

**Identifier:** `shopware.forwardSalesChannelContext`

**Prüft:** Aufrufe von `SystemConfigService::get()`, `getString()`, `getInt()`, `getFloat()`, `getBool()` wenn im Scope eine `SalesChannelContext`-Variable vorhanden ist, aber kein `salesChannelId`-Parameter übergeben wird.

**Verstoß:**
```php
public function handle(SalesChannelContext $context): void {
    $value = $this->systemConfig->get('MyPlugin.config.key'); // ← Fehler, salesChannelId fehlt
}
```

**Fix:**
```php
$value = $this->systemConfig->get('MyPlugin.config.key', $context->getSalesChannelId());
```

---

## 22. ForbidPredictableSaltRule (`ForbidPredictableSaltRule`)

**Identifier:** `shopware.forbidPredictableSalt`

**Prüft:** Hardcodierte Salts bei Passwort-Hashing:
- `crypt($password, $salt)` mit literal String als 2. Argument
- `password_hash($password, $algo, ['salt' => '...'])` mit explizitem `salt`-Key

**Verstoß:**
```php
crypt($password, 'mysecret'); // ← Fehler
password_hash($pw, PASSWORD_BCRYPT, ['salt' => 'abc']); // ← Fehler
```

---

## 23. ForbidWeakCryptoKeyRule (`ForbidWeakCryptoKeyRule`)

**Identifier:** `shopware.forbidWeakCryptoKey`

**Prüft:** `openssl_pkey_new(['private_key_bits' => N])` mit N < 2048.

**Verstoß:**
```php
openssl_pkey_new(['private_key_bits' => 1024]); // ← Fehler
```

---

## 24. ForbidInsecureCookieRule (`ForbidInsecureCookieRule`)

**Identifier:** `shopware.forbidInsecureCookie`

**Prüft:** `setcookie()` / `setrawcookie()` ohne `secure=true`.

Beide Signaturen werden geprüft:
- Legacy: 6. Argument muss `true` sein
- Array-Optionen: `['secure' => true]` muss gesetzt sein

**Verstoß:**
```php
setcookie('session', $value, 0, '/', ''); // ← Fehler: kein secure
setcookie('session', $value, ['httponly' => true]); // ← Fehler: secure fehlt
```

---

## 25. ForbidInsecureSymfonyCookieRule (`ForbidInsecureSymfonyCookieRule`)

**Identifier:** `shopware.forbidInsecureSymfonyCookie`

**Prüft:** `new Cookie(...)`, `Cookie::create(...)` und `->withSecure(...)` ohne explizites `secure=true`.

Alle drei Erstellungswege werden abgedeckt. `withSecure()` ohne Argument gilt als sicher (default true).

**Verstoß:**
```php
new Cookie('name', 'value'); // ← Fehler: secure-Parameter fehlt
Cookie::create('name')->withSecure(false); // ← Fehler
```

**Fix:**
```php
new Cookie('name', 'value', secure: true);
Cookie::create('name')->withSecure(); // withSecure() ohne Arg = true
```

---

## 26. ForbidDisabledSslVerificationRule (`ForbidDisabledSslVerificationRule`)

**Identifier:** `shopware.forbidDisabledSslVerification`

**Prüft:** Deaktivierung der SSL/TLS-Zertifikatsprüfung:
- `stream_context_create(['ssl' => ['verify_peer' => false]])` oder `verify_peer_name`
- `curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false)`
- `curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0)` oder `1` (< 2 gilt als deaktiviert)

**Verstoß:**
```php
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false); // ← Fehler (MITM-Risiko)
```

---

## 27. NoEmptyResponseRule (`NoEmptyResponseRule`)

**Identifier:** `shopware.noEmptyResponse`

**Prüft:** `new Response('')` oder `new Response(null)` ohne angemessenen Status-Code.

Erlaubte Status-Codes für leere Body-Responses: `204`, `301`, `302`, `303`, `304`, `307`, `308`.

**Verstoß:**
```php
return new Response(''); // ← Fehler: kein Inhalt ohne entsprechenden Status
```

**Fix:**
```php
return new Response('', Response::HTTP_NO_CONTENT); // 204 ist erlaubt
// oder
return new JsonResponse(['data' => $result]); // Inhalt angeben
```

---

## Type-Extension

### CollectionHasSpecifyingExtension

**Tag:** `phpstan.typeSpecifier.methodTypeSpecifyingExtension`

Verbessert die Typinferenz bei `Collection::has($key)`. Nach einem erfolgreichen `has()`-Check narrowt PHPStan den Rückgabetyp von `Collection::get($key)` auf non-null.

```php
if ($collection->has($id)) {
    $item = $collection->get($id); // PHPStan weiß: nicht null
}
```

---

## Collectors

- **DALDefinitionCollector:** Sammelt Felder aller `EntityDefinition`-Subklassen (Name, `runtime`, `computed`-Flags)
- **DALEntityCollector:** Sammelt Properties und Methoden aller `Entity`-Subklassen (Sichtbarkeit, `readonly`, Getter/Setter)

Beide Collectors arbeiten zusammen mit `DALDefinitionRule`.
