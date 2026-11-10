---
id: kt:salesforce-scim
type: API
title: Salesforce SCIM API
aliases: [Salesforce SCIM, SCIM user provisioning, SCIM provisioning for Salesforce, Salesforce SCIM 2.0 endpoints]
domain: identity
summary: >-
  Salesforce's implementation of the SCIM 2.0 standard: a set of REST endpoints under /services/scim/v2 that let an
  identity provider or provisioning tool create, read, update and deactivate Salesforce users and manage their
  profiles, permission sets, roles and public group memberships.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:identity-connect, kt:profiles, kt:permission-sets, kt:role-hierarchy, kt:rest-api]
relations:
  - {predicate: implements, object: kt:scim}
  - {predicate: dependsOn, object: kt:oauth-2-0}
  - {predicate: dependsOn, object: kt:my-domain}
  - {predicate: alternativeTo, object: kt:just-in-time-provisioning}
sources:
  - id: s1
    title: "Manage Salesforce User Identities with SCIM"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.identity_scim_overview.htm&type=5
    type: official-docs
    accessed: 2026-11-10
  - id: s2
    title: "Understand the SCIM Implementation"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.identity_scim_implementation.htm&type=5
    type: official-docs
    accessed: 2026-11-10
  - id: s3
    title: "SCIM and REST API Reference Sheet"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.identity_scim_rest_api.htm&type=5
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "RFC 7644: System for Cross-domain Identity Management: Protocol"
    publisher: IETF / RFC Editor
    url: https://rfc-editor.org/rfc/rfc7644
    type: standards-body
    accessed: 2026-11-10
  - id: s5
    title: "Tutorial: Configure Salesforce for automatic user provisioning"
    publisher: Microsoft Learn
    url: https://learn.microsoft.com/en-us/entra/identity/saas-apps/salesforce-provisioning-tutorial
    type: partner
    accessed: 2026-11-10
created: 2026-11-10
---

# Salesforce SCIM API

The **Salesforce SCIM API** is Salesforce's implementation of the System for Cross-domain Identity Management (SCIM) standard. It exposes REST endpoints that let an external system provision and manage Salesforce user identities: create users, read them, update their attributes and access, and disable them.[^s1] Salesforce builds on the SCIM 2.0 specification and extends it with Salesforce-specific user properties, and the feature is available in all editions in both Lightning Experience and Salesforce Classic.[^s1]

SCIM itself is an IETF standard. RFC 7644, published in September 2015 as a Proposed Standard, defines an HTTP protocol with JSON payloads for managing identity resources such as users and groups across domains, for example from an enterprise directory to a cloud service.[^s4] It specifies GET, POST, PUT, PATCH and DELETE semantics, standard endpoints such as `/Users`, `/Groups`, `/Bulk`, `/ServiceProviderConfig`, `/Schemas` and `/ResourceTypes`, plus filter, paging and attribute-selection parameters. Authentication is left to standard HTTP schemes, with OAuth 2.0 bearer tokens over TLS among the options.[^s4]

## How it works

All endpoints live under `https://<MyDomainName>.my.salesforce.com/services/scim/v2/`, and every request must carry an OAuth 2.0 access token.[^s3][^s1] The resources map onto Salesforce's access model:[^s2][^s3]

- **Users** (`/Users`): POST creates a user, GET reads one, PATCH updates one.[^s3]
- **Entitlements** (`/Entitlements`): Salesforce exposes profiles and permission sets as SCIM entitlements, each with a type and member list.[^s2]
- **Roles** (`/Roles`): read-only views of user roles and their members, which drive record sharing.[^s2]
- **Groups** (`/Groups`): public groups, readable with GET and with membership changed through PATCH.[^s3]
- **Discovery** (`/ServiceProviderConfigs`, `/Schemas`, `/ResourceTypes`): describe the capabilities, attribute definitions and the four resource types.[^s2]

