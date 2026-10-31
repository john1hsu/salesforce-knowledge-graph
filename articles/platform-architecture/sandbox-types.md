---
id: kt:sandbox-types
type: Feature
title: Sandbox Types
aliases: [Salesforce sandboxes, Developer sandbox, Developer Pro sandbox, Partial Copy sandbox, Full sandbox, Full Copy sandbox, sandbox license types]
domain: platform-architecture
summary: >-
  The four kinds of Salesforce sandbox (Developer, Developer Pro, Partial Copy and Full), which are copies of a
  production org that differ in how much data they receive, how much storage they get, how often they can be
  refreshed and what they cost.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:application-lifecycle-management, kt:change-sets, kt:devops-center]
relations:
  - {predicate: partOf, object: kt:environment-strategy}
  - {predicate: alternativeTo, object: kt:scratch-orgs}
  - {predicate: dependsOn, object: kt:sandbox-templates}
  - {predicate: configuredVia, object: kt:salesforce-cli}
sources:
  - id: s1
    title: "Sandboxes: Staging Environments for Customizing and Testing (Salesforce Help PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/deploy_sandboxes.pdf
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "Sandbox Definition File (Salesforce DX Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_sandbox_definition.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "SandboxPostCopy Interface (Apex Reference Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_interface_System_SandboxPostCopy.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s4
    title: "Sandbox Pricing (Salesforce Platform environments)"
    publisher: Salesforce
    url: https://www.salesforce.com/editions-pricing/platform/environments/
    type: official-docs
    accessed: 2026-10-31
  - id: s5
    title: "Choose the Right Salesforce Org for the Right Job"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/05/choose-the-right-salesforce-org-for-the-right-job
    type: official-blog
    accessed: 2026-10-31
  - id: s6
    title: "Set Up a Sandbox in Your Salesforce Org"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/nonprofit-success-pack-maintenance/set-up-a-sandbox-in-your-salesforce-org
    type: official-learning
    accessed: 2026-10-31
created: 2026-10-31
---

# Sandbox Types

A sandbox is a separate Salesforce org created as a copy of a production org, used to build, test and train without touching live users or data. Salesforce sells four types, and the type decides what gets copied: Developer and Developer Pro sandboxes receive the production org's metadata only, Partial Copy sandboxes add a sample of records chosen by a template, and Full sandboxes copy metadata and every record.[^s1] Because a sandbox is cloned from production, it inherits that org's edition, licences, features and limits, which is the main thing that sets it apart from a scratch org built from source.[^s5]

## The four types at a glance

| Type | What is copied[^s1] | Data storage[^s1] | Minimum refresh interval[^s1] | Commercial model[^s4] |
|---|---|---|---|---|
| Developer | Metadata | 200 MB | 1 day | Included with CRM licences |
| Developer Pro | Metadata | 1 GB | 1 day | Add-on, priced as 5% of net spend |
| Partial Copy | Metadata plus template-selected sample data | 5 GB | 5 days | Add-on, priced as 20% of net spend |
| Full | Metadata and all data | Same as production | 29 days | Add-on, priced as 30% of net spend |

Storage and refresh figures come from Salesforce Help and the pricing page; the percentages are list guidance that Salesforce says may change.[^s1][^s4] Buying a Developer Pro, Partial Copy or Full add-on also brings extra Developer sandboxes: 5, 10 and 15 respectively.[^s1] Trailhead maps the types to jobs: Developer for building and unit testing, Developer Pro for QA and training that needs more sample data, Partial Copy for UAT and integration testing, and Full as the only type suited to performance, load and staging tests.[^s6]

## How creation and refresh work

A sandbox can be created from Setup or from the Salesforce CLI with a JSON definition file. That file names the sandbox (alphanumeric, ten characters at most) and sets exactly one source: a `licenseType` of `Developer`, `Developer_Pro`, `Partial` or `Full` for a fresh copy, or a source sandbox name or ID to clone an existing sandbox.[^s2] A `templateId` is mandatory for Partial Copy, optional for Full and unavailable for the two Developer types. On Full sandboxes `historyDays` controls how much field history comes across (up to 180 days, or `-1` for all available). A `SandboxStorage` feature doubles Developer storage to 400 MB and Developer Pro to 2 GB.[^s2]

Cloning copies data and metadata from another sandbox rather than from production. The clone consumes a licence of its source's type, so cloning a Full sandbox needs a free Full licence. A clone later refreshes from its source, or from production if the source has been deleted.[^s1]

Each create or refresh can run an Apex class that implements `SandboxPostCopy`. Its `runApexClass(SandboxContext)` method receives the org ID, sandbox ID and sandbox name, and it runs at the end of the copy as a hidden Automated Process user. Typical jobs are creating users, seeding data and scrubbing records. Because that user cannot reach every object, a failed script can be re-run by an admin after activation, and `Test.testSandboxPostCopyScript()` lets you unit-test it.[^s3][^s1]

## Limits and gotchas

- **Copy side effects.** Usernames gain the sandbox name as a suffix, and user email addresses gain `.invalid`, so production users do not receive sandbox mail. Contact email addresses are left unchanged, and new sandboxes default to system-only email deliverability.[^s1]
- **What is reset.** Org IDs change on every refresh, so scripts with hard-coded IDs break. MFA registrations are not copied, and SAML settings are disabled until re-enabled.[^s1]
- **Not copied anywhere.** Setup audit trail history, user password history, archived activities and Big Object records stay behind. Chatter data comes across only if selected, and it can slow the copy considerably.[^s1]
- **Lifecycle.** A refreshed sandbox must be activated within 30 days or it is deleted. Activation permanently replaces the previous copy. A sandbox nobody logs into for 180 days becomes eligible for deletion, and deleted sandboxes cannot be recovered.[^s1]
- **Developer types and data.** Because Developer and Developer Pro sandboxes copy no Contact records, portal users do not come across, and configuration that lives in records, such as NPSP's default GAU records, will be missing.[^s1][^s6]

## When to use which (and when not)

Use a Developer sandbox per person for isolated feature work, and Developer Pro when a shared environment needs more test data.[^s5][^s6] Reach for Partial Copy when testers need realistic but bounded production data, and reserve Full for staging, load testing and training. Avoid Full sandboxes for day-to-day development because of their 29-day refresh cadence.[^s6] Scratch orgs suit source-driven, disposable work: they last at most 30 days (7 by default) and contain only what you deploy. Sandboxes give a refreshable replica of production, and many teams run both.[^s5]

## Connections

Sandbox types sit **under** `kt:salesforce-platform`: each is a full org that inherits production's edition and limits.[^s5] They are **part of** `kt:environment-strategy`, which decides how many of each to buy and how they line up in a promotion path.[^s1] Partial Copy and Full sandboxes **depend on** `kt:sandbox-templates` to choose which objects are copied.[^s1][^s2] They are **configured via** `kt:salesforce-cli` through the sandbox definition file, and are an **alternative to** `kt:scratch-orgs` for development environments.[^s2][^s5] They are **related** to `kt:application-lifecycle-management`, `kt:change-sets` and `kt:devops-center`, which move changes between sandboxes and production.[^s5][^s6]

## Sources

[^s1]: Salesforce, "Sandboxes: Staging Environments for Customizing and Testing" (Help PDF). https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/deploy_sandboxes.pdf (accessed 2026-10-31)
[^s2]: Salesforce, "Sandbox Definition File" (Salesforce DX Developer Guide). https://developer.salesforce.com/docs/atlas.en-us.264.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_sandbox_definition.htm (accessed 2026-10-31)
[^s3]: Salesforce, "SandboxPostCopy Interface" (Apex Reference Guide). https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_interface_System_SandboxPostCopy.htm (accessed 2026-10-31)
[^s4]: Salesforce, "Sandbox Pricing". https://www.salesforce.com/editions-pricing/platform/environments/ (accessed 2026-10-31)
[^s5]: Emily Kapner, "Choose the Right Salesforce Org for the Right Job", Salesforce Developers Blog, 2024-05-21. https://developer.salesforce.com/blogs/2024/05/choose-the-right-salesforce-org-for-the-right-job (accessed 2026-10-31)
[^s6]: Trailhead, "Set Up a Sandbox in Your Salesforce Org". https://trailhead.salesforce.com/content/learn/modules/nonprofit-success-pack-maintenance/set-up-a-sandbox-in-your-salesforce-org (accessed 2026-10-31)
