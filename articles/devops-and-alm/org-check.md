---
id: kt:org-check
type: Tool
title: Org Check
aliases: [Org Check by Salesforce Labs, OrgCheck, "@orgcheck/sfdx-plugin"]
domain: devops-and-alm
summary: >-
  A free, open-source Salesforce Labs app (and sf CLI plugin) that reads an org's configuration metadata through
  standard APIs and scores each component for anti-patterns, helping admins, developers and architects find and
  prioritize technical debt.
release: "Winter '27"
status: current
broader: [kt:application-lifecycle-management]
related: [kt:technical-debt-in-salesforce, kt:code-analyzer, kt:salesforce-optimizer, kt:appexchange-security-review]
relations:
  - {predicate: queriedWith, object: kt:tooling-api}
  - {predicate: queriedWith, object: kt:metadata-api}
  - {predicate: governedBy, object: kt:api-request-limits}
  - {predicate: integratesWith, object: kt:salesforce-cli}
sources:
  - id: s1
    title: "Org Check — FAQ"
    publisher: Salesforce Labs (Org Check project)
    url: https://salesforcelabs.github.io/OrgCheck/faq/
    type: community
    accessed: 2026-11-11
  - id: s2
    title: "Org Check — Security Questions"
    publisher: Salesforce Labs (Org Check project)
    url: https://salesforcelabs.github.io/OrgCheck/security/
    type: community
    accessed: 2026-11-11
  - id: s3
    title: "Org Check — Queries"
    publisher: Salesforce Labs (Org Check project)
    url: https://salesforcelabs.github.io/OrgCheck/queries/
    type: community
    accessed: 2026-11-11
  - id: s4
    title: "SalesforceLabs/OrgCheck (GitHub repository)"
    publisher: Salesforce Labs
    url: https://github.com/SalesforceLabs/OrgCheck
    type: community
    accessed: 2026-11-11
  - id: s5
    title: "Optimizer Is Sunsetting: Learn How To Use Org Check"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2025/optimizer-is-sunsetting-learn-how-to-use-org-check-kate-clicks-through-it
    type: official-blog
    accessed: 2026-11-11
  - id: s6
    title: "Salesforce Optimizer App Retirement: Optimization without Salesforce Optimizer"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005167013&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-11
  - id: s7
    title: "Org Check by Salesforce Labs (Trailblazer Community group)"
    publisher: Trailblazer Community
    url: https://trailhead.salesforce.com/trailblazer-community/groups/0F94V0000002E6cSAE?tab=discussion
    type: community
    accessed: 2026-11-11
created: 2026-11-11
---

# Org Check

**Org Check** is a free, open-source tool for analyzing a Salesforce org and the technical debt in it. It comes in two forms: a Salesforce app with a browser UI, installed from AppExchange, and an sf CLI plugin (`@orgcheck/sfdx-plugin`) for scripted and multi-org scans.[^s4] The code lives in the public `SalesforceLabs/OrgCheck` repository under the MIT license.[^s4][^s2] Salesforce's Admins blog calls it a free Salesforce Labs product and suggests it in place of Salesforce Optimizer for keeping metadata manageable.[^s5]

Org Check is **not a Salesforce product**. Salesforce has not officially tested or documented it, Salesforce Support does not cover it, and help comes through GitHub issues and the Trailblazer Community group.[^s1][^s2][^s7] Salesforce Labs apps carry no warranty.[^s2]

## How it works

The app runs in the user's browser and connects only to the org it is installed in. It uses a bundled copy of the JSForce library hosted in the org, so there are no external calls, and no custom object is created to store results.[^s2] It reads **configuration metadata only**, not records such as Accounts or Opportunities. That metadata can be cached in the browser, and Excel exports are generated locally.[^s2] Calls run under the current user's session through REST, Tooling, Metadata, Bulk v2, Limits and Dependency APIs.[^s2]

The published query list shows Tooling API SOQL on code and setup objects (ApexClass, ApexTrigger, FlowDefinition, LightningComponentBundle, CustomField, ValidationRule and others), composite batches of `MetadataComponentDependency` queries, and Metadata API `readMetadata` for SharingRules and ProfilePasswordPolicy.[^s3] It also covers security setup such as Profile, PermissionSet, PermissionSetAssignment, UserRole and LoginHistory.[^s3] Flows are checked with the bundled Lightning Flow Scanner library, which also runs in the browser.[^s2]

Each analyzed item gets a **score**. A blank or zero score is good, and the score goes up by one for every anti-pattern found, so a score of 4 means four issues to review. The score helps rank work but does not replace human judgment.[^s1]

## Installing and running it

