# Item icons

Where the item icons live, how to get them out, and the exact byte layout of the packs that hold
them. Measured against build 42.20.2 with `scripts/extract_item_icons.py`.

## Contents

- [Extracting them](#extracting-them)
- [What is in there](#what-is-in-there)
- [The icon name is not derivable from the item id](#the-icon-name-is-not-derivable-from-the-item-id)
- [The pack format](#the-pack-format)
  - [Reading it, exactly](#reading-it-exactly)
  - [Verified byte trace](#verified-byte-trace)
- [Loose icons](#loose-icons)

## Extracting them

The game does not ship item icons as individual files. Roughly a hundred sit loose in `media/ui/`;
the other ~4,400 are packed into sprite atlases under `media/texturepacks/*.pack`. Anything that
displays a real item icon outside the game — a control panel, a loot planner, a wiki — has to unpack
them first.

`scripts/extract_item_icons.py` does that. It reads every pack, crops each `Item_*` sprite out of its
atlas and writes one image per icon plus an index.

```
python3 scripts/extract_item_icons.py \
  --game "~/Library/Application Support/Steam/steamapps/common/ProjectZomboid/Project Zomboid.app/Contents/Java" \
  --out pz-icons --webp
```

`--list` prints what is there without writing (and needs no Pillow). `--only Item_Axe,Item_Bandage`
extracts a subset. `--webp` is worth taking: 4,363 icons come to 18 MB as WebP.

**The extracted images are The Indie Stone's assets.** Keep them out of any repository and out of
anything you publish; extract at build time or on the user's own machine.

## What is in there

Measured on build 42.20.2:

| Pack | `Item_*` sprites | Layout |
|---|---|---|
| `UI2.pack` | 3,848 | PZPK |
| `UI.pack` | 563 | legacy |
| `ApComUI.pack` | 44 | legacy |
| `RadioIcons.pack` | 13 | legacy |
| `IconsMoveables.pack` | 7 | legacy |

4,475 sprites across 15 atlas pages; 4,363 distinct names after de-duplication (a few appear in more
than one pack — later packs win). Icons are small pixel art, mostly 29–32 px square, so render them
with `image-rendering: pixelated` rather than smooth scaling.

Names starting `WItem_` are the world-model sprite for the same item, not the inventory icon. Filter
to `Item_` unless you specifically want the dropped-on-the-ground look.

## The icon name is not derivable from the item id

This is the part that costs time. An item's `Icon` property names its sprite, and that name follows
no rule you can reconstruct from the item id:

| Item id | Icon sprite |
|---|---|
| `Base.Axe` | `Item_Axe` |
| `Base.WaterBottleFull` | `Item_WaterBottle_Full` |
| `Base.Disinfectant` | `Item_Alcohol` |
| `Base.Saw` | `Item_Handsaw` |
| `Base.Pistol` | `Item_HandGun` |
| `Base.TinnedBeans` | `Item_Beans` |
| `Base.Log` | `Item_Logs` |
| `Base.CannedSoup` | `Item_Soup` |
| `Base.Pasta` | `Item_MacaroniRaw` |
| `Base.PillsVitamins` | `Item_Vitamins` |

Read the `Icon` key from the item's script block; do not construct it. Where an item sets no `Icon`,
the game falls back to the item name, which is exactly why some ids happen to match and mislead you
into thinking there is a rule.

`DATA-ITEM.md` lists every item with the file it is defined in — that file holds its `Icon`.

## The pack format

Undocumented, and there are two variants. Both matter: skipping PZPK loses 3,848 of 4,475 icons.

**Legacy** (`UI.pack`, `ApComUI.pack`, `RadioIcons.pack`, `IconsMoveables.pack`):

```
uint32   page count
per page:
  uint32 length of page name
  bytes  page name                    e.g. "itemThuztorFarming1"
  uint32 sprite count
  uint32 reserved, always 0
  per sprite:
    uint32 length of sprite name
    bytes  sprite name                e.g. "Item_HandShovel"
    int32  x, y, w, h, offX, offY, origW, origH    (8 values)
  bytes  a complete PNG (\x89PNG … IEND + 4 byte CRC)
  uint32 0xDEADBEEF, separating this page from the next
```

**PZPK** (`UI2.pack` and the 2x tile packs):

```
bytes  "PZPK"
uint32 version (1)
uint32 unknown (15)
then pages exactly as above — but no page count in the header and no 0xDEADBEEF
separator, so read until the buffer runs out
```

Three things bite, in the order you hit them:

1. **Everything is little-endian.** A length like `0x0000000f` reads plausibly in either direction,
   so a big-endian misread survives the first field and only shows up at the next one, as a number
   like `1543503872` — which is 92 read the other way.
2. **The reserved word after the sprite count.** Miss those four bytes and every name length after
   it is garbage.
3. **The `0xDEADBEEF` page separator.** Without skipping it you read page one and stop, getting
   about 60 sprites instead of 4,400. This is the single most likely reason a hand-written reader
   "works" and still returns almost nothing.

Sprite coordinates are pixels into that page's PNG; `w`/`h` are the crop size. `offX`/`offY` and
`origW`/`origH` describe trimmed transparent padding and are not needed to crop.

### Reading it, exactly

Every integer is `uint32`/`int32` little-endian. The cursor advances by the bytes read, and by
nothing else — there is no alignment or padding beyond the one reserved word.

```
cursor = 0

if bytes[0..4] == "PZPK":              # PZPK variant
    cursor = 4
    read uint32                        # version, is 1
    read uint32                        # unknown, is 15
    pages = until end of buffer        # NOT stored in the header
else:                                  # legacy variant
    pages = read uint32

repeat pages times:
    n     = read uint32                # length of page name
    page  = read n bytes as utf-8
    count = read uint32                # sprites on this page
    read uint32                        # reserved, is 0 (legacy) / 1 (PZPK)

    repeat count times:
        m    = read uint32             # length of sprite name
        name = read m bytes as utf-8
        x, y, w, h            = read 4 × int32
        offX, offY, origW, origH = read 4 × int32     # not needed to crop

    png_start = find "\x89PNG" from cursor
    png_end   = find "IEND" from png_start, + 8       # 4 bytes IEND + 4 bytes CRC
    atlas     = bytes[png_start .. png_end]
    cursor    = png_end

    if next uint32 == 0xDEADBEEF: cursor += 4         # legacy page separator
    if fewer than 8 bytes remain: stop                # PZPK ends without a marker
```

Cropping is then plain:

```
icon(name) = atlas.crop(left = x, top = y, right = x + w, bottom = y + h)
```

Guard the crop: a sprite whose `x + w` or `y + h` exceeds the atlas size belongs to a page whose
parse desynchronised — drop it rather than clamping, because a clamped crop is silently the wrong
picture.

### Verified byte trace

`UI.pack`, build 42.20.2, so a new reader can be checked field by field:

| Offset | Field | Value |
|---|---|---|
| 0 | page count | `8` |
| 4 | length of page name | `19` |
| 8 | page name | `"itemThuztorFarming1"`, ends at 27 |
| 27 | sprite count | `6` |
| 31 | reserved | `0` |
| 35 | length of sprite name | `15` |
| 39 | sprite name | `"Item_HandShovel"` |
| 54 | x, y, w, h | `0, 0, 32, 31` |
| 70 | offX, offY, origW, origH | `0, 0, 32, 31` |
| 362 | PNG begins | 12,272 bytes, to 12,634 |
| 12634 | separator | `0xDEADBEEF` |

If your reader produces `19` at offset 4 and `"Item_HandShovel"` at 39, the layout is right. If it
produces `1543503872` anywhere, it read big-endian.

Tile packs (`Tiles2x`, `JumboTrees*`, `DepthMaps2x`, `B42ChunkCaching2x`) hold no `Item_*` sprites
and may use yet another layout. The script skips anything it cannot parse instead of failing.

## Loose icons

`media/ui/` holds ~100 PNGs directly, and a handful of `Item_*.png` live under
`media/textures/WorldItems/`. Check there first for a single icon — no unpacking needed.
