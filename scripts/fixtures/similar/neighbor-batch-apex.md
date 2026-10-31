---
id: kt:fixture-batch-apex
title: Batch Apex
summary: The Database.Batchable interface for processing very large record sets in chunks, each in its own transaction.
expect: none
---
# Batch Apex

Batch Apex processes large data sets by splitting them into chunks. A class implements Database.Batchable with a
start method that returns a QueryLocator or an iterable, an execute method that receives each scope, and a finish
method for post-processing such as sending a summary email or chaining the next job.

Database.executeBatch takes an optional scope size, which defaults to 200 and can be raised to 2,000. Each execute
call is its own transaction, so a failure in one chunk does not roll back the others. Database.Stateful keeps
member variables between chunks, at the cost of serialising state.

Jobs wait in the Apex flex queue and are monitored through AsyncApexJob records or the Apex Jobs page. Batch Apex is
the classic choice for nightly clean-up, recalculation and archiving, often launched by a scheduled class, while
Queueable chains with cursors are a newer alternative for some workloads.
