---
id: kt:oauth-scopes
type: SecurityControl
title: OAuth Scopes in Salesforce
aliases: [OAuth scopes, Salesforce OAuth scopes, scope parameter, commaSeparatedOauthScopes, selected OAuth scopes]
domain: identity
summary: >-
  The named permissions (such as api, refresh_token, web, full, openid and cdp_api) that an external client app or
  connected app is allowed to request, which bound what an issued OAuth access token can be used for on top of, not
  instead of, the user's own Salesforce permissions.
release: "Winter '27"
status: current
broader: [kt:oauth-2-0, kt:api-access-control]
related: [kt:refresh-token-policies, kt:openid-connect, kt:headless-identity, kt:mobile-sdk, kt:data-cloud]
relations:
  - {predicate: implements, object: kt:oauth-2-0}
  - {predicate: configuredVia, object: kt:external-client-apps}
  - {predicate: configuredVia, object: kt:connected-apps}
  - {predicate: consumedBy, object: kt:oauth-2-flows-in-salesforce}
  - {predicate: dependsOn, object: kt:permission-sets}
  - {predicate: implements, object: kt:principle-of-least-privilege}
sources:
  - id: s1
    title: "Scope Parameter Values (Mobile SDK Development Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/mobile-sdk/guide/oauth-scope-parameter-values.html
    type: official-docs
    accessed: 2026-11-26
  - id: s2
    title: "ExtlClntAppOauthSettings (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_extlclntappoauthsettings.htm
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "RFC 6749: The OAuth 2.0 Authorization Framework"
    publisher: IETF
    url: https://datatracker.ietf.org/doc/rfc6749
    type: standards-body
    accessed: 2026-11-26
  - id: s4
    title: "Create an External Client App (Hosted MCP Servers)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/create-external-client-app.html
    type: official-docs
    accessed: 2026-11-26
  - id: s5
    title: "Architecting Inbound Governance with External Client Apps"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/architecting-inbound-governance-external-client-apps/
    type: official-blog
    accessed: 2026-11-26
created: 2026-11-26
---

# OAuth Scopes in Salesforce

An **OAuth scope** is a named permission that says which Salesforce resources an access token may reach: the REST API, Salesforce-hosted web pages, the identity service, Data Cloud APIs and so on.[^s1] Scopes are selected on the server side, in the external client app or connected app, and that selection is the ceiling: whatever a client requests in its `scope` parameter must be a subset of the app's configured scopes.[^s1] Scopes limit what the integration is allowed to do, but Salesforce's architecture guidance stresses that they do not replace the user security model; record and field access still comes from the user's profile and permission sets.[^s5]

## The standard underneath

RFC 6749 defines `scope` as a list of space-delimited, case-sensitive strings whose meaning is set by the authorization server, with each string adding to the access requested.[^s3] The server may ignore all or part of the request according to its policy, and it must return a `scope` parameter in the token response when the scope it granted differs from what was asked for.[^s3] When a client sends no scope at all, the server either applies a documented default or rejects the request as having an invalid scope.[^s3] Salesforce follows that model: the app's configured scopes play the role of server policy.[^s1]

## Common scope values

The Mobile SDK guide keeps the reference list of server-side values.[^s1] The ones most integrations meet:

- `api`: REST API and Bulk API 2.0 on the user's behalf; it also covers `chatter_api` (Connect REST API).[^s1]
- `refresh_token` (synonym `offline_access`): lets an eligible client receive a refresh token so it can act when the user is away.[^s1]
- `web`: lets the token be used for Salesforce web pages, and it includes `visualforce`, which alone reaches only customer-built Visualforce pages.[^s1]
- `full`: everything the user can access; the guide says it encompasses all other scopes, yet it does not return a refresh token.[^s1]
- `openid` adds a signed ID token for OpenID Connect, while `id`, `profile`, `email`, `address` and `phone` all reach the identity URL service.[^s1]
- `custom_permissions`: reveals the org's custom permissions and whether the user holds each one.[^s1]
- Product scopes such as `cdp_api` (all Data Cloud APIs), `cdp_query_api`, `cdp_ingest_api`, `wave_api`, `pardot_api` and `chatbot_api`.[^s1]
- Headless identity scopes `user_registration_api` and `forgot_password`; `lightning` and `content` grant hybrid-app child sessions.[^s1]

