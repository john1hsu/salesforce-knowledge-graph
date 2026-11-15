---
id: kt:backup-and-recover
type: Product
title: Salesforce Backup & Recover
aliases: [Backup & Recover, Backup and Recover, Backup & Recover for Salesforce, Own Recover, OwnBackup Recover]
domain: clouds-and-products
summary: >-
  Salesforce's paid backup and restore product, formerly Own Recover, that keeps automated, independently stored
  backups of an org's data, files and metadata and lets admins compare backups and restore selected records or fields.
release: "Winter '27"
status: current
broader: [kt:data-governance]
related: [kt:shared-responsibility-model, kt:backup-and-recover-next, kt:sandbox-types, kt:data-loader, kt:shield-platform-encryption]
relations:
  - {predicate: contrastsWith, object: kt:archiving-strategy}
  - {predicate: integratesWith, object: kt:data-mask-and-seed}
  - {predicate: dependsOn, object: kt:connected-apps}
  - {predicate: governedBy, object: kt:api-request-limits}
sources:
  - id: s1
    title: "Get Started with Backup & Recover (Backup & Recover Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/backup-recover-basics/get-started-with-backup-recover
    type: official-learning
    accessed: 2026-11-15
  - id: s2
    title: "Create Your First Salesforce Backup (Backup & Recover Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/backup-recover-basics/create-your-first-salesforce-backup
    type: official-learning
    accessed: 2026-11-15
  - id: s3
    title: "Backup & Recover for Salesforce"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.backup_recover_o.htm&amp=&type=5
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "Back Up and Recover Data with Salesforce Backup & Recover Next"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.backup_recover.htm&type=5
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "Data Backup and Recovery"
    publisher: Salesforce
    url: https://www.salesforce.com/platform/data-backup-recovery/
    type: official-blog
    accessed: 2026-11-15
  - id: s6
    title: "Introducing Salesforce Backup & Recover Next"
    publisher: Salesforce Blog
    url: https://www.salesforce.com/blog/introducing-salesforce-backup-recover-next/
    type: official-blog
    accessed: 2026-11-15
created: 2026-11-15
---

# Salesforce Backup & Recover

**Salesforce Backup & Recover** is Salesforce's add-on for protecting the data an org holds: it takes automated backups of records, files and metadata, keeps them in storage independent of the org, and restores what was lost or corrupted. It is the former **Own Recover**, which came to Salesforce with the Own acquisition, and its help content still sits under the "Own from Salesforce" documentation set.[^s3][^s5] Pricing is quoted per customer rather than published.[^s5]

The product exists because of the shared responsibility split. Salesforce secures and runs the platform, but the customer is responsible for its own records, files, metadata and customizations, and for guarding them against accidental or malicious change.[^s1] Native tools cover only part of that: the Recycle Bin holds deleted records only briefly and does nothing about bad updates, and weekly exports are manual snapshots with no recovery tooling.[^s1] Typical loss scenarios are user mistakes, failed integrations, buggy code or automation, insider or attacker activity, and imports that fail halfway.[^s1]

## How it works

An admin adds a **backup service** per source: production data, production metadata, sandbox data or sandbox metadata. After setup, backups run on their own; they can also be scheduled or run on demand, and scheduled exports can push the latest successful backup to existing endpoints.[^s3] Trailhead describes three backup types.[^s2]

- **Full**: the first backup covers all org data, and later full backups run weekly on a day you pick or the service picks.[^s2]
- **Synthetic full**: runs daily, captures only changes since the last run, and merges them into the previous backup.[^s2]
- **On demand**: started at any time, for example before and after a deployment, mass update or migration.[^s2]

Coverage includes standard and custom objects and fields, files, Chatter feeds and attachments, and metadata through a separate metadata backup service.[^s2] Data and files back up as separate processes, so record recovery can start while files are still finishing.[^s2]

