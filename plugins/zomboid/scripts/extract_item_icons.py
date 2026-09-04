#!/usr/bin/env python3
"""Extract item icons from Project Zomboid's texture-pack atlases.

Why this exists: the game does not ship item icons as individual files. About a
hundred sit loose in `media/ui/`; the remaining ~4,400 are packed into sprite
atlases under `media/texturepacks/*.pack`. Anything that needs to show a real
item icon — a control panel, a wiki, a loot planner — has to unpack them.

The format is undocumented. Two variants exist:

  Legacy (UI.pack, ApComUI.pack, RadioIcons.pack, IconsMoveables.pack)
    uint32   page count
    per page:
      uint32 length of page name
      bytes  page name                     e.g. "itemThuztorFarming1"
      uint32 sprite count
      uint32 reserved, always 0            <- easy to miss; skipping it
                                              desynchronises everything after
      per sprite:
        uint32 length of sprite name
        bytes  sprite name                 e.g. "Item_HandShovel"
        int32  x, y, w, h, offX, offY, origW, origH   (8 values)
      bytes  a complete PNG (\\x89PNG … IEND + 4 byte CRC)
      uint32 0xDEADBEEF separator before the next page
                                           <- without this you read one page
                                              and stop, getting ~60 sprites
                                              instead of ~4,400

  PZPK (UI2.pack and the 2x tile packs)
    bytes  "PZPK"
    uint32 version (1)
    uint32 unknown (15)
    then pages exactly as above, but with no page count in the header and no
    0xDEADBEEF separator — read until the buffer runs out.

Everything is little-endian. That is the real trap: a value like 0x0000000f
reads plausibly either way, so a big-endian misread only surfaces at the next
field, as a number like 1543503872 (which is 92 little-endian).

Tile packs (Tiles2x, JumboTrees, DepthMaps, B42ChunkCaching) carry no `Item_*`
sprites and may use yet another layout; they are skipped without complaint.

Usage:
    python3 extract_item_icons.py --game <Contents/Java> --out <dir> [--webp]
    python3 extract_item_icons.py --game <Contents/Java> --list
    python3 extract_item_icons.py --game <Contents/Java> --only Item_Axe,Item_Bandage

Requires Pillow for cropping (`pip install Pillow`); `--list` needs nothing.

The extracted images are The Indie Stone's game assets. Keep them out of any
repository and out of anything you publish.
"""
import argparse, io, json, pathlib, struct, sys

DEADBEEF = 0xDEADBEEF


