---
id: kt:trialforce
type: Feature
title: Trialforce
aliases: [Salesforce Trialforce, Trialforce template, Trialforce source org, Trialforce Source Organization, TSO, Trialforce Management Org, TMO]
domain: devops-and-alm
summary: >-
  The ISV partner feature that provisions free trial orgs of a partner's solution from a template: a snapshot of a
  configured Trialforce source org, optionally branded through a Trialforce management org, delivered via
  AgentExchange, the SignupRequest API or Environment Hub demo orgs.
release: "Winter '27"
status: current
broader: [kt:agentexchange, kt:application-lifecycle-management]
related: [kt:second-generation-managed-packages, kt:first-generation-managed-packages, kt:sandbox-templates]
relations:
  - {predicate: dependsOn, object: kt:partner-business-org}
  - {predicate: integratesWith, object: kt:environment-hub}
  - {predicate: integratesWith, object: kt:license-management-app}
  - {predicate: hasPart, object: kt:signup-request-api}
sources:
  - id: s1
    title: "Trialforce Key Concepts and Relationships (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/trialforce-conceptual-overview.html
    type: official-docs
    accessed: 2026-11-23
  - id: s2
    title: "Create a Trialforce Template (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/trialforce-creating-template.html
    type: official-docs
    accessed: 2026-11-23
  - id: s3
    title: "Considerations for Trialforce Templates (ISVforce Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/trialforce-template-considerations.html
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "Get Your Orgs Ready (Trailhead: ISV App Trials)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/isv_app_trials/isv_app_trials_ready
    type: official-learning
    accessed: 2026-11-23
  - id: s5
    title: "Deliver Your Trial (Trailhead: ISV App Trials)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/isv_app_trials/units/isv_app_trials_deliver
    type: official-learning
    accessed: 2026-11-23
created: 2026-11-23
---

# Trialforce

**Trialforce** is how a Salesforce ISV partner hands prospects a ready-to-use trial org of its solution. Instead of asking a prospect to install a package into an empty org, the partner configures one org exactly as a customer should first see it, captures it as a template, and lets Salesforce stamp out new trial orgs from that template on demand.[^s1] The same templates also feed SignupRequest-based sign-up flows and demo orgs created from the Environment Hub.[^s1]

## How it works

A Trialforce setup has three layers.[^s1]

- **Trialforce management org (TMO):** the top of the hierarchy, used to create source orgs and to define custom branding.[^s1]
- **Trialforce source org (TSO):** the org you install the solution into, populate with sample data and configure; templates are created from it.[^s1]
- **Trialforce template:** an approximate snapshot, not an exact copy, of the TSO that defines what each new trial org contains.[^s1]

Salesforce recommends one TMO per company, one TSO per solution and one template per solution version, so a change touches only one layer; a new product version gets a new template that is swapped into the listing.[^s1] A TMO is only required for branded trials. An unbranded TSO is easiest to create from the Environment Hub, choosing the Trialforce Source Organization purpose and an Enterprise or Professional TSO edition; a TMO is requested through a Salesforce Help case.[^s4]

To build a template, a user with Modify All Data logs in to the TSO, opens Trialforce in Setup and creates a new template, choosing **All Data and Setup** (metadata plus data) or **Setup Only** (metadata only).[^s2] Options shift dates relative to the new org's creation date, exclude Chatter feed items, or make the template private so only up to 51 listed org IDs can sign up.[^s2] An email delivers the template ID; the template moves from In Progress to Success (usable) or Error.[^s2] Regenerate the template after every TSO change so trials reflect the current build.[^s2]

## Delivering trials

Trailhead describes three delivery routes.[^s5]

- **AgentExchange listing:** the simplest, but only one template can be offered at a time and no SignupRequest record is captured.[^s5]
- **Signup Request:** a standard object holding the prospect's name, company, email, trial username and template, with status history; it can be created manually or via the API.[^s5]
- **Hosted trials on demand:** your own web form calls the SignupRequest API; it must mirror the object's fields and link to the Main Services Agreement.[^s5]

A TSO's templates must be approved through a Partner Community case before they can be used with the SignupRequest API.[^s4][^s5]

## Limits and gotchas

- A TSO can create templates only while it is itself a trial org; one converted to an active, paying org cannot create templates.[^s3]
- The TSO must be 1 GB or smaller, and at most 10 templates can exist per TSO unless Partner Support raises it.[^s3]
- The TSO admin needs a license for the installed solution before a template is created.[^s3]
- Trial orgs last 10 days by default; changing the length requires a request to Salesforce support.[^s3][^s2]
- PII in User object fields such as addresses is scrubbed, but PII in custom objects and fields is copied unchanged.[^s3]
- Environment Hub cannot create branded TSOs; branding needs a TMO.[^s4]

## When to use it

Use Trialforce when prospects should experience a preconfigured, data-rich org rather than a bare install. For a read-only walkthrough, a test drive org created from a template via the Environment Hub may suffice; for a self-serve evaluation in the customer's own org, an installable trial from the listing is simpler.[^s4]

## Connections

Trialforce is part of the partner distribution toolkit around **AgentExchange** and the broader **application lifecycle** of a commercial app.[^s1][^s5] It **depends on** the **Partner Business Org**, where the License Management App and Environment Hub live and where packages are registered with trial license settings.[^s4] It **integrates with** the **Environment Hub**, which can create TSOs and template-based demo orgs, and with the **License Management App**, which tracks trial licenses.[^s4][^s1] Its **SignupRequest API** is the programmatic route for branded sign-up forms.[^s5] Trials usually carry a **managed package** (first- or second-generation), and templates are conceptually close to **sandbox templates**, though they seed new trial orgs rather than sandboxes.[^s4]

## Sources
[^s1]: Salesforce Developers, "Trialforce Key Concepts and Relationships" (ISVforce Guide). https://developer.salesforce.com/docs/platform/isvforce/guide/trialforce-conceptual-overview.html (accessed 2026-11-23)
[^s2]: Salesforce Developers, "Create a Trialforce Template" (ISVforce Guide). https://developer.salesforce.com/docs/platform/isvforce/guide/trialforce-creating-template.html (accessed 2026-11-23)
[^s3]: Salesforce Developers, "Considerations for Trialforce Templates" (ISVforce Guide). https://developer.salesforce.com/docs/platform/isvforce/guide/trialforce-template-considerations.html (accessed 2026-11-23)
[^s4]: Trailhead, "Get Your Orgs Ready" (ISV App Trials). https://trailhead.salesforce.com/content/learn/modules/isv_app_trials/isv_app_trials_ready (accessed 2026-11-23)
[^s5]: Trailhead, "Deliver Your Trial" (ISV App Trials). https://trailhead.salesforce.com/modules/isv_app_trials/units/isv_app_trials_deliver (accessed 2026-11-23)
