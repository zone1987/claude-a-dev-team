---
name: panther-test
description: Scaffold eines Symfony-Panther-Tests aus einer Beschreibung — wählt den passenden Client (WebDriver für JS / KernelBrowser / HttpBrowser), baut Navigation, Formular-Interaktion, korrekte waitFor*-Aufrufe und Panther-/Web-Assertions; optional als Page-Object.
argument-hint: <beschreibung> z.B. "Login-Formular absenden und Dashboard prüfen" [--browserkit] [--js] [--pom]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /panther-test

Erzeuge einen lauffähigen Panther-Test. Skills: `panther-testcase`, `panther-client`, `panther-crawler`,
`panther-interactions`, `panther-javascript-screenshots`; bei `--browserkit` `panther-browserkit-clients`.

## Ablauf
1. Szenario aus `$ARGUMENTS` interpretieren; Client wählen:
   - JS/AJAX/Real-Time → `createPantherClient()` (echter Browser)
   - reine Server-/HTML-Prüfung → `createClient()` (KernelBrowser) oder `--browserkit` `createHttpBrowserClient()`
2. **Navigation/Interaktion:** `$client->request('GET', …)`, `$crawler->filter(...)`/`selectButton(...)`, `submitForm(...)`/`click(...)`.
3. **Warten (nur WebDriver/JS):** `waitForVisibility`/`waitForElementToContain`/`waitFor` mit korrekter Signatur statt `sleep()`.
4. **Assertions:** `assertSelectorTextContains`/`assertPageTitleSame`/`assertSelectorIsVisible`/… (`panther-testcase`).
5. `--pom` → Locators/Aktionen in eine Page-Object-Klasse kapseln.

Methoden/Signaturen gegen die (quellverifizierten) `panther-*`-Skills prüfen — Panthers Crawler unterstützt NICHT alle DomCrawler-Methoden. Keine `sleep()`-Hacks.
