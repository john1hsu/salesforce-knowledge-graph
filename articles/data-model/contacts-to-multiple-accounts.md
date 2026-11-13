---
id: kt:contacts-to-multiple-accounts
type: Feature
title: Contacts to Multiple Accounts
aliases: [AccountContactRelation, Account Contact Relationship, shared contacts, indirect account relationships, relate a contact to multiple accounts]
domain: data-model
summary: >-
  An Account Settings option that lets one contact be related to several accounts: the contact's primary account is a
  direct relationship and every other link is an indirect relationship stored as an AccountContactRelation record.
release: "Winter '27"
status: current
broader: [kt:standard-objects, kt:object-relationships]
related: [kt:person-accounts, kt:junction-object, kt:duplicate-management, kt:salesforce-sharing-model, kt:agentforce-nonprofit]
relations:
  - {predicate: dependsOn, object: kt:salesforce-sharing-model}
  - {predicate: integratesWith, object: kt:change-data-capture}
  - {predicate: consumedBy, object: kt:health-cloud}
  - {predicate: consumedBy, object: kt:experience-cloud}
sources:
  - id: s1
    title: "Considerations for Relating a Contact to Multiple Accounts"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sales.shared_contacts_considerations.htm&type=5
    type: official-docs
    accessed: 2026-11-13
  - id: s2
    title: "Object Reference for the Salesforce Platform: AccountContactRelation"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_accountcontactrelation.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s3
    title: "Accounts and Contacts: Understand Account and Contact Relationships"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/accounts_contacts_lightning_experience/understand-account-and-contact-relationships-lightning
    type: official-learning
    accessed: 2026-11-13
  - id: s4
    title: "Health Cloud Administration: Enable Contacts to Relate to Multiple Accounts"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.health_cloud.meta/null/enable_shared_contacts.htm
    type: official-docs
    accessed: 2026-11-13
created: 2026-11-13
---

# Contacts to Multiple Accounts

**Contacts to Multiple Accounts** lets a single contact be linked to more than one account, so a consultant, board member or care provider who works with several organisations is one record instead of a set of duplicates.[^s3] Every contact still has exactly one account it is most closely tied to, shown in its Account Name field; links to any other accounts are recorded as additional relationships with their own details.[^s3] The feature is available in Salesforce Classic and Lightning Experience, in Contact Manager, Group, Professional, Enterprise, Performance, Unlimited and Developer Editions.[^s1]

## How it works

The account in the contact's Account Name field is the **direct** relationship; every other related account is an **indirect** relationship.[^s1] Each link is a row of the standard **AccountContactRelation** object, available since API version 33.0, which pairs an `AccountId` with a `ContactId`; neither reference can be changed on an existing row.[^s2] The object adds `StartDate`, `EndDate` and `IsActive` so a relationship's history can be kept rather than deleted, a `Roles` multi-select picklist (Decision Maker, Influencer, Technical Buyer and similar values), and a read-only flag marking the relationship to the contact's primary account.[^s2] Admins can edit the Roles values and add custom fields, such as a checkbox for an account's main contact.[^s3]

Saving a non-private contact with an account creates its relationship row immediately, and validation rules and triggers on that row run straight after the contact save; changing the contact's primary account can create or edit a row the same way.[^s2] Since API 37.0, person accounts can take part on either side: as a related contact of a business account, as a related account of a contact, or related to another person account.[^s2] Changes publish as `AccountContactRelationChangeEvent` from API 59.0.[^s2]

On the page layout, an account's Related Contacts list shows both direct and indirect contacts, and a contact's Related Accounts list shows its accounts; the related lists show current and past relationships.[^s3][^s1]

## Enabling it

An admin turns the feature on in Setup under **Account Settings** by selecting **Allow users to relate a contact to multiple accounts**.[^s4] It cannot be enabled through the Metadata API.[^s1] Industry products depend on it: Health Cloud requires the setting because patients are person accounts and a care provider must relate to both an organisation and a patient.[^s4]

## Limits and gotchas

Checked this run (Winter '27) against current Salesforce documentation:

- Disabling the feature deletes every indirect relationship; primary account links survive.[^s1]
- Private contacts (no account) cannot have indirect relationships, because an indirect link needs a primary account first.[^s1]
- Deleting a direct relationship also removes the contact's indirect ones; deleted indirect relationships cannot be restored from the Recycle Bin.[^s1]
- Deleting an account deletes its direct contacts even when they have other account relationships.[^s1]
- Duplicate matching compares only primary accounts, and some lookups and recent-item lists show only direct relationships.[^s1]
- Indirect contacts do not appear in reports built on the standard Accounts and Contacts report type.[^s1]
- Merges are blocked when contacts share an indirect account, or accounts share an indirect contact, until the duplicate link is removed.[^s1]
- The relationship object does not support lookup, master-detail, roll-up summary, long text or rich text fields, nor field history, field sets, approvals or record types.[^s1]
- Users see a related record only with Read access to it, and Experience Cloud users created from such contacts need a sharing set to reach their records.[^s1]
- Microsoft Outlook sync carries only the primary account.[^s1]

## When to use it (and when not)

Use it when real people genuinely hold relationships with several organisations and users need to see those links on both records, with roles and dates, instead of cloning contacts.[^s3] Because the relationship object cannot hold lookups, roll-ups or record types, richer relationship data (for example, a relationship with its own child records or approvals) calls for a custom **junction object** instead.[^s1] Plan reporting, duplicate rules and account-deletion behaviour before enabling it, since standard report types and duplicate matching ignore indirect links.[^s1]

## Connections

The feature extends the **standard objects** Account and Contact and is a specialised many-to-many case of **object relationships**, conceptually similar to a **junction object** but with a fixed, limited schema.[^s2][^s1] It works with **person accounts**, which get their own relationship rows and are evaluated separately during merges.[^s1] It **depends on** the **Salesforce sharing model**, since related records are visible only with read access.[^s1] Its blind spot in **duplicate management** is that only primary accounts are compared.[^s1] It **integrates with** **Change Data Capture** through its change event[^s2], is required by **Health Cloud**[^s4], is consumed by **Experience Cloud** sites with sharing sets[^s1]. The graph's **Agentforce Nonprofit** article relies on these relationship records for its stakeholder model.

## Sources

[^s1]: Salesforce Help, "Considerations for Relating a Contact to Multiple Accounts". https://help.salesforce.com/s/articleView?language=en_US&id=sales.shared_contacts_considerations.htm&type=5 (accessed 2026-11-13)
[^s2]: Salesforce Developers, "Object Reference for the Salesforce Platform: AccountContactRelation". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_accountcontactrelation.htm (accessed 2026-11-13)
[^s3]: Trailhead, "Accounts and Contacts: Understand Account and Contact Relationships". https://trailhead.salesforce.com/content/learn/modules/accounts_contacts_lightning_experience/understand-account-and-contact-relationships-lightning (accessed 2026-11-13)
[^s4]: Salesforce Developers, "Health Cloud Administration: Enable Contacts to Relate to Multiple Accounts". https://developer.salesforce.com/docs/atlas.en-us.health_cloud.meta/null/enable_shared_contacts.htm (accessed 2026-11-13)
