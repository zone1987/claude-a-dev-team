---
name: playwright-api-locator
description: >
  Vollstaendige Playwright API-Referenz fuer Locator, FrameLocator und Selectors: jede
  Methode mit vollstaendiger Signatur, allen Parametern (Name/Typ/required/Default),
  Rueckgabetyp und kurzem Beispiel. Playwright Locator API class-locator class-framelocator
  class-selectors all methods getBy filter and or nth first last all contentFrame owner.
triggers:
  - playwright locator api
  - class-locator
  - class-framelocator
  - class-selectors
  - playwright locator methoden
  - locator all methods
  - playwright locator reference
  - locator signatur
  - playwright api locator
  - playwright framelocator api
  - playwright selectors api
  - playwright locator vollstaendig
  - playwright locator complete reference
  - locator api reference
  - playwright locator class
  - playwright framelocator class
  - playwright selectors class
  - playwright locator alle methoden
  - playwright locator parameters
  - playwright locator typescript
---

Erschoepfende API-Referenz fuer alle drei Klassen rund um Playwright-Locatoren.

## Enthaltene Klassen

- [references/deep/class-locator.md](references/deep/class-locator.md) — 57 Methoden
- [references/deep/class-framelocator.md](references/deep/class-framelocator.md) — 11 Methoden (incl. deprecated)
- [references/deep/class-selectors.md](references/deep/class-selectors.md) — 2 Methoden

## Manifest

| Klasse | Methoden/Properties | Fazit |
|---|---|---|
| Locator | 57 | Kernklasse fuer alle Element-Interaktionen; alle getBy*-Fabrikmethoden, Filterung, Komposition und Aktionen vollstaendig dokumentiert. |
| FrameLocator | 11 | Schmale Schnittstelle fuer iframe-Navigation; owner() und contentFrame() sind die modernen Alternativen zu den deprecated first/last/nth. |
| Selectors | 2 | Nur register() und setTestIdAttribute(); beide sind einmalig vor Seitenerstellung aufzurufen. |
