---
id: kt:fixture-record-locking
title: Record Locking
summary: Row-level locks taken on records and their parents during saves, and the UNABLE_TO_LOCK_ROW errors they cause.
expect: none
---
# Record Locking

When a transaction updates a record, the database holds a row lock on it until the transaction commits. Saving a
child in a master-detail relationship also locks the parent, and some lookups lock the referenced record. A second
transaction that needs the same row waits up to about ten seconds and then fails with UNABLE_TO_LOCK_ROW.

Code can request locks explicitly with SELECT ... FOR UPDATE, which is useful for counters and allocation logic
where two users must not read the same value. Locks are released at commit or rollback.

Contention shows up in parallel Bulk API loads, in integrations that update the same records, and in roll-up
summary recalculation. Sorting load files by parent ID, using serial mode, keeping transactions short, and
retrying with backoff reduce failures. Approval processes can also lock a record against editing, which is a
different, declarative kind of lock.
