---
id: kt:agentforce-specialist-certification
type: Certification
title: Agentforce Specialist Certification
aliases: [Salesforce Certified Agentforce Specialist, AI Specialist Certification, Salesforce Certified AI Specialist, Agentforce Specialist exam, AI-201]
domain: data-cloud-and-ai
summary: >-
  Salesforce's credential for people who build, ground, test and deploy agents with Agentforce, covering agent
  design, prompt engineering, Data 360 grounding, the deployment lifecycle and multi-agent interoperability.
  It replaced the Salesforce AI Specialist credential in March 2025.
release: "Winter '27"
status: current
broader: [kt:salesforce-certification-program]
related: [kt:agentforce, kt:prompt-builder, kt:agentforce-data-library, kt:agentforce-testing-center, kt:model-context-protocol-in-agentforce, kt:platform-administrator-certification]
sources:
  - id: s1
    title: "Salesforce Certified Agentforce Specialist (credential page)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/aispecialist
    type: official-learning
    accessed: 2026-11-13
  - id: s2
    title: "Get Started with Salesforce Agentforce Specialist Certification Prep"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cert-prep-agentforce-specialist/get-started-with-salesforce-agentforce-specialist-certification-prep
    type: official-learning
    accessed: 2026-11-13
  - id: s3
    title: "Get Started with Salesforce AI Specialist Certification Prep"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/ko/content/learn/modules/cert-prep-ai-specialist/get-started-with-salesforce-ai-specialist-certification-prep
    type: official-learning
    accessed: 2026-11-13
  - id: s4
    title: "Prepare for the Agentforce Specialist Exam"
    publisher: Salesforce Admins blog
    url: https://admin.salesforce.com/blog/2024/prepare-for-the-salesforce-ai-specialist-exam-and-agentforce
    type: official-blog
    accessed: 2026-11-13
  - id: s5
    title: "Salesforce AI certification"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/ai-certification/
    type: official-blog
    accessed: 2026-11-13
  - id: s6
    title: "Salesforce Changes AI Specialist Exam to Certified Agentforce Specialist"
    publisher: Salesforce Ben
    url: https://www.salesforceben.com/salesforce-changes-ai-specialist-exam-to-certified-agentforce-specialist/
    type: news
    accessed: 2026-11-13
created: 2026-11-13
---

# Agentforce Specialist Certification

The **Salesforce Certified Agentforce Specialist** is the credential for people who manage and optimize Agentforce in their organization, combining Salesforce platform configuration skills with knowledge of what Agentforce agents can do.[^s1] It is the successor to the Salesforce AI Specialist credential: the Trailhead credential page still lives at the old `aispecialist` address but now shows the Agentforce Specialist name, and its exam link carries the code AI-201.[^s1] The exam is aimed at builders rather than end users, so expect scenario questions about designing, grounding, testing and shipping agents.[^s2][^s5]

## From AI Specialist to Agentforce Specialist

The AI Specialist exam centred on generative AI features inside the CRM. Its outline weighted Prompt Builder at 37%, Agentforce tools at 23%, generative AI in CRM applications at 17%, the Einstein Trust Layer at 15% and Model Builder at 8%.[^s3] Salesforce renamed it the Certified Agentforce Specialist with registration opening on March 3, 2025, and converted existing AI Specialist holders to the new credential without a new exam.[^s6] The first Agentforce-era outline shifted weight to agents: prompt engineering 30%, Agentforce concepts 30%, Agentforce and Data Cloud 20%, and Agentforce with Service Cloud and with Sales Cloud at 10% each.[^s4][^s6]

## Exam format and current outline

The current prep module lists 60 multiple-choice questions plus up to five unscored ones, a 73% passing score, immediate results, delivery online or at a test centre, no reference materials, and a $100 retake fee.[^s2] Salesforce's AI certification page gives the time limit as 90 minutes.[^s5] The module's fee note still describes the AI for All offer of a free first attempt through the end of 2025, so confirm the current registration fee when you book.[^s2]

