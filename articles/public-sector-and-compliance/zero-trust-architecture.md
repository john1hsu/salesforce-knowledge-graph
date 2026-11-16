---
id: kt:zero-trust-architecture
type: ExternalConcept
title: Zero Trust Architecture
aliases: [zero trust, ZTA, "NIST SP 800-207", zero trust security model, never trust always verify]
domain: public-sector-and-compliance
summary: >-
  A security architecture, defined by NIST SP 800-207, that grants no implicit trust based on network
  location and instead authenticates, authorizes and continually re-evaluates every access request to each
  resource; US federal agencies were directed toward it by OMB M-22-09, and it shapes how Salesforce orgs
  and Salesforce's own Hyperforce infrastructure are secured.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:nist-sp-800-53, kt:shared-responsibility-model, kt:hyperforce]
relations:
  - {predicate: hasPart, object: kt:principle-of-least-privilege}
  - {predicate: hasPart, object: kt:multi-factor-authentication}
  - {predicate: hasPart, object: kt:mutual-tls-authentication}
sources:
  - id: s1
    title: "Zero Trust Architecture (NIST SP 800-207)"
    publisher: NIST
    url: https://www.nist.gov/publications/zero-trust-architecture
    type: standards-body
    accessed: 2026-11-16
  - id: s2
    title: "NIST Special Publication 800-207, Zero Trust Architecture (PDF)"
    publisher: NIST
    url: https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf
    type: standards-body
    accessed: 2026-11-16
  - id: s3
    title: "M-22-09, Moving the U.S. Government Toward Zero Trust Cybersecurity Principles"
    publisher: Office of Management and Budget, The White House
    url: https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf
    type: government
    accessed: 2026-11-16
  - id: s4
    title: "Identify Technologies Behind Zero Trust (Zero Trust Security Model module)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/zero-trust-security-model/identify-technologies-behind-zero-trust
    type: official-learning
    accessed: 2026-11-16
  - id: s5
    title: "Behind the Zero-Trust Infrastructure Powering Agentforce 360 Platform, Protecting 20 Trillion Transactions"
    publisher: Salesforce Engineering
    url: https://engineering.salesforce.com/behind-the-zero-trust-infrastructure-powering-agentforce-360-platform-protecting-20-trillion-transactions/
    type: official-blog
    accessed: 2026-11-16
  - id: s6
    title: "Enhance Integration Security with mTLS for Salesforce and MuleSoft"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/10/enhance-integration-security-with-mtls-for-salesforce-and-mulesoft
    type: official-blog
    accessed: 2026-11-16
created: 2026-11-16
---

# Zero Trust Architecture

Zero trust (ZT) is NIST's name for an evolving set of cybersecurity paradigms that move defenses away from static, network-based perimeters and toward users, assets and resources; a zero trust architecture (ZTA) is an enterprise plan that applies those principles to infrastructure and workflows.[^s1] The core idea is that no asset or user account receives implicit trust because of its physical or network location or because the enterprise owns it, so protection centers on individual resources rather than network segments.[^s1] The reference text is NIST Special Publication 800-207, published in August 2020 by Scott Rose, Oliver Borchert, Stuart Mitchell and Sean Connelly and updated in March 2021.[^s1] For Salesforce practitioners it matters twice over: public sector customers must show how a SaaS org fits their agency's ZTA, and Salesforce describes its own Hyperforce infrastructure in zero trust terms.[^s3][^s5]

## The seven tenets

SP 800-207 frames ZT as seven tenets: every data source and computing service is a resource; all communication is secured regardless of network location; access to each resource is granted per session with least privilege; access follows dynamic policy that weighs identity, asset state, behavior and environment; the enterprise monitors the integrity and posture of all its assets; authentication and authorization are dynamic, strictly enforced and continually re-evaluated; and the enterprise gathers as much data as it can about assets, network and communications to improve its posture.[^s2]

## How it works

