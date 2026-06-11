# config/packages/monolog.yaml (`ResubmissionAppServer/config/packages/monolog.yaml`)

## Zweck
Logging-Konfiguration (Symfony-Standard) je Umgebung: dev → Datei-/Console-Handler (debug); test/prod → fingers_crossed (action_level error), prod schreibt JSON nach `php://stderr`, eigener `deprecation`-Channel.

## Bezüge
Symfony MonologBundle (weitgehend Boilerplate).
