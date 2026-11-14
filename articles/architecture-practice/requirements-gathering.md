---
id: kt:requirements-gathering
type: Concept
title: Requirements Gathering
aliases: [requirements elicitation, requirements discovery, customer discovery, discovery workshops]
domain: architecture-practice
summary: >-
  The practice of drawing out, analysing and confirming what stakeholders need from a Salesforce solution, using
  techniques such as interviews, workshops, observation and process mapping, and recording the results as
  requirements, user stories and acceptance criteria that design, build and testing can trace back to.
release: "Winter '27"
status: concept
broader: [kt:requirements-engineering]
related: [kt:non-functional-requirements, kt:salesforce-diagrams, kt:change-management-and-adoption, kt:testing-strategy]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: usedBy, object: kt:business-analyst}
  - {predicate: hasPart, object: kt:user-stories}
  - {predicate: hasPart, object: kt:business-process-mapping}
sources:
  - id: s1
    title: "Explore Techniques for Information Discovery"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/business-analyst_skills-strategies/explore-techniques--information-discovery
    type: official-learning
    accessed: 2026-11-14
  - id: s2
    title: "Learn About User Stories"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/user-story-creation/learn-about-user-stories
    type: official-learning
    accessed: 2026-11-14
  - id: s3
    title: "Construct a User Story"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/user-story-creation/construct-a-user-story
    type: official-learning
    accessed: 2026-11-14
  - id: s4
    title: "See Business Process Mapping in Practice"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/business-process-mapping/see-business-process-mapping-in-practice
    type: official-learning
    accessed: 2026-11-14
  - id: s5
    title: "Get Started with Salesforce Business Analyst Certification Prep"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-business-analyst-certification-prep/get-started-with-salesforce-business-analyst-certification-prep
    type: official-learning
    accessed: 2026-11-14
  - id: s6
    title: "The state-of-practice in requirements elicitation: an extended interview study at 12 companies"
    publisher: Requirements Engineering (Springer), preprint on arXiv
    url: https://arxiv.org/pdf/2102.11556
    type: peer-reviewed
    accessed: 2026-11-14
created: 2026-11-14
---

# Requirements Gathering

Requirements gathering, which business analysis practice calls elicitation, is how a Salesforce team finds out what a solution must do before it designs one. Trailhead adopts the BABOK definition: drawing forth or receiving information from stakeholders and other sources, the main way requirements and design information are discovered.[^s1] Much of the knowledge a project needs sits in people's heads and is seldom written down, so it has to be drawn out deliberately rather than collected from documents alone.[^s1]

## How it works

Trailhead splits elicitation into three stages. **Prepare** builds an accurate picture of the business need. **Conduct** meets stakeholders to learn their needs. **Confirm** checks that the stated requirements match the real problem and what stakeholders actually intended.[^s1] Before that, the analyst identifies stakeholders early, internal and external, and can use a stakeholder wheel to map each one's influence. They also study project history so past decisions are not reopened.[^s1] Strategy analysis frames the work: observe the current state, define the future and transition states, and run a gap analysis between them.[^s1]

Trailhead lists ten techniques: brainstorming, document analysis, focus groups, interface analysis, interviews, observation, process modelling, prototyping, requirements workshops and surveys. The analyst picks the mix that suits the project.[^s1] Who, what, where, why, when and how questions keep interviews concrete. For example, ask where data is entered, where it goes and how often a report is checked.[^s1]

Practice outside Salesforce looks similar. An interview study of 24 practitioners at 12 companies found that 83% used group techniques such as meetings and workshops, 42% used individual interviews, and most combined several techniques.[^s6] The same study found end users were rarely involved. The most common problems were stakeholders who could not state or rank their needs and requirements that kept changing, each reported by 54%.[^s6]

## From discovery to backlog

Process maps are a common bridge between discovery and build. Trailhead's mapping guidance prefers live workshops to questionnaires or one-to-one interviews, because a group can validate the map as it is drawn and settle disagreements on the spot. The end-to-end process owner chairs and resolves disputes.[^s4] Maps are drilled down level by level until the ambiguity is gone. Each activity box can carry its requirements, user stories, metadata and ERDs, so every build artefact traces back to a process step.[^s4]

Requirements then become user stories in the form "As a <who>, I want <what> so that <why>". Trailhead treats a story as a summary of a requirement told from the user's point of view, not the full specification.[^s2] Each story needs at least one acceptance criterion. Criteria are pass/fail statements that state intent rather than a solution, and testers use them to verify the build.[^s3] Stories should pass the INVEST check: independent, negotiable, valuable, estimable, small and testable. Writing them with the whole team in an early workshop avoids common faults such as undefined personas and vague criteria.[^s3]

## Gotchas

- **Solutioning too early.** A criterion that names a button instead of an outcome locks in design before the team has weighed options.[^s3]
- **Missing stakeholders.** A process workshop loses most of its value if anyone from input to outcome is absent.[^s4]
- **Unstable requirements.** Expect change and plan to re-elicit and re-prioritise, since unstable requirements are among the most common problems in practice.[^s6]

## Connections

Requirements gathering sits **broader** under requirements engineering, the wider discipline of which elicitation is the discovery step.[^s1] It is **used by** the business analyst and the Salesforce architect. The Salesforce Business Analyst certification weights Customer Discovery at 17%, Requirements at 18% and User Stories at 18% of its exam.[^s5] It **has part** business process mapping and user stories, the two main artefacts it produces.[^s4][^s2] It is **related** to non-functional requirements, the quality half of what discovery must capture; to Salesforce Diagrams, the notation for documenting current and future state; to the testing strategy, which turns acceptance criteria into tests;[^s3] and to change management and adoption, which reuses the stakeholder map built during discovery.[^s1]

## Sources

[^s1]: Trailhead, "Explore Techniques for Information Discovery". https://trailhead.salesforce.com/content/learn/modules/business-analyst_skills-strategies/explore-techniques--information-discovery (accessed 2026-11-14)
[^s2]: Trailhead, "Learn About User Stories". https://trailhead.salesforce.com/content/learn/modules/user-story-creation/learn-about-user-stories (accessed 2026-11-14)
[^s3]: Trailhead, "Construct a User Story". https://trailhead.salesforce.com/content/learn/modules/user-story-creation/construct-a-user-story (accessed 2026-11-14)
[^s4]: Trailhead, "See Business Process Mapping in Practice". https://trailhead.salesforce.com/content/learn/modules/business-process-mapping/see-business-process-mapping-in-practice (accessed 2026-11-14)
[^s5]: Trailhead, "Get Started with Salesforce Business Analyst Certification Prep". https://trailhead.salesforce.com/content/learn/modules/salesforce-business-analyst-certification-prep/get-started-with-salesforce-business-analyst-certification-prep (accessed 2026-11-14)
[^s6]: C. Palomares, X. Franch, C. Quer, P. Chatzipetrou, L. López, T. Gorschek, "The state-of-practice in requirements elicitation: an extended interview study at 12 companies", Requirements Engineering (2021). https://arxiv.org/pdf/2102.11556 (accessed 2026-11-14)