NIST splits the access decision into logical components. A **policy engine** decides whether to grant, deny or revoke access, feeding enterprise policy and external signals such as threat intelligence into a trust algorithm; a **policy administrator** opens or closes the path between subject and resource and issues session credentials; together they form the policy decision point. A **policy enforcement point** enables, monitors and terminates each connection.[^s2] The publication describes three ways to build this: enhanced identity governance (policy keyed to the subject's identity and attributes), micro-segmentation (resources behind gateway enforcement points), and software-defined perimeters on a network overlay.[^s2] NIST notes that the identity-driven approach suits SaaS offerings where customers cannot run their own ZT components, which is the usual situation for a Salesforce org.[^s2]

Salesforce's Trailhead treatment lists the same building blocks in practical terms: identity and access management through a central identity provider, MFA on each request for protected data, granular access based on identity, device and context, least privilege, device inventory and management, and continuous monitoring with a SIEM.[^s4] It also advises starting from the most critical data and assets, since they define the attack surface where policies matter first.[^s4]

## Federal mandate

OMB memorandum M-22-09, issued on 26 January 2022 to implement Executive Order 14028, set federal zero trust goals to be met by the end of fiscal year 2024.[^s3] It adopts the pillars of CISA's Zero Trust Maturity Model: identity (enterprise-managed identities and phishing-resistant MFA), devices (complete inventories and endpoint detection and response), networks (encrypted DNS and HTTP traffic), applications and workloads (treat every application as internet-connected) and data (categorization, access auditing and enterprise logging).[^s3] It also tells agencies to enforce MFA at the application layer rather than the network layer and to drop password rules that force special characters or regular rotation.[^s3] The memo calls itself a starting point and refers agencies to SP 800-207 for architecture detail.[^s3]

## Zero trust and Salesforce

- **Platform side.** Salesforce Engineering describes Hyperforce as using a service mesh in which mutual TLS protects every service-to-service call, with cells and service boundaries limiting the blast radius of a failure.[^s5]
- **Integration side.** Salesforce's developer guidance presents inbound mutual TLS, paired with an API-only integration user and the OAuth JWT bearer flow, as an integration pattern consistent with zero trust.[^s6]
- **Customer side.** Because the identity-centric model is the one that fits SaaS, a customer's ZTA for Salesforce rests mainly on identity, MFA, least-privilege access and monitoring rather than on network location.[^s2][^s4]

## Connections

ZTA sits under security compliance frameworks (`kt:security-compliance-frameworks`) as the architectural model federal agencies must report against.[^s3] It `hasPart` the principle of least privilege (`kt:principle-of-least-privilege`), which SP 800-207 builds into its per-session access tenet.[^s2] It `hasPart` multi-factor authentication (`kt:multi-factor-authentication`), the identity-pillar control M-22-09 requires in phishing-resistant form.[^s3] It `hasPart` mutual TLS authentication (`kt:mutual-tls-authentication`), which secures communication independent of network location both inside Hyperforce and for integrations.[^s5][^s6] It is related to NIST SP 800-53 (`kt:nist-sp-800-53`), the control catalog behind federal systems, and to the shared responsibility model (`kt:shared-responsibility-model`), since Salesforce secures the platform while customers enforce ZT policy on identities and data.[^s2][^s5] It is related to Hyperforce (`kt:hyperforce`), the infrastructure Salesforce describes as zero trust by default.[^s5]

## Sources
[^s1]: NIST, "Zero Trust Architecture (NIST SP 800-207)". https://www.nist.gov/publications/zero-trust-architecture (accessed 2026-11-16)
[^s2]: NIST, "NIST Special Publication 800-207, Zero Trust Architecture (PDF)". https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf (accessed 2026-11-16)
[^s3]: OMB, "M-22-09, Moving the U.S. Government Toward Zero Trust Cybersecurity Principles". https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf (accessed 2026-11-16)
[^s4]: Salesforce Trailhead, "Identify Technologies Behind Zero Trust". https://trailhead.salesforce.com/content/learn/modules/zero-trust-security-model/identify-technologies-behind-zero-trust (accessed 2026-11-16)
[^s5]: Salesforce Engineering, "Behind the Zero-Trust Infrastructure Powering Agentforce 360 Platform, Protecting 20 Trillion Transactions". https://engineering.salesforce.com/behind-the-zero-trust-infrastructure-powering-agentforce-360-platform-protecting-20-trillion-transactions/ (accessed 2026-11-16)
[^s6]: Salesforce Developers Blog, "Enhance Integration Security with mTLS for Salesforce and MuleSoft". https://developer.salesforce.com/blogs/2025/10/enhance-integration-security-with-mtls-for-salesforce-and-mulesoft (accessed 2026-11-16)
