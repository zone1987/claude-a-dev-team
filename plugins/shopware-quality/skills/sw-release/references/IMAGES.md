# Shopware 6 plugin — images

Applies to **`README.md` and the wiki**. Recorded as an ADR:
`adr/YYYY-MM-DD-every-image-is-licence-free-and-documented.md`.

## Contents

- [The three conditions](#the-three-conditions)
- [An image is never bought](#an-image-is-never-bought)
- [The trap: Shopware's demo data](#the-trap-shopwares-demo-data)
- [AI images](#ai-images)
- [Labelling under the AI Act](#labelling-under-the-ai-act)
- [The source overview](#the-source-overview)
- [Choice of subject](#choice-of-subject)

---

## The three conditions

**Every image is licence-free or explicitly cleared for commercial use, neutral in subject, and fully documented. An
image failing any one of the three is not used.**

---

## An image is never bought

**No stock licence, no subscription, no single-image payment, no trial access that turns into one.** Where the only
route to an image leads through money, the image is not used and a free one is found.

**Why this is a rule and not a budget question:** a bought licence is a contract with terms, a renewal date and a
scope. A manual that outlives it makes a statement nobody maintains any more. A free licence with written evidence
does not expire.

**Permitted sources:** Unsplash, Pexels, Pixabay under their respective current licences; Wikimedia Commons with the
individual licence checked; screenshots taken of one's own shop; AI images from a model with a commercially usable
licence.

---

## The trap: Shopware's demo data

**This is the reason the rule is written down.**

The tea and product photographs of a demo shop look like free material that is already sitting in the media library.
They are **licensed to Shopware**, for running a Shopware demo. They are not ours and must not go into a manual.

**A screenshot is a reproduction, not a transformation.** Where a storefront screenshot shows a product image, the
screenshot is subject to that image's licence. **The licence travels with the pixels.**

---

## AI images

**Two things are to be checked, not one:**

1. **The model licence.** Not every image model permits commercial use. Example: FLUX.1 [schnell] is under Apache 2.0
   — commercially usable. FLUX.1 [dev] is under a non-commercial licence — **not usable**, although it is the same
   model family and often the same tool.
2. **The labelling obligation.**

---

## Labelling under the AI Act

**[Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj), Article 50** requires AI-generated
content to be recognisable as such.

**Every AI-generated image is labelled visibly:**

- a watermark in the image itself, at a position that stays visible even when the image is cropped
- a note in the caption
- an entry in the source overview

The EU icons are suitable as a label, see
[it-recht-kanzlei.de](https://www.it-recht-kanzlei.de/ki-inhalte-kennzeichnen-eu-icon.html).

> **A practical lesson:** a watermark in a corner can be cut off by `object-fit: cover` when the image lands in a tile
> with a different aspect ratio than it was generated at. The label therefore belongs in the middle of the image or
> centred at its lower edge — and **is checked in the browser**, not assumed.

---

## The source overview

**A page of its own in the wiki**, for example "Quellen". Per image:

| Entry | Example |
|---|---|
| File name | `listing-with-badge.png` |
| Place in the plugin | `docs/images/listing-with-badge.png` |
| What is shown | "product listing with a badge at position 5" |
| Source | Unsplash / own screenshot / AI-generated |
| Licence | Unsplash License / — / Apache 2.0 (FLUX.1 [schnell]) |
| AI label | yes / no |

**The same overview applies to `README.md`.**

---

## Choice of subject

**Neutral.** No foreign products, no recognisable people, no brands, no third-party logos.

**Why no foreign products:** a screenshot showing a foreign product advertises it unasked — and raises the same
licence question as the product photograph itself.
