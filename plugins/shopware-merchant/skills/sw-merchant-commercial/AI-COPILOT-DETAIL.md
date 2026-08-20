# Shopware AI Copilot – Complete documentation

## Contents

- [Overview](#overview)
- [Functions in detail](#functions-in-detail)
- [Translation functions](#translation-functions)
- [Technical prerequisites](#technical-prerequisites)
- [Integration with other features](#integration-with-other-features)

## Overview

The **Shopware AI Copilot** is an AI assistant natively integrated into Shopware 6. It uses artificial intelligence to simplify e-commerce workflows.

**Availability:** Rise plan and higher (Commercial extension required)

---

## Functions in detail

### 1. Content for Erlebniswelten (Shopping Experiences)

The AI Copilot helps to create various kinds of text content for Shopping Experiences. Texts can be generated directly and translated into several languages.

**Usage:** In the Erlebniswelten editor → activate the AI Copilot function → enter a description → generate/translate text

### 2. Image keywords

The system analyses uploaded product images and automatically assigns relevant keywords. These are used for search and classification.

**Path:** Edit a product → Medien (Media) area → AI keyword suggestion

### 3. Produkteigenschaften (Product properties)

Based on existing product descriptions, the AI suggests matching product attributes and properties. The merchant accepts or adjusts them.

### 4. Personalised checkout message (post-purchase messaging)

After checkout, customers receive a personalised, AI-generated message. The AI uses the cart contents to phrase relevant, loyalty-building messages.

**Configuration:** Flow Builder → trigger: Bestellung abgeschlossen (Order completed) → action: AI checkout message

### 5. Review summaries (Bewertungszusammenfassung)

Instead of reading individual reviews, customers get a concise AI summary of all product reviews on the product detail page.

**Display:** Shown automatically on product detail pages (from the configured minimum number of reviews)

### 6. Customer classification

The system automatically creates customer labels based on purchase history. These labels enable targeted marketing and segmentation.

**Path:** Kunden (Customers) > Kunden-Übersicht (Customer overview) → AI labels are assigned automatically

### 7. Export assistant

Merchants can export shop data in CSV format by entering natural language commands. No manual configuration of the export parameters is needed.

**Example:** "Export all products from the category Schuhe with a price below 100 euro"

### 8. Product descriptions

Merchants enter core information about a product and the AI generates complete, sales-optimised product descriptions from it. These can be used directly or adjusted further.

**Path:** Edit a product → description field → open the AI assistant → enter keywords → generate

### 9. Intelligent search (Advanced Search integration)

Two search modes that are combined with Advanced Search 2.0:

**Context-based search:**
- Customers describe their product need in natural language
- The system interprets the intent taking the shop context into account
- Maximum keyword length: 100 characters
- In the storefront: icon next to the search field with example suggestions

**Image-based search:**
- Customers upload a photo
- The system finds visually similar products

**Prerequisite:** Advanced Search 2.0 (Evolve+) for full functionality; basic AI search is already in Rise

### 10. Image generation

Merchants create product images through natural-language descriptions. No image editing program is required.

**Path:** Medien area → AI Bild generieren (Generate AI image) → enter a description → create the image

---

## Translation functions

The AI Copilot can translate generated content automatically into all configured shop languages:
- Review translations for international customers
- Product descriptions in several languages
- Translating Erlebniswelten texts

---

## Technical prerequisites

- Shopware Commercial extension active
- Rise plan or higher booked
- For image-based search: Advanced Search 2.0 (Evolve+)
- Internet connection for AI API calls

---

## Integration with other features

| Feature | AI Copilot function |
|---|---|
| Erlebniswelten | Content creation and translation |
| Flow Builder | Personalised checkout messages |
| Advanced Search | Context-based and image-based search |
| Product management | Descriptions and properties |
| Medien area | Image keywords and image generation |
| Customer management | Customer classification and labels |

---

*Source: https://docs.shopware.com/de/shopware-6-de/features/shopware-rise/ai-copilot (as of: 2026-06)*
