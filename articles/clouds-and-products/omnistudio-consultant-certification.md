---
id: kt:omnistudio-consultant-certification
type: Certification
title: Omnistudio Consultant Certification
aliases: [Salesforce Certified Omnistudio Consultant, Salesforce Certified OmniStudio Consultant, OmniStudio Consultant Certification, Salesforce Omnistudio Consultant Certification]
domain: clouds-and-products
summary: >-
  Salesforce's consultant-level credential for designing maintainable, scalable solutions with Omnistudio tools
  (FlexCards, OmniScripts, Integration Procedures and Data Mappers); a 60-question proctored exam with no
  prerequisite, maintained through a yearly Omnistudio Consultant maintenance module.
release: "Winter '27"
status: current
broader: [kt:salesforce-certification-program]
related: [kt:omnistudio, kt:omnistudio-developer-certification, kt:salesforce-industries, kt:business-analyst, kt:experience-cloud]
relations:
  - {predicate: dependsOn, object: kt:business-rules-engine}
sources:
  - id: s1
    title: "Salesforce Certified Omnistudio Consultant Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298970&language=en_US&type=1
    type: official-learning
    accessed: 2026-11-18
  - id: s2
    title: "Certification - Salesforce Certified Omnistudio Consultant"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/credentials/omnistudioconsultant
    type: official-learning
    accessed: 2026-11-18
  - id: s3
    title: "Prepare for Your Salesforce Omnistudio Consultant Certification (trail)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/trails/prepare-for-your-salesforce-omnistudio-consultant-certification
    type: official-learning
    accessed: 2026-11-18
  - id: s4
    title: "Maintain Your Omnistudio Consultant Certification for Summer '26"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/omnistudio-consultant-certification-maintenance-summer-26/maintain-your-omnistudio-consultant-certification-for-summer-26
    type: official-learning
    accessed: 2026-11-18
created: 2026-11-18
---

# Omnistudio Consultant Certification

The **Salesforce Certified Omnistudio Consultant** credential is for consultants who use Omnistudio tools to design and implement solutions that are sustainable and scalable.[^s2] The official exam guide pictures a customer-facing consultant. This person can explain what the Omnistudio tools do and design maintainable solutions with them, and typically has two to three years of Salesforce experience as a business analyst, consultant, solution architect, delivery manager, project or product manager, or UX designer.[^s1] Older material spells the product "OmniStudio". The current guide and credential page use "Omnistudio" for the same certification.[^s1][^s2]

## Exam format

According to the exam guide, the exam has 60 scored multiple-choice and multiple-select questions plus up to five unscored ones, a 105-minute time limit and a 67% passing score.[^s1] Registration costs USD 200 and a retake USD 100, plus applicable taxes. The exam is proctored, at a test centre or online, and no reference material is allowed.[^s1] The guide lists **no prerequisite** credential, and the version current at writing aligns its questions to the Spring '26 release.[^s1] Trailhead's credential page lists Platform Administrator, Platform App Builder and Revenue Management Consultant as related certifications, not as requirements.[^s2]

## What the exam covers

The outline has six sections with roughly even weights:[^s1]

- **Omnistudio Fundamentals (16%)**: use cases by industry, assessing requirements and risks, the tools' purposes, managed-package versus standard runtime, and licences and permission sets.[^s1]
- **FlexCards (18%)**: choosing data sources, multi-source cards, card actions, conditional rendering with state variables, and where to embed cards.[^s1]
- **OmniScripts (17%)**: branched multi-step designs, multi-language support, choosing elements, LWC embeds and child scripts, and validation and error handling.[^s1]
- **Integration Procedures (17%)**: HTTP Actions to REST and SOAP endpoints with authentication and mapping, and shaping data with Transform, Set Values and Response actions.[^s1]
- **Data Mappers (17%)**: picking Extract, Turbo Extract, Load or Transform, formulas and functions, query performance, and ID mapping, upserts and errors on Load.[^s1]
- **Best Fit Solutions (15%)**: architectural justification, cross-component performance, governance for build, test and deployment, and data modelling for Omnistudio artifacts.[^s1]

