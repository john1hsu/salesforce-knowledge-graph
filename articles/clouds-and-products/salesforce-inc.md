---
id: kt:salesforce-inc
type: Organization
title: Salesforce, Inc.
aliases: [Salesforce Inc, salesforce.com inc, Salesforce (company), NYSE CRM]
domain: clouds-and-products
summary: >-
  The San Francisco-based enterprise software company, founded in 1999, that builds and operates the
  Salesforce Platform and its clouds and has grown its portfolio through acquisitions such as MuleSoft,
  Tableau, Slack and Informatica.
release: "Winter '27"
status: current
broader: [kt:salesforce-ecosystem]
related: [kt:salesforce-platform, kt:salesforce-certification-program]
relations:
  - {predicate: hasPart, object: kt:agentforce}
  - {predicate: hasPart, object: kt:mulesoft-anypoint-platform}
  - {predicate: hasPart, object: kt:tableau}
  - {predicate: hasPart, object: kt:slack-platform}
sources:
  - id: s1
    title: "Salesforce, Inc. Form 10-K for the fiscal year ended January 31, 2026"
    publisher: U.S. Securities and Exchange Commission (EDGAR)
    url: https://www.sec.gov/Archives/edgar/data/1108524/000110852426000060/crm-20260131.htm
    type: government
    accessed: 2026-11-06
  - id: s2
    title: "Get to Know the Salesforce Release Process"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sf_releases/sf_releases_start
    type: official-learning
    accessed: 2026-11-06
  - id: s3
    title: "Salesforce Releases"
    publisher: Salesforce
    url: https://www.salesforce.com/releases/
    type: official-docs
    accessed: 2026-11-06
  - id: s4
    title: "Salesforce Has Announced the Close of Its MuleSoft Acquisition"
    publisher: Salesforce Newsroom
    url: https://www.salesforce.com/news/stories/salesforce-has-announced-the-close-of-its-mulesoft-acquisition/
    type: news
    accessed: 2026-11-06
  - id: s5
    title: "Salesforce Completes Exchange Offer for Tableau Common Stock"
    publisher: Salesforce Investor Relations
    url: https://investor.salesforce.com/news/news-details/2019/Salesforce-Completes-Exchange-Offer-for-Tableau-Common-Stock/default.aspx
    type: news
    accessed: 2026-11-06
  - id: s6
    title: "Salesforce Announces Second Quarter Fiscal 2022 Results (Form 8-K, Exhibit 99.1)"
    publisher: U.S. Securities and Exchange Commission (EDGAR)
    url: https://www.sec.gov/Archives/edgar/data/1108524/000110852421000044/crm-q2fy22xexhibit991.htm
    type: news
    accessed: 2026-11-06
created: 2026-11-06
---

# Salesforce, Inc.

Salesforce, Inc. is the company behind the Salesforce Platform, its clouds and the wider ecosystem this graph describes. It was founded in 1999, is incorporated in Delaware, has its headquarters in Salesforce Tower on Mission Street in San Francisco, and trades on the New York Stock Exchange under the ticker CRM.[^s1] For practitioners the company matters less as a corporate entity than as the single vendor that sets release timing, product names, licensing and the roadmap every org runs on.

## Scale and portfolio

Salesforce's fiscal year ends on January 31. For fiscal 2026 it reported revenue of $41.5 billion, up 10% year over year, and 83,334 employees as of January 31, 2026.[^s1] Its 10-K positions Agentforce as the agentic layer of the Agentforce 360 Platform, alongside Data 360 (the product formerly called Data Cloud), Slack, Tableau, MuleSoft and Informatica. The company lists five core values: trust, customer success, innovation, equality and sustainability.[^s1]

## Growth by acquisition

Much of today's product map arrived through acquisitions, which is why naming, licensing and architecture often differ between "core" Salesforce and the acquired lines.[^s1]

