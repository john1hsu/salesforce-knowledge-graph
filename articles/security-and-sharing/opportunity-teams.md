---
id: kt:opportunity-teams
type: Feature
title: Opportunity Teams
aliases: [Opportunity Team, Team Selling, OpportunityTeamMember, Opportunity Team Members, Default Opportunity Team]
domain: security-and-sharing
summary: >-
  Sales Cloud team-selling feature that lists the users working an opportunity, each with a team role and an
  opportunity access level, and grants that access through "Sales Team" share rows on top of the org-wide default.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model, kt:sales-cloud]
related: [kt:account-teams, kt:opportunity-splits, kt:organization-wide-defaults, kt:implicit-sharing, kt:role-hierarchy]
relations:
  - {predicate: partOf, object: kt:sales-cloud}
  - {predicate: dependsOn, object: kt:organization-wide-defaults}
  - {predicate: enables, object: kt:opportunity-splits}
  - {predicate: contrastsWith, object: kt:account-teams}
  - {predicate: queriedWith, object: kt:soql}
sources:
  - id: s1
    title: "OpportunityTeamMember (Object Reference for the Salesforce Platform)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunityteammember.htm
    type: official-docs
    accessed: 2026-11-20
  - id: s2
    title: "OpportunityShare (Object Reference for the Salesforce Platform)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunityshare.htm
    type: official-docs
    accessed: 2026-11-20
  - id: s3
    title: "Team Selling & Opportunity Splits"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/leads_opportunities_lightning_experience/sell-as-a-team-and-split-the-credit
    type: official-learning
    accessed: 2026-11-20
  - id: s4
    title: "Sell as a Team (Sales Team Collaboration)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sales-team-collaboration/sell-as-a-team
    type: official-learning
    accessed: 2026-11-20
  - id: s5
    title: "Team Selling Implementation Guide (Salesforce help PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/team_selling_implementation_guide.pdf
    type: official-docs
    accessed: 2026-11-20
created: 2026-11-20
---

# Opportunity Teams

An **opportunity team** is the set of users working together on one opportunity. Each member is stored as an `OpportunityTeamMember` record that links a user to the opportunity with a team role and an opportunity access level, and the object exists only in orgs where team selling has been enabled.[^s1] Trailhead describes an opportunity team as a temporary group assembled to close a particular deal, unlike an account team, whose members are expected to build a long-term relationship with the customer.[^s3]

## How it works

An admin with the Customize Application permission turns the feature on under **Opportunity Team Settings** by selecting Enable Team Selling and choosing which opportunity page layouts receive the Opportunity Team related list.[^s5] The implementation guide lists team selling for Enterprise, Performance, Unlimited and Developer Editions; it is a Spring '23 document, so check current edition details before relying on it.[^s5] Team roles come from a picklist that the admin edits under Team Roles, and that picklist is shared with account team roles, so removing a value removes it from account teams as well.[^s5]

Users then open an opportunity, choose **Add Opportunity Team Members**, and set each person's name, role and opportunity access.[^s3] A user can also define a default opportunity team that is added automatically to new opportunities, or apply a default account team to an opportunity instead.[^s3]

In the data model, `OpportunityTeamMember` requires `OpportunityId` and `UserId`, neither of which can be changed after creation; an upsert that matches an existing pair updates that record rather than creating another.[^s1] `OpportunityAccessLevel` is a picklist of Read, Edit and All, editable from API version 36.0, and it can be used in triggers but not in workflow or validation rules.[^s1] Field history is available through `OpportunityTeamMemberHistory` from API version 59.0.[^s1]

## Sharing mechanics

Team access is enforced through the opportunity's share table. `OpportunityShare` rows carry a `RowCause`, and team access appears under the "Sales Team" row cause, whose access level is set by the team member record.[^s2] Only Manual share rows can be created, edited or deleted directly; team rows are read-only in the share object and are managed by adding, changing or removing team members.[^s2] A share's access must be higher than the org-wide default for opportunities, and when a user has access for several reasons the rows compress into one with the highest level.[^s2]

With a Private default for accounts and opportunities, giving a user access to an opportunity also gives read-only access to its primary account.[^s4] This is why opportunity teams are a common way to open individual deals to specialists without widening the org-wide default.

## Limits and gotchas

- **Owner changes through the API.** The previous owner stays on the team with Read Only or the org-wide default, whichever is greater; the UI lets the user choose the level instead.[^s1]
- **Access must exceed the default.** If opportunities are already Public Read/Write, a Read or Edit team grant adds nothing, because share access must be higher than the org-wide default.[^s2]
- **Shared role picklist.** Renaming or deleting a team role affects account teams, and the owner role should be left unchanged because opportunity splits depend on it.[^s5]
- **No direct share edits.** Integrations that try to insert or update "Sales Team" share rows will fail; write `OpportunityTeamMember` records instead.[^s2][^s1]

## When to use it (and when not)

Use opportunity teams when a few deals need extra people, such as product experts or a stalled deal that needs help, and those people need record access, accountability and reporting by role.[^s4] Use account teams when the same people should cover every opportunity on a long-term customer relationship.[^s3] For broad, rule-based access across many records, sharing rules or territory management scale better than per-record team membership, which users maintain by hand or through default teams.[^s2][^s3]

## Connections

Opportunity teams are **part of** `kt:sales-cloud` and are one of the record-level mechanisms in the `kt:salesforce-sharing-model`, writing "Sales Team" rows to the opportunity share table.[^s2] They **depend on** `kt:organization-wide-defaults`, since a team grant only matters when it exceeds the default.[^s2] Access to an opportunity can open its parent account read-only, which is the `kt:implicit-sharing` behaviour.[^s4] Team selling must be on before `kt:opportunity-splits` can be enabled, so teams **enable** splits.[^s5] They **contrast with** `kt:account-teams`, which share the same role picklist but model longer-term coverage.[^s3][^s5] Only the owner or users above the owner in the `kt:role-hierarchy` can add splits for team members.[^s3] Team membership is **queried with** `kt:soql` against `OpportunityTeamMember`.[^s1]

## Sources

[^s1]: Salesforce, "OpportunityTeamMember (Object Reference for the Salesforce Platform)". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunityteammember.htm (accessed 2026-11-20)
[^s2]: Salesforce, "OpportunityShare (Object Reference for the Salesforce Platform)". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunityshare.htm (accessed 2026-11-20)
[^s3]: Trailhead, "Team Selling & Opportunity Splits". https://trailhead.salesforce.com/content/learn/modules/leads_opportunities_lightning_experience/sell-as-a-team-and-split-the-credit (accessed 2026-11-20)
[^s4]: Trailhead, "Sell as a Team (Sales Team Collaboration)". https://trailhead.salesforce.com/content/learn/modules/sales-team-collaboration/sell-as-a-team (accessed 2026-11-20)
[^s5]: Salesforce, "Team Selling Implementation Guide". https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/team_selling_implementation_guide.pdf (accessed 2026-11-20)
