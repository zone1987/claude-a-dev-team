# Plugin rules: Process, documentation and repository
## Contents

- [language-code-english-markdown-german: Code, identifiers, file names, comments and commits are English, and every Markdown file of a plugin is German](#language-code-english-markdown-german-code-identifiers-file-names-comments-and-commits-are-english-and-every-markdown-file-of-a-plugin-is-german)
- [no-semicolons-or-dashes-in-texts: No text a person reads contains semicolons or dashes, and a test checks it](#no-semicolons-or-dashes-in-texts-no-text-a-person-reads-contains-semicolons-or-dashes-and-a-test-checks-it)
- [assets-built-with-shopware-cli: Assets are built with shopware-cli and nothing else](#assets-built-with-shopware-cli-assets-are-built-with-shopware-cli-and-nothing-else)
- [ci-pipeline: CI pipeline with staged checks, tag-driven release and an enforced version match](#ci-pipeline-ci-pipeline-with-staged-checks-tag-driven-release-and-an-enforced-version-match)
- [changelog-and-upgrade-guide: The changelog is written in German from a git-cliff draft, and an upgrade guide is maintained](#changelog-and-upgrade-guide-the-changelog-is-written-in-german-from-a-git-cliff-draft-and-an-upgrade-guide-is-maintained)
- [git-workflow: Work happens on content-named feature branches in grouped Conventional Commits, merged by the owner and never pushed](#git-workflow-work-happens-on-content-named-feature-branches-in-grouped-conventional-commits-merged-by-the-owner-and-never-pushed)
- [every-decision-is-an-adr: Every decision is an ADR, and the ADR folder with its index is the rule book](#every-decision-is-an-adr-every-decision-is-an-adr-and-the-adr-folder-with-its-index-is-the-rule-book)
- [knowledge-in-adrs-claude-md-and-context-md: Knowledge lives in ADRs, CLAUDE.md and a local, unversioned CONTEXT.md](#knowledge-in-adrs-claude-md-and-context-md-knowledge-lives-in-adrs-claudemd-and-a-local-unversioned-contextmd)
- [a-new-request-is-recorded-before-it-is-followed: A new request is routed to its record before it is followed](#a-new-request-is-recorded-before-it-is-followed-a-new-request-is-routed-to-its-record-before-it-is-followed)
- [one-task-at-a-time: One task at a time with a measurable definition of done, features first, tests next, mutation testing last](#one-task-at-a-time-one-task-at-a-time-with-a-measurable-definition-of-done-features-first-tests-next-mutation-testing-last)
- [model-choice-and-subagents: The model is chosen per task, Opus work stays in the main session, and delegated agents own disjoint files](#model-choice-and-subagents-the-model-is-chosen-per-task-opus-work-stays-in-the-main-session-and-delegated-agents-own-disjoint-files)
- [licence-is-proprietary: The licence is proprietary and is checked by hand at the start of every piece of work](#licence-is-proprietary-the-licence-is-proprietary-and-is-checked-by-hand-at-the-start-of-every-piece-of-work)
- [images-are-licence-free: Every image is licence-free, documented, and marked when a machine made it](#images-are-licence-free-every-image-is-licence-free-documented-and-marked-when-a-machine-made-it)
- [measure-before-assuming: A margin is measured before it is assumed](#measure-before-assuming-a-margin-is-measured-before-it-is-assumed)
- [built-assets-are-not-committed: Built assets are not committed and a release archive is built with the storefront build](#built-assets-are-not-committed-built-assets-are-not-committed-and-a-release-archive-is-built-with-the-storefront-build)

## language-code-english-markdown-german: Code, identifiers, file names, comments and commits are English, and every Markdown file of a plugin is German

**Area:** documentation **Status:** accepted

> Earlier variant: older records wrote everything in English except the README (and some also the security policy), with ADRs, plans and other documentation in English. A still older variant wrote the ADRs, drafts, plans, README, security policy, changelog, upgrade guides and `CLAUDE.md` in German, with only the code English. The newest rule below replaces them.

### Context

The plugin is developed and operated by a German-speaking team for shops in German-speaking markets. Whoever maintains it reads the documentation in German. The client has set several times that all Markdown files are German. The earlier rule had only the README in German.

The global rule demands English code and English project documentation, so that everybody who takes over the code understands it. A reader who does not speak German loses not a word but the reasoning behind a decision, exactly in the comment that explains why a branch exists and in the test name that states the rule. For the code this rule stays unchanged: whoever reads it and cannot read German must not lose the knowledge behind a name.

ADRs, drafts, plans and the other documents have a different audience than the code: the people who decide and carry responsibility here. They work in German, and a trade-off is more precise in the mother tongue than in the second language. For a document whose only purpose is the reasoning, this loss weighs more than for an identifier. A comment explains too, but it lives in the code and is read together with it, so it stays English. The same holds for test names.

Mixing two languages in one repository is worse than either choice alone, which is why the split follows one clear line: German is what explains, English is what is executed.

Where the plugin is a middleware used by thin provider plugins written by other people, those people cannot be assumed to read German. The moment a German comment, identifier or file name enters the tree, the reasoning behind a decision becomes unreadable for exactly the people who have to extend it. The words are still there, the knowledge is gone.

A second failure appears in the form of multi-line prose comments. A comment that explains why a decision was taken lives next to code that changes. The code moves, the paragraph stays, and within a few releases the file carries a confident explanation of something that is no longer true. Reasoning does not belong in a place nothing verifies.

A third pressure comes from tooling. php-cs-fixer and Rector both ship rules that remove DocBlock tags they consider redundant, such as `@param` on a typed parameter or `@return` on a typed return. Left enabled, a formatting run silently strips the type information the project relies on for static analysis, and the next run strips a little more.

Finally, the code is not the only artifact that has to survive a handover. A session that is compacted or restarted loses everything that was not written down. `CONTEXT.md` is the one file that must let work resume without loss, which only holds if it is read first, written after and never trimmed for tidiness.

The plugin runs in shops of several languages, and a text written into PHP or Twig cannot be translated or checked.

### Decision

| What | Language |
|---|---|
| Code, identifiers (variables, parameters, functions, classes, methods, enums, types), PHP, JavaScript, Twig, SCSS | English |
| File and directory names | English |
| Comments, DocBlocks, DocBlock tags and the rare single-line note | English |
| Test names (PHPUnit, Jest and Playwright alike) | English |
| Commit messages and branch names | English |
| Every Markdown file: `README.md`, `CLAUDE.md`, `CONTEXT.md`, `CHANGELOG.md`, `SECURITY.md`, `UPGRADE-*.md`, `DEPRECATIONS.md`, `TODO.md`, everything under `docs/`, all ADRs, the index in `adr/README.md`, plans and specifications, Markdown under `tests/` | German |
| Snippets and texts in `config.xml` | the language of their file, keys are English |
| The conversation with the client or maintainer in the terminal | German, never part of the repository |

- The Markdown rule is German in every Markdown file, including the plugin rule files and drafts. A new or changed Markdown text is written in German at once, never translated later.
- ADRs use the sections `## Kontext`, `## Entscheidung` and `## Konsequenzen` (older variants used `Ausgangslage` and `Folgen`). The keys of the front matter and the values of `area` and `status` stay English because tools read them. ADR titles, tags and text are German.
- Class names, methods, configuration keys, routes, commands and paths stand in backticks and are not translated.
- Markdown file names are written in capitals with a lowercase extension (`README.md`, `UPGRADE-6.7.md`). ADR files follow the lowercase kebab pattern and stay English, because file and directory names are always English.
- German text always uses real umlauts (ä, ö, ü, ß) and never uses dashes as punctuation.
- Spelling in code and comments is US English: `optimization`, `catalog`, `canceled`, `fulfillment`, `color`, `behavior`.
- There is one changelog only (`CHANGELOG.md`). A second-language version is not maintained.
- The vendor prefix is the one of the plugin's own vendor (namespace and composer package, plus the database table prefix where one is defined). Prefixes of any other vendor or agency are forbidden anywhere in the repository. The prefix is not cosmetic: table names, class names and namespaces are the identifiers a Shopware installation resolves at runtime, and a foreign prefix is a collision waiting for the installation that also has that vendor's plugin.
- There are no prose comments and no copyright headers in classes. Reasoning goes to ADRs, to `CONTEXT.md` or to a test name that states the intent.
- Rules of the code and annotation set, each with a rule id and severity MUST:

| ID | Rule |
|---|---|
| R-001 | All code, identifiers, file names, comments, commit messages and branch names are English. Only the terminal conversation with the user is German. |
| R-002 | Spelling is US English. |
| R-003 | The vendor prefix is the plugin's own. Prefixes of any other vendor are forbidden anywhere in the repository. |
| R-004 | No prose comments. No multi-line explanations, reasoning, trade-offs or decision history in code. |
| R-005 | Permitted comments: single-line notes on non-obvious constraints, `TODO`/`FIXME` with a concrete reference, tool directives. |
| R-006 | Reasoning goes to the ADRs, `CONTEXT.md`, or a test name stating the intent. |
| R-007 | Every class, property and method carries the conventional DocBlock tags (`@class`, `@package`, `@param`, `@return`, `@throws`, `@var`). Tags only, never prose. The annotation style is decided in its own ADR. |
| R-007a | Whatever annotation or `extends` clause Shopware writes on a class of a given kind, the plugin writes too. Collections carry `@template`, `@extends EntityCollection<TElement>` and `@codeCoverageIgnore`. `getExpectedClass()` returns `@return class-string<X>`. Migrations carry `@internal`. The corresponding core class is checked before a new class kind is added. |
| R-007b | DocBlock tags sit on consecutive lines. No blank ` * ` separator lines inside a DocBlock, even where the core uses them. |
| R-007c | Whatever Shopware marks `@deprecated`, the plugin's code that uses or mirrors it carries the same annotation with the same target tag (`@deprecated tag:v6.8.0 - …`). Every occurrence is listed in `docs/DEPRECATIONS.md`. |
| R-007d | A deprecated core API is used only when no alternative exists. `phpstan-deprecation-rules` is active and fails the gate otherwise. |
| R-008 | Generic and shape types (`list<>`, `array<k,v>`, `Collection<>`) are given wherever they apply. Adding tags never removes type information. |
| R-009 | The php-cs-fixer rules and Rector rules that strip redundant DocBlock tags stay disabled. Two consecutive gate runs must leave the tags intact. |
| R-010 | `CONTEXT.md` is read before starting or resuming a task and updated after finishing one, with exact file paths, verification state and open points. |
| R-011 | `CONTEXT.md` is never shortened to save space. Completed items are marked done, not deleted. |

- On R-003: the vendor prefix of a private plugin carries exactly one vendor's marks.
- On R-004 to R-006: the rule is not "fewer comments". It is that explanation moves to a place that is reviewed and versioned as a decision: an ADR, `CONTEXT.md` or a test name. A test called `rejects_offer_without_delivery_to_destination` states the rule and fails when the rule stops holding. A paragraph above the method does neither.
- On R-007 and R-007a: measured against Shopware 6.7.14.0, `@class` appears zero times in the core and `@package` as a DocBlock only once, because the core uses the `#[Package]` attribute instead. The project deliberately requires the full tag set anyway, and that deviation is settled in the annotation style ADR and not reopened here. R-007a is the other direction of the same principle: where the core does write something (`@template` and `@extends` on collections, `@internal` on migrations), the plugin writes it too, in addition to its own tag set and never instead of it. Before adding a class kind the plugin does not yet have, the corresponding core class is opened and its structure copied.
- On R-007c and R-007d: mirroring Shopware's deprecation markers verbatim, target tag included, turns the 6.8 upgrade into `grep -rn "@deprecated tag:v6.8" src/` instead of a survey. `docs/DEPRECATIONS.md` is the single list that upgrade works through.
- On R-009: the two fixer families that strip "redundant" DocBlock tags directly contradict R-007 and R-008. They stay disabled, and the check is empirical: two consecutive gate runs must leave the tags byte-identical. A single run proves nothing, because a fixer that removes one tag per pass looks stable until the second pass.

Locales and origin of texts:

- Every text a person reads comes from snippets: administration snippets, storefront snippets, labels in `config.xml` and the texts of exceptions and notifications.
- Administration snippets are shipped in `de-DE` and `en-GB` with identical key sets. Storefront snippets are likewise shipped in `de-DE` and `en-GB` with identical key sets.
- Snippet keys are English and follow the core schema. The values stand in the language of the file.
- A new key goes into every language file in the same change. Tests compare the key sets.
- Other languages fall back to the core's fallback chain until a new ADR adds them.

### Consequences

The documentation is directly readable for operators and developers in the house. Whoever does not read German still understands the code, the identifiers, the comments, the commit history and the state of the plugin, but not the reasoning of the ADRs. This is accepted on purpose, because the plugin is maintained by a German-speaking team. Whoever switches between this plugin and a neighbor that uses another documentation language notices the change, and is meant to.

A test checks the German ADR sections. An English ADR or Markdown file that is newly added is a defect and is translated at once. A German test name or comment that slips in is a defect like any other and is corrected when noticed.

Every contributor can read the code, including a provider-plugin author who has never spoken to the maintainer. Reviews cite stable identifiers (R-001 through R-011) instead of restating preferences, and a disagreement about style becomes a disagreement about a numbered rule with a written justification.

Code review becomes cheaper in one direction and stricter in another. There is less to read in the files, because reasoning is not interleaved with implementation. But a reviewer must check that the reasoning actually landed somewhere (an ADR, `CONTEXT.md` or a test name) rather than accepting a deleted comment as an improvement.

The cost is real and falls in three places. Writing the full tag set on every class, property and method is more typing than the core requires, and PHPStan does not catch a missing `@class` or `@package`, so R-007 needs review attention or a custom sniff. Keeping the strip-tags fixers disabled means the project cannot adopt an upstream php-cs-fixer or Rector rule set wholesale, and every tooling upgrade has to be checked against R-009, with the two-consecutive-runs test as the check. And `CONTEXT.md` grows without bound by construction (R-011). That is accepted: length is not a defect, loss is.

US spelling (R-002) is enforceable with a word list in CI. The vendor-prefix rule (R-003) is enforceable with a grep over table names, namespaces and documentation. The language rule (R-001) is not mechanically enforceable beyond obvious cases and remains a review obligation. `phpstan-deprecation-rules` enforces R-007d automatically and fails the gate. R-007c is a review obligation paired with the `docs/DEPRECATIONS.md` list.

German and English shops are complete from the start, and a missing snippet key is a red test instead of a gap in the interface.

## no-semicolons-or-dashes-in-texts: No text a person reads contains semicolons or dashes, and a test checks it

**Area:** documentation **Status:** accepted

### Context

Dashes used as punctuation and semicolons in prose usually replace a decision about how two parts of a sentence relate to each other. They are a recognizable trait of machine-generated text, they stand out in documents sent to clients, and they read clumsily in short interface texts. Help texts and messages in the administration and storefront had contained semicolons, for example a help text that read "Choose granted only if ... applies. When in doubt, leave it declined." Where such a character stands, the decision is usually missing whether a new sentence, a list or a justification is meant.

### Decision

- The en dash and the em dash are never used, neither in code, comments, documents, commit messages, snippets nor ADRs.
- No text a person reads contains a semicolon. This applies to labels, help texts, placeholders, titles and options in `config.xml`, to administration and storefront snippets in every language, to texts rendered from code and shown to people (exception messages, notifications, default descriptions of services and groups), to documentation, ADRs, `CLAUDE.md` and commit messages.
- Instead: a period that turns the sentence into two sentences, a colon before an explanation, a comma for a short aside, parentheses for a side remark.
- Allowed: the hyphen in compound words, identifiers, paths and commands, number ranges where a format demands them (the copyright years in `LICENSE`), and semicolons as syntax in PHP, JavaScript, SCSS, SQL and JSON.
- `CodingStyleTest` checks dashes in all text files, semicolons in Markdown prose, and semicolons and dashes in the texts of `config.xml` and in every value of the snippet JSON files. The snippet convention spec additionally checks the administration snippets.
- New texts are checked before the commit. Before every completion the files are checked with `grep` for these characters, and a hit is corrected at once, not later.

### Consequences

Texts state how their parts relate to each other, and the rule is checked by machines, not by reviewers. A test reads all snippet files and `config.xml` and fails as soon as a text contains a semicolon or a dash.

## assets-built-with-shopware-cli: Assets are built with shopware-cli and nothing else

**Area:** devops **Status:** accepted

### Context

Ad-hoc builds with webpack or npm and wrapper scripts produce output that differs from what Shopware produces, differs between machines, breaks on Shopware updates and does not limit a build to one plugin.

### Decision

- The administration is built with `shopware-cli project admin-build --only-extensions <PluginName>`.
- The storefront is built with `shopware-cli project storefront-build --only-extensions <PluginName>`.
- No `bin/build-*.sh`, no direct `npm run build` as a deliverable, no committed build output that was produced in another way.
- The plugin ships no bundler configuration. The entry points are `src/Resources/app/administration/src/main.js` and `src/Resources/app/storefront/src/main.js`.
- `npm` in the app folders is used only for linting and Jest.
- The gate, the end-to-end setup and the release process call the same commands. Caches are cleared after template or service changes.

### Consequences

One documented command per bundle delivers the same assets in every shop and every environment.

## ci-pipeline: CI pipeline with staged checks, tag-driven release and an enforced version match

**Area:** devops **Status:** accepted

### Context

The plugin should be verifiable in a GitLab pipeline, and releases should be produced by tagging rather than by hand.

Two conflicting needs had to be balanced. Running the full suite on every merge into the main branch (`6.7`) is wasteful, because Playwright alone needs a running shop and several minutes. Running nothing until a tag is worse in a different way: with twenty merges between two tags, a failure points at twenty changes instead of one, and the sourcing golden master tests are exactly where a silent regression hides.

A second problem is version drift. Shopware requires a `version` field in `composer.json` for plugin management, so it cannot be removed. If a tag says `1.3.16` and the field still says `1.3.15`, the built artifact is mislabelled and the mistake surfaces only at install time.

### Decision

**Staged execution.**

| Check | Merge into `6.7` | Tag |
|---|---|---|
| Version match | no | first, aborts everything on mismatch |
| ECS, Rector (dry run) | yes | yes |
| PHPStan, Deptrac | yes | yes |
| PHPUnit unit | yes | yes |
| PHPUnit integration | no | yes |
| Playwright E2E | no | yes |
| Build, package, release | no | yes |

The fast path runs in roughly two minutes and catches most regressions at the commit that caused them. Everything requiring a database or a browser is deferred to the tag.

**Version match.** The `verify` stage compares `CI_COMMIT_TAG` (with an optional `v` prefix stripped) against the `version` field in `composer.json` and fails the pipeline before any other job starts.

**Release on tag.** `shopware-cli extension build --only-extensions` followed by `extension zip` produces the installable artifact. The package is published to the GitLab Composer registry, and a GitLab release is created with the changelog and the ZIP attached.

**Tag cleanup on failure.** A `.post` job deletes the tag when the pipeline failed, so the same version can be tagged again after a fix. It requires a project access token with `write_repository` in the CI variable `GIT_PUSH_TOKEN`. Without the token the job reports what to delete manually and exits successfully rather than failing the pipeline a second time.

**Portability.** No job invokes `ddev`. Configuration comes from environment variables, and Shopware is provided by the official Docker image with MySQL as a service.

### Consequences

- Easier: regressions surface at the merge that caused them, tagging produces a complete, verified release without manual steps, and a mislabelled artifact cannot be built.
- Harder: integration and E2E failures appear only at tag time, so a tag may need to be cut twice. That is the accepted trade-off for short merge pipelines.
- The cleanup job writes to the repository. A tag can therefore disappear on failure. The job logs why, and it is deliberately a no-op when the token is absent.
- `version` in `composer.json` must be raised before tagging. It is the one manual step of a release.

## changelog-and-upgrade-guide: The changelog is written in German from a git-cliff draft, and an upgrade guide is maintained

**Area:** documentation **Status:** accepted

> Earlier variant: git-cliff generated `CHANGELOG.md` from the Conventional Commits and any manual edit was forbidden. Other plugins kept an English `CHANGELOG.md` (one changelog only, no second-language version). That position is replaced by the rule below, because every Markdown file is German.

### Context

The earlier rule let git-cliff generate `CHANGELOG.md` from the Conventional Commits and forbade any manual editing. Since every Markdown file is German (see the language rule), explicitly including `CHANGELOG.md`, and commit messages stay English, a generated changelog would consist of English lines and violate the language rule, while a German changelog would be overwritten on the next run of `composer changelog`. Both rules cannot be followed at the same time.

### Decision

- `CHANGELOG.md` is German and follows the layout of Keep a Changelog (Hinzugefügt, Geändert, Behoben, Entfernt, Sicherheit). It is extended in the same change that a merchant notices, under `## [Unveröffentlicht]`, and is moved under the version number at release.
- `composer changelog` produces with git-cliff (`cliff.toml`) only a draft of the unreleased commits on standard output and writes no file. The draft serves as a completeness check: every commit visible to merchants appears as a German line in the changelog. The command runs on the host.
- Commit messages are still written so that merchants understand them, because they are the basis of the draft.
- Fixed security vulnerabilities appear in `CHANGELOG.md` under `Sicherheit` with the affected and the correcting version.
- `docs/UPGRADE-6.7.md` lists every 6.6 API that the plugin uses or mirrors and that 6.7 marks as deprecated, removes or replaces, with the replacement and the affected file: administration (Vuex to Pinia, webpack to Vite, Meteor components), PHP signatures and the PHP version. It is updated in the same change that touches such an API.
- `docs/DEPRECATIONS.md` lists used deprecated core elements, deprecations of the plugin itself and breaking changes.
- A release is tagged to match the version in `composer.json` and the entry in `CHANGELOG.md`.

### Consequences

The changelog is written in the language of its readers and is no longer overwritten by accident. In return, a line can be missing if it is forgotten at commit time. The git-cliff draft makes such gaps visible before a release. The move to the next Shopware minor version still begins with a list instead of a search.

## git-workflow: Work happens on content-named feature branches in grouped Conventional Commits, merged by the owner and never pushed

**Area:** process **Status:** accepted

> Earlier variant: older records let the agent merge a finished feature locally with `--no-ff` into the main branch (after a green gate), and one record said every git operation that writes is performed by the plugin owner without exception. Another record split the work into a time-limited initial phase in which commits, branches, checkouts and merges were allowed on request, and a permanent second phase after the handover to review in which every writing git command belongs to the owner. The newest rule below wins: the agent commits on feature branches, the user merges into the main branch, and nothing is ever pushed.

> Earlier variant: the agent asked once before the first commit of a project whether committing was wanted, and a "no" was binding for the whole project. The newest rule commits on a feature branch without asking.

### Context

Work that goes directly to the main branch or to a remote cannot be reviewed or undone cleanly. A single collective commit at the end hides which change belongs to which area. A branch named after a work phase says nothing about its content a month later, which the owner has corrected.

The plugin comes into being in successive steps. Every step should be traceable and reversible. The user decides about merging and publishing. A commit that somebody else sets in the owner's name takes the decision away from the one who carries its consequences. The line is drawn where reversibility ends: a local commit can be rewritten, a push cannot.

The main branch (named after the Shopware minor version the plugin targets, for example `6.7`) is the branch an installation is expected to be able to check out and run. If work also happens on it, every intermediate state (a half-migrated entity, a service that no longer compiles, a red test) is briefly the released state. There is no window in which that is safe, because the plugin is consumed as a static plugin from the tree rather than from a tagged artifact. Plugins installed in selling shops reach shops that are selling, so seeing exactly which commit introduced a behavior is not a nicety. A history where a feature arrives as one traceable unit and every commit says why rather than what makes a change safe to ship and possible to undo.

History is the second concern. A plugin whose decisions must stay explainable cannot afford a commit log in which a feature is a shapeless run of fixups spread across unrelated modules. Conventional Commits with the module name as scope make the log queryable: what changed in a module, when and as part of which feature. `--no-ff` keeps the feature's commits grouped under a merge commit instead of flattening them into the trunk, so the grouping survives.

The generated changelog (`cliff.toml`, see the changelog rule) is built from the commit messages, so the messages are part of the release documentation.

The tooling constraint is sharper than it looks. A plugin that mirrors Shopware core conventions closely (annotations, `final` placement, service definition format) is only checked meaningfully if the static analysis is the same analysis the core runs. A newer php-cs-fixer changes formatting the core does not have, and a newer PHPStan reports on core code paths the core itself accepts. Shopware 6.7.14.0 declares php-cs-fixer 3.95.15, phpstan 2.2.8, phpat 0.12.4 and rector/type-perfect 2.1.4, and those are the versions pinned.

PHPUnit is a special case, learned the hard way: two PHPUnit versions in one tree break the event subscribers. The plugin lives inside a Shopware installation that already has PHPUnit in `vendor/`. A second copy under the plugin's own `vendor/` produces two sets of PHPUnit event classes, and the subscriber registration that Shopware's test bootstrap relies on silently binds against the wrong one.

### Decision

| Rule | Content |
|---|---|
| Branches | The main branch is never worked on directly. Every task has its own branch that forks from the main branch. A feature branch the maintainer created is used and no other branch is created, checked out or rewritten |
| Branch names | Named after their content: `feature/<topic>`, `fix/<topic>`, `refactor/<topic>`, `docs/<topic>`, using the module names of the plugin as topic (`feature/sourcing`, `fix/pricing`). Never after waves, phases or sprints |
| Commit messages | Conventional Commits in English with the types `feat`, `fix`, `refactor`, `test`, `docs`, `build`, `chore` (and `style`), an optional scope (the module name) and a subject in the imperative. The body says why, because what the code does is visible in the diff |
| Commit size | Committed in between, in sensible blocks: one logical change per area, one commit per finished task that bundles everything belonging to it, never one commit per file and never a collective commit at the end |
| Precondition | No commit of code without a green gate (`composer gate`). An unfinished task is not committed. The working tree may be unclean between commits, the branch never |
| Merge | The user merges into the main branch, not the agent. The merge is done with `--no-ff` and the branch is deleted afterwards. The merge commit is the unit of a feature and turns a revert into one step |
| Where | Commit only on a feature branch. On `main`, `master`, `trunk` or a release branch nothing is committed: branch first, or leave the work uncommitted and say so |
| Push | Never. Not even when a remote exists, as long as the user does not ask for it explicitly. Not once, not "just this branch", not after a green gate. Nothing that reaches a remote is run either. The work stays in the plugin repository. Push is the one rule that is absolute because it is the only step that cannot be quietly undone once somebody else has fetched. Commit, rebase and reset all stay locally repairable. Within these rules the ordinary writing commands (`add`, `commit`, `branch`, `rm --cached`) are available, outside them nothing is written |
| History | Published history is never rewritten |
| Changelog | `composer changelog` builds a draft from the commit messages (git cliff). The commit messages are therefore written so that merchants can read them |
| Releases | Releases are tagged to match the version in `composer.json` and the entry in `CHANGELOG.md`. A shop reporting a bug names a version, and that version has to be findable |
| `CONTEXT.md` | Never committed |
| Gate | No merge without a green gate. A red gate is reported, never worked around, never merged "just this once" |
| Other branches | A leftover branch such as `develop` from an initial commit may remain but is not used as a target |

Numbered rules (MUST):

| ID | Rule |
|---|---|
| R-101 | Never commit directly to the main branch. Work happens on feature branches. |
| R-102 | Branch names use the module names of the plugin: `feature/sourcing`, `fix/pricing`. |
| R-103 | Commits follow Conventional Commits, in English, scope = module name. |
| R-104 | Merge into the main branch with `--no-ff` and delete the branch afterwards. |
| R-105 | No merge without a green gate. A red gate is reported, never worked around. |
| R-106 | Tooling matches the targeted Shopware release exactly: php-cs-fixer 3.95.15, phpstan 2.2.8 with the deprecation, phpunit, strict-rules and symfony extensions, phpat 0.12.4, rector/type-perfect 2.1.4. The release tag's `composer.json` is checked before a version is changed. |
| R-107 | PHPUnit comes from the project (`../../../vendor/bin/phpunit`), never from the plugin. Two PHPUnit versions in one tree break the event subscribers. |

The full cycle, as it is actually run:

```bash
git checkout -b feature/<module>       # module names of the plugin
# work, commit with conventional commits
ddev exec composer gate                # must be green
git checkout 6.7
git merge --no-ff feature/<module>
git branch -d feature/<module>
```

- On R-103: English and the module name as scope, for example `feat(sourcing): add branch-and-bound optimizer`, `fix(pricing): prevent rounding drift in landed cost`, `docs(adr): decide provider coupling`.
- On R-105: "Reported, never worked around" is the operative half. A red gate is a finding, and the finding is stated. It is not silenced with a baseline entry, an inline ignore or a narrowed test selection, unless that suppression is itself the reviewed change. The composition of the gate is described in the CI rule.
- On R-106: versions are pinned exactly, `"phpstan/phpstan": "2.2.8"` and not `"^2.2"`. A gate that passes today and fails tomorrow because a patch release changed a rule is a gate nobody trusts. Upgrades are deliberate acts with the diff read. The version numbers are not preferences and are not rounded. Before changing any of them, the `composer.json` of the Shopware release tag the plugin targets is opened and the constraint read there. If the core moves, this rule moves with it and does not drift ahead of it.
- On R-107: the invocation is `../../../vendor/bin/phpunit`, the installation's binary reached from the plugin directory. PHPUnit is never added to the plugin's own `require-dev`.
- The conventions describe what the owner and the agent do. They are not a licence for anyone else to write to the history.

### Consequences

The main branch is always in a state that has passed the gate, because nothing reaches it except through a merge that required one. Bisecting is meaningful, since each merge commit is a complete feature rather than an arbitrary midpoint. The log answers "what happened to pricing" with a scope filter instead of a reading exercise. The history tells per area what happened, the changelog is generated from it, and a faulty feature can be reverted as a whole. Publishing is a deliberate act of the owner. Because nothing is ever pushed, the work exists only locally until the user publishes it.

The branch history is part of the release: a sloppy message becomes a sloppy changelog line that a customer reads. Conventional Commits are a discipline with no tooling behind them unless a commit-message hook or CI lint step is added. They are kept because the changelog draft is built from them.

What becomes harder is the small change. A one-line typo fix still costs a branch, a conventional commit, a green gate and a `--no-ff` merge. R-101 has no size exemption, and adding one would immediately be the exemption every change claims. The gate itself is the main friction, and it is deliberate friction: the moment a red gate can be merged "just this once", R-105 stops meaning anything and the branch's guarantee goes with it. If the gate becomes slow enough to tempt anyone to skip it, the gate gets faster and the rule does not get softer. Requiring a green gate before every merge makes the gate a bottleneck.

`--no-ff` produces merge commits in the history that a fast-forward workflow would not have. That is the intent: they are the unit of a feature. Branch-per-change means more branches than a small plugin strictly needs, and it means the main branch never holds half a feature, which is what allows it to be releasable at all times.

Enforcement splits cleanly. R-101 and R-104 are enforceable by branch protection on the main branch requiring a merge and a passing check. R-103 is enforceable by a commit-message hook or a CI lint step. R-105 is the CI check itself. R-106 is enforceable by pinning exact versions in `composer.json` and by a CI step that diffs the declared versions against the Shopware release tag. Without that step it degrades into a periodic manual audit. R-107 is enforceable by asserting that the plugin's own `vendor/bin/phpunit` does not exist and that the composer scripts point at the project binary. R-102 remains a review obligation, since the valid module names come from the plugin's module list rather than from anything a hook can read.

A commit written on request can be wrong in message or cut. It is corrected by rewriting, which is possible exactly as long as nothing has been pushed.

## every-decision-is-an-adr: Every decision is an ADR, and the ADR folder with its index is the rule book

**Area:** process **Status:** accepted

### Context

Many decisions shape a plugin: architecture, tools, rules. Reasons get lost when they live in a chat history or in the head of a single person, and a silently changed decision is worse than a wrong one. A rule that stands only in `CLAUDE.md` has no reasoning.

### Decision

- Every decision and every rule is written as an ADR in `adr/` when it is made, not only after the implementation.
- File name `YYYY-MM-DD-kebab-title.md`. Front matter `title`, `date`, `area`, `tags`, `status`, then `supersedes` or `superseded-by` where they apply. Sections Kontext, Entscheidung, Konsequenzen. German and concise (see the language rule).
- Allowed `area` values: core, storefront, administration, devops, process, documentation, legal, security, sync, api, data.
- An accepted ADR is never edited. A changed decision gets a new ADR. The old one is moved to `adr/_superseded/` with `status: superseded` and `superseded-by: ../<new file>`, and the new one carries `supersedes: _superseded/<old file>`.
- No two active ADRs treat the same topic. An ADR that treats a topic only in part is replaced by a merged ADR.
- An ADR argues only from the context of its own plugin and names no other plugin.
- `adr/README.md` is the index: a table with decision and area, sorted alphabetically by title, that lists every active ADR exactly once.
- The ADRs of an area are read before that area is changed.
- The ADR folder is the complete rule book. `CLAUDE.md` summarizes it and points to it. A rule that stands only in `CLAUDE.md` has no reasoning and is moved into an ADR.
- `CodingStyleTest` checks file name, front matter, allowed areas, sections, the index and the consistency of `supersedes` and `superseded-by`.

### Consequences

The history of a decision stays readable, and a rule change costs one new file. Code that contradicts an accepted ADR is wrong even if it works, and when an ADR and `CLAUDE.md` contradict each other, the ADR wins.

## knowledge-in-adrs-claude-md-and-context-md: Knowledge lives in ADRs, CLAUDE.md and a local, unversioned CONTEXT.md

**Area:** process **Status:** accepted

> Earlier variant: `CONTEXT.md` was committed together with the plugin, and the knowledge was split across ADRs, `CLAUDE.md` and a committed context file. That variant is replaced by the unversioned file below.

### Context

A session can end at any time through compression or restart. Knowledge that stands only in the conversation is lost. Until now `CONTEXT.md` was committed with the plugin. The file contains development knowledge such as local paths, names of other projects and the course of the work. That does not belong in the repository of a plugin that runs in many shops.

### Decision

- ADRs contain decisions and their reasons.
- `CLAUDE.md` contains the rules and commands for every session. Its first rule describes how to handle `CONTEXT.md`.
- `CONTEXT.md` contains state, proven facts, history and pitfalls. It lives in the plugin directory, is listed in `.gitignore` and is never committed.
- `CONTEXT.md` is exempt from the name checks of `CodingStyleTest`, because it carries local development knowledge.
- No credentials stand in any of these files or anywhere in the repository. They live in the plugin configuration or in `.env.local` and are named only by their variable name.
- Only the leading session writes `CONTEXT.md`.

### Consequences

The work can be continued from the local files. Whoever clones the repository anew has no `CONTEXT.md` and starts with the ADRs and `CLAUDE.md`. Older commits still contain the file, new ones no longer.

## a-new-request-is-recorded-before-it-is-followed: A new request is routed to its record before it is followed

**Area:** process **Status:** accepted

> Earlier variant: an older record wrote every new request, question or finding into `TODO.md` first and finished the running task before touching it. The newest rule routes the request to the place that fits its kind (ADR, `CLAUDE.md`, `CHANGELOG.md`, `CONTEXT.md`) instead of a single to-do file. The older variant is kept below in its reasoning and in its rules for finishing a task.

### Context

Requests that arrive during the work get lost easily when a session is compressed or an agent is replaced.

Work on a plugin arrives while other work is running. A screenshot of something broken, a new requirement, a question about a field, a fault noticed in passing: all of it lands mid-task, and all of it is genuinely worth doing. Following it immediately is the natural response and the wrong one. Three things went wrong that way.

**Branches stopped meaning anything.** 93 files from five unrelated subjects (images, destinations, the buy box, the accordion, the sync lock) ended up on one branch named after none of them, because each new subject was picked up where it appeared. Sorting that out afterwards produced twenty merge conflicts and cost more than doing it in order would have. A second branch cut while the first was still open is cut from whichever base happened to be checked out, which is how that began.

**Half-finished work hides what is missing.** It passes its tests, renders and looks done. The gallery accordion rendered nothing but its empty state while 58 specs stayed green. Five products were buyable for nothing while every test passed. Work abandoned at "the code works" is indistinguishable from work that is finished, and the difference only shows in production.

**A request nobody wrote down is a request nobody does.** The map sat in `TODO.md` for slices under a description that turned out to be wrong. The meeting-point import was recorded as broken when it was not. Both were only recoverable because they were written down at all. The cost of writing is a minute, the cost of forgetting is the whole item.

### Decision

- A new instruction, correction or decision is acknowledged and written down before work on it begins. Then the running task continues.
- Routing: a decision goes into an ADR, a working rule into `CLAUDE.md`, a change visible to merchants into `CHANGELOG.md` (via its commit message), state and next steps into `CONTEXT.md`. A lasting instruction of the user additionally goes into section 2 of `CONTEXT.md`.
- A change to `CLAUDE.md` is made at once.
- A correction by the user is recorded with its reason, and the affected files are reworked, not patched.

A new request, question or finding that arrives during a running task is written down first (in `TODO.md` where a plugin keeps one), and the running task is then finished before it is touched.

Written down means: what it is, what was already established about it, and the next concrete step, enough that a session starting cold can pick it up. Not a one-line reminder.

Finished means: the gate is green, `CLAUDE.md` carries what the task taught, the work is committed, merged and the branch is deleted. Not "the code works".

Two things interrupt a running task and nothing else does:

- A change to `CLAUDE.md`. That file outranks the work, so it is carried out at once.
- An emergency the user names as one. The user decides that, not the model.

Investigating far enough to write a useful entry is part of recording it and not a breach of this decision. Reading a value out of the database to describe a fault precisely is recording. Fixing it is not.

### Consequences

Instructions survive compression and agent changes. Recording takes a minute and prevents repeating a mistake.

Every finding is on the list, in order, with its evidence beside it. The list grows faster than it shrinks for a while, and that is the honest picture rather than a symptom.

Some items are recorded and never done, because by the time they come up they no longer matter. That is cheaper than the alternative, and it is visible: an item that has sat unchanged through several slices is asking to be dropped rather than deferred again.

The user sees a delay between asking and getting. It is paid back in branches that carry one subject, merges that do not conflict, and work that is done when it is called done.

This decision applies to the model's own curiosity too. Noticing an interesting adjacent fault mid-task and pulling at it is the same failure as following a new request, and it is recorded like anything else.

## one-task-at-a-time: One task at a time with a measurable definition of done, features first, tests next, mutation testing last

**Area:** process **Status:** accepted

> Earlier variant: one record demanded a specification and a failing test before every implementation (test first, with a failing test written before the class), and one wanted a brief and a plan (`superpowers:brainstorming`, `writing-plans`, `executing-plans`) before any code. The newest rule orders the work as all features first, then all tests, then mutation testing, and keeps the brief, plan and ADR as written artifacts.

> Earlier variant: mutation testing ran only when the maintainer said so, and a running mutation test was stopped when a new task came and started again from the beginning at the end. The newest rule runs mutation tests last, once no task is open and the implementation is stable, and the plugin's `CLAUDE.md` states whether that needs a request (default: on request).

> Earlier variant: one record removed `TODO.md` and `CONTEXT.md` altogether once the plugin was finished, and forbade any general-purpose task file. The newest rule keeps a local, unversioned `CONTEXT.md` as the working log (see the knowledge rule).

### Context

Open tasks pile up and are reported as finished while checks are still red. Without a shared definition, finished means whatever is convenient at the moment, and a decision that is only mentioned in a reply is lost. Several open work items at the same time produce a working tree in which it is no longer possible to tell which change belongs to which intention, and a red gate can no longer be traced to a cause.

A plugin has several parts (task, synchronization, configuration, tests, documentation) and a plan, a scope and many decisions. The temptation to work in parallel is large, and mutation tests could start at once. Mutation tests take long and say something about the shape of the test suite. As long as tests are still being added, a run measures a state that will not exist a moment later. A number measured against code that is still being written measures nothing, and reading it invites acting on it.

A large release brings new tools, a new rule model, a derived set, a reworked usability in storefront and administration and a configuration matrix. Work of this size tempts one to start the next part before the current one is finished and to run checks against code that is still moving.

Plugins that are built largely in agent-assisted sessions against a very long specification (188 chapters in one case) have one characteristic failure mode: code appears quickly, plausibly and in the wrong shape, because the session started from a request rather than from an understanding of what was actually being asked. The code then works, passes review on its own terms and is discovered to be wrong weeks later when it meets a requirement nobody had restated. The correction is to make the brief and the plan artifacts rather than internal states. A brief that exists as a file in `docs/superpowers/specs/` can be disagreed with before any code is written. A plan in `docs/superpowers/plans/` can be checked against the specification. Neither survives inside a conversation, which is exactly the context that compaction and session restarts destroy, the same problem `CONTEXT.md` solves for state.

Decisions have the same property but a longer lifetime. A load-bearing decision recorded after implementation is not a decision, it is a description of what was built: the alternatives were never weighed, and the record cannot be trusted to say why. Recording it first means the ADR is the thing being reviewed, at the moment when changing course is still cheap.

Editing an accepted ADR destroys the one thing the record is for. If the file that said "we call providers synchronously at checkout" is quietly rewritten to say the opposite, nothing in the repository shows that the first decision was ever made, or when it stopped holding, or why. Reviews cite ADRs by filename, and a filename whose contents change is a citation to nothing. So a changed decision gets a new ADR, the old one moves to `adr/_superseded/` and the new one links back.

"Done" needs a definition for the same reason a gate needs to be green: without one, done means whoever declares it.

A plugin that is live in customer shops has no unfinished work by definition. A template that is live gets rewritten and code that changes what a shopper pays gets added, and the order in which that happens decides whether a regression is caught in a test or in a support ticket. A plugin that arrives with no gate, no coverage and one test that proves nothing needs a workflow that is the target, and the first tasks are the ones that build it.

### Decision

**One task is open, never two.** It is finished or explicitly set aside before the next one begins. Within a task, parallel subagents may work on separate files. A task is complete when the gate is green and the change has been handed over (committed).

**Finished means:** written, checked, the gate green, the documentation updated and committed. Not "the code works". A task is not finished because its own tests pass while the gate is red, and a decision is not recorded by being mentioned in a reply. It is in an ADR, in `CLAUDE.md` or in `CHANGELOG.md`, or it does not exist.

**Order within a release, fixed:**

1. All features and requirements first (the implementation phase, with green static checks). After every step `CONTEXT.md` is updated and, where sensible, a commit is made.
2. Then all tests: unit, integration, architecture, Jest, coverage (100 percent), end-to-end, `composer gate` green. The test phase follows after the whole implementation and is planned, not forgotten. The gate still runs after every task, so that the existing suite guards each change before the new tests exist.
3. Then builds, end-to-end tests, mutation tests and the release documents.
4. Mutation tests last, after every other level is green and when no task is open and the implementation is stable. Whether they run without an explicit request is stated in the plugin's `CLAUDE.md`, the default is on request. A baseline is measured and stored, every surviving mutant is classified first: a missing test becomes a test that states the rule, dead or redundant code is removed, an equivalent mutant is documented with its reason in the baseline. The baseline is outdated between two runs, which is acceptable because it is a snapshot of suite quality and not a running check.

**A task is done** when `composer gate` is green twice in a row with identical output and a byte-identical tree, the documentation and the fitting ADR are updated, `CONTEXT.md` is updated, and the branch has been merged by the user (nothing is pushed).

**The plugin is done** when in addition: PHP coverage (classes, methods, lines) is 100 percent in a measuring run, Jest reaches 100 percent by threshold, every end-to-end test is green, two consecutive end-to-end runs leave the shop and the test account of the connected system unchanged, every surviving mutant is classified and, where equivalent, documented in `docs/mutation/<date>/README.md`, and `README.md`, `CHANGELOG.md`, `SECURITY.md`, `docs/UPGRADE-6.7.md` and `docs/DEPRECATIONS.md` are written and the ADR index is current.

**A user interface is finished only when a browser has shown it.**

**A decision that is only mentioned in a reply does not exist.** It is recorded (see the rule on new requests).

**Requests during a task.** A new request arriving mid-task is acknowledged, not followed. The running task continues to its commit first. A requirement that changes the working rules applies at once. Where the request is then recorded depends on what it is:

| The request is | It goes |
|---|---|
| a decision about how the plugin works | into a new ADR |
| a change to the rules of working | into `CLAUDE.md` |
| a behavior change a merchant will notice | into `CHANGELOG.md` |
| state and next steps | into `CONTEXT.md` |
| a piece of work to do next | into the reply, and then done |

An incidental finding is not fixed at once but noted and handled afterwards. The one thing that interrupts a running task is a change to `CLAUDE.md` itself, which is carried out at once.

**`CONTEXT.md` in the plugin directory is the working log of a release.** It is updated after every step, kept before, during and after every task, is listed in `.gitignore` and is never committed. It describes work in progress, and a checked-in status file claims with authority what was once true. A blocked task does not hold up the others, because its material lies in `CONTEXT.md`. There is no `TODO` directory in the repository: what is open stands in the plan of the respective subsystem, because a second list becomes outdated and then contradicts the first.

**Written artifacts of the development workflow:**

| ID | Sev | Rule |
|---|---|---|
| R-801 | MUST | `superpowers:brainstorming`, then `writing-plans`, then `executing-plans` precedes every implementation. No code without a brief and a plan. |
| R-802 | MUST | Briefs and designs go to `docs/superpowers/specs/`, plans to `docs/superpowers/plans/`. |
| R-803 | MUST | Load-bearing decisions are recorded as an ADR before implementation, not after. |
| R-804 | MUST | An ADR is never edited into something else. A changed decision gets a new ADR that supersedes the old one. |
| R-805 | MUST | Definition of done: rules kept, gate green, tests green, `CONTEXT.md` updated, merged into the main branch. |

- On R-801: the three phases are sequential and none is optional. Brainstorming produces the brief (what is being solved, for whom, and what the alternatives were). Planning produces the implementation plan. Only then is code written, and it is written against the plan. "No code without a brief and a plan" has no size exemption, for the same reason the git rule R-101 has none: the exemption is what every change would claim.
- On R-803: "load-bearing" is the test. Would a different answer here change what gets built elsewhere? Provider coupling, persistence, money handling and sourcing determinism were all load-bearing and each has an ADR. A choice that only affects one file's internals does not.
- On R-804: the mechanics are fixed. The superseded ADR moves to `adr/_superseded/`, the replacement links to it, and the metadata block of the new file carries its own date. What was decided, and when, stays readable. This applies to accepted ADRs. A draft that has not been accepted is still being written, not being rewritten.
- On R-805: all five hold at once, and the last one has an order to it. "Rules kept" means the numbered rules of the project, which is what makes them citable in review. "Gate green" and "tests green" are separate conditions because they fail differently: the gate covers static analysis and formatting, the tests cover behavior. `CONTEXT.md` is updated with exact file paths, verification state and open points, so the next session resumes rather than rediscovers. The merge into the main branch happens last, with `--no-ff`. A feature branch that has not been merged is not done, and a merge that happened before the other four conditions held was premature.

**Practices for a plugin that is live in shops or built from nothing:**

- Specification before code. What a class must do is written down (in `docs/SPECIFICATION.md` or an ADR) before the class exists. The rules in the calculating sections of the specification were written before any of them had an implementation, and every one of them is a test name.
- Test before implementation where practical, and the test fails first. A test that passes the moment it is written has not been shown to test anything. This applies to the calculating classes without exception, and for wiring and configuration where it is practical.
- The gate runs before every merge: `composer gate`. It auto-fixes what can be fixed, then checks static analysis, style, Rector, unit tests and integration tests. Green means mergeable, red means the work is not done.
- Coverage and mutation runs are separate, because they are slow and because a filtered test run must never overwrite a full report:

```bash
composer coverage    # pcov, into var/coverage/
composer infection   # mutation testing, into var/infection/
```

- `CONTEXT.md` is read before starting and updated after finishing. It carries what the next session needs to know: what was decided and why, what is verified, what is open, what the next concrete step is.
- Verification is claimed only when it has been run. "Tests green" means a test run was observed. A figure quoted in a report is a figure that was measured.
- For a live plugin, the rewrite of a template is preceded by a Playwright suite that pins the current rendering. That suite is a precondition, not a follow-up, and it is the only thing that can prove a shop without the new feature looks unchanged.

### Consequences

Reports are reliable, and nothing counts as done while one of the conditions is red. The test phase is planned and not forgotten. The plugin becomes runnable in clearly separable parts, and every commit is one of the steps and not an ingredient to one. When a task stalls, the material is at hand to begin another without losing the blocked one.

An incidental finding is noted and handled afterwards, which feels slower and keeps the working tree readable. The mutation number is unknown for most of the work, and that is correct. It is a closing measurement, like counting the rows a test run left behind, not a gauge to watch. A request that arrives mid-task and is not written into one of the places above is lost when the session ends. That is deliberate, because it forces the question "where does this belong?" at the moment the request arrives, rather than letting a list absorb everything and decay.

Work survives its session. A brief, a plan and a `CONTEXT.md` entry are files, so a compacted context or a new session resumes from the artifacts instead of reconstructing intent from the diff. Disagreement moves earlier: it happens over a brief, where changing direction costs a paragraph, rather than over a merge request, where it costs the implementation.

The ADR set stays trustworthy as a set. Because R-804 forbids editing, a filename cited in a review in March still means in September what it meant then, and the supersession chain shows the actual sequence of decisions. That property is worth more than the tidiness of a single up-to-date file, and it is the reason the tidier option is rejected.

The cost is front-loading, and it is a real cost. A change that would take twenty minutes to write takes longer once a brief and a plan precede it, and the ratio is worst for the smallest changes, which is precisely where the temptation to skip R-801 lives. Writing the specification first front-loads work that feels like delay. It is the reason rules such as the highest reached tier, `>=` at the boundary, rounding towards zero and goods value as base exist as decisions rather than as whatever the first implementation happened to do. The ADR directory also grows monotonically: superseded decisions are never deleted, only moved, so `adr/` plus `adr/_superseded/` accumulates permanently. That is accepted for the same reason `CONTEXT.md` is never shortened.

A gate that must be green before every merge will occasionally block work that "obviously" works. That is the cost of the guarantee that the main branch is releasable. `CONTEXT.md` is only worth its maintenance if it is genuinely read at the start of a session. If it decays into a changelog nobody opens, the discipline has failed and the file should be fixed rather than abandoned.

Almost none of this is enforceable by tooling. CI can check that `adr/` files parse, that the metadata block is present and well-formed, and that a file in `adr/_superseded/` is referenced by some replacement. That much is a linting script. It cannot check that a brief preceded the code rather than being written alongside it, that a decision was load-bearing, or that `CONTEXT.md` was updated with anything meaningful. R-801 through R-804 are review obligations. Only two of R-805's five conditions, gate green and tests green, are mechanical. The other three are checked by a human, and a definition of done is only as good as the willingness to withhold the word.

## model-choice-and-subagents: The model is chosen per task, Opus work stays in the main session, and delegated agents own disjoint files

**Area:** process **Status:** accepted

> Earlier variant: older records assigned Opus to complex logic (entity hydrator, event handler, tracking builder, DAL queries, server events), Sonnet to simple tasks (one class, one fix, routines) and Haiku to pure text files (`CONTEXT.md`, ADRs, documentation), decided per task in the plan. Another allowed delegated agents with haiku, sonnet or opus, with opus for design-heavy or risky logic and for reviews. The newest rule keeps Opus work in the main session and lets subagents run only with Haiku or Sonnet.

### Context

The work is mixed: logic in code, simple tasks, pure text files. One model for everything is either too slow for simple work or too weak for difficult logic, and it is not the fastest. The choice of the model should secure quality where it counts and save effort where it does not. Larger models solve harder problems, smaller ones save compute on simple orders.

Parallel agents that write the same file or run git at the same time destroy each other's work. The context of the main session is limited.

### Decision

- Work is delegated so that the main session keeps its context for coordination.
- **The model is chosen by oneself per task**, not per file and not per plan entry. Opus work runs directly in the main session.
- **Subagents run only with Haiku or Sonnet.** Haiku is for research with a simple answer, mechanical text work and small bundles. Sonnet is for well-specified implementation. Research that has to be exact is not given to Haiku, which was an expensively paid lesson. No forks.
- **Markdown files (ADRs, README, documentation) are written by a subagent with Haiku or Sonnet.** The main agent writes no ADRs. The main agent keeps the responsibility for correctness and checks the texts against the code.
- Code, identifiers, comments and commit messages are English, the Markdown of the ADRs German.
- Each agent owns a list of files and folders. The ownership table is part of every task. Owners do not overlap. A change outside one's own area goes to the orchestrator.
- Agents never commit, branch, merge or push, never run `composer require` and never change the database, plugin state or message queue unless the task demands it.
- Agents that start later wait until their prerequisites are met.
- Every agent reports files, decisions, open points and deviations. Accepted deviations are recorded in `CONTEXT.md`. Only the orchestrator writes `CONTEXT.md`.

### Consequences

The difficult logic gets the strongest model, and the text work is done cheaply. Parallel work stays conflict-free and verifiable. Deviations become visible in a report instead of in a broken build. The orchestrator carries the integration work. Work is finished faster.

## licence-is-proprietary: The licence is proprietary and is checked by hand at the start of every piece of work

**Area:** legal **Status:** accepted

> Earlier variant: an older record had `CodingStyleTest` check `proprietary` in `composer.json` and in every `package.json` (outside `node_modules`) as well as the current year in `LICENSE`, and declared `proprietary` in every `package.json` of the plugin too. The newest rule has no test for this and relies on a manual check at every piece of work. The `package.json` declaration is kept as good practice.

### Context

The plugin is a commercial product of the company that owns it. A permissive licence text still grants redistribution and modification even with a changed title, because the grant stands in the text. A copyright year that lags behind reads like an abandoned work.

### Decision

- `composer.json` declares `"license": "proprietary"`. Every `package.json` of the plugin (outside `node_modules`) declares `proprietary` as well.
- `LICENSE` is a complete proprietary licence text, written as a whole and never pieced together from another licence. A foreign licence text is replaced completely, not amended and not adapted: the old text goes out and the new one comes in.
- The copyright line reads `Copyright (c) <first year>-<current year> <owner company>`. A range appears as soon as the years differ. The first year stays, the end year is the current year (currently 2026). The year is always checked when the licence is checked.
- Licence and copyright stand only in these places (`LICENSE` and `composer.json`), not in class files.
- There is no test for this in the plugin. The check happens by hand at every piece of work on the plugin, and whoever works on the plugin checks both files at the start.

### Consequences

The legal situation has a single authoritative source. Because no test checks the year, an outdated year is noticed only by the manual check. Where a test is used, the year is a small recurring check that turns the test red at the beginning of a new year.

## images-are-licence-free: Every image is licence-free, documented, and marked when a machine made it

**Area:** documentation **Status:** accepted

### Context

The wiki (both halves of it, the user and the developer one) and the `README.md` need pictures: a listing with an interruptor in it, the administration form, the result in the storefront.

Two of those three are screenshots of the own shop and raise no question. The third does. An interruptor carries an image, so a storefront screenshot showing one shows that image. A screenshot is a reproduction, not a transformation: if the picture inside it may not be used commercially, the screenshot may not either. The licence travels with the pixels.

The plugin is proprietary software distributed to customers, and its documentation goes with it. An image whose terms nobody read is a claim that cannot be answered when it is questioned, and the party who has to answer is the one who shipped it.

Shopware's own demo data is the obvious trap and the reason this is written down. The product photographs in a demo shop look like free material sitting right there in the media library. They are licensed to Shopware, for running a Shopware demo. They are not ours to put in a manual.

### Decision

**Every image in the wiki and in the README is licence-free or explicitly cleared for commercial use, neutral in subject, and documented in full. An image that fails any of those three is not used.**

#### Licence

**No image is ever bought.** No stock licence is purchased, no subscription is taken out, no single-image payment is made, and no trial that converts into one is started. Where the only route to a picture is money, the picture is not used and a free one is found instead. This is a rule, not a budget: a purchased licence is a contract with terms, a renewal date and a scope, and a manual that outlives it starts making a claim nobody is tracking. A free licence with a written record does not expire.

Acceptable: Unsplash, Pexels and Pixabay under their current licences, and Wikimedia Commons where the file itself states CC0 or a public-domain mark. **The licence is read on the image's own page at the moment of download**, never inferred from the platform. A platform hosts files under more than one licence, and the terms of all three named here have changed before.

Not acceptable: an image search result, any file already in the shop's media library whose origin is unknown, the Shopware demo data, and anything behind a payment, a paywalled preview or a watermark.

#### Generated images

**An image may be generated rather than found**, through the fal.ai account whose key lives in `FAL_AI_KEY`. Two conditions attach to it, and both are absolute.

**The licence comes from the model, not from the service.** The terms of fal.ai are silent on who owns the output: section 6(b) assigns the input to the customer, section 4(c) disclaims warranties about the output, and nothing grants rights in it. So the question "may this image be used commercially" is answered by the model that produced it, before it is generated. FLUX.1 [schnell] is Apache 2.0 and may be used. FLUX.1 [dev] carries a non-commercial licence and may not. **The model is chosen for its licence first.** A plugin that is sold cannot use a non-commercial model, regardless of how good the picture is.

**Every generated image is marked as AI generated.** Article 50 of the EU AI Act (Regulation 2024/1689) requires it from 02.08.2026, and the Commission publishes icons for exactly this. The "AI GENERATED" label, the one for wholly artificial content, is burnt into the picture as a watermark, in the same position, size and opacity on every image. It is a watermark rather than a caption because the obligation is that the mark survives sharing and download, and a caption does not travel with the file.

The Commission states the icons are "made publicly available for everyone to use freely, without the need for attribution to the Commission or the AI Office", which is recorded here so nobody has to look it up again.

**A generated image is not licence-free.** It is licensed under the model's terms, and the record names them along with the model id and the prompt.

#### Subject

Landscapes and nature. **No people, no recognizable brands, no logos, no product of an identifiable manufacturer.** Those carry rights that exist beside the photograph's own licence. A personality right or a trade mark is not settled by the photographer's permission, and a free licence on the photograph says nothing about them.

#### Documentation

Every image gets a complete record, on a page of its own. The record exists in both wikis and in the README: **each document that shows an image documents it**, because each may be read alone.

| Field | Content |
|---|---|
| File name | the path in the wiki or in the plugin |
| Title | as the source names it |
| What it shows | one plain sentence |
| Source | the direct link to the image's own page, not the platform's home page |
| Author | photographer or uploader, as named |
| Licence | the exact designation, for example "Unsplash License", "CC0 1.0" |
| Licence text | a link to the full text |
| Retrieved on | the date of download |
| Commercial use | permitted, with the sentence in the licence that says so |
| Attribution | required or not, and where it is given |
| Where it lives | the path in the plugin or in the wiki repository |

For a generated image, four more:

| Field | Content |
|---|---|
| Generated with | the service and the exact model id |
| Model licence | the designation and a link |
| Prompt | verbatim |
| AI marking | that it carries the EU "AI GENERATED" watermark |

The wiki carries this on `quellen.md`, linked from the sidebar and the home page, and it covers the images of both the user and the developer half. The README carries it in a `## Quellen` section towards the end. An image used in both the wiki and the README is documented in both.

### Consequences

The documentation has fewer pictures than it could have, and each one costs a few minutes of reading terms before it is downloaded. That is the price, and it is small.

**A record that cannot be completed settles the question by itself.** If the author is not named on the source page, or the licence designation is not stated plainly, the image is not used. There is no judgment call to make, and nobody has to weigh how likely a complaint is.

This applies to both halves of the wiki and to the README, which are the only documents of the plugin that carry images and the only ones written in German. It does not reach the plugin's own assets: the storefront ships no images, and the placeholder an interruptor without a picture falls back to is drawn in CSS.

**Generating an image is cheaper than finding one, and that is the trap.** It removes the search but not the record: the model, its licence, the prompt and the AI marking all have to be written down, and an image generated in ten seconds that nobody documented is worth less than no image at all.

**The date of retrieval is the part that looks pointless and is not.** A licence can change, and a source page can go away. The record says what the terms were when the decision was made, which is the question actually asked afterwards.

## measure-before-assuming: A margin is measured before it is assumed

**Area:** statistics **Status:** accepted

### Context

The statistics report a margin per sale, computed from the net price the supplier sends beside the retail price. Measured over the catalog: **2229 of 2531 fares carry both**, at 13.78 % (supplier A), 20.00 % (supplier B) and 20.23 % (supplier C).

**302 fares carry no net price at all** (293 of them from supplier A), and their revenue therefore reported no margin whatsoever. A merchant reading the assortment analysis saw a supplier that apparently earns nothing on a fifth of what it sells.

`ff_ticket_supplier.markup_percent` had existed since the first migration as a field labelled with a German "markup in percent", sitting last in the behavior card with no help text. **Not one line of PHP read it.** A merchant who typed 15 into it had every reason to believe prices would carry 15 % more, and nothing on the screen said otherwise.

A further measurement decided the shape: **437 fares of supplier A price net equal to retail.** That is a margin of zero, which the supplier stated, not a missing one.

### Decision

**A measured difference always beats an assumed one.** `FareCatalogue::netPriceOf()` reads the stored ratio first and reaches the assumption only where there is none. Switching an assumption on cannot move a single figure the supplier already priced, which is what makes the feature safe to enable on a shop with live orders.

**A fare priced net equal to retail is measured, not missing.** Those 437 fares report a margin of zero. Treating them as unpriced would have inflated supplier A by a fifth of its catalog.

**Three modes, and "none" is the normal one.** `MarkupMode` is `none`, `percent` or `absolute`. A percentage is a share of what the guest paid. An absolute amount is **per fare sold**: a family ticket for four counts four times, the same distinction `FareRow` already makes.

**An assumption that cannot hold is refused rather than drawn.** A margin above what the guest paid would make the supplier pay the shop, which is a mistyped figure and not a windfall. `netFor()` answers null there, as it does for a negative one and for a fare priced at nothing.

**A ticket overrides its supplier, including downwards.** `ff_ticket.markup_mode` is nullable and null means "follow the supplier". A ticket stating `none` against a supplier that assumes something is the merchant saying "not this one".

**It changes no price.** Nothing a guest pays depends on any of this, and the card says so in its own subtitle, because a field called "markup" in a shop's administration reads as though it does.

### Consequences

- The card states the gap before it asks for a figure (in German: "The supplier gives no purchase price for 293 of 2225 fares"). Where every fare is priced it says an assumption would change nothing, which is the honest answer to a merchant about to type one in.
- `markup_mode` cannot be `Required` on the supplier: `SupplierProvisioner` does not set it, and a required field broke provisioning a connection entirely. Assuming nothing is the normal state and an absent value reads as `none`.
- `DestinationReach` gained an interface. It is `final`, and a test that cannot double it cannot prove the verdict tells a destination the channel does not sell apart from an unpriced fare.
- The percentage is formatted through the administration's locale rather than the browser's, the same rule the timestamps already follow.

## built-assets-are-not-committed: Built assets are not committed and a release archive is built with the storefront build

**Area:** devops **Status:** accepted

### Context

`src/Resources/app/storefront/dist/` is a build artifact. What ships in a release archive is built, and what lives in git is source.

One plugin had three stale files under `dist/`, two of them hash-named leftovers, and the build had been failing for months over a missing `.js` in one import. Those stale files were the only JavaScript it had been shipping. Committed build output hides a broken build.

### Decision

- `src/Resources/app/storefront/dist/` is not committed.
- **The consequence is written down where someone will read it**, because it is easy to get wrong: a release archive built without `shopware-cli project storefront-build --only-extensions <Plugin>` carries no JavaScript at all, and the plugin silently does nothing.

### Consequences

A broken build shows up as a missing bundle and not as a stale file that hides it. The release process must run the storefront build before the archive is made, see `assets-built-with-shopware-cli`.
