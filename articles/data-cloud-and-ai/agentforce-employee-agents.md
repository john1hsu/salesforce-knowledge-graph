---
id: kt:agentforce-employee-agents
type: Feature
title: Agentforce Employee Agents
aliases: [Agentforce Employee Agent, employee agent, employee-facing agents, Agentforce for Employees, internal agents]
domain: data-cloud-and-ai
summary: >-
  Internal Agentforce agents built from the Agentforce Employee Agent template that help Salesforce users in the flow
  of work (in Lightning Experience, the mobile app and Slack), running as the logged-in user so every action respects
  that user's licenses, permissions and sharing; usage is billed in Flex Credits.
release: "Winter '27"
status: current
broader: [kt:agentforce]
related: [kt:agentforce-subagents, kt:agent-actions, kt:slack-platform, kt:knowledge-base, kt:salesforce-mobile-app, kt:agentforce-in-slack]
relations:
  - {predicate: partOf, object: kt:agentforce}
  - {predicate: configuredVia, object: kt:agentforce-studio}
  - {predicate: dependsOn, object: kt:salesforce-sharing-model}
  - {predicate: dependsOn, object: kt:einstein-trust-layer}
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: integratesWith, object: kt:slack-platform}
sources:
  - id: s1
    title: "Get Started with Agentforce for Employees (Agentforce for Employees: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-for-employees-quick-look/get-started-with-agentforce-for-employees
    type: official-learning
    accessed: 2026-11-23
  - id: s2
    title: "Employee Agents and Foundations: The Admin Advantage for User Support"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2025/employee-agents-foundations-the-admin-advantage-for-user-support
    type: official-blog
    accessed: 2026-11-23
  - id: s3
    title: "Create an Employee Agent (Quick Start: Create Employee Agents in Agentforce)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/quick-start-create-employee-agents-in-agentforce/create-two-employee-agents
    type: official-learning
    accessed: 2026-11-23
  - id: s4
    title: "Exercise 1: Get Started with the Employee Agent (Agentforce Workshop)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/workshops/agentforce-new-workshop/employee-agents/1-get-started
    type: official-learning
    accessed: 2026-11-23
  - id: s5
    title: "Agentforce Implementation Guide: Employee-Facing Agents"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/agentforce_implementation_employee.pdf
    type: official-docs
    accessed: 2026-11-23
  - id: s6
    title: "Configure a Slack Agent in Salesforce (Agentforce Configuration for Slack Deployment)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-configuration-for-slack-deployment/configure-a-slack-agent-in-salesforce
    type: official-learning
    accessed: 2026-11-23
created: 2026-11-23
---

# Agentforce Employee Agents

**Agentforce employee agents** are the internal-facing kind of Agentforce agent: conversational AI assistants for a
company's own Salesforce users rather than for its customers. Trailhead frames them as role-based peers that take on
routine and complex internal work such as summarizing an account, drafting a sales email, answering a benefits
question or handling an IT request, with example agents for HR, IT, sales, service, marketing, legal, engineering and
supply chain teams.[^s1] The Salesforce Admins blog describes them as dedicated AI assistants for internal users that
work through natural-language chat inside the user's existing workflow.[^s2]

## How they differ from customer-facing agents

Out-of-the-box agents such as Agentforce Service Agent or the sales development agents target a fixed use case,
whereas employee agents are customized to internal needs, and an org can run several, each dedicated to a job,
function or process.[^s1][^s2] The developer workshop contrasts its employee agent with a customer-facing service
agent: the internal agent is read-heavy, and the Employee Agent template does not ask for a role or company the way
the customer-facing template does.[^s4]

The defining difference is identity. An employee agent runs in the context of the currently logged-in user, not as a
shared agent user, so its actions are limited by that person's licenses and permissions.[^s5] Trailhead stresses the
consequence: a manager and a direct report asking the same agent see only what their own access allows, because the
agent follows the same permissions and org security settings as the person it helps.[^s1] Field-level security and
sharing settings carry over when the agent is used from Slack as well.[^s6]

## Where users reach them

Inside Salesforce, users open the Agentforce icon in an app and switch between the agents they have access to; the
same agents can be summoned in Slack channels or direct messages with an @mention, and used on mobile.[^s1] The
implementation guide's worked example deploys one agent to the Salesforce desktop app, the Salesforce mobile app and
Slack.[^s5] According to Trailhead, Salesforce identity licenses let even non-CRM users work with Agentforce in
Slack without an extra Salesforce license.[^s1]

