---
id: kt:omni-channel
type: Feature
title: Omni-Channel
aliases: [Salesforce Omni-Channel, Enhanced Omni-Channel, Omni-Channel routing]
domain: clouds-and-products
summary: >-
  Service Cloud's declarative work-routing engine, which pushes calls, messages, chats, cases and other records to
  available, qualified service reps based on queues, skills, capacity and presence.
release: "Winter '27"
status: current
broader: [kt:service-cloud]
related: [kt:flow-builder, kt:skills-based-routing, kt:agentforce]
relations:
  - {predicate: partOf, object: kt:service-cloud}
  - {predicate: dependsOn, object: kt:queues}
  - {predicate: configuredVia, object: kt:presence-configuration}
  - {predicate: governedBy, object: kt:omni-channel-limits}
  - {predicate: integratesWith, object: kt:agentforce}
sources:
  - id: s1
    title: "Route Work with Omni-Channel"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.omnichannel_intro.htm&type=5
    type: official-docs
    accessed: 2026-10-30
  - id: s2
    title: "Routing Configuration Settings"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=service.service_presence_routing_configuration_settings.htm&type=5
    type: official-docs
    accessed: 2026-10-30
  - id: s3
    title: "Routing Model Options for Omni-Channel"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=service.service_presence_routing_options.htm&type=5
    type: official-docs
    accessed: 2026-10-30
  - id: s4
    title: "Create Presence Configurations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=service.service_presence_create_presence_configurations.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-10-30
  - id: s5
    title: "How Does Skills-Based Routing Work?"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=service.omnichannel_how_skills_based_routing_works.htm&type=5
    type: official-docs
    accessed: 2026-10-30
  - id: s6
    title: "Omni-Channel Limit Exceeded Errors and Troubleshooting in Agentforce Service"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000383291&language=en_US&type=1
    type: official-docs
    accessed: 2026-10-30
created: 2026-10-30
---

# Omni-Channel

Omni-Channel is the Service Cloud feature that decides which service rep gets which piece of incoming work. Admins configure it declaratively, without code. It routes work to reps who are available and qualified, tracks how much each rep can take on, and controls which reps handle which kinds of work. It runs in Lightning Experience and Salesforce Classic, in both standard and console apps.[^s1] It handles real-time work such as phone calls, messaging sessions and chats, as well as cases (including those created by Email-to-Case) and other supported objects. Salesforce is retiring the original ("standard") version and automatically upgrading orgs to **Enhanced Omni-Channel**, so new designs should assume the enhanced version.[^s1]

## How it works

Omni-Channel offers several routing styles. **Queue-based routing** sends work to queues whose members are reps. **Skills-based routing** sends work only to reps with the required skills. **Omni-Channel flows** let you build more complex logic, such as skill requirements, screen pops and scheduled routing. **Direct routing** sends an item to a named rep, an Agentforce Service Agent or a bot.[^s1] Reps work from the Omni-Channel utility. There they set their presence status, see incoming and active work, and watch their capacity. Supervisors monitor operations in real time with Command Center for Service.[^s1]

A **routing configuration** tells Omni-Channel how to distribute work from the queues that use it. **Routing Priority** decides which queue is served first, with lower numbers going first. Omni-Channel weighs this priority together with how long each item has waited and which queue members are available.[^s2] **Push Time-Out** sets how long a rep has to accept an item before it goes to someone else and the first rep's status changes. **Capacity Type** marks work as primary, interruptible, or inherited from the service channel. Each item's size, in units or as a percentage of a rep's capacity, sets how much of the rep's capacity it uses.[^s2] The **routing model** then picks among eligible reps. *Least Active* chooses the rep whose current work uses the least capacity. *Most Available* chooses the rep with the most free capacity. If reps are tied, Omni-Channel prefers reps with no active work (earliest Omni-Channel login first), and after that the rep who has gone longest without an assignment.[^s3]

