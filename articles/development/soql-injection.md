---
id: kt:soql-injection
type: Concept
title: SOQL Injection
aliases: [SOQL injection vulnerability, SOSL injection, Apex query injection, insecure database query construction]
domain: development
summary: >-
  A code vulnerability in which user-controlled input is concatenated into a dynamic SOQL (or SOSL) string, letting
  the user alter the query's logic and read records the code never meant to return. The Apex counterpart of SQL
  injection, prevented chiefly with static queries and bind variables, typecasting and allowlisting.
release: "Winter '27"
status: concept
broader: [kt:soql]
related: [kt:dynamic-soql, kt:apex, kt:field-level-security, kt:experience-cloud, kt:appexchange-security-review, kt:code-analyzer]
relations:
  - {predicate: causes, object: kt:data-breach-risk}
  - {predicate: dependsOn, object: kt:salesforce-sharing-model}
sources:
  - id: s1
    title: "SOQL Injection (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/pages_security_tips_soql_injection.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s2
    title: "Mitigate SOQL Injection (Secure Server-Side Development)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/secure-serverside-development/mitigate-soql-injection
    type: official-learning
    accessed: 2026-11-10
  - id: s3
    title: "SOQL Injection Due to Insecure Database Query Construction"
    publisher: Salesforce Developers (ISVforce Guide)
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/secure-code-violation-soql-injection.html
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "Dynamic SOQL (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_dynamic_soql.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s5
    title: "SOQL Injection (Experience Cloud Developer Guide, guest user security)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/communities-dev/guide/communities-dev-security-guest-users-soql-injection.html
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# SOQL Injection

SOQL injection is the Salesforce form of SQL injection: Apex code builds a query string at run time, splices user input into it without validation, and hands it to `Database.query`. Because the input is parsed as query syntax, an attacker can change the query's logic and make the application run a query its author never intended.[^s1] SOQL is a read-only, less expressive language than SQL, so the blast radius is smaller (no stacked `DROP TABLE` statements), but the attack technique is almost identical.[^s1]

## How the attack works

Salesforce's own example is a Visualforce controller that wraps a name parameter in `LIKE '%…%'` and appends a filter for non-deleted contacts. Supplying a crafted value that closes the quote and adds an `OR` clause rewrites the `WHERE` condition, so the query returns every contact, deleted ones included.[^s1] The same pattern applies to numeric filters: if an age value is concatenated without quotes, a payload such as an extra `limit` clause is accepted as SOQL.[^s2]

The impact is amplified by Apex's execution context. Apex queries run in system mode unless told otherwise, ignoring the running user's object and field permissions, so an injected query can expose data that the user could never see through the UI; Salesforce's security review guidance treats this as privilege escalation.[^s3] Guest users on Experience Cloud sites are a particularly exposed audience: the Experience Cloud guide shows an injected `OR` condition returning every account above a revenue threshold despite a permission check in the code.[^s5]

Salesforce distinguishes two variants. In the first, the user supplies an object or field name that the code drops into `SELECT` or `FROM`; in the second, the user supplies a value (or a fragment) for the `WHERE` clause that escapes its quoted string.[^s3]

## Defenses

The guidance across the Apex Developer Guide, Trailhead and the ISVforce Guide converges on a layered set of controls, in rough order of preference:[^s1][^s2][^s3]

- **Static SOQL with bind variables.** Reference input as `:variable` so it is treated as data, never syntax.[^s2]
- **Bind variables in dynamic SOQL.** `Database.queryWithBinds` (API 57.0+) resolves binds from a `Map<String, Object>`.[^s4]
- **Typecasting.** Convert non-text input to Integer, Boolean or Id so malformed values fail before reaching the query.[^s2][^s5]
- **Allowlisting.** Accept only known-good object and field names, for example checked against `Schema.getGlobalDescribe()` plus an accessibility check.[^s3]
- **Escaping as a fallback.** `String.escapeSingleQuotes()` backslash-escapes single quotes, but only protects values inside quotes.[^s2][^s4]
- **Blocklisting (character stripping).** Removing non-word characters helps, but Trailhead ranks it weaker than allowlisting.[^s2]

Bind variables only work in specific positions: search strings in `FIND`, filter literals in `WHERE`, values for `IN`/`NOT IN`, `WITH DIVISION` names, and the numbers in `LIMIT` and `OFFSET`.[^s2] They cannot stand in for field or object names, which is why allowlisting exists.[^s2] In `Database.queryWithBinds`, map keys are matched case-insensitively and keys differing only in case throw a `QueryException`.[^s4]

## Gotchas

Escaping is the most common false comfort. `String.escapeSingleQuotes()` does nothing for an unquoted numeric value, and Trailhead's age example is still injectable after escaping.[^s2] The Experience Cloud guide warns against escaping every input indiscriminately and asks for context-appropriate encoding instead; it also notes that `WITH SECURITY_ENFORCED` is not an injection defense because it only covers the `SELECT` and `FROM` clauses, not `WHERE`.[^s5] Plain `Database.query` also cannot resolve bind expressions on object fields such as `:record.Name__c`; copy the field into a local variable first.[^s4] Since API 55.0, `Database.query` accepts an `AccessLevel` argument; running in `AccessLevel.USER_MODE` enforces the user's object and field permissions, which narrows what an injected query can reveal but does not stop the injection itself.[^s4]

## When it matters

Any Apex that builds query strings from request parameters, Lightning or Visualforce controller inputs, or agent and integration payloads should be reviewed for injection. The ISVforce Guide recommends not letting users supply any query fragment beyond object names, field names and `WHERE` values, and moving genuinely user-composed queries to the REST or SOAP API where the platform enforces the caller's access.[^s3]

## Connections

SOQL injection sits under **SOQL** and is chiefly a hazard of **dynamic SOQL** written in **Apex**.[^s4] It is one of the code violations checked in **AppExchange security review**, and static analysis with **Salesforce Code Analyzer** is a way to catch it before submission.[^s3] Because injected queries bypass object and field permissions in system mode, it undermines **field-level security** and the **sharing model**, and the resulting exposure feeds **data breach risk**.[^s3] Guest-user code on **Experience Cloud** sites is a high-risk place for it.[^s5]

## Sources
[^s1]: Salesforce Developers, "SOQL Injection" (Apex Developer Guide). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/pages_security_tips_soql_injection.htm (accessed 2026-11-10)
[^s2]: Trailhead, "Mitigate SOQL Injection" (Secure Server-Side Development). https://trailhead.salesforce.com/content/learn/modules/secure-serverside-development/mitigate-soql-injection (accessed 2026-11-10)
[^s3]: Salesforce Developers, "SOQL Injection Due to Insecure Database Query Construction" (ISVforce Guide). https://developer.salesforce.com/docs/platform/isvforce/guide/secure-code-violation-soql-injection.html (accessed 2026-11-10)
[^s4]: Salesforce Developers, "Dynamic SOQL" (Apex Developer Guide). https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_dynamic_soql.htm (accessed 2026-11-10)
[^s5]: Salesforce Developers, "SOQL Injection" (Experience Cloud Developer Guide). https://developer.salesforce.com/docs/platform/communities-dev/guide/communities-dev-security-guest-users-soql-injection.html (accessed 2026-11-10)
