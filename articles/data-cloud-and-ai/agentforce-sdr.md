---
id: kt:agentforce-sdr
type: Feature
title: Agentforce SDR
aliases: [Agentforce Sales Development Representative, Agentforce Sales Development, Agentforce Sales Development Rep, Agentforce Lead Nurturing, SDR Agent, "SDR Agent | Inbound Nurturing", Sales Agent for Lead Nurturing]
domain: data-cloud-and-ai
summary: >-
  A prebuilt, autonomous Agentforce for Sales agent that nurtures inbound leads by email: it sends personalized
  outreach and nudges, answers prospect questions from grounded company data, books meetings for the lead owner and
  hands interested leads back to human sellers.
release: "Winter '27"
status: current
broader: [kt:agentforce, kt:sales-cloud]
related: [kt:prompt-builder, kt:agentforce-data-library, kt:agentforce-testing-center, kt:agent-actions, kt:lead-conversion]
relations:
  - {predicate: partOf, object: kt:agentforce}
  - {predicate: configuredVia, object: kt:salesforce-go}
  - {predicate: configuredVia, object: kt:agentforce-studio}
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: dependsOn, object: kt:einstein-activity-capture}
  - {predicate: dependsOn, object: kt:retrieval-augmented-generation-in-salesforce}
sources:
  - id: s1
    title: "Get to Know Agentforce SDR (Agentforce SDR Setup and Customization)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-sdr-setup-and-customization/get-to-know-agentforce-sdr
    type: official-learning
    accessed: 2026-11-23
  - id: s2
    title: "Customize Agentforce SDR (Agentforce SDR Setup and Customization)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-sdr-setup-and-customization/customize-agentforce-sdr
    type: official-learning
    accessed: 2026-11-23
  - id: s3
    title: "Set Up Agentforce SDR (Build an Agent to Nurture Leads)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/build-an-agent-to-nurture-leads/set-up-agentforce-sdr
    type: official-learning
    accessed: 2026-11-23
  - id: s4
    title: "Configure and Activate Your Agentforce SDR Agent (Build an Agent to Nurture Leads)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/build-an-agent-to-nurture-leads/configure-and-activate-your-agentforce-sdr-agent
    type: official-learning
    accessed: 2026-11-23
  - id: s5
    title: "Discover Agentforce for Sales (Agentforce for Sales: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-sales-agents-quick-look/discover-agentforce-sales-agents
    type: official-learning
    accessed: 2026-11-23
  - id: s6
    title: "Agentforce for Sales Development Implementation Guide"
    publisher: Salesforce
    url: https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/guides/Agentforce-for-Sales-Development-Implementation-Guide.pdf
    type: official-docs
    accessed: 2026-11-23
created: 2026-11-23
---

# Agentforce SDR

**Agentforce SDR** (Sales Development Representative) is the prebuilt top-of-funnel agent in Agentforce for Sales.
Trailhead describes it as a first point of contact for inbound leads that does personalized outreach, answers
customer questions and books meetings on a seller's behalf.[^s3] Its main goal is nurturing leads, and Salesforce
positions it for companies with high-volume lead generation, where it makes sure every lead gets attention before
passing it to a sales rep.[^s5] Agentforce for Sales ships it next to Sales Coach, which instead gives deal-specific
feedback and role-play to sellers.[^s3][^s5]

The product carries several names. Trailhead uses "Agentforce SDR" and "Agentforce Lead Nurturing", Salesforce Go
shows the toggle as "SDR Agent | Inbound Nurturing", the agent type in the builder is "Agentforce Sales Development
Rep", and the implementation guide notes the name was updated to "Sales Development".[^s1][^s3][^s4][^s6]

## How it works

The agent runs as its own Salesforce user and works by email against Lead, Contact or Person Account records.[^s1][^s6]
It is grounded in the company's sales, product and customer data.[^s5] Three standard subagents (topics) hold its
actions:[^s4][^s6]

- **Send Outreach**: draft an initial outreach email, draft a nudge email, and schedule the email.[^s6]
- **Respond to Prospect**: draft a generic reply, a meeting-request reply, or an answer to a lead's question.[^s6]
- **Manage Opt-Out**: a flow action that marks the lead as opted out, using Email Opt Out by default.[^s6]

The implementation guide's instructions require the agent to draft before it schedules each email.[^s6] Outreach
starts either when a user activates the agent on a record or when the record meets the agent's Engagement Rules; the
guide lists a one-hour send delay, and emails due outside the configured working hours wait for the next
window.[^s6] If the lead stays silent, nudges follow, bounded by the time between attempts and a maximum number of
replies.[^s6] A request to meet produces a booking link (when Salesforce Inbox is on) and copies the lead owner; a
"not now" or off-topic reply gets a generic answer with the owner copied; "not interested" opts the lead out so no
more email is sent.[^s6] Product questions are answered by retrieval over files in the agent's data
library.[^s2][^s6]