The guide also expects working knowledge of Expression Sets and Decision Matrices from the Business Rules Engine, prebuilt industry processes, and the Agentforce Sales, Agentforce Service and Experience Cloud lifecycles.[^s1] It scopes out hands-on work: implementing the design, configuring the application, writing code (JavaScript, HTML, CSS or Apex), troubleshooting, performance analysis and platform security configuration are not tested.[^s1] The exam therefore rewards recommending the right tool and design rather than building it.[^s1]

## Preparing

Trailhead's official trailmix runs about seven and a half hours and starts with the exam guide itself.[^s3] It covers Omnistudio fundamentals badges, then units on FlexCards, OmniScripts, Integration Procedures and Data Mappers. It ends with "best fit" material on combining the tools, planning implementations, deploying between orgs and UI testing.[^s3] The exam guide also points to the Omnistudio and Business Rules Engine documentation and the instructor-led course Design and Administer an Omnistudio Solution (OMS335).[^s1]

## Maintenance

This certification has its own Trailhead maintenance module, aimed at holders of the Omnistudio Consultant credential and ending in a quiz.[^s4] The Summer '26 module covered FlexCards and OmniScripts on LWR Experience Cloud sites, Data Mapper versioning and the IS NULL operator, Omni Global Auto Number, enforced security checks, enhanced Save for Later and accessibility work.[^s4] Holders complete it by the due date on Salesforce's maintenance schedule to keep the credential current.[^s4]

## Gotchas

- **Consulting, not configuring.** Questions ask which tool or design to recommend; build steps and code are out of scope.[^s1]
- **Know both runtimes.** The fundamentals section tests managed-package versus standard runtime and which upgrades need manual work.[^s1]
- **Business Rules Engine counts.** Expression Sets and Decision Matrices appear in the expected knowledge even though they have no section of their own.[^s1]

## Connections

- **broader → `kt:salesforce-certification-program`**: one of the consultant-tier credentials Trailhead lists in its catalogue.[^s2]
- **related → `kt:omnistudio`**: the toolset whose four components each get their own exam section.[^s1]
- **related → `kt:omnistudio-developer-certification`**: the build-focused sibling credential for the same toolset; the consultant exam explicitly leaves coding and configuration out.[^s1]
- **related → `kt:salesforce-industries`**: the guide frames Omnistudio around industry use cases and prebuilt industry processes.[^s1]
- **related → `kt:business-analyst`**: the trail targets the business analyst role, and the guide lists analysts among typical candidates.[^s1][^s3]
- **related → `kt:experience-cloud`**: the Experience Cloud lifecycle is expected knowledge, and the Summer '26 maintenance covered Omnistudio on LWR sites.[^s1][^s4]
- **dependsOn → `kt:business-rules-engine`**: candidates need the benefits, limits and basic builds of Expression Sets and Decision Matrices.[^s1]

## Sources
[^s1]: Salesforce Help, "Salesforce Certified Omnistudio Consultant Exam Guide". https://help.salesforce.com/s/articleView?id=005298970&language=en_US&type=1 (accessed 2026-11-18)
[^s2]: Trailhead, "Certification - Salesforce Certified Omnistudio Consultant". https://trailhead.salesforce.com/en/credentials/omnistudioconsultant (accessed 2026-11-18)
[^s3]: Trailhead, "Prepare for Your Salesforce Omnistudio Consultant Certification". https://trailhead.salesforce.com/content/learn/trails/prepare-for-your-salesforce-omnistudio-consultant-certification (accessed 2026-11-18)
[^s4]: Trailhead, "Maintain Your Omnistudio Consultant Certification for Summer '26". https://trailhead.salesforce.com/content/learn/modules/omnistudio-consultant-certification-maintenance-summer-26/maintain-your-omnistudio-consultant-certification-for-summer-26 (accessed 2026-11-18)
