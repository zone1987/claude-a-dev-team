# Testing

Two independent ways to test, for different stages.

## EdinExplore: a fictional supplier

Ventrata runs **EdinExplore**, a test supplier account with common product configurations. It gives
access to products, bookings and API logs — the fastest way to exercise an integration without a
real supplier relationship.

- **Sign up**: <https://dashboard.ventrata.com/octo/signup> (company name, email, password). The
  page then shows the API endpoint and key to use.
- **Booking portal**: <https://edinexplore.portal.ventrata.site/> — the `Bookings` tab lists every
  booking made through the portal and the API, which is how you confirm your field values actually
  landed.
- **API logs**: the `API Logs` tab lists every request received for your credentials, and opens a
  full request/response view per entry.

The logs are the reason to prefer EdinExplore over a mock server: when a `400` is unclear, the log
shows exactly what arrived.

## `Octo-Env: test` against live credentials

When you must test with a real supplier's key, send `Octo-Env: test`. Such bookings:

- do not consume availability,
- produce barcodes that will not redeem,
- are not invoiced.

Switch to `Octo-Env: live` to sell for real.

**A supplier can force your connection into test mode**, which processes every request as
`Octo-Env: test` regardless of what you send. Suppliers commonly do this while reviewing test
bookings before approving go-live — so read the `Octo-Env` **response** header to learn which mode
actually applied. A confirmed booking that never appears in the supplier's system is usually this,
not a bug.

## Source

[docs.ventrata.com/getting-started/test-credentials](https://docs.ventrata.com/getting-started/test-credentials)
and `getting-started/headers`, retrieved 2026-08-20.
