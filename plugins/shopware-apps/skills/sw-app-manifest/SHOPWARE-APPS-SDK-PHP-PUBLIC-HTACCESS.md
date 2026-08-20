---
title: App Server Public Directory & .htaccess
impact: HIGH
impactDescription: Every PHP/Symfony app server needs an .htaccess in the public directory so that Apache requests are forwarded correctly to the front controller (index.php).
tags: sdk, php, symfony, app-server, apache, htaccess, public
---

## .htaccess in the public directory

Every Shopware app server based on PHP/Symfony **MUST** contain an `.htaccess` file in the `public/` directory.

### Why is the .htaccess required?

- Apache forwards all requests to `public/index.php` (the Symfony front controller)
- Without `.htaccess`, URL routing does not work – all webhook and API endpoints are unreachable
- The file enables hosting under a subpath (e.g. `example.com/subpath`)
- The `HTTP_AUTHORIZATION` header (needed for HMAC verification) is passed through correctly

### Required structure

```
my-app-server/
├── public/
│   ├── .htaccess        ← REQUIRED for Apache
│   └── index.php
├── src/
├── config/
└── composer.json
```

### Example file

See `examples/public.htaccess` for the complete, commented reference file.

### Important functions of the .htaccess

| Directive | Purpose |
|-----------|-------|
| `DirectoryIndex index.php` | Front controller as the default index |
| `Options -MultiViews` | Prevents unwanted content negotiation |
| `RewriteRule .* - [E=BASE:%1]` | Determines the RewriteBase path dynamically (subpath support) |
| `E=HTTP_AUTHORIZATION:%0` | Ensures the Authorization header (Apache strips it otherwise) |
| `R=301` for `/index.php/` | Removes `/index.php/` from URLs |
| `RewriteCond %{REQUEST_FILENAME} !-f` | Forwards only non-existing files |

### Nginx alternative

With Nginx hosting the `.htaccess` is not needed. Instead, a `try_files` block is used directly in the Nginx configuration:

```nginx
location / {
    try_files $uri /index.php$is_args$args;
}
```

### Checklist for the app server setup

- [ ] `public/.htaccess` exists
- [ ] `public/index.php` exists (Symfony front controller)
- [ ] Apache has `mod_rewrite` enabled
- [ ] `AllowOverride All` is set for the directory
