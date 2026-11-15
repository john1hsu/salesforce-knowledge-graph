---
id: kt:data-loader
type: Tool
title: Data Loader
aliases: [Salesforce Data Loader, dataloader, Data Loader CLI]
domain: data-model
summary: >-
  Salesforce's downloadable client application for bulk importing, updating, upserting, deleting and exporting
  records from CSV files, through a desktop interface or (on Windows) a scriptable command line, using SOAP API,
  Bulk API or Bulk API 2.0 under the hood.
release: "Winter '27"
status: current
broader: [kt:data-integration]
related: [kt:data-migration-strategy, kt:external-id-fields, kt:upsert, kt:large-data-volumes]
relations:
  - {predicate: dependsOn, object: kt:soap-api}
  - {predicate: dependsOn, object: kt:bulk-api-1}
  - {predicate: dependsOn, object: kt:bulk-api-2}
  - {predicate: alternativeTo, object: kt:data-import-wizard}
sources:
  - id: s1
    title: "When to Use Data Loader (Data Loader Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.dataLoader.meta/dataLoader/when_to_use_the_data_loader.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s2
    title: "Configure Data Loader (Data Loader Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/data-loader-impl/guide/configuring-the-data-loader.html
    type: official-docs
    accessed: 2026-11-15
  - id: s3
    title: "Considerations for Installing Data Loader (Data Loader Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/data-loader-impl/guide/installing-the-data-loader.html
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "Data Loader Command-Line Operations and Exit Codes (Data Loader Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/data-loader-impl/guide/loader-operations.html
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "Import Data (Data Management module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lex_implementation_data_management/lex_implementation_data_import
    type: official-learning
    accessed: 2026-11-15
created: 2026-11-15
---

# Data Loader

Data Loader is Salesforce's own client application for moving records in and out of an org in bulk. It reads and writes CSV files and runs either through a point-and-click interface or from the command line, which makes it the default free tool for loads that outgrow the browser-based import wizards in Setup.[^s1][^s5] Salesforce positions it as a complement to those wizards rather than a replacement: the wizards suit small, simple imports, while Data Loader handles any object, larger volumes and repeatable jobs.[^s1]

## How it works

Data Loader is installed on the user's machine, not in the org. It needs a Java Runtime Environment at version 17 or later, and the Windows installer no longer bundles Java, so the JRE must be installed first. The official download sits in the Tools section of the Salesforce Developers site, and the source is published as an open-source project on GitHub for teams that want to modify it.[^s3]

Each load maps CSV columns to object fields and then calls a Salesforce API. By default it uses SOAP API; selecting **Use Bulk API** or **Use Bulk API 2.0** switches insert, update, upsert, delete and hard delete to the asynchronous bulk engines, which process large files in parallel.[^s2][^s5] The batch size you configure depends on the engine: up to 200 records per call with SOAP API, up to 10,000 with Bulk API, and none at all with Bulk API 2.0, where Salesforce sizes the batches itself. Exports through SOAP use a separate export batch size that defaults to 500 and ranges from 200 to 2,000.[^s2]

For automation, the command-line mode drives the same engine from configuration files, so a scheduler can run nightly imports or exports without anyone at the keyboard.[^s5] The supported batch operations are `extract`, `extract_all`, `insert`, `update`, `upsert`, `delete` and `hard_delete`. From version 62 the CLI returns distinct exit codes: 0 for success, 1 for a client-side error, 2 for a server-side error, 3 for an operation error, and 4 for partial row failures when `process.batchMode.exitWithErrorOnFailedRows` is enabled.[^s4] Without that flag a run can exit 0 even though some rows failed, so scripts should check the error files rather than trust the exit code alone.[^s4]

## Limits and gotchas

- **Volume.** Salesforce recommends Data Loader for CSV files of up to 150,000,000 records; beyond that it points customers to a partner or an AppExchange product.[^s1]
- **CLI is Windows-only.** The command-line interface is supported on Windows only, which matters when planning scheduled jobs on macOS or Linux hosts.[^s3][^s4]
- **Nulls with bulk APIs.** The *Insert null values* setting doesn't work with either bulk option; to blank a field in a bulk load, put `#N/A` in the CSV cell instead.[^s2]
- **Hard delete is permanent.** Hard delete, available only through Bulk API and Bulk API 2.0, bypasses the Recycle Bin, so the records can't be restored.[^s2]
- **Serial mode.** *Enable serial mode for Bulk API* processes batches one at a time, which reduces database contention such as lock errors but makes the job slower.[^s2]
- **Time zone.** Date and time values are read in the configured time zone; if it is blank the computer's zone is used, and an invalid value falls back to GMT.[^s2]

## When to use it (and when not)

Choose Data Loader when the object isn't supported by the Data Import Wizard, when the file is large, when field mappings are complex and reused, when loads must run on a schedule, or when you need CSV exports for backup.[^s1] Choose the Data Import Wizard for fewer than 50,000 records on supported objects, for targets with fewer than 50 fields, or when you want the wizard's built-in duplicate matching on account name and site or contact and lead email.[^s1][^s5] Whichever tool you pick, Trailhead advises removing duplicates from the file during cleanup before the import.[^s5]

## Connections

Data Loader sits under **data integration** as the hands-on client for file-based loads, and it is a common workhorse in a **data migration strategy**.[^s1] It depends on **SOAP API** by default and on **Bulk API** or **Bulk API 2.0** when bulk mode is selected, so those APIs' limits and locking behaviour carry through to every Data Loader job; the serial-mode switch exists for that reason, and it links to **large data volumes** planning.[^s2] Because **upsert** is one of its core operations, both in the interface and on the command line, Data Loader connects directly to the **upsert** pattern, which in turn links it to **external ID fields**.[^s4] Its main alternative inside Setup is the **Data Import Wizard**, which trades scale and automation for simplicity and duplicate matching.[^s1][^s5]

## Sources
[^s1]: Salesforce Developers, "When to Use Data Loader". https://developer.salesforce.com/docs/atlas.en-us.dataLoader.meta/dataLoader/when_to_use_the_data_loader.htm (accessed 2026-11-15)
[^s2]: Salesforce Developers, "Configure Data Loader". https://developer.salesforce.com/docs/platform/data-loader-impl/guide/configuring-the-data-loader.html (accessed 2026-11-15)
[^s3]: Salesforce Developers, "Considerations for Installing Data Loader". https://developer.salesforce.com/docs/platform/data-loader-impl/guide/installing-the-data-loader.html (accessed 2026-11-15)
[^s4]: Salesforce Developers, "Data Loader Command-Line Operations and Exit Codes". https://developer.salesforce.com/docs/platform/data-loader-impl/guide/loader-operations.html (accessed 2026-11-15)
[^s5]: Trailhead, "Import Data". https://trailhead.salesforce.com/content/learn/modules/lex_implementation_data_management/lex_implementation_data_import (accessed 2026-11-15)
