---
id: kt:api-access-control
type: SecurityControl
title: API Access Control
aliases: [API client allowlisting, allowlisted connected apps, limit API access to allowlisted connected apps, connected app API allowlist]
domain: identity
summary: >-
  An org-level Salesforce setting, enabled on request by Customer Support, that blocks API access unless the call comes
  through an admin-approved (allowlisted) connected app, either for all users or only for customer and partner users.
release: "Winter '27"
status: current
broader: [kt:integration-security, kt:connected-apps]
related: [kt:device-flow, kt:experience-cloud-identity, kt:visualforce, kt:external-client-apps]
relations:
  - {predicate: configuredVia, object: kt:permission-sets}
  - {predicate: configuredVia, object: kt:profiles}
  - {predicate: mitigates, object: kt:account-takeover}
  - {predicate: implements, object: kt:principle-of-least-privilege}
sources:
  - id: s1
    title: "Manage API Access"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_api_access_control_about.htm&type=5
    type: official-docs
    accessed: 2026-11-16
  - id: s2
    title: "Restrict Access to APIs with Connected Apps"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_api_access_control_all_users.htm&type=5
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "Restrict Customers and Partners from Accessing APIs"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=security_api_access_control_external_users.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "Salesforce Platform: Security Updates to the \"Use Any API Client\" Permission"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005228838&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "Salesforce Platform: Developer Console Access with API Access Control Enabled"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005132451&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-16
  - id: s6
    title: "Get Ready for Changes to Connected App Usage Restrictions"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2025/get-ready-for-changes-to-connected-app-usage-restrictions
    type: official-blog
    accessed: 2026-11-16
created: 2026-11-16
---

# API Access Control

API Access Control is an org-wide lockdown for Salesforce APIs. When it is on, a user can reach the APIs only through a connected app the admin has approved, instead of through any OAuth client that a user happens to authorize.[^s1] It runs in one of two modes: restrict all users, or restrict only customers and partners.[^s1] It is not self-service: an org must ask Salesforce Customer Support to make the setting available, and it is offered in Professional, Enterprise, Performance, Unlimited and Developer Editions.[^s1][^s2]

## How it works

In the all-users mode, an admin opens **API Access Control** in Setup and selects the option that limits API access for admin-approved users to allowlisted connected apps.[^s2] Every installed connected app then gets the "Admin approved users are pre-authorized" Permitted Users policy, so only users holding that app's assigned profile or permission set can use it.[^s2] Approving more apps later is done on the **Connected Apps OAuth Usage** page: installing an app allowlists it, after which access is granted through profiles or permission sets.[^s2]

In the customers-and-partners mode, external users can call the APIs only through connected apps installed in the Experience Cloud site, while internal users can still reach uninstalled apps.[^s3] The app's own Permitted Users policy can then narrow access further.[^s3]

Both modes offer an optional checkbox that lets Visualforce pages call the APIs. Users still need API Enabled, and only calls from Visualforce domains pass.[^s2][^s3]

## Limits and gotchas

- **Use Any API Client bypasses the allowlist.** Salesforce says to give it only to a few admins, with great caution.[^s2][^s3]
- **Self-authorization changed in December 2025.** Use Any API Client no longer lets a user self-authorize uninstalled apps when the setting is on.[^s4]
- **Approve Uninstalled Connected Apps** is now the permission that allows that self-authorization, meant for trusted admins and developers.[^s4]
- **Integration users are untouched by that change.** Default "force"-namespace permission sets for the Platform Integration User are not affected.[^s4]
- **Salesforce's own apps still need approval.** Salesforce auto-installs connected apps for its common apps, but the admin must approve them and grant access.[^s2]
- **Visualforce and getSessionId() break silently.** Without the Visualforce option, those calls are denied for the restricted users.[^s2][^s3]
- **Missing scopes on an allowlisted app** are fixed by clicking Block and then Unblock on Connected Apps OAuth Usage.[^s2]
- **UI and API can disagree.** For flows other than JWT bearer, the ConnectedApplication object may show a different policy than Setup; treat the UI as authoritative.[^s2]
- **Developer Console can fail to open** when Use Any API Client is granted only through a session-based permission set; grant it via a regular permission set or profile.[^s5]

## When to use it (and when not)

Use it when an org needs a closed list of approved API clients, for example after an audit finds unknown OAuth apps reading data. It goes further than the September 2025 connected app usage restrictions, which blocked uninstalled apps for most users but left previously authorized users working unless the app used the device flow.[^s6] Those baseline restrictions plus "Admin approved users are pre-authorized" on trusted apps may be enough for many orgs; API Access Control adds a hard default-deny across every API client.[^s6][^s2] Before requesting it, inventory every integration on Connected Apps OAuth Usage, because a client whose app is not installed and assigned will stop working.[^s2][^s6]

## Connections

API Access Control is a control within **integration security** and is built on **connected apps**: it changes their Permitted Users policy and allowlists them by installation.[^s2] User access is **configured via** **permission sets** and **profiles** assigned to each app, which **implements** the **principle of least privilege**.[^s2][^s4] It **mitigates** **account takeover** and consent phishing, the risk Salesforce cited for tightening self-authorization.[^s4] It relates to the **OAuth 2.0 device flow**, which lost its grandfathered access under the 2025 usage restrictions, and to **Experience Cloud identity**, since the external-user mode keys on apps installed in a site.[^s6][^s3] It relates to **Visualforce** through the optional Visualforce API access setting.[^s2] It relates to **external client apps**, the OAuth path Salesforce recommends for integrations moving off SOAP API login() before that call retires in Summer '27.[^s4]

## Sources
[^s1]: Salesforce Help, "Manage API Access". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_api_access_control_about.htm&type=5 (accessed 2026-11-16)
[^s2]: Salesforce Help, "Restrict Access to APIs with Connected Apps". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.security_api_access_control_all_users.htm&type=5 (accessed 2026-11-16)
[^s3]: Salesforce Help, "Restrict Customers and Partners from Accessing APIs". https://help.salesforce.com/s/articleView?id=security_api_access_control_external_users.htm&language=en_US&type=5 (accessed 2026-11-16)
[^s4]: Salesforce Help, "Salesforce Platform: Security Updates to the 'Use Any API Client' Permission". https://help.salesforce.com/s/articleView?id=005228838&language=en_US&type=1 (accessed 2026-11-16)
[^s5]: Salesforce Help, "Salesforce Platform: Developer Console Access with API Access Control Enabled". https://help.salesforce.com/s/articleView?id=005132451&language=en_US&type=1 (accessed 2026-11-16)
[^s6]: Salesforce Admins Blog, "Get Ready for Changes to Connected App Usage Restrictions". https://admin.salesforce.com/blog/2025/get-ready-for-changes-to-connected-app-usage-restrictions (accessed 2026-11-16)
