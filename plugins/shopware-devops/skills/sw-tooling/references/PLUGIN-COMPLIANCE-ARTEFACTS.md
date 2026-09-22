# Shopware 6 plugin — compliance artefacts

The three artefacts a plugin carries for legal and supply-chain reasons: `SECURITY.md`, `sbom.json` and the licence.
None of them is code, all three are checked whenever a plugin is worked on.

Placeholders follow the plugin ground rules — `<PLUGIN-NAME>`, `<VENDOR-LABEL>`, `<SECURITY-EMAIL>`, `<YEAR-FROM>` /
`<YEAR-TO>`. A file still containing them has been copied, not adopted.

## Contents

- [1. SECURITY.md](#1-securitymd)
- [2. sbom.json](#2-sbomjson)
- [3. Licence](#3-licence)

---

## 1. `SECURITY.md`

### Legal basis

**[Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj)** (Cyber Resilience Act) requires
manufacturers to have a policy on coordinated vulnerability disclosure — **Article 13(8)**.

**Format and file name are not prescribed.** `SECURITY.md` in the repository is the common convention, not a
requirement of the regulation.

### Structure

```markdown
# Sicherheitsrichtlinie

Introduction: which plugin, which regulation, what this document is.

*English: report vulnerabilities to <SECURITY-EMAIL>. Reports in English are welcome;
the response times and scope below apply equally.*

## Schwachstelle melden
## Reaktionszeiten
## Offenlegung
## Geltungsbereich
## Supported versions
```

**The English insert matters.** Security researchers are international. A policy written only in German leads to a
finding being published rather than reported.

### Response times

Binding commitments, not statements of intent:

| Step | Target |
|---|---|
| Acknowledgement of receipt | 2 working days |
| First assessment and severity rating | 5 calendar days |
| Fix or mitigation for critical findings | 21 calendar days |
| Fix or mitigation for the remaining findings | 60 calendar days |

**What makes a report useful** is listed explicitly: affected plugin and Shopware version, description and impact,
reproduction steps, the configuration required, a severity estimate as a CVSS v3.1 vector.

### Support period

**It must be named.** Which versions receive security updates, and for how long.

The CRA requires a support period matching the expected lifetime of the product — at least five years, unless the
product is used for a shorter time.

### Disclosure

A clear rule, so that both sides know where they stand:

> Findings are disclosed as soon as a fixed version is available, and at the latest 60 days after the report —
> whichever comes first.

Fixed vulnerabilities are documented in `CHANGELOG.md` under the heading `Security`, naming the affected version and
the version that fixes it.

### What is asked for explicitly

> Please do **not** open a public issue, merge request or changelog entry for a vulnerability that is not yet fixed.

Together with the offer to request an OpenPGP key for encrypted transmission.

---

## 2. `sbom.json`

### What an SBOM is

**Software Bill of Materials** — a machine-readable list of every dependency with its version and licence. It answers
the question "is library X at version Y contained here?" — the question asked after every larger security incident.

**The CRA requires it**: manufacturers must produce and keep an SBOM covering at least the top-level dependencies.

### Generating it

```bash
composer CycloneDX:make-sbom --output-file=sbom.json --output-format=JSON
```

Further options of the command:

| Option | Purpose |
|---|---|
| `--spec-version` | which CycloneDX version to emit |
| `--omit` | leave out dependency types |
| `--output-reproducible` | drop the timestamp, so two runs produce the same result |

The package sits in `require-dev` and additionally has to be allowed under `config.allow-plugins`:

```json
{
    "require-dev": {
        "cyclonedx/cyclonedx-php-composer": "^6.2"
    }
}
```

**CycloneDX** is the OWASP Foundation standard and one of the two formats the CRA accepts (the other is SPDX).

### Why it is not committed

```gitignore
/sbom.json
```

**Three reasons:**

1. **It is generated.** Everything in it is already in `composer.lock`. A generated file in the repository is a second
   truth that can diverge from the first.
2. **It goes stale immediately.** Every `composer update` makes it wrong — and a wrong SBOM is worse than none,
   because it makes a statement about security.
3. **It belongs to the release, not to the source.** It is generated when the delivery package is built, and shipped
   with it.

### When it is generated

| Occasion | Why |
|---|---|
| **On every release** | it describes exactly that version |
| **On request** | when a customer or auditor asks for it |
| **After a security report** | to answer whether the affected library is contained |

**Not** on every commit, and not in the gate.

---

## 3. Licence

### The rule

**Every plugin carries the licence `proprietary`** — in `composer.json` **and** in every `package.json`, plus the
`LICENSE` file:

```json
{
    "license": "proprietary"
}
```

**Not in the classes.** There it is forbidden by ground rule 3 (no copyright headers in classes).

### The `LICENSE` file

Where a foreign licence text stands there — MIT, for instance — the file is **rewritten completely**. Not extended,
not adjusted: the old text goes out, the new one comes in.

**Why completely:** an MIT text with a swapped heading still permits redistribution and modification — that stands in
the text, not in the title. Whoever reads it reads the permission. A half-changed licence is worse than a wrong one,
because it looks deliberate.

The structure of a proprietary licence:

```
Proprietary Software License

Copyright (c) <YEAR-FROM>–<YEAR-TO> <VENDOR-LABEL> <info@example.com>
All rights reserved.

This software and its source code are the confidential and proprietary property of
<VENDOR-LABEL>. They are licensed, not sold.

No part of this software may be used, copied, modified, merged, published, distributed,
sublicensed, sold, reverse engineered, decompiled or disassembled, in whole or in part,
by any means, without the prior written permission of <VENDOR-LABEL>.

Where <VENDOR-LABEL> grants a licence in writing, that licence governs what the licensee
may do, and this notice governs everything it does not address. A licence is granted for
the agreed installations only and may not be transferred to a third party.

Access to this source code — whether through a repository, a delivered package or any
other means — grants no licence of any kind and creates no right to use it.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, …
```

**The sentence about access matters more than it looks:** it makes clear that merely holding the source — because it
is delivered through a Composer registry, say — establishes no permission to use it.

### The year

**The end year is always the current year.** Where `2021–2026` stands and the year is 2028, it becomes `2021–2028`.
The start year stays: it says since when the work exists.

**Why it counts:** a copyright notice three years out of date reads like a work nobody has touched for three years —
and that is exactly the argument someone brings against the protection.

**The year is checked when the licence is checked:** the same handgrip, at the start of every piece of work on a
plugin.

### Where it is checked

| Place | Rule |
|---|---|
| `custom/static-plugins/<own plugin>` | **this is where it is checked and changed** |
| `custom/plugins/` | do not touch |
| `vendor/` | **never** touch |

A plugin that is not being worked on is not touched — not even when its licence is wrong. The rule is a duty while
working, not an order to search foreign directories.
