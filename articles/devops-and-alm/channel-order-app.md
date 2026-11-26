---
id: kt:channel-order-app
type: Tool
title: Channel Order App
aliases: [COA, Salesforce Channel Order App, Partner Order app, CHANNEL_ORDERS]
domain: devops-and-alm
summary: >-
  The managed app, preinstalled in every Partner Business Org, that ISV and OEM partners use to submit service
  orders to Salesforce Partner Operations after each customer transaction, driving revenue sharing, billing and
  (for OEM) license provisioning; net-new eligible deals now go through the AgentExchange Go-To-Market App instead.
release: "Winter '27"
status: current
broader: [kt:agentexchange]
related: [kt:license-management-app, kt:environment-hub, kt:appexchange-security-review, kt:permission-sets]
relations:
  - {predicate: partOf, object: kt:partner-business-org}
  - {predicate: alternativeTo, object: kt:agentexchange-go-to-market-app}
  - {predicate: dependsOn, object: kt:license-management-app}
  - {predicate: consumedBy, object: kt:batch-apex}
sources:
  - id: s1
    title: "Channel Order App (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/coa-welcome.html
    type: official-docs
    accessed: 2026-11-26
  - id: s2
    title: "Report Orders to Salesforce with the Channel Order App (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/coa-intro.html
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "Channel Order App Objects (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/coa-objects.html
    type: official-docs
    accessed: 2026-11-26
  - id: s4
    title: "Service Order (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/coa-objects-service-order.html
    type: official-docs
    accessed: 2026-11-26
  - id: s5
    title: "Channel Order App Upgrade Considerations (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/coa-upgrade-considerations.html
    type: official-docs
    accessed: 2026-11-26
  - id: s6
    title: "Partner Order Submit API (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/coa-serviceorderprocessor.html
    type: official-docs
    accessed: 2026-11-26
  - id: s7
    title: "Intro to Channel Order App for AppExchange Partners (Trailhead)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/channel-order-app-basics/appexchange_channel_orders_get_started
    type: official-learning
    accessed: 2026-11-26
  - id: s8
    title: "Migrate Existing Orders to the Go-To-Market App (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/partner-marketplace-coa-transition.html
    type: official-docs
    accessed: 2026-11-26
created: 2026-11-26
---

# Channel Order App

The Channel Order App (COA) is how a Salesforce partner tells Salesforce that a customer bought, changed or cancelled the partner's AgentExchange product. Each submitted order goes to Salesforce Partner Operations, which activates or provisions the product and invoices the partner under the partnership agreement. The guide is explicit that partners must submit an order after every customer transaction to stay compliant with their revenue-sharing agreement.[^s1]

COA comes preinstalled in the partner's Partner Business Org. OEM partners use it both for revenue sharing and to provision Salesforce licenses, while ISV partners use it for revenue sharing only. Partners who collect payments through AgentExchange Checkout should not use COA, because that revenue is reported automatically.[^s2] Before first use, a partner acquires its PBO, passes security review and completes Partner Operations training, requested through a support case.[^s2]

## How it works

The app is built on a small set of custom objects in the `CHANNEL_ORDERS` namespace:[^s3]

- **Customer**: the buyer's billing address and Salesforce org ID, created by the wizard on an initial order.[^s3]
- **Partner Product Catalog** and **Partner Contract Terms**: what the partner may sell and the default contract terms; Salesforce configures both.[^s3]
- **Service Order** and **Service Order Detail**: the order itself and its line items, such as license count and price per license.[^s3]

Contract terms carry defaults such as contract length, auto-renewal, renewal length, cancellation terms and billing frequency, and catalog entries are priced either as a fixed monthly rate or as a percentage of net revenue, per org or per user.[^s7]

