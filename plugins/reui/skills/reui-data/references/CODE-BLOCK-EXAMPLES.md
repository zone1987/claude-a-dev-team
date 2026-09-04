# Code Block — examples

Part of [CODE-BLOCK.md](./CODE-BLOCK.md). Free component — no licence key required. Base UI build
(see [CODE-BLOCK.md#base-ui-vs-radix-ui](./CODE-BLOCK.md#base-ui-vs-radix-ui) — the upstream pages
state no code differences between builds for this component).

## Contents

- [Framing](#framing)
- [Scrolling](#scrolling)
- [Streaming and AI SDK](#streaming-and-ai-sdk)
- [Markdown code fences](#markdown-code-fences)
- [Dark Theme](#dark-theme)
- [Pinned copy button](#pinned-copy-button)
- [Diff](#diff)
- [Nested code folding](#nested-code-folding)
- [Fix with AI on the failing line](#fix-with-ai-on-the-failing-line)
- [Reference lines in chat](#reference-lines-in-chat)
- [Unified patch review](#unified-patch-review)
- [API Reference demo snippet](#api-reference-demo-snippet)
- [Source](#source)

## Framing

Tabs switching between framed, ghost `CodeBlock`s inside one dense `Frame`, so the set reads as one
editor.

```tsx
"use client"

import {
  CodeBlock,
  CodeBlockCopyButton,
} from "@/components/reui/code-block/code-block"
import {
  Frame,
  FrameHeader,
  FramePanel,
  FrameTitle,
} from "@/components/reui/frame"
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@/components/ui/tabs"

const samples = [
  {
    file: "greeting.tsx",
    language: "tsx",
    code: `export function Greeting({ name }: { name: string }) {
  return <p>Hello {name}</p>
}`,
  },
  {
    file: "greeting.py",
    language: "python",
    code: `def greeting(name: str) -> str:
    return f"Hello {name}"`,
  },
  {
    file: "greeting.sql",
    language: "sql",
    code: `select id, email
from users
where created_at > now() - interval '7 days';`,
  },
  {
    file: "greeting.sh",
    language: "bash",
    code: `curl -s https://api.example.com/v1/users \\
  -H "Authorization: Bearer $TOKEN"`,
  },
]

/*
 * One grammar chunk loads per selected language, so switching files is also a
 * lazy-loading demo.
 *
 * A dense frame is what makes this read as one editor: the panel meets the
 * header with no gap or inset, and the ghost block inside contributes no
 * second border. The tabs live in the header, so the blocks stay headerless
 * and the copy button pins itself over the code.
 */
export function Pattern() {
  return (
    <Tabs defaultValue={samples[0].file} className="w-full max-w-2xl">
      <Frame dense spacing="sm">
        <FrameHeader className="flex-row items-center gap-2">
          <FrameTitle>Examples</FrameTitle>
          <TabsList className="ml-auto bg-transparent">
            {samples.map((sample) => (
              <TabsTrigger key={sample.file} value={sample.file}>
                {sample.file}
              </TabsTrigger>
            ))}
          </TabsList>
        </FrameHeader>
        <FramePanel className="p-0!">
          {samples.map((sample) => (
            <TabsContent key={sample.file} value={sample.file}>
              <CodeBlock
                code={sample.code}
                language={sample.language}
                variant="ghost"
                showLineNumbers
              >
                <CodeBlockCopyButton
                  variant="outline"
                  size="icon-xs"
                  className="bg-card hover:bg-muted"
                />
              </CodeBlock>
            </TabsContent>
          ))}
        </FramePanel>
      </Frame>
    </Tabs>
  )
}
```

## Scrolling

Composed `CodeBlockContent` inside a `ScrollArea`, plus the `css-variables` theme mapped onto Tailwind
design tokens for both light and dark.

```tsx
import {
  CodeBlock,
  CodeBlockContent,
  CodeBlockCopyButton,
  CodeBlockHeader,
  CodeBlockTitle,
} from "@/components/reui/code-block/code-block"
import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"

const code = `export function useTheme() {
  const [theme, setTheme] = useState<"light" | "dark">("light")
  const toggle = () => setTheme((value) => (value === "light" ? "dark" : "light"))
  return { theme, toggle }
}`

/*
 * The "css-variables" theme emits var(--code-token-*) references instead of
 * hex colors, so the palette below IS the syntax theme: swap these lines for
 * your design tokens and the highlighting follows your brand in both modes.
 */
const paletteClass = [
  "[--code-token-keyword:var(--color-rose-600)]",
  "[--code-token-function:var(--color-violet-600)]",
  "[--code-token-string:var(--color-emerald-600)]",
  "[--code-token-string-expression:var(--color-emerald-600)]",
  "[--code-token-constant:var(--color-sky-600)]",
  "[--code-token-parameter:var(--color-amber-600)]",
  "[--code-token-comment:var(--muted-foreground)]",
  "[--code-token-punctuation:var(--foreground)]",
  "[--code-foreground:var(--foreground)]",
  "dark:[--code-token-keyword:var(--color-rose-400)]",
  "dark:[--code-token-function:var(--color-violet-400)]",
  "dark:[--code-token-string:var(--color-emerald-400)]",
  "dark:[--code-token-string-expression:var(--color-emerald-400)]",
  "dark:[--code-token-constant:var(--color-sky-400)]",
  "dark:[--code-token-parameter:var(--color-amber-400)]",
].join(" ")

export function Pattern() {
  return (
    <CodeBlock
      code={code}
      language="typescript"
      showLineNumbers
      themes={{ light: "css-variables", dark: "css-variables" }}
      className={"w-full max-w-2xl " + paletteClass}
    >
      <CodeBlockHeader>
        <CodeBlockTitle>use-theme.ts</CodeBlockTitle>
        <div className="ml-auto flex items-center gap-1.5">
          <span className="text-muted-foreground text-xs">
            Colors from design tokens
          </span>
          <CodeBlockCopyButton />
        </div>
      </CodeBlockHeader>
      {/* The ScrollArea composes INSIDE the block, so the block's own border
          and per-style radius stay the container, the header above never
          scrolls, and `max-h` means the area grows to the content instead of
          stretching past a short file. */}
      <ScrollArea className="rounded-[inherit] **:data-[slot=scroll-area-viewport]:max-h-72">
        <CodeBlockContent />
        <ScrollBar orientation="horizontal" />
      </ScrollArea>
    </CodeBlock>
  )
}
```

## Streaming and AI SDK

Simulated token-by-token stream (a `setTimeout` loop appending characters) driving `streaming` and a
Complete/Generating `Badge`. The sample deliberately omits its import statements — the registry
verifier scans raw file text for import shapes and would read them as real package dependencies of
the example, which then fails `registry:verify`.

```tsx
"use client"

import { useEffect, useState } from "react"
import { Badge } from "@/components/reui/badge"
import {
  CodeBlock,
  CodeBlockContent,
  CodeBlockCopyButton,
  CodeBlockHeader,
  CodeBlockLanguage,
  CodeBlockTitle,
} from "@/components/reui/code-block/code-block"
import { Button } from "@/components/ui/button"
import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"

const target = `export async function POST(request: Request) {
  const { messages } = await request.json()
  const result = streamText({
    model: openai("gpt-5"),
    system: "You are a concise assistant.",
    messages,
    temperature: 0.2,
    maxOutputTokens: 1024,
  })
  result.usage.then((usage) => {
    metrics.record("chat.tokens", usage.totalTokens)
  })
  return result.toUIMessageStreamResponse()
}`

export function Pattern() {
  const [length, setLength] = useState(0)
  useEffect(() => {
    if (length >= target.length) return
    const id = window.setTimeout(() => setLength((value) => value + 3), 24)
    return () => window.clearTimeout(id)
  }, [length])
  const done = length >= target.length

  return (
    <div className="flex w-full max-w-2xl flex-col gap-3">
      <CodeBlock
        code={target.slice(0, length)}
        language="typescript"
        showLineNumbers
        streaming={!done}
      >
        <CodeBlockHeader>
          <CodeBlockTitle>app/api/chat/route.ts</CodeBlockTitle>
          <CodeBlockLanguage />
          <div className="ml-auto flex items-center gap-1.5">
            <Badge variant={done ? "success-light" : "info-light"}>
              {done ? "Complete" : "Generating"}
            </Badge>
            <CodeBlockCopyButton />
          </div>
        </CodeBlockHeader>
        {/* The consumer's ScrollArea owns the scroll, and stick-to-bottom
            follows it: the primitive resolves the nearest scrolling ancestor
            per chunk, so the caret stays in view exactly as it does with the
            built-in viewport. */}
        <ScrollArea className="rounded-[inherit] **:data-[slot=scroll-area-viewport]:max-h-60">
          <CodeBlockContent />
          <ScrollBar orientation="horizontal" />
        </ScrollArea>
      </CodeBlock>
      <Button
        variant="outline"
        size="sm"
        className="self-start"
        onClick={() => setLength(0)}
      >
        Replay stream
      </Button>
    </div>
  )
}
```

## Markdown code fences

Chat transcript streaming a fenced reply; `markdownFences` splits prose from code and flags the
in-progress fence as `open` while it streams.

```tsx
"use client"

import { useEffect, useState } from "react"
import {
  CodeBlock,
  CodeBlockCopyButton,
  markdownFences,
} from "@/components/reui/code-block/code-block"
import {
  Frame,
  FrameDescription,
  FrameHeader,
  FramePanel,
  FrameTitle,
} from "@/components/reui/frame"
import {
  Avatar,
  AvatarFallback,
  AvatarImage,
} from "@/components/ui/avatar"

const reply = `Use the streaming helper, then render it:
\`\`\`tsx
const { messages } = useChat({ api: "/api/chat" })
\`\`\`
That keeps the transcript in sync.`

/*
 * `markdownFences` flags a fence whose closing delimiter has not arrived as
 * `open`, which is what lets the transcript render the partial block mid
 * stream instead of dropping it until the closer lands.
 */
export function Pattern() {
  const [length, setLength] = useState(0)
  useEffect(() => {
    if (length >= reply.length) return
    const id = window.setTimeout(() => setLength((value) => value + 4), 30)
    return () => window.clearTimeout(id)
  }, [length])
  const streamed = reply.slice(0, length)
  const streaming = length < reply.length

  return (
    <Frame dense className="w-full max-w-2xl">
      <FrameHeader>
        <FrameTitle>Assistant</FrameTitle>
        <FrameDescription>
          Generated responses may contain mistakes.
        </FrameDescription>
      </FrameHeader>
      <FramePanel className="flex flex-col gap-4">
        <div className="flex gap-3">
          <Avatar className="size-7 shrink-0 rounded-full">
            <AvatarImage
              src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=96&h=96&dpr=2&q=80"
              alt="Mira Stone"
            />
            <AvatarFallback className="text-[10px] font-medium">
              MS
            </AvatarFallback>
          </Avatar>
          <p className="pt-1 text-sm">How do I stream chat messages?</p>
        </div>
        <div className="flex gap-3">
          <Avatar className="size-7 shrink-0 rounded-full">
            <AvatarFallback className="bg-muted text-muted-foreground text-[10px] font-medium">
              AI
            </AvatarFallback>
          </Avatar>
          <div className="flex min-w-0 flex-1 flex-col gap-2 pt-1">
            {markdownFences(streamed).map((part, index) =>
              part.type === "text" ? (
                <p key={index} className="text-sm whitespace-pre-wrap">
                  {part.content}
                </p>
              ) : (
                <CodeBlock
                  key={index}
                  code={part.content}
                  language={part.language}
                  streaming={streaming && part.open}
                >
                  <CodeBlockCopyButton />
                </CodeBlock>
              )
            )}
          </div>
        </div>
      </FramePanel>
    </Frame>
  )
}
```

## Dark Theme

A marketing hero snippet forced dark via a wrapping `.dark` scope, combining `highlightedLines`,
`highlightedWords`, `diff`, and all three `lineLevels` at once.

```tsx
import {
  CodeBlock,
  CodeBlockCopyButton,
  CodeBlockHeader,
  CodeBlockTitle,
} from "@/components/reui/code-block/code-block"

const code = `export function Hero({ headline, snippet }: HeroProps) {
  const seats = useSeatCount()
  return (
    <section className="dark bg-background py-24">
      <h1 className="text-4xl font-semibold">{headline}</h1>
      <img src={cover} />
      <pre className="overflow-x-auto">{snippet}</pre>
      <CodeBlock code={snippet} language="tsx" showLineNumbers />
      <a onClick={goToPricing}>Start free</a>
      <p>{seats} seats claimed</p>
    </section>
  )
}`

/*
 * A block that stays dark in both site themes, the way marketing pages and
 * landing heroes usually want code to read. The `dark` class on the wrapper
 * re-scopes every semantic token inside it, so the primitive needs nothing:
 * the highlight, both diff tints, the three diagnostic levels and the word
 * mark all resolve against the dark palette here instead of the page's.
 */
export function Pattern() {
  return (
    <div className="dark w-full max-w-2xl">
      <CodeBlock
        code={code}
        language="tsx"
        showLineNumbers
        highlightedLines={[5]}
        highlightedWords={["useSeatCount"]}
        diff={{ removed: [8], added: [9] }}
        lineLevels={{ error: [10], warning: [7], info: [11] }}
      >
        <CodeBlockHeader>
          <span
            aria-hidden="true"
            className="flex shrink-0 items-center gap-1.5"
          >
            <span className="size-2.5 rounded-full bg-[#ff5f57]" />
            <span className="size-2.5 rounded-full bg-[#febc2e]" />
            <span className="size-2.5 rounded-full bg-[#28c840]" />
          </span>
          <CodeBlockTitle className="ml-1">hero.tsx</CodeBlockTitle>
          <CodeBlockCopyButton className="ml-auto" />
        </CodeBlockHeader>
      </CodeBlock>
    </div>
  )
}
```

## Pinned copy button

No header: the copy button pins over the code surface, hidden until hover/focus. Both scroll axes
belong to the consumer's `ScrollArea`.

```tsx
import {
  CodeBlock,
  CodeBlockContent,
  CodeBlockCopyButton,
} from "@/components/reui/code-block/code-block"
import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"

const code = `export async function resolveWorkspaceMembershipForActiveSubscription(workspaceId: string, userId: string) {
  const membership = await db.membership.findFirst({ where: { workspaceId, userId, status: "active" } })
  if (!membership) throw new WorkspaceAccessError("No active membership for this workspace")
  return membership
}

export function formatSeatSummary(seats: number, used: number) {
  return \`\${used} of \${seats} seats in use, \${Math.max(0, seats - used)} remaining\`
}

export function countBillableSeats(members: Member[]) {
  return members.filter((member) => member.status === "active" && !member.isGuest).length
}

export function canInviteMember(seats: number, used: number) {
  return used < seats
}`

/**
 * Both axes belong to the consumer's ScrollArea here: `CodeBlockContent`
 * hands the surface over without an internal scroll container, and the block
 * itself stays the bordered chrome. `max-h` rather than a fixed height, so a
 * short file does not leave dead space under the code.
 *
 * With no header the copy button pins itself over the code surface, hidden
 * until the block is hovered or the button takes focus. Line 1 scrolls
 * underneath it, so the button needs a backdrop of its own: `outline` draws
 * the border, and `bg-card` fills it (the variant's own dark fill is 4.5%
 * opaque, which the code shows through).
 */
export function Pattern() {
  return (
    <CodeBlock code={code} language="typescript" className="w-full max-w-2xl">
      <CodeBlockCopyButton
        variant="outline"
        size="icon-sm"
        className="bg-card hover:bg-muted"
      />
      {/* The cap goes on the ScrollArea VIEWPORT, not its root: the viewport
          is height-100% of the root, and a percentage against a max-height
          only parent resolves to auto, so a root-level cap clips without ever
          scrolling. */}
      <ScrollArea className="rounded-[inherit] **:data-[slot=scroll-area-viewport]:max-h-56">
        <CodeBlockContent />
        <ScrollBar orientation="horizontal" />
      </ScrollArea>
    </CodeBlock>
  )
}
```

## Diff

Line state comes straight from props here — the simplest form. For a real patch, see Unified patch
review below.

```tsx
import {
  CodeBlock,
  CodeBlockCopyButton,
  CodeBlockHeader,
  CodeBlockTitle,
} from "@/components/reui/code-block/code-block"

const code = `export function getCacheKey(request: Request) {
  const url = new URL(request.url)
  return url.href
  url.searchParams.delete("utm_source")
  url.searchParams.delete("utm_medium")
  url.searchParams.sort()
  return url.toString()
}`

export function Pattern() {
  return (
    <div className="w-full max-w-2xl">
      <CodeBlock
        code={code}
        language="typescript"
        showLineNumbers
        diff={{ added: [4, 5, 6, 7], removed: [3] }}
      >
        <CodeBlockHeader>
          <CodeBlockTitle>lib/cache-key.ts</CodeBlockTitle>
          <CodeBlockCopyButton className="ml-auto" />
        </CodeBlockHeader>
      </CodeBlock>
    </div>
  )
}
```

## Nested code folding

Regions come from indentation rather than the grammar, so folding works in every language the block
can render. Folding an outer region swallows the inner toggles and leaves their own state untouched
underneath.

```tsx
"use client"

import { useState } from "react"
import {
  CodeBlock,
  CodeBlockContent,
  CodeBlockCopyButton,
  CodeBlockHeader,
  CodeBlockTitle,
} from "@/components/reui/code-block/code-block"
import { Button } from "@/components/ui/button"
import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area"
import { Separator } from "@/components/ui/separator"

const code = `export async function syncWorkspace(workspaceId: string) {
  const workspace = await db.workspace.findUnique({ where: { id: workspaceId } })
  if (!workspace) {
    throw new WorkspaceNotFoundError(workspaceId)
  }
  const members = await db.member.findMany({ where: { workspaceId } })
  for (const member of members) {
    if (member.status === "invited") {
      await mail.send({
        to: member.email,
        template: "workspace-reminder",
      })
    }
  }
  return { synced: members.length }
}`

/*
 * The block detects its own regions from indentation, so the only reason this
 * list exists is the "Fold all" button: the snippet is a literal here, so its
 * region starts are known without asking the primitive for them.
 *
 * The ScrollArea composes INSIDE the block, under the header, so the fold
 * controls never scroll away and the block's own chrome stays the container.
 */
const REGION_STARTS = [1, 4, 10, 11, 12]

export function Pattern() {
  /* Opens with the inner branch folded, so the nesting is visible at a glance:
     folding line 10 swallows it, and unfolding 10 brings it back still
     folded. */
  const [folded, setFolded] = useState<number[]>([11])

  return (
    <CodeBlock
      code={code}
      language="typescript"
      showLineNumbers
      className="w-full max-w-2xl"
      foldable
      folded={folded}
      onFoldedChange={setFolded}
    >
      <CodeBlockHeader className="gap-1.5">
        <CodeBlockTitle>sync-workspace.ts</CodeBlockTitle>
        <div className="ml-auto flex items-center gap-1">
          <Button
            size="xs"
            variant="ghost"
            onClick={() => setFolded(REGION_STARTS)}
          >
            Fold all
          </Button>
          <Button
            size="xs"
            variant="ghost"
            disabled={!folded.length}
            onClick={() => setFolded([])}
          >
            Unfold all
          </Button>
          <Separator orientation="vertical" className="h-4" />
          <CodeBlockCopyButton />
        </div>
      </CodeBlockHeader>
      <ScrollArea className="rounded-[inherit] **:data-[slot=scroll-area-viewport]:max-h-72">
        <CodeBlockContent />
        <ScrollBar orientation="horizontal" />
      </ScrollArea>
    </CodeBlock>
  )
}
```

## Fix with AI on the failing line

The render prop receives each line's state, so one action group serves the whole block and still only
offers the fix where a diagnostic actually sits.

```tsx
"use client"

import { useState } from "react"
import { Badge } from "@/components/reui/badge"
import {
  CodeBlock,
  CodeBlockHeader,
  CodeBlockLineActions,
  CodeBlockTitle,
} from "@/components/reui/code-block/code-block"
import { Button } from "@/components/ui/button"
import { SparklesIcon } from 'lucide-react'

const broken = `export function totalDue(invoice: Invoice) {
  const lines = invoice.lines.map((line) => line.amount)
  const subtotal = lines.reduce((sum, amount) => sum + amount)
  return subtotal + invoice.tax
}`

const patched = `export function totalDue(invoice: Invoice) {
  const lines = invoice.lines.map((line) => line.amount)
  const subtotal = lines.reduce((sum, amount) => sum + amount, 0)
  return subtotal + invoice.tax
}`

export function Pattern() {
  const [fixed, setFixed] = useState(false)

  return (
    <div className="w-full max-w-2xl">
      <CodeBlock
        code={fixed ? patched : broken}
        language="typescript"
        showLineNumbers
        lineLevels={fixed ? undefined : { error: [3] }}
      >
        <CodeBlockHeader>
          <CodeBlockTitle>invoice.ts</CodeBlockTitle>
          <div className="ml-auto flex items-center gap-1.5">
            {fixed ? (
              <>
                <Badge variant="success-light">Patch applied</Badge>
                <Button
                  size="xs"
                  variant="ghost"
                  onClick={() => setFixed(false)}
                >
                  Undo
                </Button>
              </>
            ) : (
              <Badge variant="destructive-light">
                Empty array crashes reduce
              </Badge>
            )}
          </div>
        </CodeBlockHeader>
        {/*
          The action is scoped to the line that actually carries the diagnostic:
          the render prop receives that line's state, so one group serves the
          whole block and still only offers the fix where there is something to
          fix.
        */}
        <CodeBlockLineActions>
          {({ state }) =>
            state?.level === "error" ? (
              <Button size="xs" onClick={() => setFixed(true)}>
                <SparklesIcon />
                Fix with AI
              </Button>
            ) : null
          }
        </CodeBlockLineActions>
      </CodeBlock>
    </div>
  )
}
```

## Reference lines in chat

`side="gutter"` moves the control into the channel beside the line number, where an editor puts it.
Pressing it turns the hovered line, or the current selection via `useCodeBlockSelection`, into
`file:line` reference badges in the composer below.

```tsx
"use client"

import { useState } from "react"
import { Badge } from "@/components/reui/badge"
import {
  CodeBlock,
  CodeBlockHeader,
  CodeBlockLineActions,
  CodeBlockTitle,
  useCodeBlockSelection,
} from "@/components/reui/code-block/code-block"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { PlusIcon, XIcon } from 'lucide-react'

const FILE = "use-mobile.ts"
const PATH = "src/hooks/use-mobile.ts"

const code = `import { useEffect, useState } from "react"
const MOBILE_BREAKPOINT = 768
export function useIsMobile() {
  const [isMobile, setIsMobile] = useState<boolean>()
  useEffect(() => {
    const mql = window.matchMedia("(max-width: 767px)")
    const onChange = () => {
      setIsMobile(window.innerWidth < MOBILE_BREAKPOINT)
    }
    mql.addEventListener("change", onChange)
    setIsMobile(window.innerWidth < MOBILE_BREAKPOINT)
    return () => mql.removeEventListener("change", onChange)
  }, [])
  return !!isMobile
}`

/*
 * The gutter button turns code into REFERENCES: press + on a line and the
 * composer below gains a file:line badge, or select a range first and one
 * press references every selected line. `useCodeBlockSelection` is what makes
 * the range case possible - the render prop alone only knows its own line.
 */
function AddToChat({
  line,
  onAdd,
}: {
  line: number
  onAdd: (lines: number[]) => void
}) {
  const { selectedLines, clearSelection } = useCodeBlockSelection()
  const batch = selectedLines.length > 0 ? selectedLines : [line]
  return (
    <Button
      type="button"
      size="icon-xs"
      aria-label={
        batch.length > 1
          ? `Reference ${batch.length} selected lines in the chat`
          : `Reference line ${line} in the chat`
      }
      title={
        batch.length > 1
          ? `Reference ${batch.length} lines`
          : `Reference line ${line}`
      }
      onClick={() => {
        onAdd(batch)
        clearSelection()
      }}
      /* Trimmed below the icon-xs rung: the control hangs over the line
         numbers, so a full 24px chip covers the digits it floats above. */
      className="size-5"
    >
      <PlusIcon />
    </Button>
  )
}

export function Pattern() {
  const [refs, setRefs] = useState<number[]>([])
  const [highlighted, setHighlighted] = useState<number | null>(null)
  const addLines = (lines: number[]) =>
    setRefs((current) =>
      [...new Set([...current, ...lines])].sort((a, b) => a - b)
    )

  return (
    <div className="flex w-full max-w-2xl flex-col gap-3">
      <CodeBlock
        code={code}
        language="typescript"
        showLineNumbers
        selectable
        highlightedLines={highlighted === null ? undefined : [highlighted]}
      >
        <CodeBlockHeader>
          <CodeBlockTitle>{FILE}</CodeBlockTitle>
          <span className="text-muted-foreground ml-auto text-xs">
            Press + on a line to reference it
          </span>
        </CodeBlockHeader>
        <CodeBlockLineActions side="gutter">
          {({ line }) => <AddToChat line={line} onAdd={addLines} />}
        </CodeBlockLineActions>
      </CodeBlock>
      {/* The composer the references land in. A Card, not a hand-rolled
          bordered div, so its radius resolves per style. */}
      <Card size="sm" className="gap-2 p-3">
        <div className="flex flex-wrap items-center gap-1.5">
          {refs.length === 0 ? (
            <span className="text-muted-foreground px-1 text-sm">
              Ask about {FILE}...
            </span>
          ) : (
            refs.map((line) => (
              <Badge
                key={line}
                variant={highlighted === line ? "primary-light" : "outline"}
                title={`${PATH}:${line}`}
                className="gap-0.5 font-mono"
              >
                {/* Two actions per chip, so two real buttons: the label
                    highlights the referenced line in the block above through
                    `highlightedLines`, the X removes the reference. */}
                <Button
                  variant="ghost"
                  size="xs"
                  aria-pressed={highlighted === line}
                  aria-label={`Highlight line ${line} in the code`}
                  onClick={() =>
                    setHighlighted((current) =>
                      current === line ? null : line
                    )
                  }
                  className="h-auto p-0 font-mono hover:bg-transparent"
                >
                  {FILE}:{line}
                </Button>
                <Button
                  variant="ghost"
                  size="icon-xs"
                  aria-label={`Remove the reference to line ${line}`}
                  onClick={() => {
                    setRefs((current) =>
                      current.filter((value) => value !== line)
                    )
                    setHighlighted((current) =>
                      current === line ? null : current
                    )
                  }}
                  className="size-4 hover:bg-transparent [&_svg]:size-2.5"
                >
                  <XIcon />
                </Button>
              </Badge>
            ))
          )}
        </div>
        <div className="flex items-center gap-2">
          <span className="text-muted-foreground text-xs">
            {refs.length > 0
              ? `${refs.length} ${refs.length === 1 ? "line" : "lines"} in context`
              : "No context yet"}
          </span>
          <Button size="xs" className="ml-auto" disabled={!refs.length}>
            Ask AI
          </Button>
        </div>
      </Card>
    </div>
  )
}
```

Note: the upstream mirrored page's own "Reference lines in chat" section body shows only placeholder
"Copy" / "View Code" markers with no inline source; the full source above is reconstructed from the
identical code block that appears later on the same page under the API Reference / Accessibility
section (the page reuses this exact example there). Both locations on the upstream page carry the same
`Pattern()` implementation.

## Unified patch review

`parseUnifiedDiff` turns a git patch into per-file lines: tints, `+`/`-` glyphs and the dual old/new
gutter numbers all come from the parse, and the download button saves each file's patch.

```tsx
import { Badge } from "@/components/reui/badge"
import {
  CodeBlock,
  CodeBlockDownloadButton,
  CodeBlockHeader,
  CodeBlockTitle,
  parseUnifiedDiff,
} from "@/components/reui/code-block/code-block"

const patch = `diff --git a/lib/seats.ts b/lib/seats.ts
--- a/lib/seats.ts
+++ b/lib/seats.ts
@@ -12,7 +12,8 @@ export async function countBillableSeats(workspaceId: string) {
   const members = await db.member.findMany({ where: { workspaceId } })
-  const used = members.length
+  const used = members.filter((member) => !member.isGuest).length
+  if (used < 0) throw new SeatCountError(workspaceId)
   return { used, total: await seatAllowance(workspaceId) }
 }
diff --git a/app/api/invites/route.ts b/app/api/invites/route.ts
--- a/app/api/invites/route.ts
+++ b/app/api/invites/route.ts
@@ -3,6 +3,7 @@ export async function POST(request: Request) {
   const { email } = await request.json()
+  if (!email) return new Response("email required", { status: 422 })
   const invite = await createInvite(session.workspaceId, email)
   return Response.json(invite, { status: 201 })
 }`

/*
 * The whole review renders from ONE `parseUnifiedDiff` call: tints, +/-
 * glyphs and the dual old/new gutter numbers all come out of the parse, so
 * nothing here counts lines against a hand-concatenated string. The parsed
 * lines go in through the `lines` prop, which also means no highlighter runs.
 */
const files = parseUnifiedDiff(patch)

export function Pattern() {
  return (
    <div className="flex w-full max-w-2xl flex-col gap-3">
      {files.map((file) => (
        <CodeBlock
          key={file.file}
          lines={file.lines}
          showLineNumbers
          label={`Patch for ${file.file}`}
        >
          <CodeBlockHeader>
            <CodeBlockTitle>{file.file}</CodeBlockTitle>
            <div className="ml-auto flex items-center gap-1.5">
              <Badge variant="success-light">+{file.added}</Badge>
              <Badge variant="destructive-light">-{file.removed}</Badge>
              <CodeBlockDownloadButton
                filename={`${file.file.split("/").pop()}.patch`}
              />
            </div>
          </CodeBlockHeader>
        </CodeBlock>
      ))}
    </div>
  )
}
```

## API Reference demo snippet

The plain use-totals example shown inline in the API Reference section:

```tsx
import {
  CodeBlock,
  CodeBlockCopyButton,
  CodeBlockHeader,
  CodeBlockLanguage,
  CodeBlockTitle,
} from "@/components/reui/code-block/code-block"

const code = `export function useTotals(items: Item[]) {
  return useMemo(() => {
    const subtotal = items.reduce((sum, item) => sum + item.price, 0)
    const tax = Math.round(subtotal * 0.2)
    return { subtotal, tax, total: subtotal + tax }
  }, [items])
}`

export function Pattern() {
  return (
    <div className="w-full max-w-2xl">
      <CodeBlock code={code} language="typescript" showLineNumbers>
        <CodeBlockHeader>
          <CodeBlockTitle>use-totals.ts</CodeBlockTitle>
          <CodeBlockLanguage />
          <CodeBlockCopyButton className="ml-auto" />
        </CodeBlockHeader>
      </CodeBlock>
    </div>
  )
}
```

## Source

- https://reui.io/docs/components/base/code-block (Base UI)
- https://reui.io/docs/components/radix/code-block (Radix UI)
- Mirrored 2026-09-04.
