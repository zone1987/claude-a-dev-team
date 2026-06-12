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

`sw-concept-api`, `sw-concept-app-system`, `sw-concept-architecture`, `sw-concept-catalog`, `sw-concept-checkout`, `sw-concept-content-cms`, `sw-concept-dal`, `sw-concept-data-stores`, `sw-concept-extensions`, `sw-concept-messaging`, `sw-concept-rule-system`, `sw-concept-translations`

## Agents (1)

- **`shopware-concepts`** — Shopware-6-Konzept-Berater. Beantwortet architektonische und konzeptionelle Fragen zu Shopware — "wie funktioniert X in Shopware", "was ist der Unterschied zwischen App und Plugin", "wie arbeitet der Cart", "wie funktion
