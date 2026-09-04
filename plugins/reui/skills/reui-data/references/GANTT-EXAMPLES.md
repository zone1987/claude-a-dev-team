# Gantt — examples

Part of [GANTT.md](./GANTT.md). Free component — no licence key required. Base UI build (see
[GANTT.md#base-ui-vs-radix-ui](./GANTT.md#base-ui-vs-radix-ui) for the Radix diff: `asChild` instead
of `render`, otherwise identical).

Every example below is a complete, standalone `Pattern()` component from the docs page. Shared
composition shape across all of them: `<Card><CardContent className="p-0"><Gantt ...><div
className="flex ... border-b"><GanttNav className="min-w-0 flex-1 border-b-0" /><GanttToolbar>...
</GanttToolbar></div><GanttView /></Gantt></CardContent></Card>`, with `apiRef` wired to a
`useRef<GanttApi | null>(null)` when the toolbar needs to call `addEvent`/`getEvents`.

## Contents

- [Flagship demo (top of the docs page)](#flagship-demo-top-of-the-docs-page)
- [Annual Product Roadmap](#annual-product-roadmap)
- [Team Capacity Schedule](#team-capacity-schedule)
- [Project Status Report](#project-status-report)
- [As-Built Baseline Tracking](#as-built-baseline-tracking)
- [Dependencies and Milestones](#dependencies-and-milestones)
- [Source](#source)

## Flagship demo (top of the docs page)

The full composition: every view configuration and interaction flag as a controlled prop, driven
from a settings menu, plus locale/time-zone switching and the unscheduled-row scheduling contract.

```tsx
"use client"

import { useMemo, useRef, useState } from "react"
import {
  Gantt,
  type GanttApi,
} from "@/components/reui/gantt/gantt"
import type { GanttI18nOverrides } from "@/components/reui/gantt/gantt-i18n"
import {
  GanttNav,
  GanttToolbar,
} from "@/components/reui/gantt/gantt-nav"
import type {
  GanttEvent,
  GanttInteractions,
  GanttResource,
  GanttSlotDraft,
} from "@/components/reui/gantt/gantt-types"
import { GanttView } from "@/components/reui/gantt/gantt-view"
import { addDays, startOfDay, startOfWeek, type Locale } from "date-fns"
import { ar, de, es, fr, ja } from "date-fns/locale"
// ... resource tree (RESOURCES), event fixture (buildBars), locale table (LOCALES),
// time-zone table (TIME_ZONES), a RESOURCE_TITLES lookup, and SETTINGS_DEFAULTS
// mirror the shape used in EVENT-CALENDAR-EXAMPLE.md's flagship demo, one settings
// field per view-configuration/interaction prop documented in GANTT.md.

export function Pattern() {
  const bars = useMemo(() => buildBars(new Date()), [])
  const apiRef = useRef<GanttApi | null>(null)
  const [rowCheckboxes, setRowCheckboxes] = useState(SETTINGS_DEFAULTS.rowCheckboxes)
  const [summaryBars, setSummaryBars] = useState(SETTINGS_DEFAULTS.summaryBars)
  const [zoomControl, setZoomControl] = useState(SETTINGS_DEFAULTS.zoomControl)
  const [offscreenIndicators, setOffscreenIndicators] = useState(SETTINGS_DEFAULTS.offscreenIndicators)
  const [infiniteScroll, setInfiniteScroll] = useState(SETTINGS_DEFAULTS.infiniteScroll)
  const [nowIndicator, setNowIndicator] = useState(SETTINGS_DEFAULTS.nowIndicator)
  const [offDays, setOffDays] = useState(SETTINGS_DEFAULTS.offDays)
  const [dragCreate, setDragCreate] = useState(SETTINGS_DEFAULTS.dragCreate)
  const [displayScheduleHint, setDisplayScheduleHint] = useState(SETTINGS_DEFAULTS.displayScheduleHint)
  const [barLabel, setBarLabel] = useState<"inside" | "outside" | "auto">(SETTINGS_DEFAULTS.barLabel)
  const [timelineLines, setTimelineLines] = useState<"vertical" | "both" | "none">(SETTINGS_DEFAULTS.timelineLines)
  const [interactions, setInteractions] = useState<GanttInteractions>(SETTINGS_DEFAULTS.interactions)
  const [localeId, setLocaleId] = useState(SETTINGS_DEFAULTS.localeId)
  const [timeZoneId, setTimeZoneId] = useState(SETTINGS_DEFAULTS.timeZoneId)
  const activeLocale = LOCALES.find((entry) => entry.id === localeId) ?? LOCALES[0]
  const activeTimeZone = TIME_ZONES.find((entry) => entry.id === timeZoneId) ?? TIME_ZONES[0]

  const resetSettings = () => {
    setRowCheckboxes(SETTINGS_DEFAULTS.rowCheckboxes)
    setSummaryBars(SETTINGS_DEFAULTS.summaryBars)
    setZoomControl(SETTINGS_DEFAULTS.zoomControl)
    setOffscreenIndicators(SETTINGS_DEFAULTS.offscreenIndicators)
    setInfiniteScroll(SETTINGS_DEFAULTS.infiniteScroll)
    setNowIndicator(SETTINGS_DEFAULTS.nowIndicator)
    setOffDays(SETTINGS_DEFAULTS.offDays)
    setDragCreate(SETTINGS_DEFAULTS.dragCreate)
    setDisplayScheduleHint(SETTINGS_DEFAULTS.displayScheduleHint)
    setBarLabel(SETTINGS_DEFAULTS.barLabel)
    setTimelineLines(SETTINGS_DEFAULTS.timelineLines)
    setInteractions(SETTINGS_DEFAULTS.interactions)
    setLocaleId(SETTINGS_DEFAULTS.localeId)
    setTimeZoneId(SETTINGS_DEFAULTS.timeZoneId)
  }

  // Unscheduled rows accept ONE schedule: the hint tile (or a drag-create
  // range) proposes a slot, and the handler turns it into a real bar.
  const canSelectSlot = (slot: GanttSlotDraft) =>
    !!slot.resourceId &&
    !(apiRef.current?.getEvents() ?? []).some(
      (event) => event.resourceId === slot.resourceId
    )

  const handleSelectSlot = (slot: GanttSlotDraft) => {
    const api = apiRef.current
    if (!api || !slot.resourceId) return
    api.addEvent({
      id: `scheduled-${slot.resourceId}`,
      title: RESOURCE_TITLES.get(slot.resourceId) ?? "New schedule",
      start: slot.start,
      end: slot.end,
      allDay: true,
      color: "var(--color-indigo-500)",
      resourceId: slot.resourceId,
    })
  }

  return (
    <div className="w-full p-4" dir={activeLocale.dir}>
      <Card className="w-full py-0">
        <CardContent className="p-0">
          <Gantt
            defaultEvents={bars}
            resources={RESOURCES}
            defaultScale="month"
            apiRef={apiRef}
            locale={activeLocale.locale}
            i18n={activeLocale.i18n}
            timeZone={activeTimeZone.value}
            treePanel={{ width: 200 }}
            rowCheckboxes={rowCheckboxes}
            summaryBars={summaryBars}
            zoomControl={zoomControl}
            offscreenIndicators={offscreenIndicators}
            infiniteScroll={infiniteScroll}
            nowIndicator={nowIndicator}
            offDays={offDays}
            dragCreate={dragCreate}
            displayScheduleHint={displayScheduleHint}
            barLabel={barLabel}
            timelineLines={timelineLines}
            interactions={interactions}
            onInteractionsChange={setInteractions}
            canSelectSlot={canSelectSlot}
            onSelectSlot={handleSelectSlot}
            className="h-[520px] w-full"
          >
            {/* one bordered header row, same look as the plain GanttNav:
                the row owns the border and end padding so the toolbar never
                sits glued to the edge */}
            <div className="flex flex-wrap items-center gap-2 border-b pe-3">
              <GanttNav className="min-w-0 flex-1 border-b-0" />
              <GanttToolbar>
                <SettingsMenu
                  rowCheckboxes={rowCheckboxes}
                  onRowCheckboxesChange={setRowCheckboxes}
                  summaryBars={summaryBars}
                  onSummaryBarsChange={setSummaryBars}
                  zoomControl={zoomControl}
                  onZoomControlChange={setZoomControl}
                  offscreenIndicators={offscreenIndicators}
                  onOffscreenIndicatorsChange={setOffscreenIndicators}
                  infiniteScroll={infiniteScroll}
                  onInfiniteScrollChange={setInfiniteScroll}
                  nowIndicator={nowIndicator}
                  onNowIndicatorChange={setNowIndicator}
                  offDays={offDays}
                  onOffDaysChange={setOffDays}
                  dragCreate={dragCreate}
                  onDragCreateChange={setDragCreate}
                  displayScheduleHint={displayScheduleHint}
                  onDisplayScheduleHintChange={setDisplayScheduleHint}
                  barLabel={barLabel}
                  onBarLabelChange={setBarLabel}
                  timelineLines={timelineLines}
                  onTimelineLinesChange={setTimelineLines}
                  interactions={interactions}
                  onInteractionsChange={setInteractions}
                  localeId={localeId}
                  onLocaleChange={setLocaleId}
                  timeZoneId={timeZoneId}
                  onTimeZoneChange={setTimeZoneId}
                  onReset={resetSettings}
                />
              </GanttToolbar>
            </div>
            <GanttView />
          </Gantt>
        </CardContent>
      </Card>
    </div>
  )
}
```

The `SettingsMenu` sub-component (referenced but whose own body the mirrored page does not print
separately) renders the same Popover + Tabs + Switch/Select shape as the Event Calendar flagship
demo's settings panel — see
[EVENT-CALENDAR-EXAMPLE.md](./EVENT-CALENDAR-EXAMPLE.md) for that pattern in full, including the
Base UI `SelectValue` children-override note that also applies here (see
[GANTT.md#base-ui-vs-radix-ui](./GANTT.md#base-ui-vs-radix-ui)).

## Annual Product Roadmap

Quarter-scale swimlanes (`defaultScale="quarter"`). Workstream groups (`Platform`, `Growth`, `Design
System`, `Backlog`) carry no bars of their own — `summaryBars` (default `true`) rolls up their
children's envelope automatically. The toolbar's "Add to roadmap" button schedules the next
unscheduled `BACKLOG` initiative via `api.addEvent`, tracking progress with a `scheduled` counter
derived from `api.getEvents()` (not a stale closure count) so rapid clicks stay correct:

```tsx
const addInitiative = () => {
  const api = apiRef.current
  if (!api) return
  const scheduledIds = new Set(api.getEvents().map((event) => event.id))
  const index = BACKLOG.findIndex((item) => !scheduledIds.has(`bar-${item.id}`))
  if (index === -1) return
  const item = BACKLOG[index]
  const week = startOfWeek(startOfDay(new Date()), { weekStartsOn: 0 })
  const start = addDays(week, 12 + index * 20)
  api.addEvent({
    id: `bar-${item.id}`,
    title: item.title,
    start,
    end: addDays(start, 24),
    allDay: true,
    color: item.color,
    resourceId: item.id,
  })
  setScheduled((count) => count + 1)
}
```

Resource tree: `Platform` (`Auth Revamp`, `API v2`), `Growth` (`Onboarding Flow`, `Referral
Program`), `Design System` (`Design Tokens`, `Component Library`), `Backlog` (`Search Revamp`,
`Billing v2`, `Mobile App` — initially unscheduled). `buildBars` seeds the four non-backlog leaves
with multi-month bars (offsets straddling today, `progress` values 0/30/45/80/100) so the quarter
axis shows real content immediately; `BACKLOG` names the three initiatives the button schedules in
order, each with its own accent color (`rose-500`, `amber-500`, `cyan-500`).

## Team Capacity Schedule

Week-scale (implicit default `"day"` scale is NOT used here — the example relies on the default
scale with day-precision bars) people board. Rows are teammates grouped under `Product Squad` /
`Design Squad`; `renderResourceLabel` swaps the plain title for an avatar + name using a
`resourceMeta` lookup keyed by person id (since `GanttResource` carries no custom fields):

```tsx
const resourceMeta: Record<string, { initials: string; avatar: string }> = {
  ada: { initials: "AL", avatar: "https://randomuser.me/api/portraits/women/44.jpg" },
  alan: { initials: "AT", avatar: "https://randomuser.me/api/portraits/men/32.jpg" },
  grace: { initials: "GH", avatar: "https://randomuser.me/api/portraits/women/68.jpg" },
  linus: { initials: "LT", avatar: "https://randomuser.me/api/portraits/men/54.jpg" },
}
```

`buildBars` seeds one 3-day assignment per teammate for "this week" (`Checkout API`, `Search
Indexing`, `Dashboard Redesign`, `Infra Migration`). The toolbar's "Add assignment" button
(`addAssignment`) cycles through `PEOPLE` via a `useRef` counter (not `useState`, so rapid clicks
stay correctly sequential) and a small `TASK_POOL` (`Bug triage`, `Code review`, `Spec draft`,
`Pairing`), adding a 2-day bar to the next teammate in rotation each click; successive adds to the
same person overlap and stack into extra lanes on that row. `offDays` shades weekends so real
working-day capacity reads at a glance.

## Project Status Report

Month-scale status report. Adds `Owner` and `Status` tree-panel columns beside the phase name via the
`columns` prop (each a `GanttColumn` with `id`, `title`, and a `render(ctx: GanttColumnContext)` cell
renderer), and every bar carries a `progress` fill (`buildBars` values include 100/60/45/0/0 across
`Design`, `Frontend`, `Backend`, `QA & Testing`, `Rollout`). Drag, resize, and slot-select are turned
off (`interactions={{ drag: false, resize: false, selectSlot: false }}` — the shipped default for all
three is `true`, so this example explicitly disables every one) so the plan can't be shifted by
dragging; the toolbar instead appends whole new task rows through controlled `resources` state
(`useState<GanttResource[]>(INITIAL_RESOURCES)`), i.e. the "add" affordance here grows the tree, not
just the bars.

## As-Built Baseline Tracking

Every bar in `buildBars` sets both `baselineStart`/`baselineEnd` (the frozen plan) alongside its
actual `start`/`end`; equal baseline instants render a planned milestone diamond (seen on the
`handover` bar: `bar("handover", 9, 1, 8, 0, "var(--color-amber-500)")` — a zero-length planned
window against a 1-day actual). Dragging a bar re-times the actual dates while the baseline ghost
holds still behind it; each bar exposes `data-baseline-variance="early|late|on-time"` for styling,
and the built-in tooltip names the planned range. The `Implementation` resource group additionally
sets `GanttResource.baselineStart`/`baselineEnd` directly on the node, which the view draws as a
faint band behind the WHOLE row (not per-bar) — this is what `renderRowBaseline`/`GanttRowBaselineProps`
in the API reference exist for. Ghosts can be disabled with `baselineBars={false}` or restyled via
`classNames.baseline`, `renderBaseline`, and `renderRowBaseline`.

## Dependencies and Milestones

A chained rollout: each `GanttEvent.dependencies` array names predecessor event ids, and
`dependencyLines` (default `true`) draws a finish-to-start elbow arrow from every predecessor's end
into the dependent's start, under the bars — for example
`bar("live", 9, 1, "var(--color-teal-500)", ["bar-signoff"])` draws one arrow in from the `Sign-off`
milestone. The zero-duration `Sign-off` event (`bar("signoff", 8, 0, "var(--color-amber-500)",
["bar-staging"])`) renders as a milestone diamond: it moves like any bar (staying a point under drag)
but has no resize edges, its title always sits beside it (never inside, since there is no bar body to
hold it), and screen readers hear the `milestone` i18n clause appended to its label. Turn the arrow
layer off with `dependencyLines={false}` or restyle it via `classNames.dependencies` (color flows
from `currentColor`).

## Source

- https://reui.io/docs/components/base/gantt (Base UI)
- https://reui.io/docs/components/radix/gantt (Radix UI)
- Mirrored 2026-09-04.
