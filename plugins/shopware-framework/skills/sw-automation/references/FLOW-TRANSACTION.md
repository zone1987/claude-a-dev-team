# Shopware 6 — Flow transactions

Since the ADRs "transactional flow actions" / "move flow execution after business process", flow actions run **after**
the triggering business process completes, in a transaction of their own.

- A failing action rolls back **only its own** transaction, not the business process (for example the order
  survives even if the notification action fails).
- Perform DB writes inside actions through the DAL (transaction-safe); make external calls idempotent/fault-tolerant.
- Move long-running or expensive work to an asynchronous path (message queue, `sw-message-queue`).

Practical consequence: never assume an action is "atomic with the order". Action implementation: `sw-flow-action`.
