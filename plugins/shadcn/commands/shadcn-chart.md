---
name: shadcn-chart
description: Erstellt ein shadcn/ui-Chart (Recharts) — wählt den passenden Diagrammtyp/die Variante, übernimmt den kompletten Beispiel-Code aus dem shadcn-charts-*-Skill und passt ChartConfig, Daten und --chart-Farbtokens an.
argument-hint: <typ> area|bar|line|pie|radar|radial [--variant z.B. stacked|interactive|donut] [--data "Beschreibung"]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-chart

Chart erstellen. Skills: `shadcn-charts-overview` + `shadcn-charts-<typ>`.

## Ablauf
1. Diagrammtyp + Variante aus `$ARGUMENTS`.
2. **Basis sicherstellen:** `npx shadcn@latest add chart` (ChartContainer/ChartTooltip/ChartLegend).
3. Nächstgelegenes Beispiel aus `shadcn-charts-<typ>` als Vorlage nehmen (kompletter Code).
4. **`ChartConfig`** (label/icon/color je Reihe) + Datenstruktur an den Use-Case anpassen; Achsen/Tooltip/Legend konfigurieren.
5. **Farben:** `--chart-1..5`-Tokens in `globals.css` (Light/Dark) setzen/prüfen — ggf. `/shadcn-theme`.

Recharts-Props/ChartConfig-Felder gegen `shadcn-charts-overview`/`shadcn-chart` prüfen — nicht raten.
