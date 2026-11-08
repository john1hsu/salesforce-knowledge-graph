---
id: kt:data-and-file-storage-allocations
type: Limit
title: Data and File Storage Allocations
aliases: [Salesforce storage limits, data storage limit, file storage limit, org storage allocation, Storage Usage]
domain: platform-architecture
summary: >-
  The edition- and license-based amounts of data storage (records) and file storage (attachments, Files, content)
  a Salesforce org receives, how record storage is estimated per object, and what happens in production and
  sandboxes when usage reaches the allocation.
release: "Winter '27"
status: current
broader: [kt:governor-limits, kt:multitenancy]
related: [kt:large-data-volumes, kt:archiving-strategy, kt:big-objects, kt:sandbox-types, kt:person-accounts, kt:data-migration-strategy]
relations:
  - {predicate: contrastsWith, object: kt:api-request-limits}
  - {predicate: coveredBy, object: kt:platform-data-architect-certification}
sources:
  - id: s1
    title: "Data and File Storage Allocations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.overview_storage.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Salesforce Files Storage Allocations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.files_storage.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Salesforce Data Storage: Estimated Record Size by Object Type"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000383664&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "Data storage amount limit exceeded"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000386657&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-08
  - id: s5
    title: "Sandbox Licenses and Storage Limits by Type"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=deploy_sandboxes_limits.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s6
    title: "Archive Basics: Optimize Data with Archive"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/archive-basics/optimize-data-with-archive
    type: official-learning
    accessed: 2026-11-08
created: 2026-11-08
---

# Data and File Storage Allocations

Every Salesforce org is sold two separate pools of storage. **Data storage** holds records: accounts, contacts, cases, leads, opportunities, tasks, events, email messages, custom object rows and similar. **File storage** holds binary content: attachments, Files home, Salesforce CRM Content, Chatter files including user photos, the Documents tab, Knowledge file fields and Site.com assets.[^s1] The two pools are measured and allocated independently, so a full file store says nothing about remaining record capacity and vice versa. Big objects have a third, record-count-based allocation of their own.[^s1]

## How the allocation is calculated

Allocations combine a per-org base with a per-license increment. For data storage, most paid editions (Contact Manager, Group, Essentials, Professional, Enterprise, Performance, Unlimited and Starter) get a 10 GB minimum. Contact Manager, Group, Professional and Enterprise then add 20 MB per user license, while Performance and Unlimited add 120 MB per license (20 MB for Lightning Platform Starter licenses). Developer Edition gets 5 MB and Personal Edition 20 MB, with no per-license increment.[^s1] Salesforce's own worked example: a 10-user Professional Edition org has 10 GB plus 200 MB, or 10.2 GB.[^s1]

File storage follows the same shape. Contact Manager, Group, Professional, Enterprise, Performance and Unlimited get 10 GB per org; Essentials and Starter get 1 GB; Developer and Personal get 20 MB.[^s1] On top of the org base, each standard user license adds 612 MB in Contact Manager, Group and Professional (1 GB when those orgs have fewer than 10 users) and 2 GB in Enterprise, Performance and Unlimited.[^s2] The minimums apply to Salesforce and Salesforce Platform licenses; orgs with custom user licenses need to confirm their amounts with Salesforce.[^s1][^s2]

## How record storage is counted

Data storage is not measured by actual bytes per row. Salesforce estimates most records at about 2 KB regardless of how many fields are filled.[^s3] The documented exceptions matter for capacity planning:[^s3]

- **Person accounts:** 4 KB, because each is an Account plus a Contact.[^s3]
- **Campaigns:** 8 KB; **campaign members:** 1 KB.[^s3]
- **Knowledge articles:** about 4 KB, varying with rich text content; images in rich text fields count as file storage.[^s3]
- **Email messages:** 2 KB baseline, but HTML email is counted at its actual size, so a 100 KB HTML email uses 100 KB.[^s3]
- **Quote, order and work order line items:** 2 KB each, counted separately from their parent.[^s3]

Files, by contrast, consume their actual uploaded size.[^s3] This makes record counts, not field width, the main driver of data storage: half a million person accounts cost roughly 1.9 GB, as Salesforce's own example shows.[^s3] Usage is calculated asynchronously, so a large import may not appear immediately on the **Storage Usage** page in Setup, which shows usage by object, top users and largest files.[^s1][^s3]

## Limits and gotchas

- **Production overage is soft but risky.** At or near 100% the org keeps working, but Salesforce says performance degrades at some unpredictable point beyond the allocation.[^s4] Contracts make the overage a commercial issue as well, since you pay for what you use.[^s6]
- **Sandboxes are hard-capped.** Full sandboxes enforce limits strictly, and a Full sandbox refreshed from an over-limit production org inherits that usage and can't create records.[^s4] Developer sandboxes get 200 MB of data and file storage (data upgradable to 400 MB), Developer Pro 1 GB (upgradable to 2 GB), Partial Copy 5 GB of data with production's file storage, and Full sandboxes match production. Sandboxes send no alert when full; they simply stop saving data.[^s5]
- **Big objects:** eligible editions get storage for 1 million big object records per org, raisable on request and enforced contractually in production.[^s1]
- **Order Management** data is allocated separately: 50 MB each for managed and unmanaged orders in that SKU.[^s1]

## Managing storage (and the alternatives)

Salesforce's remedies are to buy more storage or licenses, delete outdated records and attachments, or archive.[^s4] The paid Archive app moves historical, rarely used records to its own secure archive outside the org, applies retention and purge policies, surfaces archived data back in Salesforce through widgets, and includes a Storage Analyzer that ranks objects by storage and tracks usage history.[^s6][^s1] Architecturally, the choice is usually between paying for storage, offloading cold data (archiving, big objects or external systems), and reducing record counts through design, for example avoiding high-volume child records that duplicate data available elsewhere.[^s3][^s6]

## Connections

Storage allocations are one of the org-wide resource caps that come with **multitenancy**, sitting alongside per-transaction **governor limits** and the daily **API request limits** they are often confused with.[^s1] They drive **large data volumes** and **archiving strategy** decisions and shape **data migration strategy**, since bulk loads consume data storage at the per-record estimates above.[^s3][^s6] **Person accounts** double the per-record cost, **big objects** offer a separately counted store for high-volume history, and **sandbox types** each carry their own storage cap.[^s1][^s3][^s5] The topic is examined in the **Platform Data Architect certification**.

## Sources

[^s1]: Salesforce Help, "Data and File Storage Allocations". https://help.salesforce.com/s/articleView?id=sf.overview_storage.htm&language=en_US&type=5 (accessed 2026-11-08)
[^s2]: Salesforce Help, "Salesforce Files Storage Allocations". https://help.salesforce.com/s/articleView?id=sf.files_storage.htm&language=en_US&type=5 (accessed 2026-11-08)
[^s3]: Salesforce Help, "Salesforce Data Storage: Estimated Record Size by Object Type". https://help.salesforce.com/s/articleView?id=000383664&language=en_US&type=1 (accessed 2026-11-08)
[^s4]: Salesforce Help, "Data storage amount limit exceeded". https://help.salesforce.com/s/articleView?id=000386657&language=en_US&type=1 (accessed 2026-11-08)
[^s5]: Salesforce Help, "Sandbox Licenses and Storage Limits by Type". https://help.salesforce.com/s/articleView?id=deploy_sandboxes_limits.htm&language=en_US&type=5 (accessed 2026-11-08)
[^s6]: Trailhead, "Archive Basics: Optimize Data with Archive". https://trailhead.salesforce.com/content/learn/modules/archive-basics/optimize-data-with-archive (accessed 2026-11-08)
