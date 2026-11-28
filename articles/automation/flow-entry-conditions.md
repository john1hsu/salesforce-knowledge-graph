---
id: kt:flow-entry-conditions
type: Feature
title: Flow Entry Conditions
aliases: [record-triggered flow entry conditions, start element conditions, flow entry criteria, condition requirements to execute outcome]
domain: automation
summary: >-
  The filter on a record-triggered flow's Start element (field conditions, condition logic or a formula,
  plus the "when to run for updated records" choice) that decides whether a record save launches the flow at all.
release: "Winter '27"
status: current
broader: [kt:record-triggered-flow, kt:flow-builder]
related: [kt:flow-formula-resources, kt:scheduled-paths, kt:flow-bulkification, kt:flow-decision-element, kt:flow-debugging]
relations:
  - {predicate: partOf, object: kt:record-triggered-flow}
  - {predicate: alternativeTo, object: kt:flow-decision-element}
  - {predicate: dependsOn, object: kt:order-of-execution}
  - {predicate: contrastsWith, object: kt:process-builder}
sources:
  - id: s1
    title: "Build a Record-Triggered Flow (Record-Triggered Flows module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/build-a-record-triggered-flow
    type: official-learning
    accessed: 2026-11-28
  - id: s2
    title: "Get Started with Triggered Flows (Record-Triggered Flows module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/get-started-with-triggered-flows
    type: official-learning
    accessed: 2026-11-28
  - id: s3
    title: "Record-Triggered Automation (Platform Decision Guides)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered
    type: official-docs
    accessed: 2026-11-28
  - id: s4
    title: "Automate This! — Use Formulas in Record-Triggered Flows with Aleksandra Radovanovic"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2022/automate-this-use-formulas-in-record-triggered-flows-with-aleksandra-radovanovic
    type: official-blog
    accessed: 2026-11-28
  - id: s5
    title: "Automate This! — Designing Record-Triggered Flows"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2022/automate-this-designing-record-triggered-flows
    type: official-blog
    accessed: 2026-11-28
  - id: s6
    title: "What Is a Record-Triggered Flow?"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2023/what-is-a-record-triggered-flow
    type: official-blog
    accessed: 2026-11-28
  - id: s7
    title: "Record-Triggered Automation Guide (trigger automation decision guide)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/decision-guides/trigger-automation
    type: official-docs
    accessed: 2026-11-28
created: 2026-11-28
---

# Flow Entry Conditions

**Entry conditions** are the filter configured on the Start element of a record-triggered flow. After the admin picks the object and the trigger (for example, a record is created or updated), the entry conditions decide whether a particular save launches the flow at all. A record that fails them never starts a flow interview, so none of the flow's elements run.[^s1][^s6] Salesforce product managers sum up the design principle by saying the fastest flow is one that never has to run.[^s5]

## How it works

The trigger choices on the Start element are: only when a record is created, anytime a record is updated, anytime a record is created or updated, and only when a record is deleted.[^s2] Entry conditions are then built from field conditions on the triggering record. Trailhead's worked example uses "All Conditions Are Met (AND)" with two rows, an Opportunity Stage that equals Closed Won and an Amount greater than 25,000.[^s1] Conditions can also check whether a field has changed. The Admins blog shows an Account flow that runs only when the status field is changed and set to Inactive, so ordinary edits to the account don't launch it.[^s6]

Since Summer '22, a **formula** can serve as the entry condition. It uses the same formula builder as formula fields, validation rules and flow formula resources, so syntax errors show up while the flow is being built. The formula can traverse relationships from the triggering record and must return true or false.[^s4] The triggering record is available as the `$Record` global variable, for example `$Record.Account.Name`.[^s6][^s4]

For update triggers, the admin also chooses **when to run the flow for updated records**. With "Only when a record is updated to meet the condition requirements," the flow fires only when a record goes from not meeting the conditions to meeting them. Without it, every later edit to a record that still qualifies runs the flow again. In Trailhead's example, that would create a duplicate contract each time someone edited a Closed Won opportunity.[^s1] Salesforce's decision guide notes that running only on this transition also helps guard against unwanted recursion.[^s3]

