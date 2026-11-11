---
id: kt:continuous-monitoring
type: ExternalConcept
title: Continuous Monitoring
aliases: [ConMon, information security continuous monitoring, ISCM, NIST SP 800-137, collaborative continuous monitoring]
domain: public-sector-and-compliance
summary: >-
  The ongoing, largely automated practice of tracking assets, vulnerabilities, threats and control effectiveness after
  a system is authorized, defined by NIST SP 800-137 and operationalized by FedRAMP; it is what keeps an Authority to
  Operate for a Salesforce government cloud deployment valid over time.
release: "Winter '27"
status: concept
broader: [kt:nist-risk-management-framework, kt:security-compliance-frameworks]
related: [kt:fisma, kt:fedramp, kt:event-monitoring, kt:security-center]
relations:
  - {predicate: dependsOn, object: kt:nist-sp-800-53}
  - {predicate: enables, object: kt:authority-to-operate}
sources:
  - id: s1
    title: "SP 800-137, Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/sp/800/137/final
    type: standards-body
    accessed: 2026-11-11
  - id: s2
    title: "SP 800-137A, Assessing Information Security Continuous Monitoring (ISCM) Programs"
    publisher: NIST
    url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-137A.pdf
    type: standards-body
    accessed: 2026-11-11
  - id: s3
    title: "Continuous Monitoring: Vulnerability Scanning (legacy playbook)"
    publisher: FedRAMP (GSA)
    url: https://fedramp.gov/legacy/playbook/csp/continuous-monitoring/vulnerability-scanning/
    type: government
    accessed: 2026-11-11
  - id: s4
    title: "Collaborative Continuous Monitoring — Rev5 provider rules (Consolidated Rules for 2026)"
    publisher: FedRAMP (GSA)
    url: https://fedramp.gov/2026/providers/rev5/rules/collaborative-continuous-monitoring/
    type: government
    accessed: 2026-11-11
  - id: s5
    title: "Learn the Core Concepts of Event Monitoring"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/event-monitoring-basics/learn-the-core-concepts-of-event-monitoring
    type: official-learning
    accessed: 2026-11-11
  - id: s6
    title: "Learn About Security Center"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/security-center/learn-about-security-center
    type: official-learning
    accessed: 2026-11-11
created: 2026-11-11
---

# Continuous Monitoring

Continuous monitoring (often shortened to **ConMon**, and formally **information security continuous monitoring**, ISCM) is the discipline of keeping an up-to-date view of a system's assets, threats, vulnerabilities and the effectiveness of its security controls, so that risk decisions are made on current evidence rather than on a point-in-time assessment.[^s1] NIST published the governing guidance, SP 800-137, in September 2011; it frames ISCM as the way an organization shows that its implemented controls still match its risk tolerance and gets information quickly enough to respond when they don't.[^s1] For Salesforce practitioners in the public sector, ConMon is the phase that begins the day an agency grants an Authority to Operate, and it applies both to the cloud provider and to the agency's own configuration of the org.

## How it works

SP 800-137 describes ISCM as a six-step cycle: define a strategy based on risk tolerance; establish the program (metrics, monitoring frequencies, technical architecture); implement it and collect data; analyze and report findings; respond by mitigating, accepting, transferring or avoiding the risk; and review and update the program.[^s2] The output that matters is security-related information gathered from every system and its environment and presented so that leaders can act on it.[^s2] NIST allows manual and automated methods, but expects manual steps to be repeatable and recommends automating collection, analysis and reporting wherever possible.[^s2] A companion publication, SP 800-137A (May 2020), gives a method for assessing whether an ISCM program itself is complete and effective, focusing on governance and structure rather than on individual tools.[^s2]

## Continuous monitoring under FedRAMP

