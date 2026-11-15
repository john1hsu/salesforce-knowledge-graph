---
id: kt:distributed-computing
type: ExternalConcept
title: Distributed Computing
aliases: [distributed systems, distributed system]
domain: platform-architecture
summary: >-
  The study and practice of systems made of spatially separated processes that cooperate only by exchanging messages,
  where message delay, partial failure and the lack of a shared clock force explicit trade-offs between consistency,
  availability and partition tolerance; it is the foundation that cloud platforms such as Hyperforce are built on.
release: "Winter '27"
status: concept
broader: [kt:computer-science]
related: [kt:cloud-computing, kt:hyperforce, kt:multitenancy, kt:event-driven-architecture, kt:platform-cache]
relations:
  - {predicate: hasPart, object: kt:cap-theorem}
sources:
  - id: s1
    title: "Time, Clocks, and the Ordering of Events in a Distributed System"
    publisher: Communications of the ACM (Leslie Lamport)
    url: https://amturing.acm.org/p558-lamport.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s2
    title: "Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services"
    publisher: Seth Gilbert and Nancy Lynch, MIT Laboratory for Computer Science
    url: https://www.cs.princeton.edu/courses/archive/spring22/cos418/papers/cap.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "Perspectives on the CAP Theorem"
    publisher: Seth Gilbert and Nancy A. Lynch (MIT CSAIL)
    url: https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer2.pdf
    type: academic
    accessed: 2026-11-15
  - id: s4
    title: "Platform Transformation (Salesforce Architecture Fundamentals)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-transformation
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "Behind the Scenes of Hyperforce: Salesforce's Infrastructure for the Public Cloud"
    publisher: Salesforce Engineering
    url: https://engineering.salesforce.com/behind-the-scenes-of-hyperforce-salesforces-infrastructure-for-the-public-cloud-429309542d8e
    type: official-blog
    accessed: 2026-11-15
created: 2026-11-15
---

# Distributed Computing

Distributed computing is the branch of computer science concerned with systems whose components run on separate machines and coordinate only by sending messages. Leslie Lamport's 1978 paper in *Communications of the ACM* gives the classic working definition: a collection of spatially separated processes that communicate by exchanging messages, where a system counts as distributed when message transmission delay is not negligible compared with the time between events inside one process.[^s1] Everything a Salesforce architect relies on, from a multi-zone database to an event bus, is an engineered answer to the problems that definition implies.[^s1][^s4]

## Core problems

**No shared clock.** Separate machines cannot agree exactly on physical time, so Lamport defined ordering logically. Event *a* "happened before" event *b* if both occur in one process and *a* comes first, if *a* sends a message that *b* receives, or by transitive chains of those two cases; events not related this way are concurrent, so the relation is only a partial order.[^s1] Logical clocks number events so that causally earlier events always get smaller values, and breaking ties by a fixed process order turns this into a total order that every process can agree on.[^s1] Lamport used that total order to build distributed mutual exclusion, granting a shared resource in request order without a central coordinator.[^s1]

**Partial failure and partitions.** Messages can be delayed or lost, and groups of servers can be cut off from each other. Eric Brewer's conjecture, presented in 2000, says a networked service cannot simultaneously guarantee consistency, availability and partition tolerance.[^s3] Gilbert and Lynch formalised it: consistency means atomic (linearizable) reads and writes, availability means every request to a non-failing node eventually gets a response, and partition tolerance means the network may lose arbitrarily many messages between nodes.[^s2] They proved that no read/write object can guarantee both availability and atomic consistency once messages can be lost, in asynchronous networks and also in partially synchronous ones where nodes have clocks.[^s2]

**Living with the trade-off.** Because a partition forces a choice, practical systems relax one property. Gilbert and Lynch describe weaker models used in practice, including sequential and causal consistency, best-effort consistency in web caching where content can be briefly stale, and tunable "continuous" consistency where the allowed staleness is set at runtime.[^s3] They also note that many real systems partition their guarantees, choosing differently for different data, operations or users.[^s3] On consensus, the same paper notes that agreement is solvable under eventual synchrony only while fewer than half of the servers crash.[^s3]

## Distributed computing in Salesforce's platform

Salesforce's architecture documentation describes Hyperforce as a deliberately distributed design. Each Hyperforce instance maps to one public cloud region and can operate independently, and inside it services are grouped into **cells**, repeatable units that act both as a scale unit and as a blast-radius boundary; a Hyperforce cell corresponds to what was traditionally called a Salesforce instance.[^s4] Mission-critical services and data are replicated across at least three availability zones, and SalesforceDB runs a primary cluster for writes with two standby clusters serving queries, with automated, quorum-monitored failover.[^s4] The engineering blog adds that the zones are close enough to act as one system yet share no single point of failure such as power, cooling or network links.[^s5]

The same documentation lists familiar distributed-systems techniques: timeouts, circuit breakers and retries with backoff on inter-service calls; caching as a soft dependency because stale data is often acceptable; brokered asynchronous messaging over Kafka-backed streams to absorb spikes; and load shedding and tenant-fairness limits to protect shared services.[^s4] Hyperforce also applies immutable infrastructure, replacing rather than patching running resources, and zero-trust rules under which no component gets implicit access to another.[^s5]

## Why it matters to practitioners

The CAP trade-off explains behaviour customers see: asynchronous features deliver eventually rather than instantly, caches may serve slightly old values, and limits exist so one tenant cannot starve others on shared infrastructure.[^s2][^s4] Designing integrations as asynchronous, idempotent and retry-tolerant follows the same principles the platform uses internally.[^s4]

## Connections

Distributed computing is the broader discipline of **cloud computing**, whose pooled, networked resources are distributed systems by Lamport's definition.[^s1] **Hyperforce** is Salesforce's concrete distributed architecture of instances, cells and multi-zone replication, and **multitenancy** relies on the tenant-fairness limits and isolation boundaries described above.[^s4][^s5] **Event-driven architecture** applies the brokered asynchronous messaging pattern, and **Platform Cache** is a caching layer where the weaker, best-effort consistency of the CAP discussion is an accepted trade-off.[^s3][^s4] The **CAP theorem** is a core part of the field.[^s2][^s3]

## Sources

[^s1]: Leslie Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System", Communications of the ACM 21(7), July 1978. https://amturing.acm.org/p558-lamport.pdf (accessed 2026-11-15)
[^s2]: Seth Gilbert and Nancy Lynch, "Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services". https://www.cs.princeton.edu/courses/archive/spring22/cos418/papers/cap.pdf (accessed 2026-11-15)
[^s3]: Seth Gilbert and Nancy A. Lynch, "Perspectives on the CAP Theorem". https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer2.pdf (accessed 2026-11-15)
[^s4]: Salesforce Architects, "Platform Transformation". https://architect.salesforce.com/fundamentals/platform-transformation (accessed 2026-11-15)
[^s5]: Salesforce Engineering, "Behind the Scenes of Hyperforce: Salesforce's Infrastructure for the Public Cloud". https://engineering.salesforce.com/behind-the-scenes-of-hyperforce-salesforces-infrastructure-for-the-public-cloud-429309542d8e (accessed 2026-11-15)
