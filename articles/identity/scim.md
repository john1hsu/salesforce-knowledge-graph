---
id: kt:scim
type: ExternalConcept
title: SCIM (System for Cross-domain Identity Management)
aliases: [SCIM 2.0, System for Cross-domain Identity Management, SCIM standard, RFC 7643, RFC 7644]
domain: identity
summary: >-
  The IETF standard (RFC 7642, 7643 and 7644, later extended by RFC 9865 and RFC 9967) that defines a JSON schema for
  users and groups and an HTTP/REST protocol for creating, reading, updating and deprovisioning identities across
  domains; Salesforce and Slack both expose SCIM endpoints so identity providers can manage their users.
release: "Winter '27"
status: concept
broader: [kt:user-provisioning]
related: [kt:salesforce-identity, kt:saml-2-0, kt:openid-connect, kt:identity-connect, kt:user-management]
relations:
  - {predicate: consumedBy, object: kt:salesforce-scim}
  - {predicate: consumedBy, object: kt:slack-platform}
  - {predicate: contrastsWith, object: kt:just-in-time-provisioning}
  - {predicate: dependsOn, object: kt:oauth-2-0}
sources:
  - id: s1
    title: "RFC 7642: System for Cross-domain Identity Management: Definitions, Overview, Concepts, and Requirements"
    publisher: IETF / RFC Editor
    url: https://www.rfc-editor.org/info/rfc7642
    type: standards-body
    accessed: 2026-11-17
  - id: s2
    title: "RFC 7643: System for Cross-domain Identity Management: Core Schema"
    publisher: IETF / RFC Editor
    url: https://www.rfc-editor.org/rfc/rfc7643
    type: standards-body
    accessed: 2026-11-17
  - id: s3
    title: "RFC 7644: System for Cross-domain Identity Management: Protocol"
    publisher: IETF / RFC Editor
    url: https://rfc-editor.org/rfc/rfc7644
    type: standards-body
    accessed: 2026-11-17
  - id: s4
    title: "RFC 9865: Cursor-Based Pagination of SCIM Resources"
    publisher: IETF Datatracker
    url: https://datatracker.ietf.org/doc/rfc9865/
    type: standards-body
    accessed: 2026-11-17
  - id: s5
    title: "RFC 9967: SCIM Profile for Security Event Tokens (SETs)"
    publisher: IETF / RFC Editor
    url: https://www.rfc-editor.org/rfc/rfc9967
    type: standards-body
    accessed: 2026-11-17
  - id: s6
    title: "Provision Users and Groups with SCIM"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/slack-apis-for-automating-and-managing-your-org/provision-users-and-groups-with-scim
    type: official-learning
    accessed: 2026-11-17
created: 2026-11-17
---

# SCIM (System for Cross-domain Identity Management)

**SCIM** is an open IETF standard for moving identity records between systems. It defines a common JSON representation of users and groups and a REST protocol for creating, reading, changing and removing them, so that an identity provider or HR system can keep accounts in many cloud services in step.[^s2][^s3] Salesforce's own Trailhead content describes it as an open standard for provisioning and updating users and groups through RESTful APIs.[^s6]

The SCIM 2.0 baseline is three documents published in September 2015. RFC 7642 is Informational and sets out the concepts, actors, flows and requirements. RFC 7643 (Core Schema) and RFC 7644 (Protocol) are Proposed Standards on the standards track.[^s1][^s2][^s3] A Salesforce engineer is among the co-authors of both standards-track RFCs.[^s2][^s3]

## Concepts and use cases

RFC 7642 frames SCIM around a cloud service provider that holds identities, an enterprise subscriber that administers a group of them, and the end user who signs in. It describes create, update, delete and single sign-on triggers, in push and pull modes.[^s1] Its scenarios include enterprise-to-cloud and cloud-to-cloud provisioning, migrating identities between providers, and change notification. It stresses that SCIM handles provisioning separately from authentication, unlike SAML web SSO, which can create accounts only at sign-in.[^s1]

## Core schema

Every SCIM resource lists the schema URIs it uses in a `schemas` array. The core User schema is `urn:ietf:params:scim:schemas:core:2.0:User` and the Group schema is `urn:ietf:params:scim:schemas:core:2.0:Group`.[^s2] All resources share three common attributes. `id` is a stable, read-only identifier issued by the service provider. `externalId` is issued by the client. `meta` carries the resource type, created and last-modified timestamps, location and an optional version.[^s2] On a User, `userName` is required and unique, and attributes such as `name`, `emails`, `active` and a read-only `groups` list follow. An enterprise extension adds fields like `employeeNumber`, `costCenter`, `department` and `manager` in its own namespace.[^s2]

