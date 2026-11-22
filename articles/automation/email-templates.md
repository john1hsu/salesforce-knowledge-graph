---
id: kt:email-templates
type: Feature
title: Email Templates
aliases: [email template, Lightning email templates, Classic email templates, Visualforce email templates, EmailTemplate]
domain: automation
summary: >-
  Reusable, merge-field-driven email bodies and subjects stored as records in Salesforce, in Lightning
  (builder- or HTML-based, optionally with an enhanced letterhead) or Classic (text, HTML, custom or
  Visualforce) form, that users, email alerts, flows and other automation send against a record.
release: "Winter '27"
status: current
broader: [kt:process-automation]
related: [kt:email-alerts, kt:auto-response-rules, kt:record-triggered-flow, kt:flow-versioning, kt:approval-processes]
relations:
  - {predicate: consumedBy, object: kt:email-alerts}
  - {predicate: consumedBy, object: kt:auto-response-rules}
  - {predicate: dependsOn, object: kt:enhanced-letterheads}
  - {predicate: integratesWith, object: kt:visualforce}
sources:
  - id: s1
    title: "Create a Visualforce Email Template (Visualforce Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-pages-developers-guide/guide/pages-email-templates-creating.html
    type: official-docs
    accessed: 2026-11-22
  - id: s2
    title: "EnhancedLetterhead (Object Reference for Salesforce and Lightning Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.228.0.api.meta/api/sforce_api_objects_enhancedletterhead.htm
    type: official-docs
    accessed: 2026-11-22
  - id: s3
    title: "Create Professional Email Letterheads and Templates Easily"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/customize-an-org-to-support-a-new-business-unit/configure-an-email-letterhead-and-template
    type: official-learning
    accessed: 2026-11-22
  - id: s4
    title: "Create Your Email Template (Build an Email Flow for Program Management Module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/build-an-email-flow-for-program-management-module/create-your-email-template
    type: official-learning
    accessed: 2026-11-22
  - id: s5
    title: "Communicate Using the Action Element (Data and Actions in Flows)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/it/content/learn/modules/data-and-actions-in-flows/communicate-with-users-flow
    type: official-learning
    accessed: 2026-11-22
  - id: s6
    title: "Learn MOAR in Winter '21 With Lightning Email Templates"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2020/learn-moar-in-winter-21-with-lightning-email-templates
    type: official-blog
    accessed: 2026-11-22
created: 2026-11-22
---

# Email Templates

An email template is a stored subject and body, with merge fields, that Salesforce fills in from a record when a message is sent. Users insert templates when emailing from a record's Activity tab, and automation such as email alerts reuses them so that the wording lives in one place.[^s3][^s5] Salesforce keeps two families side by side: **Lightning email templates**, created from the Email Templates item in the App Launcher, and **Classic email templates**, managed in Setup, which include Visualforce templates.[^s4][^s1]

## How it works

A Lightning email template is a record with a name, a folder such as Public Email Templates, a subject, an HTML body and an optional **Related Entity Type** that names the object its merge fields draw from.[^s4] Merge fields use triple curly braces, for example the sender's name or a field on the related record, and work in the subject line as well as the body; an Insert merge field button helps build them.[^s4] For a custom object to be chosen as the related entity, it needs Allow Activities enabled in Object Manager.[^s4] Since Winter '21, a drag-and-drop builder produces responsive HTML templates without code, shared across Sales, Service and Marketing, for users with the Access drag-and-drop content builder permission.[^s6]

An **enhanced letterhead** supplies a reusable header and footer. Admins create one from the App Launcher, can place a logo uploaded through Files and add merge fields such as the recipient's first name, and then pick the letterhead on a template.[^s3] In the API it is the EnhancedLetterhead object, available from API version 46.0, with name, description, header and footer fields; it attaches only to Lightning templates that do not use Salesforce Merge Language.[^s2]

A **Visualforce email template** is a Classic template written in markup. The `messaging:emailTemplate` component sets the recipient type, related-to type, subject and language, and separate components define the HTML and plain-text bodies; merge fields such as the recipient's or related record's name can be repeated over child records.[^s1] Templates can be translated by setting the language attribute from a merge field, which requires the Translation Workbench.[^s1]

## Limits and gotchas

- A Visualforce template can be at most 1 MB, its markup must be valid before it saves, and it can't be used for mass email.[^s1]
- The Receiving_User and Sending_User merge fields work only for mass and list email, so they aren't available in Visualforce templates.[^s1]
- A Template Unique Name uses letters, digits and underscores, starts with a letter, and can't end in or double an underscore.[^s1]
- If letterhead content shows an insufficient-privileges error, turn on Folders and Enhanced Sharing under Lightning Email Templates in Setup.[^s3]
- When choosing a template for an email alert, the lookup defaults to Classic templates; switch it to Lightning to see Lightning templates.[^s4]
- Trailhead notes that, from March 2026, sending email needs domain-level and user-level verification, and the module's flow sends no email without that setup.[^s4]

## When to use it (and when not)

Keeping message text in an email template rather than in a flow text template lets admins and users change the wording without editing the flow, and so without spending flow versions; Trailhead points out that only 50 versions of an activated flow are kept.[^s4] For automated sends, Trailhead recommends an email alert called from a flow's Action element, where the related record decides which values fill the merge fields and where the sent email is logged.[^s5] A text template inside the flow is simpler when the message is one-off and tightly coupled to flow variables.[^s4] Choose a Visualforce template when the body needs markup logic such as iterating over related records, and a Lightning template with a letterhead for branded, builder-maintained messages.[^s1][^s3]

## Connections

Email templates sit under **process automation** as the content layer for notifications. **Email alerts** and **auto-response rules** consume them, pairing a template with recipients, and **record-triggered flows** reach them through email alert actions.[^s5][^s4] Storing text in a template rather than the flow eases **flow versioning**.[^s4] Lightning templates depend on **enhanced letterheads** for branding, and Visualforce templates integrate with the **Visualforce** framework.[^s2][^s1] Flows that send notifications often sit beside **approval processes**, which a flow can submit records to in the same Trailhead unit.[^s5]

## Sources

[^s1]: Salesforce Developers, "Create a Visualforce Email Template (Visualforce Developer Guide)". https://developer.salesforce.com/docs/platform/salesforce-pages-developers-guide/guide/pages-email-templates-creating.html (accessed 2026-11-22)
[^s2]: Salesforce Developers, "EnhancedLetterhead (Object Reference for Salesforce and Lightning Platform)". https://developer.salesforce.com/docs/atlas.en-us.228.0.api.meta/api/sforce_api_objects_enhancedletterhead.htm (accessed 2026-11-22)
[^s3]: Trailhead, "Create Professional Email Letterheads and Templates Easily". https://trailhead.salesforce.com/content/learn/projects/customize-an-org-to-support-a-new-business-unit/configure-an-email-letterhead-and-template (accessed 2026-11-22)
[^s4]: Trailhead, "Create Your Email Template (Build an Email Flow for Program Management Module)". https://trailhead.salesforce.com/content/learn/projects/build-an-email-flow-for-program-management-module/create-your-email-template (accessed 2026-11-22)
[^s5]: Trailhead, "Communicate Using the Action Element (Data and Actions in Flows)". https://trailhead.salesforce.com/it/content/learn/modules/data-and-actions-in-flows/communicate-with-users-flow (accessed 2026-11-22)
[^s6]: Salesforce Admins, "Learn MOAR in Winter '21 With Lightning Email Templates". https://admin.salesforce.com/blog/2020/learn-moar-in-winter-21-with-lightning-email-templates (accessed 2026-11-22)
