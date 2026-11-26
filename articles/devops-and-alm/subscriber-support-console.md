---
id: kt:subscriber-support-console
type: Tool
title: Subscriber Support Console
aliases: [Subscriber Support, LMA Subscribers tab, Log in to Subscriber Org]
domain: devops-and-alm
summary: >-
  The part of the License Management App that lets eligible ISV partners look up the orgs that installed their
  managed packages, log in to a subscriber org once a customer grants login access, and switch on namespace debug
  logs to troubleshoot their package in that org.
release: "Winter '27"
status: current
broader: [kt:license-management-app]
related: [kt:second-generation-managed-packages]
relations:
  - {predicate: dependsOn, object: kt:grant-login-access}
  - {predicate: dependsOn, object: kt:multi-factor-authentication}
  - {predicate: configuredVia, object: kt:permission-sets}
  - {predicate: integratesWith, object: kt:apex-logging-and-debug-logs}
  - {predicate: enables, object: kt:isv-customer-debugger}
sources:
  - id: s1
    title: "Troubleshoot Subscriber Issues"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/lma-subscriber-support-overview.html
    type: official-docs
    accessed: 2026-11-26
  - id: s2
    title: "Log In to Subscriber Orgs"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/lma-logging-in-to-sub-org.html
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "Request Login Access from Subscribers"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/lma-requesting-login-access.html
    type: official-docs
    accessed: 2026-11-26
  - id: s4
    title: "Debug Subscriber Orgs"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/apex_debugging_sub_org.htm
    type: official-docs
    accessed: 2026-11-26
  - id: s5
    title: "Customer Support Solutions (App Licensing and Customer Support for AgentExchange)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/appexchange_licensing/appexchange_licensing_support
    type: official-learning
    accessed: 2026-11-26
  - id: s6
    title: "Assign Permissions to the Subscriber Support Console"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/lma-subscriber-org-permissions.html
    type: official-docs
    accessed: 2026-11-26
created: 2026-11-26
---

# Subscriber Support Console

The **Subscriber Support Console** is the troubleshooting side of the License Management App (LMA). It lets eligible Salesforce partners see information about the customers who installed their managed packages and, when a customer allows it, log in to that customer's org to inspect configuration and data and diagnose problems with the package.[^s1] Partners reach it through the **Subscribers** tab of the LMA in their License Management Org (LMO); clicking an org's name opens its subscriber overview.[^s1] The record page for a subscriber org shows company name and contact details, org ID and instance, plus sections for limits, login access, and packages and licensing.[^s5] That contact information can differ from the Lead, Account or Contact records the LMA keeps for the same customer.[^s5]

## How it works

Logging in is a two-sided handshake. The customer first grants access from their personal settings with **Grant Login Access** (or **Grant Account Login Access**), choosing the partner's company and an access duration.[^s3][^s5] The partner then opens the Subscribers tab, searches by subscriber name or org ID, opens the org, and clicks **Login** next to the user who granted access on the Org Details page.[^s2] The partner works with the same permissions as that user, and should log out when done.[^s2] Changes made during the session are written to the subscriber org's audit trail.[^s3]

If the partner's company is missing from the customer's grant list, the documented causes are:

- An administrator has turned off the ability of non-admin users to grant login access.[^s3]
- The user has no license for the package, or the package is licensed to the whole org, so only an admin with Manage Users can grant it.[^s3]
- The org setting **Administrators Can Log in as Any User** is enabled; it must be off for partner grants.[^s3][^s5]

While logged in, a partner can view managed package code and debug logs, view and edit protected custom settings from their packages, and start an ISV Customer Debugger session.[^s4][^s5] Separately, the partner can enable **Subscriber Debug Logs** for a package from the org's Packages & Licensing section in the LMA; in second-generation packaging this switches logging on for every package in that namespace.[^s4]

## Setup and limits

Logging in to subscriber orgs is available in Enterprise, Performance and Unlimited Editions and needs the **Log in to Subscriber Org** permission.[^s2] Salesforce documents a permission set that grants Visualforce page access to `sfLma.LoginToPartnerBT` and `sfLma.SubscriberSupport` plus that system permission, with the License Management App and a default-on Subscribers tab assigned on the profile.[^s6]

- Only subscriber orgs with a Salesforce Platform or full Salesforce license qualify; Government Cloud instances and scratch orgs are excluded.[^s2]
- Since Spring '22, LMO users who use the console must log in to the LMO with multi-factor authentication.[^s2]
- A subscriber that requires MFA receives a notification, and the login waits until they respond.[^s2]
- When Administrators Can Log in as Any User is off, the grant lasts for a limited time and the customer can revoke it whenever they like.[^s3]
- The ISV Customer Debugger allows one session at a time per LMO, runs only in sandboxes, and caps a session at 4 hours.[^s4][^s5]

## Gotchas and good practice

Debug logs enabled for a namespace expose your unobfuscated Apex code to the subscriber, and they stay on until you disable them in the LMA.[^s4] Because a login can give full read/write access to customer data, Salesforce advises limiting the permission to trusted support and engineering staff, logging a case in the LMO before each login as an audit trail, and using the org's My Domain login URL so the LMO session is not logged out.[^s2] To reproduce a production issue without touching live data, Trailhead suggests asking the customer for a full sandbox.[^s5]

## Connections

The console is a part of the **License Management App** and serves partners who ship **first- and second-generation managed packages**.[^s1][^s4] It **depends on** the customer's **Grant Login Access** setting and on **multi-factor authentication** for LMO users, and it is **configured via** a **permission set**.[^s2][^s3][^s6] It **integrates with** **debug logs** through namespace-level Subscriber Debug Logs, and it **enables** the **ISV Customer Debugger**, which partners start from a subscriber sandbox.[^s4][^s5]

## Sources

[^s1]: Salesforce Developers, "Troubleshoot Subscriber Issues". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/lma-subscriber-support-overview.html (accessed 2026-11-26)
[^s2]: Salesforce Developers, "Log In to Subscriber Orgs". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/lma-logging-in-to-sub-org.html (accessed 2026-11-26)
[^s3]: Salesforce Developers, "Request Login Access from Subscribers". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/lma-requesting-login-access.html (accessed 2026-11-26)
[^s4]: Salesforce Developers, "Debug Subscriber Orgs". https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/apex_debugging_sub_org.htm (accessed 2026-11-26)
[^s5]: Trailhead, "Customer Support Solutions". https://trailhead.salesforce.com/content/learn/modules/appexchange_licensing/appexchange_licensing_support (accessed 2026-11-26)
[^s6]: Salesforce Developers, "Assign Permissions to the Subscriber Support Console". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/lma-subscriber-org-permissions.html (accessed 2026-11-26)
