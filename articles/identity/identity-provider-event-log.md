---
id: kt:identity-provider-event-log
type: Feature
title: Identity Provider Event Log
aliases: [IdP Event Log, IdpEventLog, IdpEventLog object, Identity Provider error log]
domain: identity
summary: >-
  The Setup page and IdpEventLog object that record successes and failures of single sign-on requests handled
  when Salesforce acts as an identity provider (SAML and OpenID Connect) and of related OAuth authorization and
  token-exchange requests, used to troubleshoot SSO into connected apps.
release: "Winter '27"
status: current
broader: [kt:salesforce-as-identity-provider, kt:salesforce-identity]
related: [kt:login-history, kt:event-monitoring, kt:connected-apps, kt:openid-connect, kt:session-security-levels]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: instanceOf, object: kt:standard-objects}
  - {predicate: dependsOn, object: kt:my-domain}
  - {predicate: contrastsWith, object: kt:login-history}
sources:
  - id: s1
    title: "Use the Identity Provider Event Log"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=identity_provider_error_log.htm&type=0
    type: official-docs
    accessed: 2026-11-21
  - id: s2
    title: "IdpEventLog | Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_idpeventlog.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s3
    title: "IdpEventLog | Salesforce Field Reference Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.sfFieldRef.meta/sfFieldRef/salesforce_field_reference_IdpEventLog.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s4
    title: "Monitor Access to Your Salesforce Orgs and Experience Cloud Sites"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.identity_monitor_access.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-21
created: 2026-11-21
---

# Identity Provider Event Log

The Identity Provider Event Log is the troubleshooting record Salesforce keeps for single sign-on traffic in which Salesforce is the identity provider (IdP). Each entry captures one attempt by a user to reach a service provider through Salesforce, whether it succeeded or failed, so an admin can see why SSO into a connected app broke.[^s1] Under the hood it is the `IdpEventLog` object, which logs problems and successes with inbound SAML or OpenID Connect authentication requests from other app providers and with the outbound SAML responses Salesforce sends; the object has been available since API version 39.0.[^s2] Salesforce groups it with the other access-monitoring tools for orgs and Experience Cloud sites, alongside login history and device tracking.[^s4]

## How it works

Admins open it from Setup by searching Quick Find for "Identity Provider Event Log". The list shows all attempts by default, and a dropdown narrows it to errors only or successes only. The page is available in Lightning Experience and Salesforce Classic, in Developer, Enterprise, Performance, Unlimited and Database.com editions.[^s1] Each row shows the username, usage type, timestamp, entity ID, status and the connected app (service provider) the user tried to reach.[^s1]

The usage type says how the request started: IdP-initiated SAML, SP-initiated SAML, OAuth authorization, or OAuth token exchange.[^s1] In the API these are the `InitiatedBy` values `IdP`, `SP`, `OauthAuthorize` and `OauthTokenExchange`, and a separate `SsoType` picklist marks the protocol as SAML or OpenID Connect.[^s2]

The object's fields include:[^s2][^s3]

- `AppId` (Connected App ID) and `UserId`: the app provider and the user seeking authentication.[^s2]
- `AuthSessionId`: the authentication session the attempt belongs to.[^s2]
- `IdentityUsed`: the username being authenticated, a string of up to 765 characters.[^s2][^s3]
- `SamlEntityUrl` (labelled Entity ID): the SAML provider's authentication URL, up to 1,500 characters.[^s2][^s3]
- `ErrorCode` (labelled Status): a restricted picklist holding `Success` or one of the failure codes.[^s2][^s3]
- `OptionsHasLogoutUrl`: whether the app has a logout URL that users are redirected to on logout.[^s2]
- `Timestamp`: when the event occurred.[^s2]

The object supports only `describeSObjects()`, `query()` and `retrieve()`, so it is read-only from the API and is read with SOQL.[^s2]

## Reading the status codes

The status picklist is what makes the log useful. Codes separate configuration faults from user-level problems.[^s2] Examples: `InvalidSignature` means the SAML assertion signature was wrong; `InvalidSettings` means the IdP certificate is invalid or missing; `InvalidIssuer` and `InvalidSp` point at a misconfigured service provider; `NoAccess` means the user lacks access to that service provider; and `NoUserFedId` means the user has no Federation Identifier when the app expects one.[^s1][^s2] OAuth-side codes include `CodeExpired`, `InvalidCode`, `InvalidClientCredentials` and `InvalidScope`.[^s2] `InvalidSessionLevel` means the connected app's session policy wasn't met, and `NoSubdomain` signals that no My Domain is deployed.[^s1][^s2] `UnknownError` covers failures outside Salesforce, such as a lost connection.[^s1]

## Limits and gotchas

- The Setup page shows only the 50 most recent login attempts; for more, build a custom report.[^s1]
- Defining identity providers and service providers requires the Customize Application permission.[^s1]
- It covers Salesforce acting as IdP for other apps; logins into the org itself are reviewed through Login History.[^s2][^s4]
- The help article doesn't state a retention period, so don't treat the log as a long-term audit trail.[^s1]

## When to use it

Reach for the log first when users report that a "Login to app" link or SP-initiated redirect fails. The status code usually names the fix (certificate, issuer, federation ID or user access) faster than reading raw SAML traces.[^s1] For durable, organization-wide activity monitoring, export data to a SIEM through Event Monitoring instead.[^s4]

## Connections

The log is a diagnostic tool for `kt:salesforce-as-identity-provider` and belongs to the wider `kt:salesforce-identity` toolset.[^s4] Its rows tie each attempt to a connected app (`kt:connected-apps`), and the protocol field distinguishes SAML from `kt:openid-connect`.[^s2] It contrasts with `kt:login-history`: that object records logins into the org, while this one records Salesforce issuing identities to other apps.[^s4] Some failures trace back to `kt:session-security-levels` or a missing `kt:my-domain`.[^s1][^s2] Like other `kt:standard-objects` it can be queried with `kt:soql`, and `kt:event-monitoring` is the heavier option for long-term security analytics.[^s2][^s4]

## Sources

[^s1]: Salesforce Help, "Use the Identity Provider Event Log". https://help.salesforce.com/s/articleView?language=en_US&id=identity_provider_error_log.htm&type=0 (accessed 2026-11-21)
[^s2]: Salesforce Developers, "IdpEventLog | Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_idpeventlog.htm (accessed 2026-11-21)
[^s3]: Salesforce Developers, "IdpEventLog | Salesforce Field Reference Guide". https://developer.salesforce.com/docs/atlas.en-us.sfFieldRef.meta/sfFieldRef/salesforce_field_reference_IdpEventLog.htm (accessed 2026-11-21)
[^s4]: Salesforce Help, "Monitor Access to Your Salesforce Orgs and Experience Cloud Sites". https://help.salesforce.com/s/articleView?id=sf.identity_monitor_access.htm&language=en_US&type=5 (accessed 2026-11-21)
