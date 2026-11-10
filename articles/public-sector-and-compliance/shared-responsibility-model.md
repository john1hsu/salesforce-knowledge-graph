---
id: kt:shared-responsibility-model
type: Concept
title: Shared Responsibility Model
aliases: [cloud shared responsibility model, shared security responsibility, security of the cloud vs security in the cloud]
domain: public-sector-and-compliance
summary: >-
  The cloud security principle that the provider and the customer each own a defined part of security and
  compliance: on Salesforce, the provider secures the infrastructure and platform, while the customer secures
  its own users, configuration and data.
release: "Winter '27"
status: concept
broader: [kt:cloud-computing]
related: [kt:platform-as-a-service, kt:data-breach-risk, kt:multi-factor-authentication, kt:salesforce-shield]
relations:
  - {predicate: consumedBy, object: kt:fedramp}
  - {predicate: consumedBy, object: kt:dod-cloud-computing-srg}
sources:
  - id: s1
    title: "Security as a Shared Responsibility Between Provider and Customer"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/shared-responsibility-model/
    type: official-blog
    accessed: 2026-11-10
  - id: s2
    title: "Security Perspective on the Shared Responsibility Model"
    publisher: Salesforce Compliance Portal
    url: https://compliance.salesforce.com/documents/a006e000010nW2FAAU
    type: official-docs
    accessed: 2026-11-10
  - id: s3
    title: "General Access Control Guidance for Cloud Systems (NIST SP 800-210)"
    publisher: National Institute of Standards and Technology
    url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-210.pdf
    type: standards-body
    accessed: 2026-11-10
  - id: s4
    title: "Who is responsible for the cloud security controls?"
    publisher: FedRAMP (GSA)
    url: https://help.fedramp.gov/hc/en-us/articles/27700955089563-Who-is-responsible-for-the-cloud-security-controls
    type: government
    accessed: 2026-11-10
  - id: s5
    title: "Improve Your Org's Security with Salesforce Health Check (Security Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/security_basics/security_basics_healthcheck
    type: official-learning
    accessed: 2026-11-10
  - id: s6
    title: "Learn About the Shared Responsibility Model (AWS Cloud Security)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/aws-cloud-security/learn-about-the-shared-responsibility-model
    type: official-learning
    accessed: 2026-11-10
created: 2026-11-10
---

# Shared Responsibility Model

The shared responsibility model is the principle that, in a cloud service, security and compliance are split between the provider and the customer, with each side owning a different part of the work.[^s1][^s6] Salesforce describes its version plainly: Salesforce protects the infrastructure and platform, and the customer protects its own data, configuration and user access.[^s1] The major infrastructure clouds use the same model, though each draws the line in a slightly different place.[^s1]

## How the split works

A common shorthand separates security *of* the cloud from security *in* the cloud. In Trailhead's AWS unit, the provider secures the compute, storage, network, facilities, host operating systems and virtualization layer, while the customer secures its data, applications, configurations and who can reach its content.[^s6]

Where the line falls depends on the service model. NIST SP 800-210 explains that in IaaS the consumer controls access in the operating system, middleware, application and data layers; in PaaS the provider's administrators handle access control from the runtime down, and consumer developers may share some of it; in SaaS the provider covers every layer except the consumer's application data.[^s3] The same guidance says provider administrators should not have access to consumer data, and that the consumer should be told at once if unencrypted data is exposed to them.[^s3] Salesforce sits mostly at the SaaS and PaaS end, so most of the stack is the provider's job, but the data and how it is exposed remain the customer's.[^s3][^s1]

## Salesforce's three layers

Salesforce frames the model as three layers of controls:[^s1]

- **Foundationals** — protections built into Salesforce's infrastructure and platform, managed by Salesforce and always on.[^s1]
- **Configurables** — built-in settings each customer must turn on and tune, such as MFA and SSO, least-privilege permission sets, Login History review and login IP restrictions on profiles.[^s1]
- **Enhanceables** — optional paid add-ons for higher needs: Shield, Security Center, Privacy Center, Data Mask & Seed, Archive, and Backup & Recover.[^s1]

Salesforce also publishes a security whitepaper on the model in its compliance portal. It says Salesforce, as a data processor, applies measures to protect customer data, while customers and partners must review the available controls and secure their own orgs to meet their security, contractual and regulatory duties.[^s2] The whitepaper covers a wide range of services, from Agentforce and Data Cloud to MuleSoft, Heroku, Slack and the Government Cloud Plus offerings.[^s2]

## Putting it into practice

The customer's half is mostly configuration, and Health Check is the built-in tool for measuring it. It lists an org's security settings on one page in Setup, compares them with Salesforce's recommended baseline (or a custom baseline imported as XML), and scores the result from 0 to 100.[^s5] Trailhead advises testing changes that affect user access or integrations in a sandbox first, and agreeing any custom baseline with IT or compliance teams.[^s5]

A practical gotcha: a provider's certifications do not cover the customer's half. A strong platform attestation says nothing about whether an org enforces MFA, over-assigns admin rights or leaves risky settings at weak values; those are configurables the customer owns.[^s1][^s5]

## In compliance programmes

Regulated buyers make the split explicit. FedRAMP requires a provider to submit a Control Implementation Summary / Customer Responsibility Matrix workbook as Appendix J to its System Security Plan.[^s4] The workbook marks each control as implemented by the provider, by the customer, shared by both, or inherited from an underlying FedRAMP-authorized IaaS or PaaS, and describes what the customer must do for its part.[^s4] An agency reusing a provider's authorization still has to implement and evidence the customer-owned controls itself.[^s4]

## Connections

The model sits under cloud computing (`kt:cloud-computing`), since it follows from renting a provider's stack rather than running your own, and its split varies with the platform-as-a-service (`kt:platform-as-a-service`) and SaaS models.[^s3] Data breach risk (`kt:data-breach-risk`) is largely the customer's half of the model, and multi-factor authentication (`kt:multi-factor-authentication`) is the first configurable Salesforce lists.[^s1] Salesforce Shield (`kt:salesforce-shield`) is the leading example of an enhanceable add-on.[^s1] FedRAMP (`kt:fedramp`) consumes the model through its customer responsibility matrix, and the DoD Cloud Computing SRG (`kt:dod-cloud-computing-srg`) applies the same idea to mission owners.[^s4]

## Sources

[^s1]: Salesforce, "Security as a Shared Responsibility Between Provider and Customer". https://www.salesforce.com/blog/shared-responsibility-model/ (accessed 2026-11-10)
[^s2]: Salesforce Compliance Portal, "Security Perspective on the Shared Responsibility Model". https://compliance.salesforce.com/documents/a006e000010nW2FAAU (accessed 2026-11-10)
[^s3]: NIST, "General Access Control Guidance for Cloud Systems", SP 800-210 (July 2020). https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-210.pdf (accessed 2026-11-10)
[^s4]: FedRAMP, "Who is responsible for the cloud security controls?". https://help.fedramp.gov/hc/en-us/articles/27700955089563-Who-is-responsible-for-the-cloud-security-controls (accessed 2026-11-10)
[^s5]: Trailhead, "Improve Your Org's Security with Salesforce Health Check" (Security Basics). https://trailhead.salesforce.com/content/learn/modules/security_basics/security_basics_healthcheck (accessed 2026-11-10)
[^s6]: Trailhead, "Learn About the Shared Responsibility Model" (AWS Cloud Security). https://trailhead.salesforce.com/en/content/learn/modules/aws-cloud-security/learn-about-the-shared-responsibility-model (accessed 2026-11-10)
