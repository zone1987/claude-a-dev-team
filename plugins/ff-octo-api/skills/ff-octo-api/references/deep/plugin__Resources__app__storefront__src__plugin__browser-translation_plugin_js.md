# FfBrowserTranslationPlugin (`src/Resources/app/storefront/src/plugin/browser-translation.plugin.js`)

## Zweck
Übersetzt ausgewählte Label-Texte clientseitig mit der experimentellen Browser-**Translation-/LanguageDetector-API** (z.B. englische OCTO-Optionsnamen → Deutsch), sofern der Browser sie unterstützt.

## Typ & Vererbung
- `export default class FfBrowserTranslationPlugin extends Plugin` (Shopware-Basis, NICHT OctoBasePlugin)
- Registriert (als Child) auf `[data-ff-browser-translation]`.

## Optionen (`static options`)
`sourceLanguage` (`en`), `targetLanguage` (`de`), `selector` (`.translatable`), `confidenceThreshold` (0.5).

## Methoden
- `async init()` — wenn `_isSupported()`, `_translateLabels()`.
- `_isSupported()` — prüft `Translator`/`LanguageDetector` in `self`; sonst warn + false.
- `async _translateLabels()` — erzeugt Detector + Translator; übersetzt alle `selector`-Elemente + deren Kinder; `destroy()` im finally.
- `async _translateElement(element, detector, translator)` — erkennt Sprache; übersetzt nur, wenn Quellsprache + Confidence > Threshold.

## Besonderheiten / Fallstricke
- **Experimentelle API** — nur in unterstützenden Browsern aktiv; sonst No-Op.
- Verändert `textContent` direkt.

## Bezüge
`buy-box.plugin.js` (registriert es), Twig-Labels mit `.translatable`.
