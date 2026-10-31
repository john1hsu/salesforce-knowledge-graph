---
id: kt:roll-up-summary-field
type: Feature
title: Roll-Up Summary Field
aliases: [rollup summary field, roll-up summary, RSF, declarative roll-up]
domain: data-model
summary: >-
  A read-only custom field on the master side of a master-detail relationship that aggregates related detail records
  with COUNT, SUM, MIN or MAX, optionally filtered, and is recalculated by the platform during the save process.
release: "Winter '27"
status: current
broader: [kt:object-relationships]
related: [kt:order-of-execution, kt:data-skew]
relations:
  - {predicate: dependsOn, object: kt:lookup-vs-master-detail}
  - {predicate: alternativeTo, object: kt:record-triggered-flow}
  - {predicate: alternativeTo, object: kt:apex-triggers}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: causes, object: kt:record-locking}
sources:
  - id: s1
    title: "Implement Roll-Up Summary Fields (Formulas and Validations module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/point_click_business_logic/roll_up_summary_fields
    type: official-learning
    accessed: 2026-10-31
  - id: s2
    title: "Increase the Maximum Limit of Roll-Up Summary Fields on Salesforce Objects"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000386702&language=en_US&type=1
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "Triggers and Order of Execution (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s4
    title: "CustomField (Metadata API Developer Guide, API v30.0)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.188.0.api_meta.meta/api_meta/customfield.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s5
    title: "A Declarative Rollup Summary Tool for Force.com Lookup Relationships"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2018/07/a-declarative-rollup-summary-tool-for-force-com-lookup-relationships
    type: official-blog
    accessed: 2026-10-31
  - id: s6
    title: "How to create and deploy Salesforce roll-up summary fields"
    publisher: Gearset
    url: https://gearset.com/blog/salesforce-roll-up-summary-field-deployment/
    type: partner
    accessed: 2026-10-31
created: 2026-10-31
---

# Roll-Up Summary Field

A roll-up summary field is a custom field type that computes a value from a set of child records and stores the result on their parent. Where an ordinary formula field only looks at values inside its own record, a roll-up aggregates across the detail records shown in a related list, for example totalling every Opportunity Amount on an Account.[^s1] The field always lives on the master object, and the child records must be linked to it directly through a master-detail relationship.[^s1]

## How it works

An admin creates the field in Object Manager by choosing the Roll-Up Summary data type, then picking the summarized (detail) object, the roll-up type and, where needed, the field to aggregate.[^s1] Four roll-up types exist. COUNT tallies related records. SUM adds number, currency or percent values. MIN and MAX return the lowest or highest number, currency, percent, date or date/time value.[^s1] Optional filter criteria restrict which children are included in the calculation.[^s4]

In metadata, the field is a `CustomField` whose `summaryOperation` takes the values Count, Min, Max or Sum. `summarizedField` names the detail field being aggregated and may be empty only for a count. `summaryForeignKey` points at the master-detail field on the child, and `summaryFilterItems` holds the filter conditions.[^s4]

Recalculation is part of the save pipeline. After a detail record is saved, the platform recalculates the roll-up on the parent, and the parent then runs through its own save procedure. If that parent update changes a grandparent that also carries a roll-up, the grandparent is recalculated and saved in turn.[^s3] Those steps are skipped during a recursive save.[^s3]

## Limits and gotchas

- An object starts with an allocation of 25 roll-up summary fields. Salesforce Support can raise it, but 40 per object is a hard ceiling.[^s2]
- Only COUNT, SUM, MIN and MAX are available. There is no native average, text concatenation or mode.[^s6]
- Gearset reports several filter restrictions. Long text areas, multi-select picklists, cross-object formulas and relative date literals such as "last 90 days" cannot be used as filter criteria.[^s6]
- Once saved, the summarized object cannot be changed, and fields that the roll-up references cannot be deleted while it exists.[^s6]
- With advanced currency management enabled, some currency roll-ups such as Opportunity Amount on Account are unavailable. Trailhead advises disabling it if Amount does not appear as a field to aggregate.[^s1][^s6]
- Deployments fail unless the master-detail field, the summarized field and any filter fields travel with the roll-up, a frequent trap with change sets.[^s6]
- Every child save also updates the parent, which adds work to bulk loads and concentrates writes on popular parents.[^s3][^s6]

## When to use it (and when not)

Prefer a native roll-up whenever the relationship is master-detail and one of the four operations suffices. It needs no code, is maintained by the platform and can be edited later without a redeploy.[^s1][^s5] Lookup relationships have no native roll-ups, a long-standing gap. Teams have filled it with Apex triggers running SOQL aggregate queries, or with the open-source Declarative Lookup Rollup Summaries tool. That tool stores roll-up definitions as records and generates a small trigger. It can calculate in real time or on a schedule through batch jobs, trading immediacy for headroom against query-row limits.[^s5] Record-triggered flows are another declarative option, at the cost of maintaining the aggregation logic yourself.[^s5][^s6]

## Connections

A roll-up summary field is a specialised kind of **object relationship** feature, so that concept is its broader node.[^s1] It **depends on** the master-detail side of **lookup vs. master-detail**: without a master-detail link the field type is not offered.[^s1] Its recalculation is a defined step in the save **order of execution**, which is why parent and grandparent saves cascade from a child edit.[^s3] It is defined through `CustomField` in the **Metadata API**, which is how it is deployed between orgs.[^s4] For lookups or unsupported aggregates, **Apex triggers** and **record-triggered flows** are the usual **alternatives**.[^s5] Because each child save writes to the parent, heavy fan-in **causes** **record locking** contention and aggravates **data skew**.[^s3][^s6]

## Sources

[^s1]: Trailhead, "Implement Roll-Up Summary Fields". https://trailhead.salesforce.com/content/learn/modules/point_click_business_logic/roll_up_summary_fields (accessed 2026-10-31)
[^s2]: Salesforce Help, "Increase the Maximum Limit of Roll-Up Summary Fields on Salesforce Objects". https://help.salesforce.com/s/articleView?id=000386702&language=en_US&type=1 (accessed 2026-10-31)
[^s3]: Salesforce Developers, "Triggers and Order of Execution". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm (accessed 2026-10-31)
[^s4]: Salesforce Developers, "CustomField" (Metadata API Developer Guide, API v30.0). https://developer.salesforce.com/docs/atlas.en-us.188.0.api_meta.meta/api_meta/customfield.htm (accessed 2026-10-31)
[^s5]: Salesforce Developers Blog, "A Declarative Rollup Summary Tool for Force.com Lookup Relationships". https://developer.salesforce.com/blogs/2018/07/a-declarative-rollup-summary-tool-for-force-com-lookup-relationships (accessed 2026-10-31)
[^s6]: Gearset, "How to create and deploy Salesforce roll-up summary fields". https://gearset.com/blog/salesforce-roll-up-summary-field-deployment/ (accessed 2026-10-31)
