---
id: kt:agentforce-nonprofit
type: Product
title: Agentforce Nonprofit
aliases: [Nonprofit Cloud, Salesforce Nonprofit Cloud, NPC]
domain: clouds-and-products
summary: >-
  Salesforce's built-in industry solution for nonprofits (formerly Nonprofit Cloud), which adds standard objects
  and apps for fundraising, program and case management, outcome management and stakeholder relationships to the
  core platform, as the native successor path to the Nonprofit Success Pack managed package.
release: "Winter '27"
status: current
broader: [kt:salesforce-industries]
related: [kt:contacts-to-multiple-accounts, kt:agentforce, kt:agentforce-nonprofit-consultant-certification]
relations:
  - {predicate: dependsOn, object: kt:person-accounts}
  - {predicate: alternativeTo, object: kt:nonprofit-success-pack}
sources:
  - id: s1
    title: "Learn About Salesforce for Nonprofits (Nonprofit Cloud Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/nonprofit-cloud-basics/learn-about-salesforceorg-nonprofit-cloud
    type: official-learning
    accessed: 2026-11-12
  - id: s2
    title: "Track Stakeholders and Their Relationships in Nonprofit Cloud"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/stakeholder-management-in-nonprofit-cloud/track-stakeholders-and-their-relationships-in-nonprofit-cloud
    type: official-learning
    accessed: 2026-11-12
  - id: s3
    title: "Meet Nonprofit Cloud for Fundraising"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/nonprofit-cloud-for-fundraising-quick-look/meet-nonprofit-cloud-for-fundraising
    type: official-learning
    accessed: 2026-11-12
  - id: s4
    title: "Fundraising Standard Objects (Nonprofit Cloud Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.nonprofit_cloud.meta/nonprofit_cloud/npc_fundraising_standard_objects.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s5
    title: "Program Management Standard Objects (Nonprofit Cloud Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.nonprofit_cloud.meta/nonprofit_cloud/npc_pm_standard_objects.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s6
    title: "Salesforce Certified Agentforce Nonprofit Consultant (credential page)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/it/credentials/agfnonprofitconsultant
    type: official-learning
    accessed: 2026-11-12
created: 2026-11-12
---

# Agentforce Nonprofit

**Agentforce Nonprofit** is Salesforce's built-in industry solution for charities, foundations and other mission-driven organizations. It was previously called **Nonprofit Cloud**, and Trailhead warns that the older name still shows up in the product and its documentation.[^s1] The core product bundles tools for fundraising, program management, case management and outcome management; a separate **Agentforce Nonprofit for Grantmaking** edition adds everything needed to run the grantmaking lifecycle for organizations that hand out funds or in-kind grants.[^s1] Unlike the older Nonprofit Success Pack (NPSP), which is a managed package installed into an org, Agentforce Nonprofit ships as standard platform functionality.[^s1][^s3]

## How it works

**Stakeholder model.** Individuals such as donors, program participants and grantmaker staff are stored as person accounts, which merge Account and Contact fields into one record.[^s2] A household is a business account that a **Party Relationship Group** record marks as a household (or other group); that object also carries household-level details such as financial information.[^s2] Three relationship objects connect records: account-contact relationships (person to business account), contact-contact relationships (person to person) and account-account relationships (organization to organization).[^s2] **Party Role Relationship** records define what a contact-contact or account-account link means, such as spouse or client and advisor, and reciprocal links like spouse-to-spouse need two records.[^s2]

**Fundraising.** Fundraising is delivered through four role-based apps: Fundraising Strategy, Donor Engagement, Philanthropy & Partnerships and Fundraising Operations.[^s3] Gift Entry lets processors key single, recurring or batched gifts, while Source Code and Campaign records track outreach and Actionable Lists help gift officers work major-donor portfolios.[^s3] Underneath sits a dedicated set of standard objects rather than repurposed Opportunities: GiftCommitment holds a pledge or recurring promise, GiftCommitmentSchedule defines how it is fulfilled, GiftTransaction records each completed payment, GiftDesignation and its junction to transactions allocate money to funds, and GiftSoftCredit credits people or organizations who influenced a gift.[^s4] Later API versions added planned giving (PlannedGift, annuity rates and performance), gift agreements, stewardship and prospect-research objects.[^s4]

