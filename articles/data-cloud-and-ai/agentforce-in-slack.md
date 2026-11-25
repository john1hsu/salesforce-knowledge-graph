---
id: kt:agentforce-in-slack
type: Feature
title: Agentforce in Slack
aliases: [Agentforce for Slack, Slack agents, Agentforce Slack deployment, Agentforce Hub in Slack, Slack connection for agents]
domain: data-cloud-and-ai
summary: >-
  The deployment channel that takes an Agentforce agent built in Salesforce and installs it in a Slack workspace or
  Enterprise organization, where members reach it from the Agents area, direct messages or channel @mentions, after
  the Salesforce org is connected to Slack and Slack members are mapped to Salesforce users.
release: "Winter '27"
status: current
broader: [kt:agentforce]
related: [kt:agentforce-employee-agents, kt:agentforce-subagents, kt:agent-actions, kt:permission-sets]
relations:
  - {predicate: partOf, object: kt:agentforce}
  - {predicate: integratesWith, object: kt:slack-platform}
  - {predicate: configuredVia, object: kt:agentforce-studio}
  - {predicate: dependsOn, object: kt:salesforce-sharing-model}
  - {predicate: dependsOn, object: kt:einstein-trust-layer}
  - {predicate: dependsOn, object: kt:connected-apps}
sources:
  - id: s1
    title: "Set up and manage Agentforce in Slack"
    publisher: Slack (Salesforce)
    url: https://slack.com/help/articles/36218109305875-Set-up-and-manage-Agentforce-in-Slack
    type: official-docs
    accessed: 2026-11-25
  - id: s2
    title: "Configure a Slack Agent in Salesforce (Enhance Your Agent with Slack Integration and Actions)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-configuration-for-slack-deployment/configure-a-slack-agent-in-salesforce
    type: official-learning
    accessed: 2026-11-25
  - id: s3
    title: "Deploy an Agent in Slack (Deploy and Manage AI Agents in Your Organization's Slack)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-configuration-for-slack-deployment/deploy-an-agent-in-slack
    type: official-learning
    accessed: 2026-11-25
  - id: s4
    title: "Integrate AI Agents with Slack for Productivity"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/slack-ai/integrate-ai-agents-with-slack
    type: official-learning
    accessed: 2026-11-25
created: 2026-11-25
---

# Agentforce in Slack

Agentforce in Slack is how an agent that lives in Salesforce shows up where employees already talk. The agent is designed, given subagents and actions, and activated in Salesforce; Slack is a connection added to that agent, after which admins install it into Slack and members find it under the Agents area or message it in channels.[^s1] Trailhead frames such an agent as a digital assistant that can understand, respond and act on its own initiative inside Slack.[^s4] It is a channel, not a separate agent builder: the reasoning, grounding and permissions all come from the Salesforce side.

## How it works