User fields map to SCIM attributes. For example, `Username` becomes `userName`, `FederationIdentifier` becomes the external ID, `IsActive` becomes `active`, `UserRoleId` becomes a role, and `ProfileId` and permission sets become entitlements.[^s3] Some User fields have no SCIM equivalent, such as `CompanyName` and the marketing, offline and call-center auto-login user permissions.[^s3]

Deprovisioning deactivates rather than deletes. Either a PATCH or a DELETE on `/Users/<id>` sets the user inactive, so the person can't log in. The record stays queryable and can be reactivated later.[^s3][^s1]

## Limits and gotchas

The service provider configuration advertises support for PATCH, filtering and password changes. It does not support bulk operations, sorting or ETags, so the SCIM `/Bulk` endpoint and `sortBy` parameter from the RFC aren't available.[^s2][^s4] Filtered and list responses return at most 200 results. Querying all entitlements is capped at 200 records, and you query specific entitlements to see the rest.[^s2][^s3] The help docs show appending `*` to `/Groups` to get past the 200-result cap, without saying whether this works on other endpoints.[^s2]

Filter syntax has quirks. Attribute names and operators are case-sensitive, and `AND` doesn't take precedence over `OR`, so mixed clauses need brackets. Entitlements and groups on a user, and members on groups and entitlements, must be filtered on their own.[^s3] Paging follows the stateless SCIM model with `totalResults`, `itemsPerPage` and `startIndex`. Under the RFC, results can shift between page requests if the data changes.[^s2][^s4]

Not every provisioning connector uses these endpoints. Microsoft's Entra ID connector for Salesforce, for instance, calls Salesforce's user provisioning API through a SOAP `login()` with an admin username and security token.[^s5] That route needs SOAP API login enabled, which is off by default for orgs created in Winter '26 and later. It also needs an integration profile with API Enabled, Manage Users and Use Any API Auth. Check which API your identity provider actually calls before you design permissions and monitoring around SCIM.[^s5]

## When to use it (and when not)

Use the SCIM API when an external identity provider or HR-driven provisioning system should own the user lifecycle, including creating users before they first sign in, keeping attributes, profiles, permission sets, roles and public group memberships in sync, and deactivating leavers.[^s1][^s2][^s3] Because the API is a standard, any SCIM 2.0 client can drive it, but test against `/ServiceProviderConfigs` and `/Schemas` first, since unsupported features such as bulk requests and sorting will fail.[^s2][^s4] Login-time provisioning from SAML assertions, also called just-in-time provisioning, is the lighter alternative when users only need creating or updating at sign-in. For User fields the SCIM schema marks as not compatible, use the standard REST API on the User object instead.[^s3]

## Connections

The SCIM API is part of **Salesforce Identity** (`broader`) and `implements` the **SCIM** standard defined in RFC 7644.[^s1][^s4] It `dependsOn` **OAuth 2.0** for request authorization and on **My Domain**, which forms the endpoint's base URL.[^s1][^s3] Its entitlement and role resources manage **profiles**, **permission sets** and the **role hierarchy**, and its attribute mappings mirror the User fields of the **REST API**.[^s2][^s3] It is an `alternativeTo` **just-in-time provisioning** for creating users, and it is related to **Identity Connect**, the older directory-sync product whose `replacedBy` edge already points here.[^s1]

## Sources

[^s1]: Salesforce Help, "Manage Salesforce User Identities with SCIM". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.identity_scim_overview.htm&type=5 (accessed 2026-11-10)
[^s2]: Salesforce Help, "Understand the SCIM Implementation". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.identity_scim_implementation.htm&type=5 (accessed 2026-11-10)
[^s3]: Salesforce Help, "SCIM and REST API Reference Sheet". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.identity_scim_rest_api.htm&type=5 (accessed 2026-11-10)
[^s4]: IETF, "RFC 7644: System for Cross-domain Identity Management: Protocol". https://rfc-editor.org/rfc/rfc7644 (accessed 2026-11-10)
[^s5]: Microsoft Learn, "Tutorial: Configure Salesforce for automatic user provisioning". https://learn.microsoft.com/en-us/entra/identity/saas-apps/salesforce-provisioning-tutorial (accessed 2026-11-10)