The email wording comes from five out-of-the-box Prompt Builder templates covering the intro email, follow-up,
fallback reply, meeting reply and product Q&A reply.[^s2]

## Setup

Setup starts in Salesforce Go: turn on Agentforce for Sales, then toggle on the SDR agent.[^s1][^s3] Trailhead's
overview lists six steps: turn on Agentforce, enable the engagement agent, assign user access, set up the agent
user, configure a Data 360 data library, and build, test and activate the agent.[^s1] In the builder, the agent type
is preselected with its three subagents; the admin fills in a role, a company description for grounding, the agent
user and enhanced event logging, then creates and activates the agent.[^s4]

The implementation guide adds the operational pieces. The agent needs a dedicated company-domain mailbox, and the
connected email account must be the same address as on the agent's user record.[^s6] Engagement Rules set the number
of attempts, time between attempts, maximum replies and the outreach schedule, while entity assignments choose Lead,
Contact or Person Account.[^s6] Data library uploads accept text or HTML files up to 4 MB and PDFs up to 100
MB.[^s6] Permission sets split by persona: the agent user gets the Agentforce SDR Agent set, admins and managers get
Configure Agentforce SDR Agent plus Data Cloud access, and sellers can get Use Agentforce SDR Agent.[^s6]

## Limits and gotchas

- **Prerequisites are strict**: Einstein Activity Capture, Salesforce Inbox for meeting links, and Data Cloud for RAG.[^s6]
- **Testing does not send mail**: the builder's test environment can't schedule or send emails to leads.[^s4]
- **Test utterances matter**: use the guide's static "do not schedule" prompts, or expect scheduling errors.[^s6]
- **Disclosure**: a sign-off disclosure is added to the agent's emails but does not show in the Activity Timeline.[^s6]
- **Threading**: replies use a "Re:" subject but can appear as separate emails in the lead's inbox.[^s6]

When customizing prompts, Trailhead recommends absolute wording such as "must" and "never" for guardrails, and
default values for merge fields that might be null.[^s2] It rates engagement rules and data library uploads as
low-effort changes, and prompt template edits as medium-to-high effort.[^s2]

## When to use it

Use Agentforce SDR when inbound lead volume exceeds what human SDRs can follow up on and email is the main
channel.[^s5] It covers the first touches only; qualified interest is handed to the lead owner, who then works the
lead toward conversion.[^s5][^s6] For a custom internal assistant, build an employee agent instead; for coaching
sellers, use Sales Coach.[^s3][^s5]

## Connections

Agentforce SDR is part of `kt:agentforce` and sits in `kt:sales-cloud`'s lead funnel ahead of
`kt:lead-conversion`.[^s5] It is switched on through `kt:salesforce-go` and configured in the Agentforce builder
(`kt:agentforce-studio`), where its subagents bundle `kt:agent-actions`.[^s3][^s4] Its emails are shaped by
`kt:prompt-builder` templates, its answers are grounded through `kt:agentforce-data-library` retrieval on
`kt:data-cloud` (`kt:retrieval-augmented-generation-in-salesforce`), and it depends on
`kt:einstein-activity-capture` to send and log email.[^s1][^s2][^s6] Batch tests run in
`kt:agentforce-testing-center`.[^s6]

## Sources

[^s1]: Trailhead, "Get to Know Agentforce SDR". https://trailhead.salesforce.com/content/learn/modules/agentforce-sdr-setup-and-customization/get-to-know-agentforce-sdr (accessed 2026-11-23)
[^s2]: Trailhead, "Customize Agentforce SDR". https://trailhead.salesforce.com/content/learn/modules/agentforce-sdr-setup-and-customization/customize-agentforce-sdr (accessed 2026-11-23)
[^s3]: Trailhead, "Set Up Agentforce SDR". https://trailhead.salesforce.com/content/learn/projects/build-an-agent-to-nurture-leads/set-up-agentforce-sdr (accessed 2026-11-23)
[^s4]: Trailhead, "Configure and Activate Your Agentforce SDR Agent". https://trailhead.salesforce.com/content/learn/projects/build-an-agent-to-nurture-leads/configure-and-activate-your-agentforce-sdr-agent (accessed 2026-11-23)
[^s5]: Trailhead, "Discover Agentforce for Sales". https://trailhead.salesforce.com/content/learn/modules/agentforce-sales-agents-quick-look/discover-agentforce-sales-agents (accessed 2026-11-23)
[^s6]: Salesforce, "Agentforce for Sales Development Implementation Guide". https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/guides/Agentforce-for-Sales-Development-Implementation-Guide.pdf (accessed 2026-11-23)
