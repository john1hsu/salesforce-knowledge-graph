---
id: kt:sharing-and-visibility-architect-certification
type: Certification
title: Sharing and Visibility Architect Certification
aliases: [Salesforce Certified Platform Sharing and Visibility Architect, Sharing and Visibility Architect exam]
domain: security-and-sharing
summary: >-
  Salesforce's domain architect credential for designing scalable record-access (sharing and visibility) solutions on
  the Salesforce Platform; it is one of the four certifications that together grant the Application Architect
  credential on the path to Certified Technical Architect.
release: "Winter '27"
status: current
broader: [kt:salesforce-architect]
related: [kt:salesforce-sharing-model, kt:organization-wide-defaults, kt:role-hierarchy, kt:sharing-rules, kt:restriction-rules, kt:data-skew, kt:sharing-recalculation]
relations:
  - {predicate: partOf, object: kt:application-architect-certification}
  - {predicate: contrastsWith, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "Certification - Salesforce Certified Platform Sharing and Visibility Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/sharingandvisibilityarchitect
    type: official-learning
    accessed: 2026-11-03
  - id: s2
    title: "Certification - Salesforce Certified Application Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/applicationarchitect
    type: official-learning
    accessed: 2026-11-03
  - id: s3
    title: "Certification - Architect Overview"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/architectoverview
    type: official-learning
    accessed: 2026-11-03
  - id: s4
    title: "Certification - Salesforce Certified Technical Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/technicalarchitect
    type: official-learning
    accessed: 2026-11-03
  - id: s5
    title: "Platform Sharing Architecture"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-sharing-architecture
    type: official-docs
    accessed: 2026-11-03
  - id: s6
    title: "Designing Record Access for Enterprise Scale: Introduction"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/draes/guide/draes-introduction.html
    type: official-docs
    accessed: 2026-11-03
created: 2026-11-03
---

# Sharing and Visibility Architect Certification

The Salesforce Certified Platform Sharing and Visibility Architect is the architect-level credential for people who design scalable, high-performing Salesforce Platform solutions that satisfy sharing and visibility security requirements — in other words, who decides which users can see and edit which records, and how that design behaves at volume.[^s1] Trailhead lists it among the architect credentials alongside data, integration, identity and development-lifecycle domain exams.[^s3]

## Where it sits in the architect path

Like the other domain architect exams, it is mostly a stepping stone. Salesforce grants the **Application Architect** credential automatically once a candidate holds four prerequisites: Platform App Builder, Platform Data Architect, Platform Developer and Platform Sharing and Visibility Architect; there is no separate Application Architect exam.[^s2] Application Architects are described as experts at modelling a role hierarchy, data and the appropriate sharing mechanisms.[^s2][^s3] The Certified Technical Architect (CTA) credential lists Application Architect and System Architect as its two prerequisites, so every CTA candidate passes this exam on the way.[^s4]

## What it tests (at a practitioner level)

The credential page frames the exam around designing record-access solutions rather than configuring individual settings, and recommends the "Architect Journey: Sharing and Visibility" Trailmix as preparation.[^s1] Salesforce's own architecture guidance on the platform sharing model maps the territory well: organization-wide defaults as the baseline, then role hierarchy, public groups, owner- and criteria-based sharing rules, guest user sharing rules, manual sharing, teams, territory hierarchy, Apex managed sharing and implicit sharing to open access, with restriction rules to narrow it.[^s5] Object and field permissions sit alongside record access, and the guidance prefers permission sets over profiles.[^s5]

The architect-level angle is scale. The same guidance gives design numbers a candidate should be comfortable reasoning about: up to 5,000 roles in orgs created in Spring '21 or later, no more than 10 levels of role-hierarchy branches, public groups nested no more than five levels, 300 owner-based sharing rules per object, and 50 criteria-based plus guest user sharing rules per object combined.[^s5] It also warns about data and ownership skew, recommending ratios no worse than about 1:10,000, and about the cost of sharing recalculation when OWDs, hierarchies, groups or ownership change.[^s5] The deeper reference is *Designing Record Access for Enterprise Scale*, written for expert architects handling complex access requirements or large realignments, and covering group maintenance, sharing recalculation, bulk loading and realignment tooling.[^s6]

## Gotchas

- **Exam logistics live elsewhere.** The credential page links out to a separate exam page for registration; check question count, timing, fee and section weightings there at registration time rather than in third-party summaries.[^s1]
- **Know the edges of each mechanism.** Implicit sharing does not apply to custom objects, manual shares are removed when ownership changes, and guest user sharing rules expose matching records to unauthenticated users immediately — the kind of detail scenario questions hinge on.[^s5]
- **Recalculation is a design constraint.** Bulk realignments can have automatic recalculation deferred via Salesforce Support, and structural hierarchy changes are best kept to roughly quarterly.[^s5]

## When to pursue it

Pursue it if you design record-level security, data access for internal and external users, or large-volume orgs, or if you are aiming for Application Architect or CTA.[^s2][^s4] If your security work is mainly authentication, SSO and API authorization, the Identity and Access Management Architect exam (which feeds System Architect) is the closer fit.[^s3]

## Connections

- **broader → `kt:salesforce-architect`**: one rung of the Salesforce architect credential ladder.[^s3]
- **partOf → `kt:application-architect-certification`**: one of the four certifications that roll up into Application Architect.[^s2]
- **contrastsWith → `kt:identity-and-access-management-architect-certification`**: both are security-flavoured domain exams, but one covers who can see which records and the other how users authenticate, and they feed different designations.[^s2][^s3]
- **related → `kt:salesforce-sharing-model`, `kt:organization-wide-defaults`, `kt:role-hierarchy`, `kt:sharing-rules`, `kt:restriction-rules`**: the record-access building blocks the exam is built around.[^s5]
- **related → `kt:data-skew`, `kt:sharing-recalculation`**: the scale and performance concerns that distinguish architect-level sharing design.[^s5][^s6]

## Sources
[^s1]: Trailhead, "Certification - Salesforce Certified Platform Sharing and Visibility Architect". https://trailhead.salesforce.com/credentials/sharingandvisibilityarchitect (accessed 2026-11-03)
[^s2]: Trailhead, "Certification - Salesforce Certified Application Architect". https://trailhead.salesforce.com/credentials/applicationarchitect (accessed 2026-11-03)
[^s3]: Trailhead, "Certification - Architect Overview". https://trailhead.salesforce.com/credentials/architectoverview (accessed 2026-11-03)
[^s4]: Trailhead, "Certification - Salesforce Certified Technical Architect". https://trailhead.salesforce.com/credentials/technicalarchitect (accessed 2026-11-03)
[^s5]: Salesforce Architects, "Platform Sharing Architecture". https://architect.salesforce.com/fundamentals/platform-sharing-architecture (accessed 2026-11-03)
[^s6]: Salesforce Developers, "Designing Record Access for Enterprise Scale: Introduction". https://developer.salesforce.com/docs/platform/draes/guide/draes-introduction.html (accessed 2026-11-03)
