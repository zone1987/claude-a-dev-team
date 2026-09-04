# Plans

Free vs Pro vs Ultimate, stated as facts (pricing/marketing enthusiasm removed).

Team size selector on the pricing page offers: Personal, Team, Growth, Enterprise. The full
comparison table shown below is captured under the "Personal" team-size selection — the mirrored
page does not show line-item content that differs for Team/Growth/Enterprise (see Gaps below).

## Plan comparison table

| Feature | Free | Pro | Ultimate |
|---|---|---|---|
| Price | $0, forever, no account required | $249 USD, one-time payment | $499 USD, one-time payment |
| Users | No auth needed | 1 user access | 1 user access |
| Free Components | 1105 — Included | Included | Included |
| ReUI Primitives | 21 — Included | Included | Included |
| Free Figma | Included | Included | Included |
| Free Updates | Included (see Changelog) | Included | Included |
| Unlimited Commercial Usage | Included (see License) | Included | Included |
| Registry | Included | Included | Included |
| Agent Skills | Included | Included | Included |
| MCP Server | Included | Included | Included |
| MCP Requests | 100 / day | Unlimited | Unlimited |
| Shared team access | Not included | Not included | Not included |
| Team management | Not included | Not included | Not included |
| Pro Blocks | 533 — Not included | Included | Included |
| Icons | 2552 — Not included | Not included | Included |
| Full Page Templates | 14 — Not included | Not included | Included |
| Support | Community | Email | Email |

Pro is marked "Best Value" on the pricing page (marketing label, kept as a fact of the page's
labeling, not a recommendation).

Payment: "Secure 256-bit SSL encrypted payments" via Paddle. "The standard local tax rate may be
charged, following the law of your country." Pro/Ultimate purchases are described as "One-time
payment + Local taxes · Lifetime access to updates."

## What each plan unlocks (explicit, per RULES)

- **Free**: 1105 free components, all 21 ReUI primitives, free Figma file, free updates,
  unlimited commercial usage license, registry access, Agent Skills, MCP server access capped at
  **100 MCP tool calls/day**, community support. No account required for registry access ("No
  auth needed").
- **Pro** ($249, one-time): everything in Free, plus all 533 Pro Blocks, **unlimited MCP
  requests** (daily cap removed), email support. Does NOT include Icons or Full Page Templates.
- **Ultimate** ($499, one-time): everything in Pro, plus all 2552 Icons and all 14 Full Page
  Templates, email support.

The icon counts differ across pages, and the machine-readable index resolves it: the 30 icon
categories in [`llms.txt`](https://reui.io/llms.txt) sum to exactly **638 icons**, which at 4 styles
each gives the **2,552 variants** this pricing table counts. The Introduction page's "562 icons" is
a stale figure. So: 638 icons, 2,552 installable variants, Ultimate only.

## Free vs Pro vs Ultimate quick reference (for use elsewhere in this skill)

- Components (21 primitives) and Examples (1,000+): **Free**, no license key needed.
- Blocks (533 in this page's count / 485+ per the Introduction page): **Pro or Ultimate**.
- Icons: **Ultimate only**.
- Full Page Templates (14): **Ultimate only**.
- MCP server access itself: **Free** at every tier; the tier changes only the **daily MCP request
  cap** (100/day on Free, unlimited on Pro/Ultimate) — see the reui-mcp skill's
  TROUBLESHOOTING.md for the 429 error this produces.

## Gaps

The pricing page's FAQ section lists question headings only — "What's included in the library?",
"What is ReUI and what should I use it for?", "What's the difference between shadcn blocks and
components?", "What are 'ReUI custom primitives' and how do they differ from shadcn/ui?", "Can I
see the code before I buy?", "How do I install shadcn blocks and components?", "Can I modify the
components after installing?", "Are the free shadcn components really free to use?", "Does ReUI
support dark mode and theme customization?", "What is the Free shadcn/ui Figma Design System by
ReUI for?", "Are the components accessible (a11y / WCAG)?", "Does ReUI work with AI coding agents
like Codex, Claude, Cursor, OpenCode, Copilot and others?", "How do I get updates and support?" —
under tabs Product / AI Tools / Pricing / Licenses. **The mirrored markdown does not capture the
answer text** (collapsed accordion content not present in the static extraction). This is a real
gap in the mirror, not an omission by this distillation: no answer content exists in the source
file to extract.

The testimonial/social-proof section ("Trusted by builders", named individuals' quotes) is
marketing content with no technical facts and is intentionally excluded per the neutralize-tone
rule.

## Source

https://reui.io/pricing — mirrored 2026-09-04.
