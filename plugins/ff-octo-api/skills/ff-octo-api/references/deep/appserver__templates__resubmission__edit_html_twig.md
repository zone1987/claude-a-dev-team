# templates/resubmission/edit.html.twig (`ResubmissionAppServer/templates/resubmission/edit.html.twig`)

## Zweck
Iframe-Seite „Wiedervorlage bearbeiten". Mountet `edit-form` mit `orderId` + `order` (Custom-Fields).

## Inhalt
- `vue_component('edit-form', {urlParams, orderId, order})`.

## Bezüge
`assets/vue/controllers/edit-form.vue`, `Controller/ResubmissionController.php::edit`.
