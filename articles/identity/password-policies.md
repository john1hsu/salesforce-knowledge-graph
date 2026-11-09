---
id: kt:password-policies
type: SecurityControl
title: Password Policies
aliases: [Salesforce password policies, org-wide password policies, profile password policies, ProfilePasswordPolicy, password complexity requirement, password expiration policy, account lockout policy]
domain: identity
summary: >-
  The Salesforce settings that govern user passwords (expiration, history, minimum length, complexity, lockout
  after failed logins and forgotten-password handling), set org-wide in Setup and optionally overridden per profile.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:multi-factor-authentication, kt:login-ip-ranges-and-trusted-ip-ranges, kt:session-security-levels, kt:single-sign-on-saml]
relations:
  - {predicate: configuredVia, object: kt:profiles}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: mitigates, object: kt:account-takeover}
  - {predicate: contrastsWith, object: kt:nist-digital-identity-guidelines}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "Manage User Passwords"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=security_overview_passwords.htm&language=en_US&type=0
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "View and Edit Password Policies in Profiles"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.users_profiles_password_policies.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-09
  - id: s3
    title: "FAQs for Password Policies in Salesforce Sales and Service"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=001094362&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-09
  - id: s4
    title: "ProfilePasswordPolicy (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta.%20%20/api_meta/meta_profilepasswordpolicy.htm
    type: official-docs
    accessed: 2026-11-09
  - id: s5
    title: "Data Security: Control Access to the Org"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/data_security/units/data_security_org
    type: official-learning
    accessed: 2026-11-09
  - id: s6
    title: "NIST SP 800-63B-4: Authenticators and Verifiers"
    publisher: NIST
    url: https://pages.nist.gov/800-63-4/sp800-63b/authenticators
    type: standards-body
    accessed: 2026-11-09
created: 2026-11-09
---

# Password Policies

**Password policies** are the Salesforce settings that decide what a valid user password looks like and what happens when users get it wrong. Admins with the Manage Password Policies permission set password history, length and complexity, and choose how forgotten passwords are handled; the feature is available in all editions and in both Salesforce Classic and Lightning Experience.[^s1][^s2] Trailhead groups the settings into three jobs: how long a password lives and how complex it must be, how many failed logins trigger a lockout, and how forgotten passwords and locked accounts are dealt with.[^s5]

## How it works

Policies exist at two levels. The org-wide policy lives in Setup under **Password Policies**, and each profile can carry its own policy that overrides the org-wide one for that profile's users; profiles without their own settings fall back to the org-wide values.[^s2][^s5] Editing profile policies needs Manage Profiles and Permission Sets, and in the enhanced profile UI they sit under a dedicated Password Policies section.[^s2]

The settings map one-to-one onto the `ProfilePasswordPolicy` metadata type (API 40.0 and later, stored as `.profilePasswordPolicy` files in a `profilePasswordPolicies` folder), which is a convenient reference for the allowed values:[^s4]

- **Expiration:** 30, 60, 90, 180 or 365 days, or never.[^s4]
- **History:** the number of previous passwords remembered so they can't be reused; a history of zero is only valid when passwords never expire.[^s4]
- **Minimum length:** 5 to 50 characters.[^s4]
- **Complexity:** five levels, from any characters, through letter-plus-number, up to number, upper- and lowercase letter and a special character.[^s4]
- **Lockout:** 3, 5 or 10 invalid attempts (or 0) before lockout, with a lockout period of 15, 30 or 60 minutes (or 0).[^s4]
- **Other switches:** whether the password hint answer may contain the password, whether security answers are obscured while typed, a one-change-per-24-hours minimum lifetime, and keeping forgot-password reset links valid until the user confirms on an interstitial page (API 43.0+).[^s4]

Alongside the policies, admins can reset individual passwords, unlock locked-out users, and expire passwords for every user in an org or Experience Cloud site so all users must set a new one at next login.[^s1][^s5]

## Limits and gotchas

- **Changes aren't always retroactive.** New profile policies reach existing users of that profile only when they next reset their password.[^s2] Shortening expiration, or switching to never expires, takes effect immediately, but lengthening it applies only from the next password change.[^s3]
- **Profile drift.** Once a profile has its own policy, changes to the org-wide policy no longer reach its users.[^s2] In the original profile UI, any profile that was ever edited stops following org-wide policy; Salesforce suggests changing an org setting temporarily and checking whether each profile picked it up.[^s3]
- **Password Never Expires** on a profile or permission set overrides both org and profile expiration, and is the one exemption when all passwords are expired.[^s3][^s5]
- **Stale expiration dates.** A user moved from an expiring profile to a never-expires profile can still be prompted to change their password, because the stored expiration date isn't cleared automatically.[^s3]

## When to use it (and when not)

Treat password policies as a baseline, not the main defence. NIST's SP 800-63B-4 now asks verifiers to require at least 15 characters for single-factor passwords (8 when the password is one factor of MFA), allow at least 64, impose no composition rules, force changes only on evidence of compromise, screen new passwords against a blocklist, and cap consecutive failed attempts at 100.[^s6] Salesforce's options can approximate parts of that, such as a long minimum length, the lowest complexity setting and never-expiring passwords, but there is no blocklist setting among the policy fields, so admins should weigh compliance frameworks that still mandate rotation or complexity against the current NIST guidance.[^s4][^s6] Use a stricter profile policy for high-risk populations, such as admins, rather than tightening the whole org.[^s2]

## Connections

Password policies are a building block of **Salesforce Identity** and are configured partly through **profiles** and deployed as metadata via the **Metadata API**.[^s2][^s4] They pair with **multi-factor authentication**, which NIST treats as the context in which a shorter password is acceptable, and with network controls such as **login IP ranges and trusted IP ranges** and **session security levels**.[^s6][^s5] Lockout and history settings help limit **account takeover** from guessed or reused credentials, while their composition and rotation options are where Salesforce's model diverges from the **NIST digital identity guidelines**.[^s4][^s6] **SAML single sign-on** is the related alternative to Salesforce-managed passwords, and password policy design sits within the scope of the **Identity and Access Management Architect** certification alongside the other org access controls Trailhead covers.[^s5]

## Sources
[^s1]: Salesforce Help, "Manage User Passwords". https://help.salesforce.com/s/articleView?id=security_overview_passwords.htm&language=en_US&type=0 (accessed 2026-11-09)
[^s2]: Salesforce Help, "View and Edit Password Policies in Profiles". https://help.salesforce.com/s/articleView?id=sf.users_profiles_password_policies.htm&language=en_US&type=5 (accessed 2026-11-09)
[^s3]: Salesforce Help, "FAQs for Password Policies in Salesforce Sales and Service". https://help.salesforce.com/s/articleView?id=001094362&language=en_US&type=1 (accessed 2026-11-09)
[^s4]: Salesforce Developers, "ProfilePasswordPolicy". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta.%20%20/api_meta/meta_profilepasswordpolicy.htm (accessed 2026-11-09)
[^s5]: Trailhead, "Data Security: Control Access to the Org". https://trailhead.salesforce.com/modules/data_security/units/data_security_org (accessed 2026-11-09)
[^s6]: NIST, "SP 800-63B-4: Authenticators and Verifiers". https://pages.nist.gov/800-63-4/sp800-63b/authenticators (accessed 2026-11-09)
