---
id: kt:just-in-time-provisioning
type: Feature
title: Just-in-Time User Provisioning
aliases: [JIT provisioning, SAML JIT, just-in-time provisioning for SAML, SAML JIT handler, Auth.SamlJitHandler]
domain: identity
summary: >-
  A SAML single sign-on option that creates or updates a Salesforce user (and, for Experience Cloud, the related
  contact and account) at login from attributes in the identity provider's assertion, using either standard field
  mapping or a custom Apex SamlJitHandler.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:single-sign-on-saml, kt:openid-connect-authentication-providers, kt:experience-cloud-identity, kt:profiles, kt:role-hierarchy]
relations:
  - {predicate: dependsOn, object: kt:single-sign-on-saml}
  - {predicate: integratesWith, object: kt:apex}
sources:
  - id: s1
    title: "Just-in-Time Provisioning Requirements"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.sso_jit_requirements.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Just-in-Time SAML Assertion Fields for Portals"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.sso_jit_portal_requirements.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Edit the SAML JIT Handler"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.sso_jit_edit_jit_handler.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "SAML Just-in-Time Provisioning Errors"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.sso_jit_errors.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s5
    title: "SamlJitHandler Interface (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_interface_Auth_SamlJitHandler.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s6
    title: "Just-in-Time User Provisioning in Summer '11"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2011/05/just-in-time-user-provisioning-in-summer-11
    type: official-blog
    accessed: 2026-11-08
created: 2026-11-08
---

# Just-in-Time User Provisioning

Just-in-time (JIT) provisioning lets an external identity provider (IdP) create Salesforce users on the fly. During SAML single sign-on the IdP places user data in the Attributes statement of its assertion, and Salesforce uses those values to create the user at login, or to update an existing one, instead of requiring an admin to set the account up in advance.[^s1] The feature arrived in the Summer '11 release, where Salesforce pitched it as a lightweight on-ramp for account creation: lighter than manual onboarding (painful after a merger or acquisition) and cheaper than a full identity-management suite.[^s6]

## How it works

JIT is configured on a SAML Single Sign-On setting where Salesforce is the service provider, and offers two provisioning types. **Standard JIT** maps assertion attributes directly onto a new User record with no code. **Custom JIT** generates an Apex handler class that admins edit to add custom logic.[^s3][^s1]

For standard JIT every User attribute is prefixed `User.` (for example `User.Username`). The required fields are `Email`, `LastName`, `ProfileId` and `Username` (insert only). A long list of optional fields is accepted, including `FirstName`, `FederationIdentifier`, `Role`, `TimeZoneSidKey`, `LocaleSidKey`, `Manager` and `Department`. Because profile IDs differ between orgs, Salesforce suggests sending the profile *name* in `ProfileId`. An optional `ProvisionVersion` attribute defaults to 1.0. Custom User fields in the assertion must be text fields.[^s1]

The custom handler implements `Auth.SamlJitHandler`, named in the **SAML JIT Handler** field of the SSO setting, and runs as a user with Manage Users. `createUser` returns a User for the federation ID, either a new unsaved record or an existing one. `updateUser` runs when a user who has logged in through SAML before returns, or when the Existing User Linking URL is used. Both receive the SAML provider ID, optional Experience Cloud site and portal IDs, the federation ID, a case-sensitive attribute map and the base64 assertion. When the assertion is encrypted, the decrypted copy is available under the `Sfdc.SamlAssertion` key.[^s5] The generated class is where teams add custom-field mapping, fuzzy profile or role matching, contact lookup by email, account lookup by account number, and site provisioning.[^s3]

## External users: contacts and accounts

For portal and site users the assertion also carries `Account.`- and `Contact.`-prefixed fields. A federation ID is required: a match updates the user (an inactive user stays inactive unless `User.IsActive` is true), and no match creates one. Accounts are matched on `Account.AccountNumber` and contacts on `Contact.Email`. More than one match is an error, one match is updated and none creates a record. `Account.Owner` is required, and that owner's profile needs field-level visibility on AccountNumber. Portal users use `User.PortalRole` (Worker) and leave `User.Role` null. Customer and partner portals have been unavailable to new orgs since Summer '13, and Salesforce points those designs to JIT with Experience Cloud instead.[^s2] The Apex interface creates no Account or Contact records itself, so a custom handler has to manage them.[^s5]

## Limits and gotchas

- **Username is insert-only**, and neither Username nor FederationIdentifier can be changed through the SOAP or REST API. An assertion that tries to rename a user fails with `USER_NAME_CHANGE_NOT_ALLOWED`.[^s1][^s4]
- **Failures surface in the URL** as an error code, a description and details, or at the custom error URL if one is set. Common codes cover a missing or mismatched federation ID, a reached license limit (`LICENSE_LIMIT_EXCEEDED`), a role name that maps to more than one role, an invalid handler class and Apex execution errors.[^s4]
- **Mixed DML**: when one assertion carries User attributes alongside Contact or Account attributes, the generated handler usually can't update the latter, because certain User fields can't share a DML operation with them.[^s3]
- **Signatures**: one signature on either the response or the assertion is enough; if both are present, both are validated. Use the SAML Assertion Validator and SAML login history to troubleshoot.[^s3]
- Viewing the settings needs View Setup and Configuration; editing needs Customize Application and Modify All Data.[^s3]

## Connections

JIT is part of **Salesforce Identity** and **depends on SAML single sign-on**: it rides on the SSO setting and the federation ID that SAML uses to match users.[^s1][^s5] Its counterpart for OIDC federation is the Apex registration handler described under **OpenID Connect authentication providers**. For external users it ties into **Experience Cloud identity**, the recommended home for JIT since portals closed to new orgs.[^s2] Assertions assign **profiles** and roles in the **role hierarchy** by name or ID.[^s1][^s4] Custom provisioning **integrates with Apex** through `Auth.SamlJitHandler`.[^s5]

## Sources

[^s1]: Salesforce Help, "Just-in-Time Provisioning Requirements". https://help.salesforce.com/s/articleView?id=xcloud.sso_jit_requirements.htm&language=en_US&type=5 (accessed 2026-11-08)
[^s2]: Salesforce Help, "Just-in-Time SAML Assertion Fields for Portals". https://help.salesforce.com/s/articleView?id=xcloud.sso_jit_portal_requirements.htm&language=en_US&type=5 (accessed 2026-11-08)
[^s3]: Salesforce Help, "Edit the SAML JIT Handler". https://help.salesforce.com/s/articleView?id=xcloud.sso_jit_edit_jit_handler.htm&language=en_US&type=5 (accessed 2026-11-08)
[^s4]: Salesforce Help, "SAML Just-in-Time Provisioning Errors". https://help.salesforce.com/s/articleView?id=xcloud.sso_jit_errors.htm&language=en_US&type=5 (accessed 2026-11-08)
[^s5]: Salesforce Developers, "SamlJitHandler Interface", Apex Reference Guide. https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_interface_Auth_SamlJitHandler.htm (accessed 2026-11-08)
[^s6]: Salesforce Developers Blog, "Just-in-Time User Provisioning in Summer '11" (2011). https://developer.salesforce.com/blogs/2011/05/just-in-time-user-provisioning-in-summer-11 (accessed 2026-11-08)
