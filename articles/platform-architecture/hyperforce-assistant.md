---
id: kt:hyperforce-assistant
type: Tool
title: Hyperforce Assistant
aliases: [Salesforce Hyperforce Assistant, Hyperforce upgrade assistant]
domain: platform-architecture
summary: >-
  An in-app Setup tool that guides admins through preparing a Salesforce org for its upgrade from Salesforce's
  first-party data centers to Hyperforce, combining a learning area, a readiness checklist with automated
  checks, and upgrade details for the org.
release: "Winter '27"
status: current
broader: [kt:hyperforce]
related: [kt:instance-refresh-and-org-migration, kt:sandbox-types, kt:trust-and-status-site, kt:login-ip-ranges-and-trusted-ip-ranges]
relations:
  - {predicate: dependsOn, object: kt:my-domain}
  - {predicate: partOf, object: kt:salesforce-platform}
sources:
  - id: s1
    title: "How to Prepare for a First-Party to Hyperforce Salesforce Core Org Migration (Knowledge Article 000386897)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000386897&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-26
  - id: s2
    title: "Salesforce Hyperforce — General Information, FAQ, Migration Guide, and Security Overview (Knowledge Article 000388902)"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000388902&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "Upgrade to Hyperforce with Confidence Using Hyperforce Assistant"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2023/upgrade-to-hyperforce-with-confidence-using-hyperforce-assistant
    type: official-blog
    accessed: 2026-11-26
  - id: s4
    title: "New Hyperforce Assistant | Learn MOAR Spring '23"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2023/new-hyperforce-assistant-learn-moar-spring-23
    type: official-blog
    accessed: 2026-11-26
created: 2026-11-26
---

# Hyperforce Assistant

**Hyperforce Assistant** is a guided workspace inside Setup for orgs that still run in Salesforce's first-party (1P) data centers and are scheduled to move to Hyperforce. Admins open it by typing "Hyperforce Assistant" in the Setup Quick Find box.[^s1] Salesforce's own migration guidance names running it as one of the pre-migration steps, and the Hyperforce FAQ points customers to it as the in-app guide for the upgrade.[^s1][^s2] Salesforce describes the upgrade as free, and its FAQ states that Hyperforce carries no additional cost.[^s3][^s2]

## How it works

Salesforce designed the assistant around four phases: **learn**, **prepare**, **upgrade** and **manage**. When it was introduced, only the first two were live; the later phases were roadmap items.[^s4]

- **Learn** gathers resources, the key benefits of Hyperforce, and important notices about the move.[^s3]
- **Prepare** is a six-step readiness checklist. Three steps run automatically from a **Verify** button; the other three are manual, with instructions.[^s3]
- **Upgrade** surfaces the org's scheduled upgrade date and the new region, added as a tab in Spring '23.[^s4]
- **Manage** was announced as a later phase that would add automated post-upgrade checks.[^s3]

The three automated Prepare checks are the core of the tool:[^s3]

1. A scan for hard-coded instance references such as `na14.salesforce.com`; Spring '23 extended this to Apex code.[^s3][^s4]
2. A connectivity test from the org's environment to its target Hyperforce instance.[^s3]
3. A check that enhanced domains are turned on, so the org uses stable My Domain hostnames.[^s3]

Each page also offers thumbs-up and thumbs-down feedback to Salesforce.[^s4] The assistant runs in both sandboxes and production, so teams can rehearse fixes in a sandbox first.[^s3]

## Availability and history

According to Salesforce's Spring '23 overview, the assistant first became available with Winter '22 to customers who were eligible to upgrade; ineligible orgs were told to contact their account executive.[^s4] A later Salesforce Admins post describes it as generally available with Summer '23, when the guided Prepare checks matured.[^s3] As of the Winter '27 release, Salesforce's help articles still direct customers to run it before a 1P-to-Hyperforce move.[^s1][^s2]

## Limits and gotchas

- **It doesn't schedule or defer the move.** Salesforce sends a migration notice 30 days ahead and a reminder 15 days before.[^s2] From July 1, 2026, Salesforce no longer defers 1P-to-Hyperforce migrations.[^s1][^s2]
- **Passing the checks is not the whole job.** The help guidance also asks admins to review IP allowlists, remove certificate pinning and avoid large jobs within 72 hours of the window.[^s1]
- **Sandbox timing matters.** Don't request a Full sandbox refresh within two weeks of migration, or start Developer or Developer Pro copies within one week.[^s1]
- **Plan for the window itself.** Production is read-only for roughly three hours, and sandboxes are fully inaccessible because they don't support read-only mode.[^s2][^s1]
- **The Trust site won't show it.** Migration maintenance isn't posted on Trust; notices come through Product and Service notifications.[^s2]
- **Edge cases sit outside its checks.** Own Archive needs its mTLS setting enabled, and iOS mTLS clients need Salesforce Edge, before upgrading.[^s1]

## When to use it

Use the assistant as soon as an org is eligible or receives a migration notice: run Verify in a sandbox, fix what it flags, then repeat in production before the date.[^s3][^s2] Treat it as the starting checklist and pair it with the help article's full preparation steps, especially for integrations, allowlists and refresh schedules.[^s1]

## Connections

The assistant is the preparation tool for **Hyperforce**, Salesforce's public-cloud infrastructure, and a configuration path for an **org migration** between instances.[^s2][^s1] Its enhanced-domains check makes it depend on **My Domain**, which keeps hostnames stable when the instance name changes.[^s3] Refresh-timing rules tie it to **sandbox types**, and allowlist guidance ties it to **login IP ranges and trusted IP ranges**.[^s1] Unlike routine maintenance, migration windows are not posted on the **Trust site**.[^s2] It is part of the wider **Salesforce Platform** Setup tooling.[^s1]

## Sources

[^s1]: Salesforce Help, "How to Prepare for a First-Party to Hyperforce Salesforce Core Org Migration" (Knowledge Article 000386897). https://help.salesforce.com/s/articleView?id=000386897&language=en_US&type=1 (accessed 2026-11-26)
[^s2]: Salesforce Help, "Salesforce Hyperforce — General Information, FAQ, Migration Guide, and Security Overview" (Knowledge Article 000388902). https://help.salesforce.com/s/articleView?id=000388902&language=en_US&type=1 (accessed 2026-11-26)
[^s3]: Salesforce Admins Blog, "Upgrade to Hyperforce with Confidence Using Hyperforce Assistant" (2023). https://admin.salesforce.com/blog/2023/upgrade-to-hyperforce-with-confidence-using-hyperforce-assistant (accessed 2026-11-26)
[^s4]: Salesforce Admins Blog, "New Hyperforce Assistant | Learn MOAR Spring '23" (2023). https://admin.salesforce.com/blog/2023/new-hyperforce-assistant-learn-moar-spring-23 (accessed 2026-11-26)
