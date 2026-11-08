---
id: kt:classic-encryption
type: SecurityControl
title: Classic Encryption
aliases: [Classic Encryption for Custom Fields, classic encrypted custom fields, Text (Encrypted) field, encrypted text field, EncryptedString field]
domain: security-and-sharing
summary: >-
  Salesforce's original, no-extra-cost field encryption: a dedicated Text (Encrypted) custom field type, limited to
  175 characters and encrypted with 128-bit AES keys, whose values are masked for users who lack the View Encrypted
  Data permission.
release: "Winter '27"
status: current
broader: [kt:salesforce-sharing-model]
related: [kt:salesforce-shield, kt:field-level-security, kt:permission-sets, kt:security-compliance-frameworks]
relations:
  - {predicate: contrastsWith, object: kt:shield-platform-encryption}
  - {predicate: alternativeTo, object: kt:shield-platform-encryption}
  - {predicate: mitigates, object: kt:data-breach-risk}
  - {predicate: queriedWith, object: kt:soql}
sources:
  - id: s1
    title: "Custom Field Types (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_types.htm&type=5
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Strengthen Your Data's Security with Shield Platform Encryption (Salesforce Help, PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/setup_security_platform_encryption.pdf
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "What's the Difference Between Classic Encrypted Custom Fields and Platform Encryption? (Security Implementation Guide, Summer '15)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.196.0.securityImplGuide.meta/securityImplGuide/security_pe_comparison_table.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "Get Started with Shield Platform Encryption (Trailhead, Shield Platform Encryption for Admins)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/spe_admins/spe_admins_get_started
    type: official-learning
    accessed: 2026-11-08
  - id: s5
    title: "Schema.DisplayType Enum (Apex Reference Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_enum_Schema_DisplayType.htm
    type: official-docs
    accessed: 2026-11-08
created: 2026-11-08
---

# Classic Encryption

Classic Encryption is the field-encryption option Salesforce includes with every org at no additional cost. Instead of
encrypting existing fields, it provides a separate custom field type, **Text (Encrypted)**, that stores letters,
numbers or symbols in encrypted form, with a maximum length of 175 characters.[^s1] Salesforce's current encryption
documentation describes it as included in the base user license and positions Shield Platform Encryption as the paid
capability built on top of these classic options.[^s2] It remains available in Winter '27, but it is a narrow tool:
it protects a handful of short, sensitive values (an ID number, a card fragment, a secret answer), not a data model.

## How it works

Values in a Text (Encrypted) field are encrypted with the Advanced Encryption Standard using 128-bit master keys.[^s1]
The current comparison table specifies the mode as 128-bit AES-CBC, against 256-bit AES for Shield's database
encryption and 256-bit AES-GCM for its field-level encryption.[^s2] Trailhead likewise summarises Classic Encryption
as 128-bit protection for certain sensitive fields, while Shield offers 256-bit strength across much more of the
database.[^s4]

Key management is minimal: admins can archive, delete and import the master encryption key, but master key management
has to be enabled by contacting Salesforce.[^s1] There is no HSM-based key derivation and no dedicated Manage
Encryption Keys permission; those belong to Platform Encryption.[^s3]

Reading the plaintext is gated by a user permission. Salesforce's original comparison of the two features lists the
View Encrypted Data permission as required to see encrypted values, with masking and configurable mask types and
characters as Classic-specific options; users without the permission see a masked value.[^s3] In Apex describe
results the field surfaces as the `ENCRYPTEDSTRING` value of `Schema.DisplayType`, so dynamic code can detect it.[^s5]

## Limits and gotchas

- **175 characters, text only.** The field type caps length at 175 characters, and only this one dedicated type can be
  encrypted; standard fields, other custom field types, files and attachments cannot.[^s1][^s3]
- **No retrofitting.** You cannot switch on encryption for an existing field; you create a new Text (Encrypted) field
  and migrate the data. Encrypting existing custom fields of supported types is a Platform Encryption feature.[^s3]
- **Not on external objects.** The Text (Encrypted) type isn't available for external objects.[^s1]
- **Reduced usability in automation and search.** Salesforce's comparison marks classic encrypted fields as unavailable
  in workflow rule and approval process criteria and in UI search, partial search and lookups, although API access is
  supported.[^s3]
- **Doesn't mix with Shield by design.** Turning on Platform Encryption leaves fields already encrypted with Classic
  Encryption unchanged.[^s2] For orgs that do have Shield, Salesforce recommends creating encrypted text fields from
  the standard Text type and encrypting them with Platform Encryption rather than using Text (Encrypted).[^s1]

## When to use it (and when not)

Use Classic Encryption when an org without a Shield licence needs to protect a few short values from casual view, and
the masking plus a permission check is the real requirement. The original comparison credits it with PCI-DSS Level 1
compliance support and with masking options Platform Encryption does not offer.[^s3] Choose Shield Platform Encryption
when you need to encrypt standard fields, long text, files or the search index, rotate tenant secrets, bring your own
key, or keep encrypted fields usable in automation and search.[^s3][^s4] Neither replaces access control: who can see
a field in the first place is still a matter of field-level security and permission sets.

## Connections

Classic Encryption **contrasts with** and is the no-cost **alternative to** `kt:shield-platform-encryption`, which
Salesforce documents side by side with it and which leaves classic-encrypted fields untouched when enabled.[^s2]
It is a building block beneath `kt:salesforce-shield`, whose Platform Encryption extends these classic options.[^s2]
Its unmasked display depends on the View Encrypted Data permission, granted through `kt:permission-sets`, and sits
alongside `kt:field-level-security` within the `kt:salesforce-sharing-model`.[^s3] It **mitigates**
`kt:data-breach-risk` for a narrow set of values, supports compliance work tracked under
`kt:security-compliance-frameworks`, and its values remain reachable through the API and `kt:soql` for permitted
users.[^s3][^s5]

## Sources

[^s1]: Salesforce, "Custom Field Types" (Salesforce Help). https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_types.htm&type=5 (accessed 2026-11-08)
[^s2]: Salesforce, "Strengthen Your Data's Security with Shield Platform Encryption" (PDF). https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/setup_security_platform_encryption.pdf (accessed 2026-11-08)
[^s3]: Salesforce, "What's the Difference Between Classic Encrypted Custom Fields and Platform Encryption?" (Security Implementation Guide, Summer '15). https://developer.salesforce.com/docs/atlas.en-us.196.0.securityImplGuide.meta/securityImplGuide/security_pe_comparison_table.htm (accessed 2026-11-08)
[^s4]: Salesforce Trailhead, "Get Started with Shield Platform Encryption". https://trailhead.salesforce.com/content/learn/modules/spe_admins/spe_admins_get_started (accessed 2026-11-08)
[^s5]: Salesforce, "Schema.DisplayType Enum" (Apex Reference Guide). https://developer.salesforce.com/docs/atlas.en-us.264.0.apexref.meta/apexref/apex_enum_Schema_DisplayType.htm (accessed 2026-11-08)
