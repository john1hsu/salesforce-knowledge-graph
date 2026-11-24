---
id: kt:account-teams
type: Feature
title: Account Teams
aliases: [Account Team, AccountTeamMember, Account Team Members, Default Account Team, UserAccountTeamMember]
domain: security-and-sharing
summary: >-
  Sales Cloud feature that lists the users who jointly cover an account, each with a team role and separate access
  levels for the account and its contacts, opportunities and cases, granted through "Team" rows in the account share table.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model, kt:sales-cloud]
related: [kt:opportunity-teams, kt:organization-wide-defaults, kt:implicit-sharing, kt:enterprise-territory-management, kt:sharing-rules]
relations:
  - {predicate: partOf, object: kt:sales-cloud}
  - {predicate: dependsOn, object: kt:organization-wide-defaults}
  - {predicate: contrastsWith, object: kt:opportunity-teams}
  - {predicate: alternativeTo, object: kt:enterprise-territory-management}
  - {predicate: queriedWith, object: kt:soql}
sources:
  - id: s1
    title: "AccountShare (Object Reference for the Salesforce Platform)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s2
    title: "UserAccountTeamMember (Object Reference for the Salesforce Platform)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_useraccountteammember.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s3
    title: "Set Up Account Teams (Protect Your Data in Salesforce)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/protect-your-data-in-salesforce/set-up-account-teams
    type: official-learning
    accessed: 2026-11-24
  - id: s4
    title: "Sell as a Team (Sales Team Collaboration)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sales-team-collaboration/sell-as-a-team
    type: official-learning
    accessed: 2026-11-24
created: 2026-11-24
---

# Account Teams

An **account team** is the group of users who work together on one account, such as an account manager, a sales engineer and a support representative. Trailhead frames the feature around three benefits: each member's role on the account is explicit, each member gets access to the records they need, and team membership can drive reporting for compensation and quota credit.[^s4] Unlike an opportunity team, which forms around a single deal, an account team gives its members access to the account itself and to related contacts, cases and opportunities.[^s4]

## How it works

Account teams are off by default. An admin enables them in Setup under **Account Teams** by selecting Account Teams Enabled, then chooses which account page layouts get the Account Team related list, optionally adding it to users' customized related lists as well.[^s3] Team roles are defined under **Team Roles**, one value per line, for example Sales Engineer or Customer Support Rep.[^s3]

Each team member gets a role plus separate access levels for the account and for its opportunities, cases and contacts. The account-level grant is Read or Edit (shown as Read Only or Read/Write in the UI), while the opportunity, case and contact grants each allow None, Read or Edit.[^s2][^s3] The contact grant was added in API version 10.0 and cannot be set when the org's default contact access is Controlled by Parent.[^s2]

Users can also keep a **default account team**: from their user settings they add the colleagues they usually work with, each with a role and access levels, and then click **Add Default Team** on an account's Account Team related list to apply it.[^s3] Each rep has one default team, and the admin decides whether it is added automatically or whether reps apply it account by account.[^s4] In the API the default team is stored as `UserAccountTeamMember` records, available since API version 8.0 and only in orgs where account teams are enabled; Customer Portal and Chatter Free users can't use the object.[^s2]

## Sharing mechanics

Team access is enforced through the account share table. Each `AccountShare` row carries a `RowCause`, and the value **Team** marks a user or group that has access because it is an account team member.[^s1] Only rows with the Manual row cause can be created, edited or deleted directly; Team rows are read-only and change only when team membership changes.[^s1] An `AccountShare` row holds account, opportunity, case and contact access levels, and at least one of the account, opportunity or case levels must exceed the org-wide default for that object.[^s1] When a user has access for several reasons, such as Owner, Manual and ImplicitParent, Salesforce compresses those rows into one with the highest access.[^s1]

## Limits and gotchas

- **Grants must exceed the default.** Default team access levels must be higher than the org-wide default for accounts, cases, contacts and opportunities respectively, so a Public Read/Write org gains little from Edit grants.[^s2][^s1]
- **No direct share edits.** Integrations can't insert or update Team rows in `AccountShare`; they must write team membership records, because only Manual rows are writable.[^s1]
- **Controlled by Parent contacts.** When contacts are Controlled by Parent, the contact access level can't be set on default team members.[^s2]
- **Missing related list.** If the Account Team related list doesn't appear after enabling, add it to the account page layout from Object Manager.[^s3]
- **Share records aren't a contract.** Salesforce warns it may stop storing some share records, so don't build logic that depends on reading them.[^s1]

## When to use it (and when not)

Use account teams when the same people should cover a customer over the long term and need access to everything under that account, including its opportunities and cases.[^s4] Use opportunity teams when extra people are needed only on particular deals; with Private defaults, access to one opportunity already gives read-only access to its primary account.[^s4] Because teams are maintained per account by users, rule-based tools such as sharing rules or territory management scale better when access follows criteria like region or segment rather than named relationships.[^s1][^s4]

## Connections

Account teams are **part of** `kt:sales-cloud` and are one of the record-level access mechanisms of the `kt:salesforce-sharing-model`, writing Team rows to the account share table.[^s1] They **depend on** `kt:organization-wide-defaults`, since team grants must exceed the default to matter.[^s2] They **contrast with** `kt:opportunity-teams`: both assign people to roles, but account teams cover the whole account and its related records.[^s4] The ImplicitParent row cause that sits alongside Team rows is the `kt:implicit-sharing` behaviour.[^s1] For criteria-based coverage, `kt:enterprise-territory-management` (whose assignments appear as Territory row causes) and `kt:sharing-rules` (Rule rows) are the **alternatives**.[^s1] Team membership is **queried with** `kt:soql` against the team member objects.[^s2]

## Sources

[^s1]: Salesforce, "AccountShare (Object Reference for the Salesforce Platform)". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_accountshare.htm (accessed 2026-11-24)
[^s2]: Salesforce, "UserAccountTeamMember (Object Reference for the Salesforce Platform)". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_useraccountteammember.htm (accessed 2026-11-24)
[^s3]: Trailhead, "Set Up Account Teams (Protect Your Data in Salesforce)". https://trailhead.salesforce.com/content/learn/projects/protect-your-data-in-salesforce/set-up-account-teams (accessed 2026-11-24)
[^s4]: Trailhead, "Sell as a Team (Sales Team Collaboration)". https://trailhead.salesforce.com/content/learn/modules/sales-team-collaboration/sell-as-a-team (accessed 2026-11-24)