## Building one

Admins create an employee agent in Agentforce Studio (Agentforce Builder): New Agent, then the **Agentforce Employee
Agent** template, a name and developer name, and Let's Go.[^s3][^s4] The template ships with an Agent Router that has
three system subagents (General FAQ, Off Topic and Ambiguous Question); General FAQ carries the standard action that
answers questions from Knowledge articles using retrieval-augmented search.[^s4] Admins then set the description,
agent-level instructions, welcome and error messages, and add subagents and actions from the asset library, such as a
General CRM subagent with a Summarize Record action.[^s3][^s4] The quick-start project removes General FAQ in its
practice org because that subagent relies on Data 360, which the org lacks.[^s3]

Before go-live the agent is tried in Preview, which offers a simulated mode with mock data and a live test against
real records; it is then saved, its version committed and activated.[^s3] A live agent must be deactivated before it
can be changed, and once active it is available wherever it has been shared.[^s6] Users get access through a
permission set whose Agent Access setting lists the enabled agents.[^s6] Slack deployment adds the Slack connection
and optional Slack actions such as searching Slack, sending a direct message or creating and updating a canvas.[^s6]

## Requirements, cost and gotchas

- **Prerequisites**: Lightning Experience, Einstein generative AI and Data Cloud (Data 360) must be enabled.[^s5]
- **Admin permission**: Manage AI Agents plus the agent type's permissions, or Customize Application.[^s5]
- **Billing**: employee agent actions consume Flex Credits, which replaced the older per-conversation model.[^s2]
- **Foundations**: the Admins blog says Salesforce Foundations brings employee agents to Enterprise Edition and above Sales or Service orgs, with Flex Credits provisioned as an entitlement and usage tracked in Digital Wallet.[^s2]
- **Trust**: requests pass through the Einstein Trust Layer, whose zero-data-retention terms mean the LLM provider does not keep prompts or responses.[^s1]
- **Least privilege still matters**: because the agent inherits the user's access, over-broad permission sets give the agent the same reach; Trailhead notes that each user's role decides which actions are unlocked.[^s1]

## Connections

An employee agent is **part of** and narrower than `kt:agentforce`, and is **configured via** `kt:agentforce-studio`.
[^s3] Its behavior is organized into `kt:agentforce-subagents` that invoke `kt:agent-actions`, with the default FAQ
subagent grounded in `kt:knowledge-base`.[^s4] It **depends on** `kt:salesforce-sharing-model` because it acts as the
logged-in user, on `kt:einstein-trust-layer` for its guardrails, and on `kt:data-cloud` as a setup prerequisite.
[^s1][^s5] It **integrates with** `kt:slack-platform` and is also surfaced in `kt:salesforce-mobile-app`.[^s5][^s6]

## Sources

[^s1]: Trailhead, "Get Started with Agentforce for Employees". https://trailhead.salesforce.com/content/learn/modules/agentforce-for-employees-quick-look/get-started-with-agentforce-for-employees (accessed 2026-11-23)
[^s2]: Salesforce Admins, "Employee Agents and Foundations: The Admin Advantage for User Support". https://admin.salesforce.com/blog/2025/employee-agents-foundations-the-admin-advantage-for-user-support (accessed 2026-11-23)
[^s3]: Trailhead, "Create an Employee Agent". https://trailhead.salesforce.com/content/learn/projects/quick-start-create-employee-agents-in-agentforce/create-two-employee-agents (accessed 2026-11-23)
[^s4]: Salesforce Developers, "Exercise 1: Get Started with the Employee Agent". https://developer.salesforce.com/workshops/agentforce-new-workshop/employee-agents/1-get-started (accessed 2026-11-23)
[^s5]: Salesforce, "Agentforce Implementation Guide: Employee-Facing Agents". https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/agentforce_implementation_employee.pdf (accessed 2026-11-23)
[^s6]: Trailhead, "Configure a Slack Agent in Salesforce". https://trailhead.salesforce.com/content/learn/modules/agentforce-configuration-for-slack-deployment/configure-a-slack-agent-in-salesforce (accessed 2026-11-23)
