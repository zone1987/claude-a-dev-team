---
name: shadcn-vue-chart
description: Erstellt ein shadcn-vue-Chart — wählt Diagrammtyp/Variante, übernimmt den kompletten Beispiel-Vue-Code aus dem shadcn-vue-charts-*-Skill und passt Daten, Config und --chart-Farbtokens an.
argument-hint: <typ> area|bar|line|pie [--variant z.B. interactive|stacked|donut] [--data "Beschreibung"]
allowed-tools: Read, Glob, Grep, Write, Edit, Bash
model: sonnet
---

# /shadcn-vue-chart

Chart erstellen. Skills: `shadcn-vue-charts-overview` + `shadcn-vue-charts-<typ>`.

## Ablauf
1. Diagrammtyp + Variante aus `$ARGUMENTS`.
2. **Basis sicherstellen:** `npx shadcn-vue@latest add chart` (ChartContainer/ChartTooltip/ChartLegend).
3. Nächstgelegenes Beispiel aus `shadcn-vue-charts-<typ>` als Vorlage (kompletter SFC-Code).
4. Datenstruktur + Config anpassen; Tooltip/Legend/Achsen konfigurieren.
5. **Farben:** `--chart-1..5`-Tokens in `globals.css` (Light/Dark) setzen/prüfen — ggf. `/shadcn-vue-theme`.

Chart-Props/Config gegen `shadcn-vue-charts-overview`/`shadcn-vue-chart` prüfen — nicht raten.
