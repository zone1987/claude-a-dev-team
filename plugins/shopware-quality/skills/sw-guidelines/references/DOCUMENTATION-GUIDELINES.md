# Shopware — documentation guidelines

## Contents

- [Structure](#structure)
- [Language and tone](#language-and-tone)
- [Markdown conventions](#markdown-conventions)
- [Asset management](#asset-management)
- [Shopware documentation guidelines: complete reference](#shopware-documentation-guidelines-complete-reference)

## Structure

- **Concepts**: explain concepts (what/why), no code, no step-by-step instructions
- **Guides**: how-tos, tutorials, code examples, concrete steps
- **Resources**: API references, code references, tooling, contribution guidelines

## Language and tone

- American English; friendly, direct, clear
- Prefer active voice; second person ("you") instead of first person ("we")
- Simple present tense; no future or past tense
- No slang, buzzwords, idioms, "please"/"request"

## Markdown conventions

- Fenced code blocks with a language identifier (`php`, `bash`, etc.)
- Bulleted lists with `*`, never mixed with `-`
- H1 in camel case; sub-headings in sentence case
- Inline code with backticks for classes, methods, file paths, CLI commands
- No underscores or underlining; bold for UI elements and notices
- Version notices: `:::info\nThis functionality is available starting with Shopware 6.4.3.0.\n:::`

## Asset management

- Images: `.png` (screenshots), `.svg` (diagrams, logos); max. 5 MB; max. 768×576px
- Naming: `<topicName>-<meaningfulImageName>.svg`
- Diagrams: Mermaid (embedded) or the Meteor Diagram Kit (Figma)
- Alt text is mandatory for all images

## Shopware documentation guidelines: complete reference

Sources: `resources/guidelines/documentation-guidelines/` (every file)

---

### Contents

- [Audiences](#audiences)
- [Documentation structure](#documentation-structure)
- [Language and grammar](#language-and-grammar)
- [Formatting: text](#formatting-text)
- [Formatting: code](#formatting-code)
- [Asset management](#asset-management-1)
- [The documentation process](#the-documentation-process)
- [Embedding in the developer portal](#embedding-in-the-developer-portal)
- [References](#references)

### Audiences

| Audience | What they work on |
|-----------|---------|
| Fullstack developer | plugin development, templates, routes and controllers |
| Frontend developer | the administration, themes, PWA |
| Backend developer | DI and service architecture, message queues, the DAL, Elasticsearch |
| API developer | consuming and extending the API, its paradigms |
| DevOps | hosting, deployment, performance |
| Solution architect | hosting, architecture, the extension system, paradigms |
| Designer | the component library, the design system |

---

### Documentation structure

#### Concepts

Explains Shopware's core concepts. The entry point for understanding how the platform is organised.
- **Explains** what something is and why it is that way, rather than showing it
- No code, no step-by-step instructions
- Pseudo-code is acceptable purely to illustrate, never Shopware source
- Maintain cross-links to related concepts

**How a concept article is built:**
1. **Introduction**: what is the concept? What can it contain? How does it relate to other parts? What will the reader find in related articles?
2. **Comprehensive explanation**: the detail, with examples, tables and diagrams
3. **Conclusions**: the bridge to the next article

#### Guides

Home for how-tos, tutorials, cookbooks and examples.
- Carries code, gives concrete examples, and instructs step by step
- Cross-links back to the concepts section for the concepts involved
- Explains Shopware-specific terms and links to their definitions

#### Resources

- API references, code references, testing references
- Tooling documentation
- Links, SDKs, libraries
- Contribution guidelines (this document)

---

### Language and grammar

#### Voice and tone

**Friendly** — less formal, more human than a robot; the occasional touch of humour where it fits.

**Direct and clear** — to the point, skimmable, as simple as the subject allows.

**Customer focussed** — assume a competent reader, but not a uniform level of knowledge.

#### Active versus passive voice

Prefer the active:
```
Good: The user passes the access-key.
Bad:  The access-key is passed by the user.
```

The passive is acceptable when the object is what matters, when the subject should recede, or when the actor is unknown.

#### Person

- Second person ("you") rather than first ("we", "I")
- The imperative: "Create a PDF file." rather than "You need to create a PDF file."
- Avoid "our"

#### Tense

- The simple present
- No future or past tense

#### Abbreviations

- Spell it out on first use, with the abbreviation in brackets: "JSON Web Token (JWT)"
- Familiar abbreviations (API, HTTPS, PDF) need no explanation
- Never invent an abbreviation of your own
- Plural: "APIs", "IDEs"; where the abbreviation ends in s, sh, ch or x, "OSes"

#### Conjunctions and punctuation

- No slash as a conjunction: "blue or red", never "blue/red"
- No ampersand as a conjunction: "and", never "&"
- The Oxford comma in a list: "assets, controllers, services, or tests"
- An em dash (—) for a break in thought; a hyphen (-) for compounds, number ranges and prefixed words

#### What not to write

- No internet slang
- No buzzwords or jargon
- No idioms or set phrases
- Do not keep opening sentences with "In order to"
- No "please" or "request" — documentation instructs, it does not ask
- Do not write the way you speak

---

### Formatting: text

#### Emphasis

- **Bold** (`**bold**`): UI elements, notices (warning, important), API status codes, the title in a description list
- *Italic* (`*italic*`): a specific word or phrase, parameter values, classes, methods, product versions, key terms
- Underline: NEVER

#### Lists

- **Numbered list**: sequential steps, or a fixed number of items
- **Bulleted list**: a general enumeration, with `*` rather than `-`
- **Description list**: a bold title plus its description; either numbered or bulleted
- Sentence case for every list item

#### Headings

- `#` (H1): camel case — e.g. "Flow Sequence Evaluation"
- `##` and below: sentence case — e.g. "Flow sequence evaluation"
- Never skip a heading level (no H3 directly under an H1)
- No full stop at the end of a heading

#### Hyperlinks

- Meaningful link text: never "click here" or "read this document"
- A complete sentence carrying the context: "For more information, see [XY]"
- Keep the link text short, with the words that matter first
- Never use the same wording for links to different places

#### Tables

- Do not embed a table in a sentence
- Only where there is more than one row and one column
- Sentence case throughout
- No full stop at the end of a cell
- Introduce a table with a complete sentence naming "the following table"

---

### Formatting: code

#### Inline Code

Backticks for: attributes, CLI names, class, method and function names, enum names, file paths, directories, HTTP methods, parameter values, environment variables and command output.

#### Code Blocks

- Fenced code blocks (three backticks) for multi-line code or terminal output
- Always give the language identifier: ` ```php `, ` ```bash `, ` ```twig ` and so on
- Inside a list, indent correctly so the list does not break
- Two spaces for indentation, never tabs
- Three dots (`...`) on a line of their own where output is elided

#### Placeholders

- Upper case and italic: `*`PLACEHOLDER_NAME`*`
- Use an informative name; never "X"

#### HTTP Status Codes

- Code font: `400 Bad Request`
- Range: `HTTP 2xx`
- An explicit range: `400-499`

#### CLI commands

- A `$` prompt at the start of every input line
- No directory path before the prompt

#### API reference

- Describe every class, interface, constant and method
- HTTP methods in upper case: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- Describe each parameter, with its valid values and default
- Method names with brackets: `getProduct()`

#### Deprecations

```markdown
::: warning
**Deprecated** - Access it using this getProd() method instead.
:::
```

---

### Asset management

#### Images

| Attribute | Requirement |
|----------|---------|
| Format | `.png` (screenshots), `.svg` (diagrams, logos, vectors), `.gif` (animations) |
| Size | max. 5 MB |
| Dimensions | max. 768×576px (4:3) |
| Alt text | mandatory for every image |
| Border | none |
| PII | mask it: passwords, logins, account details |

**Naming:**
```
<topicName>-<meaningfulImageName>.svg
storefront-pages.svg

<topicName>-<subtopicName>-<meaningfulImageName>.svg
storefront-dataHandling-pages.svg

Serialisiert bei mehreren Bildern:
storefront-dataHandling-pages_01.svg
```

Alle Assets in `assets/`-Verzeichnis.

#### Diagramme

Einsetzen bei:
- Architektur darstellen
- Komplexe Beziehungen zeigen
- Komplexe Workflows definieren

Tools:
- **Mermaid**: Flowcharts, Sequence Diagrams, State Machine Diagrams, Class Diagrams (als `mermaid`-Code-Block eingebettet)
- **Meteor Diagram Kit** (Figma): andere Diagramm-Typen; folgt Shopware-Design-Standards

#### Screenshots

Einsetzen bei:
- Visualisierungen/Beispiele zeigen
- Panels showing the query or settings
- Neue Features hervorheben

Regeln:
- Neuestes OS-Versionen
- Fokussiertes aktives Fenster
- No needless whitespace or scrollbars
- Real data, or data that looks real
- No code inside a screenshot — use a code block
- No screenshot of a page that changes often

#### Videos and GIFs

Use them for: walking through a procedure, demonstrating a feature visually, setup instructions.

- Captions and transcripts for videos
- Naming analog zu Bildern

#### Datei-Naming

```
<two_digit_number>-<meaningful-name>.md
01-doc-process.md
```

---

### Dokumentationsprozess

#### 1. Ideate

Settle before writing:
- Who is the audience?
- What is being documented?
- What are the prerequisites?
- Which questions does it answer?
- Which other topics bear on it?

#### 2. Write — 30/90 Rule

- Bei **30% fertig**: Erster Draft + erstes Feedback auf High Level
- At **90% done**: a steady review, for in-depth validation

Erster Draft:
- Dokumentstruktur (Themen-Fluss) vorbereiten
- Alle Punkte kurz skizzieren
- Gemeinsamen roten Faden beibehalten
- Placeholders for images and code
- Cross-Referenzen einbauen
- Nicht-Shopware-spezifische Sprache bevorzugen oder verlinken

#### 3. Review

The reviewer checks the overall approach, the tone, and the wording against these guidelines.

More than one reviewer often helps. Repeat the cycle until the version is final.

#### 4. Publish

Before publishing, check that every original question and goal has been met.

#### 5. Versionen pflegen

Content is tied to Shopware major versions (6.3, 6.4, …). Current is the `main` branch; older versions live in their own Branches.

Versions-Hinweis:
```markdown
::: info
This functionality is available starting with Shopware 6.4.3.0.
:::
```

---

### Embedding in Developer Portal

A repository can embed content through the docs CLI (`developer-portal`):

```bash
## portal.json anpassen, dann:
./docs-cli manage
```

Then configure it in `.vitepress/navigation.ts` for the sidebar, and in `.github/scripts/mount.sh` for the production build.

Shortcuts in `package.json`:
- `docs:env` — Portal klonen/aktualisieren
- `docs:link` — Docs symlinken
- `docs:preview` — Vitepress Dev Server

---

### Referenzen

- `resources/guidelines/documentation-guidelines/01-general.md`
- `resources/guidelines/documentation-guidelines/02-conceptual-structure.md`
- `resources/guidelines/documentation-guidelines/03-language-and-grammar.md`
- `resources/guidelines/documentation-guidelines/04-fonts-and-formats/01-text.md`
- `resources/guidelines/documentation-guidelines/04-fonts-and-formats/02-code.md`
- `resources/guidelines/documentation-guidelines/05-methodize-assets.md`
- `resources/guidelines/documentation-guidelines/06-doc-process.md`
- `resources/guidelines/documentation-guidelines/07-embedding-external-repositories.md`
