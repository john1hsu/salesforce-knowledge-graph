---
id: kt:email-alerts
type: Feature
title: Email Alerts
aliases: [email alert, Email Alert actions, email alert action, workflow email alert, WorkflowAlert, email alerts and actions]
domain: automation
summary: >-
  Reusable, object-specific email actions defined in Setup that pair an email template with a recipient list,
  extra CC addresses and a sender, and that flows and other automation invoke against one record to send a
  templated notification.
release: "Winter '27"
status: current
broader: [kt:process-automation]
related: [kt:workflow-rules, kt:record-triggered-flow, kt:approval-processes]
relations:
  - {predicate: consumedBy, object: kt:flow-builder}
  - {predicate: integratesWith, object: kt:invocable-actions-api}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: dependsOn, object: kt:email-templates}
  - {predicate: dependsOn, object: kt:organization-wide-email-addresses}
sources:
  - id: s1
    title: "Email Alert Actions (Actions Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_action.meta/api_action/actions_obj_email_alert.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s2
    title: "Simple Email Actions (Actions Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_action.meta/api_action/actions_obj_email_simple.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s3
    title: "Workflow (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_workflow.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s4
    title: "Data and Actions in Flows: Communicate Using the Action Element"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/de/content/learn/modules/data-and-actions-in-flows/communicate-with-users-flow
    type: official-learning
    accessed: 2026-11-12
  - id: s5
    title: "Use an Organization-Wide Address on a Notification (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/cma-customize-email-org-wide-address.html
    type: official-docs
    accessed: 2026-11-12
created: 2026-11-12
---

# Email Alerts

An **email alert** is a reusable email action defined once in Setup for a specific object. It bundles the
email template, the recipients, any extra CC addresses and the sender, so the automation that fires it only
has to say which record the email is about.[^s1][^s3] Email alerts began life as workflow actions, but they are
not workflow rules: Trailhead stresses that actions are not being deprecated along with workflow rules, and
it recommends an email alert as the most fully featured way to send email from a flow.[^s4]

## How it works

In metadata an alert is a `WorkflowAlert` stored in the object's `Workflow` file. Its required fields are a
description, a `protected` flag and a named reference to an email template; `recipients`, `ccEmails`,
`senderType` and `senderAddress` are optional, but either recipients or CC addresses must be set for the
email to go out.[^s3] Merge fields in the template are filled from the record the caller supplies.[^s4]

Recipients are typed rather than typed in. The metadata recognises 18 recipient types, grouped roughly as:[^s3]

- Record-relative people such as the owner, creator, account owner, or the account or opportunity team.[^s3]
- Values read from the record: a contact lookup, a user lookup, or an email field on the object.[^s3]
- Named users, public groups, roles and roles with subordinates, plus portal and partner variants.[^s3]

Up to 5 additional addresses can be added as CC.[^s3] The sender is the current user by default; the
alternatives are the default workflow user or a verified organization-wide address.[^s3] An admin chooses an
organization-wide address as the alert's From Email Address in Setup, and creating such an address requires
the Modify All Data permission.[^s5]

To run an alert, a flow uses the Action element and picks the alert; in a record-triggered flow the
**Send Email Alert** shortcut narrows the action list to email alerts only.[^s4] Through the REST API, the same
alerts appear as custom actions under `/actions/custom/emailAlert`, available from API version 32.0. The only
input is `SObjectRowId`, the record to use, and the action returns no outputs.[^s1]

## Limits and gotchas

- Alerts are entity-specific: an alert built on Case can't be fired for an Account record.[^s1]
- Email sent by alerts is subject to Salesforce's documented daily email limits.[^s1]
- When an alert installed from a package used the default workflow user, its sender becomes the current user.[^s3]
- Lightning email templates aren't packageable, so Salesforce advises Classic templates for alerts you package.[^s3]
- Because the template and recipients live in the alert, a flow can't change them per run; edit the alert instead.[^s1]

## When to use it (and when not)

Use an email alert when the same notification is reused across several automations, or when recipients are
best expressed as roles, teams or record owners rather than computed addresses.[^s3][^s4] The alternative is
the flow **Send Email** action, which takes subject, body and recipients as inputs at run time. It allows up to
150 recipients across its inputs, can log the email to the record's activity timeline and attach files, and
in scheduled flows only accepts an organization-wide sender.[^s2] Its daily limit depends on how it is used:
with a template or activity logging it counts against the single-email limit, otherwise against the workflow
email limit.[^s2]

## Connections

Email alerts are a building block of **process automation** and were originally attached to **workflow
rules**, where the `Workflow` metadata type still stores them alongside the rules that reference them.[^s3]
Today they are mostly consumed by **Flow Builder** flows, such as a **record-triggered flow** using the Send
Email Alert shortcut.[^s4] **Approval processes** are a neighbouring declarative automation tool in the same Setup toolkit.
The **Invocable Actions API** exposes every
alert as a callable custom action, and alerts deploy through the **Metadata API** inside the `Workflow`
type.[^s1][^s3] Each alert depends on an **email template** for its content and can send from an
**organization-wide email address**.[^s3][^s5]

## Sources

[^s1]: Salesforce Developers, "Email Alert Actions (Actions Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_action.meta/api_action/actions_obj_email_alert.htm (accessed 2026-11-12)
[^s2]: Salesforce Developers, "Simple Email Actions (Actions Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_action.meta/api_action/actions_obj_email_simple.htm (accessed 2026-11-12)
[^s3]: Salesforce Developers, "Workflow (Metadata API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_workflow.htm (accessed 2026-11-12)
[^s4]: Trailhead, "Data and Actions in Flows: Communicate Using the Action Element". https://trailhead.salesforce.com/de/content/learn/modules/data-and-actions-in-flows/communicate-with-users-flow (accessed 2026-11-12)
[^s5]: Salesforce Developers, "Use an Organization-Wide Address on a Notification (ISVforce Guide)". https://developer.salesforce.com/docs/platform/isvforce/guide/cma-customize-email-org-wide-address.html (accessed 2026-11-12)
