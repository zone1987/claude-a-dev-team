# Shopware 6 – product reviews: complete reference

> Source: https://docs.shopware.com/de/shopware-6-de/kataloge/bewertungen  
> Applies from: Shopware 6.0.0+

---

## Contents

- [1. Overview](#1-overview)
- [2. Review overview](#2-review-overview)
- [3. Moderating a review](#3-moderating-a-review)
- [4. Deactivating reviews (globally)](#4-deactivating-reviews-globally)
- [5. Frontend presentation for customers](#5-frontend-presentation-for-customers)
- [6. AI features](#6-ai-features)
- [7. Reviews in the product context](#7-reviews-in-the-product-context)
- [8. Tips and best practices](#8-tips-and-best-practices)
- [9. Data protection notes](#9-data-protection-notes)

## 1. Overview

Product reviews let customers leave reviews for products they have bought or viewed. In the administration, shop operators can moderate, approve and comment on reviews and have them summarised or translated with AI support.

Managed under: **Kataloge** (Catalogues) > **Bewertungen** (Reviews)

---

## 2. Review overview

### Columns of the overview

| Column | Description |
|---|---|
| Titel (Title) | Title of the review (given by the customer) |
| Sterne (Stars) | Number of stars awarded (1–5) |
| Produkt (Product) | The reviewed product |
| Kunde (Customer) | Name of the reviewing customer |
| Status / Sichtbarkeit (Visibility) | Whether the review is visible in the frontend |

### Views

- **Übersicht** (Overview): list view with the columns named above
- **Details**: full review text with all management options

---

## 3. Moderating a review

### 3.1 Approving a review (making it visible)

1. Open the review in the overview (click on the review or Bearbeiten (Edit) in the context menu)
2. Open the tab **"Eigenschaften"** (Properties)
3. Activate **"Sichtbar"** (Visible)
4. Set the **Sprache** (Language) of the review (important for language filtering in the frontend)
5. Save

> **Important**: after being submitted by the customer, reviews are **not visible** by default and have to be approved manually!

### 3.2 Commenting on a review

Shop operators can leave a reply to reviews:
1. Open the review
2. Fill in the comment field
3. Save

The comment appears **below the review** in the frontend area.

### 3.3 Rejecting a review / making it invisible

- Deactivate "Sichtbar" → the review disappears from the frontend
- The review is kept in the system (not deleted)

---

## 4. Deactivating reviews (globally)

To deactivate the review system completely for a Verkaufskanal (Sales channel):

1. Einstellungen (Settings) > Handel (Commerce) > **Produkte** (Products)
2. Area **"Bewertungen"**
3. Set the toggle **"Bewertungen anzeigen"** (Show reviews) to **off**
4. Select the Verkaufskanal (channel-specific setting)
5. Save

---

## 5. Frontend presentation for customers

On the product detail page, customers see:

| Element | Description |
|---|---|
| Gesamtbewertung (Overall rating) | Average star rating shown in large form |
| Bewertungsverteilung (Rating distribution) | Percentage and absolute count per number of stars |
| Filterung (Filtering) | Customers can filter by number of stars (e.g. only 5 stars) |
| "Bewertung schreiben" (Write review) button | Opens the review form |
| Reviews in other languages | Option to display reviews in other languages |

### Review form (customer view)

- Title field
- Star rating (1–5)
- Review text: **minimum length 40 characters**
- Submit button → the review waits for approval by the shop operator

---

## 6. AI features

### 6.1 KI-Übersetzung (AI translation) (from Shopware Rise)

- Activation: Einstellungen > [shop name] > selection of the Verkaufskanal
- Translates reviews automatically into the language of the shop/channel
- Customers see reviews in their own language

### 6.2 AI summary (from Shopware Rise)

The **AI Copilot** automatically generates a short summary from all reviews of a product:

- **Wording style selectable**: neutral or positive
- **Editable**: the generated summary can be adjusted manually
- **Show in the frontend**: the summary appears prominently on the product detail page

Activated in the review management of the respective product.

---

## 7. Reviews in the product context

Reviews can also be opened directly from the product screen:

1. Kataloge > Produkte > open the product
2. Tab **"Bewertungen"**
3. Overview of all reviews for this product
4. Direct approval or link to the review detail page

---

## 8. Tips and best practices

- Set up review notifications: send new reviews by e-mail to the shop operator (configurable via triggers/flows)
- **Replies to negative reviews** are publicly visible and show customers that the operator is active
- **Set the language correctly** when approving – a wrong language assignment can cause reviews to appear in the wrong language context
- Regular moderation is recommended (daily or weekly review of the new reviews)
- For a **Trustpilot integration** or external review tools: Shopware offers plugins for all common platforms

---

## 9. Data protection notes

- Customer data in reviews is subject to the GDPR
- On customer request, it must be possible to delete reviews
- Deletion happens directly in the review management via the context menu

---

*Source: https://docs.shopware.com/de/shopware-6-de/kataloge/bewertungen*
