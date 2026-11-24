---
id: kt:data-reconciliation
type: Concept
title: Data Reconciliation
aliases: [migration reconciliation, post-load reconciliation, data migration validation, source-to-target reconciliation, migration data validation]
domain: architecture-practice
summary: >-
  The practice of proving that a Salesforce data load or migration is complete and correct by systematically
  comparing what left the source with what arrived in the org: record counts, failed rows, sampled field values and
  relationships, followed by repair and re-load until the differences are explained and signed off.
release: "Winter '27"
status: concept
broader: [kt:data-migration-strategy]
related: [kt:cutover-plan, kt:data-loader, kt:data-quality, kt:user-acceptance-testing, kt:hypercare, kt:go-live-readiness-assessment]
relations:
  - {predicate: dependsOn, object: kt:external-id-fields}
  - {predicate: dependsOn, object: kt:upsert}
sources:
  - id: s1
    title: "Salesforce Data Migration Best Practices: How to Plan, Execute, and Validate a Data Import or Update"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000385417&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-24
  - id: s2
    title: "Best Practices with Any Data Loader (SOAP API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/best_practices_with_any_data_loader.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s3
    title: "Review Data Loader Output Files (Data Loader Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/data-loader-impl/guide/reviewing-output-files.html
    type: official-docs
    accessed: 2026-11-24
  - id: s4
    title: "Our Top 4 Tips for Massive Data Migrations"
    publisher: Salesforce Engineering Blog
    url: https://engineering.salesforce.com/our-top-4-tips-for-massive-data-migrations-565daaa83cfc/
    type: official-blog
    accessed: 2026-11-24
  - id: s5
    title: "Validate data integrity after migration"
    publisher: Microsoft Learn
    url: https://learn.microsoft.com/en-us/training/modules/azure-storage-migration/12-validate-data-integrity-after-migration
    type: partner
    accessed: 2026-11-24
  - id: s6
    title: "AWS DMS data validation"
    publisher: AWS Documentation
    url: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html
    type: partner
    accessed: 2026-11-24
created: 2026-11-24
---

# Data Reconciliation

Data reconciliation is the evidence-gathering step of a data migration: after records are loaded into Salesforce, the team compares the target against the source and accounts for every difference before the business relies on the new system. Salesforce's own migration guidance treats validation as a distinct step after loading, built from reports that compare source and destination record counts, spot checks of sampled records, and review of error logs and exception reports for rows that failed.[^s1] The SOAP API guide frames the same step as custom reports for record counts, spot checks and exception reports that show what was not migrated, followed by re-migrating or updating data as needed.[^s2]

## How it works

Reconciliation is designed in before the first load, not bolted on afterwards. The key enabler is a legacy identifier: Salesforce recommends a custom field on each object to hold the source system's ID, optionally flagged as an External ID so it is indexed, can drive upsert and helps prevent duplicates.[^s1] With that key in place, every Salesforce record can be traced back to exactly one source row, and validation reports can be grouped and compared by it.[^s2]

A typical reconciliation pass works in layers, from cheap and coarse to expensive and precise:

- **Counts.** Compare per-object record totals in the source extract with report or query totals in the org, ideally broken down by meaningful slices such as record type or owner.[^s1]
- **Load outcomes.** Data Loader writes a success file (with the new Salesforce IDs) and an error file (with the reason each row was rejected) for every operation, so loaded plus failed rows should equal the rows submitted.[^s3]
- **Field and relationship checks.** Spot-check sampled records against the source, and confirm parents and children landed together; the Salesforce engineering team describes a validation job that groups migrated items by a shared ID to confirm every related entity arrived, then re-migrates failures.[^s4]
- **Fix and re-run.** Correct the cause, re-load or update the affected rows with upsert on the external ID, and repeat the comparison until the remaining differences are explained.[^s2]

Generic migration tooling outside Salesforce follows the same pattern and is a useful reference for automation. AWS Database Migration Service compares each source row with its target row and records failures by type, such as a row that differs or a row missing from the source or target.[^s6] Microsoft's migration guidance adds checksums for critical data, sampling across a large estate, and a formal sign-off gate with named approvers.[^s5]

## Limits and gotchas

- **Test on one record first.** Load a single record, verify it in Salesforce, and only then load the full file; this catches mapping mistakes before they multiply.[^s1]
- **Export status files are off by default.** Data Loader exports do not produce a success file unless "Generate status files for exports" is enabled in Advanced Settings.[^s3]
- **Column names can collide.** If the object has a column named "success" or "error", Data Loader's output columns can show incorrect information, so rename them first.[^s3]
- **Load order affects failures.** Objects must be loaded in dependency order (for example users, then accounts, then opportunities); a broken order shows up as error rows that reconciliation has to explain.[^s2]
- **Moving targets skew results.** Comparing against a target that users or integrations are still writing to can make validation results inaccurate, so reconcile against a frozen state where possible.[^s6]
- **Validation is not one-time.** Run completeness checks after every load pass and mock run, not only on the final cutover load.[^s5]

## When to use it (and when not)

Every migration or bulk data change that the business will depend on needs some reconciliation; the depth scales with risk. A one-off import of a few hundred leads may need only a count check and a glance at the error file, while a regulated or financial migration warrants automated row-level comparison, structured logs of successes and errors, and documented sign-off.[^s4][^s5] Reconciliation proves the data moved faithfully; it does not prove the data was good to begin with, which is the job of cleansing and data quality work done before the load.[^s2]

## Connections

Data reconciliation sits **broader** under data migration strategy as one of its phases, and it **depends on** external ID fields and upsert to tie each record back to its source and to re-load fixes without creating duplicates.[^s1] Its main evidence comes from tools such as Data Loader and its success and error files.[^s3] Reconciliation results feed the go/no-go decision in a cutover plan and a go-live readiness assessment, complement user acceptance testing (which checks behaviour rather than data completeness), and leave a baseline that hypercare teams use when users report missing or wrong records after launch.[^s5] It is distinct from ongoing data quality management, which keeps data accurate after the migration is over.[^s1]

## Sources

[^s1]: Salesforce Help, "Salesforce Data Migration Best Practices: How to Plan, Execute, and Validate a Data Import or Update". https://help.salesforce.com/s/articleView?id=000385417&language=en_US&type=1 (accessed 2026-11-24)
[^s2]: Salesforce Developers, "Best Practices with Any Data Loader". https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/best_practices_with_any_data_loader.htm (accessed 2026-11-24)
[^s3]: Salesforce Developers, "Review Data Loader Output Files". https://developer.salesforce.com/docs/platform/data-loader-impl/guide/reviewing-output-files.html (accessed 2026-11-24)
[^s4]: Salesforce Engineering Blog, "Our Top 4 Tips for Massive Data Migrations". https://engineering.salesforce.com/our-top-4-tips-for-massive-data-migrations-565daaa83cfc/ (accessed 2026-11-24)
[^s5]: Microsoft Learn, "Validate data integrity after migration". https://learn.microsoft.com/en-us/training/modules/azure-storage-migration/12-validate-data-integrity-after-migration (accessed 2026-11-24)
[^s6]: AWS Documentation, "AWS DMS data validation". https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html (accessed 2026-11-24)
