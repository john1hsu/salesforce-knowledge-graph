---
id: kt:client-credentials-flow
type: Feature
title: OAuth 2.0 Client Credentials Flow
aliases: [client credentials flow, client credentials grant, grant_type=client_credentials, run-as user flow]
domain: identity
summary: >-
  Salesforce's implementation of the RFC 6749 client credentials grant: a back-end client exchanges an external
  client app's or connected app's consumer key and secret for an access token that always runs as one designated
  run-as (integration) user, with no browser login and no refresh token.
release: "Winter '27"
status: current
broader: [kt:oauth-2-flows-in-salesforce]
related: [kt:permission-set-licenses, kt:rest-api, kt:jwt-bearer-flow]
relations:
  - {predicate: implements, object: kt:oauth-2-0}
  - {predicate: configuredVia, object: kt:external-client-apps}
  - {predicate: configuredVia, object: kt:connected-apps}
  - {predicate: alternativeTo, object: kt:jwt-bearer-flow}
  - {predicate: alternativeTo, object: kt:username-password-flow}
  - {predicate: dependsOn, object: kt:permission-sets}
sources:
  - id: s1
    title: "RFC 6749: The OAuth 2.0 Authorization Framework"
    publisher: IETF
    url: https://datatracker.ietf.org/doc/html/rfc6749.html
    type: standards-body
    accessed: 2026-11-15
  - id: s2
    title: "Using the Client Credentials Flow for Easier API Authentication"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/03/using-the-client-credentials-flow-for-easier-api-authentication
    type: official-blog
    accessed: 2026-11-15
  - id: s3
    title: "Invoke REST APIs with the Salesforce Integration User and OAuth Client Credentials"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/02/invoke-rest-apis-with-the-salesforce-integration-user-and-oauth-client-credentials
    type: official-blog
    accessed: 2026-11-15
  - id: s4
    title: "ExtlClntAppOauthConfigurablePolicies (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_extlclntappoauthconfigurablepolicies.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "Create an External Client App for the OAuth 2.0 Client Credentials Flow"
    publisher: Salesforce Developers (Loyalty Management Developer Guide)
    url: https://developer.salesforce.com/docs/industries/loyalty/guide/authorization.html
    type: official-docs
    accessed: 2026-11-15
  - id: s6
    title: "Connected App Basics: Integrate with an API"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/connected-app-basics/connected-app-basics-api-integration
    type: official-learning
    accessed: 2026-11-15
created: 2026-11-15
---

# OAuth 2.0 Client Credentials Flow

The **client credentials flow** lets a server-side integration obtain a Salesforce access token using nothing but the app's own credentials: the consumer key (client ID) and consumer secret (client secret) of an external client app or connected app.[^s2] Because no person logs in, Salesforce needs some user to run as, so the admin assigns a **run-as user** to the app and every token the flow issues carries that user's permissions.[^s2][^s4] Trailhead positions it for app-to-app data exchange without user interaction and as a more secure replacement for the username-password flow.[^s6] The umbrella article on OAuth flows compares it with its siblings; this node covers the standard, the setup and the operational gotchas.

## The standard underneath

RFC 6749 section 4.4 defines the grant for a client acting on resources it controls, or on resources whose owner arranged access with the authorization server in advance.[^s1] There is no authorization request at all: the client authenticates at the token endpoint and the authentication itself is the grant. The request carries `grant_type=client_credentials` and an optional `scope`, the grant is restricted to confidential clients that can keep a secret, and the spec says a refresh token should not be returned.[^s1] For password-style client credentials the RFC expects HTTP Basic authentication and discourages putting the secret in the request body, which must in any case travel only over TLS.[^s1]

## How it works in Salesforce

Setup has two halves.[^s5] On the app, enable OAuth, add the `api` scope, select **Enable Client Credentials Flow** and accept the risk warning; then, under the app's policies, pick the **Run As** user in the Client Credentials Flow section.[^s5][^s2] In metadata for an external client app these appear as `isClientCredentialsFlowEnabled` (default false) and `clientCredentialsFlowUser`, both available since API version 60.0 on the `ExtlClntAppOauthConfigurablePolicies` type.[^s4] Salesforce's integration-user guidance also sets the permitted-users policy to admin pre-approved and adds the integration user's permission set to the app, so only holders of that permission set can use it.[^s3]

