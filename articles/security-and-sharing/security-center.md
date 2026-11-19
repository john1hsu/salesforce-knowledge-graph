---
id: kt:security-center
type: Product
title: Security Center
aliases: [Salesforce Security Center, Security Center app]
domain: security-and-sharing
summary: >-
  A separately licensed Salesforce app that collects security and governance metrics (authentication,
  permissions, users, packages, configuration and Health Check) from many orgs into one parent tenant,
  with trends, threshold alerts and deployable security policies.
release: "Winter '27"
status: current
broader: [kt:security-governance]
related: [kt:event-monitoring, kt:continuous-monitoring, kt:salesforce-shield, kt:transaction-security-policies]
relations:
  - {predicate: dependsOn, object: kt:security-health-check}
  - {predicate: integratesWith, object: kt:agentforce}
  - {predicate: integratesWith, object: kt:data-cloud}
  - {predicate: consumedBy, object: kt:model-context-protocol-in-agentforce}
sources:
  - id: s1
    title: "Learn About Security Center"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/security-center/learn-about-security-center
    type: official-learning
    accessed: 2026-11-19
  - id: s2
    title: "Gather and Review Security Data"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/ko/content/learn/modules/security-center/gather-and-review-security-data
    type: official-learning
    accessed: 2026-11-19
  - id: s3
    title: "Security Center: A Single View Into Your Security Controls Across All Your Orgs"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2020/security-center-a-single-view-into-your-security-controls-across-all-your-orgs
    type: official-blog
    accessed: 2026-11-19
  - id: s4
    title: "Learn About Security Center with Agentforce"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/security-center-with-agentforce-quick-look/learn-about-security-center-with-agentforce
    type: official-learning
    accessed: 2026-11-19
  - id: s5
    title: "Winter '27 Release: Architect Highlights"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/winter-27-release-architect-highlights/
    type: official-blog
    accessed: 2026-11-19
created: 2026-11-19
---

# Security Center

Security Center is a Salesforce app that gives admins and security teams one dashboard of security and data-governance metrics across a Salesforce estate. It covers authentication methods, sensitive permission assignments, installed packages, Security Health Check scores and settings, and security-related user and configuration data, so a team can check policy compliance and gather audit evidence without logging into every org.[^s1] It runs inside a Salesforce org and was introduced to the admin community in October 2020, initially as a read-only view of posture, with management capabilities planned for later versions.[^s3]

## How it works

**Parent and child tenants.** One org acts as the parent tenant and aggregates data; other orgs are connected as child tenants that send their data up. Once connected, the parent's Security Center app shows every connected tenant plus the parent itself.[^s1] Trailhead states you can connect as many child tenants as you like and disconnect them at any time. A production parent can connect production or sandbox children, while a sandbox parent can connect only sandbox children. The Manage Security Center permission is needed in both parent and child, and the credentials used for a child must belong to a user holding it.[^s2]

**Metrics.** Metrics fall into authentication, permission, user and configuration categories. Summary and category dashboards give snapshots, and each metric has a detail page with trend graphs, daily change highlights and record-level lists.[^s1] Typical views include assignments of Modify All Data, View All Data and Author Apex; logins by authentication type and MFA adoption; users inactive for 90 days; and managed, unmanaged and AgentExchange packages with whether each is on its latest version.[^s2] The original release also tracked which profile or permission set granted a sensitive permission, connected apps, and users who had never logged in.[^s3]

**Freshness and history.** Data updates once per day, and admins can refresh metrics on demand several times a day when they need closer watch. Up to 6 months of history is retained for trend review and sharing.[^s1][^s2]

**Alerts and policies.** Admins define custom alerts that fire by email or in-app when a metric crosses a threshold, for example the count of users with Modify All Data or a drop in the Health Check score, and Flow can tie those alerts into business processes.[^s1][^s2] Security Center data can also drive policies deployed to chosen tenants: a company might upload a Health Check baseline stricter than the Salesforce Baseline Standard and push it to selected orgs, then publish a new policy version if it proves too strict; the new version applies to the same tenants.[^s1]

