---
id: kt:partner-console
type: Tool
title: Partner Console
aliases: [AgentExchange Partner Console, AppExchange Partner Console, Salesforce Partner Console]
domain: devops-and-alm
summary: >-
  The business management site inside the Salesforce Partner Community where ISV partners and consultants connect
  their orgs and packages, register packages with the License Management App, start security reviews, build and
  publish AgentExchange listings, and track listing analytics.
release: "Winter '27"
status: current
broader: [kt:agentexchange, kt:application-lifecycle-management]
related: [kt:agentexchange-go-to-market-app, kt:second-generation-managed-packages, kt:first-generation-managed-packages, kt:trialforce]
relations:
  - {predicate: integratesWith, object: kt:license-management-app}
  - {predicate: hasPart, object: kt:appexchange-security-review}
  - {predicate: dependsOn, object: kt:partner-business-org}
  - {predicate: integratesWith, object: kt:dev-hub}
sources:
  - id: s1
    title: "Access the AppExchange Partner Console (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packageGuide/appexchange_launch_partner_console.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s2
    title: "Explore the AgentExchange Partner Console Features"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/appexchange-partners-publishing/appexchange-partner-console
    type: official-learning
    accessed: 2026-11-25
  - id: s3
    title: "Connect and Select Your Listing Type for AgentExchange"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/appexchange-partners-publishing/appexchange-technologies
    type: official-learning
    accessed: 2026-11-25
  - id: s4
    title: "Get to Know AgentExchange NextGen Publishing"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/appexchange_publishing_quick_look/get-to-know-appexchange-nextgen-publishing
    type: official-learning
    accessed: 2026-11-25
  - id: s5
    title: "The AppExchange Partner Console Guide"
    publisher: Salesforce
    url: https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/partners/readiness/the_appexchange_partner_console_guide.pdf
    type: official-docs
    accessed: 2026-11-25
created: 2026-11-25
---

# Partner Console

The **Partner Console** is the business management site for ISV partners and consultants who list on AgentExchange (formerly AppExchange).[^s1][^s4] From one place a partner creates and publishes listings, connects the orgs and packages behind them, runs the security review, and watches how listings perform.[^s2][^s4] It is not a separate login: a partner signs in to the Salesforce Partner Community and clicks **Publishing**, which opens the console already authenticated.[^s1][^s2] Users need the **Manage Listings** permission to work with listings.[^s1] Salesforce's documentation is mid-rename: Trailhead says "AgentExchange Partner Console" while the ISVforce Guide and the older partner guide still say "AppExchange Partner Console".[^s1][^s2][^s5]

## How it works

The console has three main areas.[^s2]

- **Home** is the landing page. It holds company info (name, description, contacts and the logo shown on listings), notifications and a summary of analytics.[^s2][^s4]
- **Home also lists listings.** Your Listings shows up to four in-progress or published listings and links to the full library.[^s2][^s4]
- **Listings** is where consultant and solution listings are built in the Listing Builder, submitted for approval and published.[^s4]
- **Technologies** connects the technical side: orgs, managed packages, APIs and add-ons such as trial templates and demos.[^s2][^s4]

The Technologies tab is split into Solutions, Trial Templates and Orgs.[^s3] To add a packaged solution, the partner clicks Connect Technology, picks Packaged Solution and a type (Salesforce Platform Package, Quip or B2C Commerce Cartridge), then logs in to the source org and allows access; the packages in that org then appear.[^s3][^s5] API solutions are added with a link to the live app instead.[^s5] Connecting orgs is required before trial templates and packages can be linked.[^s3]

From a connected solution the partner clicks **Register Package** and signs in to an org that has the License Management App installed, such as a Partner Business Org.[^s3] The default license applied at install is active and site-wide; partners can instead choose a free trial with a length in days or a per-seat license.[^s3][^s5] The same solution page has **Start Review**, which opens the security review wizard.[^s3]

## Limits and gotchas

- **Security review is required for some solution types only.** It applies to Salesforce Platform packages, Marketing Cloud Engagement API solutions and Salesforce Platform API solutions.[^s2][^s3]
- **Review takes time.** Trailhead advises allowing two to four weeks for the security review, and a listing can't be published until it passes.[^s3][^s5]
- **License registration is conditional.** It is required for solutions sold through AgentExchange Checkout and optional for other pricing types.[^s3]
- **Listing approval is separate.** The partner guide puts listing approval at about 30 days and requires a signed Partner Application Distribution Agreement to publish.[^s5]
- **Resubmission triggers.** Changing a listing's title or pricing model while it is in review means submitting it again.[^s5]
- **Drafts are cheap.** The Listing Builder has five steps, and only the listing title is needed to save a draft.[^s3][^s5]

Language matters at listing creation: English listings publish to AgentExchange and Japanese listings to AgentExchange Japan.[^s3] Support for the console is requested by logging a case through the help icon in the Partner Community.[^s5]

## When to use it (and when not)

Any partner preparing a public or private AgentExchange presence works in the Partner Console, whether the listing is a packaged app or agent, an API integration or a consulting practice.[^s3][^s4] It is the gateway, not the place where licenses are managed day to day: once a package is registered, seats, expiry and status are handled in the License Management App.[^s3][^s5] Teams building internal unlocked packages for their own orgs have no reason to use it, because the console exists to list and license solutions for other customers.[^s1][^s4]

## Connections

The console is the partner-facing front door of **AgentExchange** and the distribution end of ISV **application lifecycle management**.[^s1][^s4] It **integrates with** the **License Management App**, which receives registered packages, and **depends on** a **Partner Business Org** as the usual home of that app.[^s3] It **contains** the entry point to the **AgentExchange Security Review**.[^s2][^s3] Packages come from **first-generation** packaging orgs or, for **second-generation managed packages**, from a connected **Dev Hub**, and trial templates link it to **Trialforce**.[^s3][^s5] The ISVforce Guide documents the console alongside the **AgentExchange Go-To-Market App**, the partner tool for the selling that follows a published listing.[^s1]

## Sources

[^s1]: Salesforce Developers, "Access the AppExchange Partner Console" (ISVforce Guide). https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packageGuide/appexchange_launch_partner_console.htm (accessed 2026-11-25)
[^s2]: Trailhead, "Explore the AgentExchange Partner Console Features". https://trailhead.salesforce.com/content/learn/modules/appexchange-partners-publishing/appexchange-partner-console (accessed 2026-11-25)
[^s3]: Trailhead, "Connect and Select Your Listing Type for AgentExchange". https://trailhead.salesforce.com/content/learn/modules/appexchange-partners-publishing/appexchange-technologies (accessed 2026-11-25)
[^s4]: Trailhead, "Get to Know AgentExchange NextGen Publishing". https://trailhead.salesforce.com/content/learn/modules/appexchange_publishing_quick_look/get-to-know-appexchange-nextgen-publishing (accessed 2026-11-25)
[^s5]: Salesforce, "The AppExchange Partner Console Guide". https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/partners/readiness/the_appexchange_partner_console_guide.pdf (accessed 2026-11-25)
