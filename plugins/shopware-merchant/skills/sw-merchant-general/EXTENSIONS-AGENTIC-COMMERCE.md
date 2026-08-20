# Agentic Commerce – AI commerce agents & product feeds

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/agentic-commerce  
**Status**: Beta (limited functionality, extension to follow)

## Contents

- [Overview](#overview)
- [Universal Commerce Protocol (UCP)](#universal-commerce-protocol-ucp)
- [Product Feed Sales Channel](#product-feed-sales-channel)
- [Tracking & analytics](#tracking--analytics)
- [ChatGPT marketplace: availability](#chatgpt-marketplace-availability)
- [Beta note](#beta-note)
- [Vision for the future](#vision-for-the-future)

## Overview

**Agentic Commerce** integrates Shopware 6 with AI commerce agents and enables
automated trading via AI platforms such as ChatGPT.

### Two main components:

1. **Universal Commerce Protocol (UCP)** – standardised interface for AI agents
2. **Product Feed Sales Channel** – product data export for external systems and AI agents

---

## Universal Commerce Protocol (UCP)

### What it is
A standardised protocol that allows AI commerce agents to:
- **Detect your shop automatically**
- Interact through a **standardised interface**
- **Fully automate** purchasing processes

### Configuration
**Einstellungen** (Settings) **> Commerce > UCP**

There you control which sales channels are accessible to AI agents and
which capabilities are enabled:

| Capability | Description |
|---|---|
| **Catalogue access** | The AI agent can browse products |
| **Cart management** | The AI agent can fill the cart |
| **Discount application** | The AI agent can use vouchers |
| **Checkout process** | The AI agent can complete an order |
| **Order creation** | The AI agent creates orders |
| **Payment tokenisation** | Secure payment handling by the AI agent |
| **Customer identity linking** | The AI agent can map customer data |

---

## Product Feed Sales Channel

### Supported platforms

| Platform | Feed format | Status |
|---|---|---|
| OpenAI / ChatGPT | JSONL | Available (US-only for the ChatGPT marketplace) |
| Google Shopping | XML | Available |
| Others | Planned | Beta |

### Setup

1. **Verkaufskanäle** (Sales channels) → add a new channel → choose "Agentic Commerce"
2. Select the feed type (JSONL for OpenAI / XML for Google)
3. Configure product variants:

### Variant mapping
Map product attributes to the AI platform's requirements:

| Shopware attribute | AI platform attribute |
|---|---|
| Property "Farbe" (Colour) | color |
| Property "Größe" (Size) | size |
| Property "Material" | material |
| Product number | sku |

---

## Tracking & analytics

The Agentic Commerce channel tracks:
- Orders from AI agent traffic
- Customer acquisition via AI channels
- Revenue from AI commerce

---

## ChatGPT marketplace: availability

> **Currently**: ChatGPT marketplace registration is available only to **US merchants**.
> European availability is planned but not yet announced (as of 2024).

---

## Beta note

- The feature is under **active development**
- Its scope of functionality will be extended
- Before productive use: use a test environment
- Changes to the API and the protocol are possible

---

## Vision for the future

Shopware positions Agentic Commerce as a strategic investment in the future:
- Shopping without manual intervention by the customer
- AI agents as new "customer touchpoints"
- Fully automated B2B purchasing via AI
