---
id: kt:frontdoor-jsp-session-bridging
type: API
title: Frontdoor.jsp Session Bridging
aliases: [frontdoor.jsp, frontdoor URL, Single Access UI Bridge API, singleaccess endpoint, /services/oauth2/singleaccess, UI bridge frontdoor URL]
domain: identity
summary: >-
  The mechanism that turns an OAuth access token into a browser UI session without a second login: an app calls the
  Single Access UI Bridge API (services/oauth2/singleaccess) and receives a one-time, short-lived
  /secur/frontdoor.jsp URL that signs the user into Lightning, a My Domain page or an Experience Cloud site.
release: "Winter '27"
status: current
broader: [kt:oauth-2-flows-in-salesforce, kt:salesforce-identity]
related: [kt:web-server-flow, kt:headless-identity, kt:experience-cloud-identity, kt:salesforce-cli, kt:tableau-next, kt:login-flows]
relations:
  - {predicate: dependsOn, object: kt:oauth-scopes}
  - {predicate: dependsOn, object: kt:my-domain}
  - {predicate: configuredVia, object: kt:external-client-apps}
  - {predicate: configuredVia, object: kt:connected-apps}
  - {predicate: consumedBy, object: kt:salesforce-cli}
  - {predicate: dependsOn, object: kt:bearer-token-security}
sources:
  - id: s1
    title: "Generate a Frontdoor URL to Bridge into UI Sessions"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.frontdoor_singleaccess.htm&type=5
    type: official-docs
    accessed: 2026-11-26
  - id: s2
    title: "Generate the Access Token and Frontdoor URL for Tableau Next Embedding"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/analytics/sdk/guide/sdk-access-token.html
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "Generate the Access Token for Agentforce Conversation Client Web SDK"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/accsdk/guide/acc-sdk-setup-token.html
    type: official-docs
    accessed: 2026-11-26
  - id: s4
    title: "RFC 6750: The OAuth 2.0 Authorization Framework: Bearer Token Usage"
    publisher: IETF
    url: https://rfc-editor.org/rfc/rfc6750.html
    type: standards-body
    accessed: 2026-11-26
  - id: s5
    title: "org open | Salesforce CLI Command Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_org_open.html
    type: official-docs
    accessed: 2026-11-26
  - id: s6
    title: "@salesforce/plugin-org 5.6.1 messages (SecurityWarning, BehaviorChangeWarning)"
    publisher: Salesforce CLI (npm package via unpkg)
    url: https://unpkg.com/@salesforce/plugin-org@5.6.1/messages/messages.md
    type: community
    accessed: 2026-11-26
created: 2026-11-26
---

# Frontdoor.jsp Session Bridging

**Frontdoor.jsp** is the Salesforce page at `/secur/frontdoor.jsp` that accepts a one-time credential and establishes a normal browser session, so a user who is already authenticated to an app through OAuth can land on a My Domain page, such as a Setup page in Lightning, or an Experience Cloud site without typing credentials again.[^s1] The supported way to get such a URL is the **Single Access UI Bridge API**: the app sends an access token to `services/oauth2/singleaccess` and gets back a ready-made frontdoor URL.[^s1] Salesforce's own embedding SDKs, such as the Tableau Next Embedding SDK and the Agentforce Conversation Client Web SDK, use exactly this pattern to bridge a server-side token into an in-browser Salesforce session.[^s2][^s3]

## How it works

1. The app obtains an access token through an OAuth flow, for example the web server flow with the `web` scope, as the Tableau Next guide shows, or the client credentials flow, as the Agentforce Conversation Client guide shows.[^s2][^s3]
2. It calls `https://<My Domain>/services/oauth2/singleaccess` with POST or GET. With GET the token must go in the `Authorization: Bearer` header; with POST it may go in the header or in an `access_token` body parameter.[^s1]
3. An optional `redirect_uri` names the landing page. It must be a relative path such as `lightning/setup/ManageUsers/home`; absolute URLs are rejected, and without it the user lands on the My Domain or site home page.[^s1]
4. The JSON response carries a `frontdoor_uri` of the form `/secur/frontdoor.jsp?otp=…&startURL=…&cshc=…`, where `startURL` appears only when a redirect path was sent.[^s1]
5. The app sends the browser to that URL, and Salesforce creates a new UI session for the token's user.[^s1][^s2]

## Limits and gotchas

