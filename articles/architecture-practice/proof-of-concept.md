---
id: kt:proof-of-concept
type: Concept
title: Proof of Concept
aliases: [POC, PoC, proof-of-concept, technical spike, feasibility prototype]
domain: architecture-practice
summary: >-
  A small, time-boxed build that tests whether a proposed Salesforce design, product or AI use case can work before
  the organization commits to full delivery, judged against success criteria agreed in advance and usually run in a
  disposable org such as a scratch org, Developer Edition org or sandbox.
release: "Winter '27"
status: concept
broader: [kt:solution-design-tradeoffs]
related: [kt:scratch-orgs, kt:sandbox-types, kt:scale-test, kt:risk-and-assumption-logs, kt:build-vs-buy-decisions, kt:agent-development-lifecycle]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: mitigates, object: kt:technical-debt-in-salesforce}
  - {predicate: contrastsWith, object: kt:user-acceptance-testing}
sources:
  - id: s1
    title: "Technology Readiness Levels"
    publisher: NASA
    url: https://www.nasa.gov/directorates/spacetech/spinoff/feature/technology-readiness-levels
    type: government
    accessed: 2026-11-16
  - id: s2
    title: "Scratch Orgs (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-scratch-orgs.html
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "Explore Available Developer Environments (Environments for Salesforce Developers)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/es/content/learn/modules/environments-for-developers/explore-available-developer-environments
    type: official-learning
    accessed: 2026-11-16
  - id: s4
    title: "Create a Prototyping Plan (Strategy Design Prototyping)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/design-strategy-prototyping/create-prototyping-plan
    type: official-learning
    accessed: 2026-11-16
  - id: s5
    title: "New Report Says Most AI Pilots 'Remain Stuck' — Here's How To Move Ahead"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/agentic-ai-pilot-launch/
    type: official-blog
    accessed: 2026-11-16
  - id: s6
    title: "The Agentforce Operations Process Evolution Playbook: 8 Steps to Scale AI Process Automation"
    publisher: Salesforce
    url: https://www.salesforce.com/agentforce/process-evolution-playbook/
    type: official-blog
    accessed: 2026-11-16
created: 2026-11-16
---

# Proof of Concept

A proof of concept (POC) is a deliberately small build whose only job is to answer a feasibility question: can this design, product or use case actually work here? In engineering terms it sits early on the maturity ladder. NASA's Technology Readiness Levels place a proof-of-concept model at TRL 3, where analytical and laboratory studies check whether a technology is viable, and only reach a fully functional prototype at TRL 6.[^s1] On Salesforce projects, architects borrow the same idea: before committing a release plan to an untested integration pattern, an unfamiliar managed package, an agent use case or a data-volume assumption, they build just enough to prove or disprove it.

## Why architects run one

A POC converts an open assumption into evidence. The useful framing comes from Salesforce's own prototyping guidance: a prototype should answer one specific question with the least work possible, in the format most likely to answer it, and the team should decide in advance which signals it will look for.[^s4] If the foundational assumptions turn out wrong, the right response is to go back to research or design rather than push ahead.[^s4] That is exactly the outcome a POC exists to make cheap: discovering in two weeks of throwaway work that a design will not hold, instead of in month six of delivery.

## Running a POC well

- **Scope one question.** Salesforce advises starting from a business pain point and a single, tightly focused use case rather than the technology itself.[^s5]
- **Agree success criteria before building.** Decide how success will be measured and which metrics to track before launch.[^s5]
- **Pick a disposable environment.** Scratch orgs and Developer Edition orgs suit greenfield experiments; sandboxes suit tests that need production metadata.[^s3]
- **Use representative data, not real personal data.** Scratch orgs accept synthetic or dummy test data, and Salesforce advises against loading personal data into them.[^s2]
- **Bring the right people in early.** Technical experts judge feasibility, while business leaders and end users confirm fit and value.[^s5]
- **Write up and decide.** Check whether the build produced a clear answer to the original question, and run more sessions if it did not.[^s4]

## Choosing an environment

