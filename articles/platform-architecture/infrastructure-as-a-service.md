---
id: kt:infrastructure-as-a-service
type: ExternalConcept
title: Infrastructure as a Service
aliases: [IaaS, infrastructure-as-a-service, IaaS cloud service model]
domain: platform-architecture
summary: >-
  The cloud service model, defined by NIST SP 800-145, in which a provider supplies processing, storage, networks and
  other fundamental computing resources on which the customer deploys and runs arbitrary software, including its own
  operating systems; Salesforce's Hyperforce infrastructure is built on public cloud IaaS.
release: "Winter '27"
status: concept
broader: [kt:cloud-computing]
related: [kt:shared-responsibility-model, kt:multitenancy, kt:data-residency]
relations:
  - {predicate: contrastsWith, object: kt:platform-as-a-service}
  - {predicate: contrastsWith, object: kt:software-as-a-service}
  - {predicate: consumedBy, object: kt:hyperforce}
sources:
  - id: s1
    title: "The NIST Definition of Cloud Computing (NIST SP 800-145)"
    publisher: National Institute of Standards and Technology
    url: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf
    type: standards-body
    accessed: 2026-11-12
  - id: s2
    title: "NIST Cloud Computing Reference Architecture (NIST SP 500-292)"
    publisher: National Institute of Standards and Technology
    url: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication500-292.pdf
    type: standards-body
    accessed: 2026-11-12
  - id: s3
    title: "What is IaaS (Infrastructure as a Service)?"
    publisher: Salesforce
    url: https://www.salesforce.com/platform/iaas/
    type: official-blog
    accessed: 2026-11-12
  - id: s4
    title: "Learn About the Cloud (Cloud Security Engineering)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cloud-security-engineering/learn-about-the-cloud
    type: official-learning
    accessed: 2026-11-12
  - id: s5
    title: "Behind the Scenes of Hyperforce: Salesforce's Infrastructure for the Public Cloud"
    publisher: Salesforce Engineering
    url: https://engineering.salesforce.com/behind-the-scenes-of-hyperforce-salesforces-infrastructure-for-the-public-cloud-429309542d8e
    type: official-blog
    accessed: 2026-11-12
  - id: s6
    title: "Hyperforce: Public Cloud Infrastructure"
    publisher: Salesforce
    url: https://www.salesforce.com/platform/public-cloud-infrastructure/
    type: official-blog
    accessed: 2026-11-12
created: 2026-11-12
---

# Infrastructure as a Service

Infrastructure as a Service (IaaS) is the lowest-level of the three cloud service models in NIST Special Publication 800-145, *The NIST Definition of Cloud Computing*, by Peter Mell and Timothy Grance (September 2011).[^s1] Under IaaS, the provider gives the consumer processing, storage, networks and other fundamental computing resources, and the consumer can deploy and run arbitrary software on them, including operating systems and applications.[^s1] The consumer does not manage the underlying cloud infrastructure. It does control the operating systems, storage and deployed applications, and it may have limited control over some networking components such as host firewalls.[^s1]

## How it works

NIST's companion reference architecture, SP 500-292, describes what each side does. The IaaS provider acquires the physical servers, networks, storage and hosting facilities. It runs the cloud software that exposes them through abstractions such as virtual machines and virtual network interfaces, and it controls the host operating system and the hypervisors.[^s2] The consumer takes full responsibility for its guest operating systems, middleware and applications.[^s2] Typical IaaS consumers are system developers, system administrators and IT managers who install, manage and monitor infrastructure services.[^s2]

Virtualization is the core mechanism. Salesforce's explainer describes IaaS as dividing physical hardware into virtual machines, and lists compute, block, file and object storage, networking (VPNs, firewalls, load balancers), APIs and orchestration tools, and monitoring as its main components.[^s3] A Trailhead unit on cloud security puts it more simply: IaaS lets customers run virtualized applications on rented infrastructure instead of their own hardware.[^s4]

