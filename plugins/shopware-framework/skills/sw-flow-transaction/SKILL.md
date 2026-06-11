---
name: sw-flow-transaction
description: >
  Transaktionsverhalten von Flow-Builder-Actions in Shopware 6: transactional flow actions (Ausführung nach dem
  Business-Prozess), Fehler/Rollback, TransactionFailedException. Trigger: "transactional flow action", "flow transaction",
  "flow nach business process", "TransactionFailedException", "flow rollback". Shopware 6.7.
---

# Shopware 6 — Flow-Transaktionen

Seit ADR „transactional flow actions" / „move flow execution after business process" laufen Flow-Actions **nach**
Abschluss des auslösenden Geschäftsprozesses, in einer eigenen Transaktion.

- Eine fehlschlagende Action rollt **nur ihre eigene** Transaktion zurück, nicht den Geschäftsprozess (z.B. die Bestellung
  bleibt bestehen, auch wenn die Benachrichtigungs-Action scheitert).
- In Actions DB-Writes über DAL ausführen (transaktionssicher); externe Calls idempotent/fehlertolerant gestalten.
- Dauerhafte/teure Aktionen ggf. asynchron (MessageQueue, `sw-message-queue`) anstoßen.

Praktische Folge: keine Annahme, dass eine Action „atomar mit der Bestellung" ist. Action-Implementierung: `sw-flow-action`.
