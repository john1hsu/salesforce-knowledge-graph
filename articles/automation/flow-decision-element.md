---
id: kt:flow-decision-element
type: Feature
title: Decision Element
aliases: [Flow Decision element, Decision element in Flow, Flow Builder Decision, flow decision outcomes, flow branching logic]
domain: automation
summary: >-
  The Flow Builder logic element that branches a flow into outcomes: it evaluates each outcome's condition
  requirements in a set order, follows the first outcome whose conditions are met, and falls back to a default
  outcome when none match.
release: "Winter '27"
status: current
broader: [kt:flow-builder]
related: [kt:record-triggered-flow, kt:get-records-element, kt:flow-loop-element, kt:screen-flow, kt:flow-assignment-element]
relations:
  - {predicate: dependsOn, object: kt:flow-formula-resources}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: alternativeTo, object: kt:business-rules-engine}
  - {predicate: governedBy, object: kt:flow-limits}
sources:
  - id: s1
    title: "Define Multiple Paths in a Flow (Improve Your Salesforce Flow with Branching Logic)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/flow-build-logic/define-multiple-paths-in-a-flow
    type: official-learning
    accessed: 2026-11-25
  - id: s2
    title: "Build Logic to Determine the Right Discount to Apply"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/flow_calculate/flow_calculate_determine
    type: official-learning
    accessed: 2026-11-25
  - id: s3
    title: "Create Branching with Decision Elements (Optimize Campaign Flows with Decision Elements)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/campaign-optimization-with-flows-in-marketing-cloud-next/create-branching-with-decision-elements
    type: official-learning
    accessed: 2026-11-25
  - id: s4
    title: "The Ultimate Guide to Flow Best Practices and Standards"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2021/the-ultimate-guide-to-flow-best-practices-and-standards
    type: official-blog
    accessed: 2026-11-25
  - id: s5
    title: "Flow (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-flow.html
    type: official-docs
    accessed: 2026-11-25
  - id: s6
    title: "Build a Record-Triggered Flow"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/build-a-record-triggered-flow
    type: official-learning
    accessed: 2026-11-25
created: 2026-11-25
---

# Decision Element

The **Decision** element is how a flow chooses between paths. It holds a list of **outcomes**, and each outcome becomes its own branch on the Flow Builder canvas.[^s1] Every outcome except the last carries condition requirements; the last one is the **default outcome**, which has no conditions and runs when none of the others match.[^s1] The element is available in every flow type, from record-triggered flows to screen flows, and Salesforce also uses it in Marketing Cloud Next campaign flows to split an audience into groups.[^s3]

## How it works

When a flow interview reaches a Decision, it checks the outcomes in the sequence shown under **Outcome Order**. If the first outcome's conditions are met, the flow takes that path; otherwise it moves to the next outcome, and so on. If nothing matches, it takes the default path.[^s1] Only one path runs: the first match wins, even if a later outcome would also have been true.[^s3]

Each condition is a row of **Resource**, **Operator** and **Value**, for example a triggering record's field, an operator such as Equals, Does Not Equal, Greater Than or Is Null, and a literal or another resource.[^s3] An outcome with several rows needs a condition requirement: Flow Builder applies **All Conditions Are Met (AND)** when you add a condition, and you can switch to any-condition (OR) or custom logic.[^s2][^s5] Conditions can reference fields on related records, such as a case's contact, and formula resources, such as a date computed with `TODAY()`.[^s1][^s3]

Trailhead's case-triage example shows why order matters. Its Severity 1 outcome requires a Usability case type and a VIP contact, while Severity 2 requires only the Usability type. Because Severity 1 is checked first, Severity 2 effectively catches the non-VIP usability cases without restating the VIP check.[^s1] A discount example works the same way: a Full Discount outcome for annual revenue above 200,000,000, a Partial Discount outcome for revenue from 100,000,000 to 200,000,000, and No Discount as the default.[^s2]

In metadata, a flow stores its decisions as an array of decision nodes. Each decision has a list of rules, which Flow Builder shows as outcomes, and a default connector to the node that runs when no rule is true.[^s5] A rule records its condition logic, its conditions and its connector, and record-triggered flows can mark a rule so that it counts as met only when the record changes to meet the conditions.[^s5] The Start element of a record-triggered flow has a similar setting for the whole flow: run only when a record is updated to meet the condition requirements, which stops repeated actions on later edits.[^s6]

## Limits and gotchas

- Always add a Decision right after a Get Records element whose result you'll use later, checking Is Empty or Is Blank equals False, the flow version of a null check.[^s4]
- Some components return an empty collection rather than null, so the Salesforce Admins guide recommends Is Empty, which covers both cases.[^s4]
- A Decision inside a loop counts as an element execution on every pass, and general governor limits still apply to the flow's transaction.[^s4]
- Avoid hard-coding values that change, such as queue IDs, owner IDs or discount percentages, in outcome conditions; store them in custom labels or custom metadata.[^s4]
- Put the most specific outcome first. Outcomes are evaluated in order, so a broad outcome placed early hides the narrower ones below it.[^s1][^s3]

## When to use it (and when not)

Use a Decision when different records or users need different actions. If a condition decides whether the flow should run at all, put it in the record-triggered flow's entry criteria instead, so the automation doesn't start for changes it will ignore.[^s4][^s6] When a decision exists only to pick a value, such as a discount percentage, one formula resource and one Assignment can sometimes replace several outcomes. Decisions whose rules change often, or that business users must maintain as lookup tables, fit better in custom metadata or a dedicated rules engine.[^s2][^s4]

## Connections

The Decision element is a core logic element of **Flow Builder** and works with the other elements around it: it guards the output of **Get Records**, it often follows a **Loop** or sits inside one, and its outcomes usually lead to **Assignment** or data elements.[^s1][^s2][^s4] It **depends on** **flow formula resources** when a condition needs a calculated value, and it is common in **record-triggered** and **screen** flows.[^s3][^s6] Each decision is stored as a FlowDecision node, so it is **configured via** the **Metadata API** when flows are deployed.[^s5] For decision tables maintained outside a flow, the **Business Rules Engine** is the **alternative**. Element executions inside loops count against **flow limits**.[^s4]

## Sources
[^s1]: Trailhead, "Define Multiple Paths in a Flow (Improve Your Salesforce Flow with Branching Logic)". https://trailhead.salesforce.com/content/learn/modules/flow-build-logic/define-multiple-paths-in-a-flow (accessed 2026-11-25)
[^s2]: Trailhead, "Build Logic to Determine the Right Discount to Apply". https://trailhead.salesforce.com/content/learn/projects/flow_calculate/flow_calculate_determine (accessed 2026-11-25)
[^s3]: Trailhead, "Create Branching with Decision Elements (Optimize Campaign Flows with Decision Elements)". https://trailhead.salesforce.com/content/learn/modules/campaign-optimization-with-flows-in-marketing-cloud-next/create-branching-with-decision-elements (accessed 2026-11-25)
[^s4]: Salesforce Admins Blog, "The Ultimate Guide to Flow Best Practices and Standards". https://admin.salesforce.com/blog/2021/the-ultimate-guide-to-flow-best-practices-and-standards (accessed 2026-11-25)
[^s5]: Salesforce Developers, "Flow (Metadata API Developer Guide)". https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-flow.html (accessed 2026-11-25)
[^s6]: Trailhead, "Build a Record-Triggered Flow". https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/build-a-record-triggered-flow (accessed 2026-11-25)
