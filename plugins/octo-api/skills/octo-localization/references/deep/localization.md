# OCTO API — Lokalisierung

## Überblick

Ventrata ermöglicht Suppliern, Inhalte in mehreren Sprachen zu speichern. Das System nutzt den `Accept-Language` HTTP-Header, um zu bestimmen, welche Sprachversion an Clients zurückgegeben wird.

---

## Accept-Language Request-Header

```http
Accept-Language: de
Accept-Language: en-US
Accept-Language: en-US,fr-CA;q=0.8,fr;q=0.7
```

- **Standard:** HTTP BCP 47 Language Tags (RFC 5646 / RFC 4647)
- **Pflicht:** Nein (optional)
- **Format:** Einzel-Sprachtag oder kommagetrennte Liste mit optionalen Qualitätswerten (`q`)
- **Beispiel-Priorität:** `en-US, fr-CA;q=0.8, fr;q=0.7` = bevorzugt US-Englisch, dann kanadisches Französisch, dann allgemeines Französisch
- **Empfehlung:** Anfragen sollten den `Accept-Language`-Header enthalten, idealerweise passend zu den Sprachpräferenzen des Client-Browsers oder User-Agents

---

## Response-Header für Lokalisierung

### Content-Language

```
Content-Language: de
```

- Gibt die tatsächlich zurückgegebene Sprache an
- Konsistent mit dem HTTP-Standard

### Octo-Available-Languages

```
Octo-Available-Languages: en,de,fr,es
```

- Listet alle Sprachen auf, in die der Supplier seinen Inhalt übersetzt hat
- Nützlich für Caching-Strategien: Separate Anfragen für jede unterstützte Sprache stellen

---

## Wie Lokalisierung funktioniert

1. Reseller sendet `Accept-Language: de` im Request-Header
2. OCTO API prüft, ob der Supplier deutschen Inhalt hat
3. Falls ja: deutsche Inhalte in `title`, `shortDescription`, `description`, etc. zurückgeben
4. Falls nein: Fallback auf Englisch (Standardsprache)
5. Response-Header `Content-Language` zeigt die tatsächlich gelieferte Sprache
6. Response-Header `Octo-Available-Languages` zeigt alle verfügbaren Sprachen

---

## Fehlermeldungen und Lokalisierung

Auch Fehlermeldungen werden lokalisiert. Das `errorMessage`-Feld in Error-Responses wird entsprechend dem `Accept-Language`-Header übersetzt.

---

## Caching-Strategie für lokalisierte Inhalte

Um Inhalte lokal in mehreren Sprachen zu speichern:

1. Zuerst `GET /products/` aufrufen und `Octo-Available-Languages` aus dem Response-Header lesen
2. Für jede verfügbare Sprache separate Anfragen mit dem entsprechenden `Accept-Language`-Header stellen
3. Lokalisierte Inhalte lokal cachen

```http
# Schritt 1: Verfügbare Sprachen ermitteln
GET /products/
Authorization: Bearer {token}
Octo-Capabilities:
→ Response-Header: Octo-Available-Languages: en,de,fr,es

# Schritt 2: Für jede Sprache abrufen
GET /products/{productId}
Authorization: Bearer {token}
Octo-Capabilities: octo/content
Accept-Language: de
→ Content-Language: de

GET /products/{productId}
Authorization: Bearer {token}
Octo-Capabilities: octo/content
Accept-Language: fr
→ Content-Language: fr
```

---

## Lokalisierbare Felder (mit octo/content Capability)

Wenn `octo/content` in `Octo-Capabilities` angegeben wird, enthält die Response:

### Product
- `title` — Öffentlicher, kundenorientierter Produktname
- `shortDescription` — Kurze Produktbeschreibung
- `description` — Ausführliche Produktbeschreibung
- `features[]` — Produktmerkmale (inkl., exkl., Highlights, etc.)
- `faqs[]` — Häufig gestellte Fragen
- `media[]` — Bilder, Videos (mit URL, Titel, Caption)
- `locations[]` — Geografische Standorte (mit Beschreibung)
- `categoryLabels[]` — Kategorien
- `commentary[]` — Kommentar-Optionen (Format + Sprache)

### Option
- `title`, `shortDescription`, `description`
- `features[]`, `faqs[]`, `media[]`, `locations[]`
- `categoryLabels[]`, `commentary[]`

### Unit
- `title` — Öffentlicher Name (z.B. "Erwachsener")
- `shortDescription`
- `features[]`

---

## Sprachcode-Beispiele

| BCP 47 Tag | Sprache |
|-----------|---------|
| `en` | Englisch |
| `en-US` | Amerikanisches Englisch |
| `de` | Deutsch |
| `de-DE` | Deutsch (Deutschland) |
| `fr` | Französisch |
| `fr-FR` | Französisch (Frankreich) |
| `es` | Spanisch |
| `es-ES` | Spanisch (Spanien) |
| `it` | Italienisch |
| `pt` | Portugiesisch |
| `zh` | Chinesisch |
| `ja` | Japanisch |

---

**Quellen:**
- https://docs.ventrata.com/getting-started/localization
- https://docs.ventrata.com/getting-started/headers
