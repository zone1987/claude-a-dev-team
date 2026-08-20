# playwright-api-test

Erschoepfende API-Referenz aller Playwright Test Runner-Klassen mit vollstaendigen
Signaturen, allen Parametern (Name, Typ, Required, Default), Rueckgabetypen und Beispielen.

## Deep-Reference-Dateien

| Datei | Inhalt | Methoden/Felder |
|-------|--------|-----------------|
| [class-test.md](`API-TEST-CLASS-TEST.md`) | Alle test()-Methoden, Hooks, Modifier (skip/fail/slow/fixme), describe, step, use, extend | 39 |
| [class-testconfig.md](`API-TEST-CLASS-TESTCONFIG.md`) | Alle Top-Level-Felder der playwright.config.ts | 38 |
| [class-testproject.md](`API-TEST-CLASS-TESTPROJECT.md`) | Alle Felder eines projects[]-Eintrags inkl. expect-Sub-Felder | 20 + 14 |
| [class-testoptions.md](`API-TEST-CLASS-TESTOPTIONS.md`) | Alle use-Optionen (Browser, Netzwerk, Emulation, Recording) | 35 |
| [class-fixtures.md](`API-TEST-CLASS-FIXTURES.md`) | Built-in Fixtures + test.extend()-Muster (Scopes, Options, Auto) | 5 built-in |
| [class-testinfo.md](`API-TEST-CLASS-TESTINFO.md`) | Alle Methoden und Properties von TestInfo | 8 Methoden, 22 Properties |
| [class-testinfoerror.md](`API-TEST-CLASS-TESTINFOERROR.md`) | TestInfoError-Properties (Laufzeit-Fehler) | 5 |
| [class-teststep.md](`API-TEST-CLASS-TESTSTEP.md`) | TestStep: Methoden, Properties, category-Werte | 1 Methode, 10 Properties |
| [class-teststepinfo.md](`API-TEST-CLASS-TESTSTEPINFO.md`) | TestStepInfo: attach, skip, titlePath | 2 Methoden, 1 Property |
| [class-testcase.md](`API-TEST-CLASS-TESTCASE.md`) | TestCase (Reporter): ok, outcome, titlePath + alle Properties | 3 Methoden, 12 Properties |
| [class-testresult.md](`API-TEST-CLASS-TESTRESULT.md`) | TestResult: alle Properties inkl. steps, attachments, stderr/stdout | 13 Properties |
| [class-testerror.md](`API-TEST-CLASS-TESTERROR.md`) | TestError (Reporter): location, snippet + Vergleich zu TestInfoError | 6 Properties |
| [class-suite.md](`API-TEST-CLASS-SUITE.md`) | Suite-Hierarchie: allTests, entries, project, titlePath | 4 Methoden, 6 Properties |
| [class-reporter.md](`API-TEST-CLASS-REPORTER.md`) | Alle 11 Reporter-Hooks mit Signaturen und Beispielen | 11 Methoden |
| [class-fullconfig.md](`API-TEST-CLASS-FULLCONFIG.md`) | FullConfig: aufgeloeste Laufzeit-Konfiguration | 24 Properties |
| [class-fullproject.md](`API-TEST-CLASS-FULLPROJECT.md`) | FullProject: aufgeloeste Projekt-Konfiguration | 16 Properties |
| [class-timeouterror.md](`API-TEST-CLASS-TIMEOUTERROR.md`) | TimeoutError: instanceof-Nutzung, Abgrenzung | 0 eigene, erbt Error |
