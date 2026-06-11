# templates/resubmission/index.html.twig (`ResubmissionAppServer/templates/resubmission/index.html.twig`)

## Zweck
Iframe-Seite „Wiedervorlagen" (aktive). Mountet die Vue-Komponente `order-table` mit `state: true`.

## Inhalt
- `extends base.html.twig`; `vue_component('order-table', {urlParams, state: true})`.

## Bezüge
`assets/vue/controllers/order-table.vue`, `Controller/ResubmissionController.php::index`.