Only agents of the Agentforce Employee Agent type can be built for Slack, and Slack offers three starter templates: Customer Insights Agent, Employee Help Agent and Onboarding Agent.[^s1] Builders add a **General Slack Actions** subagent so the agent can work with Slack itself, for example creating a canvas (not available on Slack's free plan) or searching Slack.[^s1] The Trailhead project adds four standard actions from the asset library to a subagent: Create a Slack Canvas, Update a Slack Canvas, Search Slack and Send a Slack Direct Message.[^s2] Those actions fail in the Salesforce preview because they have to run inside Slack, so testing a canvas flow means testing in Slack.[^s2]

Setup runs in a fixed order:

1. **Connect the org.** Connect Salesforce and Slack, then map Slack members to Salesforce users, one at a time or by CSV, from workspace settings (Pro, Business+) or organization settings (Enterprise).[^s1]
2. **Enable OAuth (legacy builder only).** Install the Slack connected app from Connected Apps OAuth Usage in Setup; the newer Agentforce Builder does not need this step.[^s1][^s2]
3. **Add the connection.** In Agentforce Studio, open the agent, add a Slack connection, commit the version and activate it; a live agent must be deactivated before it is changed.[^s1][^s2]
4. **Install in Slack.** On Pro or Business+, install from Manage Agentforce; on Enterprise Grid, approve and install at the org level, then add the agent to chosen workspaces.[^s1][^s3]

Approving and installing needs Slack org or workspace owner/admin privileges together with the Salesforce admin system role.[^s3]

## Using an agent in Slack

Members reach agents in several places: an @mention in a channel, thread or DM; the Agentforce Hub, a directory of agents; and a sidebar tab that lists agents and past conversations.[^s4] An @mention in a channel opens a thread that any member of the channel can follow, which makes agent answers shared by default.[^s2] Slack also hosts third-party agents from its Marketplace (Trailhead names Adobe Express, Asana, Box and Workday), which admins govern alongside Agentforce agents.[^s4]

## Access, security and gotchas

- Employee agents get member access automatically from Salesforce permissions; Service Agents are blocked for everyone until an admin assigns access.[^s1]
- Slack members without a Salesforce account need a provisional Salesforce license before they can be mapped and use an agent.[^s1]
- In the Trailhead org, access is granted by enabling the agent in a permission set, and Slack honors those permissions by default.[^s2]
- Agents respect licenses, permissions, field-level security and sharing, and the Einstein Trust Layer protects every interaction.[^s2][^s4]
- Navigation labels differ between sources ("Tools" versus "Agents & tools"), so expect UI wording to drift between releases.[^s1][^s3]

Owners, admins, Agent Builders and assigned Agent Managers can edit an agent's Slack profile; Enterprise admins can remove an agent from individual workspaces or uninstall it org-wide, and the admin dashboard surfaces workspaces, member and agent permissions plus agent analytics.[^s1][^s3]

## When to use it

Choose Slack as the channel when the users are employees who already coordinate work in Slack and the agent's value is in conversation, search or canvases. Keep a customer-facing service agent on messaging or web channels; Slack is an internal surface, and service agents there stay locked until access is assigned.[^s1]

## Connections

- `broader` / `partOf` **kt:agentforce**: this is one deployment channel of the Agentforce platform.[^s1]
- `integratesWith` **kt:slack-platform**: the agent is installed into Slack workspaces and uses Slack canvases, search and DMs.[^s2]
- `configuredVia` **kt:agentforce-studio**: the Slack connection is added, committed and activated in the builder.[^s1]
- `related` **kt:agentforce-employee-agents**, **kt:agentforce-subagents**, **kt:agent-actions**: the agent type, the General Slack Actions subagent and the Slack actions it reasons over.[^s1][^s2]
- `dependsOn` **kt:salesforce-sharing-model**, **kt:einstein-trust-layer**, **kt:connected-apps**, and `related` **kt:permission-sets**: access and data security come from Salesforce controls, the Trust Layer and (in the legacy builder) the Slack connected app.[^s1][^s2][^s4]

## Sources

[^s1]: Slack Help Center, "Set up and manage Agentforce in Slack". https://slack.com/help/articles/36218109305875-Set-up-and-manage-Agentforce-in-Slack (accessed 2026-11-25)
[^s2]: Trailhead, "Configure a Slack Agent in Salesforce". https://trailhead.salesforce.com/content/learn/modules/agentforce-configuration-for-slack-deployment/configure-a-slack-agent-in-salesforce (accessed 2026-11-25)
[^s3]: Trailhead, "Deploy an Agent in Slack". https://trailhead.salesforce.com/content/learn/modules/agentforce-configuration-for-slack-deployment/deploy-an-agent-in-slack (accessed 2026-11-25)
[^s4]: Trailhead, "Integrate AI Agents with Slack for Productivity". https://trailhead.salesforce.com/content/learn/modules/slack-ai/integrate-ai-agents-with-slack (accessed 2026-11-25)
