---
id: kt:consent-management-in-data-cloud
type: Feature
title: Consent Management in Data 360
aliases: [consent management in Data Cloud, Data 360 consent management, Data Cloud consent, Marketing Cloud Next consent management, consent DMOs]
domain: data-cloud-and-ai
summary: >-
  The way Data 360 (formerly Data Cloud) stores and enforces customers' privacy and communication preferences as
  consent data model objects tied to contact points, subscriptions and channels, so that Marketing Cloud Next and
  other consumers check one central record of opt-ins and opt-outs instead of per-system checkboxes.
release: "Winter '27"
status: current
broader: [kt:data-cloud, kt:consent-data-model]
related: [kt:gdpr-international-transfers, kt:data-cloud-segmentation, kt:data-cloud-activation, kt:identity-resolution]
relations:
  - {predicate: dependsOn, object: kt:data-model-objects}
  - {predicate: consumedBy, object: kt:marketing-cloud-next}
  - {predicate: configuredVia, object: kt:data-cloud-triggered-flows}
sources:
  - id: s1
    title: "Explore Consent Tools and Concepts (Consent Management Fundamentals for Marketing Cloud Next)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/consent-management-fundamentals-for-marketing-cloud-next/explore-consent-tools-and-concepts
    type: official-learning
    accessed: 2026-11-20
  - id: s2
    title: "Get to Know Consent Best Practices and Considerations"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/consent-management-fundamentals-for-marketing-cloud-next/get-to-know-consent-best-practices-and-considerations
    type: official-learning
    accessed: 2026-11-20
  - id: s3
    title: "Party Consent DMO (Data 360 DMO and Mapping Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/data/data-cloud-dmo-mapping/guide/c360dm-party-consent-dmo.html
    type: official-docs
    accessed: 2026-11-20
  - id: s4
    title: "Privacy Overview Data Model (Data 360 Data Model Gallery)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/data-models/guide/privacy-overview.html
    type: official-docs
    accessed: 2026-11-20
  - id: s5
    title: "Design the Platform Consent Data Model for General Consent"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/consent-management-with-salesforce/design-the-consent-data-model-for-general-consent
    type: official-learning
    accessed: 2026-11-20
created: 2026-11-20
---

# Consent Management in Data 360

Consent management in Data 360 (formerly Data Cloud) is the practice of recording every opt-in and opt-out as data model objects (DMOs) in Data 360 rather than as a checkbox on a Lead or Contact. Marketing Cloud Next keeps all consent centrally in Data 360, which unifies inputs from sales, service and external sites around the Unified Individual, and checks those consent DMOs for the recipient's exact email address or phone number when a message is queued.[^s1] Salesforce's guidance frames Data 360 as the single source of truth, so that a customer who unsubscribes through one cloud does not keep receiving messages from another.[^s2]

## How it works

Consent hangs off the **contact point**, not the person. An email address or phone number is the anchor; if a customer's address changes, the old consent does not carry over and a new consent record is needed for the new address.[^s1][^s2] The Marketing Cloud Next model layers several objects on top of that anchor:[^s1]

- **Communication Subscription**: a list, topic or category such as a monthly newsletter or product updates.[^s1]
- **Engagement Channel Type**: the medium, for example email, SMS or WhatsApp.[^s1]
- **Communication Subscription Channel Type**: ties a subscription to a channel; a subscription can span channels, but the customer opts in per channel.[^s1]
- **Communication Subscription Consent**: the intersection of contact point, subscription and channel, holding the explicit opt-in or opt-out status, when it was captured and its source.[^s1]

These sit inside Salesforce's wider privacy data model, which the Data 360 data model gallery lists alongside Individual, Party Consent, Contact Point Email and Phone, Data Use Purpose, Data Use Legal Basis, Engagement Channel Type Consent and Authorization Form Consent.[^s4] The platform consent model distinguishes four levels: general consent (Individual or Party Consent), engagement channel consent, contact point consent for a data use purpose, and communication subscription consent for a specific publication.[^s5] In Data 360 the **Party Consent DMO** (API name `ssot__PartyConsent__dlm`, privacy subcategory) captures an individual's general consent, with fields for the captured contact point type, capture date and source, privacy consent status, party and party role, and effective-from and effective-to dates.[^s3]

