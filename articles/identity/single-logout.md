---
id: kt:single-logout
type: Feature
title: Single Logout
aliases: [SLO, SAML single logout, OpenID Connect single logout, OIDC single logout, federated logout]
domain: identity
summary: >-
  Salesforce's front-channel single logout (SLO) support, which propagates a logout between Salesforce and a
  federated partner over SAML 2.0 or OpenID Connect, whether Salesforce is the identity provider, the service
  provider or the OpenID Connect provider.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity, kt:single-sign-on-saml]
related: [kt:connected-apps, kt:my-domain, kt:experience-cloud-identity, kt:event-monitoring, kt:openid-connect-authentication-providers]
relations:
  - {predicate: implements, object: kt:saml-2-0}
  - {predicate: implements, object: kt:openid-connect}
  - {predicate: configuredVia, object: kt:connected-apps}
  - {predicate: dependsOn, object: kt:my-domain}
sources:
  - id: s1
    title: "Configure SAML Single Logout with Salesforce as the Identity Provider"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.security_auth_slo_saml_idp_configuring.htm&type=5
    type: official-docs
    accessed: 2026-11-11
  - id: s2
    title: "Configure SAML Single Logout with Salesforce as the Service Provider"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.security_auth_slo_saml_sp_configuring.htm&type=5
    type: official-docs
    accessed: 2026-11-11
  - id: s3
    title: "Configure OpenID Connect Single Logout with Salesforce as the OpenID Connect Provider"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=security_auth_slo_oidc_idp_configuring.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-11
  - id: s4
    title: "Create Logout Event Triggers"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.security_auth_create_logout_event_trigger.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-11
  - id: s5
    title: "Security Assertion Markup Language (SAML) V2.0 Technical Overview"
    publisher: OASIS
    url: https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html
    type: standards-body
    accessed: 2026-11-11
  - id: s6
    title: "OpenID Connect Front-Channel Logout 1.0"
    publisher: OpenID Foundation
    url: https://openid.net/specs/openid-connect-frontchannel-1_0.html
    type: standards-body
    accessed: 2026-11-11
created: 2026-11-11
---

# Single Logout

Single logout (SLO) is the counterpart of single sign-on: when a user logs out of one party in a federated session, the logout is carried to the other party so that neither session is left open. In Salesforce it is configured per trust relationship and comes in three shapes: SAML SLO with Salesforce as the identity provider (IdP), SAML SLO with Salesforce as the service provider (SP), and OpenID Connect SLO with Salesforce as the OpenID Connect provider.[^s1][^s2][^s3] Viewing the settings takes View Setup and Configuration; editing them takes Customize Application and Modify All Data.[^s1]

## The standards behind it

The SAML 2.0 Single Logout Protocol aims at near real-time logout of a user from every participant that shares one authentication context after SSO. Any participant can start it; in the usual pattern the IdP coordinates, sending logout requests to the other SPs and returning a response to the originator. Messages may travel over front-channel bindings (HTTP Redirect, POST, Artifact) or the back-channel SOAP binding. OASIS notes that because the user can interrupt the browser hops, the overall result cannot be guaranteed.[^s5] OpenID Connect Front-Channel Logout, a Final specification, has the provider render a page of iframes pointing at each relying party's registered logout URI, optionally with `iss` and `sid` parameters; browsers that block third-party content can make that logout fail silently.[^s6]

## How it works in Salesforce

**Salesforce as SAML IdP.** SLO is set on the connected app for the SP: under Web App Settings, select Enable Single Logout, enter the SP's Single Logout URL (it must start with `https://`) and choose HTTP POST or HTTP Redirect as the Single Logout Binding. When Salesforce starts the logout it sends a LogoutRequest carrying the session index; when the SP starts it, Salesforce returns the LogoutResponse there. The SP starts SLO against `https://MyDomainName.my.salesforce.com/services/auth/idp/saml2/logout`.[^s1]

**Salesforce as SAML SP.** In the SAML Single Sign-On Settings, select Single Logout Enabled, enter the Identity Provider Single Logout URL, pick the request binding and optionally a custom logout URL for SP-initiated logouts. An option reuses the SSO request signature method for SLO; without it, SLO signs with RSA-SHA1 and a SHA1 digest.[^s2]

