# Shopware 6 — ADR-Index (Architecture Decision Records)

149 ADRs aus dem Core-Repository, chronologisch. Jede ADR dokumentiert eine bindende Architekturentscheidung.
Quelle: shopware/shopware `adr/`.


## 2020

- **2020-06-25** — implement architecture decision records
- **2020-07-02** — control clone behavior
- **2020-07-02** — implement sales channel context token requirement
- **2020-08-12** — document template refactoring
- **2020-08-12** — implement app system inside platform
- **2020-08-14** — implement individual sorting
- **2020-08-14** — merchant registration
- **2020-08-21** — unified notification titles
- **2020-08-28** — import acl privileges from other roles
- **2020-09-08** — custom field label loading in storefront
- **2020-09-17** — the best practice to always re fetch the data after saving
- **2020-11-06** — creating events
- **2020-11-19** — dal join filter
- **2020-11-20** — add login required annotation
- **2020-11-25** — decoration pattern
- **2020-12-02** — removing api version

## 2021

- **2021-03-24** — nested line items
- **2021-05-14** — when to use plain sql or dal
- **2021-05-28** — introduce eslint on vue admin
- **2021-06-14** — introduce jest fail on console
- **2021-07-22** — move storefront scripts to head
- **2021-08-10** — storefront coding standards
- **2021-08-11** — make platform stand alone
- **2021-08-31** — refactor admin build process to webpack multi compiler mode
- **2021-09-06** — make core mail templates independent from storefront urls
- **2021-09-14** — technical concept custom entities
- **2021-09-22** — refactor theme inheritance
- **2021-10-01** — payment flow
- **2021-10-13** — refund handling
- **2021-10-21** — app scripting
- **2021-11-02** — preparing data for rule evaluation
- **2021-11-05** — adjust adr approval rules
- **2021-11-09** — increment pattern
- **2021-11-22** — merge e2e projects into a single project
- **2021-11-23** — add possibility for plugin to add a html file
- **2021-12-07** — admin extension api standards

## 2022

- **2022-01-05** — add feature flag support for storefront scss
- **2022-01-06** — custom app api endpoints
- **2022-01-20** — feature flags for major versions
- **2022-02-09** — controller configuration route defaults
- **2022-02-21** — rule scripting in apps
- **2022-02-24** — domain exceptions
- **2022-02-28** — consistent deprecation notices in core
- **2022-03-09** — reset class state during requests
- **2022-03-15** — extract data handling classes to extension sdk
- **2022-03-17** — new nested line items
- **2022-03-25** — available stock
- **2022-03-25** — base context factory
- **2022-03-25** — cache stampede protection
- **2022-03-25** — initial state id loader
- **2022-03-25** — prevent mail updates
- **2022-03-25** — profiler integrations
- **2022-03-25** — redis cart persister
- **2022-03-29** — specify priority of translations in dal write payloads
- **2022-04-06** — add default cms layouts to products and categories
- **2022-04-19** — integrate app into flow action
- **2022-04-28** — tax providers
- **2022-05-12** — remove static analysis with psalm
- **2022-05-23** — rule condition field abstraction
- **2022-06-17** — integrate app into flow event
- **2022-06-24** — add typescript support for storefront js
- **2022-06-27** — providing the admin extension sdk
- **2022-07-19** — blog concept
- **2022-07-21** — adding the storable flow to implement delay action in flow builder
- **2022-09-23** — add bootstrap util
- **2022-09-27** — vue 2.7 update
- **2022-09-28** — mapping of product area
- **2022-10-17** — hide and show cms content
- **2022-10-20** — deprecation handling during phpunit test execution
- **2022-10-20** — test structure
- **2022-11-09** — composer based web updater
- **2022-11-16** — deprecate csrf
- **2022-11-21** — replace drop shadow with box shadow
- **2022-11-25** — run lighthouse test ine2e env

## 2023

- **2023-01-10** — atomic theme compilation
- **2023-01-16** — npm packages pre release versions
- **2023-01-30** — image lazy loading
- **2023-02-01** — app script product pricing
- **2023-02-02** — deprecate autoload true in dal associations
- **2023-02-02** — flow storer with scalar values
- **2023-02-13** — follow test pyramid
- **2023-02-20** — unstructured adrs
- **2023-02-27** — native extension system with vue
- **2023-03-27** — admin text editor evaluation
- **2023-04-01** — mocking repositories
- **2023-04-03** — disable css autoprefixer
- **2023-04-11** — new language inheritance mechanism for opensearch
- **2023-04-14** — jest test files should be javascript only
- **2023-05-09** — optimise cart cleanup
- **2023-05-10** — experimental features
- **2023-05-15** — stock api
- **2023-05-16** — php enums
- **2023-05-22** — switch to uuidv7
- **2023-05-25** — exception log levels
- **2023-06-27** — store api to app server
- **2023-06-28** — default handle for non specified salutations
- **2023-07-13** — flow builder preview
- **2023-08-03** — collecting entity data
- **2023-08-17** — media path
- **2023-08-27** — post updater
- **2023-09-06** — feature property for experimental anotation
- **2023-10-17** — add unique identifiers for checkout methods
- **2023-10-19** — bootstrap css utils
- **2023-11-29** — toggle feature flag on demand
- **2023-12-12** — acceptance test suite

## 2024

- **2024-02-11** — transactional flow actions
- **2024-03-11** — disable vue compat mode per component level
- **2024-03-21** — implementation of meteor component library
- **2024-04-01** — checkout gateway
- **2024-06-12** — add jest runner with disabled compat mode
- **2024-06-17** — error code log level configuration in cloud and platform
- **2024-06-17** — replace vuex with pinia
- **2024-06-18** — extended event system
- **2024-07-16** — deprecating sdk public api
- **2024-07-30** — add telemetry abstraction layer
- **2024-07-31** — add more unit tests namespaces to featureflag extension
- **2024-08-02** — system health check
- **2024-09-26** — native block system
- **2024-10-02** — vue 2 options api to vue 3 composition api conversion codemod
- **2024-12-19** — offer html alternative to our pdf standard document

## 2025

- **2025-01-01** — remove asterisk next to every price
- **2025-01-29** — make rule classes internal
- **2025-01-31** — move flow execution after business process
- **2025-02-06** — deprecate iterator iterate
- **2025-04-01** — context gateway
- **2025-05-12** — implement measurement system
- **2025-06-03** — integrating the language pack into platform
- **2025-08-19** — cache layer for navigation loader
- **2025-09-01** — adding a country agnostic language layer
- **2025-09-05** — app requirements validation
- **2025-09-15** — store api cache strategy
- **2025-10-14** — colocate administration technical docs
- **2025-10-23** — pin npm dependencies
- **2025-10-28** — changelog release info process
- **2025-11-03** — improved http cache layer
- **2025-11-14** — introduce product type and deprecate states

## 2026

- **2026-01-28** — apply opensearch in admin api
- **2026-03-17** — mcp server placement and extensibility
- **2026-03-17** — refactor of document generation
- **2026-03-18** — app url verify utils
- **2026-03-18** — new document generation architecture
- **2026-03-19** — new document generation extension points
- **2026-04-14** — webhook outbox transport
- **2026-04-15** — keep administration top bar under shopware control
- **2026-04-16** — storefront component build time scss
- **2026-04-23** — telemetry v2 metrics evolution
- **2026-05-06** — split large administration test files
- **2026-05-13** — administration pr guidelines

## YYYY

- **YYYY-MM-DD** — template
