# templates/base.html.twig (`ResubmissionAppServer/templates/base.html.twig`)

## Zweck
Basis-Layout aller Iframe-Seiten. Bindet die Webpack-Encore-Assets (`app`) ein und stellt den `body`-Block bereit.

## Inhalt
- Encore `encore_entry_link_tags('app')` / `encore_entry_script_tags('app')`.
- Blöcke `title`, `stylesheets`, `javascripts`, `body`.

## Bezüge
`assets/app.js`, alle `templates/*` (extends), `webpack_encore.yaml`.