A **presence configuration** sets each rep's total capacity and separate interruptible capacity. It also controls whether work is auto-accepted or can be declined (the two cannot be combined), whether decline reasons are required, which status a rep moves to after a decline or timeout, and an optional after-conversation wrap-up period.[^s4] Each org gets a Default Presence Configuration. Custom configurations can be assigned to profiles or users, and a user-level assignment overrides a profile-level one.[^s4]

## Skills-based routing in practice

With skills-based routing, an item goes to a rep who has every required skill, at the minimum level if one is set, and has capacity free. Among those qualified reps, the routing model breaks the tie. Required skills can be static (set on the routing configuration) or dynamic (added by skills-based routing rules or an Omni-Channel flow).[^s5] You can mark some skills as *additional skills*. These are dropped in priority order when no rep has them all, so work is not stranded. They are reset if the rep declines the item or goes offline.[^s5]

## Limits and gotchas

- A user can belong to only one presence configuration. Assigning a user to a second one silently removes them from the first.[^s4]
- Skills are evaluated when a record enters an Omni-Channel queue. Later edits to the record's skills have no effect until it is assigned to a queue again. If no rep has the required skills, the item is not routed, and supervisors see it on the Skills Backlog tab.[^s5]
- Omni-Channel counts an item as assigned as soon as it is routed, even if the rep declines it. A rep who goes offline and comes back starts a new session, and capacity is recalculated.[^s3]
- Push Time-Out is not supported when a specific rep is required. Without Unified Routing, Amazon Connect caps the value at 20 seconds.[^s2]
- Org-level caps on queued work items per hour and on pending routing requests apply. Their values are published in Salesforce Features and Edition Limits rather than in the troubleshooting article. Once the hourly cap is reached, records are no longer assigned to Omni-Channel queues. Set an **Overflow Assignee** on routing configurations (a user, or a queue without a routing configuration) to catch that overflow.[^s6][^s2]

## When to use it (and when not)

Use Omni-Channel when work must go to reps based on real-time availability and workload. Assignment rules or round-robin queue ownership cannot see whether a rep is online or how busy they are. Use queue-based routing when teams are organized by channel or product. Switch to skills-based routing or Omni-Channel flows when the right rep depends on language, product expertise or other attributes of the record.[^s1][^s5]

## Connections

Omni-Channel is **part of** `kt:service-cloud`. It **depends on** `kt:queues` for queue-based routing, and each rep's capacity and accept or decline behaviour are **configured via** a `kt:presence-configuration`.[^s1][^s4] Its throughput is **governed by** `kt:omni-channel-limits`, the org-wide caps on queued and pending work.[^s6] It is **related** to `kt:skills-based-routing`, one of its routing styles. It is also related to `kt:flow-builder`, because routing logic can be written as Omni-Channel flows.[^s1][^s5] It **integrates with** `kt:agentforce`, since direct routing can send conversations to Agentforce Service Agents.[^s1]

## Sources

[^s1]: Salesforce Help, "Route Work with Omni-Channel". https://help.salesforce.com/s/articleView?language=en_US&id=sf.omnichannel_intro.htm&type=5 (accessed 2026-10-30)
[^s2]: Salesforce Help, "Routing Configuration Settings". https://help.salesforce.com/s/articleView?language=en_US&id=service.service_presence_routing_configuration_settings.htm&type=5 (accessed 2026-10-30)
[^s3]: Salesforce Help, "Routing Model Options for Omni-Channel". https://help.salesforce.com/s/articleView?language=en_US&id=service.service_presence_routing_options.htm&type=5 (accessed 2026-10-30)
[^s4]: Salesforce Help, "Create Presence Configurations". https://help.salesforce.com/s/articleView?id=service.service_presence_create_presence_configurations.htm&language=en_US&type=5 (accessed 2026-10-30)
[^s5]: Salesforce Help, "How Does Skills-Based Routing Work?". https://help.salesforce.com/s/articleView?language=en_US&id=service.omnichannel_how_skills_based_routing_works.htm&type=5 (accessed 2026-10-30)
[^s6]: Salesforce Help, "Omni-Channel Limit Exceeded Errors and Troubleshooting in Agentforce Service". https://help.salesforce.com/s/articleView?id=000383291&language=en_US&type=1 (accessed 2026-10-30)
