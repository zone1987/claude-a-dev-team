---
name: sw-admin-map
description: Scans a Shopware 6 project for administration building blocks and writes a cached catalogue of modules, components, services, mixins, directives and filters.
argument-hint: [--custom-only]
allowed-tools: Read, Glob, Grep, Bash, Write, Task
model: haiku
---

# /sw-admin-map

Create or refresh the admin catalogue. Delegate to the `shopware-admin-mapper` agent (skill
`sw-data`).

## Steps
1. Scan scope: the core
   (`vendor/shopware/administration/Resources/app/administration/src/**`) plus custom code
   (`custom/plugins/*/src/Resources/app/administration/src/**`). With `--custom-only`, custom only.
2. Record the registrations: `Module.register`, `Component.register/override`, `addServiceProvider`,
   `Store.register`, `Mixin.register`, `Directive.register`, `Filter.register`, `extends *ApiService`.
   Per component also record its **props, events, slots (`<slot name>`) and Twig blocks
   (`{% block %}`)** and what it is for, including the Meteor `mt-*` and core `sw-*` components it
   uses or registers.
3. Write `.shopware-catalog/admin.md`, in sections: modules, components, services, stores, mixins,
   directives, filters, API services.
4. Head it with the scan date, scope and counts; print a short summary.

Scan with grep. Record only building blocks that really exist — never invent one.
