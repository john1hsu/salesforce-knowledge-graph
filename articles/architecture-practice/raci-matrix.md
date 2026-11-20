---
id: kt:raci-matrix
type: ExternalConcept
title: RACI Matrix
aliases: [RACI chart, responsibility assignment matrix, RASCI, RACI-VS, responsibility matrix]
domain: architecture-practice
summary: >-
  A responsibility assignment grid that maps each task, deliverable or decision to the roles that are Responsible,
  Accountable, Consulted and Informed; a general project-management tool that Salesforce programs and Centers of
  Excellence use to make decision rights explicit.
release: "Winter '27"
status: concept
broader: [kt:salesforce-governance]
related: [kt:salesforce-center-of-excellence, kt:design-authority, kt:risk-and-assumption-logs, kt:statement-of-work, kt:agentforce]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: contrastsWith, object: kt:architecture-decision-records}
sources:
  - id: s1
    title: "RACI and RASCI Definitions"
    publisher: IT@Cornell (Cornell University)
    url: https://it.cornell.edu/index.php/it-service-management/raci-and-rasci-definitions
    type: academic
    accessed: 2026-11-20
  - id: s2
    title: "Responsibility matrix"
    publisher: University of Essex, Strategic Projects Office
    url: https://www.essex.ac.uk/staff/strategic-project-delivery/responsibility-matrix
    type: academic
    accessed: 2026-11-20
  - id: s3
    title: "Lessons Learned: The RACI Diagram Tool (Sexual Risk Avoidance Program Evaluation)"
    publisher: U.S. HHS Office of Population Affairs
    url: https://www.opa.hhs.gov/sites/default/files/2020-12/short-lesson-learned-raci-diagram-tool.pdf
    type: government
    accessed: 2026-11-20
  - id: s4
    title: "Stakeholder Management and RACI: Who Does What, and Who Answers for It"
    publisher: Project Management Institute (blog, 2026-07-29)
    url: https://www.pmi.org/blog/stakeholder-management-raci
    type: community
    accessed: 2026-11-20
  - id: s5
    title: "Build a Salesforce Center of Excellence That Keeps Pace with AI"
    publisher: Salesforce Architect blog (Allison Park, 2026-08-11)
    url: https://www.salesforce.com/blog/center-of-excellence-ai-governance/
    type: official-blog
    accessed: 2026-11-20
  - id: s6
    title: "Implement Your Salesforce CoE's Core Capabilities"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-governance-with-a-center-of-excellence/implement-your-salesforce-coes-core-capabilities
    type: official-learning
    accessed: 2026-11-20
created: 2026-11-20
---

# RACI Matrix

A RACI matrix (also called a RACI chart or responsibility assignment matrix) is a grid with roles along one axis and tasks, deliverables or decisions along the other; each cell says whether that role is Responsible, Accountable, Consulted or Informed for that item.[^s1] Essex frames it as a responsibility matrix built for the project's tasks, and also uses it for process mapping, organisational analysis and defining new IT systems.[^s2] It is a general project-management technique, not a Salesforce feature, but it is a common way for Salesforce programs to write down decision rights.

## The four letters

- **Responsible**: the person or team that does the work; several people can share it, and the same person can also be the A.[^s1][^s3]
- **Accountable**: the single owner of the outcome who signs off and makes sure the work is resourced and done to standard.[^s1][^s3]
- **Consulted**: people whose input is sought before the work or decision is finalized.[^s1][^s3]
- **Informed**: people kept up to date on progress or outcomes, often leadership or wider stakeholders.[^s1][^s3]

The rule every source repeats is one Accountable per item. Cornell allows only one A per row, and Essex says conflicts must be resolved so no task has more than one accountable role.[^s1][^s2] PMI warns that two names in the A column invite disputes and an empty A column means work gets dropped; in a matrixed organization the usual fix is a sponsor decision.[^s4] An HHS program evaluation reached the same lesson in practice: naming one lead "decider" up front kept decisions fast with limited staff.[^s3]

## Building one

