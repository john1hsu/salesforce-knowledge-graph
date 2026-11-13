---
id: kt:government-cloud
type: Product
title: Government Cloud
aliases: [Salesforce Government Cloud, Salesforce GovCloud, Government Cloud orgs]
domain: public-sector-and-compliance
summary: >-
  Salesforce's family of government-only environments, launched in 2014 as a dedicated, US-staffed instance with a
  FedRAMP Moderate agency ATO and now sold as Government Cloud Plus, Plus - Defense and Plus - Premium editions on
  AWS GovCloud (US).
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:public-sector-solutions, kt:il4-and-il5, kt:salesforce-shield, kt:data-residency, kt:multitenancy]
relations:
  - {predicate: contrastsWith, object: kt:government-cloud-plus}
  - {predicate: implements, object: kt:fedramp}
  - {predicate: dependsOn, object: kt:my-domain}
sources:
  - id: s1
    title: "Salesforce.com announces new Salesforce Government Cloud"
    publisher: Salesforce
    url: https://www.salesforce.com/news/?p=20732
    type: news
    accessed: 2026-11-13
  - id: s2
    title: "Salesforce Security White Paper for Salesforce Government Cloud (November 2018)"
    publisher: Salesforce (hosted by the California Department of Technology)
    url: https://etp.ca.gov/wp-content/uploads/sites/70/2019/10/salesforce-security-white-paper-for-salesforce-government-cloud.pdf
    type: official-docs
    accessed: 2026-11-13
  - id: s3
    title: "Salesforce Government Cloud"
    publisher: Salesforce
    url: https://www.salesforce.com/government/cloud/
    type: official-docs
    accessed: 2026-11-13
  - id: s4
    title: "FedRAMP and Government Cloud FAQ"
    publisher: Salesforce
    url: https://www.salesforce.com/fedramp/
    type: official-docs
    accessed: 2026-11-13
  - id: s5
    title: "Prepare for a migration to Government Cloud"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000387917&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-13
  - id: s6
    title: "Use Agentforce Vibes with Government Cloud Orgs"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/agentforcevibes/guide/afv-government-cloud.html
    type: official-docs
    accessed: 2026-11-13
created: 2026-11-13
---

# Government Cloud

Government Cloud is the name Salesforce uses for the environments it reserves for US public-sector customers and their contractors, separate from the commercial service that most orgs run on. The term covers two things a practitioner meets in practice: the original Government Cloud instance launched in 2014, and today's product family, which Salesforce describes as a dedicated environment built on AWS GovCloud (US) and sells in several Government Cloud Plus editions.[^s1][^s3] Whichever generation an org sits in, a "Government Cloud org" behaves differently from a commercial org in its endpoints, available features and onboarding, so the label matters well beyond procurement.[^s5][^s6]

## History: the 2014 Government Cloud

Salesforce announced Government Cloud on May 30, 2014, covering both its PaaS and SaaS offerings. The Department of Health and Human Services had granted an Authority to Operate based on the FedRAMP baseline requirements, and the environment ran on isolated multitenant infrastructure (servers, storage, network gear) managed by US citizens in the US. Eligible buyers were US federal, state and local governments, federally funded research and development centers (FFRDCs) and government contractors.[^s1]

Salesforce's 2018 security white paper describes this environment as a dedicated instance of the same multitenant community-cloud architecture used commercially, hosted in two US colocation data centers in secure space dedicated to Salesforce. Hardware serving it was kept separate from hardware for other customers, and access to systems holding customer data was limited to qualified US citizens who were physically in the US and had passed a background check.[^s2] The paper aligned the environment with the FedRAMP Moderate impact level, citing the HHS agency ATO from May 2014 plus DoD Impact Level 2 and Impact Level 4 provisional authorizations, IL4 having been granted in 2017. In-scope services then included Lightning Platform, Sales, Service, Communities, Einstein Analytics, Shield (Platform Encryption, Event Monitoring, Field Audit Trail), Health Cloud and Financial Services Cloud.[^s2]

## The current product family

Salesforce's Government Cloud page now presents the offering as three Government Cloud Plus editions on AWS GovCloud (US):[^s3]

