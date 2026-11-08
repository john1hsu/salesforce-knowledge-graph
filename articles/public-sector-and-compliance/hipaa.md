---
id: kt:hipaa
type: ExternalConcept
title: HIPAA
aliases: [Health Insurance Portability and Accountability Act, HIPAA Security Rule, HIPAA compliance on Salesforce, Salesforce Business Associate Addendum, Salesforce HIPAA BAA]
domain: public-sector-and-compliance
summary: >-
  The US health-privacy law whose Privacy and Security Rules govern protected health information (PHI); Salesforce
  supports HIPAA workloads by signing a Business Associate Addendum (BAA) for a published list of covered services,
  subject to service-specific restrictions and customer encryption obligations.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:health-cloud, kt:salesforce-shield, kt:event-monitoring, kt:einstein-trust-layer, kt:government-cloud-plus, kt:slack-platform]
relations:
  - {predicate: mitigates, object: kt:data-breach-risk}
  - {predicate: dependsOn, object: kt:shield-platform-encryption}
  - {predicate: contrastsWith, object: kt:soc-2}
sources:
  - id: s1
    title: "HIPAA — Salesforce Compliance"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/hipaa
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Business Associate Addendum Restrictions"
    publisher: Salesforce
    url: https://www.salesforce.com/company/legal/business-associate-addendum/
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Guidance on HIPAA & Cloud Computing"
    publisher: U.S. Department of Health and Human Services
    url: https://www.hhs.gov/hipaa/for-professionals/special-topics/cloud-computing
    type: government
    accessed: 2026-11-08
  - id: s4
    title: "Overview of the HIPAA Security Rule"
    publisher: Military Health System (health.mil)
    url: https://health.mil/Reference-Center/Fact-Sheets/2014/12/17/Info-Paper-Overview-of-the-HIPAA-Security-Rule
    type: government
    accessed: 2026-11-08
  - id: s5
    title: "Protect Your Health Data with Salesforce Shield (Health Cloud Administration)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.health_cloud.meta/null/admin_salesforce_shield.htm
    type: official-docs
    accessed: 2026-11-08
created: 2026-11-08
---

# HIPAA

HIPAA, the US Health Insurance Portability and Accountability Act, is the regulatory regime behind most healthcare and life-sciences Salesforce implementations in the United States. Its Privacy Rule protects individually identifiable health information held by covered entities and gives patients rights over that information.[^s1] Its Security Rule, codified at 45 CFR Parts 160, 162 and 164, applies to the electronic subset of that information (ePHI) and adds protection of integrity and availability to confidentiality.[^s4] For an architect the practical question is narrower: which Salesforce services may hold PHI, under what contract, and with which configuration duties left to the customer.

## The Security Rule in brief

Covered entities and their business associates must protect ePHI against reasonably anticipated threats, and their workforces must comply.[^s4] The rule groups its standards into three safeguard families: administrative (policies, procedures and workforce management), physical (protecting systems, buildings and equipment) and technical (technology and policies that control access to ePHI), set out in sections 164.308, 164.310 and 164.312 respectively.[^s4]

## Cloud providers are business associates

HHS guidance states that a cloud service provider that creates, receives, maintains or transmits ePHI on a customer's behalf is itself a business associate, even if it only stores encrypted data and holds no decryption key.[^s3] The narrow conduit exception covers only transmission services with transient storage, so it does not fit a CRM that retains records.[^s3] A covered entity must therefore sign a business associate agreement with the provider before ePHI goes into the service; using a provider without one is a violation.[^s3] Both parties perform risk analyses of the cloud arrangement and should document in writing which party owns each Security Rule requirement.[^s3] Storing ePHI outside the US is not prohibited, but location-specific risks belong in the risk analysis.[^s3]

## How Salesforce handles it