The client then POSTs to `/services/oauth2/token` on the org's My Domain (or an Experience Cloud site's domain) with the grant type, client ID and secret.[^s3] A successful response holds `access_token`, `instance_url`, the identity URL `id`, `token_type` Bearer, `scope`, `issued_at` and `signature`, and the token is issued for the run-as user.[^s3][^s2]

## Limits and gotchas

- **No refresh token.** When a token expires, the client simply repeats the request with its key and secret.[^s3]
- **Retry on 401.** Salesforce's guidance is to use the token until a 401, then rerun the flow once and raise an error if that fails; with JWT-format tokens, checking `exp` locally helps, but a signing-key rotation can still invalidate tokens early.[^s3]
- **The token is as powerful as the run-as user.** Assigning a system administrator hands every holder of the secret admin-level API access.[^s2]
- **API Only.** The metadata reference describes the execution user as one with the API Only permission; the 2023 launch post noted that requirement for Spring '23 and said it would be lifted in Summer '23, so check your org's behavior.[^s4][^s2]
- **The secret is a password.** The flow only fits clients that can store the key and secret securely; one app per integration lets you rotate a leaked secret without touching others.[^s3]

## Pairing with the Integration user license

Enterprise, Unlimited and Performance Edition orgs come with five Salesforce Integration user licenses, which offer the "Minimum Access – API Only Integrations" profile.[^s3] That profile only sets defaults such as record types, layouts, login hours and IP ranges; object and user permissions come from a permission set built on the Salesforce API Integration permission set license, ideally one per integration.[^s3] This combination gives each integration a dedicated, least-privilege, auditable identity.[^s3]

## When to use it (and when not)

Choose it for unattended back-end jobs such as backup, analytics or middleware sync where a single fixed integration identity is acceptable and a shared secret can be stored safely.[^s2][^s3] A client that can't keep a secret confidential, such as a browser or mobile app, must not use this grant under the RFC.[^s1] For server-to-server work where you would rather manage a signing certificate than a shared secret, the JWT bearer flow is the sibling option, and anything a human drives belongs in an interactive flow.[^s6]

## Connections

It is one of the **OAuth 2.0 flows in Salesforce** and **implements** the **OAuth 2.0** client credentials grant.[^s1][^s2] It is **configured via** an **external client app** or **connected app**, and it **depends on** **permission sets** (and the API Integration **permission set license**) to keep its run-as user least-privileged.[^s3][^s5] It is an **alternative to** the **JWT bearer flow** and replaces the **username-password flow** for server-to-server work, and its tokens are typically used against the **REST API**.[^s3][^s6]

## Sources

[^s1]: IETF, "RFC 6749: The OAuth 2.0 Authorization Framework". https://datatracker.ietf.org/doc/html/rfc6749.html (accessed 2026-11-15)
[^s2]: Salesforce Developers Blog, "Using the Client Credentials Flow for Easier API Authentication". https://developer.salesforce.com/blogs/2023/03/using-the-client-credentials-flow-for-easier-api-authentication (accessed 2026-11-15)
[^s3]: Salesforce Developers Blog, "Invoke REST APIs with the Salesforce Integration User and OAuth Client Credentials". https://developer.salesforce.com/blogs/2024/02/invoke-rest-apis-with-the-salesforce-integration-user-and-oauth-client-credentials (accessed 2026-11-15)
[^s4]: Salesforce Developers, "ExtlClntAppOauthConfigurablePolicies". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_extlclntappoauthconfigurablepolicies.htm (accessed 2026-11-15)
[^s5]: Salesforce Developers, "Create an External Client App for the OAuth 2.0 Client Credentials Flow". https://developer.salesforce.com/docs/industries/loyalty/guide/authorization.html (accessed 2026-11-15)
[^s6]: Trailhead, "Connected App Basics: Integrate with an API". https://trailhead.salesforce.com/content/learn/modules/connected-app-basics/connected-app-basics-api-integration (accessed 2026-11-15)