- **One minute, one use.** A frontdoor URL is valid for up to one minute after it is returned and can be used only once.[^s1]
- **Repeat calls return the same URL.** Calling the endpoint again inside that minute returns the same URL without extending its expiry; a fresh URL is issued only after the first expires.[^s1]
- **Scope.** The access token must carry the `web` or `full` scope, set on the issuing external client app or connected app; otherwise the call fails with `Invalid_Scope`.[^s1]
- **Domains.** Only My Domain and Experience Cloud site URLs work; calls to login.salesforce.com or test.salesforce.com return `No_Access`, and a token from another org returns `Wrong_Org`.[^s1]
- **API Only users** cannot be bridged; their tokens fail with `Bad_OAuth_Token`, as do expired or invalid tokens.[^s1]
- **Experience Cloud sites** that use a URL path suffix must include the suffix in the `redirect_uri`.[^s1]
- **Token type.** Both opaque and JWT-based access tokens are accepted.[^s1]
- **Keep it server-side.** Salesforce's SDK guides warn against hard-coding OAuth tokens or frontdoor URLs in client code, because credentials in the browser can be scraped.[^s2][^s3]

## Security background

A frontdoor link is a credential: whoever opens it first gets the session. That is why the design follows the OAuth bearer-token guidance in RFC 6750, which says bearer tokens should not travel in page URLs, because history and server logs may not protect them.[^s4] The RFC also recommends short-lived tokens to limit the damage of a leak, and the singleaccess design pushes that further with a one-minute, single-use code instead of a long-lived token in the query string.[^s1][^s4]

The Salesforce CLI shows the same shift. `sf org open` opens an org in a browser, and its `--url-only` flag prints the navigation URL instead of launching it.[^s5] The plugin's own messages warn that sharing that URL is like logging someone in under your credential, and state that from August 2025 the command generates single-use URLs with `--json` or `--url-only`.[^s6]

## When to use it (and when not)

Use the singleaccess API when an integration, portal, embedded app or tool already holds a user's access token and needs to hand that user into the Salesforce UI: embedding Tableau Next or an Agentforce client, or deep-linking from an external app into a Setup page.[^s1][^s2][^s3] It is not a login mechanism in its own right: the endpoint only exchanges a token the app already has, so the user must first be authenticated by an OAuth flow, and in single sign-on scenarios the user is routed through the SSO provider's login before reaching the target app's authorization URL.[^s1] Where a new browser session isn't needed, for example server-to-server calls, keep using the access token against the APIs directly and skip the bridge, since every frontdoor URL is another credential that has to be protected.[^s2][^s4]

## Connections

Frontdoor session bridging sits under `kt:oauth-2-flows-in-salesforce` and `kt:salesforce-identity`, because it converts an OAuth access token into a UI session.[^s1] It depends on `kt:oauth-scopes` (the `web` or `full` scope) set on `kt:external-client-apps` or `kt:connected-apps`, and on `kt:my-domain`, since only My Domain and site hosts serve the endpoint.[^s1] Tokens typically come from the `kt:web-server-flow`, as in the `kt:tableau-next` embedding guide.[^s2] It serves `kt:experience-cloud-identity` and `kt:headless-identity` scenarios on sites, and the `kt:salesforce-cli` consumes it to produce single-use `org open` URLs.[^s1][^s6] Because a bridged session is created from an existing token rather than an interactive login, it is worth reviewing alongside `kt:login-flows`; its one-time design reflects `kt:bearer-token-security` guidance.[^s1][^s4]

## Sources

[^s1]: Salesforce Help, "Generate a Frontdoor URL to Bridge into UI Sessions". https://help.salesforce.com/s/articleView?language=en_US&id=sf.frontdoor_singleaccess.htm&type=5 (accessed 2026-11-26)
[^s2]: Salesforce Developers, "Generate the Access Token and Frontdoor URL for Tableau Next Embedding". https://developer.salesforce.com/docs/analytics/sdk/guide/sdk-access-token.html (accessed 2026-11-26)
[^s3]: Salesforce Developers, "Generate the Access Token for Agentforce Conversation Client Web SDK". https://developer.salesforce.com/docs/platform/accsdk/guide/acc-sdk-setup-token.html (accessed 2026-11-26)
[^s4]: IETF, "RFC 6750: The OAuth 2.0 Authorization Framework: Bearer Token Usage" (October 2012). https://rfc-editor.org/rfc/rfc6750.html (accessed 2026-11-26)
[^s5]: Salesforce Developers, "org open", Salesforce CLI Command Reference. https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_org_open.html (accessed 2026-11-26)
[^s6]: Salesforce CLI, "@salesforce/plugin-org 5.6.1 messages". https://unpkg.com/@salesforce/plugin-org@5.6.1/messages/messages.md (accessed 2026-11-26)