Salesforce customers building HIPAA-regulated solutions request a Business Associate Addendum (BAA) through their account representative.[^s1] Coverage is conditional: the signed BAA must name the specific service, and the customer must follow Salesforce's published BAA Restrictions article, with the BAA prevailing if the two conflict.[^s2] The restrictions article, last updated 30 September 2026 at the time of writing, lists covered services including Sales Cloud, Service Cloud, Experience Cloud, Lightning Platform, Health Cloud, Life Sciences Cloud, Salesforce Shield, Data 360, CRM Analytics, Marketing Cloud Engagement, MuleSoft, Tableau Cloud and Slack Enterprise plans, many with service-specific conditions.[^s2] It explicitly excludes on-premises deployments, Tableau Server and Tableau Bridge, among others.[^s2]

The customer, not Salesforce, must encrypt PHI it transmits through covered services and, as far as it controls, PHI stored in them, following HHS guidance on rendering PHI unusable to unauthorized people.[^s2] Salesforce positions Shield here: Health Cloud documentation says Shield Platform Encryption encrypts sensitive data at rest to help address HIPAA storage requirements while keeping search, workflow and validation rules working, and Event Monitoring shows who accessed critical data, when and from where.[^s5] Salesforce also publishes a whitepaper mapping its services to the Security Rule, alongside separate ones for Slack and Tableau Cloud.[^s1]

## Gotchas for architects

- **Service-by-service scope.** A BAA covers named services, not "Salesforce". Check every cloud, add-on and integration in the design against the current restrictions list.[^s2]
- **AI features carry conditions.** Einstein and Agentforce services may not be used as a medical device or to infer a person's diagnosis or eligibility, and Prompt Builder and Agentforce require Data Masking in the Einstein Trust Layer where the customer controls it.[^s2]
- **Feature-level exclusions.** Einstein Bots utterance records must not contain PHI, and the Lightning Platform Discover feature must not be enabled where it could touch PHI.[^s2]
- **Slack rules are strict.** Patients may not be added as users or guests, and PHI is barred from user profiles, custom statuses, workspace names and support requests.[^s2]
- **Third parties are yours.** Telephony, e-signature and LLM providers wired into covered services must themselves meet HIPAA requirements.[^s2]

## Connections

HIPAA sits under security compliance frameworks (`kt:security-compliance-frameworks`) as the US healthcare-specific regime.[^s4] It `dependsOn` Shield Platform Encryption (`kt:shield-platform-encryption`) in practice because the BAA puts encryption of PHI on the customer, and Shield (`kt:salesforce-shield`) and Event Monitoring (`kt:event-monitoring`) supply the encryption and access-audit evidence.[^s2][^s5] Health Cloud (`kt:health-cloud`) is the industry cloud most often deployed under a BAA.[^s5] The Einstein Trust Layer (`kt:einstein-trust-layer`) matters because Data Masking is a condition for AI features.[^s2] Government Cloud Plus (`kt:government-cloud-plus`) and Slack (`kt:slack-platform`) each carry their own BAA conditions.[^s2] HIPAA `mitigates` data breach risk (`kt:data-breach-risk`) through its safeguard requirements.[^s3] It `contrastsWith` SOC 2 (`kt:soc-2`): SOC 2 is an attestation report about a provider's controls, whereas HIPAA is a law that binds both the provider and the customer through a signed agreement.[^s3]

## Sources
[^s1]: Salesforce, "HIPAA — Salesforce Compliance". https://compliance.salesforce.com/en/hipaa (accessed 2026-11-08)
[^s2]: Salesforce, "Business Associate Addendum Restrictions". https://www.salesforce.com/company/legal/business-associate-addendum/ (accessed 2026-11-08)
[^s3]: U.S. Department of Health and Human Services, "Guidance on HIPAA & Cloud Computing". https://www.hhs.gov/hipaa/for-professionals/special-topics/cloud-computing (accessed 2026-11-08)
[^s4]: Military Health System, "Overview of the HIPAA Security Rule". https://health.mil/Reference-Center/Fact-Sheets/2014/12/17/Info-Paper-Overview-of-the-HIPAA-Security-Rule (accessed 2026-11-08)
[^s5]: Salesforce, "Protect Your Health Data with Salesforce Shield (Health Cloud Administration)". https://developer.salesforce.com/docs/atlas.en-us.health_cloud.meta/null/admin_salesforce_shield.htm (accessed 2026-11-08)
