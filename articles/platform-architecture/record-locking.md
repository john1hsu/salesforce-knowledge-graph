---
id: kt:record-locking
type: Concept
title: Record Locking
aliases: [row locking, record lock contention, UNABLE_TO_LOCK_ROW, FOR UPDATE locking, pessimistic record locking]
domain: platform-architecture
summary: >-
  The row-level locks Salesforce takes on records (and on related parent and group-membership records) during a
  transaction to keep data referentially intact, and the contention, timeouts and deadlock risks they create under
  concurrent load.
release: "Winter '27"
status: current
broader: [kt:transaction-control, kt:salesforce-platform]
related: [kt:data-skew, kt:roll-up-summary-field, kt:lookup-vs-master-detail, kt:bulk-api-2]
relations:
  - {predicate: queriedWith, object: kt:soql}
sources:
  - id: s1
    title: "Locking Statements (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/langCon_apex_locking_statements.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "Avoiding Deadlocks (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/langCon_apex_deadlocks.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "Salesforce Platform Record Locking and Concurrency"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2014/07/record-locking-cheat-sheet
    type: official-blog
    accessed: 2026-11-01
  - id: s4
    title: "General Guidelines for Data Loads (Bulk API 2.0 and Bulk API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/asynch_api_planning_guidelines.htm
    type: official-docs
    accessed: 2026-11-01
created: 2026-11-01
---

# Record Locking

**Record locking** is the mechanism by which the Salesforce platform prevents two transactions from changing the same database row at the same time. Every DML operation acquires locks on the records it touches, and in many cases on related records as well, so that relationships stay referentially consistent. Most transactions hold their locks only briefly, which is why contention is usually invisible; it becomes a design concern when many concurrent processes converge on the same rows.[^s3] Developers can also take locks explicitly with the SOQL `FOR UPDATE` clause.[^s1]

## How it works

Locks are scoped to a transaction: they are held until the transaction completes and then released. A DML operation on one record also locks records related to it.[^s1] Salesforce's own locking guidance gives concrete examples of these implicit locks: inserting an Opportunity locks its parent Account, a record with a lookup locks the lookup target on insert, and a roll-up summary field causes the master record to be locked when a detail is inserted.[^s3]

A separate, org-wide lock governs sharing infrastructure. Changes to the role hierarchy, territory hierarchy or group membership (public groups, roles, territories and queues) need a group membership lock, and only one such operation can hold it at a time.[^s3]

For explicit control, Apex supports **pessimistic locking**: appending `FOR UPDATE` to an inline SOQL query locks every returned record so the code can read, compute and update without another client changing the values underneath it. Other users can still query the locked rows, but they cannot update them through code or the UI until the lock is released. `ORDER BY` cannot be combined with `FOR UPDATE`.[^s1]

## Limits and gotchas

- **Ten-second wait.** A transaction that tries to lock a record already locked by someone else waits up to 10 seconds; after that a `QueryException` is thrown. An update against a locked record that is not released within 10 seconds fails with a `DmlException` (surfaced to API clients as the familiar `UNABLE_TO_LOCK_ROW` error).[^s1]
- **Callouts release locks.** Making a callout automatically releases `FOR UPDATE` locks, and the debug log records a `FOR_UPDATE_LOCKS_RELEASE` event, so a lock-then-callout-then-update pattern silently loses its protection.[^s1]
- **Lost updates are still possible.** If a competing client's update succeeds just after a lock is released, it can overwrite changes made from a stale copy; the documented fix is for that client to lock and re-query before writing.[^s1]
- **Deadlocks.** Apex reduces deadlock risk by locking parent records before children and by locking multiple records of the same type in ID order, but code that touches several objects should still access tables and rows in the same order everywhere.[^s2]
- **Bulk loads.** Bulk API jobs default to parallel mode, which can produce lock contention. The API waits a few seconds for a lock and then marks the record failed; if more than 100 records in a batch cannot get locks, the rest of the batch is requeued, up to 10 times before the batch is marked permanently failed. Failed records are not retried automatically and must be resubmitted.[^s4]

## When to design for it

Lock contention is a concurrency problem, so the mitigations are about serialising or partitioning work that targets the same rows. Salesforce recommends avoiding simultaneous processes that modify the same records, running group-membership and hierarchy maintenance serially, and watching multithreaded loads whose children share a parent.[^s3] For data loads, group records that reference the same parent into the same batch (the documented example groups AccountTeamMember rows by AccountId), and fall back to serial mode only when batches cannot be reorganised, because serial processing trades throughput for fewer lock timeouts. Creating users, changing ownership of privately shared records, updating user roles and updating territory hierarchies are called out as particularly contention-prone.[^s4] Use `FOR UPDATE` sparingly, for short read-modify-write sequences such as counters or allocation logic, and keep callouts out of the locked window.[^s1]

## Connections

Record locking sits under `kt:transaction-control` because locks live and die with the transaction, and under `kt:salesforce-platform` as a core behaviour of the shared database.[^s1] `kt:data-skew` is the most common root cause of chronic lock contention, since thousands of children pointing at one parent or owner all compete for the same lock.[^s3] `kt:roll-up-summary-field` and the relationship choice described in `kt:lookup-vs-master-detail` determine which parent rows get locked implicitly on child DML.[^s3] `kt:bulk-api-2` is where contention most often surfaces in practice, through parallel batches and their retry rules.[^s4] Explicit locks are requested through `kt:soql` with the `FOR UPDATE` clause.[^s1]

## Sources

[^s1]: Salesforce Developers, "Locking Statements (Apex Developer Guide)", Winter '27. https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/langCon_apex_locking_statements.htm (accessed 2026-11-01)
[^s2]: Salesforce Developers, "Avoiding Deadlocks (Apex Developer Guide)", Winter '27. https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/langCon_apex_deadlocks.htm (accessed 2026-11-01)
[^s3]: Salesforce Developers Blog, "Salesforce Platform Record Locking and Concurrency" (2014). https://developer.salesforce.com/blogs/2014/07/record-locking-cheat-sheet (accessed 2026-11-01)
[^s4]: Salesforce Developers, "General Guidelines for Data Loads (Bulk API 2.0 and Bulk API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/asynch_api_planning_guidelines.htm (accessed 2026-11-01)
