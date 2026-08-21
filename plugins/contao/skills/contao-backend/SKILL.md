---
name: contao-backend
description: Contao 5 backend: backend modules, backend routes, page controllers, routing, request tokens, response context. Use when building a Contao backend module or route.
---

# Contao backend

Extending the administration area, and the routing and CSRF machinery behind it.

## Reference map

- **[MODULES.md](MODULES.md)**: backend modules: registration, the `tables` option, loading a DCA, permissions, and the operations a module offers.
- **[ROUTES.md](ROUTES.md)**: backend controllers, the backend template, menu integration, and adding a route to an existing module.
- **[ROUTING.md](ROUTING.md)**: custom routes, request attributes, and content routing (Contao 5.3 and later).
- **[PAGE-CONTROLLERS.md](PAGE-CONTROLLERS.md)**: page controllers: both registration methods, every configuration parameter, URL generation, and a minimal example.
- **[REQUEST-TOKENS.md](REQUEST-TOKENS.md)**: CSRF tokens: generating, validating, outputting them in a template, and when protection may be disabled.
- **[RESPONSE-CONTEXT.md](RESPONSE-CONTEXT.md)**: the four-step response-context workflow, the core capabilities (HTML head, JSON-LD), and how a page controller creates one.

## Source

Distilled from [docs.contao.org/5.x](https://docs.contao.org/5.x) — the developer documentation and the German end-user manual — plus the [contao/contao](https://github.com/contao/contao) source, retrieved 2026-08-20.
