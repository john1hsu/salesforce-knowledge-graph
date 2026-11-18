---
id: kt:lightning-experience-performance
type: Concept
title: Lightning Experience Performance
aliases: [Lightning page performance, Lightning page load time, Experienced Page Time, Experience Page Time, EPT]
domain: platform-architecture
summary: >-
  How quickly Lightning Experience pages load and become usable, measured by Experienced Page Time (EPT) and shaped by
  the user's network, device and browser and by how an org's pages are configured; Salesforce exposes it through the EPT
  counter, the Lightning Usage App, Event Monitoring and Lightning Experience Insights in Scale Center.
release: "Winter '27"
status: concept
broader: [kt:salesforce-platform, kt:non-functional-requirements]
related: [kt:lightning-app-builder, kt:lightning-web-components, kt:aura-components, kt:visualforce, kt:event-monitoring, kt:scale-center]
relations:
  - {predicate: dependsOn, object: kt:content-delivery-network}
  - {predicate: dependsOn, object: kt:lightning-web-components}
  - {predicate: configuredVia, object: kt:lightning-app-builder}
  - {predicate: queriedWith, object: kt:event-monitoring}
  - {predicate: contrastsWith, object: kt:visualforce}
sources:
  - id: s1
    title: "Compare Lightning Experience to Salesforce Classic (Lightning Experience Performance Optimization)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning-experience-performance-optimization/compare-lightning-experience-to-salesforce-classic
    type: official-learning
    accessed: 2026-11-18
  - id: s2
    title: "Measure Lightning Experience Performance and Experience Page Time (EPT)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning-experience-performance-optimization/measure-lightning-experience-performance-and-experience-page-time-ept
    type: official-learning
    accessed: 2026-11-18
  - id: s3
    title: "Optimize Lightning Experience Performance"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning-experience-performance-optimization/optimize-lightning-experience-performance
    type: official-learning
    accessed: 2026-11-18
  - id: s4
    title: "Enable CDN to Load Applications Faster (Lightning Web Components Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/perf-cdn.html
    type: official-docs
    accessed: 2026-11-18
  - id: s5
    title: "Harness Lightning Experience Insights to Improve Performance"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2026/03/harness-lightning-experience-insights-to-improve-performance
    type: official-blog
    accessed: 2026-11-18
  - id: s6
    title: "Our Detailed Plan to Improve Lightning Experience Performance"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/09/our-detailed-plan-to-improve-lightning-experience-performance
    type: official-blog
    accessed: 2026-11-18
created: 2026-11-18
---

# Lightning Experience Performance

Lightning Experience performance is how fast Lightning pages load and become usable for an org's users. It behaves differently from Salesforce Classic because of where pages are built: Classic renders each page on the server and the browser simply displays it, whereas Lightning Experience assembles pages on the user's device, progressively and component by component, with subcomponents loading after their parents and logic running in client-side JavaScript that calls server-side Apex.[^s1] That shift makes the user's browser, device and network latency, as well as the complexity of each page, direct inputs to perceived speed.[^s1]

## How it is measured

Salesforce's metric is **Experienced Page Time (EPT)**: the time from when a page starts loading until no further activity occurs for roughly two frames (about 33 ms), chosen because late-loading subcomponents make simpler timings misleading.[^s1] Salesforce reports EPT at the 75th percentile (P75) and splits it into first-page-load EPT, which includes the framework bootstrap at the start of a session, and subsequent-page-load EPT for navigation once the framework is loaded.[^s5]

There are several ways to see it:

- **Header counter**: Lightning Component debug mode shows load time and bandwidth but slows pages, while the `?eptVisible=1` URL parameter shows only the counter with minified code.[^s2]
- **Lightning Usage App**: aggregated Page and Browser Performance views compare pages, browsers and devices; custom report types on `LightningUsageByBrowserMetrics` extend them.[^s2]
- **Event Monitoring**: the Lightning Page View event type (part of Salesforce Shield) logs page, browser, time on page and EPT per view.[^s2]
- **Lightning Experience Insights in Scale Center**: GA since Spring '26, with an overview, best-practice findings, trends by geography and browser, and a list of slow, high-traffic pages.[^s5]

When measuring manually, avoid opening the page in a new tab or reloading it, because the framework bootstrap then inflates the number.[^s2]

## What drives it

Trailhead groups the factors into network, device, browser and Salesforce configuration.[^s3]