Newer surfaces add their own scope. Salesforce's hosted MCP servers, for example, need an external client app with **Access MCP servers (`mcp_api`)** plus `refresh_token`, and they do not support connected apps.[^s4]

## How scopes are configured

In Setup, scopes are picked in the app's OAuth settings. For external client apps the Metadata API stores them in `ExtlClntAppOauthSettings`, a type introduced in API version 59.0, as a string field `commaSeparatedOauthScopes`, with a separate `commaSeparatedCustomScopes` field.[^s2] That field uses metadata names rather than token strings, for example `Api`, `Web`, `Full`, `RefreshToken`, `OpenID`, `CustomPermissions`, `CDPQuery`, `EinsteinGPT` and `MCP`.[^s2] `Basic` is shorthand for `Address`, `Email`, `Phone` and `Profile`, and `RefreshToken` and `OfflineAccess` behave the same.[^s2] Because scopes live in metadata, they can be reviewed and deployed through source control like any other app setting.[^s2]

## Limits and gotchas

- **`full` is not "everything" for refresh.** Without `refresh_token` selected too, the client gets no refresh token, and Mobile SDK apps must always have `refresh_token` selected server-side.[^s1]
- **Requests can only narrow.** A client can ask for fewer scopes than the app allows, never more; from Mobile SDK 13.2 an app that asks for none receives all scopes configured on the app.[^s1]
- **Broad scopes are a governance smell.** The architecture blog warns that `full` grants far more than most integrations need and recommends narrow scopes tied to the integration's job, such as not granting unrelated API scopes to a client that only publishes events.[^s5]
- **Refresh tokens last indefinitely by default.** The MCP setup guide recommends a refresh token validity of 30 days or less, plus refresh token rotation, for production.[^s4]
- **Reserved values.** `sfap_api` and `interaction_api` are listed as reserved for future use, so don't build on them yet.[^s1]

## When to use which

Pick the smallest set that does the job: `api` (plus `refresh_token` if the app must run unattended) for data integrations, `openid` and the profile scopes for login-only apps, and `web` only when the token has to open Salesforce UI pages.[^s1][^s5] Then constrain data access with a dedicated integration user and permission sets, because scopes alone don't decide which objects and fields the token can touch.[^s5]

## Connections

Scopes **implement** the scope mechanism of **OAuth 2.0** and are part of Salesforce **API access control**.[^s3][^s5] They are **configured via** **external client apps** and legacy **connected apps**, and every one of the **OAuth 2.0 flows in Salesforce** consumes them when requesting a token.[^s1][^s2] The `refresh_token` scope works with **refresh token policies**, `openid` ties into **OpenID Connect**, the registration scopes serve **headless identity**, `cdp_*` scopes cover **Data Cloud**, and the **Mobile SDK** documents the client side.[^s1][^s4] Data access still **depends on** **permission sets**, which together with narrow scopes **implements** the **principle of least privilege**.[^s5]

## Sources

[^s1]: Salesforce Developers, "Scope Parameter Values (Mobile SDK Development Guide)". https://developer.salesforce.com/docs/platform/mobile-sdk/guide/oauth-scope-parameter-values.html (accessed 2026-11-26)
[^s2]: Salesforce Developers, "ExtlClntAppOauthSettings". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_extlclntappoauthsettings.htm (accessed 2026-11-26)
[^s3]: IETF, "RFC 6749: The OAuth 2.0 Authorization Framework". https://datatracker.ietf.org/doc/rfc6749 (accessed 2026-11-26)
[^s4]: Salesforce Developers, "Create an External Client App (Hosted MCP Servers)". https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/create-external-client-app.html (accessed 2026-11-26)
[^s5]: Salesforce, "Architecting Inbound Governance with External Client Apps". https://www.salesforce.com/blog/architecting-inbound-governance-external-client-apps/ (accessed 2026-11-26)
