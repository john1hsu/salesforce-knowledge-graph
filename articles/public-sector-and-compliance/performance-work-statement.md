---
id: kt:performance-work-statement
type: ExternalConcept
title: Performance Work Statement
aliases: [PWS, performance-based work statement]
domain: public-sector-and-compliance
summary: >-
  The U.S. federal contract document, defined in FAR Subpart 37.6, that describes a services requirement by the
  results the government needs and the measurable standards it will judge them by, rather than by method or labor
  hours. Federal buyers of Salesforce implementation and managed services typically issue or accept one in place
  of a commercial statement of work.
release: "Winter '27"
status: concept
broader: [kt:federal-acquisition-regulation]
related: [kt:public-sector-solutions, kt:authority-to-operate, kt:non-functional-requirements, kt:user-acceptance-testing, kt:requirements-gathering]
relations:
  - {predicate: contrastsWith, object: kt:statement-of-work}
  - {predicate: hasPart, object: kt:quality-assurance-surveillance-plan}
  - {predicate: dependsOn, object: kt:statement-of-objectives}
sources:
  - id: s1
    title: "FAR 37.602 Performance work statement"
    publisher: U.S. General Services Administration (Acquisition.gov)
    url: https://www.acquisition.gov/far/37.602
    type: government
    accessed: 2026-11-22
  - id: s2
    title: "FAR 37.601 General (Performance-Based Acquisition)"
    publisher: U.S. General Services Administration (Acquisition.gov)
    url: https://www.acquisition.gov/far/37.601
    type: government
    accessed: 2026-11-22
  - id: s3
    title: "Acquisition of Services — Step 4: Requirements Definition"
    publisher: Defense Acquisition University, Adaptive Acquisition Framework (OUSD(A&S) guidance)
    url: https://aaf.dau.edu/aaf/services/step4
    type: government
    accessed: 2026-11-22
  - id: s4
    title: "AAS Quality Assurance Surveillance Plan (QASP) Template"
    publisher: U.S. General Services Administration, Assisted Acquisition Services
    url: https://aas.gsa.gov/assets/pdf_docs/QASP_Template_FINAL_19Sep22.pdf
    type: government
    accessed: 2026-11-22
created: 2026-11-22
---

# Performance Work Statement

A **performance work statement (PWS)** is the requirements document at the centre of performance-based acquisition of services in the U.S. federal government. The Federal Acquisition Regulation (FAR) requires every performance-based service contract to include a PWS, together with measurable performance standards, the method the government will use to assess the contractor against them, and performance incentives where appropriate.[^s2] For a Salesforce partner selling implementation, development or managed services to a federal agency, the PWS plays the role that a commercial statement of work plays elsewhere, but it is written around outcomes rather than tasks and hours.[^s1]

## How a PWS is written

FAR 37.602 tells agencies, to the maximum extent practicable, to describe the work in terms of the results required rather than how it should be done or how many hours it will take. The same section asks that performance be assessable against measurable standards, and that agencies rely on those standards and financial incentives in a competitive environment to drive results.[^s1] Each incentive must correspond to a performance standard.[^s2]

There are two routes to a PWS. The government can write it itself, or it can publish a **statement of objectives (SOO)** and let each offeror propose its own PWS in response.[^s1] An SOO must at least state the purpose, the scope or mission, the period and place of performance, background, the performance objectives, and any operating constraints. Offerors build their PWS from it, but the SOO itself is not incorporated into the contract.[^s1] Solicitations may use either a PWS or an SOO.[^s2]

The FAR prescribes no mandatory format for either document.[^s3] Defense Department services guidance recommends building a requirements roadmap first. That roadmap links high-level objectives to tasks, each task to a performance standard and an acceptable quality level (AQL), and each standard to a way of inspecting it. If a standard cannot be inspected, the guidance treats that as a defect in the requirement.[^s3] Its PWS checklist asks, among other things, whether the document avoids dictating contractor headcount, whether AQLs are clearly defined, and whether commercial performance standards are used where they exist.[^s3] Standards should express how fast, how thorough or how error-free the work must be, and should not be overstated.[^s3]

## Surveillance: the QASP

The PWS says what must be achieved; the **quality assurance surveillance plan (QASP)** says how the government will check it. GSA's template describes the QASP as a means of evaluating whether the contractor meets the standards or quality levels in the PWS, and makes its statement of need match the PWS.[^s4] The contractor's own quality-control program remains the primary control, while the government monitors through the QASP.[^s4] The QASP is a living document and not a formal part of the contract; if the two conflict, the contract governs.[^s4]

The core of the QASP is a performance requirements summary listing, for each task, the standard, the AQL, the surveillance method and its frequency.[^s4] GSA warns against setting perfection as the standard except where perfection is truly required.[^s4] Surveillance methods named in DoD guidance include metrics, random sampling, periodic or full inspection, customer feedback and third-party audits.[^s3]

## Gotchas for Salesforce projects

- Writing Salesforce work as "configure 40 objects and 25 flows" turns a PWS back into a task list; frame it as results such as case resolution times or adoption.[^s1]
- Every outcome needs a measurable, inspectable standard and AQL; non-functional targets such as availability or page performance fit naturally here.[^s3]
- When responding to an SOO, the partner's proposed PWS becomes the binding scope, so its assumptions carry contractual weight.[^s1]
- Incentives must map to specific standards, so vague success criteria cannot carry an incentive.[^s2]

The provisions above are cited as published on Acquisition.gov under Federal Acquisition Circular 2026-01; check the live FAR text before relying on a section number, because the regulation is amended through new circulars.[^s1]

## Connections

A PWS **contrasts with** `kt:statement-of-work`: a commercial SOW usually fixes deliverables, approach and effort, while a PWS fixes results and how they are measured.[^s1] It **depends on** `kt:statement-of-objectives` when the agency chooses the SOO route and offerors write the PWS.[^s1] It **has part** `kt:quality-assurance-surveillance-plan`, the surveillance companion that turns its standards into inspections.[^s4] It sits under `kt:federal-acquisition-regulation`, specifically Subpart 37.6.[^s2] Its outcome-based standards draw on the same discipline as `kt:non-functional-requirements`, and its acceptance checks overlap with `kt:user-acceptance-testing`.[^s3] Federal Salesforce programs on `kt:public-sector-solutions` are usually bought this way, and the system the contractor delivers must still obtain its own `kt:authority-to-operate`. A PWS also feeds `kt:requirements-gathering` with the objectives the delivery team must trace back to.[^s3]

## Sources
[^s1]: U.S. GSA (Acquisition.gov), "FAR 37.602 Performance work statement". https://www.acquisition.gov/far/37.602 (accessed 2026-11-22)
[^s2]: U.S. GSA (Acquisition.gov), "FAR 37.601 General". https://www.acquisition.gov/far/37.601 (accessed 2026-11-22)
[^s3]: Defense Acquisition University, "Acquisition of Services — Step 4: Requirements Definition". https://aaf.dau.edu/aaf/services/step4 (accessed 2026-11-22)
[^s4]: U.S. GSA Assisted Acquisition Services, "AAS Quality Assurance Surveillance Plan (QASP) Template". https://aas.gsa.gov/assets/pdf_docs/QASP_Template_FINAL_19Sep22.pdf (accessed 2026-11-22)
