# Digital Sales Rooms – live shopping events

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/digital-sales-rooms  
**Plan**: Shopware Beyond (exclusive)  
**Technology**: Separate frontend application + daily.co API + Mercure service

## Overview

**Digital Sales Rooms** enables interactive live shopping events with selected customers:
- Video-based product presentations
- Guided or self-directed navigation
- Direct purchase during the event

---

## Technical prerequisites

| Component | Description |
|---|---|
| **daily.co API account** | Video conferencing service (mandatory) |
| **Mercure service** | Real-time communication between the guide and the participants |
| Separate frontend app | Standalone application (not an admin plugin) |

> **Note**: The setup requires developer/administrator support.
> daily.co and Mercure are configured by the team.

---

## Operating modes

### 1. Unguided mode
- Customers navigate the presentation **on their own**
- No live interaction with a guide
- Asynchronous presentation (customers open the link whenever they like)

### 2. Guided mode
- A **guide** leads participants through the presentation in real time
- Guide view: special tools for live control
- Video connection between the guide and the participants is active

---

## Main components

### Presentations
- CMS-like layouts (similar to Erlebniswelten (Shopping Experiences))
- Individually designable shopping experiences
- Products, texts, images and videos can be embedded

### Appointments
- Scheduled events with specific customers
- Invitation emails with access links
- Date, time and participants configurable

### Guide view
The following are available during live events:
| Tool | Function |
|---|---|
| Product quick list | Show specific products immediately |
| Participant management | Mute or remove participants |
| Real-time discounts | Grant spontaneous discounts during the event |
| Chat | Written communication |

---

## Participant features (customers)

| Feature | Description |
|---|---|
| Browse products | View the presented products |
| Recently viewed products | Quick access list |
| Wishlists | Add products to the wishlist |
| Manage the cart | Buy directly within the event |
| Request quotes | (Enabled with B2B Components) |
| Shared Shopping Lists | Shared shopping lists with other participants |
| Book a follow-up appointment | Book a new appointment directly |

---

## Setup workflow (simplified)

```
1. daily.co API-Account erstellen
2. Mercure-Service konfigurieren (Entwickler)
3. Frontend-App deployen (Entwickler)
4. Im Admin: Digital Sales Rooms konfigurieren
5. Erste Präsentation erstellen
6. Create the first appointment
7. Invite customers (automatic email with link)
```

---

## Use cases

- **Fashion**: Virtual collection presentation for B2B buyers
- **Luxury goods**: Exclusive product presentations for VIP customers
- **B2B sales**: Product demonstrations for business customers
- **Beauty/cosmetics**: Live consultation with product recommendations
