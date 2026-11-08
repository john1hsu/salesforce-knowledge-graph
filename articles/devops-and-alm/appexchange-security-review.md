---
id: kt:appexchange-security-review
type: Concept
title: AgentExchange Security Review
aliases: [AppExchange Security Review, ISV security review, Salesforce partner security review, AgentExchange Security Review Wizard]
domain: devops-and-alm
summary: >-
  The mandatory security assessment Salesforce Product Security performs on partner solutions (managed packages,
  API-only and Marketing Cloud apps) before they can be listed and distributed on AgentExchange, formerly AppExchange.
release: "Winter '27"
status: current
broader: [kt:application-lifecycle-management, kt:agentexchange]
related: [kt:first-generation-managed-packages, kt:second-generation-managed-packages, kt:external-client-apps, kt:field-level-security, kt:integration-security]
relations:
  - {predicate: dependsOn, object: kt:code-analyzer}
  - {predicate: mitigates, object: kt:soql-injection}
sources:
  - id: s1
    title: "How the AgentExchange Security Review Works"
    publisher: Salesforce Developers (ISVforce Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packageGuide/security_review_how_it_works.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Required Materials for Security Review Submission"
    publisher: Salesforce Developers (ISVforce Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.262.0.packagingGuide.meta/packagingGuide/security_review_required_materials.htm
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Submit Your Solution for Security Review (ISV Security Review module)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/modules/isv_security_review/units/isv_security_review_submit
    type: official-learning
    accessed: 2026-11-08
  - id: s4
    title: "Experience the New AgentExchange"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentexchange-quick-look/experience-the-new-agentexchange
    type: official-learning
    accessed: 2026-11-08
created: 2026-11-08
---

# AgentExchange Security Review

The security review is the gate every commercial partner solution must pass before it can be listed on Salesforce's marketplace. Managed packages, Salesforce Platform API solutions and Marketing Cloud Engagement API solutions all have to be approved by Salesforce's Product Security team before distribution.[^s1] The marketplace itself was AppExchange until Salesforce merged it with the earlier AgentExchange and the Slack Marketplace into a single AgentExchange, and Trailhead presents the review as the trust mechanism behind every listing, combining technical audits with vulnerability scans.[^s4] The documentation and wizard now carry the AgentExchange name, but the process (and many URLs) are the same that partners knew as the AppExchange security review.[^s1][^s3]

## How it works

Before submitting, a partner must enrol in the partner program, connect the packaging org to the Partner Console, create a provider profile, and certify the solution as Lightning Ready, which is mandatory for all new submissions.[^s1] Submission starts from the Partner Console: open the solution under the Technologies tab, choose *Start Review*, and walk the AgentExchange Security Review Wizard through contacts, technical details, documentation, test environments and payment.[^s3] Salesforce describes five stages: submission, verification of the package, entry into the Product Security queue, testing, and notification of results.[^s1]

The test itself is a time-boxed, black-box assessment. Testers try to find vulnerabilities, but the report gives examples of each issue class rather than every instance, and some classes may only surface on a later pass, so a failed report means "find and fix this pattern everywhere", not "fix these lines".[^s1] Scope follows the data: any external website, service or third-party server that touches customer data or credentials is tested, not just the Apex in the package.[^s2]

## What you submit

Materials vary by architecture. The package must be Managed-Released; beta and unmanaged packages are rejected. Native solutions need a Developer Edition org with the package installed plus a Checkmarx source scan report, while solutions with external web apps, mobile clients or API-only designs also need dynamic application security testing (DAST) reports and working credentials for every authenticated external component.[^s2] All architectures need user documentation and, where scanners flag issues that are not real vulnerabilities, written false-positive explanations; companies also submit their information security policies, scaled to their size and maturity.[^s2] Trailhead adds that managed packages must include Salesforce Code Analyzer reports or a justification for omitting them, and points partners to a checklist builder that generates the list for a given architecture.[^s3] Extension packages are reviewed together with any base packages that have not already passed.[^s2]

## Limits, fees and timelines

Trailhead states a fee of $999 per paid solution, charged on the initial submission and again on every resubmission after a failed attempt; free solutions do not pay.[^s3][^s1] Salesforce's estimates are 1–2 weeks for verification, 3–4 weeks for a first test and 2–3 weeks to retest a resubmission that shows progress, all dependent on completeness and queue volume.[^s1] Trailhead notes that most submissions pass on the second attempt and that untested submissions rarely pass at all.[^s3][^s1]

Approval is not permanent. Solutions are typically re-reviewed about once a year, and Product Security can request a review at any time; new package versions do not need a full resubmission but require a short attestation in the Partner Console.[^s3] Submitting only major and minor versions, rather than patches, maximises how much of a prior approval later versions inherit.[^s1]

## Gotchas and practice

Run automated scanning continuously, not on the eve of submission: Salesforce recommends Code Analyzer during development and the Checkmarx-based Source Code Scanner on the Partner Security Portal, followed by manual testing because scanners miss business-logic flaws.[^s1] Fix every finding or document it as a false positive before submitting, since a submission that skips this step is likely to come back unapproved.[^s1][^s2] Omitting a component (a callout endpoint, a companion mobile app) delays the review, so include anything in doubt.[^s2] Office hours on the Partner Security Portal help interpret a failed report.[^s3]

## Connections

The review sits inside the partner side of **application lifecycle management** and is the entry ticket to **AgentExchange**.[^s1][^s4] It applies to solutions packaged as **first-generation managed packages** or **second-generation managed packages**, and the package must be Managed-Released before it is accepted.[^s1][^s2] It depends in practice on **Salesforce Code Analyzer** reports, and by forcing vulnerability testing before listing it guards subscribers against flaws like **SOQL injection** or missing **field-level security** checks in partner code.[^s3][^s1] Packaged **external client apps** and external callouts bring in the concerns of **integration security**, because the review tests every endpoint that customer data reaches.[^s2]

## Sources
[^s1]: Salesforce Developers, "How the AgentExchange Security Review Works" (ISVforce Guide). https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packageGuide/security_review_how_it_works.htm (accessed 2026-11-08)
[^s2]: Salesforce Developers, "Required Materials for Security Review Submission" (ISVforce Guide). https://developer.salesforce.com/docs/atlas.en-us.262.0.packagingGuide.meta/packagingGuide/security_review_required_materials.htm (accessed 2026-11-08)
[^s3]: Trailhead, "Submit Your Solution for Security Review". https://trailhead.salesforce.com/en/modules/isv_security_review/units/isv_security_review_submit (accessed 2026-11-08)
[^s4]: Trailhead, "Experience the New AgentExchange". https://trailhead.salesforce.com/content/learn/modules/agentexchange-quick-look/experience-the-new-agentexchange (accessed 2026-11-08)
