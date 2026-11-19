---
id: kt:licensing-strategy
type: Concept
title: Licensing Strategy
aliases: [Salesforce licensing strategy, license strategy, license selection, license mix design, persona-to-license mapping]
domain: architecture-practice
summary: >-
  The architect's practice of mapping each user persona to the least expensive Salesforce license combination that
  still meets its functional, security and scale needs — edition, user license, permission set licenses, member- or
  login-based external licenses — and of keeping that mix aligned with production as the org changes.
release: "Winter '27"
status: concept
broader: [kt:solution-design-tradeoffs, kt:salesforce-licensing]
related: [kt:user-licenses, kt:permission-set-licenses, kt:customer-community-licenses, kt:external-identity-license, kt:total-cost-of-ownership, kt:org-strategy]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: dependsOn, object: kt:profiles}
  - {predicate: dependsOn, object: kt:permission-sets}
  - {predicate: coveredBy, object: kt:experience-cloud-consultant-certification}
sources:
  - id: s1
    title: "Understand How Licenses Work (Salesforce Licensing module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/understand-how-licenses-work
    type: official-learning
    accessed: 2026-11-19
  - id: s2
    title: "Give Users the Functionality They Need (Salesforce Licensing module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/give-users-the-functionality-they-need
    type: official-learning
    accessed: 2026-11-19
  - id: s3
    title: "User Licenses"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.users_understanding_license_types.htm&type=5
    type: official-docs
    accessed: 2026-11-19
  - id: s4
    title: "When to Use an Internal or External License"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.users_internal_external_license_types.htm&type=5
    type: official-docs
    accessed: 2026-11-19
  - id: s5
    title: "Experience Cloud User Licenses"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=users_license_types_communities.htm&language=en_US&type=0
    type: official-docs
    accessed: 2026-11-19
  - id: s6
    title: "Salesforce Certified Experience Cloud Consultant Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298944&language=en_US&type=1
    type: official-learning
    accessed: 2026-11-19
    accessed: 2026-11-19
created: 2026-11-19
---

# Licensing Strategy

A **licensing strategy** is the part of solution design that decides which Salesforce licenses each group of users gets, and why. Customers buy editions and add-ons rather than individual licenses, but what those purchases contain — platform licenses for the org, one user license per user, and stackable permission set licenses — sets a hard ceiling on what any profile or permission set can grant.[^s1][^s2] Because Salesforce does not offer a license for every variation of access, the architect's job is to pick the cheapest license that covers a persona's real needs and then shape access with profiles and permission sets, instead of buying the most capable license for everyone.[^s2][^s3]

## The building blocks to combine

An org runs on exactly one edition license, which can be reached through several contracts, plus any number of add-ons.[^s1] Each user holds a single user license chosen for their role, can hold several permission set licenses on top of it, and gets one profile for baseline access plus permission sets for anything extra.[^s1][^s2] Salesforce Help adds feature licenses and usage-based entitlements as further ways to extend access without changing the user license.[^s3] Trailhead's worked example shows the pattern: an org buys Service Cloud Enterprise Edition with 100 Full CRM user licenses and an Einstein add-on with only 10 permission set licenses, because only 10 account executives need Einstein.[^s1]

## Decisions a licensing strategy makes

- **Full CRM or platform-only.** A Lightning Platform license covers custom apps, custom objects, reports and workflows but not CRM objects such as opportunities and cases, so it suits users who only work in custom apps.[^s3]
- **Seat or login.** Member (seat) licenses give one user unlimited logins and fit frequent users; login-based licenses draw from a pooled monthly allowance and fit occasional or external users.[^s3]
- **Internal or external.** Employees, and contractors treated like employees, need internal licenses; customers, partners, brokers and dealers belong on Experience Cloud licenses.[^s4]
- **Which external license.** The choice turns on B2C versus B2B, whether users need cases, reports or partner sales data, and whether person accounts are involved.[^s5]
- **Add-on or broader licenses.** An add-on supplements the single edition with platform or user licenses, and an org may carry any number of add-ons, so niche features can be bought for just the users who need them.[^s1]

