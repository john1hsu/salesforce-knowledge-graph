---
id: kt:record-types
type: Feature
title: Record Types
aliases: [record type, RecordType, RecordTypeId, master record type]
domain: data-model
summary: >-
  An object-level configuration that lets one Salesforce object offer different business processes, picklist values
  and page layouts to different users, selected per record through the RecordTypeId field.
release: "Winter '27"
status: current
broader: [kt:metadata-driven-architecture]
related: [kt:person-accounts, kt:page-layouts, kt:business-processes, kt:apex, kt:sandbox-types]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: usedBy, object: kt:person-accounts}
  - {predicate: dependsOn, object: kt:business-processes}
sources:
  - id: s1
    title: "Customize a Salesforce Object: Create Record Types"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/customize-a-salesforce-object/create-record-types
    type: official-learning
    accessed: 2026-11-03
  - id: s2
    title: "Limitations for Creating and Updating Record Types and Picklists"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.recordtypes_picklists_limitations.htm&type=5
    type: official-docs
    accessed: 2026-11-03
  - id: s3
    title: "Metadata API Developer Guide: RecordType"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_recordtype.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s4
    title: "Apex Reference Guide: RecordTypeInfo Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_Schema_RecordTypeInfo.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s5
    title: "Apex Reference Guide: DescribeSObjectResult Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_sobject_describe.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s6
    title: "Tips for Referencing Record Types in Formulas"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=referencing_record_types_in_formulas.htm&type=0
    type: official-docs
    accessed: 2026-11-03
created: 2026-11-03
---

# Record Types

A record type is a named variant of an object that controls which business process, which subset of picklist values and which page layout a user sees for a given record. Salesforce describes the metadata as a way to offer different business processes, picklist values and page layouts to different users of the same object.[^s3] Every record stores its variant in the `RecordTypeId` field; a record with no custom record type falls back to the built-in **Master** record type.[^s4] Record types are available in Professional, Enterprise, Performance, Unlimited and Developer Editions, in both Lightning Experience and Salesforce Classic.[^s2]

## How it works

An admin creates a record type in Object Manager, starting from an existing type (often Master), then gives it a label, an API name, an active flag and a description.[^s1] Three settings make it useful. First, the record type is made available to specific profiles, so only those users can create records of that type. Second, a page layout is assigned to each record type per profile. Third, each picklist field can be trimmed to the values that make sense for that variant.[^s1] In the Trailhead example, a Customer Account and a Partner Account type share the Account object but expose different Industry and Type values and are available to different profiles.[^s1]

For deployments, record types are a Metadata API type that can be created, updated and deleted as part of an object's definition, which lets them travel through source control and sandboxes like other configuration.[^s3]

In code, `Schema.DescribeSObjectResult` exposes record type metadata through `getRecordTypeInfos()`, and through maps keyed by developer name (`getRecordTypeInfosByDeveloperName()`), by ID and by label.[^s5] These methods list record types even when the running user has no access to them.[^s5] Each returned `Schema.RecordTypeInfo` reports whether the type is active, whether it is available to the current user, whether it is the user's default, and whether it is the Master type.[^s4] Because the label from `getName()` can be translated, the developer name is the safer key for logic.[^s4]

## Limits and gotchas

- **Reserved status fields.** A record type can't trim Opportunity Stage, Case or Solution Status, or Lead Status. Those values come from a sales, support, lead or solution *process*, so you assign a different process to each record type instead.[^s2]
- **Volume.** Salesforce recommends staying at no more than 200 record types; beyond that, orgs struggle to manage them.[^s2]
- **Deactivation blockers.** A record type used by an Email-to-Case or On-Demand Email-to-Case routing address can't be deactivated.[^s2]
- **Campaign members.** Campaign member record types can't vary Status, Salutation or Lead Source values, and they are assigned via the Campaign Member Type field on the campaign.[^s2]
- **IDs differ between orgs.** Record type IDs are not the same across orgs, so a formula or flow that hardcodes an ID from a sandbox breaks in production. In formulas, `RecordTypeId` is the most stable reference within one org, while `RecordType.Name` survives cross-org deployment but must be updated if the name changes.[^s6] In Apex, look IDs up by developer name at runtime rather than hardcoding them.[^s5]

## When to use it (and when not)

Use record types when the same object genuinely serves distinct processes or audiences that need different picklist choices, layouts or stage values, such as customer versus partner accounts.[^s1] Each new type adds profile availability, layout assignment and picklist trimming to maintain, which is why Salesforce warns about orgs that sprawl past a couple of hundred types.[^s1][^s2] Profile availability governs which types a user can pick when creating a record; the separate `isAvailable()` and `isDefaultRecordTypeMapping()` checks let custom UIs honour that choice.[^s4] If you need a different status path rather than different choices on ordinary picklists, the answer is a separate business process attached to the record type.[^s2]

## Connections

Record types are configuration data in Salesforce's **metadata-driven architecture** and are **configured via** the **Metadata API**.[^s3] They **depend on** **business processes** for Opportunity, Case, Lead and Solution status values[^s2], and each is paired with **page layouts** per profile.[^s1] Developers read them through **Apex** describe calls and filter on `RecordTypeId` or `RecordType.DeveloperName` in **SOQL**.[^s5] Hardcoded IDs are a classic problem when promoting changes between **sandbox types** and production.[^s6] In this graph, **person accounts** are modelled as a **user** of record types, since that feature distinguishes consumers from business accounts by Account record type.

## Sources

[^s1]: Trailhead, "Customize a Salesforce Object: Create Record Types". https://trailhead.salesforce.com/content/learn/projects/customize-a-salesforce-object/create-record-types (accessed 2026-11-03)
[^s2]: Salesforce Help, "Limitations for Creating and Updating Record Types and Picklists". https://help.salesforce.com/s/articleView?language=en_US&id=sf.recordtypes_picklists_limitations.htm&type=5 (accessed 2026-11-03)
[^s3]: Salesforce Developers, "Metadata API Developer Guide: RecordType". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_recordtype.htm (accessed 2026-11-03)
[^s4]: Salesforce Developers, "Apex Reference Guide: RecordTypeInfo Class". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_Schema_RecordTypeInfo.htm (accessed 2026-11-03)
[^s5]: Salesforce Developers, "Apex Reference Guide: DescribeSObjectResult Class". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_sobject_describe.htm (accessed 2026-11-03)
[^s6]: Salesforce Help, "Tips for Referencing Record Types in Formulas". https://help.salesforce.com/s/articleView?language=en_US&id=referencing_record_types_in_formulas.htm&type=0 (accessed 2026-11-03)
