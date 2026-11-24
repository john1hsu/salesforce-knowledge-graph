---
id: kt:fedramp-20x
type: ExternalConcept
title: FedRAMP 20x
aliases: [FedRAMP 20x Program, 20x certification path, FedRAMP 20x Certification]
domain: public-sector-and-compliance
summary: >-
  GSA's cloud-native, automation-first path to FedRAMP Certification, announced in March 2025, that replaces
  document-heavy control narratives with machine-readable Key Security Indicators validated continuously; it runs
  alongside the legacy Rev5 path and opened Classes A-C under the Consolidated Rules for 2026.
release: "Winter '27"
status: concept
broader: [kt:fedramp]
related: [kt:govramp, kt:soc-2, kt:authority-to-operate]
relations:
  - {predicate: dependsOn, object: kt:continuous-monitoring}
  - {predicate: hasPart, object: kt:key-security-indicators}
  - {predicate: contrastsWith, object: kt:fedramp-high}
sources:
  - id: s1
    title: "GSA announces FedRAMP 20x"
    publisher: US General Services Administration
    url: https://www.gsa.gov/about-us/newsroom/news-releases/gsa-announces-fedramp-20x-03242025
    type: government
    accessed: 2026-11-24
  - id: s2
    title: "FedRAMP 20x"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/20x
    type: government
    accessed: 2026-11-24
  - id: s3
    title: "Key Security Indicators - FedRAMP Consolidated Rules for 2026"
    publisher: FedRAMP (GSA)
    url: https://fedramp.gov/2026/providers/20x/key-security-indicators/
    type: government
    accessed: 2026-11-24
  - id: s4
    title: "FedRAMP Certification - FedRAMP Consolidated Rules for 2026"
    publisher: FedRAMP (GSA)
    url: https://www.fedramp.gov/2026/reference/fedramp-certification/
    type: government
    accessed: 2026-11-24
  - id: s5
    title: "FedRAMP Moderate (Compliance category page)"
    publisher: Salesforce
    url: https://compliance.salesforce.com/en/fedramp-moderate
    type: official-docs
    accessed: 2026-11-24
created: 2026-11-24
---

# FedRAMP 20x

FedRAMP 20x is the General Services Administration's effort to rebuild how cloud services earn FedRAMP Certification around automation rather than paperwork. GSA announced it on March 24, 2025 as a cloud-native approach to authorization, promising to cut manual documentation, let simple low-impact offerings proceed without a sponsoring agency, and bring most approvals down to a matter of weeks instead of years.[^s1] It is not a separate program: it is one of two certification paths inside FedRAMP, next to the legacy Rev5 path built on NIST control narratives.[^s2][^s4]

## How it works

Instead of asking a provider to prove it meets each listed control, 20x asks it to show that a set of security capabilities is working, using Key Security Indicators (KSIs) that give measurable, ongoing validation.[^s3] Providers are expected to collect evidence continuously, detect configuration drift, monitor how well protections perform, alert on deviations and report trends. Each KSI is documented in a Security Decision Record, and FedRAMP deliberately leaves the specific activities and numbers to the provider in most cases.[^s3] The KSIs are grouped into ten themes: change management; cloud-native architecture; cybersecurity education; identity and access management; incident response; monitoring, logging and auditing; policy and inventory; recovery planning; service configuration; and supply chain risk.[^s3]

A 20x applicant targets a certification profile and submits a package covering its offering overview, how each requirement or KSI is implemented, validated and assessed, and a real or example ongoing certification report. Machine-readable material must validate against FedRAMP's JSON schemas.[^s4] For Classes B, C and D the package needs an independent assessment by a FedRAMP Recognized assessor completed within the previous three months, and the package's status must have been verified within the previous seven days; a Marketplace listing comes before applying.[^s4] Class A accepts an existing credential from the past 12 months instead, such as a Rev5 authorization, a SOC 2 Type II report or a GovRAMP certification.[^s4]

## Phases and classes

FedRAMP has rolled 20x out in phases. Phase 1, a Low pilot from April to September 2025, received 26 complete packages and issued its first pilot authorizations in late July 2025. Phase 2, a Moderate pilot from November 2025 to March 2026, received 14 qualifying submissions and granted its first cohort pilot authorizations on March 6, 2026.[^s2] Phase 3 formalized the rules as the Consolidated Rules for 2026 and opened wide-scale adoption.[^s2] Under those rules, providers could adopt 20x from July 4, 2026, and ongoing-certification requirements apply from January 1, 2027.[^s4]

The FedRAMP 20x page lists Class A (for mature services new to the federal market), Class B (small-scale or light-use services) and Class C (common enterprise services likely used agency-wide) as available now. Class D, the High equivalent, is being developed in a later phase, and FedRAMP says it will stop accepting new Rev5 certifications on June 11, 2027, while flagging future dates as estimates.[^s2]

## Gotchas for Salesforce practitioners

- **Pick one path per offering.** A provider must not pursue both Rev5 and 20x certification for the same cloud offering.[^s4]
- **High workloads are not on 20x yet.** Class D is still being piloted, so High-impact environments still rely on the Rev5 path for now.[^s2]
- **Check each offering's listing.** Salesforce's compliance portal lists FedRAMP Moderate documents per offering (Slack, MuleSoft Government Cloud, OwnCompany), with no mention of 20x.[^s5]
- **Sponsorship rules changed.** GSA said simple, low-impact offerings no longer need a federal agency sponsor to start.[^s1]

## Connections

20x is a certification path within FedRAMP (`kt:fedramp`, broader).[^s2] It `hasPart` Key Security Indicators (`kt:key-security-indicators`) and `dependsOn` continuous monitoring (`kt:continuous-monitoring`), because KSIs are validated on an ongoing basis.[^s3] It `contrastsWith` FedRAMP High (`kt:fedramp-high`), whose Class D equivalent is not yet open under 20x.[^s2] SOC 2 (`kt:soc-2`) and GovRAMP (`kt:govramp`) are related as credentials Class A accepts.[^s4] An agency's authority to operate (`kt:authority-to-operate`) is related, since 20x aims to speed agency adoption.[^s1]

## Sources

[^s1]: US General Services Administration, "GSA announces FedRAMP 20x". https://www.gsa.gov/about-us/newsroom/news-releases/gsa-announces-fedramp-20x-03242025 (accessed 2026-11-24)
[^s2]: FedRAMP (GSA), "FedRAMP 20x". https://www.fedramp.gov/20x (accessed 2026-11-24)
[^s3]: FedRAMP (GSA), "Key Security Indicators - FedRAMP Consolidated Rules for 2026". https://fedramp.gov/2026/providers/20x/key-security-indicators/ (accessed 2026-11-24)
[^s4]: FedRAMP (GSA), "FedRAMP Certification - FedRAMP Consolidated Rules for 2026". https://www.fedramp.gov/2026/reference/fedramp-certification/ (accessed 2026-11-24)
[^s5]: Salesforce, "FedRAMP Moderate" compliance category. https://compliance.salesforce.com/en/fedramp-moderate (accessed 2026-11-24)