## Capturing and changing consent

Salesforce offers several entry points:[^s1]

- **Preference pages**, built in the Content tab, let subscribers manage their own choices through dynamic links placed in email templates.[^s1]
- **Consent Status**, a Lightning web component for Prospect, Lead, Contact and Person Account pages, lets reps view and change opt-in status.[^s1]
- **Consent imports** create or update subscription consent and contact point records in bulk from CSV files.[^s1]
- **Flows**: only Data Cloud record-triggered, automation event-triggered and on-demand flows are supported, using the Create Consent or Consent Request actions.[^s1]

Trailhead explicitly warns against using the older MessagingConsent invocable actions for this, because they can cause system issues.[^s1] For a double opt-in, a flow sends a transactional confirmation email first and grants the opt-in only after the verification link is clicked, using the Consent Request action; writing straight to the DMO does not update marketing consent as expected because of a cache layer.[^s2]

## Gotchas and good practice

Never delete an active or historical Communication Subscription: deletion cascades and permanently removes its consent history, so retire a subscription by hiding it from preference pages instead.[^s2] When migrating legacy consent, set an accurate consent start date on each record to preserve the audit trail.[^s2] Consent is only as good as the underlying data, so deduplicated contact data and sound identity resolution matter; opt-in and opt-out trends can be watched with standard reports or Data Cloud segments, and a spike in opt-outs after a campaign is a signal about content or frequency.[^s2] The general-consent tutorial adds that Effective To and double-consent capture fields may need to be required depending on business rules and regional privacy law.[^s5]

## When to use which level

Subscription consent gives the finest control, for example a newsletter but not product updates on one address, while contact point type and contact point consent express consent for a whole data use purpose and pay off mainly when an org has several marketing purposes.[^s5] General consent on Party Consent fits binary signals such as a request not to be contacted at all.[^s5]

## Connections

Consent management is a capability of `kt:data-cloud` and a Data 360 expression of the platform `kt:consent-data-model`, built from `kt:data-model-objects` such as Party Consent.[^s3][^s4] `kt:marketing-cloud-next` consumes it at send time, and its records are typically maintained through `kt:data-cloud-triggered-flows` and other supported flow types.[^s1] Accurate consent depends on `kt:identity-resolution` producing clean unified profiles, and consent data can be monitored with `kt:data-cloud-segmentation` before audiences reach `kt:data-cloud-activation`.[^s2] Recording a data use purpose and legal basis alongside consent supports privacy obligations such as those discussed under the related `kt:gdpr-international-transfers`.[^s5]

## Sources
[^s1]: Trailhead, "Explore Consent Tools and Concepts". https://trailhead.salesforce.com/content/learn/modules/consent-management-fundamentals-for-marketing-cloud-next/explore-consent-tools-and-concepts (accessed 2026-11-20)
[^s2]: Trailhead, "Get to Know Consent Best Practices and Considerations". https://trailhead.salesforce.com/content/learn/modules/consent-management-fundamentals-for-marketing-cloud-next/get-to-know-consent-best-practices-and-considerations (accessed 2026-11-20)
[^s3]: Salesforce Developers, "Party Consent DMO". https://developer.salesforce.com/docs/data/data-cloud-dmo-mapping/guide/c360dm-party-consent-dmo.html (accessed 2026-11-20)
[^s4]: Salesforce Developers, "Privacy Overview Data Model". https://developer.salesforce.com/docs/platform/data-models/guide/privacy-overview.html (accessed 2026-11-20)
[^s5]: Trailhead, "Design the Platform Consent Data Model for General Consent". https://trailhead.salesforce.com/content/learn/modules/consent-management-with-salesforce/design-the-consent-data-model-for-general-consent (accessed 2026-11-20)
