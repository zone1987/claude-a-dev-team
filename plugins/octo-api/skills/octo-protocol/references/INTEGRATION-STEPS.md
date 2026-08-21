# Integration steps

Ventrata's own four-step path for a reseller connecting to suppliers that use Ventrata.

## 1. Review and plan

Decide which endpoints and capabilities to implement. **Ventrata requires every reseller to support
the OCTO core endpoints as a minimum**: products, availability, bookings.

Capabilities are optional, but Ventrata **strongly recommends `octo/pricing`**, because dynamic
pricing is now widely used by their clients. Treat pricing as effectively required for a commercial
integration.

## 2. Develop

Most resellers finish in **2 to 10 days**. If you already support OCTO through another booking or
ticketing system, you can usually skip straight to testing.

Build against the EdinExplore test supplier from the first day — see [TESTING.md](TESTING.md).

## 3. Test and get reviewed

After self-testing, Ventrata reviews the integration before go-live. Response target is **1 to 2
business days**. They may ask for:

- additional test bookings, including updates and cancellations,
- a voucher sample,
- confirmation of which capabilities you support.

For the partner listing they also need a company name, logo, favicon, a short supplier-facing
description and a website link. Collecting these early avoids a second review round.

## 4. Go live

The integration joins Ventrata's partner list and helpdesk documentation, so suppliers can enable it
and issue API keys. Only then can you approach suppliers to connect products and sell.

Because each supplier issues its own key, going live is per supplier, not once — see
[AUTHENTICATION.md](AUTHENTICATION.md).

## Source

[docs.ventrata.com/getting-started/steps-to-integrate](https://docs.ventrata.com/getting-started/steps-to-integrate),
retrieved 2026-08-20. Other use cases — a Ventrata client building their own checkout, or an operator
connection — go through Ventrata's connectivity team rather than this path.
