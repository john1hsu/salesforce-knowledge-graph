---
id: kt:environment-hub
type: Tool
title: Environment Hub
aliases: [Salesforce Environment Hub, Env Hub, Environment Hub app]
domain: devops-and-alm
summary: >-
  A Salesforce app, preinstalled in every ISV partner business org, that lets a team connect, create, filter and
  single-sign-on into many orgs (development, test, demo and Trialforce source orgs) from one hub org, with each
  member represented as an EnvironmentHubMember record.
release: "Winter '27"
status: current
broader: [kt:application-lifecycle-management, kt:environment-strategy]
related: [kt:agentexchange, kt:sandbox-types, kt:scratch-orgs, kt:dev-hub, kt:second-generation-managed-packages, kt:first-generation-managed-packages]
relations:
  - {predicate: dependsOn, object: kt:partner-business-org}
  - {predicate: integratesWith, object: kt:license-management-app}
  - {predicate: integratesWith, object: kt:trialforce}
  - {predicate: dependsOn, object: kt:connected-apps}
  - {predicate: dependsOn, object: kt:single-sign-on-saml}
sources:
  - id: s1
    title: "Manage Orgs with Environment Hub (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/environment-hub-intro.html
    type: official-docs
    accessed: 2026-11-20
  - id: s2
    title: "Connect an Org to the Environment Hub (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/environment-hub-manage-connect-org.html
    type: official-docs
    accessed: 2026-11-20
  - id: s3
    title: "Single Sign-on in the Environment Hub (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/environment-hub-sso-mapping.html
    type: official-docs
    accessed: 2026-11-20
  - id: s4
    title: "Create an Org from the Environment Hub (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/environment-hub-manage-create-org.html
    type: official-docs
    accessed: 2026-11-20
  - id: s5
    title: "Configure the Environment Hub (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/environment-hub-get-started-configure-app.html
    type: official-docs
    accessed: 2026-11-20
  - id: s6
    title: "Salesforce Org Recommendations for ISVs"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/07/salesforce-org-recommendations-for-isvs
    type: official-blog
    accessed: 2026-11-20
created: 2026-11-20
---

# Environment Hub

The **Environment Hub** is a Salesforce app for connecting, creating, viewing and logging in to many orgs from one central org.[^s1] It runs in Enterprise, Performance and Unlimited Editions, in both Lightning Experience and Salesforce Classic.[^s1] ISV partners get it already installed in their **partner business org (PBO)**; other customers must open a Salesforce Support case to have it enabled.[^s5] Salesforce's ISV guidance positions the PBO's hub as the place to create the orgs a partner team uses for development, testing and demos.[^s6]

## How it works

Every org in the hub is a **member**, stored as an `EnvironmentHubMember` record. Salesforce treats it like a standard object such as Account or Contact, so teams can add custom fields and automation to it, and can set up SSO and user mappings through the API.[^s1] The member list can be filtered by edition, creation date, instance, origin and SSO status.[^s1] The ISV blog suggests adding an expiration-date field to members and using a flow to warn the team before orgs expire.[^s6]

**Connecting existing orgs.** An admin chooses Connect Org, enters the target org's admin username, signs in and approves access, which creates a connected app in the member org.[^s2] SSO is switched on by default during connection. The hub also discovers related orgs: sandboxes created from the connected org, patch orgs of a 1GP packaging org, Trialforce source orgs created from a Trialforce management org, and release orgs whose managed packages are registered in the License Management App.[^s2] Removing a member disconnects it but does not delete the org.[^s2]

**Creating new orgs.** From the PBO, users pick a purpose for the new org.[^s4]

- **Development** creates a Developer Edition org, used to define a namespace for 2GP development.[^s4]
- **Test/Demo** creates trial copies of standard editions, optionally from a Trialforce template.[^s4]
- **Trialforce Source Organization** creates a TSO directly, an alternative to running a Trialforce management org.[^s4]

