---
id: kt:user-management
type: Feature
title: User Management
aliases: [Salesforce user management, user administration, manage users, user lifecycle management, freeze users, deactivate users]
domain: identity
summary: >-
  The Setup tasks an admin uses to run the lifecycle of Salesforce User records: creating users with a
  license, profile and optional role, resetting passwords and unlocking accounts, freezing logins, and
  deactivating users (who can't be deleted) so their licenses are released.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:profiles, kt:permission-sets, kt:password-policies, kt:just-in-time-provisioning, kt:hierarchical-relationships]
relations:
  - {predicate: dependsOn, object: kt:user-licenses}
  - {predicate: hasPart, object: kt:user-access-policies}
sources:
  - id: s1
    title: "Deactivate Users"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.how_to_deactivate_users.htm&type=5
    type: official-docs
    accessed: 2026-11-14
  - id: s2
    title: "Considerations for Deactivating Users"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.users_deactivate_considerations.htm&type=5
    type: official-docs
    accessed: 2026-11-14
  - id: s3
    title: "Freeze or Unfreeze User Accounts"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.users_freeze.htm&amp=&type=5&amp=&language=en_US
    type: official-docs
    accessed: 2026-11-14
  - id: s4
    title: "Add Users (Lightning Experience Implementation: User Setup and Management)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lex_implementation_user_setup_mgmt/lex_implementation_user_setup_mgmt_adding_users-hoc
    type: official-learning
    accessed: 2026-11-14
  - id: s5
    title: "Control Access to the Org (Data Security)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_org
    type: official-learning
    accessed: 2026-11-14
created: 2026-11-14
---

# User Management

User management is the part of Salesforce administration that governs the lifecycle of internal User records: provisioning a person with a username, license and profile, keeping their login working (password resets, unlocking), and cutting off access when they leave. It sits at the boundary of identity and authorization. The User record is what every login, sharing calculation and record owner points at, so lifecycle mistakes ripple into data access and automation.[^s4][^s5]

## Creating users

Admins work from **Setup → Users**. **New User** creates one user and **Add Multiple Users** creates up to 10 at a time. How many users an org can have depends on its edition and the user licenses it has bought.[^s4] A user needs a username, email, last name, alias, nickname, license and profile. First name and role are optional.[^s4]

- **Username** must be in email format and unique across all Salesforce orgs, not just yours. It defaults to the email address. The email itself can be reused across orgs.[^s4]
- **License first, then profile.** The license chosen limits which profiles can be picked, and the role list fills in only after both are set.[^s4][^s5]
- **One profile, at most one role.** Trailhead recommends the Minimum Access – Salesforce profile, with further access added through permission sets and permission set groups.[^s4]
- **Password setup**: the "Generate password and notify user immediately" option emails login details. The emailed link works only once, and users must change their password on first login.[^s4]

## Keeping access working

Profiles carry login restrictions such as login hours and login IP ranges. A profile-level password policy overrides the org-wide one for that profile's users. Admins can reset passwords for selected users, unlock users locked out after too many failed logins, and expire all passwords at once, except for users with the Password Never Expires permission.[^s5] With the right permission, or when a user has granted login access, an admin can **log in as** that user to troubleshoot.[^s4]

## Freezing vs. deactivating

Salesforce users **can't be deleted**. Deleting them could orphan records and lose business history, so the end of the lifecycle is deactivation: on the user, clear **Active** and save. This needs the Manage Internal Users permission and works on one user at a time. The user stays in the list as inactive, can't log in, and still owns their records until ownership is transferred, for example with Mass Transfer.[^s1][^s5]

Deactivation is blocked when the user is wired into configuration. Examples include a default lead or case owner, the default workflow user, the only recipient of a workflow email alert, a user selected in a custom hierarchy field, or the Customer Portal Administrator. Automated Process and integration users can't be deactivated at all.[^s1][^s2] For those cases you **freeze** the account. That needs Freeze Users or Manage Users, and it blocks login at once while you unpick the dependencies. Freezing does **not** release the license; only deactivation does.[^s3][^s4]

## Limits and gotchas

- Deactivated users stop consuming a license, but billing doesn't change until the license count is updated.[^s2]
- Transfer records first when a user owns more than 10,000 records of one object. Delete shares through the Bulk API first when they have more than 10,000 manually shared accounts.[^s2]
- Manual and team shares are lost at once. Access through users above them in the role hierarchy is removed asynchronously.[^s2]
- Inactive users keep permission set and permission set group assignments until you remove them.[^s2]
- A user in a custom hierarchy field stays blocked even after the field is deleted. The field has to be permanently erased first.[^s2]
- Dashboards owned or run by a deactivated user stop returning expected results. A CRM Analytics dataflow they scheduled is unscheduled.[^s2]
- Approvers must be removed from approval processes, or their duties reassigned.[^s1]

## Connections

User management is the admin face of **Salesforce Identity**: the User records that SSO, OAuth and MFA authenticate are created and retired here.[^s4] It **depends on user licenses**, because the license picks the allowed profiles and deactivation is the only way to free one.[^s4][^s3] **Profiles**, **permission sets** and **password policies** define what each user can do and how they sign in.[^s5] **User access policies** automate permission assignments as users are created or updated. **Just-in-time provisioning** and SCIM are the automated alternatives to manual creation. A user selected in a custom **hierarchical relationship** field is a classic reason a deactivation is blocked and the account must be frozen first.[^s1][^s2]

## Sources

[^s1]: Salesforce Help, "Deactivate Users". https://help.salesforce.com/s/articleView?language=en_US&id=sf.how_to_deactivate_users.htm&type=5 (accessed 2026-11-14)
[^s2]: Salesforce Help, "Considerations for Deactivating Users". https://help.salesforce.com/s/articleView?language=en_US&id=sf.users_deactivate_considerations.htm&type=5 (accessed 2026-11-14)
[^s3]: Salesforce Help, "Freeze or Unfreeze User Accounts". https://help.salesforce.com/s/articleView?id=sf.users_freeze.htm&amp=&type=5&amp=&language=en_US (accessed 2026-11-14)
[^s4]: Trailhead, "Add Users", Lightning Experience Implementation: User Setup and Management. https://trailhead.salesforce.com/content/learn/modules/lex_implementation_user_setup_mgmt/lex_implementation_user_setup_mgmt_adding_users-hoc (accessed 2026-11-14)
[^s5]: Trailhead, "Control Access to the Org", Data Security. https://trailhead.salesforce.com/content/learn/modules/data_security/data_security_org (accessed 2026-11-14)
