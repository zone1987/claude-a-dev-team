---
name: pz-items
description: "Project Zomboid item scripts: every item property and enum, plus all 5,105 items with type, module, capacity and weight, and how to extract the ~4,400 item icons out of the game's sprite atlases. Use when defining a Project Zomboid item, naming Capacity, or showing a real item icon outside the game."
---

# Project Zomboid items

An item is defined in a script file under `media/scripts`, in a `module` block, as
`item Name { Key = value, }`. Its module and name together form its id: `Base.Shovel`. A mod defines
items the same way, and a mod that reuses an existing id **replaces** that item rather than adding to
it — that is the override mechanism, and load order decides who wins.

At runtime each definition becomes a `zombie.scripting.objects.Item` object, and each instance in the
world an `InventoryItem`. Those are different things: the first is the template, the second the
thing in a container. Changing the template does not retroactively change instances already spawned.

## Reference map

The property catalogue and the data tables are generated from the game's own files, so they are
complete for build 42 by construction.

- **[references/PROPERTY-CATALOGUE.md](references/PROPERTY-CATALOGUE.md)**: every property that occurs on every script block type, how many blocks set it, and every distinct value where the set is enum-sized. 2,172 property entries. This answers "what can I set" and "what values are legal".
- **[references/DATA-ITEM.md](references/DATA-ITEM.md)**: all 5,105 items with module, `Type`, `DisplayCategory`, `Weight`, `Capacity`, `WeightReduction`, damage values, `ItemType` and the file each is defined in.
- **[references/ITEM-FIELDS.md](references/ITEM-FIELDS.md)**: the 239 public fields of the runtime `Item` object, each with its setter and getter where one exists — 95 setters, 76 field/setter pairs. This is what makes runtime mutation possible, and it distinguishes a field you assign directly from one with a setter.
- **[references/ITEM-ICONS.md](references/ITEM-ICONS.md)**: where item icons actually live — ~4,400 of them are packed into sprite atlases under `media/texturepacks/`, not shipped as files. Documents both pack layouts, the three traps that make a hand-written reader return almost nothing, and why an icon name cannot be derived from the item id (`Base.Disinfectant` → `Item_Alcohol`). Use with `scripts/extract_item_icons.py`.

The other block types have their own generated tables: **[DATA-MODEL.md](references/DATA-MODEL.md)** (3,836), **[DATA-SOUND.md](references/DATA-SOUND.md)** (3,038), **[DATA-TABLE.md](references/DATA-TABLE.md)** (267), **[DATA-XUISKIN.md](references/DATA-XUISKIN.md)** (254), **[DATA-AREA.md](references/DATA-AREA.md)** (154), **[DATA-TIMEDACTION.md](references/DATA-TIMEDACTION.md)** (119), **[DATA-PHYSICSSHAPE.md](references/DATA-PHYSICSSHAPE.md)** (90), **[DATA-ANIMATIONSMESH.md](references/DATA-ANIMATIONSMESH.md)** (75), **[DATA-RAGDOLL.md](references/DATA-RAGDOLL.md)** (66), **[DATA-PHYSICS.md](references/DATA-PHYSICS.md)** (62), **[DATA-ANIM.md](references/DATA-ANIM.md)** (59), **[DATA-ATTACHMENT.md](references/DATA-ATTACHMENT.md)** (52), **[DATA-MANNEQUIN.md](references/DATA-MANNEQUIN.md)** (30), **[DATA-PHYSICSHITREACTION.md](references/DATA-PHYSICSHITREACTION.md)** (10), **[DATA-CLOCK.md](references/DATA-CLOCK.md)**, **[DATA-ENERGY.md](references/DATA-ENERGY.md)**, **[DATA-ANIMATION.md](references/DATA-ANIMATION.md)**, **[DATA-VEHICLEENGINERPM.md](references/DATA-VEHICLEENGINERPM.md)**, **[DATA-XUICONFIG.md](references/DATA-XUICONFIG.md)**.

- **[references/XML-DATA.md](references/XML-DATA.md)**: the XML data directories nothing else documents — clothing and its decals (1,857 files), action groups (3,203), animation sets (2,949), animation states, hair and beard styles, voice styles and radio content. Every element path with its frequency, its attributes and its value sets, so a mod adding clothing or an animation writes the right shape.

## Changing an existing item

Three routes, and they differ in what they touch:

1. **Redefine it in a script** — your mod ships an `item` block with the same id. Applies from load,
   affects every instance, survives saves, and is identical on client and server because both load
   the scripts. This is the route for a permanent change.
2. **Assign the runtime field** on the `Item` template. Takes effect for instances created after the
   change. Lost on restart unless your mod reapplies it on load.
3. **Change the instance** through `InventoryItem`. Affects that one object only.

For a change that must hold on a dedicated server, route 1 is the safe answer, because the server and
every client agree by construction. A runtime change made only client-side is a desync.

**An unset property is not zero.** It takes the engine's default, which the catalogue cannot show —
so read the game's own definition of a similar item before assuming a baseline.

## Related

Call the Skill tool with "pz-crafting" for recipes that consume and produce items, "pz-java-api" for
`Item`, `InventoryItem` and `ItemContainer`, "pz-lua-api" for the Lua that manipulates them, and
"pz-multiplayer" for what has to sync.

## Source

Generated by `scripts/build_script_data.py` and `scripts/build_item_fields.py` from Project Zomboid
build 42, `media/scripts` (1,004 files, sha256 `d4a48ede8b5cb907`), installed at
`~/Library/Application Support/Steam/steamapps/common/ProjectZomboid/Project Zomboid.app/Contents/Java`,
retrieved 2026-08-26.

The game's own files are the primary source; the API is cross-checked against the build 42 JavaDocs at <https://projectzomboid.com/modding/index.html> and the unofficial build <https://github.com/demiurgeQuantified/ProjectZomboidJavaDocs>.
