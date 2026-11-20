---
id: kt:pod-and-instance-architecture
type: Concept
title: Salesforce Instances and Pods
aliases: [Salesforce instance, Salesforce pod, org instance, instance name, Hyperforce cell]
domain: platform-architecture
summary: >-
  A Salesforce instance (historically called a pod, and a cell on Hyperforce) is the unit of shared infrastructure
  that hosts a set of customer orgs. Its name, such as NA01 or GBR10, tells you where the org runs and which
  status and maintenance notices apply to it.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform, kt:multitenancy]
related: [kt:trust-and-status-site, kt:my-domain, kt:sandbox-types, kt:instance-refresh-and-org-migration, kt:data-residency]
relations:
  - {predicate: partOf, object: kt:hyperforce}
sources:
  - id: s1
    title: "View Instance Information for Your Salesforce Organization"
    publisher: Salesforce Help
    url: https://help.salesforce.com/HTViewSolution?id=000002889
    type: official-docs
    accessed: 2026-11-20
  - id: s2
    title: "The Salesforce Platform - Transformed for Tomorrow"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-transformation
    type: official-docs
    accessed: 2026-11-20
  - id: s3
    title: "Get System Performance and Maintenance Information with My Domain (Identity Implementation Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_get_system_info.htm
    type: official-docs
    accessed: 2026-11-20
created: 2026-11-20
---

# Salesforce Instances and Pods

A **Salesforce instance** is the block of shared infrastructure where a group of customer orgs physically runs. Older Salesforce material calls this unit a **pod**. On Hyperforce, Salesforce's architects describe the same unit as a **Hyperforce Cell**, which they say was formerly known as a pod and which corresponds to what was traditionally called a Salesforce instance, home to one or more orgs.[^s2] Every org belongs to exactly one instance at a time, and that instance's name is how Salesforce reports availability, incidents and maintenance for the org.[^s1][^s3]

## How it works

**Cells as scale and failure units.** A cell is both a unit of scale and a blast-radius boundary: when something fails inside one cell, the tenants of other cells are not affected. Salesforce adds capacity by adding cells rather than by growing a single one without limit. Supercells group several cells that share services, which marks out a larger blast radius for those shared components.[^s2]

**Regional placement and resilience.** On Hyperforce, a regional **Hyperforce Instance** is a deployment that contains many cells. Each one maps to one availability region and is spread and replicated across at least three availability zones. Backups are copied to other suitable Hyperforce Instances for business continuity and regulatory compliance.[^s2] Note the naming clash: a classic "Salesforce instance" such as NA01 is the equivalent of a single cell, not of a whole regional Hyperforce Instance.[^s2]

**Reading an instance name.** The instance name encodes the infrastructure type. Names that start with two letters (for example AP0) run on Salesforce-managed first-party data centers. Names that start with three letters (for example GBR10) run on Hyperforce. A trailing S marks a sandbox instance, so JPN156S hosts sandboxes paired with production instance JPN156.[^s1] Salesforce Help doesn't list the cloud provider in the name; to learn whether a Hyperforce instance runs on AWS or Google Cloud, you contact Salesforce Customer Support.[^s1]

## Finding your org's instance

There are two quick ways to find it:

- In Setup, search Quick Find for Company Information and read the **Instance** field in Organization Detail.[^s1][^s3]
- On Salesforce Status (status.salesforce.com), search for your My Domain name, not the full URL. The result shows the instance next to the domain.[^s1][^s3]

For details such as the instance's location and its maintenance windows, Salesforce Help points to my.trust.salesforce.com.[^s1]

## Limits and gotchas

- **Instances change.** Salesforce creates new cells and refreshes existing ones in place, so an org's instance is not permanent.[^s2]
- **Don't hard-code instance hosts.** Customers reach their org through My Domain URLs such as acme.my.salesforce.com, which route to wherever the org currently lives.[^s2]
- **Production and sandbox differ.** A sandbox lives on its own S-suffixed instance, so its maintenance and status can differ from its production org's.[^s1]

## When it matters

Most admins never think about the instance until something goes wrong. It matters when you check whether an outage is yours or the platform's, when you plan around maintenance windows, when you answer data-residency questions about where an org runs, and when you prepare for a Salesforce-led move to a new instance.[^s1][^s2][^s3]

## Connections

Instances are the physical expression of **multitenancy**: many orgs share one cell's application and database tier while staying logically isolated, and they are part of **Hyperforce**, whose cells are the modern form of the pod.[^s2] The **Salesforce Trust and Status site** reports health per instance, and **My Domain** is the stable address that hides the instance from users and integrations.[^s1][^s3] **Sandbox types** land on separate sandbox instances.[^s1] An **instance refresh or org migration** is the event that changes an org's instance, and the regional placement of instances is what underpins **data residency**.[^s2]

## Sources

[^s1]: Salesforce Help, "View Instance Information for Your Salesforce Organization". https://help.salesforce.com/HTViewSolution?id=000002889 (accessed 2026-11-20)
[^s2]: Salesforce Architects, "The Salesforce Platform - Transformed for Tomorrow". https://architect.salesforce.com/fundamentals/platform-transformation (accessed 2026-11-20)
[^s3]: Salesforce, "Get System Performance and Maintenance Information with My Domain (Identity Implementation Guide)". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_get_system_info.htm (accessed 2026-11-20)
