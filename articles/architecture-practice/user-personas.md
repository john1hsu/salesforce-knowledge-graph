---
id: kt:user-personas
type: Concept
title: User Personas
aliases: [personas, UX personas, Salesforce personas, persona mapping, proto-persona]
domain: architecture-practice
summary: >-
  Research-based archetypes that cluster a solution's users by shared goals, behaviours and pain points; in Salesforce
  projects they are mapped to real user groups and used to frame user stories, prioritise scope and target training
  and testing.
release: "Winter '27"
status: concept
broader: [kt:requirements-gathering]
related: [kt:user-stories, kt:stakeholder-mapping, kt:change-management-and-adoption, kt:user-acceptance-testing, kt:licensing-strategy]
relations:
  - {predicate: usedBy, object: kt:business-analyst}
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: enables, object: kt:user-stories}
sources:
  - id: s1
    title: "Get Started with Personas (UX Personas for Salesforce)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/modules/ux-personas-for-salesforce/units/get_started_with_personas
    type: official-learning
    accessed: 2026-11-26
  - id: s2
    title: "Work with Personas (UX Personas for Salesforce)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/ux-personas-for-salesforce/work_with_personas
    type: official-learning
    accessed: 2026-11-26
  - id: s3
    title: "Personas: learn how to discover your audience, understand them, and pivot to address their needs"
    publisher: Digital.gov (GSA)
    url: https://digital.gov/2023/05/19/personas-learn-how-to-discover-your-audience-understand-them-and-pivot-to-address-their-needs
    type: government
    accessed: 2026-11-26
  - id: s4
    title: "Personas Make Users Memorable"
    publisher: Nielsen Norman Group
    url: https://www.nngroup.com/articles/persona/
    type: partner
    accessed: 2026-11-26
  - id: s5
    title: "Get Started with Salesforce Business Analyst Certification Prep"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-business-analyst-certification-prep/get-started-with-salesforce-business-analyst-certification-prep
    type: official-learning
    accessed: 2026-11-26
created: 2026-11-26
---

# User Personas

A **user persona** is an archetype that stands for a group of users who share behaviour, motivations, goals or pain points. It is a synthesis of many people, not a portrait of one, which is why Trailhead calls personas character sketches rather than individuals.[^s1] Nielsen Norman Group describes a persona as a fictional but realistic description of a typical or target user, and insists it must rest on research about real people even though the persona itself is invented.[^s4] US federal guidance makes the same point: a persona is not a real person but represents the needs and attributes of real ones, and it should be grounded in research.[^s3]

In a Salesforce implementation, personas sit between discovery and design. They give the business analyst, architect and delivery team a shared vocabulary for "who is this for", and they make user stories, scope decisions and training plans traceable to real user groups rather than to whoever spoke loudest in a workshop.[^s2][^s4]

## Salesforce's own persona set

Salesforce publishes research-based personas for Sales, Service, Marketing and Experience Cloud users, built through observation, interviews, surveys and analysis.[^s1] Two design choices make them unusual:

- **Task-based, not CRM-based.** They describe the general work people do in their roles, because orgs often perform the same task with different features or outside systems.[^s1]
- **Deliberately abstract.** They carry no name, photo or demographics, so they transfer between companies and avoid stereotypes and unconscious bias.[^s1]

Trailhead counts more than a dozen of these personas across sales, service and marketing; Sales Cloud examples include the Deal Closer, Pipeline Builder and Trusted Advisor.[^s2] Teams can adopt them as a baseline and refine them with their own data, rather than starting from a blank page.[^s2]

## How to build and map personas

1. **Start from what the organisation already knows.** Subject matter experts, call-centre staff, past surveys, analytics and event data can be combined into a proto-persona: a set of assumptions to verify, not a finished artefact.[^s3]
2. **Research real users.** Field studies, interviews, surveys and diary studies supply the characteristics; cluster them into roles, merge similar groups and drop the less relevant ones before adding detail.[^s4]
3. **Map Salesforce personas to your users.** Survey or interview users to learn which activities they perform most; Trailhead supplies a sample Service Cloud survey that can be adapted for sales and marketing users. One person may map to several personas.[^s2]
4. **Keep only details that change design.** Every attribute should earn its place; anything that would not alter a design decision is noise.[^s4]
5. **Treat personas as living documents.** Revisit them as analytics and new research arrive; both GSA and NN/g frame them as artefacts that keep changing.[^s3][^s4]

## Using personas on a project

- **User stories.** Trailhead's template names the persona, the task and the impact, for example a Deal Closer who wants to log every customer interaction.[^s2]
- **Prioritisation.** Pick one primary persona (two at most) whom the interface must satisfy, plus secondary personas who use it less often; then rank features on value to the primary persona against technical difficulty.[^s2]
- **Roadmap and licensing.** Knowing which personas exist, and how many users map to each, informs purchasing, licensing and custom-feature decisions.[^s2]
- **Adoption and testing.** Personas decide which users attend which training and which users are recruited to test a given feature; NN/g adds usability-study screeners and analytics segmentation.[^s2][^s4]

## Gotchas

Personas invented in a conference room without research are the common failure: they encode the team's assumptions and give false confidence, which is why every source above insists on real user data.[^s1][^s3][^s4] A persona can also mark who a feature is *not* for, which prevents scope creep; too many primary personas does the opposite and makes scope too broad.[^s2] In public-sector programmes, research with members of the public may need legal review and even institutional review board sign-off, and participant incentives can be restricted, so plan that time in.[^s3]

## Connections

Personas are a technique within `kt:requirements-gathering`, the discovery practice that turns stakeholder needs into requirements.[^s2] They feed directly into `kt:user-stories`, whose "As a…" clause should name a persona; the Business Analyst exam weights user stories at 18% and customer discovery at 17%, though its prep unit does not name personas explicitly.[^s5] They complement `kt:stakeholder-mapping` (who has influence over the project) by describing who will actually use the system, and they are consumed by `kt:change-management-and-adoption` for training audiences, by `kt:user-acceptance-testing` for picking testers, and by `kt:licensing-strategy` when sizing user groups.[^s2] The roles that build and use them are the `kt:business-analyst` and the `kt:salesforce-architect`.

## Sources

[^s1]: Trailhead, "Get Started with Personas (UX Personas for Salesforce)". https://trailhead.salesforce.com/en/modules/ux-personas-for-salesforce/units/get_started_with_personas (accessed 2026-11-26)
[^s2]: Trailhead, "Work with Personas (UX Personas for Salesforce)". https://trailhead.salesforce.com/content/learn/modules/ux-personas-for-salesforce/work_with_personas (accessed 2026-11-26)
[^s3]: Frances Carden, Digital.gov (GSA), "Personas: learn how to discover your audience, understand them, and pivot to address their needs", 2023-05-19. https://digital.gov/2023/05/19/personas-learn-how-to-discover-your-audience-understand-them-and-pivot-to-address-their-needs (accessed 2026-11-26)
[^s4]: Taylor Dykes, Nielsen Norman Group, "Personas Make Users Memorable", 2025-10-03. https://www.nngroup.com/articles/persona/ (accessed 2026-11-26)
[^s5]: Trailhead, "Get Started with Salesforce Business Analyst Certification Prep". https://trailhead.salesforce.com/content/learn/modules/salesforce-business-analyst-certification-prep/get-started-with-salesforce-business-analyst-certification-prep (accessed 2026-11-26)
