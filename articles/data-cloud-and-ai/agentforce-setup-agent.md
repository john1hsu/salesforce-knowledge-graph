---
id: kt:agentforce-setup-agent
type: Feature
title: Setup with Agentforce
aliases: [Agentforce Setup agent, Setup agent, Ask Setup Agent, Agentforce for Setup, Salesforce Setup powered by Agentforce]
domain: data-cloud-and-ai
summary: >-
  A conversational AI agent inside Salesforce Setup that lets admins ask questions and request configuration work in
  natural language (users and access, permission sets, objects and fields, flows, formulas, org health), proposing each
  change for the admin to approve and logging it in the Setup Audit Trail; generally available since May 2026.
release: "Winter '27"
status: current
broader: [kt:agentforce]
related: [kt:agentforce-for-flow, kt:setup-audit-trail, kt:permission-set-groups]
relations:
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: dependsOn, object: kt:einstein-generative-ai-setup}
  - {predicate: dependsOn, object: kt:einstein-trust-layer}
sources:
  - id: s1
    title: "Setup with Agentforce Is Now Generally Available: Built With Admin Feedback at the Center"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/setup-with-agentforce-is-generally-available
    type: official-blog
    accessed: 2026-11-24
  - id: s2
    title: "Get Started with Setup with Agentforce (Setup with Agentforce for Admins)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/setup-with-agentforce-for-admins/get-started-with-setup-with-agentforce
    type: official-learning
    accessed: 2026-11-24
  - id: s3
    title: "Get to Know Setup with Agentforce (Setup with Agentforce: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-for-setup-quick-look/get-to-know-setup-with-agentforce
    type: official-learning
    accessed: 2026-11-24
  - id: s4
    title: "Salesforce Setup powered by Agentforce"
    publisher: Salesforce
    url: https://www.salesforce.com/platform/setup/
    type: official-blog
    accessed: 2026-11-24
created: 2026-11-24
---

# Setup with Agentforce

Setup with Agentforce (the Setup agent) is an AI agent built into Salesforce Setup. Instead of hunting through Setup menus, an admin types a request or question in natural language, and the agent answers, opens the right Setup page, or proposes a configuration change to carry out.[^s3] Salesforce positions it as a conversational alternative to menu-driven Setup.[^s4] It ran as a beta, which admins used at TDX 2026 to create objects and troubleshoot user access, and Salesforce announced general availability in May 2026.[^s1]

## What it can do

Trailhead groups the agent's work into a handful of admin jobs:

- **Users and access.** List active users, clone a user with their assignments, freeze an account or reset a password, and troubleshoot object, field and record access.[^s3]
- **Permissions and sharing.** Create and manage permission sets and permission set groups, and work with org-wide defaults and sharing rules.[^s2]
- **Building.** Create custom objects and fields, custom report types and Lightning pages, and create and manage flows.[^s2]
- **Formulas.** Write, fix or explain formulas; the product page describes repairing syntax errors and logic gaps in validation rules and formula fields.[^s3][^s4]
- **Org health and help.** Report org storage, user-license usage and security metrics, search Salesforce Help, and link to the relevant configuration page.[^s3][^s4]

A typical access question is whether a named user can see accounts; the agent replies with a list view of that user's object permissions rather than a prose answer.[^s3] The product page also says it can build objects and fields from a description of a business process and scan the schema for duplicate fields.[^s4]

## How it works

Admins open the agent from Setup Home or from the **Ask Setup Agent** button available on Setup pages, and can start from a suggested recommendation or the Prompt Library. Responses can be list views, records, documentation links or components, and new conversations open in a new tab.[^s3] Before it changes anything, the agent asks for confirmation and the admin approves or pauses the action. It only helps with tasks the admin already has permission to do, and its changes are recorded in the Setup Audit Trail.[^s2][^s3] Salesforce says the agent runs inside its AI trust layer and uses a model tuned for admin tasks.[^s4]

## Setup and licensing

The agent needs Agentforce and Data 360 enabled in the org; Salesforce notes both are included in Salesforce Foundations.[^s1] Trailhead's enablement path is: finish the Data 360 setup steps and turn on generative AI if needed, search Setup for Setup with Agentforce, click Get Started so the remaining prerequisites switch on, then turn the feature on.[^s3] Each admin who will use it then needs the **Setup with Agentforce User** permission set group, assigned through Permission Set Groups in Setup.[^s2]

## Limits and gotchas

- **Consumption is described differently by source.** The GA announcement says Setup actions are non-billable and use no Agentforce credits, with only the Help and Navigation action using a small amount of Data 360 credits.[^s1]
- **Monthly action allowance.** The product page says each org gets 500 free Setup agent actions per month across all users, resetting on the first of the month, and that the feature consumes Data 360 credits.[^s4] Check the current Help considerations before relying on either statement.[^s1]
- **Outputs vary.** Trailhead warns that AI-generated responses differ between runs, so the same prompt can return different results.[^s3]
- **Not a bypass of security.** Because it acts only within the admin's own permissions and asks for approval, it does not widen what an admin can change; review each proposed change as you would a manual one.[^s2]

## When to use it (and when not)

Use it for routine, well-scoped admin work: access troubleshooting, user maintenance, quick objects and fields, and formula help.[^s3] For flow design inside Flow Builder, Agentforce for Flow is the in-builder alternative. For changes that must move between environments, keep your usual sandbox-and-deploy release process; the agent is a faster way to make a change, not a substitute for change management, and its audit-trail entries are the record of what it did.[^s2]

## Connections

Setup with Agentforce is one of the Agentforce (`kt:agentforce`) capabilities aimed at admins.[^s1] It depends on Data 360 (`kt:data-cloud`) and on turning on generative AI (`kt:einstein-generative-ai-setup`), and it runs within the trust layer (`kt:einstein-trust-layer`).[^s3][^s4] Access to it is granted through a permission set group (`kt:permission-set-groups`), and every change it makes lands in the Setup Audit Trail (`kt:setup-audit-trail`).[^s2] It overlaps with Agentforce for Flow (`kt:agentforce-for-flow`), since both can create flows, but this agent works from Setup rather than inside Flow Builder.[^s2]

## Sources
[^s1]: Salesforce Admins Blog, "Setup with Agentforce Is Now Generally Available: Built With Admin Feedback at the Center". https://admin.salesforce.com/blog/2026/setup-with-agentforce-is-generally-available (accessed 2026-11-24)
[^s2]: Trailhead, "Get Started with Setup with Agentforce". https://trailhead.salesforce.com/content/learn/modules/setup-with-agentforce-for-admins/get-started-with-setup-with-agentforce (accessed 2026-11-24)
[^s3]: Trailhead, "Get to Know Setup with Agentforce". https://trailhead.salesforce.com/content/learn/modules/agentforce-for-setup-quick-look/get-to-know-setup-with-agentforce (accessed 2026-11-24)
[^s4]: Salesforce, "Salesforce Setup powered by Agentforce". https://www.salesforce.com/platform/setup/ (accessed 2026-11-24)
