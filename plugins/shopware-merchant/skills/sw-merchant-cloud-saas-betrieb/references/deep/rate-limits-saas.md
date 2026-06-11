# Shopware SaaS — Rate Limits (API-Begrenzungen)

**Quelle**: https://docs.shopware.com/de/shopware-6-de/saas/rate-limits

---

## Überblick

Shopware SaaS implementiert **Rate Limits** für bestimmte API-Endpunkte.
Überschreitungen führen zu HTTP `429 Too Many Requests`.

---

## Routen mit Rate Limits

| HTTP-Methode | Endpoint | Limit | Begründung |
|---|---|---|---|
| POST | `/api/oauth/token` | **10 pro Minute pro IP** | Tokens sind langfristig gültig und wiederverwendbar |
| POST | `/account/register` | **3 pro Minute pro IP** | Vermeidung übermäßiger Kontoerstellungen |
| POST | `/api/_action/mail-template/send` | **3 pro Minute pro IP** | Schutz vor massenhaftem E-Mail-Versand |
| POST | `/api/_action/index` | **1 pro Stunde pro IP** | Ressourcenintensiver Indizierungsprozess |
| POST | `/api/_action/indexing` | **1 pro Stunde pro IP** | Ressourcenintensiver Indizierungsprozess |

---

## Reaktion bei Überschreitung

- **HTTP Status Code:** `429 Too Many Requests`
- **Retry-After Header:** Gibt Sekunden bis zur nächsten möglichen Anfrage an

---

## Best Practice

> „Stelle eine effiziente API-Nutzung sicher, indem du Tokens zwischenspeicherst und Anfragen, wo möglich, bündelst."

**Empfehlungen:**
- OAuth-Tokens cachen (nicht bei jeder Anfrage neu generieren)
- API-Anfragen bündeln (Batch-Verarbeitung)
- Retry-After-Header auswerten und entsprechend warten

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/saas/rate-limits*
