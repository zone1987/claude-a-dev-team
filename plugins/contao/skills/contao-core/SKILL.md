---
name: contao-core
description: Contao 5 fundamentals: bundle structure, Manager plugin, setup, coding standards, logging, profiler. Use when the request names Contao setup, a Contao bundle or the Manager plugin.
---

# Contao core concepts

How a Contao 5 extension is put together and how the framework boots it. Start here before any of the other Contao domains.

## Reference map

- **[GETTING-STARTED.md](references/GETTING-STARTED.md)**: the Managed Edition directory layout, every configuration file, autoloading, and how a project is wired together.
- **[INITIAL-SETUP.md](references/INITIAL-SETUP.md)**: installing the Managed Edition, its internals, and integrating Contao into an existing Symfony application.
- **[EXTENSION-BUNDLE.md](references/EXTENSION-BUNDLE.md)**: building an extension: `composer.json`, the development structure, path repositories for local work, and publishing.
- **[MANAGER-PLUGIN.md](references/MANAGER-PLUGIN.md)**: the Manager plugin and all its interfaces: `BundlePluginInterface`, config, routing, extension and dependent plugins.
- **[CONCEPTS.md](references/CONCEPTS.md)**: the ten concepts a Contao developer needs: DCA and models, front-end modules, content elements, hooks, templates and the rest.
- **[CODING-STANDARDS.md](references/CODING-STANDARDS.md)**: the coding standards, the tooling that enforces them, the namespace structure, and class-suffix conventions.
- **[LOGGING.md](references/LOGGING.md)**: system-log integration, `ContaoContext` actions, and the preconfigured logger services.
- **[MAINTENANCE.md](references/MAINTENANCE.md)**: writing a maintenance module and a purge task.
- **[PROFILER.md](references/PROFILER.md)**: the Contao profiler panel, its components, and when it is available.
- **[INTERNALS.md](references/INTERNALS.md)**: what the backward compatibility promise covers and the nine things
  it does not, the four experimental features and since when, the release stages and deadlines, the
  Contao Manager API with its four OAuth scopes, and the issue labels.
- **[REFERENCE-MISC.md](references/REFERENCE-MISC.md)**: the long reference, 988 lines: core services, events, console commands, `contao.yaml` configuration, environment variables and request attributes.

## Source

Distilled from [docs.contao.org/5.x](https://docs.contao.org/5.x) : the developer documentation and the German end-user manual : plus the [contao/contao](https://github.com/contao/contao) source, retrieved 2026-08-20.
