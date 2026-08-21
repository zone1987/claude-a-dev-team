# Errors

OCTO answers with `200 OK` or `400 Bad Request` — nothing else. There is no `404`: an unknown ID is
a bad request, not a missing resource.

## Contents

- [Response shape](#response-shape)
- [Error codes](#error-codes)
- [Codes with extra fields](#codes-with-extra-fields)
- [A documentation typo to expect](#a-documentation-typo-to-expect)

## Response shape

```json
{
  "error": "INVALID_PRODUCT_ID",
  "errorMessage": "The Product ID was invalid or missing",
  "productId": "123"
}
```

- **error**: the machine-readable code from the table below.
- **errorMessage**: human-readable, and translated according to `Accept-Language`. Never match on
  this string — match on `error`.

Some codes add a field echoing the offending value, which is what makes the failure diagnosable.

## Error codes

| Code | Meaning |
|---|---|
| `INVALID_PRODUCT_ID` | Missing or invalid `productId` in the request. |
| `INVALID_OPTION_ID` | Missing or invalid `optionId` in the request. |
| `INVALID_UNIT_ID` | Missing or invalid `unitId` in the request. |
| `INVALID_AVAILABILITY_ID` | Missing or invalid `availabilityId` in the request. |
| `INVALID_BOOKING_UUID` | Missing or invalid booking UUID — or, when confirming, the booking has already expired. |
| `BAD_REQUEST` | Body malformed, a required field missing, or a wrong data type. |
| `UNPROCESSABLE_ENTITY` | Body is correct but cannot be processed, e.g. cancelling after the cancellation cutoff. |
| `INTERNAL_SERVER_ERROR` | Backend down or network outage. |
| `UNAUTHORIZED` | No API key sent in `Authorization` to an endpoint that requires one. |
| `FORBIDDEN` | API key invalid or revoked, or the resource is outside your access. |

`INVALID_BOOKING_UUID` on confirm usually means expiry, not a typo: an unconfirmed reservation dies
on its own. Read it as "reserve again", not "fix the UUID".

## Codes with extra fields

| Code | Extra field | Example value |
|---|---|---|
| `INVALID_PRODUCT_ID` | `productId` | `"123"` |
| `INVALID_OPTION_ID` | `optionId` | `"321"` |
| `INVALID_UNIT_ID` | `unitId` | `"senior"` |
| `INVALID_AVAILABILITY_ID` | `availabilityId` | `"2020-01-01T10:30+08:00"` |

```json
{
  "error": "INVALID_UNIT_ID",
  "errorMessage": "The Unit ID was invalid or missing",
  "unitId": "senior"
}
```

## A documentation typo to expect

The error table spells the code `INVALID_AVAILABILITY_ID`, but the example block below it spells
`INVALID_AVAILABILIY_ID` — missing the second `T`. Handle both when matching, and treat the table
spelling as canonical unless a live response says otherwise.

## Source

[docs.ventrata.com/getting-started/errors](https://docs.ventrata.com/getting-started/errors),
retrieved 2026-08-20.
