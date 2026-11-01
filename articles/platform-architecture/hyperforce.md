---
id: kt:hyperforce
type: Product
title: Hyperforce
aliases: [Salesforce Hyperforce, Hyperforce infrastructure, Hyperforce migration]
domain: platform-architecture
summary: >-
  Salesforce's current-generation, public-cloud infrastructure, defined and managed as code, that replaces
  Salesforce's first-party data centers and hosts orgs in isolated cells across regional Hyperforce instances.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:multitenancy, kt:government-cloud-plus, kt:sandbox-types, kt:platform-events]
relations:
  - {predicate: enables, object: kt:data-residency}
  - {predicate: dependsOn, object: kt:my-domain}
sources:
  - id: s1
    title: "The Salesforce Platform - Transformed for Tomorrow | Get Started with Fundamentals"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-transformation
    type: official-docs
    accessed: 2026-11-01
  - id: s2
    title: "Salesforce Hyperforce — General Information, FAQ, Migration Guide, and Security Overview"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000388902&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-01
  - id: s3
    title: "How to Prepare for a First-Party to Hyperforce Salesforce Core Org Migration"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000386897&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-01
  - id: s4
    title: "Upgrade to Hyperforce with Confidence Using Hyperforce Assistant"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2023/upgrade-to-hyperforce-with-confidence-using-hyperforce-assistant
    type: official-blog
    accessed: 2026-11-01
created: 2026-11-01
---

# Hyperforce

Hyperforce is the current generation of Salesforce's infrastructure. It is built to run on public cloud providers worldwide, and it ends Salesforce's nearly 25-year reliance on its own first-party data centers.[^s1] Salesforce designed it for elastic scale, global data residency, higher availability, security and regulatory compliance. It also gives every Salesforce product one standard infrastructure, which speeds up integrating acquired products.[^s1] Unlike the old data centers, Hyperforce is defined and managed as code. Running on Hyperforce costs customers nothing extra.[^s2]

## How it works

**Instances, regions and operating zones.** The Hyperforce Foundation is made up of Hyperforce Instances spread across countries. Each instance maps to one availability region and can run independently of the others. Instances can be grouped into an Operating Zone to meet data residency and operational requirements.[^s1] Inside an instance, *foundational* functional domains provide shared services such as authentication, logging and monitoring. *Business* domains host products such as Sales Cloud and Service Cloud.[^s1]

**Cells.** A cell is a repeatable unit of service delivery. It is what used to be called a Salesforce instance, or pod, and it holds one or more orgs. A cell is both a scale unit and a blast-radius boundary. Supercells group several cells that share services.[^s1] A group of instances that share a control plane is called a grid. Grids are designed so that data can't leak between them, and an air-gapped control plane exists for environments that need extra safeguards.[^s1]

**Resilience.** Mission-critical services and data are replicated across at least three availability zones. Backups are copied to other suitable Hyperforce instances.[^s1] Salesforce's FAQ adds that a failure in one zone doesn't affect the others.[^s2]

**Zero-trust security.** Services talk to each other over a service mesh using mutual TLS. Engineers get just-in-time, role-based access, and data is encrypted in transit and at rest. Only the edge security group is exposed to the internet. The regional Hyperforce Edge terminates TLS and applies web application firewall policies before traffic reaches internal endpoints.[^s1] Infrastructure is declared as code and shipped as immutable, digitally signed container artifacts.[^s1]

**Cloud providers.** According to Salesforce's FAQ, Hyperforce runs on AWS today, and Google Cloud support is planned to start in late 2026. Some products may stay on AWS until they become available on Google Cloud.[^s2]

## Migration and gotchas

Most orgs reach Hyperforce through a Salesforce-scheduled migration. Customers get notice 30 days ahead and a reminder 15 days before. The notice includes the org ID, the date and the new instance name, and the move happens in the Preferred Maintenance Window.[^s2] Starting July 1, 2026, migrations can no longer be deferred.[^s2][^s3] During the move, a production org is read-only for about three hours.[^s2] Sandboxes are fully inaccessible during the window, and password resets don't work while the org is read-only.[^s3]

Preparation checklist from Salesforce's guidance:

- **Run Hyperforce Assistant** in Setup. It became generally available in Summer '23 in both sandboxes and production. Its automated checks scan code for hard-coded instance references such as `na14.salesforce.com`, test connectivity to the target instance, and confirm that enhanced domains are enabled.[^s4]
- **Remove instance-specific URLs and certificate pinning.** The instance name changes, and pinned certificates from the source instance aren't valid on the target. Record IDs don't change.[^s3]
- **Avoid IP allowlisting.** Salesforce recommends alternatives. If you must allowlist, use the published Hyperforce ranges for the target cloud.[^s3] Salesforce Express Connect doesn't work with Hyperforce. On AWS, the suggested option is Direct Connect with a public virtual interface.[^s2]
- **Mind timing.** Don't start large jobs within 72 hours of the window, and resubmit any Bulk API jobs that fail. Don't request a Full sandbox refresh within two weeks of the migration.[^s3]
- **Event data doesn't carry over.** Platform events can't be published while the org is read-only. Events published before the migration, and their 72-hour replay window, don't move with the org.[^s3]
- **After cutover**, restart integrations to clear DNS caches and check that matching and duplicate rules reactivated. Event Monitoring has no logs for the migration days. OAuth refresh tokens stay valid.[^s3] Once the org activates on the target, it can't go back to the source.[^s3]

## Connections

Hyperforce is the physical layer under the **Salesforce Platform**. It is where **multitenancy** is carried out: each org lives in a cell that isolates its failures from other tenants.[^s1] It **enables data residency** by letting customers choose the region where their data lives.[^s2] Migration readiness **depends on My Domain**, since Hyperforce Assistant checks for enhanced domains and hard-coded instance URLs.[^s4] It relates to **Government Cloud Plus**, which has its own Hyperforce IP ranges.[^s3] It also relates to **sandbox types**, whose refresh timing must avoid the migration window, and to **platform events**, whose retained events are lost during the move.[^s3]

## Sources

[^s1]: Salesforce Architects, "The Salesforce Platform - Transformed for Tomorrow | Get Started with Fundamentals". https://architect.salesforce.com/fundamentals/platform-transformation (accessed 2026-11-01)
[^s2]: Salesforce Help, "Salesforce Hyperforce — General Information, FAQ, Migration Guide, and Security Overview" (KB 000388902). https://help.salesforce.com/s/articleView?id=000388902&language=en_US&type=1 (accessed 2026-11-01)
[^s3]: Salesforce Help, "How to Prepare for a First-Party to Hyperforce Salesforce Core Org Migration" (KB 000386897). https://help.salesforce.com/s/articleView?id=000386897&language=en_US&type=1 (accessed 2026-11-01)
[^s4]: Salesforce Admins Blog, "Upgrade to Hyperforce with Confidence Using Hyperforce Assistant" (2023). https://admin.salesforce.com/blog/2023/upgrade-to-hyperforce-with-confidence-using-hyperforce-assistant (accessed 2026-11-01)
