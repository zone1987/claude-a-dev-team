# templates/resubmission/add.html.twig (`ResubmissionAppServer/templates/resubmission/add.html.twig`)

## Zweck
Iframe-Seite „Wiedervorlagen hinzufügen". Mountet `order-table` mit `state: false` (inaktive/zur Auswahl).

## Inhalt
- `vue_component('order-table', {urlParams, state: false})`.

## Bezüge
`assets/vue/controllers/order-table.vue`, `Controller/ResubmissionController.php::add`.
