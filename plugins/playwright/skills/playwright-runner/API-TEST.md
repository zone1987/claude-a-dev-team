# playwright-api-test

Exhaustive API reference of all Playwright test runner classes with complete
signatures, all parameters (name, type, required, default), return types and examples.

## Deep reference files

| File | Content | Methods/Fields |
|-------|--------|-----------------|
| [API-TEST-CLASS-TEST.md](API-TEST-CLASS-TEST.md) | All test() methods, hooks, modifiers (skip/fail/slow/fixme), describe, step, use, extend | 39 |
| [API-TEST-CLASS-TESTCONFIG.md](API-TEST-CLASS-TESTCONFIG.md) | All top-level fields of playwright.config.ts | 38 |
| [API-TEST-CLASS-TESTPROJECT.md](API-TEST-CLASS-TESTPROJECT.md) | All fields of a projects[] entry including expect sub-fields | 20 + 14 |
| [API-TEST-CLASS-TESTOPTIONS.md](API-TEST-CLASS-TESTOPTIONS.md) | All use options (browser, network, emulation, recording) | 35 |
| [API-TEST-CLASS-FIXTURES.md](API-TEST-CLASS-FIXTURES.md) | Built-in fixtures + test.extend() patterns (scopes, options, auto) | 5 built-in |
| [API-TEST-CLASS-TESTINFO.md](API-TEST-CLASS-TESTINFO.md) | All methods and properties of TestInfo | 8 methods, 22 properties |
| [API-TEST-CLASS-TESTINFOERROR.md](API-TEST-CLASS-TESTINFOERROR.md) | TestInfoError properties (runtime errors) | 5 |
| [API-TEST-CLASS-TESTSTEP.md](API-TEST-CLASS-TESTSTEP.md) | TestStep: methods, properties, category values | 1 method, 10 properties |
| [API-TEST-CLASS-TESTSTEPINFO.md](API-TEST-CLASS-TESTSTEPINFO.md) | TestStepInfo: attach, skip, titlePath | 2 methods, 1 property |
| [API-TEST-CLASS-TESTCASE.md](API-TEST-CLASS-TESTCASE.md) | TestCase (reporter): ok, outcome, titlePath + all properties | 3 methods, 12 properties |
| [API-TEST-CLASS-TESTRESULT.md](API-TEST-CLASS-TESTRESULT.md) | TestResult: all properties including steps, attachments, stderr/stdout | 13 properties |
| [API-TEST-CLASS-TESTERROR.md](API-TEST-CLASS-TESTERROR.md) | TestError (reporter): location, snippet + comparison to TestInfoError | 6 properties |
| [API-TEST-CLASS-SUITE.md](API-TEST-CLASS-SUITE.md) | Suite hierarchy: allTests, entries, project, titlePath | 4 methods, 6 properties |
| [API-TEST-CLASS-REPORTER.md](API-TEST-CLASS-REPORTER.md) | All 11 reporter hooks with signatures and examples | 11 methods |
| [API-TEST-CLASS-FULLCONFIG.md](API-TEST-CLASS-FULLCONFIG.md) | FullConfig: resolved runtime configuration | 24 properties |
| [API-TEST-CLASS-FULLPROJECT.md](API-TEST-CLASS-FULLPROJECT.md) | FullProject: resolved project configuration | 16 properties |
| [API-TEST-CLASS-TIMEOUTERROR.md](API-TEST-CLASS-TIMEOUTERROR.md) | TimeoutError: instanceof usage, distinction | 0 own, inherits Error |
