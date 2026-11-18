---
id: kt:security-governance
type: Concept
title: Security Governance
aliases: [Salesforce security governance, security governance model, cybersecurity governance]
domain: security-and-sharing
summary: >-
  The ownership, policies, review forums and audit cycle that set and enforce how a Salesforce estate is
  kept secure across its lifecycle; the security strand of IT and Salesforce governance, corresponding to the
  Govern function of NIST CSF 2.0.
release: "Winter '27"
status: concept
broader: [kt:it-governance]
related: [kt:nist-cybersecurity-framework, kt:security-center, kt:salesforce-center-of-excellence, kt:technical-debt-in-salesforce]
relations:
  - {predicate: partOf, object: kt:salesforce-governance}
  - {predicate: dependsOn, object: kt:principle-of-least-privilege}
sources:
  - id: s1
    title: "Six Steps to Establish a Security Governance Model"
    publisher: Salesforce Architects
    url: https://medium.com/salesforce-architects/six-steps-to-establish-a-security-governance-model-3e9cf461ffe1
    type: official-blog
    accessed: 2026-11-18
  - id: s2
    title: "The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)"
    publisher: NIST
    url: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
    type: standards-body
    accessed: 2026-11-18
  - id: s3
    title: "CSWP 29, The NIST Cybersecurity Framework (CSF) 2.0 (publication record)"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final
    type: standards-body
    accessed: 2026-11-18
  - id: s4
    title: "Security Policy Template"
    publisher: Salesforce Architects (architect.salesforce.com)
    url: https://architect.salesforce.com/1/asset/immutable/s/c9884a1/assets/pdf/security-policy-template.pdf
    type: official-docs
    accessed: 2026-11-18
  - id: s5
    title: "Learn About Security Center (Security Center module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/security-center/learn-about-security-center
    type: official-learning
    accessed: 2026-11-18
created: 2026-11-18
---

# Security Governance

**Security governance** is the structure that decides who owns platform security, which principles and policies apply, how designs and changes are reviewed against them, and how the result is maintained and audited over time. Salesforce's architect guidance frames it across people, processes and technologies, and scales each recommendation to small, medium or large implementations based on users, personas, integrations and regulatory exposure.[^s1] It is distinct from the security controls themselves (sharing rules, encryption, MFA): governance is the decision and accountability layer that chooses, enforces and revisits those controls.[^s1][^s2]

## The standards view: NIST CSF 2.0 Govern

NIST published CSF 2.0 as CSWP 29 on 26 February 2024, as a taxonomy of high-level cybersecurity outcomes rather than a prescribed set of practices.[^s3] Version 2.0 added **Govern (GV)** as a sixth function alongside Identify, Protect, Detect, Respond and Recover. Govern covers how the risk management strategy, expectations and policy are set, communicated and monitored, and it sits at the centre of the framework because it shapes how the other five functions are carried out.[^s2] Its six categories are a useful checklist for a Salesforce programme:[^s2]

- **Organizational Context (GV.OC)**: mission, stakeholders, dependencies and legal or contractual requirements.[^s2]
- **Risk Management Strategy (GV.RM)**: priorities, constraints, risk appetite and tolerance that drive decisions.[^s2]
- **Roles, Responsibilities and Authorities (GV.RR)**: who is accountable, and adequate resourcing for them.[^s2]
- **Policy (GV.PO)**: establishing, communicating and enforcing policy, and keeping it current.[^s2]
- **Oversight (GV.OV)**: feeding risk-management results back to adjust the strategy.[^s2]
- **Cybersecurity Supply Chain Risk Management (GV.SC)**: managing risk from suppliers and other third parties.[^s2]

## How Salesforce programmes put it in place

