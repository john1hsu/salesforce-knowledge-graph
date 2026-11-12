---
id: kt:identity-connect
type: Product
title: Identity Connect
aliases: [Salesforce Identity Connect, Identity Connect for Active Directory]
domain: identity
summary: >-
  An on-premises Salesforce Identity add-on that provisions, updates and deactivates Salesforce users from Microsoft
  Active Directory and can optionally provide single sign-on; Salesforce is retiring it at each customer's order end
  date and is not building a replacement.
release: "Winter '27"
status: deprecated
broader: [kt:salesforce-identity]
related: [kt:single-sign-on-saml, kt:just-in-time-provisioning, kt:my-domain, kt:delegated-authentication]
relations:
  - {predicate: replacedBy, object: kt:salesforce-scim}
  - {predicate: dependsOn, object: kt:connected-apps}
  - {predicate: governedBy, object: kt:api-request-limits}
  - {predicate: dependsOn, object: kt:permission-set-licenses}
  - {predicate: alternativeTo, object: kt:just-in-time-provisioning}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "Identity Connect"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.identityconnect_about.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "Get to Know Identity Connect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/identity_connect/units/identity_connect_intro
    type: official-learning
    accessed: 2026-11-09
  - id: s3
    title: "Consider Other Features (Identity Connect)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/identity_connect/units/identity_connect_other
    type: official-learning
    accessed: 2026-11-09
  - id: s4
    title: "Identity Connect Retirement"
    publisher: Salesforce Help (Knowledge Article 000390663)
    url: https://help.salesforce.com/s/articleView?id=000390663&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-09
  - id: s5
    title: "Salesforce Active Product & Feature Retirements"
    publisher: Salesforce Help (Knowledge Article 000381744)
    url: https://help.salesforce.com/s/articleView?id=000381744&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-09
created: 2026-11-09
---

# Identity Connect

Identity Connect is a Salesforce Identity product that ties Microsoft Active Directory (AD) user accounts to Salesforce user records. When an account is created in AD, the matching Salesforce user is created; when an AD account changes, the change is pushed to Salesforce; and when a user is deprovisioned, their Salesforce session is revoked right away. It can also act as the single sign-on (SSO) service for Salesforce.[^s1] Salesforce has announced its retirement: it now receives security updates only and is retired for each customer when their subscription ends.[^s4][^s5]

## How it works

Identity Connect is installed on your own network, not in Salesforce. It runs as a service on Windows or Linux on a server that serves all licensed users, and setup starts by creating a dedicated Identity Connect integration user in the org.[^s1] The download bundles the application, its web services and an OrientDB database for settings and logs, which can be swapped for another database. Configuration covers the AD connection, a connected app in Salesforce, field mapping between AD and Salesforce, a sync schedule, and optional SSO.[^s2]

Data flows one way. AD is the source of truth, Identity Connect needs only read access to the AD users and groups it syncs, and it never writes back to AD. Edits made in Salesforce to a synced field are overwritten on the next sync unless that field is excluded from mapping.[^s2] There are two sync modes: **Live Updates** react to AD changes as they happen but do not do a full comparison, so changes made during an outage can be missed; **Scheduled Updates** compare all users and groups and correct drift. Trailhead recommends running both, with the scheduled job no more than once a day.[^s3]

For sign-in, users can be redirected to Identity Connect through My Domain authentication settings. Options include its built-in SSO login page, Kerberos-based Integrated Windows Authentication for users already signed in to the domain, and disabling Salesforce passwords entirely, which needs Delegated Authentication enabled by Salesforce Support and single sign-on enabled on the affected profiles. A Password Sync agent on a domain controller is also available but rarely used.[^s3]

## Limits and gotchas

- **Licensing:** it costs extra in Enterprise, Performance and Unlimited Editions; Developer Edition includes 10 Identity Connect permission set licenses.[^s1]
- **API consumption:** provisioning uses Salesforce REST API calls that count against the org's API limits, and scheduled full comparisons use far more calls than live updates.[^s3]
- **Profile blast radius:** a full sync run before mappings are finished can change profiles or permission sets for every user, so test with one user first and run the reconciliation report before syncing.[^s3]
- **Versions:** Identity Connect 2.1 and 3.0.X can no longer be downloaded as of Summer '23, and Salesforce tells customers on older versions to upgrade to 7.1.6.[^s1]

## Retirement and migration

Salesforce's retirement notice says most customers have moved to the cloud and other vendors now offer provisioning, so it will not build a replacement. Existing subscriptions are honored and supported until they end, and the retirements list gives the timing as each customer's order end date.[^s4][^s5] After that point, new AD users are not provisioned, existing users stop receiving updates, users disabled in AD are not deactivated in Salesforce, and any SSO through Identity Connect stops working.[^s4]

The recommended plan is to inventory orgs and servers, confirm whether each deployment does provisioning only or provisioning plus SSO, migrate, then remove the servers, binaries and managed package. Suggested targets include Microsoft's Azure AD connector for Salesforce, an existing general-purpose provisioning product, third-party identity vendors, or Salesforce's SCIM APIs.[^s4]

## When to use it (and when not)

Don't start new projects on Identity Connect. Existing customers should treat it as legacy and plan the move before their subscription ends.[^s4] For login-time user creation from an identity provider, just-in-time provisioning is a lighter option; for ongoing lifecycle management, a cloud identity provider or SCIM-based provisioning is the route Salesforce points to.[^s4][^s2]

## Connections

Identity Connect is part of **Salesforce Identity** (`broader`) and depends on a **connected app** for its access to the org.[^s2] Its sign-in features rely on **My Domain** and, for password-less operation, **delegated authentication**, and it overlaps with **SAML single sign-on**.[^s3] Its provisioning calls are governed by **API request limits**, and the licenses come as **permission set licenses**.[^s3][^s1] It is an alternative to **just-in-time provisioning**, and the `replacedBy` edge to **Salesforce SCIM** records a migration path Salesforce names, not a direct successor product.[^s4] Identity lifecycle design of this kind falls under the **Identity and Access Management Architect** certification.

## Sources

[^s1]: Salesforce Help, "Identity Connect". https://help.salesforce.com/s/articleView?id=sf.identityconnect_about.htm&language=en_US&type=5 (accessed 2026-11-09)
[^s2]: Trailhead, "Get to Know Identity Connect". https://trailhead.salesforce.com/modules/identity_connect/units/identity_connect_intro (accessed 2026-11-09)
[^s3]: Trailhead, "Consider Other Features". https://trailhead.salesforce.com/modules/identity_connect/units/identity_connect_other (accessed 2026-11-09)
[^s4]: Salesforce Help, "Identity Connect Retirement" (Knowledge Article 000390663). https://help.salesforce.com/s/articleView?id=000390663&language=en_US&type=1 (accessed 2026-11-09)
[^s5]: Salesforce Help, "Salesforce Active Product & Feature Retirements" (Knowledge Article 000381744). https://help.salesforce.com/s/articleView?id=000381744&language=en_US&type=1 (accessed 2026-11-09)