- **Government Cloud Plus**, priced as 15% applied to net spend, listing FedRAMP Class D (formerly High), IRS 1075 and HIPAA.[^s3]
- **Government Cloud Plus - Defense**, priced as 25% applied to net spend, physically isolated and aimed at DoD Impact Levels 4 and 5.[^s3]
- **Government Cloud Plus - Premium**, an air-gapped, Top Secret authorized edition for classified national security systems, priced on request.[^s3]

The accompanying FAQ, first published April 30, 2024, says the Plus edition holds a JAB provisional authorization and that the Defense edition requires Common Access Card MFA, salesforce.mil domains and DISA's Boundary Cloud Access Point. Contractors may buy Defense only to support DoD mission owners, not for internal use.[^s4] The same page states that Government Cloud can help with CMMC Levels 2 and 3 for Controlled Unclassified Information, based on a third-party NIST SP 800-171 Rev 2 assessment.[^s4]

## Moving an org into Government Cloud

Getting an existing production org into Government Cloud is an instance migration, not a setting. Salesforce's preparation guide requires My Domain, because generic hosts such as login.salesforce.com are not supported there, and asks customers to remove hard-coded instance references, add the new data center IP ranges to allowlists, review SPF records and regenerate WSDLs.[^s5] Org IDs and record IDs do not change. A Government Cloud test environment should be requested more than two weeks before the migration window, and Email-to-Case messages are held for at most 24 hours during the move.[^s5]

## Limits and gotchas

- **Boundary, not marketplace.** AgentExchange apps generally sit outside the authorization boundary, even when they run natively on the platform.[^s4]
- **Feature differences are real.** Government Cloud orgs route AI developer tooling to a dedicated government endpoint, do not support Anthropic models there, and do not yet support Salesforce-hosted MCP servers.[^s6]
- **Edition matters for compliance claims.** Impact levels and authorizations differ per edition, so confirm which edition an org runs in before citing an authorization in an ATO package.[^s3][^s4]
- **Login hosts.** Tooling must log in through the org's My Domain URL rather than the standard production login host.[^s5][^s6]

## Connections

Government Cloud is a government-only deployment of the Salesforce platform (`kt:salesforce-platform`, broader), reusing the multitenant architecture (`kt:multitenancy`) on segregated hardware.[^s2] It `contrastsWith` Government Cloud Plus (`kt:government-cloud-plus`): the original instance ran in Salesforce colocation data centers at FedRAMP Moderate, while the Plus line runs on AWS GovCloud and carries the higher authorizations.[^s2][^s3] It `implements` FedRAMP (`kt:fedramp`) through its agency and JAB authorizations, and its Defense edition is the route to DoD IL4 and IL5 (`kt:il4-and-il5`).[^s2][^s3] Migration `dependsOn` My Domain (`kt:my-domain`).[^s5] Salesforce Shield (`kt:salesforce-shield`) and industry products such as Public Sector Solutions (`kt:public-sector-solutions`) run inside the boundary,[^s2][^s4] and data residency (`kt:data-residency`) is a related concern because the environment keeps data in US facilities run by US personnel.[^s2]

## Sources

[^s1]: Salesforce, "Salesforce.com announces new Salesforce Government Cloud" (May 30, 2014). https://www.salesforce.com/news/?p=20732 (accessed 2026-11-13)
[^s2]: Salesforce, "Salesforce Security White Paper for Salesforce Government Cloud" (November 2018). https://etp.ca.gov/wp-content/uploads/sites/70/2019/10/salesforce-security-white-paper-for-salesforce-government-cloud.pdf (accessed 2026-11-13)
[^s3]: Salesforce, "Salesforce Government Cloud". https://www.salesforce.com/government/cloud/ (accessed 2026-11-13)
[^s4]: Salesforce, "FedRAMP and Government Cloud FAQ". https://www.salesforce.com/fedramp/ (accessed 2026-11-13)
[^s5]: Salesforce Help, "Prepare for a migration to Government Cloud". https://help.salesforce.com/s/articleView?id=000387917&language=en_US&type=1 (accessed 2026-11-13)
[^s6]: Salesforce Developers, "Use Agentforce Vibes with Government Cloud Orgs". https://developer.salesforce.com/docs/platform/agentforcevibes/guide/afv-government-cloud.html (accessed 2026-11-13)
