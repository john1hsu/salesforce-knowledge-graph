---
id: kt:custom-authentication-providers
type: Feature
title: Custom Authentication Providers
aliases: [custom authentication provider plug-in, custom auth provider, Auth.AuthProviderPluginClass, AuthProviderPluginClass, custom external authentication provider]
domain: identity
summary: >-
  An Auth. Provider of type Custom whose OAuth handshake is written in Apex by extending the abstract class
  Auth.AuthProviderPluginClass, with its settings held in a custom metadata type, used to sign users in to Salesforce
  or obtain third-party tokens when no built-in provider type fits the external service.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:named-credentials, kt:single-logout, kt:apex-testing]
relations:
  - {predicate: dependsOn, object: kt:custom-metadata-types}
  - {predicate: dependsOn, object: kt:apex-callouts}
  - {predicate: implements, object: kt:oauth-2-0}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: alternativeTo, object: kt:openid-connect-authentication-providers}
sources:
  - id: s1
    title: "Create a Custom Authentication Provider Plug-in (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/authproviderplugin.htm
    type: official-docs
    accessed: 2026-11-28
  - id: s2
    title: "AuthProviderPlugin Interface (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apex/apex_interface_Auth_AuthProviderPlugin.htm
    type: official-docs
    accessed: 2026-11-28
  - id: s3
    title: "AuthProvider (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-authprovider.html
    type: official-docs
    accessed: 2026-11-28
  - id: s4
    title: "Create an OAuth Named Credential (Named Credentials Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/named-credentials/guide/nc-create-oauth-cred.html
    type: official-docs
    accessed: 2026-11-28
  - id: s5
    title: "RFC 6749: The OAuth 2.0 Authorization Framework"
    publisher: IETF / RFC Editor
    url: https://www.rfc-editor.org/info/rfc6749
    type: standards-body
    accessed: 2026-11-28
created: 2026-11-28
---

# Custom Authentication Providers

A **custom authentication provider** is an Auth. Provider whose provider type is **Custom**: instead of choosing one of Salesforce's built-in types, a developer writes the OAuth handshake in Apex. The Metadata API lists the Custom value, available since API version 36.0, alongside built-in types such as Apple, Facebook, GitHub, Google, LinkedIn, Microsoft, Slack and the generic OpenID Connect type.[^s3] The Apex Developer Guide frames the feature as a way to build a custom OAuth-based provider for single sign-on, and its worked example targets Concur, a service with no built-in type.[^s1]

## How it works

The provider has three parts. First, a **custom metadata type** holds the provider's settings; the guide says to create its record before writing any Apex, and the sample stores the consumer key, secret, authorize URL, token URL and user-info URLs as fields on it.[^s1] Second, an **Apex class extends the abstract class `Auth.AuthProviderPluginClass`**. Third, the Auth. Provider definition ties them together: its `plugin` field names the Apex class, and `customMetadataTypeRecord`, required for this type, gives the API name of the custom provider's configuration.[^s3]

The class overrides four methods, and Salesforce passes each one the configuration record as a map of field names to values:[^s1][^s2]

- **`getCustomMetadataType()`** returns the API name of the custom metadata type that holds the settings, not the name of a record.[^s2]
- **`initiate(config, stateToPropagate)`** builds the provider's authorize URL and returns a `PageReference` that sends the user's browser there.[^s1]
- **`handleCallback(config, callbackState)`** reads the query parameters the provider returned (such as `code` and `state`), exchanges the code for tokens, and returns an `Auth.AuthProviderTokenResponse`.[^s1]
- **`getUserInfo(config, tokenResponse)`** calls the provider's user API with the access token and returns an `Auth.UserData` object.[^s1]

That sequence is the client side of the OAuth 2.0 authorization code grant defined in RFC 6749, published in October 2012 and since updated by RFC 9700.[^s5] Once `getUserInfo` returns, the provider behaves like any other Auth. Provider: a registration handler class that implements `Auth.RegistrationHandler`, or since API version 64.0 a flow of the Identity User Registration type, creates or links the Salesforce user, and runs as an execution user who needs the Manage Users permission.[^s3]

## Limits and gotchas

- **Use the class, not the interface.** The older `Auth.AuthProviderPlugin` interface is deprecated; Salesforce directs new development to the abstract class `Auth.AuthProviderPluginClass`, and existing interface implementations keep working.[^s2]
- **No single logout hook.** The abstract class has no single-logout method, so you either configure OpenID Connect single logout in Setup or write your own logout methods.[^s1]
- **Callouts need mocks in tests.** Because the class makes HTTP callouts, the guide's tests register an `HttpCalloutMock` implementation with `Test.setMock`, then assert on the token response and user data.[^s1]
- **Don't hard-code tokens.** The sample's own comments warn against hard-coding the refresh token in `AuthProviderTokenResponse`, and the shipped test code has field-name typos, so treat it as illustrative.[^s1]
- **Access and PKCE.** Deploying or editing the definition needs Customize Application and Manage AuthProviders; the `isPkceEnabled` field lists Custom among the types that support PKCE.[^s3]

## When to use it vs. alternatives

Pick a built-in type, or the generic OpenID Connect type, whenever the external service supports it, since those need no Apex.[^s3] Write a custom provider only when the service speaks a nonstandard OAuth variant or exposes user data in a shape the built-in types can't map, and budget for maintaining and testing the class.[^s1] For outbound callouts that only need tokens rather than user login, an **external auth identity provider** used with named credentials is often the better fit: Salesforce says it offers more configuration without custom Apex and, unlike standard authentication providers, can be packaged from Apex.[^s4]

## Connections

Custom authentication providers are part of **Salesforce Identity** and **implement** the **OAuth 2.0** authorization code grant from the client side.[^s5][^s1] They are an **alternative to OpenID Connect authentication providers**, the no-code route for providers that speak OIDC.[^s3] They **depend on custom metadata types** for configuration and on **Apex callouts** for the token exchange, which is why **Apex testing** with callout mocks is part of building one.[^s1] The definition is **configured via** the **Metadata API** AuthProvider type.[^s3] Logout has to be handled separately through **single logout**, and **named credentials** with external auth identity providers cover the outbound-integration case.[^s1][^s4]

## Sources
[^s1]: Salesforce Developers, "Create a Custom Authentication Provider Plug-in", Apex Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/authproviderplugin.htm (accessed 2026-11-28)
[^s2]: Salesforce Developers, "AuthProviderPlugin Interface", Apex Reference Guide. https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apex/apex_interface_Auth_AuthProviderPlugin.htm (accessed 2026-11-28)
[^s3]: Salesforce Developers, "AuthProvider", Metadata API Developer Guide. https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-authprovider.html (accessed 2026-11-28)
[^s4]: Salesforce Developers, "Create an OAuth Named Credential", Named Credentials Developer Guide. https://developer.salesforce.com/docs/platform/named-credentials/guide/nc-create-oauth-cred.html (accessed 2026-11-28)
[^s5]: RFC Editor, "RFC 6749: The OAuth 2.0 Authorization Framework" (October 2012). https://www.rfc-editor.org/info/rfc6749 (accessed 2026-11-28)
