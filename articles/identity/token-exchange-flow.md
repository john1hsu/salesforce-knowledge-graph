---
id: kt:token-exchange-flow
type: Feature
title: OAuth 2.0 Token Exchange Flow
aliases: [token exchange flow, Salesforce token exchange, RFC 8693 token exchange grant, token exchange handler, Oauth2TokenExchangeHandler]
domain: identity
summary: >-
  Salesforce's implementation of the RFC 8693 token exchange grant: a client that already holds a token from an
  external identity provider posts it to the Salesforce token endpoint, an Apex token exchange handler validates it
  and maps its subject to a Salesforce user (optionally creating one), and Salesforce issues its own access token.
release: "Winter '27"
status: current
broader: [kt:oauth-2-flows-in-salesforce]
related: [kt:openid-connect, kt:saml-2-0, kt:just-in-time-provisioning, kt:experience-cloud-identity, kt:json-web-token]
relations:
  - {predicate: implements, object: kt:oauth-2-0}
  - {predicate: configuredVia, object: kt:external-client-apps}
  - {predicate: configuredVia, object: kt:connected-apps}
  - {predicate: dependsOn, object: kt:apex}
  - {predicate: alternativeTo, object: kt:jwt-bearer-flow}
sources:
  - id: s1
    title: "Token Exchange Flow Diagram and Process"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_token_exchange_diagram.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-19
  - id: s2
    title: "Token Exchange Flow Use Cases"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.remoteaccess_token_exchange_use_cases.htm&type=5
    type: official-docs
    accessed: 2026-11-19
  - id: s3
    title: "Oauth2TokenExchangeHandler Class (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_Auth_Oauth2TokenExchangeHandler.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s4
    title: "OAuth 2.0 Token Exchange Handler Examples (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/token_exchange_handler.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s5
    title: "OauthTokenExchangeHandler (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_oauthtokenexchangehandler.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s6
    title: "RFC 8693: OAuth 2.0 Token Exchange"
    publisher: IETF
    url: https://www.rfc-editor.org/rfc/rfc8693
    type: standards-body
    accessed: 2026-11-19
created: 2026-11-19
---

# OAuth 2.0 Token Exchange Flow

The **OAuth 2.0 token exchange flow** lets an app that has already signed a user in through an external identity provider, such as Okta, trade that provider's token for a Salesforce access token, without sending the user through a second Salesforce login.[^s1] It is Salesforce's implementation of RFC 8693, an IETF Proposed Standard published in January 2020 that defines a Security Token Service protocol on top of OAuth 2.0.[^s6] The flow is available in Enterprise, Performance, Unlimited and Developer Editions.[^s1][^s4]

## How it works

The client posts to the org's `/services/oauth2/token` endpoint with at least four parameters: `grant_type` set to the token exchange grant, the provider-issued `subject_token`, a `subject_token_type`, and the `client_id` of the app registered in Salesforce.[^s1] In the RFC, the grant type is the URN `urn:ietf:params:oauth:grant-type:token-exchange`, and token types are identified by URIs for access tokens, refresh tokens, ID tokens, SAML assertions and JWTs.[^s6] The RFC also defines optional `actor_token`, `audience`, `resource`, `scope` and `requested_token_type` parameters, plus an `act` claim for delegation chains, but Salesforce's flow description lists only the four minimum parameters and says further ones depend on the use case.[^s6][^s1]

Once the OAuth runtime has validated the request, it hands the incoming token to an Apex **token exchange handler**.[^s1] The handler validates the token, maps its subject to a Salesforce user, and returns either an existing user or a new, uninserted `User` that the runtime then inserts; either step may call back to the identity provider.[^s1] Salesforce then returns an access token and, if requested, other tokens such as a refresh token or ID token.[^s1]

## The token exchange handler

A handler is an Apex class extending `Auth.Oauth2TokenExchangeHandler`, which has two methods to override.[^s3]