- **MuleSoft** (completion announced May 2, 2018): brought the Anypoint Platform for connecting applications, data and devices across cloud and on-premises systems, initially packaged as Salesforce Integration Cloud.[^s4]
- **Tableau** (closed August 1, 2019): became a wholly owned subsidiary after a second-step merger, though it was kept operationally separate while a UK competition review was pending.[^s5]
- **Slack** (closed July 21, 2021): acquired for roughly $15.8 billion in cash plus about 46 million Salesforce shares, with Slack's convertible notes assumed.[^s6]
- **Informatica** (closed November 2025): total consideration of about $9.6 billion, partly financed by $6.0 billion of term borrowing; it contributed about $0.4 billion of fiscal 2026 revenue.[^s1]

Acquired products typically keep separate infrastructure, admin consoles and contracts for years, so architects should verify integration depth rather than assume it from shared branding.[^s4][^s5]

## How the company ships software

Salesforce delivers three seasonal major releases a year, Spring, Summer and Winter, typically arriving in February, June and October, while some products also ship monthly updates.[^s3] Because the platform is multitenant and metadata-driven, upgrades are applied automatically and every customer runs the same version; each upgrade needs only a short scheduled maintenance window.[^s2] Sandboxes are upgraded about four to six weeks before production, and the upgrade dates are published well in advance on the Salesforce Trust site, so teams should plan regression testing around that preview window.[^s2][^s3] This is also why each article in this graph is stamped with the release it was verified against.

## Gotchas for practitioners

- **Renames are frequent.** The 10-K already uses Data 360 and Agentforce 360 Platform naming, so documentation, contracts and older Trailhead content may refer to the same product by different names.[^s1]
- **Release names are seasonal, not calendar-aligned.** A Winter release ships in October of the preceding calendar year, which is why it carries the next year's number.[^s3]
- **The roadmap is set by one vendor.** Since all customers share one version, a deprecation or enforced release update reaches every org on the vendor's timeline rather than the customer's.[^s2]

## Connections

Salesforce, Inc. sits under `kt:salesforce-ecosystem` as the vendor at its centre. It owns and operates `kt:salesforce-platform`, whose multitenant design is what makes the shared, three-times-a-year upgrade model possible.[^s2] Its product portfolio `hasPart` `kt:agentforce`, the agentic layer it now leads with,[^s1] and the acquired lines `kt:mulesoft-anypoint-platform`,[^s4] `kt:tableau`[^s5] and `kt:slack-platform`;[^s6] those articles carry the inverse `acquiredBy` edges back to this node. The company also runs `kt:salesforce-certification-program`, the credentialing path for admins, developers, consultants and architects who work on its products.

## Sources
[^s1]: U.S. SEC (EDGAR), "Salesforce, Inc. Form 10-K for the fiscal year ended January 31, 2026". https://www.sec.gov/Archives/edgar/data/1108524/000110852426000060/crm-20260131.htm (accessed 2026-11-06)
[^s2]: Trailhead, "Get to Know the Salesforce Release Process". https://trailhead.salesforce.com/content/learn/modules/sf_releases/sf_releases_start (accessed 2026-11-06)
[^s3]: Salesforce, "Salesforce Releases". https://www.salesforce.com/releases/ (accessed 2026-11-06)
[^s4]: Salesforce Newsroom, "Salesforce Has Announced the Close of Its MuleSoft Acquisition" (2018). https://www.salesforce.com/news/stories/salesforce-has-announced-the-close-of-its-mulesoft-acquisition/ (accessed 2026-11-06)
[^s5]: Salesforce Investor Relations, "Salesforce Completes Exchange Offer for Tableau Common Stock" (2019). https://investor.salesforce.com/news/news-details/2019/Salesforce-Completes-Exchange-Offer-for-Tableau-Common-Stock/default.aspx (accessed 2026-11-06)
[^s6]: U.S. SEC (EDGAR), "Salesforce Announces Second Quarter Fiscal 2022 Results" (Form 8-K, Exhibit 99.1, 2021). https://www.sec.gov/Archives/edgar/data/1108524/000110852421000044/crm-q2fy22xexhibit991.htm (accessed 2026-11-06)