- **Network**: Salesforce recommends latency of 150 ms or lower and download speed of at least 3 Mbps, checked with the org's Speedtest page.[^s3]
- **Distance and VPNs**: users far from their instance pay for every round trip, and a secure session needs at least three of them.[^s3]
- **Device**: at least 8 GB of RAM with 3 GB free for Salesforce tabs; the Octane benchmark (via `speedtest.jsp`) gauges JavaScript speed.[^s3]
- **Browser**: keep it current, enable JavaScript, cookies, TLS and iframes, and disable unneeded extensions; Chrome is usually fastest.[^s3]
- **Configuration**: pages with many fields, inefficient custom components, complex layouts or embedded Visualforce load more slowly than standard pages.[^s3]

Salesforce's own engineering work shows where time goes: in 2023 it found that nearly half of P75 EPT was idle time waiting on earlier XHR requests, and that components on hidden tabs still fetched data.[^s6] Its plan targeted request concurrency, smaller bootstrap code, converting Aura components to LWC, and deferring below-the-fold rendering.[^s6] Salesforce later reported Lightning Experience 37% faster as of Dreamforce 2025.[^s5]

## Limits and gotchas

The Lightning CDN serves only the framework's static JavaScript and CSS (through Akamai), never org data or metadata.[^s4] It is enabled by default for new orgs and Experience Builder sites but off by default for orgs created before Winter '19; turn it on in Session Settings.[^s4] Networks that filter traffic must allowlist `https://static.lightning.force.com` by domain, because the CDN's IP addresses are dynamic.[^s4] Bootstrap time is not directly actionable, so tuning effort belongs on subsequent loads and on specific heavy pages.[^s5]

## When to act (and how)

Treat performance as a non-functional requirement. Start with Scale Center's slow, high-impact pages and fix the custom components and actions it names rather than refactoring broadly; reduce component counts and confirm the Lightning CDN is on.[^s5] Use the Performance Trends view to tell whether a slowdown is regional, browser-specific or org-wide before blaming page design.[^s5] For user-side causes, IT can assess latency with ping and traceroute and upgrade low-powered devices.[^s3]

## Connections

Performance sits under the **Salesforce Platform** (`kt:salesforce-platform`) and is a classic **non-functional requirements** (`kt:non-functional-requirements`) concern.[^s3] It depends on the **Content Delivery Network** (`kt:content-delivery-network`) for first loads and on the move to **Lightning Web Components** (`kt:lightning-web-components`) away from **Aura components** (`kt:aura-components`).[^s4][^s6] Pages are configured in **Lightning App Builder** (`kt:lightning-app-builder`), where component counts are decided, and embedded **Visualforce** (`kt:visualforce`) contrasts with native Lightning rendering as a common slowdown.[^s3] Per-view data is queried through **Event Monitoring** (`kt:event-monitoring`), and org-level diagnosis lives in **Scale Center** (`kt:scale-center`).[^s2][^s5]

## Sources

[^s1]: Trailhead, "Compare Lightning Experience to Salesforce Classic". https://trailhead.salesforce.com/content/learn/modules/lightning-experience-performance-optimization/compare-lightning-experience-to-salesforce-classic (accessed 2026-11-18)
[^s2]: Trailhead, "Measure Lightning Experience Performance and Experience Page Time (EPT)". https://trailhead.salesforce.com/content/learn/modules/lightning-experience-performance-optimization/measure-lightning-experience-performance-and-experience-page-time-ept (accessed 2026-11-18)
[^s3]: Trailhead, "Optimize Lightning Experience Performance". https://trailhead.salesforce.com/content/learn/modules/lightning-experience-performance-optimization/optimize-lightning-experience-performance (accessed 2026-11-18)
[^s4]: Salesforce Developers, "Enable CDN to Load Applications Faster". https://developer.salesforce.com/docs/platform/lwc/guide/perf-cdn.html (accessed 2026-11-18)
[^s5]: Salesforce Developers Blog, "Harness Lightning Experience Insights to Improve Performance" (2026). https://developer.salesforce.com/blogs/2026/03/harness-lightning-experience-insights-to-improve-performance (accessed 2026-11-18)
[^s6]: Salesforce Developers Blog, "Our Detailed Plan to Improve Lightning Experience Performance" (2023). https://developer.salesforce.com/blogs/2023/09/our-detailed-plan-to-improve-lightning-experience-performance (accessed 2026-11-18)