A partner opens the wizard from the Service Orders tab, enters or picks the customer, chooses contract terms and products, sets quantity, price and start date, and submits.[^s3] The Service Order's `Order_Type__c` picklist offers Initial, Add-On, Reduction, Cancellation Order, Upgrade - Partner App (used for renewals) and Upgrade - Org Edition (used for edition upgrades).[^s4] Status moves through Draft, Submitted, Received, In Process, Error, Activated and Provisioned, and only Draft orders can be submitted; the start date must be today or later.[^s4] Submitted orders can later be edited, recalled or cloned, and drafts deleted.[^s1]

The License Management App remains the source of truth for licenses, but changes made there don't flow into COA, so every license change needs a matching order.[^s7]

## Limits and gotchas

- COA v2 replaced the old profile with permission sets, the Orders tab with Service Orders, and the credentials page with a COA Setup page; after upgrading, refresh the connection or Salesforce can't receive orders.[^s5]
- The legacy Partner Order Submit API (`ServiceOrderProcessor`) works only in COA 1.39 and earlier, accepts one order per call, can run once per Apex transaction and takes sets of at most 5 IDs.[^s6]
- Its replacement, the Channel Order Apex API in v2, adds edit, recall and clone but no longer updates the order status field itself.[^s5]
- ISVforce partners must give Salesforce 7 days' notice before renewal for cancellations, reductions or other decreases in value; billing continues until a cancellation order is processed.[^s7]

Because the legacy API is limited to one order per call, Salesforce's own example submits draft orders from a Batch Apex job with a scope of one.[^s6]

## When to use it (and when not)

Net-new orders that meet the AgentExchange Go-To-Market App's requirements must go through that app, and "net-new" is judged per product.[^s8] COA still handles existing offline contracts: a customer who bought App A through COA keeps buying more App A licenses there until the contract ends, since GTM add-ons can't extend offline purchases.[^s8] To move a customer, the partner submits a COA cancellation at least 7 days before renewal, then sends a GTM offer whose start date matches the cancelled order's expiration.[^s8]

## Connections

COA is part of the `kt:partner-business-org` alongside the `kt:environment-hub` and `kt:license-management-app`, on which its license reconciliation depends.[^s2][^s7] It sits under `kt:agentexchange` as the offline order-reporting channel and is the alternative to the `kt:agentexchange-go-to-market-app` for deals that don't qualify for, or predate, marketplace transactions.[^s8] Access in v2 is granted through `kt:permission-sets`, onboarding follows the `kt:appexchange-security-review`, and bulk submission via the legacy API is typically wrapped in `kt:batch-apex`.[^s5][^s2][^s6]

## Sources
[^s1]: Salesforce Developers, "Channel Order App". https://developer.salesforce.com/docs/platform/isvforce/guide/coa-welcome.html (accessed 2026-11-26)
[^s2]: Salesforce Developers, "Report Orders to Salesforce with the Channel Order App". https://developer.salesforce.com/docs/platform/isvforce/guide/coa-intro.html (accessed 2026-11-26)
[^s3]: Salesforce Developers, "Channel Order App Objects". https://developer.salesforce.com/docs/platform/isvforce/guide/coa-objects.html (accessed 2026-11-26)
[^s4]: Salesforce Developers, "Service Order". https://developer.salesforce.com/docs/platform/isvforce/guide/coa-objects-service-order.html (accessed 2026-11-26)
[^s5]: Salesforce Developers, "Channel Order App Upgrade Considerations". https://developer.salesforce.com/docs/platform/isvforce/guide/coa-upgrade-considerations.html (accessed 2026-11-26)
[^s6]: Salesforce Developers, "Partner Order Submit API". https://developer.salesforce.com/docs/platform/isvforce/guide/coa-serviceorderprocessor.html (accessed 2026-11-26)
[^s7]: Trailhead, "Intro to Channel Order App for AppExchange Partners". https://trailhead.salesforce.com/content/learn/modules/channel-order-app-basics/appexchange_channel_orders_get_started (accessed 2026-11-26)
[^s8]: Salesforce Developers, "Migrate Existing Orders to the Go-To-Market App". https://developer.salesforce.com/docs/platform/isvforce/guide/partner-marketplace-coa-transition.html (accessed 2026-11-26)
