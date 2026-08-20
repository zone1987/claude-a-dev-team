# playwright-api-test

Exhaustive API reference of all Playwright test runner classes with complete
signatures, all parameters (name, type, required, default), return types and examples.

## Deep reference files

| File | Content | Methods/Fields |
|-------|--------|-----------------|
| [class-test.md](`API-TEST-CLASS-TEST.md`) | All test() methods, hooks, modifiers (skip/fail/slow/fixme), describe, step, use, extend | 39 |
| [class-testconfig.md](`API-TEST-CLASS-TESTCONFIG.md`) | All top-level fields of playwright.config.ts | 38 |
| [class-testproject.md](`API-TEST-CLASS-TESTPROJECT.md`) | All fields of a projects[] entry including expect sub-fields | 20 + 14 |
| [class-testoptions.md](`API-TEST-CLASS-TESTOPTIONS.md`) | All use options (browser, network, emulation, recording) | 35 |
| [class-fixtures.md](`API-TEST-CLASS-FIXTURES.md`) | Built-in fixtures + test.extend() patterns (scopes, options, auto) | 5 built-in |
| [class-testinfo.md](`API-TEST-CLASS-TESTINFO.md`) | All methods and properties of TestInfo | 8 methods, 22 properties |
| [class-testinfoerror.md](`API-TEST-CLASS-TESTINFOERROR.md`) | TestInfoError properties (runtime errors) | 5 |
| [class-teststep.md](`API-TEST-CLASS-TESTSTEP.md`) | TestStep: methods, properties, category values | 1 method, 10 properties |
| [class-teststepinfo.md](`API-TEST-CLASS-TESTSTEPINFO.md`) | TestStepInfo: attach, skip, titlePath | 2 methods, 1 property |
| [class-testcase.md](`API-TEST-CLASS-TESTCASE.md`) | TestCase (reporter): ok, outcome, titlePath + all properties | 3 methods, 12 properties |
| [class-testresult.md](`API-TEST-CLASS-TESTRESULT.md`) | TestResult: all properties including steps, attachments, stderr/stdout | 13 properties |
| [class-testerror.md](`API-TEST-CLASS-TESTERROR.md`) | TestError (reporter): location, snippet + comparison to TestInfoError | 6 properties |
| [class-suite.md](`API-TEST-CLASS-SUITE.md`) | Suite hierarchy: allTests, entries, project, titlePath | 4 methods, 6 properties |
| [class-reporter.md](`API-TEST-CLASS-REPORTER.md`) | All 11 reporter hooks with signatures and examples | 11 methods |
| [class-fullconfig.md](`API-TEST-CLASS-FULLCONFIG.md`) | FullConfig: resolved runtime configuration | 24 properties |
| [class-fullproject.md](`API-TEST-CLASS-FULLPROJECT.md`) | FullProject: resolved project configuration | 16 properties |
| [class-timeouterror.md](`API-TEST-CLASS-TIMEOUTERROR.md`) | TimeoutError: instanceof usage, distinction | 0 own, inherits Error |
