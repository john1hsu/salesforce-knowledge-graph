---
id: kt:shield-platform-encryption
type: SecurityControl
title: Shield Platform Encryption
aliases: [Platform Encryption, Salesforce Platform Encryption, SPE, encryption at rest in Salesforce]
domain: security-and-sharing
summary: >-
  The Salesforce Shield capability that encrypts data at rest (standard and custom fields, files and attachments,
  search indexes and other stored data) with 256-bit AES keys derived from a Salesforce primary secret and an
  org-specific tenant secret, with options for customer-supplied or externally managed key material.
release: "Winter '27"
status: current
broader: [kt:salesforce-shield]
related: [kt:field-audit-trail, kt:event-monitoring, kt:security-compliance-frameworks, kt:data-cloud, kt:sandbox-types]
relations:
  - {predicate: requiresLicense, object: kt:salesforce-shield}
  - {predicate: contrastsWith, object: kt:classic-encryption}
  - {predicate: integratesWith, object: kt:change-data-capture}
  - {predicate: integratesWith, object: kt:platform-events}
  - {predicate: mitigates, object: kt:data-breach-risk}
sources:
  - id: s1
    title: "Get to Know Shield Platform Encryption (Trailhead, Shield Platform Encryption: Quick Look)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/shield-platform-encryption-quick-look2/get-to-know-shield-platform-encryption2
    type: official-learning
    accessed: 2026-11-06
  - id: s2
    title: "Set Up and Manage Shield Platform Encryption (Trailhead, Shield Platform Encryption for Admins)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/en/modules/spe_admins/units/spe_admins_set_up
    type: official-learning
    accessed: 2026-11-06
  - id: s3
    title: "Shield Platform Encryption (Salesforce Help, PDF)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/setup_security_platform_encryption.pdf
    type: official-docs
    accessed: 2026-11-06
  - id: s4
    title: "Salesforce Shield: What's Included, How It Works, and How to Implement"
    publisher: Salesforce
    url: https://www.salesforce.com/platform/shield/guide/
    type: official-blog
    accessed: 2026-11-06
created: 2026-11-06
---

# Shield Platform Encryption

Shield Platform Encryption (often just "Platform Encryption") protects Salesforce data **at rest**: data stored on servers, in databases, in search index files and in file systems.[^s1] It is one of the four products in Salesforce Shield, the premium security and compliance suite that also contains Field Audit Trail, Event Monitoring and Data Detect.[^s4] It is a defence against unauthorised access to stored data, not an access-control mechanism: field-level security, object permissions and record sharing still decide what an authenticated user sees, and encrypted values look the same as plaintext to a user who has access.[^s3][^s2]

## How it works

Data is encrypted with 256-bit AES on Salesforce's application servers.[^s3] By default the data encryption key is derived with PBKDF2 (HMAC-SHA-256) from two inputs: a **primary secret** that Salesforce generates with each of its three yearly releases, and an org-specific **tenant secret** that an administrator generates and controls.[^s3][^s1] Derived keys are held only in memory, never written to disk, and are not shared across orgs.[^s3] Tenant secrets come in types: Fields and Files (Probabilistic), Field (Deterministic), Search Index, Analytics and Event Bus.[^s3]

Coverage extends beyond fields. The help documentation lists files and attachments (bodies encrypted on upload), search indexes, CRM Analytics datasets, Chatter data, Change Data Capture and platform event messages, and Data Cloud through a customer-managed root key.[^s3] Supported custom field types are Email, Phone, Text, Text Area (Long or Rich), URL, Date and Date/Time.[^s3]

Field encryption is **probabilistic** by default. **Deterministic** encryption, chosen when filtering matters, lets reports and list views filter on the encrypted field and can be set per field as case-sensitive or exact-match case-insensitive.[^s3][^s1] It is required for custom fields marked Unique or External ID, and is unavailable for long text fields.[^s3]

Key management options run from Salesforce-generated tenant secrets, through Bring Your Own Key (uploading your own tenant secret or final key), to an External Key Management Service and the Cache-Only Key Service, which fetch key material on demand from a service the customer controls.[^s3][^s1]

## Setup and operations

Administrators need a permission set with Customize Application and Manage Encryption Keys, generate a tenant secret under Key Management, then select standard and custom fields and turn on file encryption in the encryption policy; a validation process emails about org settings that block encryption.[^s2] Encryption applies only to data created or updated after it is enabled; existing values are brought into line via the Encryption Statistics and Data Sync pages or a background encryption process.[^s2][^s3] Rotating a secret archives the old one, which can still decrypt but no longer encrypts; each secret type is capped at 50 active and archived secrets, and production orgs can generate a new Probabilistic secret once every 24 hours.[^s2][^s3] Salesforce recommends exporting tenant secrets, testing in a sandbox, phasing rollouts for orgs with 80 or more encrypted fields, and tracking key activity in the Setup Audit Trail.[^s2][^s1]

## Limits and gotchas

- Formula fields that reference encrypted data are supported only in Salesforce Classic, and a field referenced by more than 200 formula fields cannot be encrypted.[^s3]
- Duplicate-management matching rules need deterministic encryption; standard matching rules deactivate automatically when a referenced field is encrypted.[^s3]
- Encrypting a Name field turns on enhanced lookups irreversibly, and an encrypted field's type cannot be changed afterwards.[^s3]
- Encryption does not consume data storage, but encrypt/decrypt work counts toward per-transaction Apex limits.[^s3]
- A sandbox refresh copies tenant secrets, so rotating them after refresh is recommended.[^s3]
- With cache-only keys, callouts time out after 3 seconds and an unreachable key service can leave data masked as question marks; destroying a key makes its data unreadable.[^s3]
- Encrypting fields can limit some report, filter and list-view behaviour; Salesforce points to the Platform Encryption Analyzer and sandbox testing, and positions database-level encryption as the option that keeps sorting, filtering and SOQL fully working.[^s4][^s1]

## When to use it (and when not)

Use it when regulation or policy demands customer-controlled encryption of sensitive data at rest, and choose deterministic only for fields that must be filtered or matched.[^s1][^s3] Do not use it to hide data from internal users; that is the job of field-level security and sharing.[^s3]

## Connections

It is part of and licensed through `kt:salesforce-shield`, alongside `kt:field-audit-trail` and `kt:event-monitoring`.[^s4] It contrasts with `kt:classic-encryption`, whose existing encrypted fields are left untouched when Platform Encryption is enabled.[^s3] Its Event Bus secrets cover `kt:change-data-capture` and `kt:platform-events` messages, it extends to `kt:data-cloud` through a root key, and it is a common control in `kt:security-compliance-frameworks` programs; `kt:sandbox-types` matter because refreshes copy secrets.[^s3]

## Sources

[^s1]: Salesforce Trailhead, "Get to Know Shield Platform Encryption". https://trailhead.salesforce.com/content/learn/modules/shield-platform-encryption-quick-look2/get-to-know-shield-platform-encryption2 (accessed 2026-11-06)
[^s2]: Salesforce Trailhead, "Set Up and Manage Shield Platform Encryption". https://trailhead.salesforce.com/en/modules/spe_admins/units/spe_admins_set_up (accessed 2026-11-06)
[^s3]: Salesforce, "Shield Platform Encryption" (Salesforce Help PDF). https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/setup_security_platform_encryption.pdf (accessed 2026-11-06)
[^s4]: Salesforce, "Salesforce Shield: What's Included, How It Works, and How to Implement". https://www.salesforce.com/platform/shield/guide/ (accessed 2026-11-06)
