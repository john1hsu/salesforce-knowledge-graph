---
id: kt:cap-theorem
type: ExternalConcept
title: CAP Theorem
aliases: [Brewer's theorem, Brewer's conjecture, consistency availability partition tolerance]
domain: platform-architecture
summary: >-
  The impossibility result, conjectured by Eric Brewer and proved by Gilbert and Lynch in 2002, that a replicated
  read/write service cannot guarantee both linearizable consistency and availability while the network can drop
  messages; later refinements such as PACELC add the consistency-versus-latency trade-off that applies even without partitions.
release: "Winter '27"
status: concept
broader: [kt:distributed-computing]
related: [kt:hyperforce, kt:platform-cache, kt:event-driven-architecture, kt:platform-events, kt:multitenancy]
sources:
  - id: s1
    title: "Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services"
    publisher: Seth Gilbert and Nancy Lynch (ACM SIGACT News, 2002)
    url: https://www.comp.nus.edu.sg/~gilbert/pubs/BrewersConjecture-SigAct.pdf
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s2
    title: "CAP Twelve Years Later: How the \"Rules\" Have Changed"
    publisher: Eric Brewer (IEEE Computer, February 2012)
    url: https://sites.cs.ucsb.edu/~rich/class/cs293b-cloud/papers/brewer-cap.pdf
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s3
    title: "Consistency Tradeoffs in Modern Distributed Database System Design"
    publisher: Daniel J. Abadi (IEEE Computer, February 2012)
    url: https://cs.umd.edu/~abadi/papers/abadi-pacelc.pdf
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s4
    title: "Platform Transformation (Salesforce Architecture Fundamentals)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-transformation
    type: official-docs
    accessed: 2026-11-19
created: 2026-11-19
---

# CAP Theorem

The CAP theorem states that a distributed data service cannot promise all three of **C**onsistency, **A**vailability and **P**artition tolerance at once. Eric Brewer put it forward as a conjecture in his invited talk at the PODC symposium in July 2000, and Seth Gilbert and Nancy Lynch turned it into a proved theorem in a 2002 note in *ACM SIGACT News*.[^s1] Brewer later recalled that the idea dates from autumn 1998 and was first published in 1999.[^s2] For Salesforce architects it is the vocabulary behind many platform behaviours: why some features deliver eventually, why caches can be stale, and why the platform leans on asynchronous messaging.[^s4]

## The formal statement

Gilbert and Lynch pin each letter down precisely. Consistency means an *atomic* (linearizable) object: all operations can be placed in one total order in which each appears to take effect at a single instant, so a read issued after a write finishes must see that write or a newer one.[^s1] They stress that this is narrower than the "C" in ACID transactions.[^s1] Availability means every request reaching a non-failed node eventually gets a response, with no exception for bad network conditions.[^s1] Partition tolerance means the network is allowed to lose any number of messages between nodes; any pattern of loss can be modelled as a temporary partition.[^s1]

Their first theorem shows that, in an asynchronous network, no read/write object can be both available and atomic in every fair execution where messages may be lost.[^s1] The proof idea is short: cut the nodes into two groups that cannot hear each other, let a write complete in one group, then read from the other; to stay available the reader must answer, yet it cannot know about the write, so it returns a stale value.[^s1] A second theorem extends the result to partially synchronous networks where nodes have clocks and messages arrive within a known bound or not at all.[^s1] Dropping any one property makes the other two achievable: a single authoritative node gives consistency without availability, a centralised design on a reliable LAN gives consistency and availability, and web caches illustrate availability with weak consistency.[^s1]

## Beyond "pick two of three"

Brewer's 2012 retrospective argues that the popular "two of three" slogan misleads. Partitions are rare, so a system has no reason to give up consistency or availability while the network is healthy; the choice can be made separately per subsystem, operation, data item or user; and all three properties are matters of degree rather than switches.[^s2] He reframes a partition as a time bound: when an operation cannot reach agreement before its timeout, the system must either cancel it, lowering availability, or proceed and risk inconsistency.[^s2]

His recommended design has three steps: detect the partition, enter an explicit partition mode that restricts risky operations, and run a recovery phase that merges divergent state and compensates for mistakes.[^s2] Techniques include version vectors to identify concurrent updates, commutative or lattice-based data types (CRDTs) that converge automatically, and delaying externally visible actions such as charging a card until recovery.[^s2] His ATM example caps withdrawals during a partition and relies on auditing and fees afterwards, trading strict consistency for revenue-preserving availability.[^s2]

Daniel Abadi's PACELC model adds the trade-off that applies all the time: if there is a **P**artition, choose between **A**vailability and **C**onsistency; **E**lse, choose between **L**atency and **C**onsistency.[^s3] Because high availability requires replicas, keeping replicas strictly consistent costs round trips even in normal operation, and Abadi argues this latency cost has shaped database designs more than CAP itself.[^s3] He classes default Dynamo, Cassandra and Riak as PA/EL, VoltDB/H-Store and Megastore as PC/EC, MongoDB as PA/EC and Yahoo's PNUTS as PC/EL.[^s3]

## Relevance to the Salesforce platform

Salesforce's architecture fundamentals describe Hyperforce in CAP-aware terms. Mission-critical services and data in a Hyperforce instance are replicated across at least three availability zones, and cells act as scale units and blast-radius boundaries.[^s4] The same guidance tells service teams to soften dependencies, noting that a stale cached result is often good enough to keep working, to favour asynchronous, brokered communication that buffers load spikes, and to make calls fault-tolerant with timeouts, circuit breaking and retries with backoff.[^s4] Those are the partition-mode and latency choices Brewer and Abadi describe, applied inside a multitenant service.[^s2][^s3][^s4]

For practitioners, the lesson is to decide per interaction which property matters: a payment confirmation needs consistency and can wait, while a dashboard tile or a cached configuration value can tolerate staleness for speed.[^s2][^s3]

## Connections

The CAP theorem is a core result of **distributed computing**, its broader field.[^s1] **Hyperforce** applies its trade-offs through multi-zone replication and cell boundaries, and **multitenancy** adds tenant-fairness pressure to the same shared infrastructure.[^s4] **Platform Cache** is a deliberate availability-and-latency choice where slightly stale data is acceptable, and **event-driven architecture** and **Platform Events** embody the asynchronous, eventually delivered messaging that Brewer's partition-mode thinking favours.[^s2][^s4]

## Sources

[^s1]: Seth Gilbert and Nancy Lynch, "Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services", ACM SIGACT News, 2002. https://www.comp.nus.edu.sg/~gilbert/pubs/BrewersConjecture-SigAct.pdf (accessed 2026-11-19)
[^s2]: Eric Brewer, "CAP Twelve Years Later: How the \"Rules\" Have Changed", IEEE Computer, February 2012. https://sites.cs.ucsb.edu/~rich/class/cs293b-cloud/papers/brewer-cap.pdf (accessed 2026-11-19)
[^s3]: Daniel J. Abadi, "Consistency Tradeoffs in Modern Distributed Database System Design", IEEE Computer, February 2012. https://cs.umd.edu/~abadi/papers/abadi-pacelc.pdf (accessed 2026-11-19)
[^s4]: Salesforce Architects, "Platform Transformation". https://architect.salesforce.com/fundamentals/platform-transformation (accessed 2026-11-19)
