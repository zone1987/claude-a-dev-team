# config/packages/sentry.yaml (`ResubmissionAppServer/config/packages/sentry.yaml`)

## Zweck
Sentry-Error-Tracking, nur im `prod`-Env aktiv: DSN aus `%env(SENTRY_DSN)%`, ignoriert Fatal-Error-Exceptions.

## Inhalt
- `when@prod.sentry.dsn = %env(SENTRY_DSN)%`, `options.ignore_exceptions` (FatalError/FatalErrorException).

## Besonderheiten
- Produktive Fehler des AppServers landen in Sentry (relevant fürs Debugging der RheinKurier-/Wiedervorlagen-Flows, da keine Tests existieren).

## Bezüge
Sentry SDK (Boilerplate + DSN).