The outline has since been reorganized again, into five sections:[^s2]

| Section | Weight[^s2] |
|---|---|
| AI Agents | 35% |
| Prompt Engineering | 20% |
| Data Cloud for Agentforce | 20% |
| Deployment Lifecycle | 20% |
| Multi-Agent Interoperability | 5% |

Two changes stand out against the 2025 outline. The cloud-specific Sales and Service sections are gone, replaced by a deployment lifecycle section, and multi-agent interoperability is new.[^s2][^s6] The prep module notes that Data Cloud is now called Data 360, with exam content unchanged by the rename.[^s2]

## Who it is for

Trailhead recommends at least six months of hands-on experience developing, testing and deploying Agentforce agents, plus experience with prompt engineering in Prompt Builder, grounding techniques, and configuring Agentforce Data Libraries.[^s2] There is no prerequisite, though the Platform Administrator and Platform App Builder credentials are recommended.[^s1][^s2] Salesforce's admin evangelists call admins a key audience, because they already know the platform, the business processes and what users need.[^s4]

## Maintenance and gotchas

- **Annual maintenance.** Holders must complete the release maintenance module for the credential once a year, or it expires.[^s2]
- **Old prep material.** Guides written for the AI Specialist exam overweight Prompt Builder and Model Builder compared with today's agent-first outline.[^s3][^s2]
- **Several outlines in circulation.** Blog and course outlines from early 2025 still list Sales and Service sections; use the current prep module or exam guide.[^s2][^s4]
- **Data 360 naming.** Questions and study material may say Data Cloud or Data 360; they are the same product.[^s2]

## Connections

- **broader → `kt:salesforce-certification-program`**: one credential in Salesforce's catalogue, listed with the admin and app builder credentials.[^s1]
- **related → `kt:agentforce`**: the platform the exam validates; AI agents are its largest section.[^s2]
- **related → `kt:prompt-builder`**: prompt templates, grounding and Prompt Builder use cases make up the prompt engineering section.[^s5][^s2]
- **related → `kt:agentforce-data-library`**: configuring data libraries is recommended experience and part of the Data Cloud for Agentforce section.[^s2][^s5]
- **related → `kt:agentforce-testing-center`**: testing agents before deployment sits in the lifecycle content.[^s4][^s5]
- **related → `kt:model-context-protocol-in-agentforce`**: the new multi-agent interoperability section covers how agents connect to other agents and external systems.[^s2]
- **related → `kt:platform-administrator-certification`**: the recommended starting credential.[^s1]

## Sources
[^s1]: Trailhead, "Salesforce Certified Agentforce Specialist". https://trailhead.salesforce.com/credentials/aispecialist (accessed 2026-11-13)
[^s2]: Trailhead, "Get Started with Salesforce Agentforce Specialist Certification Prep". https://trailhead.salesforce.com/content/learn/modules/cert-prep-agentforce-specialist/get-started-with-salesforce-agentforce-specialist-certification-prep (accessed 2026-11-13)
[^s3]: Trailhead, "Get Started with Salesforce AI Specialist Certification Prep". https://trailhead.salesforce.com/ko/content/learn/modules/cert-prep-ai-specialist/get-started-with-salesforce-ai-specialist-certification-prep (accessed 2026-11-13)
[^s4]: Salesforce Admins blog, "Prepare for the Agentforce Specialist Exam". https://admin.salesforce.com/blog/2024/prepare-for-the-salesforce-ai-specialist-exam-and-agentforce (accessed 2026-11-13)
[^s5]: Salesforce, "Salesforce AI certification". https://www.salesforce.com/blog/ai-certification/ (accessed 2026-11-13)
[^s6]: Salesforce Ben, "Salesforce Changes AI Specialist Exam to Certified Agentforce Specialist". https://www.salesforceben.com/salesforce-changes-ai-specialist-exam-to-certified-agentforce-specialist/ (accessed 2026-11-13)
