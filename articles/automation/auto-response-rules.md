---
id: kt:auto-response-rules
type: Feature
title: Auto-Response Rules
aliases: [auto-response rule, Case Auto-Response Rules, Lead Auto-Response Rules, autoresponse rules, AutoResponseRules]
domain: automation
summary: >-
  Declarative rules that pick which email template to send automatically to the submitter of a new lead or case,
  using ordered rule entries where the first match wins and only one rule per object is active.
release: "Winter '27"
status: current
broader: [kt:process-automation, kt:service-cloud]
related: [kt:order-of-execution, kt:escalation-rules, kt:email-alerts, kt:sales-cloud]
relations:
  - {predicate: contrastsWith, object: kt:assignment-rules}
  - {predicate: dependsOn, object: kt:email-templates}
  - {predicate: integratesWith, object: kt:web-to-case}
  - {predicate: integratesWith, object: kt:web-to-lead}
  - {predicate: configuredVia, object: kt:metadata-api}
sources:
  - id: s1
    title: "Automate Case Management (Agentforce Service Administration)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/service_lex/units/service_lex_case_manage
    type: official-learning
    accessed: 2026-11-17
  - id: s2
    title: "Case Management Implementation Guide (PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/salesforce_case_implementation_guide.pdf
    type: official-docs
    accessed: 2026-11-17
  - id: s3
    title: "Lead Implementation Guide (PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/salesforce_lead_implementation_guide.pdf
    type: official-docs
    accessed: 2026-11-17
  - id: s4
    title: "AutoResponseRules"
    publisher: Salesforce Developers (Metadata API Developer Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_autoresponserules.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s5
    title: "Triggers and Order of Execution"
    publisher: Salesforce Developers (Apex Developer Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s6
    title: "Setting DML Options"
    publisher: Salesforce Developers (Apex Developer Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/langCon_apex_dml_database_dmloptions.htm
    type: official-docs
    accessed: 2026-11-17
created: 2026-11-17
---

# Auto-Response Rules

Auto-response rules are Salesforce's declarative way to send an automatic, personalized email to the person who submitted a **case** or a **lead**. Each rule entry checks attributes of the incoming record and names the email template to send, so a customer reporting a feature request can get a different acknowledgement than one reporting an outage.[^s1][^s2] On the sales side, the same mechanism lets web-generated leads receive a template about the product they asked about.[^s3] Admins manage them in Setup under **Case Auto-Response Rules** and **Lead Auto-Response Rules**; the feature isn't offered in Group Edition.[^s1][^s3]

## How it works

A rule is a container for ordered **rule entries**. Each entry has a sort order, criteria on the record's fields, a sender name and email address for the From line, and one email template. Salesforce evaluates entries in order and sends the template of the first entry that matches; later entries are ignored.[^s1][^s2][^s3] A common starter entry is "Case Origin equals Email" with a "we received your request" template.[^s1]

Only one auto-response rule can be active per object at a time, and activating a rule deactivates the one that was active before. Variations therefore belong in entries of a single rule, not in separate rules.[^s1][^s2][^s3]

When no entry matches, Web-to-Case and Web-to-Lead fall back to the **default response template** chosen in their settings, which must be marked Available for Use.[^s2][^s3] For Web-to-Lead, the default lead creator also needs the Modify All Data and Send Email permissions, granted through either a profile or a permission set rather than a mix of both.[^s3]

## In the save, in Apex and in metadata

Auto-response rules run at step 10 of the order of execution: after `after` triggers and assignment rules, before workflow rules and escalation rules. During a recursive save Salesforce skips steps 9 through 17, so a record re-saved by automation doesn't send a second auto-response.[^s5]

Records inserted with Apex DML control the email through `Database.DMLOptions.emailHeader`. Its `triggerAutoResponseEmail` flag says whether auto-response rules fire for leads and cases, and Salesforce's own example sets it to `true` explicitly. These header settings apply only to Apex DML, not to saves from the UI.[^s6]

In the Metadata API, rules deploy as the `AutoResponseRules` type, one `.autoResponseRules` file per object (for example `Case.autoResponseRules`). Each rule has an `active` flag and `ruleEntry` items with `criteriaItems` or `formula` (never both), optional `booleanFilter`, `senderName`, `senderEmail`, `replyToEmail` and `template`.[^s4] Salesforce recommends Classic email templates here because Lightning email templates can't be packaged.[^s4]

## Limits and gotchas

- **One active rule.** Turning on a second rule silently switches off the first, so check which rule is active after a deployment.[^s1][^s4]
- **First match wins.** A broad entry placed early swallows cases meant for more specific entries; put specific entries first and a catch-all last.[^s2]
- **Defaults still send.** If no entry matches a Web-to-Case or Web-to-Lead record, the default response template goes out, so it needs to be on-brand and available for use.[^s2][^s3]
- **API and Apex inserts.** Apex callers need the email header set to trigger auto-responses; don't assume integrations send them.[^s6]
- **One shot per save.** The rules run once in the save and are skipped on recursive saves, so they suit "on submission" acknowledgements, not follow-ups.[^s5]

## When to use it (and when not)

Use auto-response rules for the first acknowledgement a customer or prospect sees after submitting a form or email, especially when different case types or lead interests deserve different wording.[^s2][^s3] For internal notifications, use the notification templates on assignment and escalation rules or email alerts, since auto-response rules are aimed at the submitter.[^s1][^s2] Anything conditional on later changes, timing or other objects fits record-triggered flows better.[^s5]

## Connections

Auto-response rules are part of Salesforce's **process automation** toolkit and a core **Service Cloud** case feature, with a lead variant used in **Sales Cloud**.[^s2][^s3] They share the rule-plus-ordered-entries structure of **assignment rules** and **escalation rules** but contrast in purpose: assignment rules pick an owner, escalation rules act on aging cases, and auto-response rules email the customer.[^s1] They run at a fixed point in the **order of execution**, right after assignment rules.[^s5] Every entry depends on an **email template**, and the rules pair naturally with **Web-to-Case** and **Web-to-Lead**, whose default templates cover unmatched submissions.[^s2][^s3] **Email alerts** are the workflow and flow counterpart for other recipients, and the rules deploy through the **Metadata API** as `AutoResponseRules`.[^s4]

## Sources
[^s1]: Trailhead, "Automate Case Management", Agentforce Service Administration module. https://trailhead.salesforce.com/modules/service_lex/units/service_lex_case_manage (accessed 2026-11-17)
[^s2]: Salesforce, "Case Management Implementation Guide" (PDF). https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/salesforce_case_implementation_guide.pdf (accessed 2026-11-17)
[^s3]: Salesforce, "Lead Implementation Guide" (PDF). https://resources.docs.salesforce.com/242/latest/en-us/sfdc/pdf/salesforce_lead_implementation_guide.pdf (accessed 2026-11-17)
[^s4]: Salesforce Developers, "AutoResponseRules", Metadata API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_autoresponserules.htm (accessed 2026-11-17)
[^s5]: Salesforce Developers, "Triggers and Order of Execution", Apex Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm (accessed 2026-11-17)
[^s6]: Salesforce Developers, "Setting DML Options", Apex Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/langCon_apex_dml_database_dmloptions.htm (accessed 2026-11-17)
