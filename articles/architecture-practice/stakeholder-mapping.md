---
id: kt:stakeholder-mapping
type: ExternalConcept
title: Stakeholder Mapping
aliases: [stakeholder analysis, power-interest grid, power/interest matrix, stakeholder wheel, stakeholder radar, influence mapping]
domain: architecture-practice
summary: >-
  The practice of systematically identifying everyone who affects or is affected by a project and analysing their
  power, interest and relationships, so that each group gets a deliberate level of engagement; on Salesforce programmes
  it drives discovery planning, sign-off and change management.
release: "Winter '27"
status: concept
broader: [kt:requirements-gathering]
related: [kt:user-personas, kt:raci-matrix, kt:change-management-and-adoption, kt:salesforce-governance, kt:design-authority]
relations:
  - {predicate: usedBy, object: kt:business-analyst}
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: enables, object: kt:change-management-and-adoption}
  - {predicate: contrastsWith, object: kt:user-personas}
sources:
  - id: s1
    title: "Techniques for Effective Information Discovery (Essential Business Analyst Skills)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/business-analyst_skills-strategies/explore-techniques--information-discovery
    type: official-learning
    accessed: 2026-11-28
  - id: s2
    title: "Review Collaboration with Stakeholders (Cert Prep: Salesforce Business Analyst)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-business-analyst-certification-prep/reivew-collaboration-with-stakeholders
    type: official-learning
    accessed: 2026-11-28
  - id: s3
    title: "4.3.2 Stakeholder mapping (Urban WASH: Working with People, Study Session 4)"
    publisher: The Open University (OpenLearn Create)
    url: https://www.open.edu/openlearncreate/mod/oucontent/view.php?id=80594&section=5.2
    type: academic
    accessed: 2026-11-28
  - id: s4
    title: "Stakeholder Analysis (A Practical Guide To Delivering Results)"
    publisher: University of Leeds
    url: https://deliveringresults.leeds.ac.uk/delivering-results-themes/people/stakeholders-2/stakeholder-management/
    type: academic
    accessed: 2026-11-28
  - id: s5
    title: "Influence Mapping"
    publisher: Your Washington (Washington State government)
    url: https://your.wa.gov/cx-resources/influence-mapping/
    type: government
    accessed: 2026-11-28
  - id: s6
    title: "Stakeholder Analysis using the Power Interest Grid"
    publisher: ProjectManagement.com wiki
    url: https://www.projectmanagement.com/wikis/368897/stakeholder-analysis--using-the-power-interest-grid
    type: community
    accessed: 2026-11-28
created: 2026-11-28
---

# Stakeholder Mapping

**Stakeholder mapping** is the work of systematically identifying the people and groups relevant to a project and analysing their relationships, their interest in it and the power they hold over it.[^s3] Trailhead defines stakeholders as individuals or groups, inside or outside the company, who make decisions or shape priorities and requirements, and it gives a simple test for inclusion: anyone with an interest in the issue, or who may be affected by it.[^s1] The output is not just a list but a plan: which groups to involve closely, which to keep satisfied or informed, and which simply to watch.[^s4][^s6]

On a Salesforce programme the map is built at the very start of discovery, because it decides who is invited to workshops, whose requirements carry weight and who must sign off. Trailhead advises identifying stakeholders early and positions the business analyst as a trusted advisor who links business and technical teams.[^s1][^s2]

## How it works

1. **Identify.** Brainstorm everyone affected by the work, everyone with power or influence over it, and everyone with an interest in the outcome.[^s6] Trailhead's role list mixes internal parties (owner, manager, employee) with external ones (customer, partner, supplier, competitor, regulator), a reminder that the map rarely stops at the org's users.[^s1]
2. **Analyse.** Rate each stakeholder on at least two dimensions, usually power (or influence) and interest. Trailhead uses a stakeholder wheel to show how much influence each party can exert on the project.[^s1]
3. **Plot.** Place stakeholders on a power/interest grid, or on a radar whose rings run from vital to engage down to courtesy to inform; the map can also show relationships between groups and arrows toward the position you want each group to reach.[^s4]
4. **Plan engagement.** Turn the picture into an engagement plan with objectives, scope and methods, matching the method to how involved each group needs to be.[^s3]
5. **Revisit.** A useful map shows gaps and assigns follow-up actions, so it should be re-checked as the project and its people change.[^s5]

