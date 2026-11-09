---
id: kt:nist-digital-identity-guidelines
type: ExternalConcept
title: NIST Digital Identity Guidelines
aliases: [NIST SP 800-63, SP 800-63-4, NIST 800-63, Digital Identity Guidelines, "NIST SP 800-63 Revision 4"]
domain: public-sector-and-compliance
summary: >-
  NIST Special Publication 800-63, the US federal suite of guidelines for identity proofing, authentication and
  federation, which defines identity, authentication and federation assurance levels (IAL, AAL, FAL); Revision 4
  (July 2025) is the benchmark Salesforce architects map MFA, session and SSO designs against.
release: "Winter '27"
status: concept
broader: [kt:security-compliance-frameworks]
related: [kt:multi-factor-authentication, kt:session-security-levels, kt:single-sign-on-saml, kt:fedramp]
relations:
  - {predicate: contrastsWith, object: kt:password-policies}
  - {predicate: mitigates, object: kt:account-takeover}
sources:
  - id: s1
    title: "SP 800-63-4, Digital Identity Guidelines"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/sp/800/63/4/final
    type: standards-body
    accessed: 2026-11-09
  - id: s2
    title: "Digital Identity Guidelines Rev 4 slides"
    publisher: NIST
    url: https://www.nist.gov/document/digital-identity-guidelines-rev-4-slides
    type: standards-body
    accessed: 2026-11-09
  - id: s3
    title: "SP 800-63B-4: Authentication Assurance Levels"
    publisher: NIST
    url: https://pages.nist.gov/800-63-4/sp800-63b/aal
    type: standards-body
    accessed: 2026-11-09
  - id: s4
    title: "SP 800-63C-4: Federation and Assertions"
    publisher: NIST
    url: https://pages.nist.gov/800-63-4/sp800-63c.html
    type: standards-body
    accessed: 2026-11-09
  - id: s5
    title: "Prepare Your Org for Salesforce MFA Enforcement"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2026/prepare-your-org-for-salesforce-mfa-enforcement
    type: official-blog
    accessed: 2026-11-09
  - id: s6
    title: "SessionLevel Enum (Apex Reference Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_enum_Auth_SessionLevel.htm
    type: official-docs
    accessed: 2026-11-09
created: 2026-11-09
---

# NIST Digital Identity Guidelines

NIST Special Publication 800-63, *Digital Identity Guidelines*, is the US federal guidance on how people prove who they are, log in and are federated into government systems over a network, whether they are employees, contractors or members of the public.[^s1] It sets technical requirements for enrollment, authenticators, their management, authentication protocols, federation and assertions.[^s1] Revision 4 (SP 800-63-4) was finalized on 31 July 2025 and supersedes SP 800-63-3.[^s1] For Salesforce architects it is the yardstick behind questions such as "is this MFA phishing-resistant?" or "is this SSO assertion strong enough?", especially on public-sector projects.

## Structure and assurance levels

The suite is a base volume plus three companion volumes: SP 800-63A-4 on identity proofing and enrollment, SP 800-63B-4 on authentication and authenticator management, and SP 800-63C-4 on federation and assertions.[^s1] Each volume has its own ladder of assurance levels: identity assurance (IAL) for proofing, authentication assurance (AAL) for login, and federation assurance (FAL) for assertions.[^s2] Revision 4 adds a lower IAL1 proofing option, offers three pathways to IAL2 (non-biometric, digital evidence and biometric), and aligns account recovery with the IAL and AAL in use.[^s2]

## Risk-based selection

Revision 4 replaces the old flow diagrams with a digital identity risk management process. Agencies assess risk to the online service and risk introduced by the identity system itself, choose initial assurance levels, tailor them, and keep evaluating, with customer experience and redress built in.[^s2] Suggested metrics include pass and fail rates, fraud rates and help desk feedback.[^s2] The levels are therefore an output of a risk assessment, not a fixed rule per system type.

## Authentication (AAL) in practice