def parse_pack(buf: bytes):
    """Yield (page_name, sprites, png_bytes) for one .pack file.

    sprites is a list of dicts: name, x, y, w, h.
    Raises ValueError when the file does not follow either known layout.
    """
    o = 0

    def u32():
        nonlocal o
        if o + 4 > len(buf):
            raise ValueError("truncated")
        v = struct.unpack_from("<I", buf, o)[0]
        o += 4
        return v

    def i32():
        nonlocal o
        v = struct.unpack_from("<i", buf, o)[0]
        o += 4
        return v

    def name():
        nonlocal o
        n = u32()
        if not 1 <= n <= 256:
            raise ValueError(f"implausible string length {n} at {o - 4}")
        v = buf[o:o + n].decode("utf-8", "replace")
        o += n
        return v

    pzpk = buf[:4] == b"PZPK"
    if pzpk:
        o = 4
        u32()          # version
        u32()          # unknown
        page_limit = 4096
    else:
        page_limit = u32()
        if not 1 <= page_limit <= 4096:
            raise ValueError(f"implausible page count {page_limit}")

    for _ in range(page_limit):
        try:
            page = name()
        except (ValueError, struct.error):
            return
        try:
            count = u32()
        except (ValueError, struct.error):
            return
        if not 0 <= count <= 100_000:
            return
        o += 4             # reserved

        sprites, broke = [], False
        for _ in range(count):
            try:
                nm = name()
            except (ValueError, struct.error):
                broke = True
                break
            if o + 32 > len(buf):
                broke = True
                break
            x, y, w, h = i32(), i32(), i32(), i32()
            i32(); i32(); i32(); i32()      # offX, offY, origW, origH
            sprites.append({"name": nm, "x": x, "y": y, "w": w, "h": h})

        start = buf.find(b"\x89PNG", o)
        if start == -1:
            return
        iend = buf.find(b"IEND", start)
        if iend == -1:
            return
        end = iend + 8                       # IEND + CRC
        yield page, sprites, buf[start:end]
        o = end
        if broke:
            return
        if o + 4 <= len(buf) and struct.unpack_from("<I", buf, o)[0] == DEADBEEF:
            o += 4
        if o + 8 > len(buf):
            return


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--game", required=True,
                    help="path to 'Project Zomboid.app/Contents/Java' (or the Windows install root)")
    ap.add_argument("--out", default="pz-icons", help="output directory")
    ap.add_argument("--only", help="comma-separated sprite names to extract")
    ap.add_argument("--manifest", default="icons.json", help="index file name")
    ap.add_argument("--webp", action="store_true", help="write WebP instead of PNG (much smaller)")
    ap.add_argument("--list", action="store_true", help="list what is there, write nothing")
    a = ap.parse_args()

    pack_dir = pathlib.Path(a.game) / "media" / "texturepacks"
    if not pack_dir.is_dir():
        sys.exit(f"no texturepacks directory under {pack_dir}")

    wanted = {s.strip() for s in a.only.split(",")} if a.only else None

    Image = None
    if not a.list:
        try:
            from PIL import Image as _Image
            Image = _Image
        except ImportError:
            sys.exit("Pillow is required to crop icons: pip install Pillow")
        pathlib.Path(a.out).mkdir(parents=True, exist_ok=True)

    index, written, skipped, unreadable = {}, 0, 0, []

    for pack in sorted(pack_dir.glob("*.pack")):
        try:
            pages = list(parse_pack(pack.read_bytes()))
        except (ValueError, struct.error) as e:
            unreadable.append(f"{pack.name}: {e}")
            continue

        for page, sprites, png in pages:
            items = [s for s in sprites
                     if s["name"].startswith("Item_") and s["w"] > 0 and s["h"] > 0
                     and (wanted is None or s["name"] in wanted)]
            if not items:
                continue

            if a.list:
                for s in items:
                    print(f"{s['name']}\t{pack.name}\t{page}\t{s['w']}x{s['h']}")
                written += len(items)
                continue

            atlas = Image.open(io.BytesIO(png)).convert("RGBA")
            for s in items:
                if s["x"] + s["w"] > atlas.width or s["y"] + s["h"] > atlas.height:
                    skipped += 1
                    continue
                crop = atlas.crop((s["x"], s["y"], s["x"] + s["w"], s["y"] + s["h"]))
                ext = "webp" if a.webp else "png"
                target = pathlib.Path(a.out) / f"{s['name']}.{ext}"
                if a.webp:
                    crop.save(target, "WEBP", quality=92, method=4)
                else:
                    crop.save(target, "PNG", optimize=True)
                index[s["name"]] = {"file": target.name, "w": s["w"], "h": s["h"],
                                    "pack": pack.name}
                written += 1

    if a.list:
        print(f"# {written} Item_* sprites")
    else:
        (pathlib.Path(a.out) / a.manifest).write_text(json.dumps(index, indent=1))
        print(f"{written} icons -> {a.out}  ({a.manifest}: {len(index)} entries)")
        if skipped:
            print(f"{skipped} skipped (crop outside atlas)")
    if unreadable:
        print(f"\n{len(unreadable)} pack(s) not in a known layout (normal for tile packs):")
        for u in unreadable[:5]:
            print(f"  {u}")


if __name__ == "__main__":
    main()
