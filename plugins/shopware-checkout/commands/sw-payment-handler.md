---
name: sw-payment-handler
description: Scaffold eines Shopware-6.7 Payment-Handlers (AbstractPaymentHandler) inkl. payment_method-Migration und Registrierung.
argument-hint: <Name> [--plugin <PluginName>] [--async] [--refund]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-payment-handler

Erzeuge einen Payment-Handler (Shopware 6.7). Skill: `sw-payment-handler`.

## Ablauf
1. Name + Ziel-Plugin; `--async` (Redirect-Flow), `--refund` (Refund-Support).
2. `src/Core/Checkout/Payment/<Name>Handler.php` extends `AbstractPaymentHandler` (`supports`, `pay`, `finalize`,
   optional `refund`); Registrierung in services.xml.
3. `payment_method`-Entity per Migration/Lifecycle anlegen und dem Handler zuordnen (handlerIdentifier).
4. Status-Übergänge über die StateMachine; Fehler via `PaymentException`. Hinweis: Aktivierung je SalesChannel.

App-basierte Zahlung stattdessen → `sw-payment-app`. Externe PayPal-API → `sw-paypal-sdk`. Bestehende nicht überschreiben.