AAL1 allows single-factor login. AAL2 needs two distinct factors or one multi-factor authenticator, and the verifier must offer at least one phishing-resistant option; federal agencies must require it for staff, contractors and partners.[^s3] AAL3 requires a phishing-resistant cryptographic authenticator with a non-exportable private key.[^s3] Reauthentication bounds tighten with level: at AAL2 sessions should last no more than 24 hours and time out after no more than an hour of inactivity, and at AAL3 they must end within 12 hours, with inactivity of 15 minutes or less.[^s3] Revision 4 accepts syncable authenticators such as passkeys at AAL2 with user verification but not at AAL3, because AAL3 forbids exportable keys.[^s2] Password length rules now depend on whether the password is used inside MFA.[^s2]

## Federation (FAL)

At FAL1 the identity provider signs a bearer assertion, which the relying party validates and protects against replay.[^s4] FAL2 adds strong injection protection, an RP-initiated flow, a single audience and a pre-established trust agreement.[^s4] FAL3 also requires proof that the subscriber holds an authenticator, through a holder-of-key assertion or bound authenticator.[^s4] The identity provider must tell the relying party which IAL, AAL and FAL applied, and the relying party sets the minimums it accepts.[^s4] Revision 4 maps OIDC and SAML features to these levels and adds subscriber-controlled wallets as a federation model.[^s2]

## How Salesforce maps to it

From 26 June 2026 Salesforce requires MFA for all users and phishing-resistant MFA for administrators and users with powerful permissions such as Modify All Data or Author Apex.[^s5] Salesforce counts physical security keys and built-in biometric authenticators as phishing-resistant, but not approving a push or entering a code.[^s5] That split mirrors the AAL2 phishing-resistant option and the AAL3 requirement.[^s3] Session security levels add a step-up dimension: the `Auth.SessionLevel` enum distinguishes `STANDARD` from `HIGH_ASSURANCE` sessions as configured by the org.[^s6] For SSO, Salesforce relies on the identity provider sending AMR or ACR claims that prove MFA (and, for privileged users, phishing-resistant FIDO2) took place, which parallels the 800-63C rule that the IdP communicates assurance to the relying party.[^s5][^s4]

Gotchas: Salesforce's settings are not a certification that a deployment meets a given AAL; timeouts, recovery flows and authenticator choices still need to be set to the target level.[^s3] Passkeys that sync across devices top out at AAL2.[^s2]

## Connections

The guidelines belong to the wider set of security compliance frameworks (`kt:security-compliance-frameworks`).[^s1] Salesforce **multi-factor authentication** is the main feature measured against AAL rules, and **session security levels** supply step-up and high-assurance sessions.[^s5][^s6] **SAML single sign-on** is where FAL concepts apply, since Salesforce acts as a relying party for assertions.[^s4][^s5] Salesforce **password policies** contrast with Revision 4's password guidance, while phishing-resistant authenticators help mitigate **account takeover**.[^s2][^s3] Because the guidelines target access to government information systems, they matter most on **FedRAMP**-authorized public-sector workloads.[^s1]

## Sources
[^s1]: NIST CSRC, "SP 800-63-4, Digital Identity Guidelines". https://csrc.nist.gov/pubs/sp/800/63/4/final (accessed 2026-11-09)
[^s2]: NIST, "Digital Identity Guidelines Rev 4 slides". https://www.nist.gov/document/digital-identity-guidelines-rev-4-slides (accessed 2026-11-09)
[^s3]: NIST, "SP 800-63B-4: Authentication Assurance Levels". https://pages.nist.gov/800-63-4/sp800-63b/aal (accessed 2026-11-09)
[^s4]: NIST, "SP 800-63C-4: Federation and Assertions". https://pages.nist.gov/800-63-4/sp800-63c.html (accessed 2026-11-09)
[^s5]: Salesforce Admins Blog, "Prepare Your Org for Salesforce MFA Enforcement". https://admin.salesforce.com/blog/2026/prepare-your-org-for-salesforce-mfa-enforcement (accessed 2026-11-09)
[^s6]: Salesforce, "SessionLevel Enum", Apex Reference Guide. https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_enum_Auth_SessionLevel.htm (accessed 2026-11-09)