The environment choice shapes what a POC can prove. A Developer Edition org is free, has no time limit and is intended for trying Salesforce and evaluating features before buying, but it carries a 250 MB data limit and older orgs may lack newer features.[^s3] A scratch org is created from a Dev Hub with the Salesforce CLI and copies no data, metadata or users from production; its "shape" of edition, features, settings, licenses and limits is set by a definition file, an org shape or a snapshot, so it can mimic production without inheriting its clutter.[^s2] Scratch orgs default to 7 days and can live for 1 to 30 days, cannot be restored once expired, and count against the Dev Hub's daily and active scratch org limits.[^s2] When the question depends on existing production configuration, a sandbox is the better base; Trailhead notes that only Full sandboxes support performance testing, load testing and staging.[^s3]

## Limits and gotchas

- **A POC is not a pilot or a production release.** Salesforce's Agentforce Operations playbook explicitly sets the goal as a real production deployment with measurable value, not a POC.[^s6]
- **Proof of feasibility is not proof of value.** Salesforce cites research that most enterprise generative AI pilots show no measurable value, and ties success to metrics chosen up front.[^s5]
- **Throwaway code tends to survive.** Rebuild a POC properly; never deploy it.
- **Small orgs hide scale problems.** A Developer Edition or scratch org cannot answer volume or concurrency questions; those need a Full sandbox or a dedicated load test.[^s3]
- **AI POCs depend on content quality.** Salesforce stresses removing outdated content, filling gaps and resolving terms with multiple meanings before judging an agent.[^s5]

## Connections

A POC is a tool of `kt:solution-design-tradeoffs` (`broader`): when two options cannot be separated on paper, a time-boxed build supplies the evidence, and the result belongs in `kt:architecture-decision-records`. It is a routine instrument of the `kt:salesforce-architect` (`usedBy`), and it closes items in `kt:risk-and-assumption-logs` by testing assumptions directly, the same discipline Salesforce's prototyping guidance describes.[^s4] It informs `kt:build-vs-buy-decisions`, since evaluating a product before purchase is a stated use of Developer Edition orgs.[^s3] Practically it runs on `kt:scratch-orgs` or one of the `kt:sandbox-types`, and performance questions escalate to `kt:scale-test`, because only Full sandboxes support load testing.[^s2][^s3] For agents, the POC corresponds to the discovery-and-demonstration stage that comes before a first live deployment, and the `kt:agent-development-lifecycle` then carries the agent toward production with gradual onboarding and guardrail testing on the way to production.[^s5][^s6] It `mitigates` `kt:technical-debt-in-salesforce` by killing bad designs early, but only if its code is discarded rather than shipped. Finally it `contrastsWith` `kt:user-acceptance-testing`: a POC asks "can this work?" before build, while UAT asks "did we build the right thing?" at the end.

## Sources
[^s1]: NASA, "Technology Readiness Levels". https://www.nasa.gov/directorates/spacetech/spinoff/feature/technology-readiness-levels (accessed 2026-11-16)
[^s2]: Salesforce Developers, "Scratch Orgs (Salesforce DX Developer Guide)". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-scratch-orgs.html (accessed 2026-11-16)
[^s3]: Trailhead, "Explore Available Developer Environments (Environments for Salesforce Developers)". https://trailhead.salesforce.com/es/content/learn/modules/environments-for-developers/explore-available-developer-environments (accessed 2026-11-16)
[^s4]: Trailhead, "Create a Prototyping Plan (Strategy Design Prototyping)". https://trailhead.salesforce.com/content/learn/modules/design-strategy-prototyping/create-prototyping-plan (accessed 2026-11-16)
[^s5]: Salesforce, "New Report Says Most AI Pilots 'Remain Stuck' — Here's How To Move Ahead". https://www.salesforce.com/blog/agentic-ai-pilot-launch/ (accessed 2026-11-16)
[^s6]: Salesforce, "The Agentforce Operations Process Evolution Playbook: 8 Steps to Scale AI Process Automation". https://www.salesforce.com/agentforce/process-evolution-playbook/ (accessed 2026-11-16)
