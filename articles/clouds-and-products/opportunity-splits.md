---
id: kt:opportunity-splits
type: Feature
title: Opportunity Splits
aliases: [Opportunity Split, OpportunitySplit, Revenue Splits, Overlay Splits, Opportunity Product Splits]
domain: clouds-and-products
summary: >-
  Sales Cloud team-selling feature that credits opportunity team members with a share of an opportunity's amount (or
  another currency field) through revenue, overlay and custom split types, feeding forecasts, reports and commissions.
release: "Winter '27"
status: current
broader: [kt:sales-cloud]
related: [kt:collaborative-forecasts, kt:opportunity-teams, kt:role-hierarchy, kt:enterprise-territory-management]
relations:
  - {predicate: partOf, object: kt:sales-cloud}
  - {predicate: dependsOn, object: kt:opportunity-teams}
  - {predicate: integratesWith, object: kt:collaborative-forecasts}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: integratesWith, object: kt:change-data-capture}
  - {predicate: coveredBy, object: kt:sales-cloud-consultant-certification}
sources:
  - id: s1
    title: "OpportunitySplit (Object Reference for the Salesforce Platform)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunitysplit.htm
    type: official-docs
    accessed: 2026-11-06
  - id: s2
    title: "Sell as a Team and Split the Credit"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/leads_opportunities_lightning_experience/sell-as-a-team-and-split-the-credit
    type: official-learning
    accessed: 2026-11-06
  - id: s3
    title: "Team Selling Implementation Guide (Salesforce help PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/team_selling_implementation_guide.pdf
    type: official-docs
    accessed: 2026-11-06
  - id: s4
    title: "Opportunity Splits (Salesforce Spiff help)"
    publisher: Salesforce
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=sales.spiff_opportunity_splits.htm
    type: official-docs
    accessed: 2026-11-06
created: 2026-11-06
---

# Opportunity Splits

**Opportunity Splits** let a sales team share credit for a deal. Each split record assigns a percentage and resulting amount of an opportunity to one opportunity team member, so that pipeline, forecasts and compensation reflect everyone who contributed rather than only the opportunity owner.[^s1][^s2] By default the owner holds 100% of the revenue split until someone redistributes it.[^s2]

## How it works

Splits sit on top of team selling: opportunity teams must be enabled before splits can be switched on, and enabling splits requires the Modify All Data permission.[^s3] The feature is available in Performance and Developer Editions and in Enterprise and Unlimited Editions with Sales Cloud.[^s3] Only the opportunity owner, or a user above the owner in the role hierarchy, can add or adjust splits, using **Edit Opportunity Splits** on the opportunity.[^s2] An admin setting lets users add coworkers to the team while editing splits; without it, a person must already be a team member before receiving a split.[^s3]

Salesforce ships two default split types, both based on the opportunity Amount field:[^s3][^s2]

- **Revenue splits** divide the deal among people who are directly responsible for it; credit is capped at 100%, which typically mirrors revenue-based compensation.[^s2]
- **Overlay splits** recognise supporting effort (for example a technical specialist who ran the demo) and may total more than 100%, so overlay credit sits on top of the primary sellers' revenue credit.[^s2]

Admins can rename or deactivate the defaults and create up to 6 custom split types. A custom type can split any standard currency field, roll-up summary field or custom currency field, but not formula currency fields, and each custom type can optionally be validated to total 100%.[^s3] **Opportunity product splits** extend the same model to individual line items, keeping the 100% cap for revenue-style types and no cap for overlay-style types.[^s2]

In the data model, each split is an `OpportunitySplit` record in a master-detail relationship to its opportunity, with the split percentage, split amount, split owner, split type and a 255-character note.[^s1] When a split type is validated to 100% the percentage ranges from 0 to 100; otherwise it can range up to 1,000.[^s1] A blank split type falls back to the default type, which is validated to 100%.[^s1] The object supports create, update, upsert, delete and query calls; it was generally available from API version 28.0, gained a read-only line-item flag in API 57.0 and a territory lookup in API 62.0.[^s1]

## Limits and gotchas

- **Enablement is a heavy background job.** Turning splits on creates a split on every opportunity and can take several hours; Salesforce advises starting it at the end of the working day.[^s3]
- **Pre-flight cleanup.** Mass operations in progress, inactive currencies on opportunities, and opportunities owned by inactive or automated-process users can all make enablement fail.[^s3]
- **Storage.** Owner team-member records added during enablement consume extra data storage.[^s3]
- **Automation is paused during enablement only.** The enablement script temporarily disables validation rules, Apex triggers and workflows on opportunity team records.[^s3]
- **Layout constraints.** The multi-line split editor does not support rich text or multi-select picklist fields; users edit those on each split's detail page.[^s3]
- **Owner changes via API.** If the owner is changed through the API, the previous owner stays on the team with read-only access or the org-wide default.[^s1]
- **Downstream totals are not always 100%.** Commission tools that read splits must handle overlay types whose totals differ from 100%.[^s4]

## When to use it (and when not)

Use splits when credit for a single deal genuinely belongs to more than one person and that credit must appear in forecasts or pay. For simple visibility or collaboration without shared credit, opportunity teams alone are enough. Revenue splits suit quota attainment; overlay splits suit specialist or partner-support roles paid on top of the core sale.[^s2] Plan custom split types early, because each one also needs its own forecast type to be forecast.[^s3]

## Connections

Opportunity Splits are **part of** `kt:sales-cloud` and **depend on** `kt:opportunity-teams`, since every split owner must be a team member.[^s3] They **integrate with** `kt:collaborative-forecasts`: the Forecasts tab offers a Revenue Splits forecast, and each split type can have its own forecast type.[^s3] Edit rights follow the `kt:role-hierarchy`, because only the owner and users above them can change splits.[^s2] Since API 62.0 a split can reference a territory, linking it to `kt:enterprise-territory-management`.[^s1] Split data is **queried with** `kt:soql` against `OpportunitySplit`, and changes stream through `kt:change-data-capture` via the OpportunitySplitChangeEvent object.[^s1] Commission tools such as Salesforce Spiff consume split records, together with split types and teams, to calculate pay.[^s4] The topic is **covered by** `kt:sales-cloud-consultant-certification`.

## Sources

[^s1]: Salesforce, "OpportunitySplit (Object Reference for the Salesforce Platform)". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunitysplit.htm (accessed 2026-11-06)
[^s2]: Trailhead, "Sell as a Team and Split the Credit". https://trailhead.salesforce.com/content/learn/modules/leads_opportunities_lightning_experience/sell-as-a-team-and-split-the-credit (accessed 2026-11-06)
[^s3]: Salesforce, "Team Selling Implementation Guide". https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/team_selling_implementation_guide.pdf (accessed 2026-11-06)
[^s4]: Salesforce, "Opportunity Splits (Salesforce Spiff help)". https://help.salesforce.com/apex/HTViewHelpDoc?id=sales.spiff_opportunity_splits.htm (accessed 2026-11-06)
