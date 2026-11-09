---
id: kt:sandbox-templates
type: Feature
title: Sandbox Templates
aliases: [sandbox template, partial copy template, Partial Copy sandbox template, sandbox data template, templateId]
domain: devops-and-alm
summary: >-
  Saved, reusable selections of standard and custom objects that decide which production records are copied into a
  Partial Copy sandbox (where a template is mandatory) or a Full sandbox (where it is optional).
release: "Winter '27"
status: current
broader: [kt:sandbox-types, kt:environment-strategy]
related: [kt:lookup-vs-master-detail, kt:testing-strategy, kt:big-objects, kt:field-history-tracking]
relations:
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: queriedWith, object: kt:tooling-api}
  - {predicate: governedBy, object: kt:data-and-file-storage-allocations}
sources:
  - id: s1
    title: "Salesforce Sandboxes: Staging Environments for Customizing and Testing (Summer '23 PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/deploy_sandboxes.pdf
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "Which Records Are Copied When You Refresh a Salesforce Partial Data Sandbox"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000386381&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-09
  - id: s3
    title: "Guidance for Partial Copy Salesforce Sandbox Creation and Refreshes"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000381868&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-09
  - id: s4
    title: "Create a Sandbox Definition File (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_sandbox_definition.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s5
    title: "Sandbox Templates and a New Look"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2013/05/sandbox-templates-and-a-new-look
    type: official-blog
    accessed: 2026-11-09
created: 2026-11-09
---

# Sandbox Templates

A **sandbox template** is a named, saved list of objects that tells Salesforce which records to bring across when it
builds or refreshes a sandbox that carries data. Templates work only with Full and Partial Copy sandboxes and are
listed on the Sandbox Templates tab of the Sandboxes setup page, which appears only in orgs that have bought one of
those two licence types.[^s1] They arrived in Summer '13: before then a Full sandbox always received every record,
and templates gave teams a way to keep sensitive data out, shrink copies so they finish sooner, and keep several
reusable selections for different teams or test purposes.[^s5]

## How it works

An admin creates a template from Setup under Sandboxes > Sandbox Templates, gives it a name and description, and ticks
the objects to include. As objects are selected the editor adds the related objects they require, shown in a Required
Objects column, and some objects are present in every template because every org needs them. Deselecting an object
also drops dependants that were not picked explicitly, after a confirmation prompt.[^s1] Because these dependencies
follow the schema, a later change to a required relationship can silently add or remove objects from saved templates,
so Salesforce advises reviewing templates after such changes. Selecting Content Body in a template brings file
content along.[^s1]

The template is then chosen when a sandbox is created or refreshed. A Partial Copy sandbox cannot be created at all
until a template exists; without one the Create button does not appear.[^s3] A Full sandbox may use a template to copy a
subset or skip it to copy everything.[^s1] From the command line, the sandbox definition file passes the template in
`templateId`, a 15-character ID beginning with `1ps` that can be read from the template page URL. The field is
required for Partial sandboxes, optional for Full and not accepted for Developer or Developer Pro sandboxes.[^s4]

## How Partial Copy sampling behaves

A template picks objects, not records. For a Partial Copy sandbox the copy engine takes a random sample of up to
10,000 records per selected object, and the sandbox shows a Sampling status while it decides which rows to take.[^s2][^s1]
Only master-detail and required lookup relationships are enforced: children on those relationships are sampled
through their parents, whereas an object linked only by ordinary lookups is sampled as a top-level object, so its
copied rows may point at parents that were never copied.[^s2] Salesforce treats the Account link on Contacts and
Opportunities as required, so records created through Apex or the API without an Account are skipped.[^s2] When many
objects exceed 10,000 rows, the per-object count can be cut to stay within the 5 GB Partial Copy storage limit.[^s2]

Beyond the template, a Partial Copy sandbox always receives metadata plus reports, dashboards, price books, products,
apps and documents; external portal and community user records are not copied on refresh, which can leave related
cases unreadable in Classic.[^s3]

## Limits and gotchas

- A template is mandatory for Partial Copy, optional for Full and unavailable for Developer and Developer Pro.[^s4]
- Up to 10,000 sampled records per selected object in Partial Copy, inside 5 GB of data storage.[^s2][^s3]
- Big object definitions are copied but their records never are, whatever the template says.[^s1]
- Field history and Chatter copy options belong to Full sandboxes; `historyDays` takes -1 (all history) or one of a fixed set
  of values from 0 to 180, and is Full-only.[^s4]
- Sampling does not guarantee referential completeness for plain lookups, so test data may need a post-refresh
  seeding step.[^s2]

## When to use it

Use a template for any Partial Copy sandbox aimed at UAT, integration testing or training, and consider one for Full
sandboxes whenever a full copy is larger or more sensitive than the work needs; Salesforce recommends templates on
Full sandboxes so they hold only required records.[^s1][^s3] Where tests need complete record graphs at volume, a Full
sandbox without a template, or a dedicated data seeding step, fits better than Partial Copy sampling.[^s2]

## Connections

Sandbox templates sit **under** `kt:sandbox-types`, because only Partial Copy and Full sandboxes consume them, and
under `kt:environment-strategy`, which decides what data each environment should hold.[^s1][^s3] They are **configured
via** `kt:salesforce-cli` through the sandbox definition file's `templateId`, and the definition file's fields map to
the `SandboxInfo` object **queried with** `kt:tooling-api`.[^s4] Their sampling rules follow
`kt:lookup-vs-master-detail` relationships, and Partial Copy volume is **governed by** the 5 GB sandbox storage cap in
`kt:data-and-file-storage-allocations`.[^s2] They are **related** to `kt:testing-strategy` (what data each test stage
needs), `kt:big-objects` (never copied) and `kt:field-history-tracking` (history copied only to Full sandboxes).[^s1][^s4]

## Sources
[^s1]: Salesforce, "Salesforce Sandboxes: Staging Environments for Customizing and Testing" (Summer '23 PDF). https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/deploy_sandboxes.pdf (accessed 2026-11-09)
[^s2]: Salesforce Help, "Which Records Are Copied When You Refresh a Salesforce Partial Data Sandbox". https://help.salesforce.com/s/articleView?id=000386381&language=en_US&type=1 (accessed 2026-11-09)
[^s3]: Salesforce Help, "Guidance for Partial Copy Salesforce Sandbox Creation and Refreshes". https://help.salesforce.com/s/articleView?id=000381868&language=en_US&type=1 (accessed 2026-11-09)
[^s4]: Salesforce Developers, "Create a Sandbox Definition File". https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_sandbox_definition.htm (accessed 2026-11-09)
[^s5]: Salesforce Developers Blog, "Sandbox Templates and a New Look" (May 2013). https://developer.salesforce.com/blogs/2013/05/sandbox-templates-and-a-new-look (accessed 2026-11-09)
