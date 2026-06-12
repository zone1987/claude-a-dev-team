# shopware-concepts

> Das „Warum" hinter Shopware: Architektur- und Domänenkonzepte.

`shopware-concepts` vermittelt das **„Warum"** hinter Shopware — die Architektur- und Domänenkonzepte, die den
konkreten How-to-Skills der anderen Plugins zugrunde liegen.

Enthalten sind die destillierten **Concept-Dokumente** der offiziellen Doku: die **Framework-Architektur** (Bundles,
DI, Adapter, Rule-System, Übersetzungen), das **Datenkonzept** (DAL als Idee, nicht als API), die **Commerce-Domänen**
(Catalog/Produkte, Checkout-Konzept, Content/CMS), das **API-Konzept** (warum drei APIs), das **Extension-/App-System**
und das **Messaging**. Diese Skills erklären Zusammenhänge und Entwurfsentscheidungen — ideal zum Einarbeiten und um
fundierte Architektur-Entscheidungen zu treffen.

Spezialist: **`shopware-concepts-guide`**. **Wann nutzen:** zum Verstehen der Hintergründe, beim Onboarding oder vor
größeren Architektur-Entscheidungen. Die konkrete Umsetzung liefern dann `shopware-data`, `shopware-framework`,
`shopware-checkout` usw.; die bindenden Entscheidungen vertieft `shopware-quality` (`sw-adr-knowledge`).

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-concepts@claude-a-dev-team
```

## Skills (12)

| Skill | Beschreibung |
|---|---|
| `sw-concept-api` | Shopware Admin API und Store API: Zweck, Unterschiede, Authentifizierung, Search Criteria |
| `sw-concept-app-system` | Shopware App-System im Detail: Manifest, Registration Handshake, Webhooks, App Scripts, Storefront-Assets, Payments, Rule Conditions, In-App Purchases |
| `sw-concept-architecture` | Shopware-6-Architektur-Konzept: Core, Storefront, Administration, API-first, Schichtentrennung |
| `sw-concept-catalog` | Shopware Produktkatalog: Products (Varianten, Properties, Options), Categories (Tree, SEO, CMS), Sales Channels (Domains, Navigation, Sichtbarkeit) |
| `sw-concept-checkout` | Shopware Checkout-Konzept: Cart (Struktur, Zustände, Berechnung), Orders (State Machines), Payments (Synchron/Asynchron, Handler) |
| `sw-concept-content-cms` | Shopware Shopping Experiences (CMS): Struktur (Page/Section/Block/Slot/Element), Content-Hydration, Headless-CMS, Cookie Consent Management |
| `sw-concept-dal` | Shopware Data Abstraction Layer (DAL): kein ORM, EntityRepository, Criteria, Translations, Versioning, Inheritance, Indexing |
| `sw-concept-data-stores` | Shopware Framework-Konzepte: Flow Builder, HTTP Cache, Elasticsearch, Migrations, System Checks, Storefront Components (ab 6.7.11) |
| `sw-concept-extensions` | Shopware Extensions: App vs. Plugin — Unterschiede, Einsatzgebiete, Cloud-Kompatibilität |
| `sw-concept-messaging` | Shopware Messaging (Symfony Messenger): Message Bus, Handler, Transport, asynchrone Verarbeitung |
| `sw-concept-rule-system` | Shopware Rule-System und Rule Builder: Rules, RuleScopes, Container Rules (AND/OR/NOT), Evaluation, Operatoren, Validierung |
| `sw-concept-translations` | Shopware Übersetzungssystem: DAL-Translations, Snippet-Dateien, Fallback-Sprachen, Built-in Translation System (ab 6.7), country-agnostic Snippets |

## Agents (1)

| Agent | Beschreibung |
|---|---|
| `shopware-concepts` | Shopware-6-Konzept-Berater. Beantwortet architektonische und konzeptionelle Fragen zu Shopware — "wie funktioniert X in Shopware", "was ist der Unterschied zwischen App und Plugin", "wie arbeitet der Cart", "wie funktioniert das Rule-System |
