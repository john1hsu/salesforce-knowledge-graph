---
id: kt:fixture-apex-execution-limits
title: Apex Execution Limits
summary: Per-transaction caps that the shared runtime enforces on queries, DML statements, CPU time and heap.
expect: kt:governor-limits
---
# Apex Execution Limits

Because many customers share the same infrastructure, the runtime enforces hard caps on what one transaction may
consume. A synchronous transaction may issue at most 100 SOQL queries and 150 DML statements, retrieve 50,000 rows,
use 10 seconds of CPU and hold 6 MB of heap. Asynchronous transactions get a larger allowance for queries, CPU and
heap.

When code exceeds a cap, the platform throws an exception that cannot be caught, and the whole transaction rolls
back. Typical causes are queries or DML inside loops, triggers that are not bulkified, and recursion between
automation.

Developers check consumption at runtime with the Limits class methods, design triggers to handle 200 records at a
time, move heavy work to Queueable or Batch jobs, and use collections and maps rather than per-record queries.
These caps protect the multitenant platform from a single runaway tenant.
