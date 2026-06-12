---
name: playwright-api-test
description: >
  Vollstaendige Playwright Test Runner API-Referenz: class-test (alle Modifier, Hooks,
  Steps, Fixtures, extend), TestConfig / TestProject / TestOptions (alle Felder),
  TestInfo / TestInfoError / TestStep / TestStepInfo, TestCase / TestResult / TestError /
  Suite (Reporter API), FullConfig / FullProject, TimeoutError. Playwright Test API,
  TestConfig reference, TestInfo, test.extend, Reporter API, Fixtures, class-test,
  Playwright test runner classes.
triggers:
  - Playwright Test API
  - class-test
  - test.extend
  - test.describe
  - test.step
  - TestConfig
  - TestProject
  - TestOptions
  - TestInfo
  - TestInfoError
  - TestStep
  - TestStepInfo
  - TestCase
  - TestResult
  - TestError
  - Suite reporter
  - Reporter API
  - FullConfig
  - FullProject
  - TimeoutError playwright
  - playwright fixtures
  - playwright built-in fixtures
  - playwright custom fixtures
  - playwright reporter
  - onBegin onTestEnd onEnd
  - playwright test runner classes
  - playwright API Referenz
  - playwright Klassen
  - playwright Fixtures erstellen
  - playwright Reporter schreiben
  - playwright Konfigurationsklassen
---

Erschoepfende API-Referenz aller Playwright Test Runner-Klassen mit vollstaendigen
Signaturen, allen Parametern (Name, Typ, Required, Default), Rueckgabetypen und Beispielen.

## Deep-Reference-Dateien

| Datei | Inhalt | Methoden/Felder |
|-------|--------|-----------------|
| [class-test.md](references/deep/class-test.md) | Alle test()-Methoden, Hooks, Modifier (skip/fail/slow/fixme), describe, step, use, extend | 39 |
| [class-testconfig.md](references/deep/class-testconfig.md) | Alle Top-Level-Felder der playwright.config.ts | 38 |
| [class-testproject.md](references/deep/class-testproject.md) | Alle Felder eines projects[]-Eintrags inkl. expect-Sub-Felder | 20 + 14 |
| [class-testoptions.md](references/deep/class-testoptions.md) | Alle use-Optionen (Browser, Netzwerk, Emulation, Recording) | 35 |
| [class-fixtures.md](references/deep/class-fixtures.md) | Built-in Fixtures + test.extend()-Muster (Scopes, Options, Auto) | 5 built-in |
| [class-testinfo.md](references/deep/class-testinfo.md) | Alle Methoden und Properties von TestInfo | 8 Methoden, 22 Properties |
| [class-testinfoerror.md](references/deep/class-testinfoerror.md) | TestInfoError-Properties (Laufzeit-Fehler) | 5 |
| [class-teststep.md](references/deep/class-teststep.md) | TestStep: Methoden, Properties, category-Werte | 1 Methode, 10 Properties |
| [class-teststepinfo.md](references/deep/class-teststepinfo.md) | TestStepInfo: attach, skip, titlePath | 2 Methoden, 1 Property |
| [class-testcase.md](references/deep/class-testcase.md) | TestCase (Reporter): ok, outcome, titlePath + alle Properties | 3 Methoden, 12 Properties |
| [class-testresult.md](references/deep/class-testresult.md) | TestResult: alle Properties inkl. steps, attachments, stderr/stdout | 13 Properties |
| [class-testerror.md](references/deep/class-testerror.md) | TestError (Reporter): location, snippet + Vergleich zu TestInfoError | 6 Properties |
| [class-suite.md](references/deep/class-suite.md) | Suite-Hierarchie: allTests, entries, project, titlePath | 4 Methoden, 6 Properties |
| [class-reporter.md](references/deep/class-reporter.md) | Alle 11 Reporter-Hooks mit Signaturen und Beispielen | 11 Methoden |
| [class-fullconfig.md](references/deep/class-fullconfig.md) | FullConfig: aufgeloeste Laufzeit-Konfiguration | 24 Properties |
| [class-fullproject.md](references/deep/class-fullproject.md) | FullProject: aufgeloeste Projekt-Konfiguration | 16 Properties |
| [class-timeouterror.md](references/deep/class-timeouterror.md) | TimeoutError: instanceof-Nutzung, Abgrenzung | 0 eigene, erbt Error |
