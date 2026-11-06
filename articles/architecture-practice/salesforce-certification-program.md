---
id: kt:salesforce-certification-program
type: Concept
title: Salesforce Certification Program
aliases: [Salesforce Certifications, Salesforce credentials, Salesforce certification catalog, Trailhead certifications]
domain: architecture-practice
summary: >-
  Salesforce's portfolio of role-based credentials (Associate, Administrator, Developer, Consultant, Architect,
  Designer, Marketer and Accredited Professional), earned by exam and kept active through one Trailhead maintenance
  badge per year, with periodic renames and retirements to track the product line.
release: "Winter '27"
status: current
broader: [kt:trailhead]
related: [kt:salesforce-architect, kt:agentforce, kt:salesforce-inc]
relations:
  - {predicate: hasPart, object: kt:platform-administrator-certification}
  - {predicate: hasPart, object: kt:platform-developer-certification}
  - {predicate: hasPart, object: kt:sales-cloud-consultant-certification}
  - {predicate: hasPart, object: kt:data-cloud-consultant-certification}
  - {predicate: hasPart, object: kt:certified-technical-architect}
sources:
  - id: s1
    title: "Salesforce Certification Maintenance Schedule"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298922&type=1
    type: official-docs
    accessed: 2026-11-06
  - id: s2
    title: "Salesforce Certification Name Changes FAQ"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298915&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-06
  - id: s3
    title: "2027 Salesforce Certification Retirements FAQ"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005360289&type=1
    type: official-docs
    accessed: 2026-11-06
  - id: s4
    title: "Certification - Administrator Overview"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/administratoroverview
    type: official-learning
    accessed: 2026-11-06
  - id: s5
    title: "The Salesforce Certification Lifecycle: How we build, maintain, and evolve our certification portfolio"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/salesforce-certification-lifecycle/
    type: official-blog
    accessed: 2026-11-06
created: 2026-11-06
---

# Salesforce Certification Program

The **Salesforce Certification Program** is the catalogue of exam-based credentials that Salesforce publishes through Trailhead to validate skills on its products. Trailhead groups the credentials by role: Administrator, Architect, Developer, Consultant, Designer, Marketer and Sales Professional. Beside those role tracks sit two special families. **Associate** certifications cover foundational knowledge of the Customer 360 platform, and partner-only **Accredited Professional** (AP) certifications validate implementation readiness for specific industry and commerce products.[^s4] The Administrator track alone currently lists Agentforce Specialist, Business Analyst, Marketing Cloud Engagement Administrator, Platform Administrator, Platform Administrator II, Platform App Builder, Slack Administrator and two Tableau credentials.[^s4] For practitioners, the catalogue works as a shared vocabulary for hiring, staffing and partner scoring. This node describes the program as a whole; individual credentials are separate nodes.

## How the lifecycle works

Salesforce describes the portfolio as a managed lifecycle with four phases. It **builds** new credentials as market demand and strategy shift (Agentforce being the current driver). It requires holders to **maintain** them. It **retires** credentials whose skills it no longer evaluates. It supports **continued learning** through Trailhead and, for partners, Partner Learning Camp.[^s5]

## Maintenance rules

Every certification needs **one maintenance badge per year**, completed on Trailhead. Badges are released at the start of the Spring, Summer and Winter release cycles. Each badge is due roughly a year after release.[^s1] On the current schedule, the Winter '26 badges are due December 4, 2026, the Spring '26 badges April 16, 2027, and the Summer '26 badges August 20, 2027 (Pacific Time, subject to change).[^s1] Some credentials stack badges:

- Application Architect and Technical Architect each need the Platform App Builder, Platform Developer and Architect badges.
- System Architect needs the Platform Developer and Architect badges.
- The single Architect badge maintains the five domain architect credentials: Data, Development Lifecycle and Deployment, Identity and Access Management, Integration, and Sharing and Visibility.[^s1]

There are several exceptions. Foundations certifications have no maintenance and never expire. AP certifications currently need no action while Salesforce designs a new maintenance plan. A completed badge can take up to 24 hours to update certification status.[^s1]

## Gotchas

- **Expiry is hard.** A missed deadline expires the certification. A holder whose certification expired recently can ask for reinstatement through a support case, but approval is decided case by case. If it has been expired for more than one cycle, the holder must retake the exam.[^s1]
- **Renames are not new credentials.** On July 24, 2026 Salesforce renamed 16 certifications to match current product names, many adding "Agentforce". For example, Sales Cloud Consultant became Agentforce Sales Consultant, and Revenue Cloud Consultant became Revenue Management Consultant. Exam content and maintenance were unchanged. Trailblazer profiles updated automatically, and verification shows the new name with the original earned date.[^s2] When searching for prep material or checking a résumé, treat both names as the same credential.
- **Retired is still valid.** Twenty-four certifications retire on February 1, 2027. Registration closed July 24, 2026, and the last exam date was August 31, 2026. Their maintenance requirements were removed. Holders keep a valid credential, marked as retired on their profile, but downloadable certificates end at retirement.[^s3] Salesforce's blog adds that retired credentials drop off the public verification page, so an employer may need to see the profile instead.[^s5]
- **Successors vary.** The retirements FAQ points CPQ Administrator and CPQ and Billing Consultant holders to the Revenue Management Consultant exam. It points Heroku Developer AP holders to Heroku Architect, and Nonprofit Success Pack Consultant holders to the Nonprofit Cloud Consultant credential. Several retiring credentials, including MuleSoft Catalyst Consultant, have no named successor yet.[^s3]

## When it matters

For architects, the program sets the ladder toward Certified Technical Architect, and the shared Architect badge is the main yearly maintenance cost. For delivery leads and partners, the rename and retirement cycles affect staffing records and Partner Navigator scores, which update automatically on a rename.[^s2] Plan each year's three maintenance windows like any other release-readiness task.[^s1]

## Connections

- **broader → `kt:trailhead`**: credentials are listed, maintained and verified through Trailhead.[^s4]
- **hasPart → individual credentials** such as `kt:platform-administrator-certification`, `kt:platform-developer-certification`, `kt:sales-cloud-consultant-certification`, `kt:data-cloud-consultant-certification` and `kt:certified-technical-architect`. Each is one entry in the catalogue, and several share maintenance badges.[^s1]
- **related → `kt:salesforce-architect`**: the architect track and its shared badge define the formal path for that role.[^s1]
- **related → `kt:agentforce`**: Agentforce shapes both the new credentials and the 2026 renames.[^s2][^s5]
- **related → `kt:salesforce-inc`**: the program is run by Salesforce's certification organization.[^s5]

## Sources
[^s1]: Salesforce Help, "Salesforce Certification Maintenance Schedule". https://help.salesforce.com/s/articleView?id=005298922&type=1 (accessed 2026-11-06)
[^s2]: Salesforce Help, "Salesforce Certification Name Changes FAQ". https://help.salesforce.com/s/articleView?id=005298915&language=en_US&type=1 (accessed 2026-11-06)
[^s3]: Salesforce Help, "2027 Salesforce Certification Retirements FAQ". https://help.salesforce.com/s/articleView?id=005360289&type=1 (accessed 2026-11-06)
[^s4]: Trailhead, "Certification - Administrator Overview". https://trailhead.salesforce.com/credentials/administratoroverview (accessed 2026-11-06)
[^s5]: Salesforce, "The Salesforce Certification Lifecycle: How we build, maintain, and evolve our certification portfolio" (Kari Lucio, 2026). https://www.salesforce.com/blog/salesforce-certification-lifecycle/ (accessed 2026-11-06)
