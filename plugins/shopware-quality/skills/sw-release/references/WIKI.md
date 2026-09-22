# Shopware 6 plugin — wiki

The documentation that ships beside the plugin but not inside it. Image rules are in [IMAGES.md](IMAGES.md); the
README itself is in [SHOPWARE-README.md](SHOPWARE-README.md).

## Contents

- [It is split in two](#it-is-split-in-two)
- [Language](#language)
- [Screenshots](#screenshots)
- [What the text has to achieve](#what-the-text-has-to-achieve)
- [Cross-references](#cross-references)

---

## It is split in two

| Part | For whom | Content |
|---|---|---|
| **User wiki** | the shop operator | what the plugin does, how it is operated, what the settings do |
| **Developer wiki** | developers | structure, extension points, tests, building, contributing |

**Why separated:** the two groups are looking for different things. An operator wanting to know how to create a record
should not have to read past an explanation of the offset arithmetic. A developer looking for the decorator should not
have to scroll through screenshots.

---

## Language

**German**, like `README.md` — both address the operator and German-speaking developers.

**The code in the plugin stays entirely English.** The wiki describes it; it is not part of it.

---

## Screenshots

**From one's own shop**, under the image rules in [IMAGES.md](IMAGES.md).

**What to watch for:**

| Point | Why |
|---|---|
| No notice bars of foreign plugins | a sandbox or demo banner in the image dates the screenshot and confuses |
| No credentials, no customer names | not in an address bar or a tab title either |
| No foreign product images | the licence travels with the pixels |
| Current state | a screenshot of an old interface is a wrong instruction |

**A foreign plugin whose notice gets in the way of the image is temporarily *deactivated* — never uninstalled.**
Uninstalling removes data.

**Highlights** (frames, arrows) are used where an image would otherwise be ambiguous — and then on **all** images of
that kind, not on individual ones.

---

## What the text has to achieve

**The labels must match the interface** — word for word.

> **A real lesson:** one version of the wiki had three statements wrong: the order of the cards in the form, which
> card a particular setting sits in, and from which value a position counts. They were found only when the form was
> **photographed** and put beside the text.
>
> Descriptions of an interface are checked against the interface, not written from memory.

---

## Cross-references

**`README.md` points to the wiki**, visibly and early — not in a footer.

**The wiki points back** to `README.md`, `CHANGELOG.md` and `SECURITY.md` instead of repeating their content. Two
versions of the same text drift apart.
