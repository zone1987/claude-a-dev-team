---
name: sw-flow-action
description: Scaffolds a Shopware 6 flow builder action (PHP plus an admin component) including its requirements and registration.
argument-hint: <Name> [--plugin <PluginName>] [--aware order|customer]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-flow-action

Produce a flow action. Skill: `sw-automation`.

## Steps
1. Settle the action name (`action.<owner>.<verb>`, e.g. `action.ff.notify`), the target plugin, and
   the aware data it needs (e.g. OrderAware).
2. PHP: `src/Core/Content/Flow/Dispatching/Action/<Name>Action.php` (`getName`, `requirements`,
   `handleFlow(StorableFlow)`), registered through the `flow.action` tag.
3. The admin component (`sw-flow-action-…`) for its configuration, registered with the flow action
   service.
4. Note the follow-up: keep it transactional with respect to the business process, and make external
   calls fault-tolerant and idempotent.

Need a trigger of your own as well? See `sw-automation`. Never overwrite an existing action.

## Before it counts as done

`composer gate` green, unit tests for `handleFlow()`, and the action proved end-to-end:
selectable in the Flow Builder and running when its trigger fires.
→ `shopware-testing` → `sw-testing-standard`
