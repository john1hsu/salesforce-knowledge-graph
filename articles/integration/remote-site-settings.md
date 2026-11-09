---
id: kt:remote-site-settings
type: SecurityControl
title: Remote Site Settings
aliases: [remote site setting, remote site, RemoteSiteSetting, remote site allowlist]
domain: integration
summary: >-
  An org-level allowlist of external URLs that Apex callouts may reach; Salesforce blocks callouts to any address not
  registered there, unless the callout's endpoint is defined by a named credential.
release: "Winter '27"
status: current
broader: [kt:integration-security]
related: [kt:apex-callouts, kt:apex-continuations, kt:metadata-api]
relations:
  - {predicate: alternativeTo, object: kt:named-credentials}
  - {predicate: usedBy, object: kt:apex-callouts}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Adding Remote Site Settings (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_callouts_remote_site_settings.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "RemoteSiteSetting (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_remotesitesetting.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s3
    title: "Named Credentials as Callout Endpoints (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/pages/apex_callouts_named_credentials.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s4
    title: "Step 1: Configure a Remote Site (Salesforce CMS Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/cms/guide/cms-dev-step-1__configure-a-remote-site.html
    type: official-docs
    accessed: 2026-11-09
created: 2026-11-09
---

# Remote Site Settings

Remote Site Settings is the Setup page where an admin registers the external web addresses that Apex code is allowed to call. Salesforce refuses callouts to network addresses that have not been authorized, so any external site an Apex callout targets must be listed here or the callout fails at runtime.[^s1] Salesforce's own setup guides describe this as a secure-by-default posture: outbound calls to remote sites are blocked until a site is explicitly allowed.[^s4] The one standard exception is a callout whose endpoint comes from a named credential, which carries its own URL and authentication definition and therefore needs no separate remote site entry.[^s1][^s3]

## How it works

Each entry is a small record: a unique name, the remote site URL, an optional description, and an active flag.[^s2] To create one, an admin searches Setup's Quick Find for Remote Site Settings, clicks New Remote Site, gives it a descriptive name, enters the site's URL, optionally describes it, and saves.[^s1] Setup guides also tell admins to confirm the Active checkbox is selected before saving; the metadata records this as the required `isActive` flag.[^s4][^s2] When Apex then makes an HTTP request to that host, the platform checks the endpoint against the active entries before letting the request leave the org.[^s1]

As metadata, each entry is a `RemoteSiteSetting` component, available since API version 19.0, stored as a `.remoteSite` file in the `remoteSiteSettings` folder of a project or package.[^s2] Its fields are `fullName`, `description`, `url`, `isActive`, and `disableProtocolSecurity`; the last three are required.[^s2] The `fullName` must start with a letter and may contain only alphanumeric characters and underscores, with no trailing or consecutive underscores.[^s2] Because the settings are metadata, they can be retrieved and deployed through Metadata API alongside the Apex that depends on them rather than being re-typed in each org.[^s2]

## Limits and gotchas

- **Protocol security.** `disableProtocolSecurity` set to true lets code exchange data between HTTP and HTTPS sessions in either direction, regardless of how the user is connected; Salesforce warns to enable it only if you understand the security implications.[^s2] Keeping it false and using HTTPS endpoints is the safe default.
- **TLS performance.** Salesforce recommends that remote HTTPS sites have OCSP stapling turned on for best callout performance.[^s1]
- **Allowlisting is not authentication.** A remote site entry only authorizes the destination; the Apex code still has to build any credentials or headers itself, which is the main reason Salesforce steers developers toward named credentials.[^s3][^s1]
- **Per-environment URLs.** A remote site entry hard-wires a host, so sandboxes and production that call different endpoints need different entries and the code needs environment-aware URLs. Named credentials avoid this, because each org can hold a same-named credential pointing at its own endpoint.[^s3]

## When to use it (and when not)

Named credentials are the preferred choice for new integrations: they keep the endpoint and authentication outside the code, let Salesforce handle authentication, let a single `callout:Name/path` reference work across orgs, and can route traffic over a private connection.[^s3] Remote Site Settings remains appropriate for simple or unauthenticated endpoints, for legacy code that builds full URLs, and for installed products whose setup instructions tell admins to register a vendor host.[^s1][^s4] An architect reviewing an org should treat the Remote Site Settings list as an inventory of outbound destinations and question entries that are inactive, unused, or allow mixed protocols.[^s2]

## Connections

`kt:remote-site-settings` sits under `kt:integration-security` because it is a destination allowlist for outbound traffic.[^s1] It is used by `kt:apex-callouts` and their UI-initiated variant `kt:apex-continuations`, both of which need an authorized endpoint before a request can leave the org.[^s1] It is an `alternativeTo` `kt:named-credentials`, which supersede it for endpoints that a named credential defines.[^s3] It is `configuredVia` `kt:metadata-api` as the `RemoteSiteSetting` type, so it belongs in deployment pipelines alongside the code that uses it.[^s2] The edge to `kt:integration-architect-certification` reflects that callout authorization is a core integration design concern.[^s1]

## Sources

[^s1]: Salesforce Developers, "Adding Remote Site Settings (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_callouts_remote_site_settings.htm (accessed 2026-11-09)
[^s2]: Salesforce Developers, "RemoteSiteSetting (Metadata API Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_remotesitesetting.htm (accessed 2026-11-09)
[^s3]: Salesforce Developers, "Named Credentials as Callout Endpoints (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/pages/apex_callouts_named_credentials.htm (accessed 2026-11-09)
[^s4]: Salesforce Developers, "Step 1: Configure a Remote Site (Salesforce CMS Developer Guide)". https://developer.salesforce.com/docs/platform/cms/guide/cms-dev-step-1__configure-a-remote-site.html (accessed 2026-11-09)
