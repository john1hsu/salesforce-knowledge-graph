---
id: kt:salesforce-go
type: Tool
title: Salesforce Go
aliases: [Sales Cloud Go, Salesforce Go feature setup hub]
domain: platform-architecture
summary: >-
  Salesforce's in-Setup hub for discovering, turning on, configuring and monitoring features across clouds, grouped
  into goal-based feature sets with guided setup steps and license-usage data.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:knowledge-base, kt:sales-cloud, kt:service-cloud, kt:agentforce, kt:user-licenses]
relations:
  - {predicate: integratesWith, object: kt:lightning-app-builder}
  - {predicate: enables, object: kt:knowledge-base}
sources:
  - id: s1
    title: "Get Started with Salesforce Go"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sales-cloud-go-quick-look/get-started-with-salesforce-go
    type: official-learning
    accessed: 2026-11-16
  - id: s2
    title: "Explore the Salesforce Go Interface for Admins"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sales-cloud-go-quick-look/streamline-your-sales-setup-with-sales-cloud-go
    type: official-learning
    accessed: 2026-11-16
  - id: s3
    title: "Set Up, Configure, and Monitor Features"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sales-cloud-go-quick-look/discover-set-up-and-configure-a-feature
    type: official-learning
    accessed: 2026-11-16
  - id: s4
    title: "Discover and set up features fast with Sales Cloud Go"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2024/discover-sales-cloud-go
    type: official-blog
    accessed: 2026-11-16
  - id: s5
    title: "Lightning Knowledge Basics: Set Up a Simple Knowledge Base"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning-knowledge-basics/set-up-a-simple-knowledge-base
    type: official-learning
    accessed: 2026-11-16
created: 2026-11-16
---

# Salesforce Go

Salesforce Go is an admin-facing hub inside Setup for finding, reviewing, enabling and trying out Salesforce features from one place. Rather than listing settings by product, it groups features into curated sets tied to business objectives, offers a step-by-step configuration journey with contextual documentation, and reports on license allocation and usage so admins can push adoption.[^s1] Admins open it from the gear menu by choosing Salesforce Go, which lands on its Home page.[^s1]

Its lineage runs through Sales Cloud Go, a Sales Cloud setup hub that the Salesforce Admins blog announced as part of Winter '25. That earlier hub was reached through Sales Setup and bundled feature discovery, fast enablement, documentation and try-and-buy options for Sales Cloud editions from Pro Suite through Einstein 1 Sales.[^s4] The Trailhead module that now teaches Salesforce Go still carries the Sales Cloud Go name in its URL, while its content covers features and clouds across the org.[^s2]

## How it works

The interface is organized into tabs.[^s2]

- **Home** shows Initial Setup, a Get Started With Agentforce section and suggested feature sets for the org.[^s2]
- **Initial Setup** gathers foundational setup cards across clouds, aimed especially at new orgs.[^s2]
- **Feature Sets** are collections of features that solve one business problem, such as keeping deals on track.[^s2]
- **Features** is the full inventory, filterable by setup status, availability and cloud, each with a Set Up link.[^s2]
- **My Clouds** lists clouds the org owns or is licensed for, plus clouds it could purchase through the hub.[^s2]

Each feature page describes what the feature does, links to help, release notes and Trailhead, and lets the admin copy key details to share with stakeholders before committing.[^s3] Clicking Get Started marks the feature In Progress; Turn On, after a disclaimer, activates it and then reveals ordered configuration steps.[^s3] For Einstein Opportunity Scoring those steps are: add components and fields to the Lightning record page (the Manage link opens Lightning App Builder), check and assign the feature's permissions in a popup, and finish model settings in Setup.[^s3]

Go distinguishes three kinds of step. Preenablement steps must be done manually first; a greyed-out Turn On button and a warning icon flag them, with a link to the right Setup page. Automated steps run without input, for example turning on Cadences also turns on Sales Engagement. Configuration steps follow activation.[^s3] Some guided flows go further: for Knowledge, Go turns the feature on, assigns licenses to article authors and creates the first data category group in one sequence.[^s5]

After setup, a feature's page shows licenses available, assigned and active, where active means the user opened the feature in the last 30 days.[^s3]

## Limits and gotchas

- Not every listed feature can be set up; some appear only as purchasable, depending on licensing.[^s2]
- Salesforce Go isn't available in the Trailhead Playground, so practise in a suitable org.[^s2]
- Automated steps change other settings silently (Cadences enables Sales Engagement), so review them before turning a feature on in production.[^s3]
- Some features are one-way: Knowledge can't be disabled once enabled, whether turned on through Go or manually.[^s5]
- The 30-day "active" window means a feature used monthly or quarterly can look unadopted.[^s3]

## When to use it (and when not)

Use Salesforce Go when enabling a feature for the first time, especially in a new org or when an admin is unfamiliar with a product's prerequisites: it sequences the work and links each step to the right page.[^s3][^s2] For repeatable environments, Go is an interactive console, not a deployment mechanism; the same feature can still be enabled through the regular Setup page, as Knowledge can via Knowledge Settings, and configuration that must move between orgs belongs in metadata and a release pipeline.[^s5]

## Connections

Salesforce Go is a Setup tool of the `kt:salesforce-platform`, its broader node.[^s1] It **integrates with** `kt:lightning-app-builder`, which its configuration steps open to place a feature's components on record pages.[^s3] It **enables** `kt:knowledge-base` setup in a single guided flow.[^s5] It grew out of a `kt:sales-cloud` setup hub and now also covers products such as `kt:service-cloud` features like Knowledge.[^s4][^s5] Its Home page includes a getting-started path for `kt:agentforce`, and its adoption view reports on `kt:user-licenses` assigned and actively used.[^s2][^s3]

## Sources

[^s1]: Trailhead, "Get Started with Salesforce Go". https://trailhead.salesforce.com/content/learn/modules/sales-cloud-go-quick-look/get-started-with-salesforce-go (accessed 2026-11-16)
[^s2]: Trailhead, "Explore the Salesforce Go Interface for Admins". https://trailhead.salesforce.com/content/learn/modules/sales-cloud-go-quick-look/streamline-your-sales-setup-with-sales-cloud-go (accessed 2026-11-16)
[^s3]: Trailhead, "Set Up, Configure, and Monitor Features". https://trailhead.salesforce.com/content/learn/modules/sales-cloud-go-quick-look/discover-set-up-and-configure-a-feature (accessed 2026-11-16)
[^s4]: Salesforce Admins, "Discover and set up features fast with Sales Cloud Go". https://admin.salesforce.com/blog/2024/discover-sales-cloud-go (accessed 2026-11-16)
[^s5]: Trailhead, "Lightning Knowledge Basics: Set Up a Simple Knowledge Base". https://trailhead.salesforce.com/content/learn/modules/lightning-knowledge-basics/set-up-a-simple-knowledge-base (accessed 2026-11-16)
