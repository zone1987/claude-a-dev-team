# order-table.vue (`ResubmissionAppServer/assets/vue/controllers/order-table.vue`)

## Zweck
Wiedervorlagen-Übersichtstabelle (Meteor `mt-data-table`): listet Bestellungen mit Status-Spalten, Paginierung, Sortierung, Filter (Status/User) und Toggle-Aktion. ~361 Zeilen.

## Typ
- Vue 3 SFC (Composition API).

## Struktur/Verhalten (Auswahl)
- Spalten inkl. Bestell-/Zahlungs-/Lieferstatus-Icons, Wiedervorlage-Status.
- Holt Daten via `/resubmission/orders` (POST), Benutzer via `/resubmission/users`.
- `state`-Prop (aktive vs. inaktive Wiedervorlagen), `urlParams` für Links.
- Toggle/Edit-Links auf `/resubmission/...`.

## Bezüge
`link-button.vue`, `Controller/ResubmissionController.php`, `templates/resubmission/index.html.twig`.
