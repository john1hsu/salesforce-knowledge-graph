---
id: kt:agentforce-observability
type: Feature
title: Agentforce Observability
aliases: [Agent Monitoring, Agentforce Monitoring, Agent Analytics and Monitoring, Observe & Optimize]
domain: data-cloud-and-ai
summary: >-
  The set of Agentforce tools for watching deployed AI agents in production: Agent Analytics dashboards,
  Agentforce Session Tracing, Agent Optimization (intent clustering and quality scoring) and Agent Health
  Monitoring alerts, all built on session telemetry stored in a Data 360 data model.
release: "Winter '27"
status: current
broader: [kt:agentforce]
related: [kt:agentforce-studio, kt:agent-development-lifecycle, kt:agentforce-testing-center, kt:agentforce-subagents]
relations:
  - {predicate: partOf, object: kt:agentforce-studio}
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: integratesWith, object: kt:generative-ai-audit-and-feedback-data}
  - {predicate: integratesWith, object: kt:einstein-trust-layer}
  - {predicate: integratesWith, object: kt:digital-wallet}
sources:
  - id: s1
    title: "Get Started with Agent Monitoring (Agent Analytics and Monitoring)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agent-analytics-and-monitoring/get-started-with-agent-monitoring
    type: official-learning
    accessed: 2026-11-20
  - id: s2
    title: "Monitor Agent Health (Agent Analytics and Monitoring)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agent-analytics-and-monitoring/monitor-agent-health
    type: official-learning
    accessed: 2026-11-20
  - id: s3
    title: "Your Agents Are Getting More Capable. Is Your Observability Tooling Keeping Up?"
    publisher: Salesforce Blog
    url: https://www.salesforce.com/blog/agentforce-observability/?bc=OTH
    type: official-blog
    accessed: 2026-11-20
  - id: s4
    title: "Salesforce Deepens Observability in Agentforce 360"
    publisher: Salesforce Newsroom
    url: https://salesforce.com/news/stories/agentforce-studio-observability-tools-announcement
    type: news
    accessed: 2026-11-20
  - id: s5
    title: "Agentforce Observability"
    publisher: Salesforce
    url: https://www.salesforce.com/agentforce/observability/
    type: official-blog
    accessed: 2026-11-20
created: 2026-11-20
---

# Agentforce Observability

Agentforce Observability is the production-monitoring layer of Agentforce: the tools teams use after an agent goes live to see what it did, how well it did it, and when it starts to misbehave. Salesforce groups it into three areas, analytics, optimization and health monitoring, surfaced inside Agentforce Studio.[^s4] Trailhead teaches the same capabilities under the name agent monitoring, and places it in the Monitor phase of the agent development lifecycle, after build and test.[^s1] Salesforce markets it as one place to supervise every deployed agent, for IT teams watching performance and service leaders watching adoption and business impact.[^s5]

## How it works

Everything starts with telemetry. The **Session Tracing Data Model (STDM)** logs each session down to a single conversation turn: user input, planner decisions, prompt and action flows, gateway inputs and outputs, errors and the final output.[^s3] Sessions, interactions and steps are stored in Data 360, where they feed analytics and alerts directly.[^s4][^s3] Trailhead names three data sources that are aggregated into that unified Data 360 model: session tracing, audit and feedback data such as knowledge-retrieval scores, and Einstein Trust Layer scores such as toxicity and instruction adherence.[^s1]

Collection is not automatic. An admin turns on Agentforce Session Tracing, Audit and Feedback, and Knowledge/RAG Quality Data and Metrics, then installs the analytics apps for each agent type.[^s1]

## Components

- **Agent Analytics.** Dashboards for latency, usage patterns, quality scores and success rates across sessions.[^s1]
- **Sessions & Intents / Agent Optimization.** An LLM clusters similar user goals into intents so teams can find off-topic answers or actions that failed to run.[^s1][^s4]
- **Session tracing.** A step-by-step replay of one conversation's inputs, decisions, actions and outputs, explaining why the agent behaved as it did.[^s1]
- **Agent Health Monitoring.** Near-real-time health metrics and alerts on errors, latency spikes and escalations.[^s4]

