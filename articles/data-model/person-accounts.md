---
id: kt:person-accounts
type: Feature
title: Person Accounts
aliases: [person account, PersonAccount record type, B2C accounts, consumer accounts, IsPersonAccount]
domain: data-model
summary: >-
  An irreversible org feature that models an individual consumer as a single record combining one Account and one
  person Contact, supporting business-to-consumer data models alongside ordinary business accounts.
release: "Winter '27"
status: current
broader: [kt:standard-objects]
related: [kt:salesforce-sharing-model, kt:contacts-to-multiple-accounts, kt:sales-cloud, kt:experience-cloud-identity, kt:data-migration-strategy]
relations:
  - {predicate: dependsOn, object: kt:record-types}
  - {predicate: dependsOn, object: kt:organization-wide-defaults}
  - {predicate: integratesWith, object: kt:change-data-capture}
  - {predicate: consumedBy, object: kt:financial-services-cloud}
sources:
  - id: s1
    title: "Setting Up Person Accounts (implementation guide)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/impl_person_accounts.pdf
    type: official-docs
    accessed: 2026-11-02
  - id: s2
    title: "SOAP API Developer Guide: Person Account Record Types"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_guidelines_personaccounts.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s3
    title: "Change Data Capture Developer Guide: Creating and Undeleting a Person Account"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/change-data-capture/guide/cdc-standard-objects-person-account-create.html
    type: official-docs
    accessed: 2026-11-02
  - id: s4
    title: "Client Management in Financial Services Cloud: Create Person Accounts for Individual Clients"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/client-management-in-financial-services-cloud/create-person-accounts-for-individual-clients
    type: official-learning
    accessed: 2026-11-02
created: 2026-11-02
---

# Person Accounts

**Person accounts** let a Salesforce org store individual consumers rather than companies. The default account model, business accounts, represents organisations with contacts hanging off them; a person account instead merges selected Account and Contact fields into one record so that a single individual can be sold to or served directly, and both kinds of account can live side by side in the same org.[^s1] The feature is available in Professional, Enterprise, Performance, Unlimited and Developer Editions.[^s1] Industry products lean on it: in Financial Services Cloud each individual client is a person account, giving advisers one record that holds the client's financial picture, with record types used to segment client tiers.[^s4]

## How it works

Under the hood a person account is still two rows. Creating one creates an Account and a matching **person contact**; the person account record types are those whose `IsPersonAccount` flag is true, Salesforce supplies a default called PersonAccount, and admins can add more.[^s2] The person contact's id is held in the account's `PersonContactId` field, and it is the only contact that may be directly associated with that account.[^s2] The person contact can be edited but not created, deleted or re-typed on its own, has no detail page of its own, and is deleted when the account is deleted.[^s2] Users simply see one record: editing it updates both underlying objects, and the record appears in both account and contact list views.[^s4]

Contact fields surface on the account with naming conventions: standard contact fields take a `Person` prefix and custom contact fields gain a `__pc` suffix when read through the Account.[^s3] Field-level security is defined on the Contact field and inherited by its person-account counterpart, which cannot be set differently.[^s2] The checkbox **Is Person Account** is the standard way to separate consumers from businesses in list views, search layouts, rules and reports.[^s1]

## Enabling it

Person accounts are switched on by contacting Salesforce and then completing the setup page, and **once enabled they cannot be turned off**, so Salesforce strongly recommends trialling in a sandbox first.[^s1][^s4] Prerequisites are that at least one business account record type exists, that the organization-wide default for contacts is Controlled by Parent, and that profiles with Read on accounts also have at least Read on contacts.[^s1] After activation, the person account record type must be assigned to the relevant profiles.[^s1]

## Limits and gotchas

Checked this run (Winter '27) against the latest published Salesforce documentation:

- Each person account consumes storage as both an account and a contact, so it costs more than a business account.[^s1]
- Person accounts cannot sit in account hierarchies, cannot relate directly to other accounts or contacts (use Contacts to Multiple Accounts for indirect links), and business-only fields such as Parent Account and contact fields such as Reports To are unsupported.[^s1]
- They merge only with other person accounts, and can be enabled for customer Experience Cloud sites but not partner sites.[^s1]
- In Lightning, a contact lookup does not return person accounts; users must scope the search to Account.[^s1]
- Lightning lead conversion produces a person account when the lead's Company is blank and a business account when it is filled in, so separate lead record types and layouts are advised.[^s1]
- `__pc` custom fields are not supported for Einstein predictions, and Shield Platform Encryption on a field is mirrored between the account and contact sides.[^s1]
- There is no UI to switch a record between business and person types. The API supports it via `update()` or `upsert()` in both directions, but a business account must have exactly one contact, matching owner and currency, and no hierarchy links; workflow rules and validation formulas do not fire during the change.[^s2][^s1]
- Converting via Data Loader drops Account Name from the account and fields such as Phone and Description from the contact unless they are first copied to custom fields.[^s1]
- Change Data Capture emits two events per person account create or undelete: an AccountChangeEvent with account fields plus `Person` and `__pc` fields, and a ContactChangeEvent carrying contact fields with `IsPersonAccount` true.[^s3]

## When to use it (and when not)

Choose person accounts when the business genuinely sells to or services individuals and wants account-centric features (opportunities, cases, assets, campaigns) on the consumer record itself.[^s1] Because enabling is permanent and every downstream integration, AppExchange package and report must handle two record shapes, avoid it for mostly B2B orgs where a handful of individuals can be modelled as contacts under a placeholder or household account. For mixed models, plan lead record types, sharing and data loads up front, since conversion between types is API-only and lossy.[^s1][^s2]

## Connections

Person accounts are a special configuration of the **standard objects** Account and Contact, and they **depend on** **record types** to distinguish consumers from businesses.[^s2] Activation **depends on** the **organization-wide defaults**: contacts must be Controlled by Parent, tying the feature to the **Salesforce sharing model**.[^s1] Indirect links to other people and companies run through **Contacts to Multiple Accounts**.[^s1] The feature **integrates with** **Change Data Capture** through paired account and contact events.[^s3] It is **used by** **Financial Services Cloud** for individual clients[^s4], supports B2C selling in **Sales Cloud** through lead conversion, can back customer users in **Experience Cloud identity** scenarios, and its type-conversion rules matter in any **data migration strategy**.[^s1]

## Sources

[^s1]: Salesforce, "Setting Up Person Accounts (implementation guide)". https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/impl_person_accounts.pdf (accessed 2026-11-02)
[^s2]: Salesforce Developers, "SOAP API Developer Guide: Person Account Record Types". https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_guidelines_personaccounts.htm (accessed 2026-11-02)
[^s3]: Salesforce Developers, "Change Data Capture Developer Guide: Creating and Undeleting a Person Account". https://developer.salesforce.com/docs/platform/change-data-capture/guide/cdc-standard-objects-person-account-create.html (accessed 2026-11-02)
[^s4]: Trailhead, "Client Management in Financial Services Cloud: Create Person Accounts for Individual Clients". https://trailhead.salesforce.com/content/learn/modules/client-management-in-financial-services-cloud/create-person-accounts-for-individual-clients (accessed 2026-11-02)