- `validateIncomingToken` receives the app's developer name and type, the raw token and its `Auth.OAuth2TokenExchangeType`, and returns an `Auth.TokenValidationResult`.[^s3]
- `getUserForTokenSubject` takes that result plus a `canCreateUser` flag and returns the `User` record to issue the token for.[^s3]

The supported incoming token types are access tokens, refresh tokens, ID tokens, SAML 2.0 assertions and any token formatted as a JWT.[^s3] Salesforce's examples validate JWTs and ID tokens with `Auth.JWTUtil` against a keys endpoint or public key, and validate opaque access tokens by calling the provider's introspection endpoint.[^s4]

The handler is registered with the **OauthTokenExchangeHandler** metadata type, introduced in API version 60.0.[^s5] Its fields name the Apex class (`tokenHandlerApex`), switch each token type on or off, and control whether user creation is allowed.[^s5] Its `enablements` entries tie the handler to specific connected apps or external client apps, name the Apex execution user (an integration user is recommended), and mark a default handler for when a request omits the `token_handler` parameter.[^s5]

## Limits and gotchas

A new user is created only when three conditions hold: `isUserCreationAllowed` is true on the metadata, `canCreateUser` is true in the call, and no matching user exists.[^s5] The handler examples are explicitly demonstration code: they run `without sharing`, query `WITH SYSTEM_MODE`, and hardcode values such as a profile name, so each one must be reviewed for security before use.[^s4] Assigning permission sets in the same transaction as user creation can raise mixed DML errors, so the examples suggest moving that work into a future method.[^s4] Handlers should reject unknown token types, and failed validation returns a generic error message unless the handler supplies its own.[^s4] Because the handler decides who the caller becomes in Salesforce, a weak validation step is effectively an authentication bypass.[^s3][^s4]

## When to use it (and when not)

Salesforce positions token exchange for estates where an external identity provider sits at the centre of many services and microservices, so that Salesforce can join without every service being redesigned to accept Salesforce-issued tokens.[^s2] It works for internal users through the org's My Domain login URL and for customers and partners through Experience Cloud sites.[^s2] For a server acting with no upstream user token, the JWT bearer flow is the more direct server-to-server choice, since token exchange presumes the user is already signed in to the identity provider.[^s1][^s2]

## Connections

Token exchange is one of the **OAuth 2.0 flows in Salesforce** and **implements** the **OAuth 2.0** token exchange grant from RFC 8693.[^s1][^s6] It is **configured via** **external client apps** or **connected apps**, and it **depends on** **Apex** for its handler.[^s5][^s3] It accepts tokens from **OpenID Connect**, **SAML 2.0** and **JSON Web Token** sources, and its user creation resembles **just-in-time provisioning**.[^s3][^s4] It is an **alternative to** the **JWT bearer flow** for integrations, and it extends to external users through **Experience Cloud identity**.[^s2]

## Sources

[^s1]: Salesforce Help, "Token Exchange Flow Diagram and Process". https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_token_exchange_diagram.htm&language=en_US&type=5 (accessed 2026-11-19)
[^s2]: Salesforce Help, "Token Exchange Flow Use Cases". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.remoteaccess_token_exchange_use_cases.htm&type=5 (accessed 2026-11-19)
[^s3]: Salesforce Developers, "Oauth2TokenExchangeHandler Class". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_Auth_Oauth2TokenExchangeHandler.htm (accessed 2026-11-19)
[^s4]: Salesforce Developers, "OAuth 2.0 Token Exchange Handler Examples". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexref/token_exchange_handler.htm (accessed 2026-11-19)
[^s5]: Salesforce Developers, "OauthTokenExchangeHandler". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_oauthtokenexchangehandler.htm (accessed 2026-11-19)
[^s6]: IETF, "RFC 8693: OAuth 2.0 Token Exchange". https://www.rfc-editor.org/rfc/rfc8693 (accessed 2026-11-19)
