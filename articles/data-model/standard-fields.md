---
id: kt:standard-fields
type: Feature
title: Standard Fields
aliases: [standard field, system fields, audit fields, SystemModstamp, Set Audit Fields upon Record Creation]
domain: data-model
summary: >-
  The fields Salesforce defines on objects itself rather than an admin adding them: the read-only system and audit
  fields present on most objects (Id, IsDeleted, CreatedById, CreatedDate, LastModifiedById, LastModifiedDate,
  SystemModstamp) plus the prebuilt business fields of standard objects, such as an account's Rating.
release: "Winter '27"
status: current
broader: [kt:standard-objects, kt:object-relationships]
related: [kt:custom-fields, kt:record-name-field, kt:data-migration-strategy, kt:data-loader, kt:field-history-tracking, kt:change-data-capture]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: dependsOn, object: kt:field-level-security}
  - {predicate: contrastsWith, object: kt:custom-fields}
  - {predicate: enables, object: kt:query-optimizer-selectivity}
sources:
  - id: s1
    title: "System Fields (Object Reference for the Salesforce Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/system_fields.htm
    type: official-docs
    accessed: 2026-11-28
  - id: s2
    title: "Indexes (Best Practices for Deployments with Large Data Volumes)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-infrastructure-indexes.html
    type: official-docs
    accessed: 2026-11-28
  - id: s3
    title: "Id Class (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apex/apex_methods_system_id.htm
    type: official-docs
    accessed: 2026-11-28
  - id: s4
    title: "Work with Standard and Custom Fields (Customize a Salesforce Object)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/customize-a-salesforce-object/standard-custom-fields
    type: official-learning
    accessed: 2026-11-28
created: 2026-11-28
---

# Standard Fields

Standard fields are the fields Salesforce itself defines on an object, as opposed to the `__c` custom fields an admin adds. They come in two families. The first is the set of **system fields**: read-only fields found on most objects that the platform updates automatically during API operations.[^s1] The second is the prebuilt business fields that ship with standard objects, such as the Rating picklist on Account, which admins can tailor but did not create.[^s4]

## The system and audit fields

The Object Reference lists a common set of system fields that are not repeated in each object's own field list:[^s1]

- **Id**: a globally unique identifier for the record, present on every object and defaulted on create.[^s1]
- **IsDeleted**: true when the record sits in the Recycle Bin, false otherwise.[^s1]
- **CreatedById / CreatedDate**: the user who created the record and when; both are defaulted on create.[^s1]
- **LastModifiedById / LastModifiedDate**: the user who last updated the record and when a user last changed it.[^s1]
- **SystemModstamp**: when a user *or an automated process* last modified the record.[^s1]
- **LastViewedDate / LastReferencedDate**: per-user timestamps of when the current user last viewed the record, or viewed or referenced it via a related record or list view.[^s1]

Audit dates must fall between 1970-01-01T00:00:00Z and 4000-12-31T00:00:00Z GMT, and are shown offset by the user's time zone.[^s1] Each relationship also surfaces a pair of fields, the relationship name and its ID field (for example `Contact` and `ContactId` on Case).[^s1]

In Apex, the Id type exposes helpers such as `to15()`, which converts an 18-character ID into the 15-character case-sensitive form, and `getSObjectType()`, which returns the object token used with describe calls.[^s3]

## LastModifiedDate vs. SystemModstamp

The two timestamps diverge because SystemModstamp also moves when platform processes touch a record, not only users; the Object Reference clarifies that "trigger" here means standard platform functionality, not Apex triggers.[^s1] It also warns that SystemModstamp does not capture every change: when object A derives a value from object B, a change on B updates B's SystemModstamp but not A's.[^s1] Incremental extract jobs that filter on either field should account for both behaviours. Both are cheap to filter on at scale: the large-data-volumes guide lists Systemmodstamp (LastModifiedDate) among the fields indexed by default.[^s2]

## Indexing and selectivity

Salesforce indexes several standard fields on most objects out of the box: RecordTypeId, Division, CreatedDate, Systemmodstamp, Name, Email on contacts and leads, lookup and master-detail foreign keys, and the record ID.[^s2] A filter on a standard indexed field is selective when it matches fewer than 30% of the first million records and 15% of the rest, a looser threshold than the 10% and 5% used for custom indexes.[^s2] Adding a custom index to a standard field requires a Salesforce Support case.[^s2] Some standard fields with special behaviour, such as Opportunity Amount, IsClosed and IsWon, or Lead Status, count as non-deterministic for indexing purposes.[^s2]

## Setting audit fields during migration

Audit fields are normally system-set, but data migrations often need to preserve the source system's creation and modification history. An admin can turn on the "Set Audit Fields upon Record Creation" permission from the User Interface page in Setup, then grant it through a profile or permission set.[^s1] Users with it can set audit fields via the API when *creating* records on objects including Account, Case, Contact, Lead, Opportunity, Task, Event, ContentVersion and custom objects.[^s1] SystemModstamp is the one audit field that can never be set.[^s1] Not every standard object carries every audit field, so the Enterprise WSDL is the reference for which exist on a given object.[^s1]

## Customizing business standard fields

Unlike system fields, business standard fields can be adjusted within limits. The Trailhead project on standard and custom fields relabels Account's Rating as "Prospect Rating" through Rename Tabs and Labels, adds help text, extends its picklist with a new value and sets field-level security on it.[^s4] The same exercise then adds custom fields for data the standard set does not cover, such as a support-plan checkbox and expiration date.[^s4] The practical rule is to reuse a standard field when its meaning fits, because platform features are built around it, and add a custom field only for what is genuinely new.[^s4]

## Connections

Standard fields are part of every [[standard-objects]] definition and contrast with admin-defined [[custom-fields]]; the [[record-name-field]] is one of them.[^s4] Lookup ID fields such as `ContactId` are the visible side of [[object-relationships]].[^s1] Their default indexes underpin [[query-optimizer-selectivity]] and [[custom-indexes]] decisions in [[large-data-volumes]] orgs.[^s2] Audit fields are read with [[soql]] and can be preserved during [[data-migration-strategy]] loads, typically with [[data-loader]], once the audit permission is enabled.[^s1] Access to business standard fields is still governed by [[field-level-security]].[^s4] For a history of value changes beyond the last-modified stamp, see [[field-history-tracking]]; for streaming changes, [[change-data-capture]].[^s1]

## Sources

[^s1]: Salesforce Developers, "System Fields (Object Reference for the Salesforce Platform)". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/system_fields.htm (accessed 2026-11-28)
[^s2]: Salesforce Developers, "Indexes (Best Practices for Deployments with Large Data Volumes)". https://developer.salesforce.com/docs/platform/salesforce-large-data-volumes-bp/guide/ldv-deployments-infrastructure-indexes.html (accessed 2026-11-28)
[^s3]: Salesforce Developers, "Id Class (Apex Reference Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apex/apex_methods_system_id.htm (accessed 2026-11-28)
[^s4]: Trailhead, "Work with Standard and Custom Fields". https://trailhead.salesforce.com/content/learn/projects/customize-a-salesforce-object/standard-custom-fields (accessed 2026-11-28)
