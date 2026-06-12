# OCTO — Questions Capability (`octo/questions`)

## Capability-Identifier

```
octo/questions
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/questions
Content-Type: application/json
```

---

## Überblick

Ermöglicht die Sammlung zusätzlicher Gäste-Informationen während des Buchungs- und
Bestellflusses. Fragen sind rein informativ — sie beeinflussen weder Verfügbarkeit
noch Preise.

---

## Question-Objekt (Produktschema)

```typescript
interface Question {
  id: string;
  title: string;
  required: boolean;
  inputType: QuestionInputType;
  options?: QuestionOption[];  // Optionen für radio/select
}

type QuestionInputType =
  | "textarea"  // Keine Optionen → Freitextfeld
  | "radio"     // 1–5 Optionen → Radiobuttons
  | "select";   // Mehr als 5 Optionen → Dropdown

interface QuestionOption {
  id: string;
  label: string;
}
```

---

## Answer-Objekt (Buchungs-/Order-Schema)

```typescript
interface QuestionAnswer {
  questionId: string;   // Referenz zur Question-Definition
  value: string | null; // Antwortinhalt; null = unbantwortet
}
```

---

## API-Erweiterungen

### Product-Routen (Read)

Endpunkte: `GET /products`, `GET /products/{productId}`

- Fragen erscheinen in `option.questions[]` (Booking-Ebene)
- Fragen erscheinen in `option.units[].questions[]` (Ticket-Ebene)

**Darstellungsregel:**
- Booking-Level-Fragen: einmal pro Buchung anzeigen
- Ticket-Level-Fragen: einmal pro Unit-Item anzeigen

### Booking-Routen (Write)

| Endpunkt | Methode | Zusatzfelder |
|----------|---------|--------------|
| `/bookings` | POST | `questionAnswers[]`, `unitItems[].questionAnswers[]` |
| `/bookings/{uuid}` | PATCH | `questionAnswers[]`, `unitItems[].questionAnswers[]` |
| `/bookings/{uuid}/confirm` | POST | `questionAnswers[]`, `unitItems[].questionAnswers[]` |

### Booking-Routen (Read)

| Endpunkt | Methode |
|----------|---------|
| `/bookings` | GET |
| `/bookings/{uuid}` | GET |
| `/bookings/{uuid}/extend` | POST |
| `/bookings/{uuid}/cancel` | POST |

### Order-Routen (benötigt `octo/questions` + `octo/cart`)

| Endpunkt | Methode |
|----------|---------|
| `/orders` | POST |
| `/orders/{orderId}` | PATCH |
| `/orders/{orderId}/preview` | PATCH |
| `/orders/{orderId}/confirm` | POST |
| `/orders/{orderId}/extend` | POST |
| `/orders/{orderId}/cancel` | POST |
| `/orders/{orderId}` | DELETE |
| `/orders` | GET |
| `/orders/{orderId}` | GET |

---

## Request/Response-Schema

### Booking/Order Write Request

```typescript
interface BookingWithQuestionsRequest {
  // ... Standard Buchungsfelder
  questionAnswers: QuestionAnswer[];        // Booking-Ebene
  unitItems: Array<{
    unitId: string;
    quantity: number;
    questionAnswers: QuestionAnswer[];      // Ticket-Ebene
  }>;
}
```

### Booking/Order Response

```typescript
interface BookingWithQuestionsResponse {
  // ... Standard Buchungsfelder
  questionAnswers: QuestionAnswer[];
  unitItems: Array<{
    // ... Standard UnitItem-Felder
    questionAnswers: QuestionAnswer[];
  }>;
}
```

---

## Verhaltensregeln

1. **Bestehende Antworten**: Werden `questionAnswers` bei PATCH-Anfragen weggelassen →
   bestehende Antworten bleiben erhalten
2. **Löschen**: `value: null` oder leerer String leert eine Antwort
3. **Ungültige ID**: `INVALID_QUESTION_ID`-Fehler bei unbekannter `questionId`
4. **inputType-Logik**:
   - `textarea`: keine `options` vorhanden
   - `radio`: 1–5 `options` vorhanden
   - `select`: mehr als 5 `options` vorhanden

