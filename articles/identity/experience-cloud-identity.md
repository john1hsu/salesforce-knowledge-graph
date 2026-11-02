---
id: kt:experience-cloud-identity
type: Feature
title: Experience Cloud Identity
aliases: [Experience Cloud site login and registration, external user login for Experience Cloud sites, site self-registration, Login Discovery, passwordless login for Experience Cloud]
domain: identity
summary: >-
  The login, self-registration, verification and password-management features of an Experience Cloud site,
  configured under Administration > Login & Registration, that let customers and partners sign up and sign in with
  a password, a verified email or phone code (Login Discovery), or a third-party identity provider.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity, kt:experience-cloud]
related: [kt:headless-identity, kt:multi-factor-authentication]
relations:
  - {predicate: configuredVia, object: kt:experience-builder}
  - {predicate: requiresLicense, object: kt:external-identity-license}
  - {predicate: integratesWith, object: kt:openid-connect-authentication-providers}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "Set Up an Experience Cloud Site for Salesforce Customer Identity (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/identity_external/identity_external_community
    type: official-learning
    accessed: 2026-11-02
  - id: s2
    title: "Create a Self-Registration Page (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/identity_external/identity_external_registration
    type: official-learning
    accessed: 2026-11-02
  - id: s3
    title: "Identity for Mobile-Centric Customers: Learn the Basics (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/identity-for-mobile-centric-customers/identity_mfi_basics
    type: official-learning
    accessed: 2026-11-02
  - id: s4
    title: "Identity for Mobile-Centric Customers: Set Up Passwordless Login and Sign-Up with Clicks (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/identity-for-mobile-centric-customers/identity_mfi_clicks
    type: official-learning
    accessed: 2026-11-02
  - id: s5
    title: "LoginDiscoveryHandler Interface (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_interface_Auth_LoginDiscoveryHandler.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s6
    title: "NetworkSelfRegistration (Object Reference for the Salesforce Platform)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_networkselfregistration.htm
    type: official-docs
    accessed: 2026-11-02
created: 2026-11-02
---

# Experience Cloud Identity

Experience Cloud identity is the set of site-level features that control how external users (customers, partners, patients, dealers) sign up for, log in to, verify themselves on and recover access to an Experience Cloud site. Salesforce delivers customer identity through Experience Cloud sites: the community licence that comes with Salesforce Identity is what lets you build pages where customers and partners self-register and log in.[^s1] Trailhead describes the scope as the whole login lifecycle (sign-up, login, identity verification, password reset and logout), designed mobile-first and configured mostly with clicks.[^s3] Where `kt:salesforce-identity` is the umbrella IAM product, this node is the practitioner's view of one site's front door.

## How it works

Each site gets default login, password-management and self-registration pages from its template. With the Customer Service template, publishing the site in Experience Builder creates the login, forgot-password, change-password and self-registration pages, and membership is controlled by adding profiles under Administration > Members.[^s1] Everything else lives in Experience Workspaces under **Administration > Login & Registration**: branding (logo, background colour or image, login button colour, footer text), which applies to the Log In, Sign Up, Verify and Reset Password pages alike, plus the login and registration page setup.[^s4][^s1]

**Login page types.** The default Experience Builder page is the quick, general-purpose option; a Visualforce page gives pixel-level control with custom CSS and JavaScript but needs developer skills.[^s2] The third option is a **Login Discovery Page**: the user first enters an identifier, such as an email or phone number, and only then is challenged.[^s4] Login Discovery deliberately separates *identification* from *verification*; the identifier may be a username, email, phone or custom value, and the challenge may be a password or passwordless.[^s3] Behind the page sits an Apex class implementing `Auth.LoginDiscoveryHandler`, whose `login(identifier, startUrl, requestAttributes)` method looks up the user and returns a PageReference. It can call `Site.passwordlessLogin` to send a one-time code by email or SMS, or redirect the user to a third-party identity provider; SSO-enabled users then skip the Salesforce login step.[^s5] Admins can generate a default handler from Login & Registration and set the user it runs as, which Trailhead advises should be a dedicated system user in production.[^s4]

