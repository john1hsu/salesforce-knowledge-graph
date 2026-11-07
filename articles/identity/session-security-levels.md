---
id: kt:session-security-levels
type: SecurityControl
title: Session Security Levels
aliases: [session security level, high assurance session, high-assurance session, Session Security Level Required at Login, step-up authentication, Auth.SessionLevel]
domain: identity
summary: >-
  The Standard or High Assurance level Salesforce assigns to each user session based on how the user logged in,
  which admins use to demand step-up verification (usually MFA) or block access for sensitive setup areas,
  reports and dashboards, connected apps and profiles.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:multi-factor-authentication, kt:single-sign-on-saml, kt:connected-apps, kt:asynchronous-apex]
relations:
  - {predicate: integratesWith, object: kt:login-flows}
  - {predicate: configuredVia, object: kt:profiles}
  - {predicate: mitigates, object: kt:account-takeover}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "Session Security"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.security_overview_sessions.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-07
  - id: s2
    title: "Require High-Assurance Session Security for Sensitive Operations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.security_auth_require_ha_session.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-07
  - id: s3
    title: "Manage Session Policies for a Connected App"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.connected_app_manage_session_policies.htm&type=5
    type: official-docs
    accessed: 2026-11-07
  - id: s4
    title: "Use Salesforce MFA for SSO (Salesforce Orgs)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.mfa_sso_logins.htm&type=5
    type: official-docs
    accessed: 2026-11-07
  - id: s5
    title: "Salesforce Session Security: \"High Assurance\" Level Blocks Asynchronous Apex Processing"
    publisher: Salesforce Help (Knowledge Article)
    url: https://help.salesforce.com/s/articleView?id=000392426&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-07
  - id: s6
    title: "SessionLevel Enum (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_enum_Auth_SessionLevel.htm
    type: official-docs
    accessed: 2026-11-07
created: 2026-11-07
---

# Session Security Levels

Every time a user logs in to Salesforce they receive a session, and every login method carries a default security level of either **Standard** or **High Assurance**.[^s1] Admins can move login methods between the two levels in Session Settings and then write policies that reserve specific resources for High Assurance sessions, so the level becomes a reusable signal of how strongly a user proved who they are.[^s1] In practice the High Assurance column is where multi-factor authentication (MFA) lives: a user who started with a Standard session and then completes MFA is raised to High Assurance.[^s4]

## How it works

The Apex `Auth.SessionLevel` enum exposes three values. `STANDARD` and `HIGH_ASSURANCE` correspond to the two columns in the org's Session Security Levels settings; `LOW` can be set through the API but is not used in the Salesforce UI, and users given it get reduced, unpredictable functionality.[^s6] Code can change a session's level with `Auth.SessionManagement.setSessionLevel`, which is how custom authentication logic can grant or withhold High Assurance.[^s6]

The level is then enforced at several points:

- **Sensitive setup areas.** Under Identity Verification, the Session Security Level Policies list operations such as Manage Users, Manage Sharing, Manage Roles, Manage Permission Sets and Profiles, Manage Connected Apps, Manage Encryption Keys, Manage Data Export, Manage IP Addresses, Manage Password Policies and View Health Check. For each, an admin can require a High Assurance session (step-up) or block access outright.[^s2]
- **Reports and dashboards.** The same policy can protect reports and dashboards, also configurable from the Reports and Dashboards Access Policies page.[^s2]
- **Connected apps.** A connected app's session policies can require a high assurance session, either raising the session level through verification at login or blocking the app entirely; blocking ends all existing user sessions with that app.[^s3]
- **Profiles.** A profile's "Session Security Level Required at Login" setting can demand High Assurance for every login by users with that profile.[^s5]

Step-up policies can also force periodic re-verification: the Step-Up Authentication Period setting makes affected users verify again after a set number of minutes, up to two hours.[^s2]

## Limits and gotchas

- Users who already hold a High Assurance session are not prompted again for the protected operations in that session.[^s2]
- You can require High Assurance for Manage Permission Sets and Profiles and Manage Users, but you cannot block those two areas. Changing these policies needs the Customize Application permission; the feature is available in all editions.[^s2]
- For connected apps, only OAuth flows with a user approval step (web server, user-agent and refresh token) can satisfy a High Assurance requirement. API logins through flows without that step, such as the JWT bearer flow, are blocked when the app demands High Assurance.[^s3]
- Setting a profile's required login level to High Assurance supports only synchronous, UI-driven work. Salesforce documents that future methods, Apex callouts and `getContentAsPDF()` fail for such users, because asynchronous contexts like future, batch and scheduled jobs can't satisfy the session requirement. The recommended fix is to grant the "Multi-Factor Authentication for User Interface Logins" permission instead and set the profile requirement back to None.[^s5]

## When to use it (and when not)

Use session-level policies for targeted step-up: making admins re-prove identity before touching sharing, encryption keys or user management, or before exporting data through reports.[^s2] For single sign-on, Salesforce now recommends putting the SSO provider in the Standard column and Multi Factor Authentication in the High Assurance column, then enabling "Use Salesforce MFA for this SSO Provider", so SSO users reach High Assurance only after MFA. Before Summer '23 this was done by requiring High Assurance on profiles, an approach Salesforce now advises removing because the session-level method works better, including with Visualforce.[^s4] Requiring High Assurance at login on a profile is the bluntest tool and the one most likely to break asynchronous Apex.[^s5]

## Connections

Session security levels are a control within **Salesforce Identity**, sitting alongside session timeouts, IP restrictions and the Session Management page as part of session security.[^s1] They are the mechanism through which **multi-factor authentication** is applied to **single sign-on** logins and to sensitive operations.[^s4][^s2] **Connected apps** consume the level through their session policies, which is why integration flows without user approval cannot meet a High Assurance requirement.[^s3] The level is configured per **profile** at login and can be adjusted in Apex, which is how **login flows** and other custom authentication steps interact with it.[^s5][^s6] Requiring High Assurance helps guard against **account takeover** of privileged users, but a profile-wide requirement conflicts with **asynchronous Apex**, so architects preparing for the **Identity and Access Management Architect** certification should know when to choose policy-level step-up over profile-level enforcement.[^s2][^s5]

## Sources
[^s1]: Salesforce Help, "Session Security". https://help.salesforce.com/s/articleView?id=sf.security_overview_sessions.htm&language=en_US&type=5 (accessed 2026-11-07)
[^s2]: Salesforce Help, "Require High-Assurance Session Security for Sensitive Operations". https://help.salesforce.com/s/articleView?id=xcloud.security_auth_require_ha_session.htm&language=en_US&type=5 (accessed 2026-11-07)
[^s3]: Salesforce Help, "Manage Session Policies for a Connected App". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.connected_app_manage_session_policies.htm&type=5 (accessed 2026-11-07)
[^s4]: Salesforce Help, "Use Salesforce MFA for SSO (Salesforce Orgs)". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.mfa_sso_logins.htm&type=5 (accessed 2026-11-07)
[^s5]: Salesforce Help, "Salesforce Session Security: High Assurance Level Blocks Asynchronous Apex Processing". https://help.salesforce.com/s/articleView?id=000392426&language=en_US&type=1 (accessed 2026-11-07)
[^s6]: Salesforce Developers, "SessionLevel Enum". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_enum_Auth_SessionLevel.htm (accessed 2026-11-07)