## Agentforce and newer capabilities

Security Center with Agentforce adds Security Agent, a conversational assistant that turns natural-language requests into queries over Security Center and Event Monitoring data, summarizes a flagged user's activity from login, report and API logs, classifies the risk and proposes remediation such as locking a user or requiring MFA through predefined flows or APIs. It requires Security Center, Event Monitoring and an Agentforce Platform add-on, and runs through the Einstein Trust Layer; the customer configures what the agent is permitted to do.[^s4] Salesforce's Winter '27 architect highlights describe two further expansions available from mid-September 2026: MCP Server Monitoring (beta), which shows configured MCP servers with risk scores and configuration changes, and Security Mesh, which brings Salesforce and external security data together and needs Security Center, Data 360 and supporting licenses.[^s5]

## Limits and gotchas

- **Licensing:** Security Center is free in Developer Edition orgs; other editions need a license, obtained through the account team.[^s2][^s3]
- **Not real-time:** metrics are collected daily, with manual refreshes when closer watch is needed, so they track posture trends rather than live activity.[^s1]
- **Retention:** 6 months of history, so longer-term audit evidence must be exported or kept elsewhere.[^s2]
- **Sandbox parents** cannot aggregate production children, so a production org is the usual parent for an estate-wide view.[^s2]

## When to use it (and when not)

Use Security Center when security or governance teams must watch many orgs and sandboxes, standardize baselines across them, or answer recurring audit questions about who holds powerful permissions and how users authenticate.[^s1] For a single org, the built-in Health Check and Setup reports may be enough; for investigating individual user behavior, Security Agent draws on Event Monitoring logs, so event-level work pairs Security Center with Event Monitoring rather than relying on daily metrics alone.[^s1][^s4]

## Connections

Security Center is a tool of security governance (`kt:security-governance`), giving that function its multi-org monitoring and policy-deployment mechanism, and it supplies customer-side evidence for continuous monitoring (`kt:continuous-monitoring`).[^s1] It `dependsOn` Security Health Check (`kt:security-health-check`), whose scores and baselines it aggregates and deploys.[^s1] It is related to Event Monitoring (`kt:event-monitoring`), the Shield component whose logs Security Agent reads, to Salesforce Shield (`kt:salesforce-shield`), and to Transaction Security Policies (`kt:transaction-security-policies`), the in-org enforcement counterpart to its cross-org monitoring.[^s4] It `integratesWith` Agentforce (`kt:agentforce`) through Security Agent and with Data Cloud (`kt:data-cloud`, now branded Data 360) through Security Mesh, and its MCP Server Monitoring consumes the servers configured under the Model Context Protocol in Agentforce (`kt:model-context-protocol-in-agentforce`).[^s4][^s5]

## Sources

[^s1]: Salesforce Trailhead, "Learn About Security Center". https://trailhead.salesforce.com/content/learn/modules/security-center/learn-about-security-center (accessed 2026-11-19)
[^s2]: Salesforce Trailhead, "Gather and Review Security Data". https://trailhead.salesforce.com/ko/content/learn/modules/security-center/gather-and-review-security-data (accessed 2026-11-19)
[^s3]: Salesforce Admins Blog, "Security Center: A Single View Into Your Security Controls Across All Your Orgs". https://admin.salesforce.com/blog/2020/security-center-a-single-view-into-your-security-controls-across-all-your-orgs (accessed 2026-11-19)
[^s4]: Salesforce Trailhead, "Learn About Security Center with Agentforce". https://trailhead.salesforce.com/content/learn/modules/security-center-with-agentforce-quick-look/learn-about-security-center-with-agentforce (accessed 2026-11-19)
[^s5]: Salesforce, "Winter '27 Release: Architect Highlights". https://www.salesforce.com/blog/winter-27-release-architect-highlights/ (accessed 2026-11-19)
