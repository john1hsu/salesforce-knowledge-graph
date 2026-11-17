---
id: kt:customer-community-licenses
type: Product
title: Customer Community Licenses
aliases: [Customer Community license, Customer Community Plus license, Customer Community Login license, Customer Community Plus Login license, Experience Cloud customer licenses]
domain: security-and-sharing
summary: >-
  The Experience Cloud user licenses for authenticated B2C customers: Customer Community, a roleless high-volume
  license that reaches records through sharing sets and share groups, and Customer Community Plus, which adds roles,
  standard sharing and reports; both come in member-based and login-based variants.
release: "Winter '27"
status: current
broader: [kt:user-licenses, kt:experience-cloud]
related: [kt:external-identity-license, kt:salesforce-sharing-model, kt:role-hierarchy, kt:person-accounts, kt:implicit-sharing]
relations:
  - {predicate: alternativeTo, object: kt:external-identity-license}
  - {predicate: dependsOn, object: kt:sharing-sets}
  - {predicate: dependsOn, object: kt:share-groups}
  - {predicate: contrastsWith, object: kt:partner-community-licenses}
  - {predicate: consumedBy, object: kt:experience-cloud}
sources:
  - id: s1
    title: "Experience Cloud User Licenses"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=users_license_types_communities.htm&language=en_US&type=0
    type: official-docs
    accessed: 2026-11-17
  - id: s2
    title: "About High-Volume Community or Site Users"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.networks_about_hvpu.htm&type=5
    type: official-docs
    accessed: 2026-11-17
  - id: s3
    title: "Experience Cloud Licenses Eligible for Upgrades"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=networks_license_upgrade_eligible.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-17
  - id: s4
    title: "Platform Sharing Architecture"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-sharing-architecture
    type: official-docs
    accessed: 2026-11-17
  - id: s5
    title: "Learn More About Experience Cloud Licenses"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=experience.exp_cloud_plan_licenses.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-17
created: 2026-11-17
---

# Customer Community Licenses

**Customer Community** and **Customer Community Plus** are the two Experience Cloud user licenses Salesforce positions for business-to-consumer sites: they give customers who have no other way into the org an authenticated login to an Experience Cloud site.[^s1][^s5] Salesforce's own shorthand is that Customer Community is the basic pass and Customer Community Plus the upgraded one.[^s5] Choosing between them is mostly a sharing-model decision, which is why the choice belongs with security and sharing rather than only with site design.

## The two tiers

**Customer Community** targets very large audiences that mainly need cases and knowledge. Salesforce recommends it for 100+ million users per org. Users can read and edit their account, and read, create and edit contacts and cases.[^s1] It replaces the old High Volume Customer Portal, Service Cloud Portal and Authenticated Sites Portal licenses.[^s1]

**Customer Community Plus** is for customers who need reports, dashboards and standard sharing. Salesforce recommends it for 1+ million users per org, or 10+ million with Account Role Optimization. It adds account create and lets users build and manage reports when they hold the extra permissions.[^s1] It is the successor to the Customer Portal Manager licenses.[^s1]

Both tiers work with person accounts and allow 10 custom objects per license.[^s1] Partner Community, the business-to-business sibling, doesn't support person accounts and is aimed at partner relationship management rather than customer self-service.[^s1]

## Member-based vs. login-based

Each tier is sold in two forms. A **member-based** license belongs to one named user, who can log in as often as they like. A **login-based** license (Customer Community Login, Customer Community Plus Login) is bought as a pool of monthly logins. Several logins by the same user on the same day count as one.[^s1] Salesforce provisions login licenses at a ratio of 1 to 20, so 1,000 monthly logins gives 20,000 login licenses. Overages are measured over 12 months, so 1,000 monthly logins buys 12,000 logins a year.[^s1] Sessions can be configured to time out after at most 24 hours.[^s1] Unauthenticated guest users don't consume any external license, but sites have monthly page-view limits.[^s1]

## How record access works