The Salesforce Architects model proceeds in six steps.[^s1] First, name a single owner of end-to-end platform security, the Salesforce Security Architect. Depending on size this is a dedicated architect, the platform technical owner, the release manager, the BAU lead or the admin. The CISO aligns guidelines with company strategy and regulation, and data owners and the privacy officer define sensitivity and access rules.[^s1] Second, set guiding principles through a risk-based security strategy: authentication, data access for the most important objects, persona strategy, secure integration patterns and coding standards, reviewed at least yearly.[^s1] Third, route designs through an architecture review board and a design authority, where the security architect approves security decisions and any deviation goes on the technical debt register with its rationale.[^s1]

The last three steps carry governance into delivery and operations.[^s1] Builds are enforced through peer review, static analysis with Salesforce Code Analyzer, scripts that flag risky security-configuration changes, persona and guest-user testing, and penetration tests before go-live and major releases. Run-time maintenance covers provisioning, access reviews, Critical Updates and credential or certificate rotation. Regular audits close the loop, and highly sensitive organisations add monitoring with Shield Event Monitoring, threat modelling and possibly bug bounties.[^s1]

## Policy and tooling

Salesforce's Well-Architected **Security Policy Template** gives the policy layer a concrete shape. Its sections cover organizational security (password, domain, IP and login-hour rules), device policies, per-object auditing, authentication methods, persona access, approved connected-app OAuth flows and scopes, and an authorization matrix of object, field, record and feature access per persona.[^s4] It ends with a change-approval process and a change log, and its example risk audit reviews all org access and sensitive-field access quarterly.[^s4] Across many orgs, **Security Center** turns policy into monitoring: it aggregates security metrics from child tenants into a parent tenant, raises threshold alerts such as for users holding Modify All Data, deploys versioned security policies to chosen tenants, and supports custom Health Check baselines.[^s5]

## Gotchas

- **Ownership without authority fails.** The model expects the security owner to chair forums and approve security decisions, not just advise.[^s1]
- **Exceptions must be recorded.** Undocumented deviations become invisible risk; the register gives each one a rationale and a path to fix.[^s1]
- **Policies go stale.** CSF 2.0 treats keeping policy current with threats and technology as part of governance itself.[^s2]

## Connections

- **broader → `kt:it-governance`**: security governance is the security slice of IT governance, and CSF 2.0 now gives it its own function.[^s2]
- **partOf → `kt:salesforce-governance`**: the security strand of the platform governance framework, alongside data governance.[^s1]
- **related → `kt:nist-cybersecurity-framework`**: the Govern function supplies the standard vocabulary for context, strategy, roles, policy, oversight and supply chain.[^s2]
- **related → `kt:security-center`**: the multi-org tool for monitoring and deploying security policy.[^s5]
- **related → `kt:salesforce-center-of-excellence`**: the governance body whose review forums host security decisions.[^s1]
- **related → `kt:technical-debt-in-salesforce`**: security deviations are logged in the technical debt register.[^s1]
- **dependsOn → `kt:principle-of-least-privilege`**: the access model the strategy and persona matrices are built on.[^s1][^s4]

## Sources
[^s1]: Salesforce Architects, "Six Steps to Establish a Security Governance Model" (Sandrine Ged, 2023-12-13). https://medium.com/salesforce-architects/six-steps-to-establish-a-security-governance-model-3e9cf461ffe1 (accessed 2026-11-18)
[^s2]: NIST, "The NIST Cybersecurity Framework (CSF) 2.0", CSWP 29. https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf (accessed 2026-11-18)
[^s3]: NIST CSRC, "CSWP 29, The NIST Cybersecurity Framework (CSF) 2.0". https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final (accessed 2026-11-18)
[^s4]: Salesforce Architects, "Security Policy Template". https://architect.salesforce.com/1/asset/immutable/s/c9884a1/assets/pdf/security-policy-template.pdf (accessed 2026-11-18)
[^s5]: Trailhead, "Learn About Security Center". https://trailhead.salesforce.com/content/learn/modules/security-center/learn-about-security-center (accessed 2026-11-18)
