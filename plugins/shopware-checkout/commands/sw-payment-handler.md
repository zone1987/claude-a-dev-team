---
name: sw-payment-handler
description: Scaffolds a Shopware 6.7 payment handler (AbstractPaymentHandler) including the payment_method migration and its registration.
argument-hint: <Name> [--plugin <PluginName>] [--async] [--refund]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-payment-handler

Produce a payment handler (Shopware 6.7). Skill: `sw-payment`.

## Steps
1. Name and target plugin; `--async` (redirect flow), `--refund` (refund support).
2. `src/Core/Checkout/Payment/<Name>Handler.php` extends `AbstractPaymentHandler` (`supports`, `pay`,
   `finalize`, optionally `refund`); register it in `src/Resources/config/services/payment.php` — PHP, not XML
   (`XmlFileLoader` is `@deprecated tag:v6.8.0`), explicitly and without autowiring
   (→ `shopware-core` → `sw-services` → `DEPENDENCY-INJECTION.md`).
3. Create the `payment_method` entity by migration or lifecycle and bind it to the handler
   (handlerIdentifier).
4. State transitions go through the state machine; errors through `PaymentException`. Note that activation
   is per sales channel.

For an app-based payment use `sw-payment` instead. For an external PayPal API, `sw-payment`. Never overwrite
an existing handler.

## Before it counts as done

`composer gate` green, unit tests for `supports()` and `pay()`, and a checkout completed
end-to-end with the payment method, through to the transaction state.
→ `shopware-testing` → `sw-testing-standard`
