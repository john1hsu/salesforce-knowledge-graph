---
id: kt:agent-development-lifecycle
type: Concept
title: Agent Development Lifecycle
aliases: [ADLC, Agentforce Development Lifecycle, Agentic Development Lifecycle]
domain: data-cloud-and-ai
summary: >-
  Salesforce's five-phase methodology for designing, building, testing, deploying and continuously tuning Agentforce
  agents, extending traditional application lifecycle management to cope with non-deterministic, natural-language
  driven agent behaviour.
release: "Winter '27"
status: current
broader: [kt:agentforce]
related: [kt:agentforce-testing-center, kt:agentforce-dx, kt:sandbox-types]
relations:
  - {predicate: partOf, object: kt:well-architected-framework}
  - {predicate: contrastsWith, object: kt:application-lifecycle-management}
  - {predicate: usedBy, object: kt:salesforce-architect}
sources:
  - id: s1
    title: "The Agent Development Lifecycle"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/agent-development-lifecycle
    type: official-docs
    accessed: 2026-10-30
  - id: s2
    title: "Trust Your Agents (Agentforce Agent Testing module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-agent-testing/trust-your-agents
    type: official-learning
    accessed: 2026-10-30
  - id: s3
    title: "Master the Agentic Development Lifecycle for Agentforce"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2026/06/master-the-agentic-development-lifecycle-for-agentforce
    type: official-blog
    accessed: 2026-10-30
  - id: s4
    title: "Exploring the Agentforce Development Lifecycle"
    publisher: Salesforce Blog
    url: https://www.salesforce.com/blog/exploring-the-agentforce-development-lifecycle/
    type: official-blog
    accessed: 2026-10-30
  - id: s5
    title: "The Agent Development Lifecycle"
    publisher: Salesforce
    url: https://www.salesforce.com/agentforce/agent-development-lifecycle/
    type: official-blog
    accessed: 2026-10-30
created: 2026-10-30
---

# Agent Development Lifecycle

The Agent Development Lifecycle (ADLC) is the methodology Salesforce recommends for taking an Agentforce agent from idea to production and keeping it healthy afterwards. It does not replace the familiar software development lifecycle. Instead it extends application lifecycle management for systems whose behaviour is non-deterministic. Because the same input can yield different outputs, the ADLC judges an agent by whether it reliably achieves its goal, not by whether it reproduces one exact answer.[^s1] Inputs are free-form natural language rather than precisely specified parameters. Data becomes a first-class design concern, and teams need skills that span data, ML and agent engineering as well as classic development.[^s1]

## The five phases

Salesforce Architects describe five phases.[^s1][^s4]

1. **Ideation and design.** Define the agent's purpose, persona, topics, tools, data sources, guardrails and escalation paths to humans, and collect a representative set of user utterances to design and test against.[^s1]
2. **Development (inner loop).** Build reasoning logic, prompts, actions and retrieval pipelines, and wire actions to secured Salesforce assets such as Flows, Apex and Prompt Builder templates. Teams can work in Agent Builder or pro-code with Agentforce DX.[^s1][^s4]
3. **Testing and validation.** Layer manual checks, automated batch tests, unit tests for the deterministic Apex and Flow logic underneath, adversarial tests and human review.[^s1]
4. **Deployment.** Treat the agent as metadata in source control, promote it with change sets, the Metadata API or Agentforce DX, and activate it explicitly as a separate step after deploying it.[^s1][^s4]
5. **Monitoring and tuning (outer loop).** Watch latency, token cost and error rates, analyse conversations for dead ends and escalations, and feed what you learn back into the next iteration.[^s1]

Salesforce's product-facing version of the lifecycle uses slightly different labels: design and build, test and evaluate, deploy and experiment, observe and monitor, and control and orchestrate. The last of these adds governance and multi-agent orchestration across vendors through MuleSoft Agent Fabric.[^s5] Salesforce also states that the whole lifecycle is now API- and CLI-first.[^s5]

## How it works in practice

Environments follow a clear split. Developers iterate in scratch orgs, test in sandboxes loaded with realistic data, and never run agent tests in production, because tests can modify CRM records.[^s1][^s2] Every change gets a new agent version that can be tested without touching the live one. The validated version is then published and activated, and teams roll back to the last known good version if a release misbehaves.[^s1]

In a pro-code workflow, the agent definition lives in an Agent Script authoring bundle (the `AiAuthoringBundle` metadata type). The Salesforce CLI generates, validates, previews, tests, publishes and activates it. Publishing creates an inactive runnable version, and activation is what makes it reachable by users.[^s3] Test specifications are written in YAML and run as batch regression suites. Production behaviour is investigated through session trace data stored in Data 360.[^s3][^s1]

## Limits and gotchas

- Agentforce Testing Center accepts up to 1,000 test cases per test and allows up to 10 test jobs at a time within a 10-hour window. Trailhead notes that the new Testing Center is in beta.[^s2][^s1]
- Test runs consume requests and credits just as live usage does, even in a sandbox.[^s2]
- Automated tests that use an LLM to judge expected outcomes are less deterministic than exact-match assertions. Salesforce notes that multi-turn and action-validation testing is still being enhanced, so automated validation does not replace human review.[^s3]
- Field-level security and object permissions for an agent's actions are easy to miss. Request or build an explicit permission set.[^s3]
- Deploying an agent does not activate it. Plan the activation step and connect monitoring from the moment a version goes live.[^s1]
- When coding agents help build Agentforce agents, keep them away from production orgs and keep secrets out of prompts.[^s3]

## When to use it

Use the ADLC for any agent destined for real users. It gives a shared vocabulary for when to test, how to promote and what to monitor. For pure deterministic automation, such as a record-triggered flow with no LLM reasoning, standard ALM and unit testing remain enough. The ADLC matters when the outcome depends on model reasoning over natural language.[^s1][^s2]

## Connections

The ADLC sits **under** `kt:agentforce`, the platform whose agents it governs.[^s5] It is **part of** the `kt:well-architected-framework`, the Architecture Center guidance that this fundamentals guide sits alongside. It **contrasts with** traditional `kt:application-lifecycle-management`, which it extends rather than replaces.[^s1] It is **related** to `kt:agentforce-testing-center` and `kt:agentforce-dx`, the main tools for its test and build phases, and to `kt:sandbox-types`, because environment choice drives where each phase runs.[^s1][^s2][^s3] It is **primarily used by** `kt:salesforce-architect`s planning agent delivery.[^s1]

## Sources

[^s1]: Salesforce Architects, "The Agent Development Lifecycle". https://architect.salesforce.com/fundamentals/agent-development-lifecycle (accessed 2026-10-30)
[^s2]: Trailhead, "Trust Your Agents". https://trailhead.salesforce.com/content/learn/modules/agentforce-agent-testing/trust-your-agents (accessed 2026-10-30)
[^s3]: Salesforce Developers Blog, "Master the Agentic Development Lifecycle for Agentforce". https://developer.salesforce.com/blogs/2026/06/master-the-agentic-development-lifecycle-for-agentforce (accessed 2026-10-30)
[^s4]: Salesforce Blog, "Exploring the Agentforce Development Lifecycle". https://www.salesforce.com/blog/exploring-the-agentforce-development-lifecycle/ (accessed 2026-10-30)
[^s5]: Salesforce, "The Agent Development Lifecycle". https://www.salesforce.com/agentforce/agent-development-lifecycle/ (accessed 2026-10-30)