Billing follows NIST's measured-service characteristic. SP 500-292 says IaaS consumers are typically charged for the amount or duration of what they use, such as CPU hours, stored data volume and duration, network bandwidth and IP addresses.[^s2] The other essential characteristics also apply: on-demand self-service, broad network access, resource pooling across tenants and rapid elasticity.[^s1]

## Compared with PaaS and SaaS

The three models differ in how much of the stack the customer runs. Salesforce's comparison says that with IaaS the customer manages the operating system, runtime and applications while the provider handles the hardware. With PaaS the customer manages only the application, and with SaaS the provider manages everything.[^s3] NIST states the trade-off in terms of control: IaaS consumers control more of the software stack, including the operating system and network, than PaaS or SaaS consumers do.[^s2] The service model is independent of the deployment model, so IaaS can be offered as a private, community, public or hybrid cloud.[^s1]

## Gotchas and when it fits

- **More control means more work.** Patching guest operating systems, middleware and runtimes is the consumer's job under IaaS, not the provider's.[^s2]
- **Security is split, not handed off.** The provider secures hardware, host OS and hypervisor, while the consumer secures everything it deploys on top.[^s2][^s4]
- **Portability takes planning.** NIST notes that moving IaaS workloads may require capturing VM images and removing or documenting provider-specific extensions.[^s2]

Salesforce lists development and test environments, high-performance computing, disaster recovery and e-commerce hosting as common IaaS uses.[^s3] For most Salesforce customers, IaaS is something they consume indirectly: the platform runs on it, but they build on the PaaS and SaaS layers above it.[^s6]

## IaaS and Salesforce

Hyperforce is Salesforce's infrastructure architecture for the public cloud, and Salesforce describes it as running on major public cloud infrastructure.[^s6] Salesforce Engineering explains that it treats public cloud IaaS as a foundation and takes a cloud-agnostic approach so infrastructure can be deployed with different providers.[^s5] On top of that IaaS, Hyperforce defines infrastructure as version-controlled code and replaces rather than patches resources (immutable infrastructure). It also applies zero-trust access and spreads compute across at least three availability zones in a region.[^s5] Because public cloud regions exist in many countries, Salesforce can offer in-country org placement in places such as the U.S., U.K., Germany, India and Japan.[^s6]

## Connections

IaaS is a service model of **cloud computing**, its broader concept, and it **contrasts with** **Platform as a Service** and **Software as a Service**.[^s1] It is **consumed by** **Hyperforce**, which runs Salesforce on public cloud infrastructure.[^s5][^s6] The provider/consumer control split NIST defines for IaaS is the starting point of the **shared responsibility model**.[^s2] NIST's resource-pooling characteristic is the same multi-tenant idea behind Salesforce **multitenancy**, applied at the infrastructure layer.[^s1] Public cloud regions are what make **data residency** choices on Hyperforce possible.[^s6]

## Sources

[^s1]: NIST, Peter Mell and Timothy Grance, "The NIST Definition of Cloud Computing", SP 800-145. https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf (accessed 2026-11-12)
[^s2]: NIST, Fang Liu et al., "NIST Cloud Computing Reference Architecture", SP 500-292. https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication500-292.pdf (accessed 2026-11-12)
[^s3]: Salesforce, "What is IaaS (Infrastructure as a Service)?". https://www.salesforce.com/platform/iaas/ (accessed 2026-11-12)
[^s4]: Trailhead, "Learn About the Cloud" (Cloud Security Engineering). https://trailhead.salesforce.com/content/learn/modules/cloud-security-engineering/learn-about-the-cloud (accessed 2026-11-12)
[^s5]: Salesforce Engineering, Srinivas Tallapragada and Laura Lindeman, "Behind the Scenes of Hyperforce: Salesforce's Infrastructure for the Public Cloud" (2022). https://engineering.salesforce.com/behind-the-scenes-of-hyperforce-salesforces-infrastructure-for-the-public-cloud-429309542d8e (accessed 2026-11-12)
[^s6]: Salesforce, "Hyperforce: Public Cloud Infrastructure". https://www.salesforce.com/platform/public-cloud-infrastructure/ (accessed 2026-11-12)