The University of Essex gives a six-step method: list tasks in completion order down the side, list roles across the top, fill in the cells, check that each task has both a responsible and an accountable role, remove duplicate As, and agree the finished matrix with stakeholders before the project starts.[^s2] It recommends building the matrix alongside the work breakdown structure, and notes that the project manager is accountable for overall delivery without being responsible for every task.[^s2] HHS adds that the chart should be drafted during planning, shared with all staff, and revised as roles change.[^s3]

Variants add letters. RASCI adds **Support** for people who help without formal responsibility, which Cornell suggests instead of piling up extra Rs. RACI-VS adds a **Verifier** and a **Signatory**.[^s1][^s2]

## Gotchas

- Too many Rs blur ownership; prefer one R and mark helpers as Support.[^s1]
- Every C and I creates a real obligation to consult or notify, so leave off people who are not needed.[^s1]
- Agreement is the hard part when people see their responsibilities differently; settle it before work starts.[^s2]
- Automation and AI agents can be Responsible for bounded tasks, but PMI says the A and escalation must stay with a named human.[^s4]

## Applying it on Salesforce programs

Salesforce's own Center of Excellence guidance does not prescribe a RACI, but it raises the questions one answers. A Salesforce Architect blog post lists roles from executive sponsor and business-lead steering committee down to admins, developers and architects. It then asks who approves changes, who owns the backlog with final say on priorities, and who decides when tech debt is fixed or worked around.[^s5] It also calls for a named owner with formal sign-off on schema changes.[^s5] Trailhead assigns a Design Authority within the CoE to set architectural guidelines, review the technical build of requests and approve rare exceptions. It also has the CoE define the sandbox-to-production path and release cadence.[^s6] Each of those activities is a natural RACI row, with the Design Authority or architect typically Accountable for design approvals and business leads Accountable for priorities.[^s5][^s6]

## Connections

The matrix sits under `kt:salesforce-governance` because it records who holds which decision rights. It is a working tool of a `kt:salesforce-center-of-excellence` and of the `kt:design-authority`, whose approval and review duties map directly onto Accountable and Consulted cells.[^s6] It is **used by** the `kt:salesforce-architect`, who usually owns data model and integration decisions.[^s5] It **contrasts with** `kt:architecture-decision-records`: an ADR records what was decided and why, while a RACI records who decides. Risk owners on a `kt:risk-and-assumption-logs` register and client-versus-partner duties in a `kt:statement-of-work` are often taken from the RACI. For `kt:agentforce` work, PMI's advice applies: an agent can do the task, but a named human stays Accountable.[^s4]

## Sources

[^s1]: IT@Cornell, "RACI and RASCI Definitions". https://it.cornell.edu/index.php/it-service-management/raci-and-rasci-definitions (accessed 2026-11-20)
[^s2]: University of Essex, Strategic Projects Office, "Responsibility matrix". https://www.essex.ac.uk/staff/strategic-project-delivery/responsibility-matrix (accessed 2026-11-20)
[^s3]: U.S. HHS Office of Population Affairs, "Lessons Learned: The RACI Diagram Tool". https://www.opa.hhs.gov/sites/default/files/2020-12/short-lesson-learned-raci-diagram-tool.pdf (accessed 2026-11-20)
[^s4]: Project Management Institute, "Stakeholder Management and RACI: Who Does What, and Who Answers for It", 2026-07-29. https://www.pmi.org/blog/stakeholder-management-raci (accessed 2026-11-20)
[^s5]: Allison Park, "Build a Salesforce Center of Excellence That Keeps Pace with AI", Salesforce Architect blog, 2026-08-11. https://www.salesforce.com/blog/center-of-excellence-ai-governance/ (accessed 2026-11-20)
[^s6]: Salesforce Trailhead, "Implement Your Salesforce CoE's Core Capabilities". https://trailhead.salesforce.com/content/learn/modules/salesforce-governance-with-a-center-of-excellence/implement-your-salesforce-coes-core-capabilities (accessed 2026-11-20)
