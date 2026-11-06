---
id: kt:assignment-rules
type: Feature
title: Assignment Rules
aliases: [Lead Assignment Rules, Case Assignment Rules, lead assignment rule, case assignment rule]
domain: automation
summary: >-
  Declarative rules that set the owner of new or updated leads and cases by evaluating ordered rule
  entries and assigning the record to the first matching user or queue.
release: "Winter '27"
status: current
broader: [kt:process-automation]
related: [kt:order-of-execution, kt:sales-cloud, kt:service-cloud, kt:apex]
relations:
  - {predicate: integratesWith, object: kt:queues}
  - {predicate: alternativeTo, object: kt:omni-channel}
  - {predicate: contrastsWith, object: kt:enterprise-territory-management}
sources:
  - id: s1
    title: "Set Up Assignment Rules"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&amp=&id=creating_assignment_rules.htm&type=5
    type: official-docs
    accessed: 2026-11-06
  - id: s2
    title: "Guidelines for Assignment Rules"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.customize_leadrules.htm&type=5&language=en_US
    type: official-docs
    accessed: 2026-11-06
  - id: s3
    title: "DmlOptions.AssignmentRuleHeader Class"
    publisher: Salesforce Developers (Apex Reference Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_class_Database_AssignmentRuleHeader.htm
    type: official-docs
    accessed: 2026-11-06
  - id: s4
    title: "Triggers and Order of Execution"
    publisher: Salesforce Developers (Apex Developer Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm
    type: official-docs
    accessed: 2026-11-06
  - id: s5
    title: "Customize an Org to Support a New Business Unit: Automate Your Business Process"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/customize-an-org-to-support-a-new-business-unit/automate-your-business-process
    type: official-learning
    accessed: 2026-11-06
  - id: s6
    title: "How to Set the Option 'Assign using active assignment rules' to True, Only When a Case or Lead is Created"
    publisher: Salesforce Help (Knowledge Article 000386582)
    url: https://help.salesforce.com/s/articleView?id=000386582&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-06
created: 2026-11-06
---

# Assignment Rules

Assignment rules are Salesforce's built-in, declarative way to decide who owns a new **lead** or **case**. An admin defines a rule made of ordered entries; each entry pairs conditions with an assignee, and the platform gives the record to the user or queue of the first entry that matches.[^s1] Trailhead describes them as the conditions that determine how leads or cases are processed, using the example of routing billing cases to a dedicated support queue.[^s5] They are configured in Setup under **Lead Assignment Rules** and **Case Assignment Rules**; viewing them needs the View Setup and Configuration permission and changing them needs Customize Application.[^s1][^s2]

## How it works

Each object can hold several rules, but only one lead rule and one case rule can be active at a time. Teams commonly keep alternates, such as a holiday or shutdown case rule, inactive and switch to them temporarily.[^s2] Every rule contains **rule entries** evaluated in their sort order. Evaluation stops at the first match, so the order is the logic.[^s1] An entry's condition is either a set of filter criteria (up to 25, each up to 255 characters) or a formula that must return true.[^s1] The entry then names:

- **Assignee**: an active user or a queue. A user assignee must have Read access to cases.[^s1]
- **Do Not Reassign Owner**: keeps the current owner when an existing record is re-evaluated on update.[^s1]
- **Email template**: optional notice to the new owner; for a queue it goes to the queue address and its members, and no template means no email.[^s1]
- **Predefined case teams** (cases only), with an option to replace teams already on the case.[^s1]

Lead rules apply to leads created manually, from Web-to-Lead and through the Data Import Wizard. Case rules apply whether a case is created manually or through Web-to-Case, Email-to-Case or portals.[^s2] Records that match no entry fall to a default: the default Web-to-Lead owner, the admin running a lead import, or the default case owner set in Support Settings.[^s1]

In the save sequence, assignment rules run at step 9 of the order of execution, after all `after` triggers and just before auto-response rules, workflow rules, escalation rules and after-save record-triggered flows.[^s4]

## Running rules from code

Apex code chooses explicitly whether a lead or case save runs the rules. `Database.DMLOptions.assignmentRuleHeader` lets a lead or case DML operation run either the default active rule (`useDefaultRule = true`) or a specific rule by `assignmentRuleId`, which may be active or inactive. Set only one of the two properties; a malformed ID throws an exception.[^s3] If the org has no assignment rules, records saved with API version 30.0 or later stay unassigned, while 29.0 and earlier assign a predefined default owner.[^s3]

## Limits and gotchas

- **Entry caps.** A case assignment rule can contain up to 3,000 rule entries, of which up to 300 can be formula entries.[^s2]
- **First match wins.** Put specific entries first and finish with a catch-all entry with no criteria so nothing falls through to a default owner by accident.[^s1]
- **The edit checkbox.** The "Assign using active assignment rules" checkbox runs the rules on create, but if it is shown and selected on edit, saving an edit can reassign the record unexpectedly. Salesforce's workaround uses page layout properties, a temporary record type and a record-triggered flow.[^s6]
- **Recursive saves.** During a recursive save, Salesforce skips steps 9 through 17, so a workflow or flow re-save does not re-run assignment rules.[^s4]
- **Multilingual orgs.** Enter filter values in the org's default language.[^s1]

## When to use it (and when not)

Use assignment rules for simple, attribute-based ownership: region, product, priority or record type sending a record to a team queue. For case visibility in a private sharing model, routing to a queue also controls who can see and take the case.[^s2] Push-based routing by agent availability and capacity is Omni-Channel's job, which works off queued records, and account ownership by geography or segment belongs to territory management rather than lead or case rules. Complex logic such as round-robin, load balancing or lookups to other objects usually moves to Flow or Apex, which can still invoke the rules through DML options.[^s3]

## Connections

Assignment rules are part of Salesforce's **process automation** toolkit and fire at a fixed point in the **order of execution**.[^s4] Their most common target is **queues**, which they integrate with: the rule fills the queue, and queue membership gives a team access.[^s5][^s2] Lead rules are core **Sales Cloud** lead management; case rules are core **Service Cloud** routing.[^s2] **Apex** code opts into them with `AssignmentRuleHeader`.[^s3] **Omni-Channel** is the alternative for capacity-based push routing, and **Enterprise Territory Management**, which assigns accounts rather than leads or cases, is commonly confused with them; Apex's DML options support assignment rules for cases and leads but not accounts.[^s3]

## Sources
[^s1]: Salesforce Help, "Set Up Assignment Rules". https://help.salesforce.com/s/articleView?language=en_US&amp=&id=creating_assignment_rules.htm&type=5 (accessed 2026-11-06)
[^s2]: Salesforce Help, "Guidelines for Assignment Rules". https://help.salesforce.com/s/articleView?id=sf.customize_leadrules.htm&type=5&language=en_US (accessed 2026-11-06)
[^s3]: Salesforce Developers, "DmlOptions.AssignmentRuleHeader Class", Apex Reference Guide. https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexcode/apex_class_Database_AssignmentRuleHeader.htm (accessed 2026-11-06)
[^s4]: Salesforce Developers, "Triggers and Order of Execution", Apex Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm (accessed 2026-11-06)
[^s5]: Trailhead, "Customize an Org to Support a New Business Unit: Automate Your Business Process". https://trailhead.salesforce.com/content/learn/projects/customize-an-org-to-support-a-new-business-unit/automate-your-business-process (accessed 2026-11-06)
[^s6]: Salesforce Help, "How to Set the Option 'Assign using active assignment rules' to True, Only When a Case or Lead is Created in Salesforce" (Knowledge Article 000386582). https://help.salesforce.com/s/articleView?id=000386582&language=en_US&type=1 (accessed 2026-11-06)
