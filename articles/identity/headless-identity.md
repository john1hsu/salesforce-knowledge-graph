---
id: kt:headless-identity
type: Feature
title: Headless Identity
aliases: [Headless Identity APIs, Headless Login API, Headless Registration API, Headless Forgot Password API, headless customer identity]
domain: identity
summary: >-
  A set of Salesforce Customer Identity APIs (headless login, registration, passwordless login, forgot password,
  guest user and native SSO) that let an off-platform web or mobile app own its entire login UI while an
  Experience Cloud site handles authentication, user records and access in the background.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:connected-apps]
relations:
  - {predicate: dependsOn, object: kt:experience-cloud}
  - {predicate: dependsOn, object: kt:oauth-2-flows-in-salesforce}
  - {predicate: configuredVia, object: kt:external-client-apps}
  - {predicate: alternativeTo, object: kt:experience-cloud-identity}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "What Is Headless Identity? (Headless Identity Implementation Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/headless-identity-impl-guide/guide/headless-identity-what-is-it.html
    type: official-docs
    accessed: 2026-11-06
  - id: s2
    title: "Learn Key Concepts in Headless Identity (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/headless-identity-basics/learn-key-concepts-in-headless-identity
    type: official-learning
    accessed: 2026-11-06
  - id: s3
    title: "OAuth 2.0 Authorization Code and Credentials Flow for Private Clients"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=remoteaccess_authorization_code_credentials_flow.htm
    type: official-docs
    accessed: 2026-11-06
  - id: s4
    title: "Configure Headless Identity Settings in Experience Cloud (Headless Identity Implementation Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/headless-identity-impl-guide/guide/headless-identity-login-registration-settings.html
    type: official-docs
    accessed: 2026-11-06
created: 2026-11-06
---

# Headless Identity

**Headless Identity** is the part of Salesforce Customer Identity that decouples the back-end authentication service from the front-end sign-in experience. A brand builds its own login, sign-up and password-reset screens in a single-page app, a native mobile app or a server-rendered web app, and calls Salesforce APIs to authenticate the user, create the account and issue tokens.[^s1] It is available in Enterprise, Unlimited and Developer editions.[^s1][^s3]

## What it includes

The documented capabilities are self-registration, username-and-password login, passwordless login over email or SMS, password reset, native single sign-on inside the app, and identification of anonymous guest users.[^s2] The implementation guide groups these into a Headless Login API, a Headless Registration API that extends the login flow to create and sign in new users, and a Headless Forgot Password API, which it says you need whenever users can both register and log in.[^s1] Native SSO is optional and is wired up by linking an SSO provider through the standard web-server and user-agent OAuth flows.[^s1]

## How it works

Most headless flows (login, registration, passwordless and guest) share one pattern: the **Authorization Code and Credentials flow**, a Salesforce-specific extension of the OAuth 2.0 authorization code grant.[^s2] The app posts the user's credentials to the `/services/oauth2/authorize` endpoint with `response_type=code_credentials`; Salesforce validates them and answers with a 302 redirect carrying an authorization code; the code is then exchanged at `/services/oauth2/token` for an access token.[^s3][^s2] Every authorization request must carry the header `Auth-Request-Type: Named-User`, and credentials go in a Basic `Authorization` header or, if the org requires it, in the POST body.[^s3] An optional Apex discovery handler lets users sign in with an email, phone number or even an order number via `login_hint`, and a `uvid_hint` can tie an earlier guest session to the now-named user (this requires JWT-based access tokens).[^s3] Forgot-password and native SSO do not follow the code-and-credentials pattern.[^s2]

The app is integrated through an external client app or connected app, and an **Experience Cloud site is mandatory** even if end users never see it: the APIs are exposed and configured through the site, and the site stores the customer accounts and contacts and controls app access.[^s1] Settings live in the site's Workspaces under Administration > Login & Registration, where admins enable headless registration and password reset, choose a default profile, an Apex registration handler and a run-as user.[^s4]

## Limits and gotchas

- The flow only works against an Experience Cloud site domain (such as `*.my.site.com`); it does not support employee logins through login.salesforce.com or a My Domain login URL.[^s3]
- **Public vs. private clients.** Browser and mobile apps are public clients that cannot keep a consumer secret, so PKCE is required for them and reCAPTCHA is their main bot defence; server-side private clients send the secret, and authenticated API calls with an integration user's token are their recommended primary protection.[^s2] For private clients, Salesforce advises PKCE plus requiring the secret for the web-server and refresh-token flows.[^s3]
- Headless registration and password reset must each require reCAPTCHA, authentication or both; at least one must be on. The lowest permitted reCAPTCHA score threshold is 0.5, and password reset defaults to a maximum of 5 attempts.[^s4]
- The registration run-as user needs access to the account that holds end users plus the Headless Identity Admin role; the guide recommends a dedicated service-style user so a departing employee cannot break sign-up.[^s4]

## When to use it (and when not)

Choose Headless Identity when the brand needs full control of the UI, for example in a **companion app** that sits beside an existing site, or a **standalone app** whose users never visit the site at all, while still keeping customer records in Salesforce for marketing and service.[^s1] If the out-of-the-box or Experience Builder login pages are acceptable, conventional site login is less work, because the headless model shifts token handling, bot protection and UI security onto your app.[^s2][^s1] SSO configured on the site's login page can also be made to feel headless, since Salesforce redirects straight to the provider without showing its own page.[^s4]

## Connections

Headless Identity is a part of `kt:salesforce-identity` and the API-driven alternative to the hosted pages described in `kt:experience-cloud-identity`.[^s1] It **depends on** `kt:experience-cloud`, since a site is required to expose the APIs and store users.[^s1] Its core mechanism is a variant of the OAuth flows covered in `kt:oauth-2-flows-in-salesforce`, and the client app is **configured via** `kt:external-client-apps` or, in older setups, `kt:connected-apps`.[^s3][^s1] The topic falls within the scope of the `kt:identity-and-access-management-architect-certification`.

## Sources
[^s1]: Salesforce Developers, "What Is Headless Identity?". https://developer.salesforce.com/docs/platform/headless-identity-impl-guide/guide/headless-identity-what-is-it.html (accessed 2026-11-06)
[^s2]: Trailhead, "Learn Key Concepts in Headless Identity". https://trailhead.salesforce.com/content/learn/modules/headless-identity-basics/learn-key-concepts-in-headless-identity (accessed 2026-11-06)
[^s3]: Salesforce Help, "OAuth 2.0 Authorization Code and Credentials Flow for Private Clients". https://help.salesforce.com/apex/HTViewHelpDoc?id=remoteaccess_authorization_code_credentials_flow.htm (accessed 2026-11-06)
[^s4]: Salesforce Developers, "Configure Headless Identity Settings in Experience Cloud". https://developer.salesforce.com/docs/platform/headless-identity-impl-guide/guide/headless-identity-login-registration-settings.html (accessed 2026-11-06)