Partner edition orgs come with higher limits, more storage and other customisations than standard trials.[^s4] Test and demo orgs expire after one year by default, and the expiry can be extended through a case.[^s6]

**Single sign-on.** Hub users can log in to members without separate passwords. The hub matches users by an explicit user mapping, then by Federation ID, then by a username formula; the first match wins, and if none matches the user sees the standard login page.[^s3]

## Limits and gotchas

- **20 orgs per day.** A hub can create up to 20 member orgs per day; more requires a support case in the Partner Community.[^s4]
- **No scratch orgs, no direct sandbox connection.** Scratch orgs cannot be connected. A sandbox joins only after its source org is connected and the sandbox is then refreshed.[^s2]
- **SSO edge cases.** SSO does not work for newly added users or for mappings defined in a sandbox; manage those in the sandbox's parent org.[^s3]
- **Branding.** Hub-created TSOs cannot carry custom login or email branding; branded trials still need a Trialforce management org.[^s4][^s6]
- **Permissions.** Creating orgs and configuring SSO need *Manage Environment Hub*; connecting orgs needs *Connect Organization to Environment Hub* plus *View Setup and Configuration*. Users need a Salesforce or Salesforce Platform license.[^s5]
- **Deleting a Hub Member record** disconnects the org and removes its service provider record if SSO was on.[^s5]

## When to use it (and when not)

Use the hub when a team, typically an ISV, juggles many long-lived orgs: packaging and namespace orgs, demo orgs, Trialforce source orgs and customer-like test editions, and wants one inventory with SSO.[^s1][^s6] It does not replace scratch orgs, which Salesforce recommends for source-driven development and automated testing and which last at most 30 days.[^s6] Nor is it a deployment tool: it manages access to orgs, not the movement of metadata between them.[^s1]

## Connections

- **Broader:** the hub is part of **application lifecycle management** and supports an **environment strategy** by inventorying the orgs in that landscape.[^s1]
- **Depends on:** the **partner business org** that hosts it for ISVs, **connected apps** created when orgs are connected, and **SAML single sign-on** for member logins.[^s5][^s2][^s3]
- **Integrates with:** the **License Management App**, whose release orgs it discovers, and **Trialforce**, whose source orgs it can create.[^s2][^s4]
- **Related:** **Sandbox types** and **scratch orgs** are the other environment kinds; **Dev Hub**, **second-generation managed packages** and **first-generation managed packages** define the packaging orgs it tracks; **AgentExchange** is where the resulting apps are listed.[^s1][^s6]

## Sources

[^s1]: Salesforce Developers, "Manage Orgs with Environment Hub" (ISVforce Guide). https://developer.salesforce.com/docs/platform/isvforce/guide/environment-hub-intro.html (accessed 2026-11-20)
[^s2]: Salesforce Developers, "Connect an Org to the Environment Hub" (ISVforce Guide). https://developer.salesforce.com/docs/platform/isvforce/guide/environment-hub-manage-connect-org.html (accessed 2026-11-20)
[^s3]: Salesforce Developers, "Single Sign-on in the Environment Hub" (ISVforce Guide). https://developer.salesforce.com/docs/platform/isvforce/guide/environment-hub-sso-mapping.html (accessed 2026-11-20)
[^s4]: Salesforce Developers, "Create an Org from the Environment Hub" (ISVforce Guide). https://developer.salesforce.com/docs/platform/isvforce/guide/environment-hub-manage-create-org.html (accessed 2026-11-20)
[^s5]: Salesforce Developers, "Configure the Environment Hub" (ISVforce Guide). https://developer.salesforce.com/docs/platform/isvforce/guide/environment-hub-get-started-configure-app.html (accessed 2026-11-20)
[^s6]: Salesforce Developers Blog, "Salesforce Org Recommendations for ISVs" (2024). https://developer.salesforce.com/blogs/2024/07/salesforce-org-recommendations-for-isvs (accessed 2026-11-20)
