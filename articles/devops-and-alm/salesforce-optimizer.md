---
id: kt:salesforce-optimizer
type: Tool
title: Salesforce Optimizer
aliases: [Optimizer, Optimizer app, Salesforce Optimizer Report, Optimizer Report]
domain: devops-and-alm
summary: >-
  A free, built-in Setup tool that scanned an org's configuration against 50+ metrics (fields, code, automation,
  limits, admins) and listed findings with recommended actions; Salesforce retired it starting in Winter '26, and
  the Admins blog points teams to the Salesforce Labs tool Org Check instead.
release: "Winter '27"
status: retired
broader: [kt:application-lifecycle-management]
related: [kt:technical-debt-in-salesforce, kt:custom-fields, kt:apex-triggers, kt:hyperforce]
relations:
  - {predicate: replacedBy, object: kt:org-check}
  - {predicate: dependsOn, object: kt:governor-limits}
sources:
  - id: s1
    title: "Salesforce Optimizer: Get Started with Salesforce Optimizer"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/modules/salesforce-optimizer/units/get-started-with-salesforce-optimizer
    type: official-learning
    accessed: 2026-11-11
  - id: s2
    title: "Salesforce Optimizer: Run a Report and Review the Findings"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce-optimizer/run-a-report-and-review-the-findings
    type: official-learning
    accessed: 2026-11-11
  - id: s3
    title: "OrgMetricScanResult (Object Reference for the Salesforce Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_orgmetricscanresult.htm
    type: official-docs
    accessed: 2026-11-11
  - id: s4
    title: "Optimizer Is Sunsetting: Learn How To Use Org Check"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2025/optimizer-is-sunsetting-learn-how-to-use-org-check-kate-clicks-through-it
    type: official-blog
    accessed: 2026-11-11
  - id: s5
    title: "Salesforce Optimizer retirement announcement (Communications & Readiness Connect group)"
    publisher: Trailblazer Community
    url: https://trailhead.salesforce.com/trailblazer-community/feed/0D5KX00000mlut50AA
    type: community
    accessed: 2026-11-11
created: 2026-11-11
---

# Salesforce Optimizer

**Salesforce Optimizer** was a free tool, built into Setup, that took a point-in-time snapshot of an org's configuration and looked for likely problems in how it was set up.[^s1] It checked more than 50 metrics. For each one it reported what it found, what to do about it, and where to learn more.[^s1] It ran in Professional, Enterprise, Performance, Unlimited and Developer Editions, in both production and sandbox orgs.[^s2] Salesforce has since **retired** the app, so this node mainly helps you read older guidance and plan replacement org-health checks.[^s4][^s5]

## What it checked

Trailhead groups Optimizer's coverage into a few broad areas:[^s1]

- **Storage and fields**: storage use, custom fields, and fields that were candidates for cleanup.[^s1]
- **Code and UI**: Apex and other custom code, custom page layouts, reports and dashboards.[^s1]
- **Automation and access**: workflow rules and user profiles, plus governor limits the org was close to hitting.[^s1]
- **Lightning readiness and adoption**: unused setup to review before moving to Lightning Experience, and new features users could benefit from.[^s1]

The findings were specific. Objects with more than 350 fields were flagged, and so were objects close to the custom field limit. A field-usage view showed whether fields actually held data.[^s2] Optimizer also warned when one object had too much sharing, flow or validation-rule automation, since that can slow saves.[^s2] It counted users with both Modify All Data and Customize Application as admins and flagged orgs with too many of them.[^s2] It also flagged objects with more than one Apex trigger, in line with the one-trigger-per-object practice.[^s2]

## How it worked

An admin opened **Optimizer** from Setup Quick Find, clicked **Allow Access**, accepted the attestation, and then launched the Optimizer app and clicked **Run Optimizer**. A scan usually finished within an hour and could take longer in complex orgs.[^s2] Results showed up as a list sorted by status, with *Review Required* items at the top. Each row opened a detail view with scan results, recommended actions, learning links, and a button that went straight to the matching Setup page.[^s2] Many teams ran it on a regular schedule so they could compare results over time.[^s2]

Behind the app, scan findings were stored as platform data. The `OrgMetricScanResult` object, available from API version 47.0, holds one item from a feature's results in an Optimizer evaluation, such as an object that is near its custom field limit.[^s3]

## Retirement

A Salesforce communications post set out a staged retirement. Orgs created after August 4, 2025 could not use Optimizer. Hyperforce orgs lost it with Winter '26. Non-Hyperforce orgs kept only the hard-coded URL detection feature, which matters for migrations, until Summer '26.[^s5] The Salesforce Admins blog, writing in August 2025, likewise said Optimizer was retiring in Winter '26 and urged admins to set up a new tool for analyzing their orgs.[^s4]

## Alternatives and gotchas

- **Org Check**: the Admins blog suggests this free Salesforce Labs app in place of Optimizer for finding metadata issues and cutting technical debt.[^s4] It is a Salesforce Labs product rather than a feature built into Setup.[^s4]
- **Old runbooks**: since the app is gone, maintenance checklists that say to run the Optimizer report each month need a new tool.[^s4][^s5]
- **Scope**: Optimizer looked at deployed configuration, not source code. Static analysis in the delivery pipeline was always a separate step.[^s1][^s2]

## Connections

Optimizer sits **under** `kt:application-lifecycle-management` as an org-health and cleanup tool.[^s1] It is **replaced by** `kt:org-check`, the Labs tool Salesforce's Admins blog recommends.[^s4] It **depends on** `kt:governor-limits`, since several metrics reported how close the org was to its limits.[^s1] It is **related** to `kt:technical-debt-in-salesforce`, which its findings made visible, and to `kt:custom-fields` and `kt:apex-triggers`, which were common subjects of its checks.[^s2] It is related to `kt:hyperforce`, whose orgs were the first to lose the app.[^s5]

## Sources
[^s1]: Trailhead, "Salesforce Optimizer: Get Started with Salesforce Optimizer". https://trailhead.salesforce.com/en/modules/salesforce-optimizer/units/get-started-with-salesforce-optimizer (accessed 2026-11-11)
[^s2]: Trailhead, "Salesforce Optimizer: Run a Report and Review the Findings". https://trailhead.salesforce.com/content/learn/modules/salesforce-optimizer/run-a-report-and-review-the-findings (accessed 2026-11-11)
[^s3]: Salesforce Developers, "OrgMetricScanResult", Object Reference for the Salesforce Platform. https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_orgmetricscanresult.htm (accessed 2026-11-11)
[^s4]: Salesforce Admins Blog, "Optimizer Is Sunsetting: Learn How To Use Org Check" (Kate Lessard, August 5, 2025). https://admin.salesforce.com/blog/2025/optimizer-is-sunsetting-learn-how-to-use-org-check-kate-clicks-through-it (accessed 2026-11-11)
[^s5]: Trailblazer Community, Salesforce Optimizer retirement post (Communications & Readiness Connect group). https://trailhead.salesforce.com/trailblazer-community/feed/0D5KX00000mlut50AA (accessed 2026-11-11)