---

## Fehler-Codes

| Code | HTTP | Beschreibung |
|------|------|--------------|
| `INVALID_QUESTION_ID` | 400 | `questionId` existiert nicht auf dem Produkt |

---

## Vollständiges Beispiel

### Response: Product mit Fragen

```bash
curl -X GET "https://api.ventrata.com/octo/products/product_abc123" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/questions"
```

```json
{
  "id": "product_abc123",
  "options": [
    {
      "id": "option_def456",
      "questions": [
        {
          "id": "question_001",
          "title": "Haben Sie spezielle Ernährungsanforderungen?",
          "required": false,
          "inputType": "radio",
          "options": [
            { "id": "opt_vegetarian", "label": "Vegetarisch" },
            { "id": "opt_vegan", "label": "Vegan" },
            { "id": "opt_glutenfree", "label": "Glutenfrei" }
          ]
        },
        {
          "id": "question_002",
          "title": "Notfallkontakt (Name und Telefonnummer)",
          "required": true,
          "inputType": "textarea"
        }
      ],
      "units": [
        {
          "id": "unit_adult",
          "questions": [
            {
              "id": "question_003",
              "title": "Vollständiger Name des Teilnehmers",
              "required": true,
              "inputType": "textarea"
            },
            {
              "id": "question_004",
              "title": "Nationalität",
              "required": false,
              "inputType": "select",
              "options": [
                { "id": "opt_de", "label": "Deutschland" },
                { "id": "opt_at", "label": "Österreich" },
                { "id": "opt_ch", "label": "Schweiz" },
                { "id": "opt_us", "label": "USA" },
                { "id": "opt_gb", "label": "Großbritannien" },
                { "id": "opt_fr", "label": "Frankreich" }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### Request: Buchung mit Fragen-Antworten

```bash
curl -X POST https://api.ventrata.com/octo/bookings \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/questions" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_abc123",
    "optionId": "option_def456",
    "availabilityId": "availability_xyz789",
    "questionAnswers": [
      { "questionId": "question_001", "value": "opt_vegetarian" },
      { "questionId": "question_002", "value": "Maria Müller, +49 170 1234567" }
    ],
    "unitItems": [
      {
        "unitId": "unit_adult",
        "questionAnswers": [
          { "questionId": "question_003", "value": "Max Mustermann" },
          { "questionId": "question_004", "value": "opt_de" }
        ]
      },
      {
        "unitId": "unit_adult",
        "questionAnswers": [
          { "questionId": "question_003", "value": "Erika Mustermann" },
          { "questionId": "question_004", "value": "opt_at" }
        ]
      }
    ]
  }'
```

### Response

```json
{
  "uuid": "booking_111222",
  "status": "ON_HOLD",
  "questionAnswers": [
    { "questionId": "question_001", "value": "opt_vegetarian" },
    { "questionId": "question_002", "value": "Maria Müller, +49 170 1234567" }
  ],
  "unitItems": [
    {
      "uuid": "unit_item_001",
      "unitId": "unit_adult",
      "questionAnswers": [
        { "questionId": "question_003", "value": "Max Mustermann" },
        { "questionId": "question_004", "value": "opt_de" }
      ]
    },
    {
      "uuid": "unit_item_002",
      "unitId": "unit_adult",
      "questionAnswers": [
        { "questionId": "question_003", "value": "Erika Mustermann" },
        { "questionId": "question_004", "value": "opt_at" }
      ]
    }
  ]
}
```

### Request: Antwort löschen (PATCH)

```bash
curl -X PATCH "https://api.ventrata.com/octo/bookings/booking_111222" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/questions" \
  -H "Content-Type: application/json" \
  -d '{
    "questionAnswers": [
      { "questionId": "question_001", "value": null }
    ]
  }'
```

---

*Quelle: https://docs.ventrata.com/capabilities/questions*
*Typen: https://github.com/octotravel/octo-types (MIT-Lizenz)*
