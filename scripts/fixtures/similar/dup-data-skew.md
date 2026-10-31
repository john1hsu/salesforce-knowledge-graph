---
id: kt:fixture-ownership-and-lookup-skew
title: Ownership and Lookup Skew
summary: When too many child records point at one parent or are owned by one user, saves slow down and lock.
expect: kt:data-skew
---
# Ownership and Lookup Skew

Skew happens when record distribution is lopsided. In account skew, a single account has a huge number of
children such as contacts or opportunities, often more than ten thousand. Every insert or update of a child
briefly locks the parent account, so parallel loads and integrations collide and fail with lock errors.

Ownership skew is the same problem on the owner side: one user, frequently an integration user or a holding
queue owner, owns a very large number of records of one object. When that user moves in the role hierarchy or
when sharing rules change, the platform has to recalculate access for all of those records, which is slow.

Lookup skew appears when many records reference the same record through a lookup field. Each save checks and
locks the referenced record, so high-volume inserts contend for it.

Mitigations include spreading children across several parent records, assigning owners without a role or at the
top of the hierarchy, deferring sharing calculation during big loads, and sequencing batches so they do not hit
the same parent at the same time. Large data volume design reviews should look for skew before go-live.
