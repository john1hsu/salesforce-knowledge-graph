---
id: kt:guest-user-record-access
type: SecurityControl
title: Guest User Record Access
aliases: [secure guest user record access, Guest User Security Policy, guest user access controls, unauthenticated guest user access]
domain: security-and-sharing
summary: >-
  The enforced set of controls that limit what unauthenticated visitors to Experience Cloud and Salesforce
  Sites can see and do: Private org-wide defaults for guests, Read Only access granted only through guest user
  sharing rules, no record ownership, and object permissions capped at Read and Create.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model, kt:experience-cloud]
related: [kt:salesforce-sites, kt:share-groups, kt:profiles, kt:field-level-security, kt:view-all-and-modify-all-permissions]
relations:
  - {predicate: dependsOn, object: kt:sharing-rules}
  - {predicate: dependsOn, object: kt:organization-wide-defaults}
  - {predicate: dependsOn, object: kt:apex-security-with-sharing}
  - {predicate: contrastsWith, object: kt:manual-sharing}
  - {predicate: contrastsWith, object: kt:apex-managed-sharing}
  - {predicate: mitigates, object: kt:data-breach-risk}
sources:
  - id: s1
    title: "Securely Share Your Experience Cloud Sites with Guest Users"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/communities_secure_guest_users.pdf
    type: official-docs
    accessed: 2026-11-26
  - id: s2
    title: "Give Guest Users Access to Read Records (Experience Cloud Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/communities-dev/guide/communities-dev-give-guest-users-read-access-to-records.html
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "Give Guest Users Access to Create Records (Experience Cloud Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/communities-dev/guide/communities-dev-give-guest-users-access-to-create-records.html
    type: official-docs
    accessed: 2026-11-26
  - id: s4
    title: "Give Guest Users Access to Update Records (Experience Cloud Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/communities-dev/guide/communities-dev-give-guest-users-access-to-update-records.html
    type: official-docs
    accessed: 2026-11-26
  - id: s5
    title: "Unauthenticated Guest User Guidelines (Experience Cloud Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/communities-dev/guide/communities-dev-security-guest-user-guidelines.html
    type: official-docs
    accessed: 2026-11-26
created: 2026-11-26
---

# Guest User Record Access

Every public Experience Cloud site and Salesforce Site runs anonymous traffic as a single **guest user**, governed by the site's guest user profile. Because anything that user can reach is reachable by anyone on the internet, Salesforce wraps the guest user in a fixed set of record access controls, centred on the **Secure guest user record access** setting in Sharing Settings. Salesforce now treats this setting as on by default and not something an admin can turn off in orgs with Experience Cloud sites.[^s1]

## How it works

With secure guest access in force, the platform applies several rules at once:[^s1]

- Org-wide defaults for guest users are Private on every object and can't be raised; detail objects controlled by their parent resolve to Private too.[^s1]
- Guests can't be added to queues or public groups, and existing memberships are not cleaned up automatically, so review them.[^s1]
- Guests can't be granted access through manual sharing or Apex managed sharing.[^s1]
- The only declarative way to open records is a **guest user sharing rule**, a criteria-based rule that grants Read Only at most.[^s1]

Guest user sharing rules count toward the per-object allowance of 50 criteria-based sharing rules. Salesforce warns that such a rule exposes every matching record to anyone, without further checks, so the criteria should be as narrow as the use case allows.[^s1]

Record ownership is also locked down. Since Winter '21, settings that assign new records created by guest users (both in Digital Experiences settings and for Salesforce Sites) to a designated default owner in the org have been enabled and can't be disabled, so the guest user never ends up owning data.[^s1]

## What guests can be allowed to do

Object permissions on the guest profile are capped. Spring '21 stripped Edit, Delete, View All and Modify All from guest profiles and from permission sets assigned to guests, and after Winter '23 only Read and Create object permissions remain available.[^s1] Creating records requires Read on the same object; if guests don't need to read it, the developer guide suggests removing object access and performing the insert from a `without sharing` controller instead.[^s3]

Updates are the hardest case. Sharing rules can't give a guest update access, and with secure guest access enabled, update-level permission checks fail, so standard Lightning components that need edit rights simply don't render.[^s4] The supported pattern is a server-side action running in system context that validates the request, restricts which fields change, and confirms the caller is entitled to that record, for example by checking an encrypted token issued when the record was created.[^s4][^s5]

## Limits and gotchas

- Code that queries `without sharing` exposes every selected record to the public, so keep such paths small and filter results deliberately.[^s2]
- Lightning components bound to fields enforce CRUD and field-level security, so records not shared with the guest silently fail to display.[^s2]
- Guest sharing rules apply only after the transaction commits, so a with-sharing method can't insert a record and then read it back.[^s3]
- In Flow, a Create Records element doesn't commit until a Screen, Local Action or Pause element runs.[^s3]
- Never send raw record IDs to the browser after a guest creates a record; return an encrypted value instead.[^s3][^s5]
- Salesforce strongly recommends disabling API Enabled on the guest profile unless guests truly need API access.[^s1]

Salesforce also recommends setting most guest object permissions to none, disabling View All Users and Run Flows where unused, restricting guest access to Apex classes, and using `with sharing` on `@AuraEnabled` methods.[^s1]

## When to use it (and when not)

Guest access suits data that is meant to be public, or a form where anonymous visitors only create records, because read access through a guest sharing rule makes matching records public by design.[^s2][^s3] Anything a visitor should see only about themselves, or edit later, belongs behind authentication, where roles, sharing sets and share groups can scope access per user; the guest model has no notion of "my records" beyond what custom token logic provides.[^s4][^s5]

## Connections

Guest user record access is a specialised layer of the `kt:salesforce-sharing-model` applied to `kt:experience-cloud` and `kt:salesforce-sites`.[^s1] It **depends on** `kt:organization-wide-defaults` (forced to Private for guests) and on `kt:sharing-rules`, whose guest variant is the sole declarative grant.[^s1] It **contrasts with** `kt:manual-sharing` and `kt:apex-managed-sharing`, both unavailable for guests, and leans on `kt:apex-security-with-sharing` choices because system-mode code is the escape hatch for create and update.[^s1][^s4] The guest's `kt:profiles` entry and `kt:field-level-security` decide what fields surface, the removal of `kt:view-all-and-modify-all-permissions` is part of the policy, and authenticated high-volume users use `kt:share-groups` instead.[^s1] Together these controls **mitigate** `kt:data-breach-risk` from misconfigured public sites.[^s1][^s2]

## Sources

[^s1]: Salesforce, "Securely Share Your Experience Cloud Sites with Guest Users". https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/communities_secure_guest_users.pdf (accessed 2026-11-26)
[^s2]: Salesforce Developers, "Give Guest Users Access to Read Records". https://developer.salesforce.com/docs/platform/communities-dev/guide/communities-dev-give-guest-users-read-access-to-records.html (accessed 2026-11-26)
[^s3]: Salesforce Developers, "Give Guest Users Access to Create Records". https://developer.salesforce.com/docs/platform/communities-dev/guide/communities-dev-give-guest-users-access-to-create-records.html (accessed 2026-11-26)
[^s4]: Salesforce Developers, "Give Guest Users Access to Update Records". https://developer.salesforce.com/docs/platform/communities-dev/guide/communities-dev-give-guest-users-access-to-update-records.html (accessed 2026-11-26)
[^s5]: Salesforce Developers, "Unauthenticated Guest User Guidelines". https://developer.salesforce.com/docs/platform/communities-dev/guide/communities-dev-security-guest-user-guidelines.html (accessed 2026-11-26)
