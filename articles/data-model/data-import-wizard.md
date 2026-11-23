---
id: kt:data-import-wizard
type: Tool
title: Data Import Wizard
aliases: [Import Wizard, Salesforce Data Import Wizard, unified import wizard]
domain: data-model
summary: >-
  Salesforce's browser-based, Setup-launched tool for importing up to 50,000 records at a time from a CSV file into
  accounts, contacts, leads, solutions, person accounts, campaign members and custom objects, with guided field
  mapping, add/update/upsert-style options and asynchronous Bulk API processing.
release: "Winter '27"
status: current
broader: [kt:data-integration]
related: [kt:duplicate-management, kt:data-migration-strategy, kt:person-accounts, kt:custom-objects, kt:standard-objects]
relations:
  - {predicate: alternativeTo, object: kt:data-loader}
  - {predicate: dependsOn, object: kt:bulk-api-1}
  - {predicate: dependsOn, object: kt:validation-rules}
  - {predicate: coveredBy, object: kt:platform-administrator-certification}
sources:
  - id: s1
    title: "Import Data (Data Management module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lex_implementation_data_management/lex_implementation_data_import
    type: official-learning
    accessed: 2026-11-23
  - id: s2
    title: "Use the Data Import Wizard (Import and Export with Data Management Tools project)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/projects/import-and-export-with-data-management-tools/steps/use-the-data-import-wizard
    type: official-learning
    accessed: 2026-11-23
  - id: s3
    title: "Data Import Wizard — Comparison with Existing Wizards (tip sheet)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/226/13/en-us/sfdc/pdf/salesforce_data_import_wizard_tipsheet.pdf
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "Salesforce Certified Platform Administrator Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298966&language=en_US&type=1
    type: official-learning
    accessed: 2026-11-23
  - id: s5
    title: "Practice Data and Analytics Management for Admins"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/administrator-certification-prep-security-and-data-management/review-data-management
    type: official-learning
    accessed: 2026-11-23
created: 2026-11-23
---

# Data Import Wizard

The Data Import Wizard is the point-and-click import tool built into Salesforce Setup. An admin launches it from Setup by searching Quick Find for "Data Import Wizard" and clicking **Launch Wizard**, then walks through choosing an object, uploading a CSV file, mapping columns to fields and starting the job, all in the browser with nothing to install.[^s1][^s2] Salesforce describes its capacity plainly: it can import up to 50,000 records at a time.[^s1][^s3]

## What it can import

The wizard covers a fixed set of standard objects (accounts, contacts, leads, solutions, person accounts and campaign members) plus custom objects; anything outside that list needs Data Loader.[^s1][^s3] Which objects a given user can import also depends on edition, permissions and the org's data storage limits.[^s1] It replaced a family of older per-object import wizards, and Salesforce's tip sheet on the change notes that the unified wizard is enabled automatically for every org.[^s3]

## How it works

1. **Choose data.** Pick the Standard Objects or Custom Objects tab, choose the object, and choose whether to add new records, update existing ones, or do both in one pass; then set the matching criteria the wizard offers for that object.[^s1]
2. **Upload.** Select the CSV file (drag and drop or browse) and a character encoding; the default encoding usually works. The guided project advises commas rather than semicolons as delimiters.[^s1][^s2]
3. **Map fields.** The wizard maps the columns it recognises automatically. Any column left unmapped is skipped, and for accounts and contacts unmapped data can be sent to a note on the record instead.[^s1][^s3]
4. **Review and start.** Check the summary, go back to fix mappings if needed, then click **Start Import**.[^s1]

Matching options vary by object. In the lead import of the guided project, for example, the user matches leads by email and can stamp every new lead with a lead source.[^s2] The tip sheet lists the operation modes the unified wizard supports, such as inserting only, updating only, inserting and updating, and inserting while ignoring matched records.[^s3] When the wizard links contacts to a manager through the Reports To field, it can match only on Salesforce ID or email, not on name.[^s3]

Behind the scenes the job runs asynchronously through the Bulk API rather than writing records synchronously as the old wizards did. Progress appears on the **Bulk Data Load Jobs** page in Setup, and the user who started the import receives an email when it finishes.[^s3][^s1]

## Data preparation and gotchas

- Clean the file first: remove duplicates, delete unneeded rows, fix errors and keep picklist values consistent.[^s1][^s2]
- Make org changes before importing, such as creating custom fields or adding picklist values, and import a small test file first.[^s1]
- Validation rules run on every record, and records that fail are not imported, so admins sometimes deactivate specific rules for a load.[^s1]
- Restricted picklists fall back to the default value or the row fails; multi-select values are separated by semicolons; checkboxes take 1 or 0.[^s1]
- Formula fields are read-only and cannot receive imported values; date and time values must match the importing user's locale format.[^s1]
- If verification fails, the guided project suggests setting the importing user's language and locale to English (United States).[^s2]

## When to use it vs. alternatives

Trailhead frames the choice by volume and automation. The wizard suits loads of fewer than 50,000 records into supported objects when the process does not need to be automated. Data Loader handles 50,000 to 150 million records, works with any object and can be scripted from the command line for jobs such as nightly loads. Beyond 150 million records, Trailhead suggests a Salesforce partner or an AgentExchange solution.[^s1]

## Exam relevance

The Platform Administrator exam guide places import considerations, naming the Import Wizard alongside the data loader, in its Data and Analytics Management section, weighted at 17%.[^s4] Trailhead's matching prep unit lists the Data Import Wizard, Data Loader, duplicate matching and external IDs among the section's key topics.[^s5]

## Connections

The wizard sits under **data integration** (`kt:data-integration`) as the lightest-weight way to load records. It is an **alternative to** `kt:data-loader`, the tool Salesforce recommends once volume, object coverage or automation needs exceed the wizard.[^s1] It **depends on** the asynchronous Bulk API (`kt:bulk-api-1`) for processing[^s3] and on `kt:validation-rules`, which run against every imported row.[^s1] It is related to `kt:duplicate-management`, since de-duplication and matching are part of preparing a load;[^s1][^s5] to `kt:data-migration-strategy`, where it covers small, one-off loads; and to `kt:standard-objects`, `kt:person-accounts` and `kt:custom-objects`, the objects it supports.[^s1] It is **covered by** `kt:platform-administrator-certification`.[^s4]

## Sources
[^s1]: Trailhead, "Import Data (Data Management module)". https://trailhead.salesforce.com/content/learn/modules/lex_implementation_data_management/lex_implementation_data_import (accessed 2026-11-23)
[^s2]: Trailhead, "Use the Data Import Wizard (Import and Export with Data Management Tools project)". https://trailhead.salesforce.com/projects/import-and-export-with-data-management-tools/steps/use-the-data-import-wizard (accessed 2026-11-23)
[^s3]: Salesforce, "Data Import Wizard — Comparison with Existing Wizards (tip sheet)". https://resources.docs.salesforce.com/226/13/en-us/sfdc/pdf/salesforce_data_import_wizard_tipsheet.pdf (accessed 2026-11-23)
[^s4]: Salesforce Help, "Salesforce Certified Platform Administrator Exam Guide". https://help.salesforce.com/s/articleView?id=005298966&language=en_US&type=1 (accessed 2026-11-23)
[^s5]: Trailhead, "Practice Data and Analytics Management for Admins". https://trailhead.salesforce.com/content/learn/modules/administrator-certification-prep-security-and-data-management/review-data-management (accessed 2026-11-23)
