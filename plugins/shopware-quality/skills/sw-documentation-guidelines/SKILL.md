---
name: sw-documentation-guidelines
description: >
  Shopware Dokumentations-Guidelines: wie Shopware-Doku und Markdown für Contributions geschrieben
  wird — Zielgruppen, Dokumentationsstruktur (Concepts/Guides/Resources), Sprache & Grammatik,
  Formatierungsregeln, Asset-Management, Doc-Prozess. Trigger: "shopware doku schreiben",
  "documentation contribution", "markdown guidelines shopware", "wie schreibe ich shopware doku",
  "doc guidelines", "technische dokumentation shopware", "contribution doku shopware",
  "developer docs beitragen". Shopware 6.7.
---

# Shopware — Dokumentations-Guidelines

Vollständige Referenz: `references/deep/documentation-guidelines.md`

## Struktur

- **Concepts**: Erklärt Konzepte (Was/Warum), kein Code, keine Schritt-für-Schritt-Anleitungen
- **Guides**: How-tos, Tutorials, Code-Beispiele, konkrete Schritte
- **Resources**: API-Referenzen, Code-Referenzen, Tooling, Contribution-Guidelines

## Sprache & Ton

- American English; freundlich, direkt, klar
- Aktiv-Stimme bevorzugen; zweite Person ("you") statt erste Person ("we")
- Einfaches Präsens; kein Zukunfts-/Vergangenheitstempus
- Keine Slang, Buzzwords, Idiome, "please"/"request"

## Markdown-Konventionen

- Fenced Code-Blocks mit Sprach-Identifier (`php`, `bash`, etc.)
- Bulleted Lists mit `*`, keine Mischung mit `-`
- H1 in Camel Case; Sub-Headings in Sentence Case
- Inline Code mit Backticks für Klassen, Methoden, Dateipfade, CLI-Befehle
- Keine Unterstriche/Unterstreichungen; Bold für UI-Elemente/Notices
- Versionierte Hinweise: `:::info\nThis functionality is available starting with Shopware 6.4.3.0.\n:::`

## Asset-Verwaltung

- Bilder: `.png` (Screenshots), `.svg` (Diagramme, Logos); max. 5 MB; max. 768×576px
- Naming: `<topicName>-<meaningfulImageName>.svg`
- Diagramme: Mermaid (embedded) oder Meteor Diagram Kit (Figma)
- Alt-Text für alle Bilder Pflicht
