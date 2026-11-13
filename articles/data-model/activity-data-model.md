---
id: kt:activity-data-model
type: StandardObject
title: Activity Data Model
aliases: [activities, tasks and events, Task and Event objects, ActivityHistory, OpenActivity, TaskRelation, EventRelation, archived activities]
domain: data-model
summary: >-
  How Salesforce stores activities: the Task and Event standard objects, their relation records (TaskRelation,
  EventRelation), the read-only ActivityHistory and OpenActivity views, and the automatic archiving of old activities.
release: "Winter '27"
status: current
broader: [kt:standard-objects]
related: [kt:polymorphic-relationships, kt:contacts-to-multiple-accounts, kt:sales-cloud, kt:archiving-strategy, kt:data-skew]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: consumedBy, object: kt:change-data-capture}
  - {predicate: configuredVia, object: kt:shared-activities}
sources:
  - id: s1
    title: "Event (Object Reference for the Salesforce Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_event.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s2
    title: "TaskRelation (Object Reference for the Salesforce Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_taskrelation.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s3
    title: "ActivityHistory (Object Reference for the Salesforce Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_activityhistory.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s4
    title: "Archived Activities (Object Reference for the Salesforce Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_guidelines_archive.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s5
    title: "Maximize Sales Productivity: Shared Activities"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/sales_admin_maximize_productivity/units/sales_admin_maximize_productivity_unit_1
    type: official-learning
    accessed: 2026-11-13
  - id: s6
    title: "Shared Activities and Parent Records for Tasks and Events (Change Data Capture Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_standard_objects_task_event_shared.htm
    type: official-docs
    accessed: 2026-11-13
created: 2026-11-13
---

# Activity Data Model

In Salesforce, "activities" is the umbrella term the UI uses for two standard objects: **Task** (a to-do, call or
email log with a status) and **Event** (a calendar entry with a start and an end).[^s1] Around those two objects sits
a small family of supporting records: relation objects that link one activity to many people and records, read-only
views that list a parent record's open and completed activities, and a background archive that moves old activities
out of normal queries.[^s2][^s3][^s4] Admins, developers and data architects meet this model whenever they report on
sales engagement, migrate history from another CRM, or write code that reads a customer's timeline.

## How it works

**Task and Event.** Both objects carry a person reference (Who, a lead or contact) and a record reference (What, such
as an account, opportunity, case or custom object); the mechanics of those polymorphic fields are covered in their own
node.[^s1] Events add timing fields: an all-day flag that switches the event between a date and a date-time, and a
duration expressed either as minutes or as an end date-time, which must agree if both are supplied.[^s1] Salesforce
derives the activity's AccountId from the What record when it is an account or an account child, and otherwise from
the contact in Who.[^s1]

**Relation records.** When Shared Activities is enabled, the links between an activity and its parents are stored as
**TaskRelation** and **EventRelation** rows. Each TaskRelation has a TaskId, a polymorphic RelationId, and an IsWhat
flag that is false for contacts and leads and true for everything else.[^s2] A task can then relate to one lead or up
to 50 contacts, plus a single What record.[^s2] Without Shared Activities, EventRelation only links an event to its
invitees; with it, the same object also carries the event's people and record links.[^s6] Change Data Capture
publishes these link changes on their own TaskRelation and EventRelation change-event channels.[^s6]

**ActivityHistory and OpenActivity.** Each contact shows its related tasks and events in an Open Activities list and
an Activity History list.[^s5] Behind the second sits ActivityHistory, a read-only object listing closed activities
(past events and closed tasks) for a parent record, including those of all related contacts.[^s3] It is read through
a parent-to-child relationship subquery, so the parent record anchors the query.[^s3]

**Archiving.** Salesforce runs a background process that archives activities once they are 365 days old: events by
their activity date, and closed tasks by their due date, or by their created date when no due date is set.[^s4] A
standard `query()` excludes archived rows; `queryAll()` returns them, and filtering on IsArchived isolates
them.[^s4] Archived records can still be updated or deleted, but the IsArchived flag itself is not writable.[^s4]

## Limits and gotchas

- Users without View All Data face strict ActivityHistory rules: one parent record, no WHERE in the subquery, ≤500 rows.[^s3]
- That subquery must also be ordered by ActivityDate descending and then LastModifiedDate descending.[^s3]
- The All Activity History list in the UI shows at most 2,000 records, archived ones included.[^s4]
- Multiday events must be enabled in Activity Settings, and a single event cannot span more than 14 days.[^s1]
- With Shared Activities on, TaskRelation does not support triggers, workflow or validation rules.[^s2]
- Lightning event series (IsRecurrence2) and Classic recurring events (IsRecurrence) cannot both be set on one event.[^s1]
- Private events are hidden from other users' calendar views and cannot be linked to accounts, contacts or opportunities.[^s1]
- Shared Activities can take up to 48 hours to enable, and only Salesforce Support can turn it off again.[^s5]

## When to use it (and when not)

Activities are the right home for discrete, user-facing interactions that should appear on a record's activity
timeline and in the Open Activities and Activity History lists of every related contact.[^s5] Because they archive
after a year and are awkward to query in bulk without View All Data, they are a poor fit for high-volume machine
events or long-term analytics; plan an export or archiving strategy before relying on years of activity
history.[^s4][^s3] Enable Shared Activities when one meeting genuinely involves several contacts, since that choice is
hard to reverse.[^s5]

## Connections

The activity objects are part of the **standard objects** catalog, and their Who and What fields are the canonical
example of **polymorphic relationships**.[^s1] **Shared Activities**, configured in Activity Settings, is what turns
the relation objects on and widens the person side of the model, much as **Contacts to Multiple Accounts** widens the
account side of a contact.[^s5][^s2] Developers read activities with **SOQL** subqueries, while **Change Data
Capture** streams both activity changes and relation changes to subscribers.[^s3][^s6] The one-year archive ties
activity design to an org's **archiving strategy**, and the heavy activity volumes typical of **Sales Cloud** orgs can
concentrate many children on one account, a form of **data skew**.[^s4]

## Sources

[^s1]: Salesforce Developers, "Event (Object Reference for the Salesforce Platform)". https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_event.htm (accessed 2026-11-13)
[^s2]: Salesforce Developers, "TaskRelation (Object Reference for the Salesforce Platform)". https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_taskrelation.htm (accessed 2026-11-13)
[^s3]: Salesforce Developers, "ActivityHistory (Object Reference for the Salesforce Platform)". https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_activityhistory.htm (accessed 2026-11-13)
[^s4]: Salesforce Developers, "Archived Activities (Object Reference for the Salesforce Platform)". https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_guidelines_archive.htm (accessed 2026-11-13)
[^s5]: Trailhead, "Maximize Sales Productivity: Shared Activities". https://trailhead.salesforce.com/modules/sales_admin_maximize_productivity/units/sales_admin_maximize_productivity_unit_1 (accessed 2026-11-13)
[^s6]: Salesforce Developers, "Shared Activities and Parent Records for Tasks and Events (Change Data Capture Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_standard_objects_task_event_shared.htm (accessed 2026-11-13)