Around the backups sit the recovery tools. **Compare** shows additions, changes and deletions between two backups, for the whole org or chosen objects; **Find** searches across snapshots, including attachment contents; and the restore application puts the affected records back.[^s3] Salesforce says restores can target data from any point in the backup history without overwriting valid records created since, and that relationships between records survive the restore.[^s5] Optional extras include Continuous Data Protection for capturing every change, Blockchain Verify for tamper evidence, and bring-your-own-key encryption options.[^s3][^s5]

## Limits and gotchas

- The service connects through the API as a dedicated integration user, set up with OAuth, an allowlisted IP range and a connected app.[^s2]
- That user needs very broad rights, including API Enabled, Modify All Data and read/edit on every object, which makes it a high-value account to protect.[^s2]
- If MFA is enforced for everyone, the headless backup user must be excluded or backups fail.[^s2]
- Knowledge articles and custom big objects are left out by default, and objects the API can't fully query can't be backed up at all.[^s2]
- Retention is set per org on daily, weekly, monthly and yearly schedules; Salesforce gives the default as 99 years.[^s5]
- Because this product works over the API, its throughput is bounded by API limits; Salesforce contrasts this with the newer native Next product.[^s6]

## Backup & Recover vs. Backup & Recover Next

Salesforce also sells **Backup & Recover Next**, a native product that stores backups in a separate stack inside the Salesforce trust boundary, is not subject to API governor limits, and is described as much faster than Backup & Recover.[^s6] Next runs daily incremental backups with a full backup on Sundays, and requires the Backup & Recover Data and Backup & Recover Files add-on licenses in Professional, Enterprise, Performance or Unlimited Edition.[^s4] Salesforce says Next holds FedRAMP High certification but is available only in select regions so far.[^s6] Backup & Recover remains the broader option: it also covers ServiceNow and Microsoft Dynamics, and exports to CSV, SQL or MySQL.[^s5]

## Connections

Backup & Recover sits under `kt:data-governance`, since it is how an org keeps a recoverable record of its data. It is the customer-side answer to `kt:shared-responsibility-model`, which leaves data protection to the org.[^s1] It **contrasts with** `kt:archiving-strategy`: backups keep restorable copies, while archiving moves data out of the org. It **integrates with** `kt:data-mask-and-seed`, the seeding add-on from the same Own lineage, and its backup services can cover sandbox data and metadata as well as production (`kt:sandbox-types`).[^s3] It **depends on** `kt:connected-apps` for its connection and is **governed by** `kt:api-request-limits` because it reads through the API.[^s2][^s6] Its native sibling `kt:backup-and-recover-next` documents encrypting backup data with `kt:shield-platform-encryption`.[^s4] Records restored outside the app can be reloaded with tools such as `kt:data-loader`.

## Sources
[^s1]: Trailhead, "Get Started with Backup & Recover". https://trailhead.salesforce.com/content/learn/modules/backup-recover-basics/get-started-with-backup-recover (accessed 2026-11-15)
[^s2]: Trailhead, "Create Your First Salesforce Backup". https://trailhead.salesforce.com/content/learn/modules/backup-recover-basics/create-your-first-salesforce-backup (accessed 2026-11-15)
[^s3]: Salesforce Help, "Backup & Recover for Salesforce". https://help.salesforce.com/s/articleView?language=en_US&id=platform.backup_recover_o.htm&amp=&type=5 (accessed 2026-11-15)
[^s4]: Salesforce Help, "Back Up and Recover Data with Salesforce Backup & Recover Next". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.backup_recover.htm&type=5 (accessed 2026-11-15)
[^s5]: Salesforce, "Data Backup and Recovery". https://www.salesforce.com/platform/data-backup-recovery/ (accessed 2026-11-15)
[^s6]: Salesforce Blog, "Introducing Salesforce Backup & Recover Next". https://www.salesforce.com/blog/introducing-salesforce-backup-recover-next/ (accessed 2026-11-15)
