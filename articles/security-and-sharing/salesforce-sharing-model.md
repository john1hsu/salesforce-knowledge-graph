---
id: kt:salesforce-sharing-model
type: Concept
title: Salesforce Sharing Model
aliases: [sharing model, record-level security, record-level sharing, record access model, sharing and visibility]
domain: security-and-sharing
summary: >-
  The layered record-level security design of a Salesforce org: organization-wide defaults set a restrictive baseline,
  and ownership, the role hierarchy, sharing rules, manual sharing and Apex managed sharing selectively open access on top.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:role-hierarchy, kt:implicit-sharing, kt:restriction-rules]
relations:
  - {predicate: hasPart, object: kt:organization-wide-defaults}
  - {predicate: hasPart, object: kt:sharing-rules}
  - {predicate: hasPart, object: kt:apex-managed-sharing}
  - {predicate: coveredBy, object: kt:sharing-and-visibility-architect-certification}
sources:
  - id: s1
    title: "Understanding Sharing (Apex Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_bulk_sharing_understanding.htm
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "Overview of Data Security (Data Security module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_overview
    type: official-learning
    accessed: 2026-10-31
  - id: s3
    title: "Control Access to Records (Data Security module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_records
    type: official-learning
    accessed: 2026-10-31
  - id: s4
    title: "Salesforce Data Security Model — Explained Visually"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/developer-relations/2017/04/salesforce-data-security-model-explained-visually
    type: official-blog
    accessed: 2026-10-31
  - id: s5
    title: "Salesforce Certified Platform Sharing and Visibility Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/de/credentials/sharingandvisibilityarchitect
    type: official-learning
    accessed: 2026-10-31
created: 2026-10-31
---

# Salesforce Sharing Model

The sharing model is the record-level layer of Salesforce data security. Trailhead describes four levels at which access is controlled: the organization (who can log in, when and from where), objects, fields, and individual records.[^s2] Object and field permissions, granted mainly through permission sets and permission set groups, decide whether a user can work with a type of data at all; the sharing model then decides which individual rows of that object the user can see or change.[^s2][^s4] The platform evaluates object access first, then field access, then record access, so sharing can never give a user more than their object permissions allow.[^s4][^s3]

## The layers

The model is built as a locked-down baseline plus a set of additive exceptions.[^s2]

- **Organization-wide defaults (OWDs)** set the baseline access a user has to records they do not own: Private, Public Read Only, Public Read/Write, or Controlled by Parent for detail objects. Defaults are set separately for internal and external users.[^s3]
- **Record ownership** gives the owner, which can be a user or, for custom objects, cases and leads, a queue, Full Access to the record.[^s1]
- **The role hierarchy** extends an owner's access to users above them; it is evaluated at runtime rather than stored as share rows, and it can be switched off per custom object.[^s1]
- **Sharing rules** are automatic exceptions that open records to public groups or roles, either based on who owns them or on field criteria; guest user rules extend read-only access to unauthenticated site visitors.[^s2][^s4]
- **Manual sharing** lets a record owner share one record ad hoc, for example to cover a colleague's absence; it is only offered when the OWD is Private or Public Read Only.[^s2][^s4]
- **Apex managed sharing** lets developers write share rows in code for logic the declarative tools cannot express.[^s1][^s4]

Every layer above the OWD only adds access, which is why Trailhead's guidance is to begin with the most restrictive defaults and open data up selectively.[^s2][^s3] To choose an object's default, it suggests identifying the most restricted user and asking whether there is any record of that object they should not see, or should not edit.[^s3]

## How access is stored and resolved

Most sharing for an object lives in a related share object (for example `AccountShare`), which works like an access control list. Each row carries a reason, exposed as `rowCause` in Apex and the API, such as `Owner`, `Rule`, `Manual`, `Team`, `ImplicitChild` or a developer-defined Apex sharing reason.[^s1] Access levels are Private (`None`, used only on `AccountShare`), Read Only (`Read`), Read/Write (`Edit`) and Full Access (`All`); when several grants apply, the most permissive one wins.[^s1]

The grant types are grouped by who maintains them. Managed sharing (ownership, hierarchy, rules, teams, territory rules) is calculated by the platform and cannot be edited directly through the UI, SOAP API or Apex. User-managed sharing is manual sharing. Apex managed sharing can be added or changed only by users with Modify All Data.[^s1]

## Gotchas

- Full Access can only come from managed sharing; a manual share cannot grant it.[^s1]
- Manual shares are deleted when the record owner changes, whereas Apex managed shares survive an ownership change or the owner's deactivation.[^s1]
- Apex sharing reasons and Apex sharing recalculation are available only for custom objects.[^s1]
- Sharing rules cannot be packaged, and criteria-based sharing rules cannot be created or tested from Apex.[^s1]
- A detail object in a master-detail relationship has no OWD of its own; it inherits the parent's setting.[^s3]
- Clearing Grant Access Using Hierarchies on a custom object limits access to owners and users reached by other sharing features.[^s3]

## When to use which tool

Use OWDs to express the strictest rule that holds for every record, the role hierarchy for vertical management access, sharing rules for repeatable lateral or criteria-driven exceptions, manual sharing for one-off cases, and Apex managed sharing only when access depends on logic such as a field pointing at a user.[^s4][^s2] The Salesforce developer blog's worked example layers all of these for a single sales executive: owned records, her reps' records via the hierarchy, lateral rules to a service team, a criteria rule for one city's accounts, and a trigger that shares premium accounts with a service lead.[^s4]

## Connections

The sharing model is part of the broader **Salesforce platform** security architecture.[^s2] It **has parts** **organization-wide defaults**, **sharing rules** and **Apex managed sharing**, alongside the **role hierarchy**, which supplies vertical access.[^s1][^s3] Platform-calculated grants such as `ImplicitChild` and `ImplicitParent` connect it to **implicit sharing** between accounts and their children.[^s1] Designing it at scale is the subject of the Salesforce **Certified Platform Sharing and Visibility Architect** credential, which covers scalable, high-performing solutions for sharing and visibility requirements.[^s5]

## Sources

[^s1]: Salesforce, "Understanding Sharing (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_bulk_sharing_understanding.htm (accessed 2026-10-31)
[^s2]: Trailhead, "Overview of Data Security (Data Security module)". https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_overview (accessed 2026-10-31)
[^s3]: Trailhead, "Control Access to Records (Data Security module)". https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_records (accessed 2026-10-31)
[^s4]: Salesforce Developers Blog, "Salesforce Data Security Model — Explained Visually". https://developer.salesforce.com/blogs/developer-relations/2017/04/salesforce-data-security-model-explained-visually (accessed 2026-10-31)
[^s5]: Trailhead, "Salesforce Certified Platform Sharing and Visibility Architect". https://trailhead.salesforce.com/de/credentials/sharingandvisibilityarchitect (accessed 2026-10-31)
