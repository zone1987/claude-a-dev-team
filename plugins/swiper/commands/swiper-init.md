---
name: swiper-init
description: Scaffold einer Swiper-Einbindung — Variante (Core/Element/React/Vue), HTML-Struktur, CSS-Imports, Modul-Registrierung (Navigation/Pagination/Autoplay/Effekte/…) und Init-Code mit den gewünschten Parametern.
argument-hint: <selector> [--variant core|element|react|vue] [--modules navigation,pagination,autoplay] [--effect slide|fade|coverflow|cards]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /swiper-init

Erzeuge eine einsatzfertige Swiper-Einbindung. Skills: `swiper-getting-started`, `swiper-parameters`, gewünschte Modul-Skills, `swiper-element`/`swiper-react`/`swiper-vue`.

## Ablauf
1. Variante + Selector + Module + Effekt aus `$ARGUMENTS`.
2. **HTML** erzeugen (`.swiper > .swiper-wrapper > .swiper-slide`; beim Element `<swiper-container>/<swiper-slide>`).
3. **CSS-Imports**: `swiper/css` + je Modul (`swiper/css/navigation`, `/pagination`, `/effect-fade` …).
4. **JS**: Module importieren + registrieren (`modules: [...]`), Init mit Parametern (slidesPerView, spaceBetween,
   loop, breakpoints, autoplay, pagination/navigation, effect-Optionen …) + ggf. Events (`on: { slideChange }`).
5. Variante-spezifisch: Core-Klasse, Swiper Element (`register()` + Attribute), React/Vue-Komponente.

Nur dokumentierte Parameter/Module (Quelle: `swiper-parameters` + Modul-Skills). CSS-Imports nie vergessen; Module ab v9 explizit registrieren.