The real difference between the tiers is roles. **Customer Community users are high-volume users with no role**, which avoids role-hierarchy performance problems at scale.[^s2] The Architect sharing guide explains that their access comes from matching the user's Account and Contact lookups, not from the normal sharing model.[^s4] Admins give these users access through **sharing sets**, and use **share groups** to share the records they own back to internal users.[^s2][^s4] They can also see records through criteria-based sharing rules, implicit access to their own account and contact, Controlled by Parent objects, and public org-wide defaults.[^s2]

**Customer Community Plus users always have a role** under their account, so owner-based sharing rules, groups and the rest of the standard sharing model apply to them.[^s1][^s3] The trade-off is cost at scale: every account with Plus users adds external roles. By default an org can have 50,000 roles across all portals and sites, and Salesforce emails a warning at 95% of that limit. Account Role Optimization delays creating roles until a second user joins an account.[^s1]

## Limits and gotchas

- **High-volume restrictions.** Customer Community users can't own accounts or join account, opportunity or case teams. They also can't be in public or personal groups, or be added to owner-based sharing rules or manual shares.[^s2]
- **Plus caveats.** Plus users can't subscribe to reports, and they can't change the account or contact on a case they own.[^s1]
- **Email from Apex.** Customer Community users can't send email through Apex when `setSaveAsActivity` is true.[^s1]
- **Upgrades go one way.** An admin can upgrade Customer Community (or External Identity) to Plus by changing the license and profile on the user record. Once a user has a license that needs a role, the change can't be reversed.[^s3]
- **Upgrades strip assignments.** An upgrade removes sharing set, permission set and permission set license assignments, and Plus licenses don't include View All or Modify All Records.[^s3]
- **Plus to Partner isn't direct.** Moving from Customer Community Plus to Partner Community means disabling the customer user, enabling the account as a partner account, and re-enabling the contact as a partner user.[^s3]

## When to use which

Choose **Customer Community** for high-volume service portals where each person only needs their own cases, account and knowledge. Choose **Customer Community Plus** when customers must see each other's records through role-based sharing, or need reports and dashboards. Pick login-based variants for infrequent visitors.[^s1][^s3] Use the **External Identity** license when people only need to sign in, since it can be upgraded to either tier later.[^s3] Start license selection from site personas and their data needs: object access, reporting, login frequency and storage.[^s5]

## Connections

These licenses are a family within **user licenses** and are **consumed by** **Experience Cloud** sites.[^s1][^s5] The **External Identity license** is the cheaper **alternative** for sign-in-only users and is an upgrade path into both tiers.[^s3] Customer Community access **depends on sharing sets and share groups** because those users sit outside the **role hierarchy**. Plus users join the standard **sharing model** through external roles.[^s2][^s4] Both tiers rely on **implicit sharing** for a user's own account and contact, and both support **person accounts**.[^s1][^s2] They **contrast with Partner Community licenses**, which serve B2B partner scenarios and can't be used with person accounts.[^s1]

## Sources

[^s1]: Salesforce Help, "Experience Cloud User Licenses". https://help.salesforce.com/s/articleView?id=users_license_types_communities.htm&language=en_US&type=0 (accessed 2026-11-17)
[^s2]: Salesforce Help, "About High-Volume Community or Site Users". https://help.salesforce.com/s/articleView?language=en_US&id=platform.networks_about_hvpu.htm&type=5 (accessed 2026-11-17)
[^s3]: Salesforce Help, "Experience Cloud Licenses Eligible for Upgrades". https://help.salesforce.com/s/articleView?id=networks_license_upgrade_eligible.htm&language=en_US&type=5 (accessed 2026-11-17)
[^s4]: Salesforce Architects, "Platform Sharing Architecture". https://architect.salesforce.com/fundamentals/platform-sharing-architecture (accessed 2026-11-17)
[^s5]: Salesforce Help, "Learn More About Experience Cloud Licenses". https://help.salesforce.com/s/articleView?id=experience.exp_cloud_plan_licenses.htm&language=en_US&type=5 (accessed 2026-11-17)
