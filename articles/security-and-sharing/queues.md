---
id: kt:queues
type: Feature
title: Queues
aliases: [Salesforce queues, queue ownership, case queue, lead queue]
domain: security-and-sharing
summary: >-
  Shared holding areas that can own records such as cases, leads, tasks and custom-object records, so a team of
  members can pick up or be routed the work; each queue is a special Group defined by members, supported objects and
  notification and hierarchy-access settings.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:role-hierarchy, kt:public-groups, kt:service-cloud, kt:approval-processes]
relations:
  - {predicate: enables, object: kt:omni-channel}
  - {predicate: integratesWith, object: kt:assignment-rules}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: coveredBy, object: kt:sharing-and-visibility-architect-certification}
sources:
  - id: s1
    title: "Create Queues"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.setting_up_queues.htm&type=5
    type: official-docs
    accessed: 2026-11-05
  - id: s2
    title: "Queue (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_queue.htm
    type: official-docs
    accessed: 2026-11-05
  - id: s3
    title: "QueueSobject (Salesforce Field Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.sfFieldRef.meta/sfFieldRef/salesforce_field_reference_QueueSobject.htm
    type: official-docs
    accessed: 2026-11-05
  - id: s4
    title: "Manage Cases (Service Cloud for Lightning Experience)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/service_lex/units/service_lex_case_manage
    type: official-learning
    accessed: 2026-11-05
  - id: s5
    title: "Create Routing Configurations for Your Queues"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.service_presence_create_routing_configuration.htm&amp=&type=5
    type: official-docs
    accessed: 2026-11-05
created: 2026-11-05
---

# Queues

A queue is a shared owner for records. Instead of assigning a case or lead to one person, an admin or an automation assigns it to a queue, and the queue's members prioritize and pick up the work as a team. Salesforce places no cap on how many queues an org can create, and each queue gets its own list view, named after the queue's label, where members see the records it currently owns.[^s1] Trailhead's Service Cloud material shows the typical pattern: a specialist team such as a premium-support group works a shared queue of cases from the console's list-view dropdown.[^s4]

## How it works

Under the hood a queue is a Group record of the queue kind, and the object types it can own are stored as QueueSobject rows. Each QueueSobject row links one queue Group (via QueueId) to one object type (via SobjectType), so one queue can serve several objects, including custom objects.[^s3] In Metadata API the Queue type supports Case, ContactRequest, Lead, ServiceContract, Task (from API 48.0) and custom objects; queues deploy as `.queue` files in a `queues` folder and the type is available from API 24.0.[^s2]

Creating a queue in Setup means choosing a label and name, deciding who is emailed when new records arrive, optionally turning on **Grant Access Using Hierarchies**, selecting the supported objects and adding members.[^s1] Members can be individual users, roles, roles with subordinates, public groups, territories, connections or partner users; guest users cannot be members, and adding a role pulls in its subordinates.[^s1] The metadata mirrors this: `queueMembers` holds users, roles, role-and-subordinates (with or without external roles) and public groups, while `doesSendEmailToMembers`, `email` and `doesIncludeBosses` capture notification and hierarchy settings.[^s2]

Records typically reach a queue through rules or routing. Lead and case assignment rules evaluate entries in sort order and can assign the record to a user or a queue, stopping at the first match; activating a rule deactivates the other rules.[^s4] Omni-Channel can also route queued work to reps: admins attach a routing configuration to a queue so the engine knows how to prioritize and size that queue's work items.[^s5]

## Sharing and access

Queue ownership is part of the sharing model. Members can see and take ownership of the queue's records, subject to the object's sharing settings. With Grant Access Using Hierarchies on, users above the members in the role hierarchy also get access, but this is ignored if the object's sharing settings disable hierarchy access. Users with View All or Modify All permissions bypass these rules entirely.[^s1] An org-level setting controls whether new queues start with hierarchy access on. Orgs created before February 8, 2024 should review queues that use role-and-subordinate members after enabling digital experiences.[^s1]

## Limits and gotchas

- Creating or editing queues requires Customize Application plus Manage Public List Views. Editing queues created by others also needs Manage Users.[^s1]
- Work routes only to members, never to their hierarchy managers, even when those managers can see the records.[^s1]
- For task queues, assignment emails are sent only when a task moves from the queue to a specific user.[^s1]
- If a queue serves several object types, such as cases and messaging sessions, routing priority can starve one type unless reps are online for every channel. For contact-center queues, membership is managed on the Contact Center page, not the Queues page.[^s1]
- If a routing configuration on a queue enables skills-based routing rules, the queue's membership no longer decides who gets the work.[^s5]
- The Case page layout properties must check "Assign using active assignment rule" for cases to use the active rule.[^s4]

## When to use it

Use a queue when work belongs to a team rather than a person, such as triage, overflow or a specialist tier, and you want the record parked visibly until someone claims it or Omni-Channel routes it. When you only need extra people to see records, use sharing rules or public groups, because ownership by a queue changes who is accountable.[^s1][^s4]

## Connections

Queues sit under the **Salesforce sharing model** because queue ownership grants access to members and, optionally, to users above them in the **role hierarchy**; members are often added through **public groups**.[^s1] Queues are a common target of **assignment rules**, which they **integrate with**, and they **enable** queue-based routing in **Omni-Channel** within **Service Cloud**.[^s4][^s5] **Approval processes** are a neighbouring work-assignment feature that links here. Queues are **configured via** the **Metadata API** `Queue` type,[^s2] and their access implications fall under the Sharing and Visibility Architect certification.

## Sources
[^s1]: Salesforce Help, "Create Queues". https://help.salesforce.com/s/articleView?language=en_US&id=sf.setting_up_queues.htm&type=5 (accessed 2026-11-05)
[^s2]: Salesforce Developers, "Queue", Metadata API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_queue.htm (accessed 2026-11-05)
[^s3]: Salesforce Developers, "QueueSobject", Salesforce Field Reference. https://developer.salesforce.com/docs/atlas.en-us.sfFieldRef.meta/sfFieldRef/salesforce_field_reference_QueueSobject.htm (accessed 2026-11-05)
[^s4]: Trailhead, "Manage Cases", Service Cloud for Lightning Experience. https://trailhead.salesforce.com/modules/service_lex/units/service_lex_case_manage (accessed 2026-11-05)
[^s5]: Salesforce Help, "Create Routing Configurations for Your Queues". https://help.salesforce.com/s/articleView?language=en_US&id=sf.service_presence_create_routing_configuration.htm&amp=&type=5 (accessed 2026-11-05)
