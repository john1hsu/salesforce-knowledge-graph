---
id: kt:security-health-check
type: Tool
title: Security Health Check
aliases: [Health Check, Salesforce Health Check, Health Check score, SecurityHealthCheck]
domain: security-and-sharing
summary: >-
  A built-in Setup tool that scores an org's security settings from 0 to 100 against the Salesforce Baseline
  Standard or an imported custom baseline, groups non-compliant settings by risk level, and can bulk-correct
  them with Fix Risks.
release: "Winter '27"
status: current
broader: [kt:security-governance]
related: [kt:session-settings, kt:password-policies, kt:org-check, kt:salesforce-optimizer]
relations:
  - {predicate: queriedWith, object: kt:tooling-api}
  - {predicate: consumedBy, object: kt:security-center}
  - {predicate: mitigates, object: kt:data-breach-risk}
sources:
  - id: s1
    title: "Improve Your Org's Security with Salesforce Health Check"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/security_basics/security_basics_healthcheck
    type: official-learning
    accessed: 2026-11-20
  - id: s2
    title: "Enhance Salesforce Org Security: Run Health Check"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/secure-salesforce-configuration/run-health-check
    type: official-learning
    accessed: 2026-11-20
  - id: s3
    title: "Exercise 1: Take Action with Health Check"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/workshops/admin-security-workshop/org-security/1-health-check
    type: official-learning
    accessed: 2026-11-20
  - id: s4
    title: "Exercise 4: Configure Health Check"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/workshops/admin-security-workshop/org-security/3-configure-health-check
    type: official-learning
    accessed: 2026-11-20
  - id: s5
    title: "Tooling API Developer Guide: SecurityHealthCheck"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/tooling_api_objects_securityhealthcheck.htm
    type: official-docs
    accessed: 2026-11-20
created: 2026-11-20
---

# Security Health Check

Security Health Check (shown in Setup simply as Health Check) is a built-in tool that inspects an org's security-related settings and reports how closely they match a recommended baseline.[^s1] It produces a single score from 0 to 100, where 100 means the configuration matches the baseline as securely as possible, and it lists each setting with the org's current value beside the recommended one.[^s1][^s2] Admins open it by typing "Health Check" into Setup's Quick Find box.[^s1][^s3] It is the usual first stop in an org security review because it turns scattered settings pages into one prioritized worklist.[^s3]

## How it works

Health Check compares the org's configuration against a security baseline, by default the Salesforce Baseline Standard; in the tool the baseline values appear as "Standard Value" next to the org's "Your Value" column.[^s1][^s3] Results are grouped into High-Risk, Medium-Risk, Low-Risk and Informational security settings, and reviewers work through those sections in order of severity.[^s3] Tightening settings toward the more restrictive recommended values generally raises the score.[^s1]

The settings it covers span several Setup areas. Trailhead's walkthrough points to session controls such as HttpOnly cookies, session timeout, clickjack protection, HTTPS and XSS protection, and notes that HTTPS has to be enforced both through HSTS in Session Settings and through the secure-connection option on sites.[^s2] The admin security workshop uses password policies as its worked example, where items such as minimum password lifetime and secret-answer obscuring are flagged critical while lockout and complexity settings are warnings.[^s4]

- **Edit**: each listed setting links to the page where it can be changed individually.[^s1]
- **Fix Risks**: selects several (or all) non-compliant settings and applies the recommended values in one action.[^s1][^s4]
- **Email notification**: Health Check can be set to notify all system admins, and other recipients such as IT or security teams, by email.[^s4]

## Custom baselines

Organizations with stricter or different requirements, typically in regulated industries such as finance or healthcare, can import their own baseline as an XML file; the tool calls these custom baselines.[^s1] A common pattern is to export the Salesforce Baseline Standard from the baseline's Settings menu, edit thresholds in the XML, and import the result under a new name and API name, optionally marking it as the default baseline.[^s4] In the workshop example, each numeric setting carries separate compliant and warning thresholds, and the exercise raises the compliant minimum password length from 8 to 11.[^s4] Trailhead advises agreeing baseline values with IT or compliance before importing one.[^s1]

## API access

The score is exposed through the Tooling API object SecurityHealthCheck, available in API version 37.0 and later, which returns the org's Health Check score.[^s5] A companion object, SecurityHealthCheckRisks, returns each setting's current value, risk and recommended value.[^s5] Only users with the View Setup and Configuration permission can query these objects, which makes them suitable for scripted monitoring across many orgs.[^s5]

## Limits and gotchas

- **Fix Risks has side effects**: bulk changes can break integrations or remove user access, so test them in a sandbox and prefer changing settings one at a time.[^s1]
- **Configuration only**: Health Check reviews settings and does not inspect your data for vulnerabilities such as over-shared records.[^s4]
- **Score is relative**: a high score means alignment with whichever baseline is active, so a lenient custom baseline can inflate it.[^s1][^s5]
- **Permissions**: the Trailhead unit requires View Setup and Configuration plus Manage Password Policies to complete its tasks.[^s1]

## When to use it (and when not)

Use Health Check as a recurring hygiene check after releases, org merges or large configuration changes, and as the baseline evidence for an internal security review.[^s2][^s3] It is scoped to one org's settings; for portfolio-wide monitoring, permission analysis or policy deployment across many orgs, Security Center (a separately licensed add-on) aggregates these results instead.[^s1] Sharing design, field-level security and data exposure need other reviews, because Health Check does not look at records.[^s4]

## Connections

Health Check sits under security governance (`kt:security-governance`) as its in-org measurement tool, and it `mitigates` data breach risk (`kt:data-breach-risk`) by flagging misconfigured access settings, which the workshop cites as a major breach cause.[^s3] It audits Session Settings (`kt:session-settings`) and Password Policies (`kt:password-policies`), the two areas its training material uses most.[^s2][^s4] It is `queriedWith` the Tooling API (`kt:tooling-api`) through SecurityHealthCheck and SecurityHealthCheckRisks, and is `consumedBy` Security Center (`kt:security-center`), which rolls scores up across orgs.[^s1][^s5] It is related to Org Check (`kt:org-check`) and Salesforce Optimizer (`kt:salesforce-optimizer`), which review org health from a configuration-quality rather than a security-baseline angle.[^s1]

## Sources

[^s1]: Salesforce Trailhead, "Improve Your Org's Security with Salesforce Health Check". https://trailhead.salesforce.com/content/learn/modules/security_basics/security_basics_healthcheck (accessed 2026-11-20)
[^s2]: Salesforce Trailhead, "Enhance Salesforce Org Security: Run Health Check". https://trailhead.salesforce.com/content/learn/modules/secure-salesforce-configuration/run-health-check (accessed 2026-11-20)
[^s3]: Salesforce Developers, "Exercise 1: Take Action with Health Check". https://developer.salesforce.com/workshops/admin-security-workshop/org-security/1-health-check (accessed 2026-11-20)
[^s4]: Salesforce Developers, "Exercise 4: Configure Health Check". https://developer.salesforce.com/workshops/admin-security-workshop/org-security/3-configure-health-check (accessed 2026-11-20)
[^s5]: Salesforce Developers, "Tooling API Developer Guide: SecurityHealthCheck". https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/tooling_api_objects_securityhealthcheck.htm (accessed 2026-11-20)
