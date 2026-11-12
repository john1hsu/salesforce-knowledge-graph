---
id: kt:software-as-a-service
type: ExternalConcept
title: Software as a Service
aliases: [SaaS, software-as-a-service, SaaS cloud service model, on-demand software]
domain: platform-architecture
summary: >-
  The cloud service model, defined by NIST SP 800-145, in which the consumer uses the provider's applications running
  on cloud infrastructure through a browser or program interface, controlling at most limited user-specific settings;
  Salesforce, founded in 1999 to deliver web-based CRM, is one of the model's early examples.
release: "Winter '27"
status: concept
broader: [kt:cloud-computing]
related: [kt:multitenancy, kt:salesforce-platform, kt:shared-responsibility-model, kt:metadata-driven-architecture, kt:governor-limits]
relations:
  - {predicate: contrastsWith, object: kt:platform-as-a-service}
  - {predicate: contrastsWith, object: kt:infrastructure-as-a-service}
sources:
  - id: s1
    title: "The NIST Definition of Cloud Computing (NIST SP 800-145)"
    publisher: National Institute of Standards and Technology
    url: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf
    type: standards-body
    accessed: 2026-11-12
  - id: s2
    title: "What is Software as a Service (SaaS)?"
    publisher: Salesforce
    url: https://www.salesforce.com/ap/saas/
    type: official-blog
    accessed: 2026-11-12
  - id: s3
    title: "Learn About the Cloud (Cloud Security Engineering)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cloud-security-engineering/learn-about-the-cloud
    type: official-learning
    accessed: 2026-11-12
  - id: s4
    title: "Understand the Salesforce Architecture (Platform Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/starting_force_com/starting_understanding_arch
    type: official-learning
    accessed: 2026-11-12
  - id: s5
    title: "Platform Multitenant Architecture"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/platform-multitenant-architecture
    type: official-docs
    accessed: 2026-11-12
created: 2026-11-12
---

# Software as a Service

Software as a Service (SaaS) is one of the three service models in NIST Special Publication 800-145, *The NIST Definition of Cloud Computing*, by Peter Mell and Timothy Grance, published in September 2011.[^s1] NIST defines it as the capability for a consumer to use a provider's applications that run on a cloud infrastructure. Users reach those applications from many kinds of client device, either through a thin client such as a web browser or through a program interface.[^s1] The consumer does not manage or control the network, servers, operating systems, storage or even individual application capabilities. The one possible exception is limited, user-specific configuration of the application.[^s1]

## How it differs from PaaS and IaaS

SaaS sits at the top of NIST's three service models: the provider runs the whole stack and the consumer only uses the application.[^s1] Under Platform as a Service (PaaS) the consumer deploys its own applications onto the provider's platform, and under Infrastructure as a Service (IaaS) it provisions raw processing, storage and networks and can run arbitrary software.[^s1] Salesforce's explainer frames the same split by who manages what. With SaaS the provider manages the application and the infrastructure under it. With PaaS the provider runs servers and networking while users manage their applications and data. With IaaS users control operating systems, applications and data on virtualized resources.[^s2] Trailhead's cloud security module gives Gmail as its SaaS example and describes the provider as running the infrastructure and offering fully managed services.[^s3]

Every service model shares NIST's five essential characteristics, including resource pooling. NIST describes pooled resources serving many consumers through a multi-tenant model, assigned and reassigned dynamically as demand changes.[^s1] Trailhead makes the economic point: sharing resources in a multitenant cloud lowers the cost of running and maintaining an application, whereas a private cloud is single-tenant.[^s3]

## Commercial model and history

Salesforce describes SaaS as a subscription model in which customers access cloud-hosted software over the internet rather than buying and installing it. The provider hosts, manages and maintains the application, and the model is also called web-based, on-demand or hosted software.[^s2] Its explainer traces the idea back to 1960s and 1970s mainframe terminals and places the modern model in the late 1990s and early 2000s. It names WebEx (1995), NetSuite (1998) and Salesforce (1999, web-based CRM) as early examples.[^s2] Marc Benioff founded Salesforce in 1999 with a mission to end traditional installed software through cloud computing.[^s2] The benefits Salesforce lists include low upfront cost, pay-as-you-go or per-seat subscription pricing, provider-run updates and maintenance, and access from any connected device.[^s2]

## How Salesforce delivers SaaS

Trailhead describes everything Salesforce offers as living in a trusted, multitenant cloud. Customers manage no hardware, every customer gets the same core services regardless of size, and new features arrive through automatic upgrades with no installation.[^s4] The architecture behind that is multitenant and metadata-driven. All tenants (orgs) share one database and schema, with each org-specific row tagged by an OrgID so the kernel keeps tenants apart.[^s5] Customizations such as objects, fields, screens and workflow rules are stored as metadata rather than physical tables or compiled code, and the kernel assembles each tenant's application at runtime.[^s5] That design lets Salesforce change the shared platform without breaking customers: on each release it reruns customers' unit tests, and schema changes are applied online without blocking other orgs.[^s5]

## Gotchas and when it fits

- **You configure; you don't control the stack.** NIST limits SaaS consumers to user-specific settings, so infrastructure tuning is off the table.[^s1]
- **Shared resources come with guardrails.** Salesforce enforces governor limits on CPU time, memory, queries, DML and callouts so that no tenant monopolizes shared capacity.[^s5]
- **Upgrades are not optional.** Features arrive automatically, so plan for testing against each release rather than choosing when to upgrade.[^s4][^s5]
- **The line with PaaS blurs on Salesforce.** Salesforce lists itself as a SaaS example, yet its metadata-driven platform also hosts applications that customers build.[^s2][^s5]

Choose SaaS when an existing application meets the need and you would rather not operate software. Choose PaaS or IaaS when you need to build, host or tune your own runtime.[^s1][^s2]

## Connections

SaaS is a service model of **cloud computing**, its broader concept, and it **contrasts with** **PaaS** and **IaaS**, which hand progressively more of the stack to the customer.[^s1] **Multitenancy** is how Salesforce implements NIST's resource-pooling characteristic for its SaaS products, and the **metadata-driven architecture** is what lets many tenants customize one shared application.[^s1][^s5] **Governor limits** exist to protect that shared capacity.[^s5] The **Salesforce Platform** underpins both Salesforce's SaaS clouds and the custom apps built on it.[^s4] The provider/consumer control split that NIST defines for SaaS is the starting point of the **shared responsibility model**.[^s1]

## Sources

[^s1]: NIST, Peter Mell and Timothy Grance, "The NIST Definition of Cloud Computing", SP 800-145. https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf (accessed 2026-11-12)
[^s2]: Salesforce, "What is Software as a Service (SaaS)?". https://www.salesforce.com/ap/saas/ (accessed 2026-11-12)
[^s3]: Trailhead, "Learn About the Cloud" (Cloud Security Engineering). https://trailhead.salesforce.com/content/learn/modules/cloud-security-engineering/learn-about-the-cloud (accessed 2026-11-12)
[^s4]: Trailhead, "Understand the Salesforce Architecture" (Platform Basics). https://trailhead.salesforce.com/content/learn/modules/starting_force_com/starting_understanding_arch (accessed 2026-11-12)
[^s5]: Salesforce Architects, "Platform Multitenant Architecture". https://architect.salesforce.com/fundamentals/platform-multitenant-architecture (accessed 2026-11-12)
