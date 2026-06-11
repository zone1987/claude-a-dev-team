---
title: App Server Public Directory & .htaccess
impact: HIGH
impactDescription: Jeder PHP/Symfony App Server benötigt eine .htaccess im public-Verzeichnis, damit Apache-Anfragen korrekt an den Front Controller (index.php) weitergeleitet werden.
tags: sdk, php, symfony, app-server, apache, htaccess, public
---

## .htaccess im public-Verzeichnis

Jeder Shopware App Server auf Basis von PHP/Symfony **MUSS** eine `.htaccess`-Datei im `public/`-Verzeichnis enthalten.

### Warum ist die .htaccess erforderlich?

- Apache leitet alle Anfragen an `public/index.php` (den Symfony Front Controller) weiter
- Ohne `.htaccess` funktioniert das URL-Routing nicht – alle Webhook- und API-Endpunkte sind nicht erreichbar
- Die Datei ermöglicht das Hosting unter einem Subpfad (z. B. `example.com/subpath`)
- Der `HTTP_AUTHORIZATION`-Header (für HMAC-Verifizierung benötigt) wird korrekt weitergereicht

### Pflichtstruktur

```
my-app-server/
├── public/
│   ├── .htaccess        ← PFLICHT für Apache
│   └── index.php
├── src/
├── config/
└── composer.json
```

### Beispieldatei

Siehe `examples/public.htaccess` für die vollständige, kommentierte Referenzdatei.

### Wichtige Funktionen der .htaccess

| Direktive | Zweck |
|-----------|-------|
| `DirectoryIndex index.php` | Front Controller als Standard-Index |
| `Options -MultiViews` | Verhindert ungewolltes Content Negotiation |
| `RewriteRule .* - [E=BASE:%1]` | Ermittelt dynamisch den RewriteBase-Pfad (Subpfad-Unterstützung) |
| `E=HTTP_AUTHORIZATION:%0` | Stellt Authorization-Header sicher (Apache entfernt ihn sonst) |
| `R=301` für `/index.php/` | Entfernt `/index.php/` aus URLs |
| `RewriteCond %{REQUEST_FILENAME} !-f` | Leitet nur nicht-existierende Dateien weiter |

### Nginx-Alterative

Bei Nginx-Hosting entfällt die `.htaccess`. Stattdessen wird in der Nginx-Konfiguration direkt ein `try_files`-Block eingesetzt:

```nginx
location / {
    try_files $uri /index.php$is_args$args;
}
```

### Checkliste beim App Server Setup

- [ ] `public/.htaccess` existiert
- [ ] `public/index.php` existiert (Symfony Front Controller)
- [ ] Apache hat `mod_rewrite` aktiviert
- [ ] `AllowOverride All` ist für das Verzeichnis gesetzt
