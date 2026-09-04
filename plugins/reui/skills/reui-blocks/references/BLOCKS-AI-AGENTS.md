# Premium blocks — AI & Agents

Generated from `https://reui.io/r/registry.json` (sha256 `a598d3b8b544a0fa`) by `scripts/gen_registry_refs.py`. 12 entries. Do not edit by hand.

**Licence: Pro or Ultimate.** Install with `shadcn add @reui/<name>` once `REUI_LICENSE_KEY` is set.

## ai-chat (12)

### `ai-chat-1`

AI copilot chat surface with streaming transcript and recent chats

Full page AI copilot chat surface with a streaming transcript, a tabbed header thread switcher over pinned and recent chats, a starter view of prompt and thread shortcuts, model switching, and a docked composer with removable context chips.

Uses: `@reui/alert`, `@reui/badge`, `@reui/code-block`, `@reui/code-block-highlight`, `@reui/frame`

npm: `sonner`

### `ai-chat-2`

Docked AI assistant chat panel beside a page with insert into draft

Sticky right side AI copilot beside a page: streaming thread, grouped Message bubbles, markdown code block, model picker, quick replies, and an Insert action that writes the reply into the document. Sheet on mobile.

Uses: `@reui/badge`, `@reui/code-block`, `@reui/code-block-highlight`, `@reui/icon-stack`, `@reui/icon-tile`

### `ai-chat-3`

AI chat welcome screen with prompt starters and a docked composer

AI assistant welcome screen and zero state: an Empty greeting with live workspace stats, one rail of start and resume rows that fill the composer and attach context, an InputGroup composer with Attachment chips, and a streaming reply with Stop. A new chat page with prompt suggestions and recent conversations.

Uses: `@reui/badge`, `@reui/code-block`, `@reui/icon-tile`

npm: `sonner`

### `ai-chat-4`

Floating right chat sidebar that pushes the page and replies to a quoted sentence

Reveal and hide a floating AI panel beside any page: select a sentence in an answer to reply to that line, a keyboard suggestion palette, a workspace Personalize toggle, thread switcher, model and mode picker, and a designed thinking indicator.

Uses: `@reui/badge`, `@reui/icon-stack`

npm: `sonner`

### `ai-chat-5`

AI chat welcome screen where connected work apps set the answer scope

A centered new chat screen whose composer sits in a ReUI Frame: the panel is the box you type into and the frame footer is a live integrations strip of Google Drive, Slack, Calendar, Dropbox, OneDrive, Box, Zoom and Loom. Switching a logo on or off changes what the assistant may read, four job modes rewrite the prompt, and sending returns a receipt per source with a Connect action on anything that was skipped.

Uses: `@reui/frame`

### `ai-chat-6`

Agentic side panel where the answers carry the controls

A docked AI panel that runs a task end to end: confirm which workspace sources and attached files the agent may read, edit and run an ordered plan step by step, retry a step that fails, answer the question the agent raises mid run to drop a branch from its own plan, then assign the finished work as a ticket with the files the run produced. Model picker, live run status in the header, and a rewind whenever the context changes.

Uses: `@reui/badge`, `@reui/code-block`, `@reui/icon-stack`

npm: `sonner`

### `ai-chat-7`

Split pane model comparison running one prompt against two AI models

Side by side compare view: two resizable panes answer one docked prompt and stream at different speeds, with sortable data tables in the replies, a scroll lock that reads both answers at the same depth, and per answer copy and rating actions. Select a line to ask both models about it, regenerate or swap either pane, attach extra files, and watch a mirrored scoreboard for latency, output rate and cost settle into a verdict with an A or B vote.

Uses: `@reui/alert`, `@reui/badge`, `@reui/code-block`

### `ai-chat-8`

Docked voice first assistant panel that answers in a different shape each time

A floating assistant panel beside any page, driven by voice as readily as typing. Hold the mic and the take lands as a playable turn with a scrubbable transport and its transcription, then the answer arrives in whichever shape the question deserves: a move plan behind an approval gate, a set of times to choose between, a roster of who is free, a figure summary, a callout that carries its own next action, a trace of the steps taken, or prose with the documents it quoted. Also carries a thread switcher, meeting attachments, citation chips you can turn off, and a widen toggle.

Uses: `@reui/alert`, `@reui/badge`, `@reui/icon-stack`

### `ai-chat-9`

Branching AI chat thread with reply versions, cited sources and code artifacts

A standalone conversation under one minimal header: a tabbed thread switcher over pinned and recency lists, a favorite toggle and a fold for earlier turns, above replies that arrive as small documents with sections, bullets and code artifacts in markdown, yaml, json, typescript and sql, each one folding its working away behind a thought row and listing the sources its inline citations point back to, over a thread held as a tree so a regenerate or an edit adds a version on the fork rail instead of overwriting the turn.

Uses: `@reui/badge`, `@reui/code-block`, `@reui/icon-stack`

npm: `sonner`

### `ai-chat-10`

AI chat welcome screen with scoped sources and structured answers

Launch surface for a source grounded copilot: a greeting, a framed ask box whose header toggles which files the chat may read, and three starter asks. Replies come back as structured documents, with sortable tables, Shiki highlighted code artifacts and proportional comparison bars beside the prose. A file switched off is named as a gap rather than guessed around.

Uses: `@reui/badge`, `@reui/code-block`, `@reui/frame`

npm: `sonner`

### `ai-chat-11`

AI chat stage with framed answer receipts on a live dot field

A self contained chat surface floating on an animated dot field. Asks stay bubbles while every reply renders as a framed receipt carrying the run behind it, a tool trace, a metric row or a code patch, with model, latency and token cost in the chrome bar. Streaming, stop, retry, thread switching and a scoped source picker are all live.

Uses: `@reui/badge`, `@reui/frame`

### `ai-chat-12`

Ask AI docs support panel that shows the knowledge base being read

A support assistant docked to a documentation page as a hideable right sidebar, answering only from the product knowledge base and showing its work while it does. Every question runs a visible retrieval: the search, then each matched article ticking from queued to read, then the write, and the finished answer folds that reading into a receipt naming how many articles were read and how many survived into the answer. Answers arrive as prose with numbered steps and a caveat, carry helpful and not helpful voting, and when the documentation genuinely does not cover a question the assistant says so and opens a support ticket instead of guessing.

Uses: `@reui/icon-stack`

