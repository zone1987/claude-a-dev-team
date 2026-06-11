---
name: sw-cart-processor
description: Scaffold eines Shopware-6 Cart-Collectors + Cart-Processors (Warenkorb-Berechnung) inkl. services.xml-Registrierung.
argument-hint: <Name> [--plugin <PluginName>] [--with-collector]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /sw-cart-processor

Erzeuge einen Cart-Processor (optional + Collector). Skills: `sw-cart-processor`, `sw-cart-collector`, `sw-cart-price`.

## Ablauf
1. Name + Ziel-Plugin; bei `--with-collector` zusätzlich einen Collector.
2. `src/Core/Checkout/Cart/<Name>Processor.php` (`CartProcessorInterface::process`), ggf. `<Name>Collector.php`
   (`CartDataCollectorInterface::collect`).
3. Registrierung via `shopware.cart.processor` / `shopware.cart.collector`-Tag (Priorität bedenken).
4. Hinweis: auf `$toCalculate` arbeiten, Preise über Calculator-Services; Collector lädt Daten gebündelt.

Validierung/Blocker stattdessen über einen Validator (`sw-cart-validator`). Rabatte: `sw-cart-discount`.