## The power/interest grid

The grid splits stakeholders into four groups.[^s3][^s6]

- **High power, high interest:** the decision makers with the most impact; manage their expectations closely.[^s6]
- **High power, low interest:** keep them satisfied and handle them with care, since an unhappy senior sponsor can derail scope.[^s6]
- **Low power, high interest:** keep them adequately informed; they often know the process detail and spot issues first.[^s6]
- **Low power, low interest:** monitor them without flooding them with communication.[^s6]

The Open University's version of the grid, adapted from UK development guidance, warns that the high-interest, low-power group often holds the most marginalised people, which is why a map should prompt deliberate effort to hear them.[^s3] In Salesforce terms this is frequently the frontline user population: low formal power, highest daily exposure to the new system.

## Gotchas

- **Groups versus people.** Stakeholders may be organisations, but communication has to reach named individuals; Washington State's guidance likewise says to name roles rather than vague groups.[^s5][^s6]
- **A static map goes stale.** Sponsors move on and interest rises near go-live, so treat the map as a living artefact with follow-up actions.[^s5]
- **Mapping is not engagement.** Leeds pairs the grid with practical habits: recruit early adopters as champions, show early wins, explain why, and keep communication two-way.[^s4]
- **Language matters.** Some public bodies now say "influence mapping" and avoid the word stakeholder in favour of more inclusive terms; the technique is the same.[^s5]

## Connections

Stakeholder mapping is a technique within `kt:requirements-gathering`: it decides whose needs are elicited before interviews, workshops and surveys begin.[^s1] It is used chiefly by the `kt:business-analyst` and the `kt:salesforce-architect`; the Business Analyst cert prep says the section on collaborating with stakeholders makes up 23% of the exam, covering discovery planning, competing priorities and sign-off.[^s2] It contrasts with `kt:user-personas`, which describe who will use the system rather than who holds power over the project, and it enables `kt:change-management-and-adoption`, whose champions and communications are drawn from the map.[^s4] Once stakeholders are known, a `kt:raci-matrix` fixes their decision rights, and the high-power group usually sits on the `kt:design-authority` or wider `kt:salesforce-governance` bodies.[^s4][^s6]

## Sources

[^s1]: Trailhead, "Techniques for Effective Information Discovery (Essential Business Analyst Skills)". https://trailhead.salesforce.com/content/learn/modules/business-analyst_skills-strategies/explore-techniques--information-discovery (accessed 2026-11-28)
[^s2]: Trailhead, "Review Collaboration with Stakeholders (Cert Prep: Salesforce Business Analyst)". https://trailhead.salesforce.com/content/learn/modules/salesforce-business-analyst-certification-prep/reivew-collaboration-with-stakeholders (accessed 2026-11-28)
[^s3]: The Open University, "4.3.2 Stakeholder mapping", Urban WASH: Working with People. https://www.open.edu/openlearncreate/mod/oucontent/view.php?id=80594&section=5.2 (accessed 2026-11-28)
[^s4]: University of Leeds, "Stakeholder Analysis", A Practical Guide To Delivering Results. https://deliveringresults.leeds.ac.uk/delivering-results-themes/people/stakeholders-2/stakeholder-management/ (accessed 2026-11-28)
[^s5]: Your Washington (Washington State), "Influence Mapping". https://your.wa.gov/cx-resources/influence-mapping/ (accessed 2026-11-28)
[^s6]: ProjectManagement.com wiki, "Stakeholder Analysis using the Power Interest Grid", last edited 2023-04-14. https://www.projectmanagement.com/wikis/368897/stakeholder-analysis--using-the-power-interest-grid (accessed 2026-11-28)