**Salesforce as OpenID Connect provider.** On the relying party's connected app, under OAuth Policies, select Enable Single Logout and enter the relying party's absolute `https://` logout URL. The relying party starts SLO at `https://MyDomainName.my.salesforce.com/services/auth/idp/oidc/logout`, which is also published through the OpenID Connect discovery endpoint.[^s3]

After an SLO, users land on the logout page set in Session Settings (org-wide, defaulting to the My Domain login page) or in an Experience Cloud site's Login & Registration settings (defaulting to the site login page).[^s1][^s3]

## Limits and gotchas

- **Front-channel only.** All redirects must happen in the same browser; cross-browser SLO isn't supported.[^s1][^s2][^s3]
- **Session index.** As SP, Salesforce keeps only the first session index if several arrive, and a session index can't exceed 512 characters.[^s2]
- **One-way endings.** Logging out of Salesforce doesn't necessarily end the IdP session, and logging out of an SP doesn't necessarily end the Salesforce session.[^s1][^s2]
- **Partner support.** Some IdPs and SPs can't initiate SLO, in which case the SP-initiated configuration steps are skipped.[^s1][^s2]
- **OIDC delay.** A Salesforce-initiated OIDC SLO waits about 10 seconds before redirecting to the login page, giving the relying party time to log out.[^s3]
- **Packaging.** SLO edits made on a connected app's edit page don't automatically update the Manage Connected Apps page, so copy them across manually.[^s1][^s3]

## When to use it (and when not)

Enable SLO whenever a shared workstation or kiosk scenario makes an orphaned session a real risk and the partner supports the same protocol. Because Salesforce's SLO is browser-mediated and best-effort, don't treat it as a security control on its own: pair it with session timeouts and, where you need to act on logout, an Apex trigger on the `LogoutEventStream` platform event, enabled through Event Manager. That event fires only for UI logouts; timeouts publish it only when Force logout on session timeout is on, and closing the browser never does.[^s4] The Help example revokes a user's refresh tokens at logout, a useful backstop for OAuth clients that SLO does not reach.[^s4]

## Connections

SLO extends `kt:single-sign-on-saml` and sits under the `kt:salesforce-identity` umbrella; it implements the logout parts of `kt:saml-2-0` and `kt:openid-connect`.[^s5][^s6] As IdP or OIDC provider it is configured on `kt:connected-apps`, its endpoints hang off `kt:my-domain`, and site-level logout pages belong to `kt:experience-cloud-identity`.[^s1][^s3] The `LogoutEventStream` object links it to `kt:event-monitoring` for logout-time automation.[^s4]

## Sources

[^s1]: Salesforce Help, "Configure SAML Single Logout with Salesforce as the Identity Provider". https://help.salesforce.com/s/articleView?language=en_US&id=sf.security_auth_slo_saml_idp_configuring.htm&type=5 (accessed 2026-11-11)
[^s2]: Salesforce Help, "Configure SAML Single Logout with Salesforce as the Service Provider". https://help.salesforce.com/s/articleView?language=en_US&id=sf.security_auth_slo_saml_sp_configuring.htm&type=5 (accessed 2026-11-11)
[^s3]: Salesforce Help, "Configure OpenID Connect Single Logout with Salesforce as the OpenID Connect Provider". https://help.salesforce.com/s/articleView?id=security_auth_slo_oidc_idp_configuring.htm&language=en_US&type=5 (accessed 2026-11-11)
[^s4]: Salesforce Help, "Create Logout Event Triggers". https://help.salesforce.com/s/articleView?id=xcloud.security_auth_create_logout_event_trigger.htm&language=en_US&type=5 (accessed 2026-11-11)
[^s5]: OASIS, "Security Assertion Markup Language (SAML) V2.0 Technical Overview". https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html (accessed 2026-11-11)
[^s6]: OpenID Foundation, "OpenID Connect Front-Channel Logout 1.0". https://openid.net/specs/openid-connect-frontchannel-1_0.html (accessed 2026-11-11)
