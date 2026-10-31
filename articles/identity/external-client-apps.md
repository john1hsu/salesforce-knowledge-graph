---
id: kt:external-client-apps
type: Feature
title: External Client Apps
aliases: [external client app, ECA, ExternalClientApplication, next-generation connected apps]
domain: identity
summary: >-
  The successor to connected apps: a packageable, metadata-compliant framework that registers third-party
  applications for OAuth and SAML access to Salesforce, local to its org by default, with developer-owned
  settings separated from subscriber-admin policies.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:connected-apps, kt:oauth-2-flows-in-salesforce, kt:single-sign-on-saml, kt:second-generation-managed-packages, kt:sandbox-types]
relations:
  - {predicate: replaces, object: kt:connected-apps}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: implements, object: kt:oauth-2-0}
  - {predicate: dependsOn, object: kt:second-generation-managed-packages}
sources:
  - id: s1
    title: "External Client Apps"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-10-31
  - id: s2
    title: "Integrate External Applications with Salesforce (connected apps and external client apps)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.external_integrations.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-10-31
  - id: s3
    title: "Use External Client Apps When Connected Apps Won't Do (External Client App Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/external-client-app-basics/use-external-client-apps-when-connected-apps-wont-do
    type: official-learning
    accessed: 2026-10-31
  - id: s4
    title: "Package and Distribute External Client Apps (External Client App Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/external-client-app-basics/package-and-distribute-external-client-apps
    type: official-learning
    accessed: 2026-10-31
  - id: s5
    title: "Create an External Client App (Mobile SDK Development Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/mobile-sdk/guide/eca-create.html
    type: official-docs
    accessed: 2026-10-31
  - id: s6
    title: "ExtlClntAppOauthSettings (Metadata API Developer Guide, Winter '27)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_extlclntappoauthsettings.htm
    type: official-docs
    accessed: 2026-10-31
created: 2026-10-31
---

# External Client Apps

An external client app (ECA) is the Salesforce framework for letting a third-party application integrate with an org through its APIs. Like its predecessor, it uses OAuth and SAML to authorize the app and to provide single sign-on, but it is designed from the start to be packageable.[^s1] Salesforce describes ECAs as the next generation of connected apps: fully metadata-compliant, with a structure that keeps developer and administrator roles apart and supports second-generation managed packaging. Salesforce now recommends ECAs in all situations and suggests migrating local connected apps to local ECAs.[^s2]

## How it works

**Secure and local by default.** A connected app, once created, is broadly available; an ECA instead works only in the org where it was created unless a developer deliberately packages it.[^s3] Each ECA has a *distribution state*: **Local** (usable only in its home org) or **Packaged** (distributed through a managed package).[^s1][^s5]

**Settings vs. policies.** ECAs split configuration by role. Developers own the **Settings** tab — default values and protected sensitive data such as the OAuth consumer secret — and those settings travel in the package. Subscriber admins own the **Policies** tab, where they tune the app for their org, for example limiting access to specific permission sets or setting refresh-token policies that cut off a third-party app after a period. Policies stay local and are never packaged, and admins cannot edit the developer's settings.[^s1][^s3]

**Global vs. local OAuth settings.** The OAuth configuration is itself split: a *global* settings file holds the consumer details, and a separate file holds the remaining OAuth settings, contains nothing sensitive, and points back to the global file.[^s1] In Metadata API this surfaces as a family of types — `ExternalClientApplication`, `ExtlClntAppOauthSettings`, `ExtlClntAppGlobalOauthSettings`, `ExtlClntAppOauthConfigurablePolicies`, plus canvas, mobile, push, notification and SAML settings and policy types.[^s6]

**Plugins and flows.** Capabilities are added as plugins — OAuth, SAML SSO, canvas, mobile, push notifications and notifications — and Salesforce Help documents ECA guides for the client credentials, device, JWT bearer and web server flows, among others.[^s1] Creating one in Setup goes through App Manager > New External Client App: enter basic information, choose the distribution state, enable OAuth, add a callback URL and scopes, and set security options such as whether a secret is required for the web server and refresh token flows.[^s5]

## Packaging and distribution

The headline advantage is distribution in second-generation managed packages, which are built with Salesforce DX tooling and Metadata API and support source-controlled package metadata.[^s4] Salesforce Help notes that first- or second-generation managed packages can carry an ECA.[^s1] The global OAuth settings must *not* be packaged; they belong in a long-lived, non-ephemeral org (for example the Dev Hub) that outlives the packages. A subscriber org can share the originating app's OAuth credentials or have new ones generated on install; configuring OAuth credentials locally breaks the association with the developer org's app.[^s4][^s1] Packaged ECAs can also be listed on AgentExchange.[^s3][^s4]

## Limits and gotchas

- **Local means local.** Only packaged ECAs can be deployed to other orgs, and local ECAs are not copied when a sandbox is created or refreshed — only packaged ones are.[^s1] Plan sandbox seeding accordingly.
- **One authorization plugin per app** is recommended, because profile and permission-set assignments apply to every plugin on the ECA.[^s1]
- **Feature parity is not complete.** Salesforce Help states that some features remain available only through connected apps, so check the comparison article before migrating an integration that relies on niche connected-app behaviour.[^s2]
- **Connected app creation is restricted** as of Spring '26; existing connected apps keep working, and creating a new one requires contacting Salesforce Support — which makes ECAs the practical default for new work.[^s5]

## When to use it (and when not)

Use an ECA for every new integration, and especially when an app must be shipped to many orgs through a managed package or AgentExchange, or when admins need tight control over which users can reach a third-party app.[^s3][^s4] Keep an existing connected app only where it depends on a capability ECAs do not yet offer, and schedule its migration; Salesforce's Insights page checks both kinds of app for required OAuth and proof-of-possession controls.[^s2]

## Connections

ECAs sit under **Salesforce Identity** and **replace connected apps** as the recommended way to register clients.[^s2] They are the configuration point for the **OAuth 2.0 flows in Salesforce** and implement the **OAuth 2.0** client-registration model, and with the SAML plugin they back **single sign-on (SAML)**.[^s1] Their packaging story **depends on second-generation managed packages** and on **Metadata API** types for source-driven development.[^s4][^s6] The local-only rule interacts with **sandbox types**, since refreshes carry only packaged ECAs.[^s1]

## Sources
[^s1]: Salesforce Help, "External Client Apps". https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm&language=en_US&type=5 (accessed 2026-10-31)
[^s2]: Salesforce Help, "Integrate External Applications with Salesforce". https://help.salesforce.com/s/articleView?id=xcloud.external_integrations.htm&language=en_US&type=5 (accessed 2026-10-31)
[^s3]: Trailhead, "Use External Client Apps When Connected Apps Won't Do". https://trailhead.salesforce.com/content/learn/modules/external-client-app-basics/use-external-client-apps-when-connected-apps-wont-do (accessed 2026-10-31)
[^s4]: Trailhead, "Package and Distribute External Client Apps". https://trailhead.salesforce.com/content/learn/modules/external-client-app-basics/package-and-distribute-external-client-apps (accessed 2026-10-31)
[^s5]: Salesforce Developers, "Create an External Client App" (Mobile SDK Development Guide). https://developer.salesforce.com/docs/platform/mobile-sdk/guide/eca-create.html (accessed 2026-10-31)
[^s6]: Salesforce Developers, "ExtlClntAppOauthSettings" (Metadata API Developer Guide, Winter '27). https://developer.salesforce.com/docs/atlas.en-us.264.0.api_meta.meta/api_meta/meta_extlclntappoauthsettings.htm (accessed 2026-10-31)