Each attribute declares its characteristics: mutability (`readOnly`, `readWrite`, `immutable`, `writeOnly`), when it is returned (`always`, `never`, `default`, `request`), uniqueness and case sensitivity.[^s2] Passwords are `writeOnly`, and a service provider must never return them in clear or hashed form.[^s2] Three discovery resources, `ServiceProviderConfig`, `ResourceType` and `Schema`, let a client learn which optional features and attributes a given provider supports.[^s2]

## Protocol

RFC 7644 maps operations onto HTTP. GET reads, POST creates or searches, PUT replaces, PATCH modifies and DELETE removes. PUT must not be used to create resources.[^s3] Standard endpoints include `/Users`, `/Groups`, `/Me`, `/Bulk` and the three discovery endpoints.[^s3] Filters use operators such as `eq`, `co`, `sw`, `pr`, `gt` and `le`, combined with `and`, `or` and `not`. Index-based paging uses a 1-based `startIndex` and `count`, and is stateless, so results can shift between pages.[^s3] PATCH is optional and applies `add`, `remove` and `replace` operations in order, as one atomic change.[^s3]

Bulk requests are optional. The provider advertises `maxOperations` and `maxPayloadSize`, rejects oversized requests with HTTP 413, and lets operations refer to each other through client-assigned `bulkId` values.[^s3] Versioning uses HTTP ETags: `If-Match` on an update returns 412 if the resource has changed since it was read.[^s3]

SCIM defines no authentication scheme of its own. It relies on TLS and standard HTTP schemes, with OAuth 2.0 bearer tokens among the options. TLS 1.2 support is mandatory.[^s3] Personal data must not travel in request URIs, so sensitive filters belong in a POST to a `/.search` endpoint rather than a GET query string.[^s3]

## Later extensions

RFC 9865 (October 2025) updates both standards-track RFCs with cursor-based pagination. Clients pass a `cursor` value and providers return `nextCursor`, so a provider can expose its native cursor backend instead of caching results to emulate indexes.[^s4] RFC 9967 (May 2026) adds a SCIM profile for Security Event Tokens. It defines provisioning events such as create, patch, delete, activate and deactivate, and an asynchronous request mode that answers HTTP 202 and later sends a completion event.[^s5]

## Gotchas for Salesforce practitioners

Most of SCIM is optional, so two compliant implementations can differ widely. Read a provider's `ServiceProviderConfig` before assuming bulk, sorting, ETags or cursor paging are available.[^s2][^s3][^s4] Deprovisioning semantics also vary: RFC 7642 notes that one provider may suspend an account where another deletes it.[^s1] Slack, for example, signs a deprovisioned user out of every device at once, and its SCIM API needs a Business+ or Enterprise plan.[^s6]

## Connections

SCIM sits under **user provisioning** (`broader`) as the standard for lifecycle sync between directories and services.[^s1] It is `consumedBy` the **Salesforce SCIM API**, Salesforce's implementation of the standard, and by the **Slack platform**, whose SCIM API lets identity providers manage members and groups.[^s6] It `contrastsWith` **just-in-time provisioning**, which creates accounts at sign-in rather than ahead of time.[^s1] It `dependsOn` **OAuth 2.0** in practice, since bearer tokens are the usual way clients authorize.[^s3] It complements **SAML 2.0** and **OpenID Connect**, which handle authentication while SCIM handles the account records behind it.[^s1]

## Sources

[^s1]: IETF, "RFC 7642: System for Cross-domain Identity Management: Definitions, Overview, Concepts, and Requirements". https://www.rfc-editor.org/info/rfc7642 (accessed 2026-11-17)
[^s2]: IETF, "RFC 7643: System for Cross-domain Identity Management: Core Schema". https://www.rfc-editor.org/rfc/rfc7643 (accessed 2026-11-17)
[^s3]: IETF, "RFC 7644: System for Cross-domain Identity Management: Protocol". https://rfc-editor.org/rfc/rfc7644 (accessed 2026-11-17)
[^s4]: IETF, "RFC 9865: Cursor-Based Pagination of SCIM Resources". https://datatracker.ietf.org/doc/rfc9865/ (accessed 2026-11-17)
[^s5]: IETF, "RFC 9967: SCIM Profile for Security Event Tokens (SETs)". https://www.rfc-editor.org/rfc/rfc9967 (accessed 2026-11-17)
[^s6]: Trailhead, "Provision Users and Groups with SCIM". https://trailhead.salesforce.com/content/learn/modules/slack-apis-for-automating-and-managing-your-org/provision-users-and-groups-with-scim (accessed 2026-11-17)
