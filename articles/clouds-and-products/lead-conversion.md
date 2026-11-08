---
id: kt:lead-conversion
type: Feature
title: Lead Conversion
aliases: [convert lead, convertLead, Database.convertLead, LeadConvert, Apex Lead Convert, converting leads]
domain: clouds-and-products
summary: >-
  The Sales Cloud process that turns a qualified lead into a contact linked to a new or existing account (or a
  person account), optionally creating or attaching an opportunity, via the Convert Lead window, Apex or the API.
release: "Winter '27"
status: current
broader: [kt:sales-cloud]
related: [kt:business-processes, kt:person-accounts, kt:assignment-rules, kt:record-types, kt:standard-objects, kt:apex]
relations:
  - {predicate: governedBy, object: kt:duplicate-management}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: coveredBy, object: kt:sales-cloud-consultant-certification}
  - {predicate: coveredBy, object: kt:platform-administrator-certification}
sources:
  - id: s1
    title: "Convert Leads"
    publisher: Salesforce Help
    url: https://help.salesforce.com/HTViewHelpDoc?id=leads_convert.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "SOAP API Developer Guide: convertLead()"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_convertlead.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Apex Reference Guide: LeadConvert Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_dml_convertLead.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "Apex Developer Guide: Converting Leads"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/langCon_apex_dml_examples_convertlead.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s5
    title: "Metadata API Developer Guide: LeadConfigSettings"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_leadconfigsettings.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s6
    title: "Leads & Opportunities for Lightning Experience: Create and Convert Leads"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/leads_opportunities_lightning_experience/create-and-convert-leads-lightning
    type: official-learning
    accessed: 2026-11-08
created: 2026-11-08
---

# Lead Conversion

A lead is an early-stage prospect that still needs qualifying; once a rep decides it is a real buying opportunity, they **convert** it. Conversion uses the lead's data to create a business account, a contact and an opportunity, or, when person accounts are enabled and the lead has no company name, a person account plus an opportunity.[^s6] In the Convert Lead window the user can create each record from the lead or pick an existing account and contact the lead already belongs to, then confirm the record owner and the converted status.[^s6] Attached files and notes carry over to the resulting records, and conversion cannot be undone.[^s1]

## How it works

Standard lead fields map automatically to the matching account, contact and opportunity fields; custom lead fields must be mapped by an administrator, or their values are left behind on the lead.[^s4] When a lead is merged into existing records, only empty target fields are filled: existing values, including IDs, are kept. The one exception is the option to overwrite the target contact's Lead Source.[^s2] New records receive the default record type of their new owner, and blank standard picklists receive default values.[^s4]

After conversion the lead is marked converted and drops out of search for users who lack the View and Edit Converted Leads permission; in Lightning Experience it cannot be opened from search results even with that permission.[^s1] Converting requires Create and Edit on leads, accounts and contacts plus the Convert Leads permission; creating a new opportunity also needs Create on opportunities, and attaching an existing one needs Edit.[^s1]

Programmatically, `Database.convertLead()` takes one or a list of `Database.LeadConvert` objects. Only the lead ID and a converted status are required; the status must be a `LeadStatus` value whose `IsConverted` is true, which code typically finds with a SOQL query.[^s3][^s4] Optional setters target an existing account, contact, person account or opportunity, set the owner of new records, name the opportunity, suppress opportunity creation, overwrite lead source and send an owner notification email.[^s3] Each `LeadConvertResult` must be checked individually.[^s2]

## Limits and gotchas

- A single SOAP `convertLead()` call accepts at most 100 LeadConvert objects; if some leads in a bulk call fail, Salesforce retries the conversion lead by lead.[^s2]
- An opportunity is created by default. The opportunity name is limited to 80 characters and defaults to the company name; an existing opportunity ID and a new name are mutually exclusive, and neither may be set when opportunity creation is turned off.[^s2]
- A contact ID requires an account ID; when converting into a person account, set only the account and never a contact ID, or the call errors.[^s3]
- Queue-owned leads need an explicit owner, because accounts and contacts cannot be owned by a queue; the owner you pass never replaces the owner of an existing merged account or contact.[^s4]
- Since API 15.0, strings too long for the target field make the call fail rather than truncate, unless the `AllowFieldTruncationHeader` is used.[^s2]
- Duplicate matching runs during conversion: standard-field matches appear when conversion starts and custom-field rules can add more on Convert, but cross-object duplicate rules do not run. Orgs still on the older PL/SQL conversion engine get fewer options and must ask Support to enable Apex Lead Convert.[^s1]

## Configuration

Lead settings are deployable as the `LeadConfig` settings component (API 47.0 and later). Notable flags include `shouldLeadConvertRequireValidation` (enforce validation rules on conversion, default true), `doesSelectNoOpportunityOnConvertLead` and `doesHideOpportunityInConvertLeadWindow` (steer users away from creating opportunities), `doesPreserveLeadStatus` (default true) and `relateEmailsToContactOnConvert`.[^s5]

## When to use it (and when not)

Use the standard Convert Lead flow when a rep qualifies prospects one at a time and should choose existing accounts, contacts and duplicates interactively.[^s6][^s1] Where reps usually attach leads to deals that already exist, lead settings can default the window to no opportunity or hide the opportunity section entirely.[^s5] Bulk or automated conversion belongs in Apex, where ownership, existing-record matching and converted status are set explicitly in code.[^s3][^s4]

## Connections

Lead conversion is a core `kt:sales-cloud` process. The lead's lifecycle is constrained by the lead process in `kt:business-processes`, and the record types assigned to the new owner decide the layouts of created records (`kt:record-types`).[^s4] Inbound leads are usually routed by `kt:assignment-rules` before conversion, and person-account orgs convert into `kt:person-accounts`.[^s6] Duplicate detection during conversion ties it to `kt:duplicate-management`.[^s1] Programmatic conversion uses `kt:apex` and lead settings ship through the `kt:metadata-api`.[^s3][^s5] The topic appears in the Sales Cloud Consultant and Platform Administrator certifications.

## Sources

[^s1]: Salesforce Help, "Convert Leads". https://help.salesforce.com/HTViewHelpDoc?id=leads_convert.htm (accessed 2026-11-08)
[^s2]: Salesforce Developers, "SOAP API Developer Guide: convertLead()". https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_convertlead.htm (accessed 2026-11-08)
[^s3]: Salesforce Developers, "Apex Reference Guide: LeadConvert Class". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_dml_convertLead.htm (accessed 2026-11-08)
[^s4]: Salesforce Developers, "Apex Developer Guide: Converting Leads". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/langCon_apex_dml_examples_convertlead.htm (accessed 2026-11-08)
[^s5]: Salesforce Developers, "Metadata API Developer Guide: LeadConfigSettings". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_leadconfigsettings.htm (accessed 2026-11-08)
[^s6]: Trailhead, "Leads & Opportunities for Lightning Experience: Create and Convert Leads". https://trailhead.salesforce.com/en/content/learn/modules/leads_opportunities_lightning_experience/create-and-convert-leads-lightning (accessed 2026-11-08)