## Performance

Entry conditions are the main performance lever for record-triggered automation. A flow that runs on every create or update of an object puts unnecessary load on each save. Admin guidance therefore recommends tight entry conditions, so a flow is called only when a relevant change happens, rather than launching it and filtering later.[^s5] Salesforce's architects add that entry conditions which exclude a flow from a record edit can greatly reduce its performance cost.[^s7] Salesforce's architect guide treats Flow as the recommended low-code tool for most record-triggered work. It recommends Apex instead for high-volume bulk processing and for objects that carry a high density of automation.[^s3] Pairing entry conditions with the before-save **Fast Field Updates** option, which updates the triggering record before it is saved and has minimal database impact, gives the cheapest same-record automation.[^s2][^s1]

## Limits and gotchas

- A flow formula, including a formula entry condition, can contain up to 3,900 characters.[^s4]
- If "only when updated to meet the condition requirements" is not selected, edits to qualifying records re-run the flow and repeat its side effects.[^s1]
- The Debug dialog can skip start condition requirements and can run the flow as if the record were created or updated. Turn that skip off to test the real filter.[^s1]
- Change Data Capture events don't carry the record's prior state, so logic that depends on a state transition is hard to move to CDC and stays in triggered automation.[^s3]

## When to use it (and when not)

Use entry conditions for any rule that decides whether a flow should run at all. Use a **Decision** element inside the flow only for branching after it has started: by then the flow has already started, and that initialization cost is lower than Process Builder's but not zero.[^s5][^s7] When many conditions on one object start to overlap, the architect guide's density thresholds suggest moving to Flow with invocable Apex, or to an Apex trigger framework.[^s3]

## Connections

Entry conditions are part of the **record-triggered flow** Start element in **Flow Builder**.[^s1] Formula entry conditions share syntax with **flow formula resources**.[^s4] The "only when updated to meet the condition requirements" option governs re-runs, and it matters most for flows with **scheduled paths**, which are cancelled and rescheduled when the record changes.[^s3] Entry conditions are an **alternative to** filtering with a **Decision element**, and they are a key technique in **flow bulkification** and performance work.[^s5] They fire within the save **order of execution**, which is why tight filters reduce the cost of every save.[^s3] They also contrast with **Process Builder**, which had no entry conditions and a higher initialization cost.[^s7] To test them, use **flow debugging** with the start-condition skip turned off.[^s1]

## Sources

[^s1]: Trailhead, "Build a Record-Triggered Flow". https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/build-a-record-triggered-flow (accessed 2026-11-28)
[^s2]: Trailhead, "Get Started with Triggered Flows". https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/get-started-with-triggered-flows (accessed 2026-11-28)
[^s3]: Salesforce Architects, "Record-Triggered Automation" decision guide. https://architect.salesforce.com/docs/architect/decision-guides/guide/record-triggered (accessed 2026-11-28)
[^s4]: Salesforce Admins, "Automate This! — Use Formulas in Record-Triggered Flows". https://admin.salesforce.com/blog/2022/automate-this-use-formulas-in-record-triggered-flows-with-aleksandra-radovanovic (accessed 2026-11-28)
[^s5]: Salesforce Admins, "Automate This! — Designing Record-Triggered Flows". https://admin.salesforce.com/blog/2022/automate-this-designing-record-triggered-flows (accessed 2026-11-28)
[^s6]: Salesforce Admins, "What Is a Record-Triggered Flow?". https://admin.salesforce.com/blog/2023/what-is-a-record-triggered-flow (accessed 2026-11-28)
[^s7]: Salesforce Architects, "Record-Triggered Automation Guide". https://architect.salesforce.com/decision-guides/trigger-automation (accessed 2026-11-28)
