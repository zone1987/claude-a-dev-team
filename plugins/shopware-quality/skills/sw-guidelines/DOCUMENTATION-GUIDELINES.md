# Shopware — documentation guidelines

Complete reference: `DOCUMENTATION-GUIDELINES-DETAIL.md`

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
