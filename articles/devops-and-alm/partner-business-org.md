---
id: kt:partner-business-org
type: Concept
title: Partner Business Org
aliases: [PBO, Salesforce Partner Business Org, Partner Business Organization]
domain: devops-and-alm
summary: >-
  The internal-use production org that Salesforce provisions for each partner when it joins the Partner Community,
  with two Sales & Service Cloud Enterprise Edition licenses and preinstalled ISV tools such as the Environment Hub,
  License Management App, Channel Order App and Checkout Management App; Salesforce recommends it as the partner's Dev Hub.
release: "Winter '27"
status: current
broader: [kt:agentexchange, kt:environment-strategy]
related: [kt:dev-hub, kt:scratch-orgs, kt:second-generation-managed-packages]
relations:
  - {predicate: hasPart, object: kt:environment-hub}
  - {predicate: hasPart, object: kt:license-management-app}
  - {predicate: hasPart, object: kt:channel-order-app}
sources:
  - id: s1
    title: "Salesforce Partner Business Org (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/appexchange-partner-pbo-reference.html
    type: official-docs
    accessed: 2026-11-21
  - id: s2
    title: "Get Ready to Distribute on AppExchange (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packageGuide/appexchange_partner_start.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s3
    title: "Verify Access to Your Salesforce Partner Business Org (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/appexchange-partner-access-pbo.html
    type: official-docs
    accessed: 2026-11-21
  - id: s4
    title: "Request a Salesforce Partner Business Org (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/appexchange-partner-request-pbo.html
    type: official-docs
    accessed: 2026-11-21
  - id: s5
    title: "Join the Salesforce Partner Community (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/appexchange-partner-join.html
    type: official-docs
    accessed: 2026-11-21
  - id: s6
    title: "Manage Orgs with Environment Hub (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/environment-hub-intro.html
    type: official-docs
    accessed: 2026-11-21
created: 2026-11-21
---

# Partner Business Org

A **Partner Business Org (PBO)** is the org a Salesforce partner uses to run its own ISV, OEM or consulting business with Salesforce.[^s1] Salesforce describes it as an internal-use production org that ships with two Sales & Service Cloud Enterprise Edition licenses and a set of preinstalled partner tools.[^s1] The ISVforce Guide treats having a PBO as the second prerequisite for distributing on AgentExchange (formerly AppExchange), right after signing up for the partner program.[^s2]

## How you get one

The PBO is provisioned automatically when a company joins the Salesforce Partner Community.[^s1][^s2] Joining starts at partners.salesforce.com: the partner creates a Salesforce username, verifies it by email, sets a password and then joins the community.[^s5] Salesforce recommends creating a separate username for the Partner Community even if the person already has a Salesforce login, because that username gives immediate access to the PBO.[^s5]

To confirm access, the partner logs in at login.salesforce.com with the Partner Community username and searches the App Launcher for Environment Hub. If the Environment Hub app opens, the PBO is in place.[^s3] If it doesn't appear, or no PBO arrived on joining, the partner logs a case in Salesforce Help under the product "Partner Programs & Benefits" and topic "Demo & Partner Business Orgs", with the partner account selected in the account switcher.[^s4] Salesforce reviews the case and replies with next steps; the guide gives no turnaround time.[^s4]

## What's inside

The PBO is where the partner-operations apps live:[^s1]

- **Environment Hub** (preinstalled) connects, creates and logs in to many orgs from one place.[^s1][^s6]
- **License Management App (LMA)** (preinstalled) tracks leads and licenses for managed packages; its host org is called the License Management Org.[^s1]
- **Channel Order App (COA)** (preinstalled) submits customer orders to Salesforce for revenue sharing, and for OEMs, license provisioning. It needs extra setup first.[^s1]
- **Checkout Management App** (preinstalled) gives a KPI dashboard for AgentExchange Checkout, for US, UK and EU-based ISVs selling managed packages.[^s1]
- **Feature Management App** extends the LMA for dark launches and trials, but is **not** preinstalled.[^s1]

The PBO is also meant to be the partner's **Dev Hub**. Salesforce says every ISV and OEM partner should designate the PBO as its Dev Hub, where scratch orgs, second-generation managed packages and namespaces are created and managed.[^s1] Dev Hub starts out disabled in a newly provisioned PBO and has to be switched on in Setup.[^s1]

## Limits and gotchas

- **Not a development org.** The PBO is a production org for internal business use. Salesforce positions Partner Developer Edition (PDE) orgs, created from the PBO's Environment Hub, as the place for managed-package development.[^s1]
- **PDEs only come from the hub.** The Environment Hub is the only way ISV partners can create PDEs, which have a higher API call limit, more storage and more licenses than a regular Developer Edition org.[^s1]
- **Edition of hub features.** The Environment Hub itself runs in Enterprise, Performance and Unlimited Editions, in Lightning Experience and Salesforce Classic.[^s6]
- **Two licenses only.** The two included Enterprise Edition licenses suit a small operations team. Plan who needs access to the LMA, COA and Dev Hub.[^s1]
- **Enable Dev Hub early.** It's off by default, and packaging work can't start until it's on.[^s1]

## When to use it

Use the PBO for everything that runs the partner business: license and lead management, order submission, managing the org fleet and owning packages through Dev Hub.[^s1] Build and test in scratch orgs or PDEs created from it, not in the PBO itself.[^s1][^s6] Partners that join with a separate Partner Community username get this org straight away, so the packaging setup can begin on day one.[^s5]

## Connections

The PBO sits under **AgentExchange** and a partner's **environment strategy**, as the org that owns the rest of the partner's org landscape.[^s1][^s2] It **has part** the preinstalled **Environment Hub**, **License Management App** and **Channel Order App**, which is why those articles list it as a dependency.[^s1] It is **related** to **Dev Hub**, the role Salesforce recommends it take, and through that to **scratch orgs** and **second-generation managed packages**, which are created and owned there.[^s1]

## Sources

[^s1]: Salesforce Developers, "Salesforce Partner Business Org (ISVforce Guide)". https://developer.salesforce.com/docs/platform/isvforce/guide/appexchange-partner-pbo-reference.html (accessed 2026-11-21)
[^s2]: Salesforce Developers, "Get Ready to Distribute on AppExchange (ISVforce Guide)". https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packageGuide/appexchange_partner_start.htm (accessed 2026-11-21)
[^s3]: Salesforce Developers, "Verify Access to Your Salesforce Partner Business Org (ISVforce Guide)". https://developer.salesforce.com/docs/platform/isvforce/guide/appexchange-partner-access-pbo.html (accessed 2026-11-21)
[^s4]: Salesforce Developers, "Request a Salesforce Partner Business Org (ISVforce Guide)". https://developer.salesforce.com/docs/platform/isvforce/guide/appexchange-partner-request-pbo.html (accessed 2026-11-21)
[^s5]: Salesforce Developers, "Join the Salesforce Partner Community (ISVforce Guide)". https://developer.salesforce.com/docs/platform/isvforce/guide/appexchange-partner-join.html (accessed 2026-11-21)
[^s6]: Salesforce Developers, "Manage Orgs with Environment Hub (ISVforce Guide)". https://developer.salesforce.com/docs/platform/isvforce/guide/environment-hub-intro.html (accessed 2026-11-21)
