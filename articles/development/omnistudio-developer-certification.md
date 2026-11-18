---
id: kt:omnistudio-developer-certification
type: Certification
title: Omnistudio Developer Certification
aliases: [Salesforce Certified Omnistudio Developer, Salesforce Certified OmniStudio Developer, OmniStudio Developer Certification, Plat-Dev-210]
domain: development
summary: >-
  Salesforce's build-focused credential for Omnistudio, covering FlexCards, OmniScripts, Integration Procedures,
  Data Mappers and troubleshooting; a proctored 60-question exam with a 72% passing score and no prerequisite,
  kept current through a yearly Omnistudio Developer maintenance badge.
release: "Winter '27"
status: current
broader: [kt:salesforce-certification-program]
related: [kt:omnistudio, kt:omnistudio-consultant-certification, kt:platform-developer-certification, kt:salesforce-industries, kt:lightning-web-components]
relations:
  - {predicate: alternativeTo, object: kt:omnistudio-consultant-certification}
sources:
  - id: s1
    title: "Salesforce Certified Omnistudio Developer Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298971&language=en_US&type=1
    type: official-learning
    accessed: 2026-11-18
  - id: s2
    title: "Certification - Salesforce Certified Omnistudio Developer"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/credentials/omnistudiodeveloper
    type: official-learning
    accessed: 2026-11-18
  - id: s3
    title: "Prepare for Your Salesforce Omnistudio Developer Certification (trail)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/trails/prepare-for-your-salesforce-omnistudio-developer-certification
    type: official-learning
    accessed: 2026-11-18
  - id: s4
    title: "Developer Certifications"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/credentials/developeroverview
    type: official-learning
    accessed: 2026-11-18
created: 2026-11-18
---

# Omnistudio Developer Certification

The **Salesforce Certified Omnistudio Developer** credential is for people with hands-on experience using Omnistudio tools to design and configure cloud applications for complex business problems.[^s2] Trailhead files it among its developer certifications, next to Platform Developer, Platform Developer II and JavaScript Developer.[^s4] The exam guide pictures a candidate who builds and customizes applications by mixing declarative tools with some code. A typical case is a guided business process with conditional navigation that reads and writes Salesforce and external data as JSON over REST.[^s1] Older material spells the product "OmniStudio", and Trailhead Academy's exam page uses the code Plat-Dev-210.[^s2]

## Who it is for

The guide recommends about a year of general developer experience plus three to six months designing, implementing and deploying with Omnistudio. It lists Platform Developers, App Builders, Solution and Technical Architects, and UI Developers as typical candidates.[^s1] Candidates should know some HTML, JavaScript and CSS.[^s1] Several things are explicitly out of scope: browser-console debugging, Lightning Web Components, Apex or Angular experience, performance and scalability tuning, integrating Omnistudio with other industry products, installation and post-install setup, and administering industry entities such as products, prices and rules.[^s1]

## Exam format

The exam has 60 scored multiple-choice and multiple-select questions plus up to five unscored ones, a 105-minute time limit and a **72% passing score**.[^s1] Registration costs USD 200 and a retake USD 100, plus applicable taxes. It is proctored, at a test centre or online, with no reference material allowed and **no prerequisite** credential.[^s1] The guide version current at writing aligns its questions to the Spring '26 release.[^s1] Trailhead lists Platform Developer, Platform Developer II and Revenue Management Consultant as related certifications, not requirements.[^s2]

## What the exam covers

The outline has six weighted sections:[^s1]

- **Omnistudio Fundamentals (18%)**: industry use cases, the two runtimes and their upgrades, licences and permission sets, implementation tooling, and testing, versioning and cloning components.[^s1]
- **FlexCards (15%)**: data sources and their JSON, multi-level cards, actions and events, states for conditional rendering, styling, and embedding across channels.[^s1]
- **OmniScripts (20%)**: Group, Action and Input elements, child scripts and custom LWCs, multi-language and save options, Knowledge and the Messaging Framework.[^s1]
- **Integration Procedures (15%)**: server-side orchestration, Data Mapper and HTTP actions, branching and loops, chainable procedures, caching, and Try/Catch with rollback.[^s1]
- **Data Mappers (17%)**: Extract, Turbo Extract, Load and Transform interfaces, formulas, and mapping to JSON, sObjects, PDF or DocuSign output.[^s1]
- **Troubleshooting and Debugging (15%)**: fixing display, mapping, caching, permission, JSON and deployment problems, using the Debug Console.[^s1]

OmniScripts carry the largest weight, and troubleshooting has its own section here, which the consultant exam lacks.[^s1]

## Preparing

The official Trailhead trail takes about 11.5 hours and opens with the exam guide.[^s3] It covers Omnistudio fundamentals and development essentials, then FlexCards, OmniScripts, Integration Procedures and Data Mappers. It closes with a troubleshooting module on previewing and testing components, monitoring component health, Integration Procedure errors, caching and security.[^s3] The guide also points to the Omnistudio documentation for both the standard runtime and the managed package, and to the instructor-led course OMS435, Build Guided Experiences with Omnistudio Tools.[^s1]

## Maintenance

Holders keep the credential by completing the Omnistudio Developer maintenance badge on Trailhead once a year. If they miss the due date, the certification expires.[^s1]

## Gotchas

- **Configuration, not code.** LWC and Apex experience are explicitly out of scope, even though custom LWCs appear inside FlexCard and OmniScript objectives.[^s1]
- **Higher bar than the consultant exam.** The passing score is 72%, and the format, time and fees otherwise match the consultant exam.[^s1]
- **Know both runtimes.** Managed-package versus standard runtime, and which upgrades need manual work, are tested under fundamentals.[^s1]
- **Debugging counts.** A full 15% is troubleshooting, so hands-on time with the Debug Console and component previews matters.[^s1][^s3]

## Connections

- **broader → `kt:salesforce-certification-program`**: one of the developer-tier credentials in Trailhead's catalogue.[^s4]
- **related → `kt:omnistudio`**: the toolset whose four components each get their own exam section.[^s1]
- **related / alternativeTo → `kt:omnistudio-consultant-certification`**: the design-focused sibling credential for the same tools; candidates choose by role, building versus recommending.[^s1]
- **related → `kt:platform-developer-certification`**: Trailhead lists it as a related developer credential, and Platform Developers are a named target audience.[^s1][^s2]
- **related → `kt:salesforce-industries`**: the guide frames Omnistudio around industry use cases such as telco, energy, healthcare and public sector.[^s1]
- **related → `kt:lightning-web-components`**: custom LWCs extend FlexCards and OmniScripts in the outline, though general LWC skill is not tested.[^s1]

## Sources
[^s1]: Salesforce Help, "Salesforce Certified Omnistudio Developer Exam Guide". https://help.salesforce.com/s/articleView?id=005298971&language=en_US&type=1 (accessed 2026-11-18)
[^s2]: Trailhead, "Certification - Salesforce Certified Omnistudio Developer". https://trailhead.salesforce.com/en/credentials/omnistudiodeveloper (accessed 2026-11-18)
[^s3]: Trailhead, "Prepare for Your Salesforce Omnistudio Developer Certification". https://trailhead.salesforce.com/content/learn/trails/prepare-for-your-salesforce-omnistudio-developer-certification (accessed 2026-11-18)
[^s4]: Trailhead, "Developer Certifications". https://trailhead.salesforce.com/en/credentials/developeroverview (accessed 2026-11-18)