Trailhead lists the metric families teams track: effectiveness (for example case deflection), usage, quality, health, trust, user satisfaction (thumbs up or down, Employee Agent only) and voice metrics such as interruption rate.[^s1] The July 2026 update made outcome metrics such as deflection and abandonment LLM evaluations of the whole session, with editable prompts, and let teams define custom LLM-as-judge scores for things like tone or competitor mentions.[^s3] It also added waterfall traces that follow delegation across multi-agent workflows and a rebuilt dashboard sliceable by subagent, action and intent.[^s3]

## Health alerts

Alerts live in Agentforce Studio under **Observe & Optimize**. Each alert ties a standard metric (such as error rate or interaction duration) or a custom score to one agent, a condition (at or above, or at or below) and a threshold value; notifications go out by email or in-app.[^s2] Trailhead recommends reviewing at least 30 days of history, setting the threshold where normal variation ends, starting with a few high-value alerts, and giving every alert an owner and a response playbook.[^s2] Its worked example picks a 5-second latency threshold because normal interactions ran 1.8 to 4.6 seconds.[^s2]

## Limits and gotchas

- **Data 360 underneath.** The telemetry lands in Data 360, so observability depends on that platform being provisioned.[^s4][^s1]
- **Cost model.** Salesforce says core observability is free and unmetered for every Agentforce customer: tracing ingestion, metric aggregation and out-of-the-box dashboard queries.[^s3]
- **What is still metered.** Building new dashboards, ingesting external sources and creating new semantic data-model objects still consume credits; editing the shipped dashboards does not.[^s3]
- **Timeline caution.** Salesforce's November 2025 announcement put Health Monitoring GA in Spring 2026 and carried a forward-looking disclaimer, so confirm feature availability in your org.[^s4]

## When to use it (and when not)

Use observability once an agent handles real traffic: Testing Center and Studio previews validate behavior before launch, while observability shows how the agent performs against live users and drifts over time.[^s1][^s2] Trailhead advises investigating sessions and conversations before changing prompt templates, subagents or actions, and re-testing a fix in Testing Center before redeploying.[^s2] For raw prompt and response records for compliance review, the audit and feedback data is the underlying store; observability is the analysis layer on top of it.[^s1]

## Connections

Agentforce Observability is a capability of `kt:agentforce` and is **part of** `kt:agentforce-studio`, where the Observe & Optimize area lives.[^s4][^s2] It **depends on** `kt:data-cloud` (Data 360) for its session data model.[^s4] It **integrates with** `kt:generative-ai-audit-and-feedback-data` and `kt:einstein-trust-layer`, which supply quality and trust scores.[^s1] Usage appears in `kt:digital-wallet`, though core observability no longer draws down flex credits.[^s3] It closes the loop of the `kt:agent-development-lifecycle`, feeding fixes back to `kt:agentforce-testing-center`, and its traces follow work across `kt:agentforce-subagents`.[^s1][^s2][^s3]

## Sources
[^s1]: Trailhead, "Get Started with Agent Monitoring". https://trailhead.salesforce.com/content/learn/modules/agent-analytics-and-monitoring/get-started-with-agent-monitoring (accessed 2026-11-20)
[^s2]: Trailhead, "Monitor Agent Health". https://trailhead.salesforce.com/content/learn/modules/agent-analytics-and-monitoring/monitor-agent-health (accessed 2026-11-20)
[^s3]: Salesforce Blog, "Your Agents Are Getting More Capable. Is Your Observability Tooling Keeping Up?" (July 21, 2026). https://www.salesforce.com/blog/agentforce-observability/?bc=OTH (accessed 2026-11-20)
[^s4]: Salesforce Newsroom, "Salesforce Deepens Observability in Agentforce 360" (November 20, 2025). https://salesforce.com/news/stories/agentforce-studio-observability-tools-announcement (accessed 2026-11-20)
[^s5]: Salesforce, "Agentforce Observability". https://www.salesforce.com/agentforce/observability/ (accessed 2026-11-20)