**Self-registration.** Enabling self-registration adds a "Not a member?" link to the login page. When someone registers, Salesforce creates a Contact and a User, links the Contact to the configured default account, and assigns the configured profile.[^s2] The account is stored per site in the `NetworkSelfRegistration` object. If no account is specified, Salesforce creates person accounts instead, but only when person accounts are enabled.[^s6] The **Configurable Self-Reg Page** type lets admins choose which user fields to collect and a verification method (Email, Text Message or None), and optionally include password fields as a fallback if the user loses access to their phone or inbox.[^s4]

## Limits and gotchas

- Passwordless login works only with **verified** email addresses or phone numbers, so the handler must give users without one a path, typically a password.[^s5]
- The default discovery handler validates identifier format before showing the verification page, which can enable **user enumeration**. Salesforce recommends a dummy verification page and generic errors.[^s5]
- Verified emails and phones can be duplicated across users in an org, but a customer identifier must resolve to exactly one user. The sample handler filters by the External Identity User profile to achieve this.[^s5] Reusing an email at sign-up produces a "portal user already exists for contact" error.[^s4]
- Email verification is included, but SMS verification needs the Identity Verification Credits add-on.[^s3]
- If sign-up doesn't collect a last name, Salesforce assigns a placeholder (for example "ExternalUser" plus a number), which you can collect later through progressive profiling. Sign-up emails also need a verified sender address and a published site.[^s4]
- `LoginDiscoveryHandler` supports Customer Community, Customer Community Plus, External Identity, Partner Community and Partner Community Plus licences.[^s5]

## When to use it (and when not)

Use the out-of-the-box pages with a Login Discovery page when you want low-friction B2C sign-in without building UI. Use Visualforce pages when branding requirements outgrow Experience Builder.[^s2] For an off-platform web or mobile app with its own native UI, consider `kt:headless-identity` instead. If customers should sign in with an existing social or enterprise account, the discovery handler can route them to that provider.[^s5][^s3]

## Connections

This feature is a part of both `kt:salesforce-identity` and `kt:experience-cloud`: sites are the container for customer identity.[^s1] It is configured through Experience Workspaces and `kt:experience-builder`, which generates the default pages.[^s1] Its users typically hold an `kt:external-identity-license`, whose cloned External Identity User profile is the basis of sample setups.[^s4][^s5] Redirects to social or enterprise providers connect it to `kt:openid-connect-authentication-providers`.[^s3][^s5] Verification codes and authenticator factors relate it to `kt:multi-factor-authentication`.[^s3] Native-app use of the same back end is `kt:headless-identity`. The topic is examined in the `kt:identity-and-access-management-architect-certification`.

## Sources
[^s1]: Trailhead, "Set Up an Experience Cloud Site for Salesforce Customer Identity". https://trailhead.salesforce.com/identity_external/identity_external_community (accessed 2026-11-02)
[^s2]: Trailhead, "Create a Self-Registration Page". https://trailhead.salesforce.com/identity_external/identity_external_registration (accessed 2026-11-02)
[^s3]: Trailhead, "Identity for Mobile-Centric Customers: Learn the Basics". https://trailhead.salesforce.com/content/learn/modules/identity-for-mobile-centric-customers/identity_mfi_basics (accessed 2026-11-02)
[^s4]: Trailhead, "Identity for Mobile-Centric Customers: Set Up Passwordless Login and Sign-Up with Clicks". https://trailhead.salesforce.com/content/learn/modules/identity-for-mobile-centric-customers/identity_mfi_clicks (accessed 2026-11-02)
[^s5]: Salesforce Developers, "LoginDiscoveryHandler Interface". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_interface_Auth_LoginDiscoveryHandler.htm (accessed 2026-11-02)
[^s6]: Salesforce Developers, "NetworkSelfRegistration". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_networkselfregistration.htm (accessed 2026-11-02)
