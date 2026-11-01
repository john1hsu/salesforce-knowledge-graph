---
id: kt:named-credentials
type: Feature
title: Named Credentials
aliases: [named credential, external credentials, external credential, callout named credential, enhanced named credentials]
domain: integration
summary: >-
  Salesforce's declarative way to define an outbound callout endpoint (named credential) separately from how Salesforce
  authenticates to it (external credential), so Apex, External Services and Salesforce Connect can call external
  systems without hard-coded URLs, secrets or remote site settings.
release: "Winter '27"
status: current
broader: [kt:integration-security]
related: [kt:apex, kt:connected-apps]
relations:
  - {predicate: replaces, object: kt:legacy-named-credentials}
  - {predicate: alternativeTo, object: kt:remote-site-settings}
  - {predicate: enables, object: kt:salesforce-connect}
  - {predicate: dependsOn, object: kt:permission-sets}
sources:
  - id: s1
    title: "Get Started with Named Credentials"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/named-credentials/guide/get-started.html
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "Named Credentials as Callout Endpoints (Apex Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_callouts_named_credentials.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "Parts of a Named Credential: Create a Basic Authentication External Credential"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=xcloud.nc_parts_of_nc.htm
    type: official-docs
    accessed: 2026-11-01
  - id: s4
    title: "Named Credentials and External Credentials"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.nc_named_creds_and_ext_creds.htm&language=pt_BR&type=5
    type: official-docs
    accessed: 2026-11-01
  - id: s5
    title: "Legacy Named Credentials"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=xcloud.named_credentials_define.htm
    type: official-docs
    accessed: 2026-11-01
created: 2026-11-01
---

# Named Credentials

Named credentials are the platform's standard mechanism for **outbound** authenticated callouts. A named credential holds the URL of a callout endpoint, and it is used in place of a raw URL by Apex callouts, external data sources and External Services.[^s1] Since Winter '23 the model splits the endpoint from the authentication: the named credential points at an **external credential**, which describes how Salesforce authenticates to the remote system, so code never carries endpoints or secrets.[^s1][^s4]

## How it works

The current model has four moving parts.[^s1][^s3]

- **Named credential** – the endpoint URL and HTTP transport. Several named credentials can share one external credential.[^s1]
- **External credential** – the authentication protocol (for example Basic, OAuth 2.0 variants, JWT, AWS Signature v4, Custom or No Authentication) and the permission sets or profiles allowed to use it.[^s1][^s3]
- **Principals** – entries on the external credential that are mapped to permission sets or profiles. A *named principal* uses a single identity for the whole org; a *per-user principal* authenticates each user individually. At runtime Salesforce checks that the running user has a mapped permission set or profile before it calls out.[^s3][^s4]
- **User external credentials** – the object where Salesforce stores the encrypted tokens. Callers need access to it; most standard profiles and permission sets already have it, but the guest user profile and some custom profiles or permission sets must be granted it explicitly.[^s1][^s4]

Custom headers can be defined on both named and external credentials for extra protocol or security requirements.[^s1]

In Apex, the endpoint is written with the `callout:` scheme followed by the named credential's API name and an optional path, for example `callout:My_Named_Credential/some_path`, with a `?` before any query string.[^s2] Salesforce generates the authorization header itself (this can be switched off), and merge fields can be used to build custom headers or bodies. Because authentication is handled by the platform, the Apex code is unchanged whichever protocol the external credential uses.[^s2]

## Benefits

- **No remote site settings** for the host defined in the named credential; other external callouts still need one.[^s2][^s5]
- **Environment portability.** Create a named credential with the same API name but a different URL in each org (sandbox, UAT, production). One Apex callout definition then deploys everywhere without environment checks, and a URL change touches only the credential.[^s2]
- **Least-privilege access.** Mapping principals to permission sets means the ability to call an external system is granted like any other permission.[^s3][^s4]
- **Private routing.** The `OutboundNetworkConnection` field routes callouts through a private connection.[^s2]

## Limits and gotchas

- External credential API names may contain only letters, numbers and underscores. They must start with a letter and can't contain spaces, end with an underscore or have consecutive underscores.[^s3]
- You can't change a principal's name or identity type after it is created; delete and recreate it instead. Principal sequence numbers set priority, and lower numbers are evaluated first.[^s3]
- Viewing credentials requires View Setup and Configuration. Creating, editing or deleting them requires Manage Named Credentials or Customize Applications.[^s3]
- Access tokens and other secrets can't be packaged. After installing or deploying, populate them through Setup or the Connect API, and plan that step into your release process.[^s1]
- **Legacy named credentials** combine the URL and authentication in one record. They are no longer enhanced, and the developer guide marks them as deprecated, with discontinuation planned for a future release. New work should use the external-credential model.[^s1][^s5]

## When to use it (and when not)

Use a named credential for any outbound HTTP integration from Salesforce: Apex REST/SOAP callouts, External Services, and Salesforce Connect adapters such as OData 2.0/4.0, Apex Connector Framework custom adapters and Amazon DynamoDB.[^s5][^s1] A hard-coded endpoint with a remote site setting and secrets in custom settings or metadata is the anti-pattern it replaces.[^s2] Named credentials do **not** govern inbound access. In this graph, inbound access is covered by connected apps and external client apps.

## Connections

Named credentials sit under **integration security** as the outbound counterpart to **connected apps**, which handle inbound OAuth clients. They **replace legacy named credentials**, the pre-Winter '23 single-record form.[^s5] They are an **alternative to remote site settings**, which they make unnecessary for their own host.[^s2] They **enable Salesforce Connect** external data sources and External Services.[^s5] Callout authorization **depends on permission sets** (or profiles) mapped to principals.[^s3] They are most often used from **Apex**, via the `callout:` endpoint syntax.[^s2]

## Sources
[^s1]: Salesforce Developers, "Get Started with Named Credentials". https://developer.salesforce.com/docs/platform/named-credentials/guide/get-started.html (accessed 2026-11-01)
[^s2]: Salesforce Developers, "Named Credentials as Callout Endpoints (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/api/apex_callouts_named_credentials.htm (accessed 2026-11-01)
[^s3]: Salesforce Help, "Parts of a Named Credential: Create a Basic Authentication External Credential". https://help.salesforce.com/apex/HTViewHelpDoc?id=xcloud.nc_parts_of_nc.htm (accessed 2026-11-01)
[^s4]: Salesforce Help, "Named Credentials and External Credentials". https://help.salesforce.com/s/articleView?id=xcloud.nc_named_creds_and_ext_creds.htm&language=pt_BR&type=5 (accessed 2026-11-01)
[^s5]: Salesforce Help, "Legacy Named Credentials". https://help.salesforce.com/apex/HTViewHelpDoc?id=xcloud.named_credentials_define.htm (accessed 2026-11-01)
