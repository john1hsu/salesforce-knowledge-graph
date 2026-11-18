---
id: kt:scale-center
type: Tool
title: Scale Center
aliases: [Salesforce Scale Center, Scale Insights, org performance analysis]
domain: platform-architecture
summary: >-
  A self-serve Setup tool that shows near real-time org performance metrics (request time, CPU, errors,
  row locks) and generates analysis reports and insights that help teams find the root cause of scale problems
  in production and Full Copy sandboxes.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:lightning-experience-performance, kt:large-data-volumes, kt:record-locking, kt:governor-limits, kt:sandbox-types, kt:well-architected-framework]
relations:
  - {predicate: integratesWith, object: kt:scale-test}
  - {predicate: hasPart, object: kt:apexguru}
sources:
  - id: s1
    title: "View and Compare Org Performance Metrics with Scale Center (Scale Center Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/scale-center-quick-look/view-and-compare-org-performance-metrics-with-scale-center
    type: official-learning
    accessed: 2026-11-18
  - id: s2
    title: "Salesforce Scale Center Is Generally Available"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/07/salesforce-scale-center-is-generally-available
    type: official-blog
    accessed: 2026-11-18
  - id: s3
    title: "Monitor and Improve Org Performance with Scale Center"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2025/scale-center-gives-admins-the-insights-and-tools-to-improve-org-performance
    type: official-blog
    accessed: 2026-11-18
  - id: s4
    title: "Empowering Admins: Build Org Scalability With New Scale Center Features"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/empowering-admins-build-org-scalability-with-new-scale-center-features
    type: official-blog
    accessed: 2026-11-18
  - id: s5
    title: "Load Test on the Salesforce Platform Using Scalability Tools"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/02/load-test-on-the-salesforce-platform-using-scalability-tools
    type: official-blog
    accessed: 2026-11-18
created: 2026-11-18
---

# Scale Center

Scale Center is a Salesforce Setup tool that gives teams self-serve, near real-time access to their org's performance metrics, so they can trace scale problems to a root cause instead of opening a support case.[^s1] Salesforce announced it as generally available in July 2023.[^s2] It is meant to "shift left": catch inefficient code and configuration in a sandbox before it reaches production, and confirm in production whether a release made things better or worse.[^s1][^s3] Salesforce states that it does not affect org performance and does not access org data.[^s1][^s2]

## How it works

An admin enables it from Setup by searching for Scale Center in Quick Find and turning on **Enable Scale Center**; metrics can take up to about two hours to appear afterwards.[^s1][^s2]

The **Org Performance** view summarizes common errors (failed logins, concurrent Apex errors, concurrent UI errors, row lock errors and callout errors) and charts average request time, request volume, application and database CPU time, logins, total errors and average callout time.[^s1] Dragging across a spike on a chart starts an analysis report for that window.[^s1][^s2] A **Compare** option sets a base time range against a second range, which suits pre-deployment sandbox testing, post-release impact checks and peak-day analysis.[^s1][^s2]

**Performance Analysis** reports go deeper for a chosen interval.[^s1] The report types listed in Trailhead are:

- Consolidated Report, Apex Summary and Concurrent Apex, for Apex CPU and concurrency problems.[^s1]
- Database Performance, Governor Limits, Row Lock, and List Views and Reports, for data-tier load.[^s1]
- Flow Performance and Integrations Performance, for automation and callout activity.[^s1]

Reports surface items such as the top SOQL queries by database CPU time, top entry points, record-type activity and the users driving the most database CPU.[^s1] The Performance Analysis page lists up to 100 reports.[^s1]

**Scale Insights** add packaged analyses. Reports Insights flag the slowest reports each week with run-time analytics and recommendations.[^s3] Since early 2026, insights can be generated on demand rather than only on a schedule, with a stated allowance of three on-demand insights per week per org.[^s4] Newer insights include Search Insights, which finds searchable entities that are never used, and Lightning Experience Insights, an open beta that uses Experienced Page Time to find slow pages, components, browsers and geographies.[^s4] **ApexGuru**, which uses AI to flag Apex anti-patterns, hotspots and unused methods, is delivered through Scale Center, and its findings can be exported as a PDF for developers.[^s3]

## Availability and gotchas

- Original availability was free for Unlimited Edition production and Full Copy sandbox orgs, plus Signature Success customers.[^s1][^s3]
- A February 2026 Salesforce update says access now extends to Enterprise and Professional Edition, partners and ISVs, and new LDV orgs.[^s4]
- It is not supported in Government Cloud Plus, Developer, Developer Pro or Partial Copy sandboxes.[^s1][^s2]
- Sandbox results are only meaningful when the Full Copy sandbox has been refreshed so metadata and data match production.[^s5]

## When to use it (and when not)

Use Scale Center when an org shows symptoms such as row lock errors, concurrent Apex errors or slow request times, or around a deployment to compare before and after windows.[^s1][^s3] It reports on load the org actually experiences; to generate production-scale load in a sandbox, teams pair it with Scale Test, which runs the test while Scale Center analyzes the results.[^s5] Signature customers can also follow links from Customer Success Score technical-health signals into the matching Scale Center views.[^s4]

## Connections

Scale Center is an org-level diagnostic tool on the **Salesforce Platform** (`kt:salesforce-platform`, broader).[^s1] It **integrates with** **Scale Test** (`kt:scale-test`): the developer guidance runs Scale Center during the initial 100-user test and again after the full test to review request volume, row lock and Apex data.[^s5] It **has part** **ApexGuru** (`kt:apexguru`), the AI code-analysis feature delivered inside it.[^s3] Its error categories map to **record locking** (`kt:record-locking`) and **governor limits** (`kt:governor-limits`), and its database reports help with **large data volumes** (`kt:large-data-volumes`).[^s1][^s4] Lightning Experience Insights extend it into **Lightning Experience performance** (`kt:lightning-experience-performance`).[^s4] Support for Full Copy but not Developer or Partial Copy sandboxes ties it to **sandbox types** (`kt:sandbox-types`), and it supplies evidence for the performance concerns of the **Well-Architected Framework** (`kt:well-architected-framework`).[^s1][^s3]

## Sources

[^s1]: Trailhead, "View and Compare Org Performance Metrics with Scale Center". https://trailhead.salesforce.com/content/learn/modules/scale-center-quick-look/view-and-compare-org-performance-metrics-with-scale-center (accessed 2026-11-18)
[^s2]: Salesforce Developers Blog, "Salesforce Scale Center Is Generally Available". https://developer.salesforce.com/blogs/2023/07/salesforce-scale-center-is-generally-available (accessed 2026-11-18)
[^s3]: Salesforce Admins Blog, "Monitor and Improve Org Performance with Scale Center". https://admin.salesforce.com/blog/2025/scale-center-gives-admins-the-insights-and-tools-to-improve-org-performance (accessed 2026-11-18)
[^s4]: Salesforce Admins Blog, "Empowering Admins: Build Org Scalability With New Scale Center Features". https://admin.salesforce.com/blog/2026/empowering-admins-build-org-scalability-with-new-scale-center-features (accessed 2026-11-18)
[^s5]: Salesforce Developers Blog, "Load Test on the Salesforce Platform Using Scalability Tools". https://developer.salesforce.com/blogs/2025/02/load-test-on-the-salesforce-platform-using-scalability-tools (accessed 2026-11-18)
