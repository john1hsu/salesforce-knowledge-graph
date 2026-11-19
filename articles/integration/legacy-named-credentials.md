---
id: kt:legacy-named-credentials
type: Feature
title: Legacy Named Credentials
aliases: [legacy named credential, NamedCredentialType Legacy, pre-Winter '23 named credentials]
domain: integration
summary: >-
  The original, pre-Winter '23 form of Salesforce named credentials, in which one record holds both a callout endpoint
  URL and its authentication settings; deprecated in favour of the extensible named credential plus external credential
  model, and no longer enhanced.
release: "Winter '27"
status: deprecated
broader: [kt:integration-security]
related: [kt:apex-callouts, kt:remote-site-settings]
relations:
  - {predicate: replacedBy, object: kt:named-credentials}
  - {predicate: consumedBy, object: kt:salesforce-connect}
  - {predicate: consumedBy, object: kt:external-services}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: dependsOn, object: kt:permission-sets}
sources:
  - id: s1
    title: "Understand Legacy Named Credentials"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.named_credentials_legacy_about.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-19
  - id: s2
    title: "Define a Legacy Named Credential"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=named_credentials_define.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-19
  - id: s3
    title: "Get Started with Named Credentials"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/named-credentials/guide/get-started.html
    type: official-docs
    accessed: 2026-11-19
  - id: s4
    title: "NamedCredential (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-namedcredential.html
    type: official-docs
    accessed: 2026-11-19
  - id: s5
    title: "Named Credentials Glossary"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/named-credentials/references/named-credentials-reference/nc-glossary.html
    type: official-docs
    accessed: 2026-11-19
created: 2026-11-19
---

# Legacy Named Credentials

A **legacy named credential** is the first-generation form of the named credential: a single Setup record that stores both the URL of a callout endpoint and the authentication parameters needed to call it.[^s1][^s5] As with the current model, Salesforce handles authentication for any callout that references it, and no remote site setting is needed for the endpoint it defines.[^s1] Winter '23 introduced an extensible replacement that splits the endpoint (named credential) from the authentication (external credential). Salesforce now describes legacy named credentials as deprecated, no longer updated or enhanced, and due to be discontinued in a future release.[^s1][^s3] The docs opened for this article give no retirement date.[^s3]

## How it works

A legacy named credential has a label, an API name, a URL, an optional certificate, an identity type, an authentication protocol and callout options, all on one record.[^s2] The URL must start with `http://` or `https://` and may include a path but not a query string. Query strings and further path segments are added in the callout reference.[^s2]

The identity type decides whose credentials are sent:[^s2]

- **Anonymous** sends no identity or authentication.[^s2]
- **Per User** has each user supply their own credentials in personal settings, once a permission set or profile grants access.[^s1][^s2]
- **Named Principal** uses one shared set of credentials for every user in the org.[^s2]

The supported protocols are basic password authentication, OAuth 2.0 (through an authentication provider and scope), JWT, JWT Token Exchange and AWS Signature Version 4.[^s1][^s2] An optional certificate supports two-way TLS and digital signatures. For JWT protocols, a separate signing certificate is chosen.[^s2] The callout options are the same as in the current model: **Generate Authorization Header** (on by default), plus switches that allow merge fields in HTTP headers and bodies for Apex callouts.[^s2]

Legacy named credentials work with Apex callouts, External Services and some Salesforce Connect external data sources: OData 2.0 and 4.0, Apex Connector Framework adapters and Amazon DynamoDB.[^s1][^s2]

## In metadata

In the Metadata API, the `NamedCredential` type has a `NamedCredentialType` value of `Legacy` for these records. That value marks a credential that doesn't use the Winter '23 schema and is kept for backward compatibility. `SecuredEndpoint` and `PrivateEndpoint` are the external-credential-based types.[^s4] All the fields that put authentication inside the named credential are valid only for the `Legacy` type and were deprecated in API version 56.0. These include `endpoint`, `principalType`, `protocol`, `authProvider`, `username`, `password`, the `jwt*` fields and the `aws*` fields.[^s4] Code or deployment pipelines that still write those fields are therefore working with the legacy model.[^s4]

## Limits and gotchas

- **Frozen feature.** Legacy named credentials get no new capabilities. Salesforce strongly recommends the extensible model for all new work.[^s1][^s2]
- **Auth tied to endpoint.** Authentication can't be shared across endpoints or swapped without editing the credential. In the current model, several named credentials can reuse one external credential.[^s3][^s5]
- **Coarser access control.** Per-user access is granted through permission sets or profiles on the credential itself. The current model maps principals on an external credential to permission sets.[^s1][^s3]
- **Permissions.** View Setup and Configuration lets you view them. Manage Named Credentials or Customize Applications lets you create, edit or delete them.[^s2]
- **Naming rules.** API names must start with a letter and use only letters, numbers and underscores. They can't contain spaces, end with an underscore or have consecutive underscores.[^s2]
- **External data sources.** Merge-field options aren't available to external data sources, which also need Generate Authorization Header enabled.[^s2]

## When to use it (and when not)

Don't create new legacy named credentials. Use a named credential backed by an external credential instead.[^s1][^s3] You will still meet legacy records in older orgs and packages. Treat them as technical debt. You can find them in metadata as type `Legacy`.[^s4] Rebuild each one as an external credential plus a named credential, with principals mapped to permission sets.[^s3][^s5] The Salesforce docs opened for this article give no step-by-step migration procedure. Plan and test the cutover yourself, including re-entering secrets and re-authorizing OAuth.[^s1][^s3]

## Connections

Legacy named credentials sit under **integration security** and are **replaced by** the current **named credentials** model, which is their migration path.[^s1][^s3] Like their successor, they remove the need for **remote site settings** for their own endpoint, and **Apex callouts** reference them by name.[^s1] They are **consumed by Salesforce Connect** external data sources and by **External Services**.[^s1] They are deployed through the **Metadata API** `NamedCredential` type, as type `Legacy`.[^s4] Per-user access **depends on permission sets** or profiles.[^s1][^s2]

## Sources
[^s1]: Salesforce Help, "Understand Legacy Named Credentials". https://help.salesforce.com/s/articleView?id=xcloud.named_credentials_legacy_about.htm&language=en_US&type=5 (accessed 2026-11-19)
[^s2]: Salesforce Help, "Define a Legacy Named Credential". https://help.salesforce.com/s/articleView?id=named_credentials_define.htm&language=en_US&type=5 (accessed 2026-11-19)
[^s3]: Salesforce Developers, "Get Started with Named Credentials". https://developer.salesforce.com/docs/platform/named-credentials/guide/get-started.html (accessed 2026-11-19)
[^s4]: Salesforce Developers, "NamedCredential (Metadata API Developer Guide)". https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-namedcredential.html (accessed 2026-11-19)
[^s5]: Salesforce Developers, "Named Credentials Glossary". https://developer.salesforce.com/docs/platform/named-credentials/references/named-credentials-reference/nc-glossary.html (accessed 2026-11-19)