Find "Org Check" on AppExchange. Use **Get It Now** for production or **Try It** for a sandbox, and install for admins only. No extra infrastructure or license is required, and it can go into any org, including sandboxes and Developer Edition.[^s1] After installing, assign the bundled **Org Check Users** permission set.[^s1] The running user also needs the ModifyAllData, AuthorApex, ApiEnabled and InstallPackaging permissions, or the app stops with a warning.[^s2] The app reads metadata but never changes metadata or data.[^s2]

The CLI plugin has commands such as `sf check apex-classes`, `sf check hardcoded-urls` and `sf check global-view`, each taking `--target-org`. It writes CSV, JSON or XLSX files and runs locally under the authenticated CLI session.[^s1][^s2] In production orgs it may need `--accept-the-terms`.[^s1]

## Limits and gotchas

- **API consumption**: Org Check watches the org's daily API request usage. Below 70% calls run normally, from 70% to 90% they run with a warning, and at 90% or more they are blocked until the rolling 24-hour count drops.[^s2]
- **Run it in a sandbox**: the project recommends a non-critical sandbox over production, and reuses cached results when they are fresh enough to save API calls.[^s2]
- **API Access Control**: orgs that allowlist connected apps need a permission set granting "Use any API Client" for the app to work. The FAQ notes this permission is being deprecated and a workaround is in progress.[^s1]
- **Identity verification**: an `INSUFFICIENT_ACCESS: Requires Extra Verification` error points to the org's identity verification settings for sensitive permissions.[^s1]
- **One install per org**: the AppExchange app and the older standalone unlocked package share a namespace, so only one can be installed. The AppExchange app is now the preferred route.[^s1]

The package passed Salesforce's ISV security review as a Salesforce Labs app in September 2022 and again in May 2026 after a major refactor. Its code-scan reports are published.[^s2]

## When to use it

Salesforce retired **Salesforce Optimizer** as of Winter '26.[^s6] Salesforce Help now points admins to built-in checks instead: Security Health Check, sharing settings, Release Updates, Storage Usage and SOQL queries for old API versions.[^s6] Org Check gathers similar checks into one scored inventory spanning Apex and Visualforce, flows and workflow rules, hard-coded URLs, profiles and permission sets, and metadata dependencies.[^s3][^s1] It complements, not replaces, static analysis in the delivery pipeline. Org Check looks at what is deployed in an org, while source-based tools scan code before it ships.

## Connections

Org Check sits **under** `kt:application-lifecycle-management` as an org-health tool for cleanup and refactoring work.[^s4] It is **related** to `kt:technical-debt-in-salesforce`, which it makes visible as scored inventory, and to `kt:code-analyzer`, the source-level scanner whose reports Org Check publishes from its own security reviews.[^s2] It is related to the retired `kt:salesforce-optimizer`, which the Admins blog presents it as an alternative to,[^s5][^s6] and to `kt:appexchange-security-review`, which its managed package has passed twice.[^s2] It is **queried with** `kt:tooling-api` and `kt:metadata-api`,[^s3] is **governed by** `kt:api-request-limits` through its usage thresholds,[^s2] and **integrates with** `kt:salesforce-cli` through its sf plugin.[^s1]

## Sources
[^s1]: Salesforce Labs, "Org Check — FAQ". https://salesforcelabs.github.io/OrgCheck/faq/ (accessed 2026-11-11)
[^s2]: Salesforce Labs, "Org Check — Security Questions". https://salesforcelabs.github.io/OrgCheck/security/ (accessed 2026-11-11)
[^s3]: Salesforce Labs, "Org Check — Queries". https://salesforcelabs.github.io/OrgCheck/queries/ (accessed 2026-11-11)
[^s4]: Salesforce Labs, "SalesforceLabs/OrgCheck" (GitHub). https://github.com/SalesforceLabs/OrgCheck (accessed 2026-11-11)
[^s5]: Salesforce Admins Blog, "Optimizer Is Sunsetting: Learn How To Use Org Check". https://admin.salesforce.com/blog/2025/optimizer-is-sunsetting-learn-how-to-use-org-check-kate-clicks-through-it (accessed 2026-11-11)
[^s6]: Salesforce Help, "Salesforce Optimizer App Retirement: Optimization without Salesforce Optimizer". https://help.salesforce.com/s/articleView?id=005167013&language=en_US&type=1 (accessed 2026-11-11)
[^s7]: Trailblazer Community, "Org Check by Salesforce Labs". https://trailhead.salesforce.com/trailblazer-community/groups/0F94V0000002E6cSAE?tab=discussion (accessed 2026-11-11)
