---
id: kt:account-takeover
type: Concept
title: Account Takeover
aliases: [ATO, account compromise, credential stuffing, compromised user account]
domain: identity
summary: >-
  The threat in which an attacker gains control of a legitimate user's Salesforce login — typically through
  phishing, vishing or credential stuffing with reused passwords — and then acts with that user's access. It is
  the main risk that Salesforce MFA, step-up session security and login monitoring are designed to blunt.
release: "Winter '27"
status: concept
broader: [kt:salesforce-identity]
related: [kt:multi-factor-authentication, kt:session-security-levels, kt:login-flows, kt:event-monitoring, kt:transaction-security-policies]
relations:
  - {predicate: causes, object: kt:data-breach-risk}
  - {predicate: contrastsWith, object: kt:integration-security}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "Multi-Factor Authentication (Identity Implementation Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/security_overview_2fa.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s2
    title: "Strengthening Salesforce Security Against AI-Driven Threats"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/strengthening-salesforce-security-against-ai-driven-threats/
    type: official-blog
    accessed: 2026-11-07
  - id: s3
    title: "How Salesforce Helps Protect You From Credential Stuffers"
    publisher: Salesforce Engineering
    url: https://engineering.salesforce.com/how-salesforce-helps-protect-you-from-credential-stuffers-ffd2a9fe0330/
    type: official-blog
    accessed: 2026-11-07
  - id: s4
    title: "More than a Password: Protect Yourself from Malicious Hackers with Multifactor Authentication"
    publisher: Cybersecurity and Infrastructure Security Agency (CISA)
    url: https://www.cisa.gov/MFA
    type: government
    accessed: 2026-11-07
  - id: s5
    title: "Multifactor Authentication"
    publisher: Cybersecurity and Infrastructure Security Agency (CISA)
    url: https://cisa.gov/topics/cybersecurity-best-practices/multifactor-authentication
    type: government
    accessed: 2026-11-07
created: 2026-11-07
---

# Account Takeover

Account takeover (ATO) is the compromise of a real user's account so that an attacker can sign in and operate with that user's identity and permissions. In a Salesforce org this is especially damaging because the attacker inherits everything the user's profile, permission sets and sharing grant — including report exports, API access and, for admins, the ability to change security settings. Salesforce's own documentation frames multi-factor authentication as the control that makes phishing and account takeovers much harder to pull off.[^s1]

## How accounts get taken over

The classic route is **credential stuffing**: attackers replay username and password pairs leaked from other breaches against many sites, betting on password reuse, and any login that succeeds becomes a takeover candidate. Salesforce Engineering describes this as an automated, high-volume attack and notes that breaches are often disclosed long after they occur, giving attackers a wide window to use the stolen data.[^s3] Phishing is the second route: a fake login page or message captures the password directly, and CISA points out that even complex passwords can be bypassed this way.[^s5]

Salesforce's 2026 security guidance adds that AI makes these attacks cheaper and more convincing: AI-assisted credential stuffing and phishing can get past login protections even when passwords are strong, and attackers may stay hidden in the account for a long time. It also highlights voice phishing (vishing) and other identity-based social engineering, which use data from earlier breaches to target admins and privileged users whose broad access makes them the most valuable accounts to seize.[^s2] Once inside, the typical objective is data exfiltration through bulk report exports and large queries, which attackers can automate faster than manual monitoring catches.[^s2]

## How Salesforce defends against it

- **MFA everywhere.** According to Salesforce, MFA has been enforced for all user logins, including SSO, in production and sandbox orgs since June 2026; admins and users with powerful permissions must use phishing-resistant methods.[^s2] The Identity Implementation Guide names authenticator apps and security keys as examples of the "something you have" factor and recommends registering more than one method.[^s1]
- **Phishing-resistant factors.** CISA treats phishing-resistant MFA as the goal, identifying FIDO/WebAuthn as the widely available option because it refuses to complete a login on a fake site; where that isn't feasible yet, it recommends number matching to counter push-bombing.[^s4]
- **Step-up and session controls.** Report actions can demand re-verification after a configurable window, and machine-learning anomaly detection triggers extra verification when behavior deviates from the user's norm.[^s2]
- **Network restrictions.** Login IP restrictions confine access to trusted networks, and Salesforce blocks anonymizing proxies, VPNs and high-risk IP addresses.[^s2]
- **Detection and remediation.** Salesforce runs anomaly detection over login traffic to spot credential stuffing in progress; when an account is known to be compromised, the user must pass an identity challenge and reset the password before getting back in.[^s3]

## Gotchas and practitioner notes

MFA alone does not end the problem: Salesforce explicitly warns that AI-assisted phishing can bypass login protections, so architects should layer detection on top of prevention.[^s2] Event Monitoring records login, export and API events, and a default transaction security policy requires step-up authentication for UI report exports above 10,000 records — a guardrail aimed squarely at post-takeover exfiltration.[^s2] Security Health Check gives a prioritized list of baseline gaps worth closing first.[^s2] Older guidance still applies too: unique passwords, password history, and rate limiting or CAPTCHA on login pages reduce the payoff of credential stuffing.[^s3]

## Connections

Account takeover sits under **Salesforce Identity** as the core threat its controls answer. **Multi-factor authentication** and **session security levels** are the primary mitigations, both of which already point to this node; **login flows** can add custom checks at sign-in. **Event Monitoring** and **transaction security policies** detect and interrupt suspicious sessions, as described above.[^s2] A successful takeover leads directly to **data breach risk**, and it contrasts with **integration security**, which concerns compromised machine credentials rather than human logins. The topic is examined in the **Identity and Access Management Architect certification**.[^s1]

## Sources
[^s1]: Salesforce Developers, "Multi-Factor Authentication (Identity Implementation Guide)". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/security_overview_2fa.htm (accessed 2026-11-07)
[^s2]: Salesforce, "Strengthening Salesforce Security Against AI-Driven Threats" (May 2026). https://www.salesforce.com/blog/strengthening-salesforce-security-against-ai-driven-threats/ (accessed 2026-11-07)
[^s3]: Salesforce Engineering, "How Salesforce Helps Protect You From Credential Stuffers". https://engineering.salesforce.com/how-salesforce-helps-protect-you-from-credential-stuffers-ffd2a9fe0330/ (accessed 2026-11-07)
[^s4]: CISA, "More than a Password: Protect Yourself from Malicious Hackers with Multifactor Authentication". https://www.cisa.gov/MFA (accessed 2026-11-07)
[^s5]: CISA, "Multifactor Authentication". https://cisa.gov/topics/cybersecurity-best-practices/multifactor-authentication (accessed 2026-11-07)