## Internal versus external is a security decision

Salesforce frames the internal/external split as more than a price question. External users can reach only the Experience Cloud sites they belong to and never the internal Lightning Experience or Classic apps, and external license types carry an extra security layer that internal licenses lack.[^s4] Putting an external use case on an internal license widens data exposure, and Experience Cloud licenses must not be given to employees or contractors.[^s4] Salesforce's own example is independent brokers who need leads and opportunities but should not see internal Chatter feeds or cases.[^s4]

## Sizing external populations

Member-based external licenses include Customer Community, Customer Community Plus, Partner Community, External Apps and Channel Account; each has a login-based counterpart.[^s5] Login licenses count daily unique logins, switching between sites after login uses no extra login, and monthly logins are provisioned at a 1-to-20 ratio, with overages measured across the 12-month contract year and unused logins rolling over.[^s5] Channel Account licenses are counted per partner account rather than per person, allowing up to 40 partner users per licensed account.[^s5] Scale also steers the choice: Help points very large audiences, 100 million or more users, to Customer Community or External Apps, and positions Partner Community, Channel Account and Customer Community Plus for 1 million or more users, or 10 million or more with account role optimization.[^s5] Unauthenticated guest users consume no external licenses at all.[^s5]

## Gotchas

- **Changing a user license is disruptive.** It removes the user's assigned permission sets and permission set licenses, so get the initial choice right.[^s3]
- **Sandboxes drift.** Provisioning applies to production only; refresh the sandbox or run the Match Production License tool after any license change.[^s1]
- **New licenses do nothing on their own.** After an upgrade or add-on, admins still assign profiles and permission sets to switch functionality on.[^s1][^s2]
- **Watch consumption.** Company Information in Setup lists purchased licenses and usage-based entitlements, and deactivating users frees seats.[^s3][^s5]

## Connections

Licensing strategy sits **under** `kt:solution-design-tradeoffs` and applies the general model of `kt:salesforce-licensing` to a specific org; it is **used by** the `kt:salesforce-architect`.[^s1] It chooses among `kt:user-licenses` and stacks `kt:permission-set-licenses` on them, and **depends on** `kt:profiles` and `kt:permission-sets`, which can never exceed what the licenses allow.[^s2] On the external side it picks between `kt:customer-community-licenses` and the other Experience Cloud types, or the identity-only `kt:external-identity-license`.[^s5] The license mix is a major input to `kt:total-cost-of-ownership` and interacts with `kt:org-strategy`, since each org needs its own edition.[^s1] Choosing external license types is an explicit objective of the `kt:experience-cloud-consultant-certification`, whose guide weights Sharing, Visibility, and Licensing at 17%.[^s6]

## Sources

[^s1]: Trailhead, "Understand How Licenses Work", Salesforce Licensing module. https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/understand-how-licenses-work (accessed 2026-11-19)
[^s2]: Trailhead, "Give Users the Functionality They Need", Salesforce Licensing module. https://trailhead.salesforce.com/content/learn/modules/salesforce-licensing/give-users-the-functionality-they-need (accessed 2026-11-19)
[^s3]: Salesforce Help, "User Licenses". https://help.salesforce.com/s/articleView?language=en_US&id=platform.users_understanding_license_types.htm&type=5 (accessed 2026-11-19)
[^s4]: Salesforce Help, "When to Use an Internal or External License". https://help.salesforce.com/s/articleView?language=en_US&id=platform.users_internal_external_license_types.htm&type=5 (accessed 2026-11-19)
[^s5]: Salesforce Help, "Experience Cloud User Licenses". https://help.salesforce.com/s/articleView?id=users_license_types_communities.htm&language=en_US&type=0 (accessed 2026-11-19)
[^s6]: Salesforce Help, "Salesforce Certified Experience Cloud Consultant Exam Guide". https://help.salesforce.com/s/articleView?id=005298944&language=en_US&type=1 (accessed 2026-11-19)
