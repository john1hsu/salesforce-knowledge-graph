---
id: kt:data-skew
type: AntiPattern
title: Data Skew
aliases: [account data skew, ownership skew, ownership data skew, lookup skew, parent-child data skew]
domain: data-model
summary: >-
  A data distribution problem in which a very large number of records concentrate on a single parent record, owner or
  lookup target, causing record-lock contention and long-running sharing recalculations.
release: "Winter '27"
status: current
broader: [kt:large-data-volumes]
related: [kt:lookup-vs-master-detail, kt:role-hierarchy, kt:roll-up-summary-field]
relations:
  - {predicate: causes, object: kt:record-locking}
  - {predicate: causes, object: kt:sharing-recalculation}
  - {predicate: contrastsWith, object: kt:salesforce-sharing-model}
sources:
  - id: s1
    title: "Large Data Volumes: Design Your Data Model"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/large-data-volumes/design-your-data-model
    type: official-learning
    accessed: 2026-10-31
  - id: s2
    title: "Designing Record Access for Enterprise Scale: Ownership Data Skew"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/draes/guide/draes-group-membership-data-skew.html
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "Managing Lookup Skew to Avoid Record Lock Exceptions"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/engineering/2013/04/managing-lookup-skew-to-avoid-record-lock-exceptions
    type: official-blog
    accessed: 2026-10-31
  - id: s4
    title: "Architect Salesforce Record Ownership Skew for Peak Performance in Large Data Volume Environments"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/engineering/2012/06/architect-salesforce-record-ownership-skew-for-peak-performance-in-large-data-volume-environments
    type: official-blog
    accessed: 2026-10-31
created: 2026-10-31
---

# Data Skew

Data skew is what happens when too many records pile up on one point of reference: a single parent record, a single owner, or a single lookup target. Trailhead's large data volumes module puts the general threshold at more than 10,000 child records sharing the same parent.[^s1] Skew is not an error in itself. It is a distribution problem that makes routine operations, such as saving a child record or changing an owner, slow or prone to failure because the platform must lock or recalculate across the whole concentration of records.[^s1][^s4] Salesforce describes three forms: account (parent-child) skew, ownership skew and lookup skew.

## How it works

**Account data skew.** In a parent-child relationship under a private sharing model, such as Accounts and Contacts, a single parent with a huge number of children becomes a hot spot. A typical cause is parking unassigned contacts under one catch-all "Unassigned" account.[^s1] Updating a child locks its parent, so many concurrent child updates, for example from a data load, compete for the same lock and some fail. Changing that account's owner also forces sharing to be re-evaluated for every child, which can take a long time with hundreds of thousands of children.[^s1]

**Ownership skew.** One user owns more than 10,000 records of a single object. This usually happens when ownership is concentrated in one user, one queue, or all members of one role or public group, such as a placeholder user who receives all unassigned leads.[^s2] The cost appears when sharing changes. Moving that owner within the role hierarchy, or adding or removing them from a role or group used as a sharing rule source, forces Salesforce to update a very large number of sharing table entries, which can cause a long-running access recalculation.[^s2] Changing ownership requires removing access from the previous owner, every user above them in the role hierarchy, and users granted access through sharing rules. The 2012 architect guidance calls ownership changes among the most costly transactions in the system.[^s4]

**Lookup skew.** A very large number of records reference a single record through a lookup field. On every insert or update, Salesforce locks the target records of each lookup field to preserve referential integrity. Saves are usually quick enough that locks rarely collide. Heavy automated processing on high-volume objects, combined with custom code that holds the lock longer, produces lock exceptions.[^s3] Unlike account skew, lookup skew is not tied to the sharing model. Any lookup, including a custom one, can create it.[^s3]

## Limits and gotchas

- The 10,000-record figure is the threshold Salesforce gives for parent-child skew and for ownership of one object by one user.[^s1][^s2] The lookup skew guidance gives no numeric threshold. Its example has roughly 166,000 accounts pointing at each of three lookup values.[^s3]
- There is no dedicated tool for finding lookup skew. Focus on objects with many records and heavy concurrent insert or update activity, review each lookup field, and extract lookup values for analysis when the data is not well known.[^s1][^s3]
- Skew under other usage patterns may cause no visible problems. Performance issues are generally rare unless updates touch many users or large data volumes.[^s1][^s2]
- Record locks are held while triggers and other save-time automation run, so slow save logic widens the window for contention.[^s3]

## Mitigation

- **Distribute the data.** Create enough parent accounts to keep each below 10,000 children and spread new children across them as they are created. Spread record ownership across more users.[^s1][^s2]
- **Take skewed owners out of the role hierarchy.** If a few users must own large volumes, do not assign them a role. If they need one, put them alone in a separate top-level role, do not move them afterwards, and keep them out of public groups used as sharing rule sources.[^s2][^s4]
- **Shrink lock time and load.** Consolidate to one trigger per object, cut or merge save-time automation, move non-essential work to asynchronous processing, and run bulk jobs serially, off-peak or in smaller batches.[^s3]
- **Remove the lookup.** For a catch-all value, leave the lookup blank where appropriate. When only a few values are needed and no related data is required, a picklist removes the lock entirely.[^s3]
- **Fix it at the source.** Better assignment rules and data quality stop records from collecting under a default owner in the first place.[^s4]

## Connections

Data skew sits under **large data volumes** (`kt:large-data-volumes`), since it is a scaling problem in high-volume orgs.[^s1] It **causes** **record locking** contention (`kt:record-locking`) on lookup targets and parents, and long-running **sharing recalculation** (`kt:sharing-recalculation`) when skewed owners or parents change.[^s2][^s3] It **contrasts with** the **Salesforce sharing model** (`kt:salesforce-sharing-model`) as a design concern: account skew is described for parent-child relationships under private sharing, and ownership changes must unwind access granted through the hierarchy and sharing rules.[^s1][^s4] It is **related** to **lookup vs. master-detail** (`kt:lookup-vs-master-detail`), because relationship fields lock their target records on save, and to the **role hierarchy** (`kt:role-hierarchy`), since where a skewed owner sits determines how much access must be recalculated.[^s2][^s3] It is also related to **roll-up summary fields** (`kt:roll-up-summary-field`), another parent-child feature whose design should account for how many children concentrate on one parent.[^s1]

## Sources

[^s1]: Trailhead, "Large Data Volumes: Design Your Data Model". https://trailhead.salesforce.com/content/learn/modules/large-data-volumes/design-your-data-model (accessed 2026-10-31)
[^s2]: Salesforce Developers, "Designing Record Access for Enterprise Scale: Ownership Data Skew". https://developer.salesforce.com/docs/platform/draes/guide/draes-group-membership-data-skew.html (accessed 2026-10-31)
[^s3]: Salesforce Developers Blog, "Managing Lookup Skew to Avoid Record Lock Exceptions" (2013). https://developer.salesforce.com/blogs/engineering/2013/04/managing-lookup-skew-to-avoid-record-lock-exceptions (accessed 2026-10-31)
[^s4]: Salesforce Developers Blog, "Architect Salesforce Record Ownership Skew for Peak Performance in Large Data Volume Environments" (2012). https://developer.salesforce.com/blogs/engineering/2012/06/architect-salesforce-record-ownership-skew-for-peak-performance-in-large-data-volume-environments (accessed 2026-10-31)
