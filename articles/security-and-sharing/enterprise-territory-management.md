---
id: kt:enterprise-territory-management
type: Feature
title: Sales Territories
aliases: [Enterprise Territory Management, ETM, Territory Management 2.0, TM2, Salesforce Sales Territories, territory model]
domain: security-and-sharing
summary: >-
  Salesforce's territory feature (formerly Enterprise Territory Management) for modelling a sales organisation as
  territory hierarchies inside versioned territory models, assigning accounts, leads, opportunities and users to
  territories by rule or by hand, and granting record access through territory membership rather than ownership.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:role-hierarchy, kt:sharing-rules, kt:sharing-recalculation, kt:implicit-sharing, kt:restriction-rules]
relations:
  - {predicate: partOf, object: kt:sales-cloud}
  - {predicate: contrastsWith, object: kt:role-hierarchy}
  - {predicate: causes, object: kt:group-membership-locking}
  - {predicate: governedBy, object: kt:data-skew}
  - {predicate: coveredBy, object: kt:sharing-and-visibility-architect-certification}
sources:
  - id: s1
    title: "Sales Territories (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=tm2_intro.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s2
    title: "Implementing Enterprise Territory Management (implementation guide PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/210/latest/en-us/sfdc/pdf/salesforce_implementing_territory_mgmt2_guide.pdf
    type: official-docs
    accessed: 2026-11-03
  - id: s3
    title: "Manage Territories and Crush Your Sales Goals (Trailhead, Sales Territories and Forecasting)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sales-territories-and-forecasting/manage-territories-and-crush-your-sales-goals
    type: official-learning
    accessed: 2026-11-03
  - id: s4
    title: "Optimize Enterprise Territory Management Performance (Trailhead)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/advanced-territory-management/optimize-enterprise-territory-management-performance
    type: official-learning
    accessed: 2026-11-03
  - id: s5
    title: "ObjectTerritory2Association (Object Reference, Winter '27, API 68.0)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_objectterritory2association.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s6
    title: "Designing Record Access for Enterprise Scale (PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/256/latest/en-us/sfdc/pdf/draes.pdf
    type: official-docs
    accessed: 2026-11-03
created: 2026-11-03
---

# Sales Territories

Sales Territories is the Salesforce feature for designing and running sales territory structures; Trailhead describes it as the product formerly known as Enterprise Territory Management (ETM), and current Salesforce Help uses the Sales Territories name throughout.[^s3][^s1] An admin creates territory types, builds a territory model, adds and tests account assignment rules, activates the model, and then assigns accounts, leads and users and reports on the result. It is available in Performance and Developer editions and in Enterprise and Unlimited editions with Sales Cloud.[^s1] Its data model is still the "Territory2" family of objects, for example ObjectTerritory2Association, which links a territory to an account or lead record and is documented in the Winter '27 (API 68.0) object reference.[^s5]

## How it works

A **territory model** is a complete hierarchy of territories that can be built and previewed without touching live access. Models move through states: *Planning* (the default for a new model, granting no access), *Active* (users get access to accounts in their territories) and *Archived* (configuration viewable, no access), plus *Activation Failed* and *Archiving Failed* error states. Only one model can be active at a time, an active model cannot be deleted, archived models cannot be reactivated, and cloning a model produces a new Planning model.[^s2] Trailhead frames this as the way to test alternative territory designs before deploying one, with account assignment happening automatically on deployment.[^s3]

**Territory types** categorise territories and carry an admin-defined numeric **priority**; they do not appear in the hierarchy itself. Priority matters when an account sits in several territories, which the feature permits.[^s2] **Assignment rules** match accounts on criteria such as postal code, industry, revenue or custom fields, and a rule can be applied to child territories so that a hierarchy branch inherits it.[^s2][^s3] Accounts can also be assigned manually.[^s2]

Opportunities get at most one territory. An Apex class implementing the OpportunityTerritory2AssignmentFilter interface decides it: if the parent account has one territory in the active model, that territory wins; with several, priority or custom logic chooses; with none, the opportunity is left unassigned.[^s2] Default access levels for accounts, opportunities, and (when their org-wide default is Private) contacts and cases are set in territory settings and can be overridden per territory.[^s2]

## Limits and gotchas

The implementation guide allows up to four territory models per org, clones included (two in Enterprise Edition), with only one active, 1,000 territories per model by default, and up to 15 assignment rules per territory; treat these as guide figures and confirm them against your org's allocations.[^s2] Trailhead's performance guidance adds practical thresholds: more than 10,000 records tied to one territory can cause performance problems, a 3:1 territories-to-users ratio is a useful rule of thumb, and assigning more than 1,500 users to a single territory should be done through the API rather than Setup.[^s4]

Other gotchas: prefer numeric rule criteria to string criteria and keep rules restrictive; the "evaluate this account against territory rules on save" option re-runs rules broadly and should be used sparingly; and when restructuring an active model, work from the lowest territory level upward to avoid recalculating the same access repeatedly.[^s4] Creating rules requires the Manage Territories permission plus View All on accounts, and disabling the feature removes all territory-based access, so archive the active model first.[^s2]

## When to use it (and when not)

Use territories when account access must follow geography, segment or product overlays that cut across the management chain, or when one account must be visible to several selling teams. The role hierarchy alone models reporting lines and a single owner per record; territories add a second, matrix-shaped access dimension.[^s1][^s2] For simple orgs where owner-plus-role access suffices, the extra model management, rule tuning and recalculation cost are not worth it.[^s4]

## Connections

Territories are a mechanism within the **Salesforce sharing model** and part of **Sales Cloud**, contrasting with **role hierarchy** as an access path that does not depend on ownership.[^s1][^s2] Territory changes feed **sharing recalculation** and take group-membership locks: Salesforce's record-access guide notes that territory operations do not block roles or public groups that exclude territories, but it lists which territory and role operations can run concurrently, the basis of **group membership locking**.[^s6] Overloaded territories behave like **data skew**, which is why the 10,000-record guidance exists.[^s4] Neighbouring controls include **sharing rules**, **implicit sharing** and **restriction rules**, and the topic is examined in the **Sharing and Visibility Architect certification**.

## Sources
[^s1]: Salesforce, "Sales Territories (Salesforce Help)". https://help.salesforce.com/apex/HTViewHelpDoc?id=tm2_intro.htm (accessed 2026-11-03)
[^s2]: Salesforce, "Implementing Enterprise Territory Management". https://resources.docs.salesforce.com/210/latest/en-us/sfdc/pdf/salesforce_implementing_territory_mgmt2_guide.pdf (accessed 2026-11-03)
[^s3]: Salesforce Trailhead, "Manage Territories and Crush Your Sales Goals". https://trailhead.salesforce.com/content/learn/modules/sales-territories-and-forecasting/manage-territories-and-crush-your-sales-goals (accessed 2026-11-03)
[^s4]: Salesforce Trailhead, "Optimize Enterprise Territory Management Performance". https://trailhead.salesforce.com/content/learn/modules/advanced-territory-management/optimize-enterprise-territory-management-performance (accessed 2026-11-03)
[^s5]: Salesforce, "ObjectTerritory2Association (Object Reference, Winter '27)". https://developer.salesforce.com/docs/atlas.en-us.264.0.object_reference.meta/object_reference/sforce_api_objects_objectterritory2association.htm (accessed 2026-11-03)
[^s6]: Salesforce, "Designing Record Access for Enterprise Scale". https://resources.docs.salesforce.com/256/latest/en-us/sfdc/pdf/draes.pdf (accessed 2026-11-03)