FedRAMP turns the NIST concept into concrete, recurring deliverables for cloud providers such as Salesforce. Under the legacy Rev5 playbook, operating-system, web-application and database scans run at least monthly, with scanner signatures updated before each deliverable.[^s3] Each month the provider submits machine-readable scan results covering findings rated low and above, an automated in-boundary asset inventory mapped to those findings, and a Plan of Action and Milestones (POA&M) in which every unique vulnerability is its own item rather than being grouped.[^s3] Risk is scored with the CVSSv3 base score where available, and configuration changes beyond routine patching need notification and approval from the authorizing official.[^s3] FedRAMP marks that playbook as reference material during the move to its Consolidated Rules for 2026.[^s3]

The 2026 rules add **Collaborative Continuous Monitoring**. Providers publish an Ongoing Certification Report every 3 months covering changes and planned changes, accepted vulnerabilities, transformative changes, the agencies using the offering, and reportable incidents (or an attestation that there were none).[^s4] A synchronous quarterly review follows each report; it is optional for Class A, recommended for Class B and required for Classes C and D, and should be held 3 to 10 business days after the report.[^s4] The rules map to SP 800-53 control CA-7, list initial certification under them from 2027-01-01, and set a grace period ending 2027-10-01.[^s4]

## Monitoring the customer side in Salesforce

Provider ConMon covers the platform, but an agency's ATO also depends on monitoring its own org. Event Monitoring supplies the raw evidence: daily event log files (hourly with a Shield or Event Monitoring license), queryable event log objects, real-time event streams and threat detection.[^s5] Free orgs get a core set of event types and one day of history; the paid license unlocks more than 70 event types and up to 30 days of retention.[^s5] Security Center adds posture tracking across orgs: a parent tenant aggregates child tenants' metrics such as permission assignments, installed packages and Health Check scores, keeps up to 6 months of trend data, and raises threshold alerts by email or in-app.[^s6]

## Gotchas

ConMon is not a single tool or report; it is a program whose frequencies are set by risk, so a monthly scan cadence that satisfies FedRAMP may still be too slow for high-risk events like mass report exports.[^s2][^s5] Inheriting a provider's ConMon does not cover customer-controlled settings, which is why org-level telemetry matters.[^s6]

## Connections

Continuous monitoring is the final, ongoing step of the NIST Risk Management Framework (`kt:nist-risk-management-framework`) and sits under security compliance frameworks (`kt:security-compliance-frameworks`).[^s1] It `dependsOn` the SP 800-53 control catalog (`kt:nist-sp-800-53`), specifically CA-7, and `enables` the Authority to Operate (`kt:authority-to-operate`) by keeping its risk picture current.[^s4] It is related to FISMA (`kt:fisma`), the federal security statute, and made concrete by FedRAMP (`kt:fedramp`) deliverables.[^s3] Inside an org, Event Monitoring (`kt:event-monitoring`) and Security Center (`kt:security-center`) supply the customer-side evidence.[^s5][^s6]

## Sources

[^s1]: NIST CSRC, "SP 800-137, Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations". https://csrc.nist.gov/pubs/sp/800/137/final (accessed 2026-11-11)
[^s2]: NIST, "SP 800-137A, Assessing Information Security Continuous Monitoring (ISCM) Programs". https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-137A.pdf (accessed 2026-11-11)
[^s3]: FedRAMP, "Continuous Monitoring: Vulnerability Scanning (legacy playbook)". https://fedramp.gov/legacy/playbook/csp/continuous-monitoring/vulnerability-scanning/ (accessed 2026-11-11)
[^s4]: FedRAMP, "Collaborative Continuous Monitoring — Rev5 provider rules". https://fedramp.gov/2026/providers/rev5/rules/collaborative-continuous-monitoring/ (accessed 2026-11-11)
[^s5]: Salesforce Trailhead, "Learn the Core Concepts of Event Monitoring". https://trailhead.salesforce.com/content/learn/modules/event-monitoring-basics/learn-the-core-concepts-of-event-monitoring (accessed 2026-11-11)
[^s6]: Salesforce Trailhead, "Learn About Security Center". https://trailhead.salesforce.com/content/learn/modules/security-center/learn-about-security-center (accessed 2026-11-11)
