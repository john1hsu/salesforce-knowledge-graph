---
id: kt:key-security-indicators
type: ExternalConcept
title: Key Security Indicators
aliases: [KSIs, FedRAMP KSIs, FedRAMP Key Security Indicators, 20x Key Security Indicators]
domain: public-sector-and-compliance
summary: >-
  The outcome-based security capabilities that FedRAMP 20x asks cloud providers to demonstrate and validate
  persistently, largely through automation, instead of writing narrative descriptions of each NIST SP 800-53
  control; grouped into ten themes such as IAM, change management and supply chain risk.
release: "Winter '27"
status: concept
broader: [kt:fedramp-20x]
related: [kt:fedramp, kt:nist-sp-800-53, kt:multi-factor-authentication]
relations:
  - {predicate: partOf, object: kt:fedramp-20x}
  - {predicate: dependsOn, object: kt:continuous-monitoring}
sources:
  - id: s1
    title: "Key Security Indicators - FedRAMP Consolidated Rules for 2026 (providers)"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/2026/providers/20x/key-security-indicators/
    type: government
    accessed: 2026-11-24
  - id: s2
    title: "Key Security Indicators - FedRAMP Consolidated Rules for 2026 (20x Class C reference)"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/2026/reference/20x/c/key-security-indicators/
    type: government
    accessed: 2026-11-24
  - id: s3
    title: "FedRAMP Key Security Indicators (20x Phase One, release 25.05C)"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/docs/20x/phase1/key-security-indicators/
    type: government
    accessed: 2026-11-24
  - id: s4
    title: "RFC-0014 Phase Two Key Security Indicators"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/rfcs/0014/
    type: government
    accessed: 2026-11-24
  - id: s5
    title: "Deep dive into FedRAMP 20x Key Security Indicators: Decoding the 63 KSIs"
    publisher: Amazon Web Services (AWS Public Sector Blog)
    url: https://aws.amazon.com/blogs/publicsector/deep-dive-into-fedramp-20x-key-security-indicators-decoding-the-63-ksis/
    type: partner
    accessed: 2026-11-24
created: 2026-11-24
---

# Key Security Indicators

Key Security Indicators (KSIs) are the building blocks of FedRAMP 20x. Rather than asking a cloud service provider to describe in prose how it satisfies each security control, FedRAMP asks it to show that a set of security capabilities is actually working, and to keep showing it: KSIs are meant to support continuous evidence collection, detection of configuration drift and monitoring of how well protections perform.[^s1] FedRAMP deliberately avoids prescribing specific tools or thresholds in most cases. Instead, the provider documents, in a Security Decision Record, the minimum information and artifacts it uses for each indicator, and is encouraged to measure things its own business cares about.[^s1]

## Structure

Under the FedRAMP Consolidated Rules for 2026, KSIs are grouped into ten themes: Cybersecurity Education (CED), Change Management (CMT), Cloud Native Architecture (CNA), Identity and Access Management (IAM), Incident Response (INR), Monitoring, Logging and Auditing (MLA), Policy and Inventory (PIY), Recovery Planning (RPL), Supply Chain Risk (SCR) and Service Configuration (SVC).[^s1][^s2] Each indicator on the reference pages has an ID, a changelog, a short outcome statement, its related NIST SP 800-53 controls and links to defined terms.[^s2] Examples from the Class C reference include KSI-CMT-LMC, which requires changes to the offering to be logged and monitored; KSI-CMT-RMV, which prefers redeploying version-controlled resources over modifying them in place; and KSI-IAM-AAM, which requires account, role and group lifecycles to be managed through automation.[^s2] The changelogs date the official launch of the 2026 rules to June 24, 2026, with control-mapping updates added in October 2026.[^s2]

## Evolution

The first published set served the 20x Phase One pilot for Low, cloud-native offerings. That release (25.05C, published June 28, 2025) listed 51 KSIs across ten themes with two-digit IDs such as KSI-IAM-01, which required phishing-resistant multi-factor authentication for all user authentication; its third-party theme was called Third-Party Information Resources (TPR) and its incident theme Incident Reporting.[^s3] FedRAMP now keeps that page only for reference.[^s3] RFC-0014 proposed the Phase Two set for Low and Moderate: it added new indicators (some Moderate-only), retired several that were superseded, renamed the incident theme to Incident Response, and published a Moderate mapping from each KSI to SP 800-53 controls to support automated comparison.[^s4] It also warned that Moderate providers would be expected to show automated validation, and that simply adopting the new indicators would not be enough.[^s4]

## Validation and automation in practice

AWS's April 2026 analysis counted 63 KSIs across 12 themes, a larger tally than the ten themes on FedRAMP's provider page, and sorted them into indicators that are fully automatable (for example, MFA enforcement), ones that are mainly process and documentation (such as after-action reviews), and mixed ones.[^s5] It reported that the Phase Two pilot required automated validation for at least 70% of KSIs, evidence in both human-readable and machine-readable form, and, for Moderate, validation of machine-based indicators at least every three days.[^s5] Practitioners should check FedRAMP's current pages before relying on any count or threshold, because the indicator set has changed between phases.[^s3][^s4]

## Why it matters for Salesforce practitioners

KSIs describe outcomes for the cloud provider's whole offering, so they matter most to teams preparing or reviewing a 20x package for a Salesforce-hosted or Salesforce-adjacent service. Several themes line up with controls a Salesforce org already exposes, such as phishing-resistant MFA under IAM and change logging under CMT.[^s2][^s3] A customer's own configuration does not earn a FedRAMP certification, though; KSIs are assessed for the provider's cloud service offering.[^s1]

## Connections

KSIs are `partOf` FedRAMP 20x (`kt:fedramp-20x`, broader), which replaces control narratives with these indicators, and they sit within the wider FedRAMP program (`kt:fedramp`).[^s1] They map back to NIST SP 800-53 controls (`kt:nist-sp-800-53`) even though they are written as outcomes.[^s2][^s4] They `dependsOn` continuous monitoring (`kt:continuous-monitoring`), since validation is persistent rather than point-in-time.[^s1][^s5] Multi-factor authentication (`kt:multi-factor-authentication`) is related because phishing-resistant MFA is a core IAM indicator.[^s3]

## Sources

[^s1]: FedRAMP (GSA), "Key Security Indicators - FedRAMP Consolidated Rules for 2026" (providers). https://www.fedramp.gov/2026/providers/20x/key-security-indicators/ (accessed 2026-11-24)
[^s2]: FedRAMP (GSA), "Key Security Indicators - FedRAMP Consolidated Rules for 2026" (20x Class C reference). https://www.fedramp.gov/2026/reference/20x/c/key-security-indicators/ (accessed 2026-11-24)
[^s3]: FedRAMP (GSA), "FedRAMP Key Security Indicators" (20x Phase One, release 25.05C). https://www.fedramp.gov/docs/20x/phase1/key-security-indicators/ (accessed 2026-11-24)
[^s4]: FedRAMP (GSA), "RFC-0014 Phase Two Key Security Indicators". https://www.fedramp.gov/rfcs/0014/ (accessed 2026-11-24)
[^s5]: Paul Keastead and Tommy Kromer, AWS Public Sector Blog, "Deep dive into FedRAMP 20x Key Security Indicators: Decoding the 63 KSIs" (2026-04-27). https://aws.amazon.com/blogs/publicsector/deep-dive-into-fedramp-20x-key-security-indicators-decoding-the-63-ksis/ (accessed 2026-11-24)
