# E2E bootstrap.php (`tests/E2E/bootstrap.php`)

## Zweck
Bootstrap der Panther-E2E-Suite. Ersetzt `%env(VAR)%`-Platzhalter in `$_SERVER`/`$_ENV` (die in `phpunit.panther.xml` als XML-Literale stehen), damit z.B. `%env(DDEV_PRIMARY_URL)%` nicht roh in Request-URLs landet. Auflösung: `$_SERVER` → `$_ENV` → `getenv()`; ungelöste Platzhalter bleiben (sichtbarer Fehler).

## Bezüge
`phpunit.panther.xml`, `Support/PantherTestCase.php`.
