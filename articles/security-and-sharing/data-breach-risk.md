---
id: kt:data-breach-risk
type: Concept
title: Data Breach Risk
aliases: [data exfiltration risk, Salesforce data theft, privacy breach risk]
domain: security-and-sharing
summary: >-
  The risk that data held in a Salesforce org is accessed, exported or disclosed by someone not authorized to
  have it — today most often through stolen credentials, social engineering or compromised integration tokens
  rather than platform flaws. Under the shared responsibility model, reducing it is largely a customer
  configuration task.
release: "Winter '27"
status: concept
broader: [kt:shared-responsibility-model]
related: [kt:account-takeover, kt:connected-apps, kt:event-monitoring, kt:transaction-security-policies, kt:shield-platform-encryption, kt:principle-of-least-privilege]
sources:
  - id: s1
    title: "Privacy Breach (CSRC Glossary)"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/glossary/term/privacy_breach
    type: standards-body
    accessed: 2026-11-07
  - id: s2
    title: "Security as a Shared Responsibility Between Provider and Customer"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/shared-responsibility-model/
    type: official-blog
    accessed: 2026-11-07
  - id: s3
    title: "Protect Your Salesforce Environment from Social Engineering Threats"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/?p=108565
    type: official-blog
    accessed: 2026-11-07
  - id: s4
    title: "Widespread Data Theft Targets Salesforce Instances via Salesloft Drift"
    publisher: Google Threat Intelligence Group / Mandiant
    url: https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift?e=48754805
    type: partner
    accessed: 2026-11-07
  - id: s5
    title: "Use Health Check to Scan Your Security Configurations (Security Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/security_basics/security_basics_healthcheck
    type: official-learning
    accessed: 2026-11-07
created: 2026-11-07
---

# Data Breach Risk

**Data breach risk** is the likelihood and impact of Salesforce data being seen, exported or disclosed by someone who should not have it. NIST's glossary frames a privacy breach as a loss of control over data, covering both cases where an unauthorized person accesses (or may have accessed) it and cases where an authorized user uses it for a purpose they were not allowed to pursue.[^s1] In Salesforce terms, that spans an outsider with a stolen session, a compromised integration user, and an insider running an oversized report export.

## Why it is mostly a customer-side risk

Salesforce describes security as a responsibility it shares with customers: it runs the protections for the infrastructure and platform, while customers own their data, their configuration and who gets access.[^s2] Salesforce groups customer controls as "configurables" — MFA and SSO, least-privilege user access via permission sets, login monitoring with Login History and login IP restrictions, and dozens of org settings — with paid "enhanceables" such as Shield, Security Center, Privacy Center and Backup & Recover layered on top.[^s2] The practical consequence is that most breach exposure in an org comes from how it is configured, not from the multitenant platform beneath it.

## How breaches happen in practice

Two campaign patterns dominated Salesforce-related data theft in 2025, and neither exploited a platform vulnerability:

- **Social engineering of users.** Salesforce warned that attackers posing as IT support used voice phishing to steer staff to credential- and MFA-harvesting pages, or to talk them into authorizing a malicious connected app — sometimes a renamed copy of Data Loader — which was then used to pull data out.[^s3] This is Account Takeover (`kt:account-takeover`) turned into bulk exfiltration.
- **Compromised integration tokens.** Google's threat intelligence team reported that, between roughly 8 and 18 August 2025, an actor used stolen OAuth tokens from the Salesloft Drift integration to query and export objects such as Accounts, Cases, Users and Opportunities from many customer orgs, and stated the issue did not come from a flaw in core Salesforce.[^s4] The attackers then searched the stolen records for secrets such as AWS keys, passwords and Snowflake tokens, and Salesloft and Salesforce revoked all of the app's access and refresh tokens on 20 August.[^s4]

Two lessons follow. First, a connected app's token is effectively a standing credential with the integration user's full reach, so over-scoped integrations widen the blast radius. Second, secrets pasted into Case descriptions or notes turn a CRM breach into a breach of other systems.[^s4]

## Reducing the risk

Salesforce's own guidance stacks several controls:

- Restrict logins to trusted networks with login IP ranges at org and profile level.[^s3]
- Apply least privilege: grant access through permission sets rather than broad profiles, review holders of high-risk permissions such as Modify All Data or Manage Connected Apps, limit Data Loader and API access, and allowlist known apps.[^s3]
- Rely on MFA, which Salesforce requires and automatically enables for direct logins.[^s3]
- Use Shield: Event Monitoring for visibility, Threat Detection for events such as session hijacking and credential stuffing, and Transaction Security Policies to flag or block actions such as large downloads.[^s3]

For integrations, the GTIG write-up adds: keep connected app scopes to the minimum (avoid `full`), enforce IP restrictions on the connected app, shorten session timeouts, grant API Enabled only through permission sets, and review `UniqueQuery` events in Event Monitoring when investigating.[^s4] To audit baseline configuration, Health Check scores org security settings from 0 to 100 against Salesforce's standard values or an imported custom baseline, and can fix flagged settings in bulk.[^s5]

## Gotchas

- Both 2025 campaigns ran through legitimate logins and tokens, so controls on who can authenticate and what they can export did more than perimeter defenses.[^s3][^s4]
- Attackers may delete Bulk API query jobs to cover tracks, but event logs survive, so retain and review them.[^s4]
- A good Health Check score covers settings, not people or third-party apps; it would not have caught an over-scoped integration token.[^s5]

## Connections

Data breach risk sits under the shared responsibility model (`kt:shared-responsibility-model`), because it is mainly the customer's half of that model.[^s2] Account Takeover (`kt:account-takeover`) is a leading cause, and controls across the graph are defined by how they reduce it: Transaction Security Policies (`kt:transaction-security-policies`) and Event Monitoring (`kt:event-monitoring`) detect and block exfiltration, Shield Platform Encryption (`kt:shield-platform-encryption`) protects data at rest, and the principle of least privilege (`kt:principle-of-least-privilege`) limits what any one compromised user or connected app (`kt:connected-apps`) token can reach.[^s3][^s4]

## Sources
[^s1]: NIST CSRC, "Privacy Breach" glossary entry. https://csrc.nist.gov/glossary/term/privacy_breach (accessed 2026-11-07)
[^s2]: Salesforce, "Security as a Shared Responsibility Between Provider and Customer". https://www.salesforce.com/blog/shared-responsibility-model/ (accessed 2026-11-07)
[^s3]: Salesforce, "Protect Your Salesforce Environment from Social Engineering Threats". https://www.salesforce.com/blog/?p=108565 (accessed 2026-11-07)
[^s4]: Google Threat Intelligence Group / Mandiant, "Widespread Data Theft Targets Salesforce Instances via Salesloft Drift". https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift?e=48754805 (accessed 2026-11-07)
[^s5]: Trailhead, "Use Health Check to Scan Your Security Configurations". https://trailhead.salesforce.com/content/learn/modules/security_basics/security_basics_healthcheck (accessed 2026-11-07)