**Program and case management.** Programs are modeled with Program, ProgramEnrollment, Benefit, BenefitAssignment, BenefitSchedule, BenefitSession and BenefitDisbursement, which together record who is enrolled, what they are entitled to and each delivery of a monetary or non-monetary benefit.[^s5] CaseProgram joins standard Cases to programs, and ProgramCohort with ProgramCohortMember (API 61.0) group enrollees into cohorts.[^s5]

## Limits and gotchas

- **Naming drift.** Help, Trailhead and API docs still say "Nonprofit Cloud", so search both names.[^s1]
- **Editions.** The program management objects list Enterprise and Unlimited Editions; fundraising objects add Developer Edition.[^s4][^s5]
- **Two-record reciprocity.** Reciprocal relationships must be stored as two records, which matters for data loads and duplicate checks.[^s2]
- **Not NPSP.** Fundraising and NPSP are separate products, so first confirm which one an org runs before applying documentation or configuration steps.[^s3]

## When to use it (and when not)

Choose Agentforce Nonprofit for a new nonprofit implementation that wants built-in tools for fundraising, programs, cases and outcomes instead of an installed package.[^s1] Orgs already on NPSP run a different, package-based data model; adopting Agentforce Nonprofit means landing their data on person accounts, party relationship groups and the gift objects, so plan it as a migration rather than an in-place upgrade.[^s1][^s2][^s4] Organizations that mainly distribute money should evaluate the Grantmaking edition rather than the base product.[^s1]

## Connections

Agentforce Nonprofit is one of the **Salesforce Industries** solutions layered on the core platform, and its stakeholder model **depends on person accounts** plus the contacts-to-multiple-accounts relationship records for households and employers.[^s1][^s2] It is the built-in **alternative to the Nonprofit Success Pack** managed package.[^s1] Its current name places it under the **Agentforce** brand.[^s1] Practitioners validate their skills with the **Salesforce Certified Agentforce Nonprofit Consultant** credential, which describes holders as experienced in designing and implementing the Nonprofit Cloud industry solution and requires Platform Administrator as a prerequisite.[^s6]

## Sources

[^s1]: Trailhead, "Learn About Salesforce for Nonprofits" (Nonprofit Cloud Basics). https://trailhead.salesforce.com/content/learn/modules/nonprofit-cloud-basics/learn-about-salesforceorg-nonprofit-cloud (accessed 2026-11-12)
[^s2]: Trailhead, "Track Stakeholders and Their Relationships in Nonprofit Cloud". https://trailhead.salesforce.com/content/learn/modules/stakeholder-management-in-nonprofit-cloud/track-stakeholders-and-their-relationships-in-nonprofit-cloud (accessed 2026-11-12)
[^s3]: Trailhead, "Meet Nonprofit Cloud for Fundraising". https://trailhead.salesforce.com/content/learn/modules/nonprofit-cloud-for-fundraising-quick-look/meet-nonprofit-cloud-for-fundraising (accessed 2026-11-12)
[^s4]: Salesforce, "Fundraising Standard Objects", Nonprofit Cloud Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.nonprofit_cloud.meta/nonprofit_cloud/npc_fundraising_standard_objects.htm (accessed 2026-11-12)
[^s5]: Salesforce, "Program Management Standard Objects", Nonprofit Cloud Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.nonprofit_cloud.meta/nonprofit_cloud/npc_pm_standard_objects.htm (accessed 2026-11-12)
[^s6]: Trailhead, "Salesforce Certified Agentforce Nonprofit Consultant". https://trailhead.salesforce.com/it/credentials/agfnonprofitconsultant (accessed 2026-11-12)
