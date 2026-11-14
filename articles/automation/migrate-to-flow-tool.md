---
id: kt:migrate-to-flow-tool
type: Tool
title: Migrate to Flow Tool
aliases: [Migrate to Flow, Migrate to Flow (Beta), Migrate to Flow setup page, workflow-to-flow migration tool, process-to-flow migration tool]
domain: automation
summary: >-
  A Setup page that converts legacy workflow rules and record-change Process Builder processes into
  record-triggered flows, creating each flow inactive so it can be tested in Flow Builder before the old
  automation is switched off; some actions convert only partially and others not at all.
release: "Winter '27"
status: current
broader: [kt:process-automation, kt:flow-builder]
related: [kt:workflow-rules, kt:process-builder, kt:flow-trigger-explorer, kt:subflows, kt:technical-debt-in-salesforce]
relations:
  - {predicate: enables, object: kt:record-triggered-flow}
sources:
  - id: s1
    title: "Migrate Workflows and Processes to Flows: Understand Automation Changes"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/migrate-workflows-and-processes-to-flows/understand-automation-changes
    type: official-learning
    accessed: 2026-11-14
  - id: s2
    title: "Migrate Workflows and Processes to Flows: Migrate a Workflow Rule"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/migrate-workflows-and-processes-to-flows/migrate-a-workflow-rule
    type: official-learning
    accessed: 2026-11-14
  - id: s3
    title: "Migrate Workflows and Processes to Flows: Migrate a Process"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/migrate-workflows-and-processes-to-flows/migrate-a-process
    type: official-learning
    accessed: 2026-11-14
  - id: s4
    title: "Automate This! Migrate Workflow Rules and Processes to Flow"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2022/automate-this-migrate-workflow-rules-and-processes-to-flow
    type: official-blog
    accessed: 2026-11-14
  - id: s5
    title: "Migrate to Flow Tool (Beta)"
    publisher: Salesforce Time
    url: https://salesforcetime.com/2022/03/17/migrate-to-flow-tool-beta/
    type: community
    accessed: 2026-11-14
created: 2026-11-14
---

# Migrate to Flow Tool

**Migrate to Flow** is a Setup page, found through Quick Find, that lists an org's workflow rules and Process Builder processes and generates an equivalent record-triggered flow for the one an admin selects.[^s2][^s3] It is Salesforce's built-in on-ramp for retiring the two legacy automation tools, which the Trailhead project on the subject now describes as disabled, in favour of Flow Builder.[^s1] The tool produces a working first draft rather than a finished design: Salesforce's own admin team called it a starting point with limitations.[^s4]

## History

The page first shipped as a beta around Spring '22 and handled workflow rules only, converting active and inactive rules alike; process support was promised for a later release at that time.[^s5][^s4] Process conversion arrived with the Spring '23 release, and the tool later gained partial migration for most process actions.[^s1]

## How it works

For a **workflow rule**, the admin selects the rule and clicks **Migrate to Flow**. A Migration details window then offers **Test in Flow Builder** and **Switch Activations**; the latter deactivates the rule and activates the new flow in one step, so both never run side by side.[^s2][^s4] Until that switch, the generated flow sits inactive and the rule keeps running.[^s5] When a rule only updates fields on the triggering record, the tool optimizes the flow for **Fast Field Updates** (a before-save flow); rules with email alerts, outbound messages or time-dependent actions become after-save flows.[^s1][^s5]

For a **process**, the admin can migrate all of its criteria to one flow or pick individual criteria (the diamonds on the Process Builder canvas) and send them to separate flows.[^s3] The Next Steps window has no Switch Activations button here: the admin opens the flow, saves and activates it, then deactivates the process in Process Builder by hand.[^s3] Migrated processes are generated with the Actions and Related Records optimization, and the Trailhead walkthrough switches a flow that only touches the triggering record to Fast Field Updates before activating.[^s1][^s3] An invoke-flow action becomes a subflow element running in the parent flow's transaction.[^s1]

## Limits and gotchas

- Workflow rules using tasks, related-record or global-variable fields, record types, relative dates or multiple currencies may not appear on the page at all.[^s1]
- Unsupported operators and functions also hide a rule, for example Includes, Excludes, Within, or formulas using ISCLONE, TIMENOW or $RecordType.[^s1]
- Process support covers record-change processes whose actions create or update records, invoke a flow or Apex, or send an email alert.[^s1]
- Processes started by a platform event or by another process, scheduled actions and field traversals are not supported.[^s1]
- Invocable actions cannot be migrated even partially; other partially migrated actions are flagged in the results for finishing in Flow Builder.[^s1]
- Recursive processes could evaluate a record up to six times per save, but a migrated flow evaluates it once, so behaviour can change silently.[^s1]
- Invoked flows that make callouts, call external actions or pause should be redesigned onto an asynchronous path after conversion.[^s1]
- In the beta, re-migrating a rule created a brand-new flow rather than a new version, leaving stale flows to delete by hand.[^s5]

Execution timing can also differ from the legacy automation, so admins should set trigger order explicitly in Flow Trigger Explorer.[^s1]

## When to use it (and when not)

Use the tool to speed up the mechanical part of migration, ideally in a sandbox or scratch org, never debugging against live production data.[^s1][^s3] Do not accept its default one-flow-per-rule output blindly. Salesforce's admin guidance is to map the business process first, delete rules that are inactive or obsolete instead of migrating them, and consolidate related logic into fewer flows using Decision elements.[^s4] The same guidance asks admins to add fault paths and tests and to swap hard-coded IDs for custom labels, custom settings or custom metadata while the flow is open.[^s4] Anything the page refuses to list has to be rebuilt by hand in Flow Builder.[^s1]

## Connections

The tool sits **under process automation** and **Flow Builder**, where every generated flow is reviewed and activated.[^s2] It is **related to workflow rules and Process Builder**, whose definitions it reads, and **enables record-triggered flows**, its only output type.[^s1] Ordering the converted flows is the job of **Flow Trigger Explorer**, and invoke-flow actions land as **subflows**.[^s1] Salesforce's advice to build tests and work in sandboxes before activating applies to every flow it generates, and unmigrated legacy automation is a classic **technical-debt** item.[^s4][^s3]

## Sources
[^s1]: Trailhead, "Migrate Workflows and Processes to Flows: Understand Automation Changes". https://trailhead.salesforce.com/content/learn/projects/migrate-workflows-and-processes-to-flows/understand-automation-changes (accessed 2026-11-14)
[^s2]: Trailhead, "Migrate Workflows and Processes to Flows: Migrate a Workflow Rule". https://trailhead.salesforce.com/content/learn/projects/migrate-workflows-and-processes-to-flows/migrate-a-workflow-rule (accessed 2026-11-14)
[^s3]: Trailhead, "Migrate Workflows and Processes to Flows: Migrate a Process". https://trailhead.salesforce.com/content/learn/projects/migrate-workflows-and-processes-to-flows/migrate-a-process (accessed 2026-11-14)
[^s4]: Salesforce Admins Blog, "Automate This! Migrate Workflow Rules and Processes to Flow". https://admin.salesforce.com/blog/2022/automate-this-migrate-workflow-rules-and-processes-to-flow (accessed 2026-11-14)
[^s5]: Salesforce Time, "Migrate to Flow Tool (Beta)". https://salesforcetime.com/2022/03/17/migrate-to-flow-tool-beta/ (accessed 2026-11-14)
