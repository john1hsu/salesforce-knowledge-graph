---
id: kt:business-processes
type: Feature
title: Business Processes
aliases: [business process, BusinessProcess, sales process, support process, lead process, solution process]
domain: data-model
summary: >-
  Named subsets of a lifecycle picklist (opportunity Stage, case Status, lead Status or solution Status) that let
  different teams follow different lifecycles on the same object; each is attached to users through a record type.
release: "Winter '27"
status: current
broader: [kt:metadata-driven-architecture]
related: [kt:record-types, kt:page-layouts, kt:path, kt:sales-cloud, kt:service-cloud, kt:lead-conversion]
relations:
  - {predicate: consumedBy, object: kt:record-types}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: contrastsWith, object: kt:process-automation}
  - {predicate: coveredBy, object: kt:platform-administrator-certification}
sources:
  - id: s1
    title: "Metadata API Developer Guide: BusinessProcess"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_businessprocess.htm
    type: official-docs
    accessed: 2026-11-06
  - id: s2
    title: "Tips & Hints for Multiple Business Processes (cheat sheet)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/220/latest/en-us/sfdc/pdf/salesforce_busprocess_cheatsheet.pdf
    type: official-docs
    accessed: 2026-11-06
  - id: s3
    title: "Create a Process for Managing Support Cases: Create Support Processes"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/create-a-process-for-managing-support-cases/create-support-processes
    type: official-learning
    accessed: 2026-11-06
  - id: s4
    title: "Customize a Sales Path for Your Team: Customize a Sales Path"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/projects/customize-a-sales-path-for-your-team/steps/customize-a-sales-path
    type: official-learning
    accessed: 2026-11-06
created: 2026-11-06
---

# Business Processes

A business process in Salesforce is a named selection of values from one of the four standard "lifecycle" picklists, so that different teams can move records through different lifecycles on the same object. Salesforce offers four kinds, each bound to one field: sales processes filter the opportunity Stage picklist, support processes filter case Status, lead processes filter Lead Status, and solution processes filter Solution Status.[^s2] In metadata the type is called `BusinessProcess`, and the Metadata API describes it as the way to show different picklist values to users based on their profile.[^s1] The name is easy to confuse with "process automation" (Flow, approvals, orchestration); a business process automates nothing, it only constrains which lifecycle values are offered.

## How it works

Setup follows a fixed order. First the admin maintains the object's master picklist, which holds every value any process could use. Next the admin creates the business process (Setup, then Sales Processes, Support Processes, Lead Processes or Solution Processes), optionally copying an existing process, and moves values between Available and Selected; lead, support and solution processes also take a default value. Then a record type is created or edited and associated with the process, and finally the record type is assigned to profiles; users only experience the process through a record type they can use.[^s2] Trailhead's support-case project, for example, creates a Product Support Process and an Inquiry Process by starting each from the Master process.[^s3]

A business process cannot be reached by users on its own: each one is assigned to a record type, and the record type decides which profiles get it.[^s1] That makes record types the delivery mechanism and business processes the content. On opportunities, the sales process also shapes Path, the guided stage bar on the record page: Trailhead's sales-path project builds a B2B Sales Process by removing three stages from the master list, links it to a B2B Opportunities record type, and only then customizes the path for that record type.[^s4]

In metadata, business processes are defined inside the object's definition rather than as standalone files. Each has a `fullName`, `description`, `isActive`, an optional `namespacePrefix` and a list of picklist `values`; when retrieving through package.xml the name is qualified with the object, as in `Opportunity.Bulk Orders`. The type has been available since API version 17.0.[^s1]

## Limits and gotchas

- **Master picklist changes don't propagate.** A value added to the master picklist is not added to existing processes or record types; it must be added to each by hand. Removing a master value blocks it on new records, but existing records keep showing it.[^s2]
- **Not a security control.** The Metadata API guide warns against using business processes for access control: profile assignment governs create and edit but not read, so users can still read records whose process their profile cannot create or edit. It also advises against putting sensitive data in process names, descriptions or values.[^s1]
- **Wildcards are constrained.** The `*` wildcard for BusinessProcess in package.xml works only when a RecordType is also specified.[^s1]
- **Who can build them.** Creating business processes needs the "Customize Salesforce" permission.[^s2]
- **Record type prompts.** If a profile has several record types, one must be the default; with only one, users are never prompted to choose.[^s2]

## When to use it (and when not)

Use multiple business processes when teams truly run different lifecycles on one object, such as a short transactional sales cycle beside a long consultative one, or product-support cases beside general inquiries.[^s2][^s3] If the only difference is the fields or layout people see, a record type with its own page layout (or dynamic forms) is enough and no extra process is needed. If the need is to enforce entry criteria between stages, pair the process with validation rules or Flow; the business process itself only filters values.

## Connections

Business processes are part of the metadata-driven model: the same object definition carries several lifecycle variants without code.[^s1] They are consumed through record types, which also pick page layouts and per-record-type picklist values,[^s2] and they feed Path on opportunities.[^s4] The four kinds map to Sales Cloud (sales and lead processes) and Service Cloud (support processes).[^s2][^s3] They are retrieved and deployed through the Metadata API and can be inspected with SOQL against the BusinessProcess object. Configuring them is core Platform Administrator material.

## Sources

[^s1]: Salesforce Developers, "Metadata API Developer Guide: BusinessProcess". https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_businessprocess.htm (accessed 2026-11-06)
[^s2]: Salesforce, "Tips & Hints for Multiple Business Processes (cheat sheet)". https://resources.docs.salesforce.com/220/latest/en-us/sfdc/pdf/salesforce_busprocess_cheatsheet.pdf (accessed 2026-11-06)
[^s3]: Trailhead, "Create a Process for Managing Support Cases: Create Support Processes". https://trailhead.salesforce.com/content/learn/projects/create-a-process-for-managing-support-cases/create-support-processes (accessed 2026-11-06)
[^s4]: Trailhead, "Customize a Sales Path for Your Team: Customize a Sales Path". https://trailhead.salesforce.com/en/projects/customize-a-sales-path-for-your-team/steps/customize-a-sales-path (accessed 2026-11-06)
