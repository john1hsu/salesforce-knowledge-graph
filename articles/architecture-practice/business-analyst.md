---
id: kt:business-analyst
type: Role
title: Salesforce Business Analyst
aliases: [Salesforce BA, business analyst role in the Salesforce ecosystem]
domain: architecture-practice
summary: >-
  The project-based Salesforce ecosystem role that elicits, documents and analyzes business requirements, maps
  current and future processes, writes user stories and drives user acceptance, acting as the interpreter between
  business stakeholders and the admins, developers and architects who build the solution.
release: "Winter '27"
status: current
broader: [kt:salesforce-ecosystem-roles]
related: [kt:requirements-gathering, kt:user-stories, kt:fit-gap-analysis, kt:user-acceptance-testing, kt:salesforce-architect]
relations:
  - {predicate: coveredBy, object: kt:business-analyst-certification}
sources:
  - id: s1
    title: "Salesforce Business Analyst Quick Look: Learn About the Salesforce Business Analyst Role"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-business-analyst-quick-look/learn-about-the-salesforce-business-analyst-role
    type: official-learning
    accessed: 2026-11-27
  - id: s2
    title: "Business Analyst Skills and Strategies: Discover the Top Business Analyst Skills"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/business-analyst_skills-strategies/discover-top-business-analyst-skills
    type: official-learning
    accessed: 2026-11-27
  - id: s3
    title: "Salesforce Admins and Salesforce BAs Quick Look: Compare the Admin and BA Roles"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-admins-and-salesforce-bas-quick-look/compare-the-admin-and-ba-roles
    type: official-learning
    accessed: 2026-11-27
  - id: s4
    title: "Business Process Mapping: Understand the Value of Business Analysis"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/business-process-mapping/understand-the-value-of-business-analysis
    type: official-learning
    accessed: 2026-11-27
  - id: s5
    title: "Salesforce Business Analyst Certification Prep: Get Started"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-business-analyst-certification-prep/get-started-with-salesforce-business-analyst-certification-prep
    type: official-learning
    accessed: 2026-11-27
  - id: s6
    title: "Certification - Salesforce Certified Business Analyst"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/credentials/businessanalyst
    type: official-learning
    accessed: 2026-11-27
created: 2026-11-27
---

# Salesforce Business Analyst

A Salesforce business analyst (BA) is a project-based role focused on improving how a business works. The BA elicits, documents and analyzes requirements, turns them into data-driven solution proposals, and serves as the interpreter between IT and business stakeholders.[^s1] Trailhead describes BAs as the "fix-it people" of a program team: they drive change at any scale, from converting a financial system to adjusting a single sales-forecast process, because they understand both the technology and the business process it supports.[^s2]

## What the role does

Trailhead breaks the BA's work into a sequence of activities: communicating with stakeholders, eliciting needs, documenting requirements, analyzing what was gathered, facilitating a solution, helping implement it (where the BA often behaves like a project manager), and testing, which includes building training material and collecting user feedback.[^s1] Concrete deliverables in Salesforce's own task list include project roadmaps, user stories, current-state and future-state process documentation, business presentations, user training materials, and resolution of issues found in testing.[^s3]

The soft skills Salesforce lists are needs analysis, requirements elicitation, writing and review, business case definition, flow and process diagramming, wireframing, business data analytics and problem solving. On the technical side a BA needs a working understanding, not deep expertise, of automation, data management, reports and dashboards, collaboration features, the platform and AgentExchange.[^s1] A separate Trailhead module condenses this into three core skills: information discovery across all levels of an organization, analysis and synthesis of detail and big-picture information, and clear communication and documentation.[^s2]

## BA versus admin

The admin and BA are often confused because one person may hold both jobs. Salesforce frames the admin as an operational role that sets up users, security, objects, automation and environments and keeps the org healthy, while the BA is project-based and uses data to plan and oversee change.[^s3] Salesforce also corrects four common misconceptions: a BA does not have to be highly technical, configuring the org is optional rather than expected, the BA should be involved from the start of a project rather than after kickoff, and the job goes well beyond writing requirements.[^s1]

## Why it matters

Trailhead's process-mapping content argues that analysis should come before architecture and build. Good analysis raises adoption by ensuring the right apps get built, reduces rework through clearer requirements, informs the data model and metrics, and supports agility during digital transformation.[^s4] A process map that captures steps, owners and success measures becomes most valuable when it is linked to the other implementation assets, such as user stories and test cases.[^s4]

## Certification

The role is validated by the Salesforce Certified Business Analyst credential, aimed at professionals who understand business needs, capture requirements and work with stakeholders to shape Salesforce solutions.[^s6] As checked for Winter '27, the exam outline weights Customer Discovery at 17%, Collaboration with Stakeholders at 23%, Business Process Mapping at 12%, Requirements at 18%, User Stories at 18% and User Acceptance at 12%. The intended candidate has about two years of business analysis experience and two years on the Salesforce Platform, and the credential must be maintained annually through release maintenance modules.[^s5]

## Connections

- **broader → `kt:salesforce-ecosystem-roles`**: the BA is one of the ecosystem's career roles alongside admins, developers and architects.[^s3]
- **related → `kt:requirements-gathering`, `kt:user-stories`, `kt:fit-gap-analysis`**: the elicitation and documentation techniques that make up most of the BA's daily work.[^s1][^s3]
- **related → `kt:user-acceptance-testing`**: the BA owns testing support, training and feedback, and User Acceptance is a scored exam section.[^s1][^s5]
- **related → `kt:salesforce-architect`**: the BA's process and requirements analysis feeds the architect's design decisions.[^s4]
- **coveredBy → `kt:business-analyst-certification`**: the credential whose exam outline maps to the role's six areas.[^s5][^s6]

## Sources

[^s1]: Trailhead, "Salesforce Business Analyst Quick Look: Learn About the Salesforce Business Analyst Role". https://trailhead.salesforce.com/content/learn/modules/salesforce-business-analyst-quick-look/learn-about-the-salesforce-business-analyst-role (accessed 2026-11-27)
[^s2]: Trailhead, "Business Analyst Skills and Strategies: Discover the Top Business Analyst Skills". https://trailhead.salesforce.com/content/learn/modules/business-analyst_skills-strategies/discover-top-business-analyst-skills (accessed 2026-11-27)
[^s3]: Trailhead, "Salesforce Admins and Salesforce BAs Quick Look: Compare the Admin and BA Roles". https://trailhead.salesforce.com/content/learn/modules/salesforce-admins-and-salesforce-bas-quick-look/compare-the-admin-and-ba-roles (accessed 2026-11-27)
[^s4]: Trailhead, "Business Process Mapping: Understand the Value of Business Analysis". https://trailhead.salesforce.com/content/learn/modules/business-process-mapping/understand-the-value-of-business-analysis (accessed 2026-11-27)
[^s5]: Trailhead, "Salesforce Business Analyst Certification Prep: Get Started". https://trailhead.salesforce.com/content/learn/modules/salesforce-business-analyst-certification-prep/get-started-with-salesforce-business-analyst-certification-prep (accessed 2026-11-27)
[^s6]: Trailhead, "Certification - Salesforce Certified Business Analyst". https://trailhead.salesforce.com/en/credentials/businessanalyst (accessed 2026-11-27)
