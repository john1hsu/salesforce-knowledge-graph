---
id: kt:cloud-computing
type: ExternalConcept
title: Cloud Computing
aliases: [the cloud, cloud services, NIST cloud model]
domain: platform-architecture
summary: >-
  The model, defined by NIST SP 800-145, for on-demand network access to a shared pool of configurable computing
  resources that can be provisioned and released quickly with minimal provider interaction; it is described by five
  essential characteristics, three service models (SaaS, PaaS, IaaS) and four deployment models.
release: "Winter '27"
status: concept
broader: [kt:distributed-computing]
related: [kt:multitenancy, kt:hyperforce, kt:shared-responsibility-model, kt:salesforce-platform, kt:fedramp]
relations:
  - {predicate: hasPart, object: kt:software-as-a-service}
  - {predicate: hasPart, object: kt:platform-as-a-service}
  - {predicate: hasPart, object: kt:infrastructure-as-a-service}
sources:
  - id: s1
    title: "The NIST Definition of Cloud Computing (NIST SP 800-145)"
    publisher: National Institute of Standards and Technology
    url: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf
    type: standards-body
    accessed: 2026-11-11
  - id: s2
    title: "NIST Cloud Computing Reference Architecture (NIST SP 500-292)"
    publisher: National Institute of Standards and Technology
    url: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication500-292.pdf
    type: standards-body
    accessed: 2026-11-11
  - id: s3
    title: "Learn About the Cloud (Cloud Security Engineering)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cloud-security-engineering/learn-about-the-cloud
    type: official-learning
    accessed: 2026-11-11
  - id: s4
    title: "What Is Cloud Computing?"
    publisher: Salesforce
    url: https://www.salesforce.com/ca/cloudcomputing
    type: official-blog
    accessed: 2026-11-11
  - id: s5
    title: "The History of Salesforce"
    publisher: Salesforce Newsroom
    url: https://www.salesforce.com/in/news/stories/the-history-of-salesforce/
    type: official-blog
    accessed: 2026-11-11
created: 2026-11-11
---

# Cloud Computing

Cloud computing is the delivery model the whole Salesforce ecosystem sits on. The reference definition comes from NIST Special Publication 800-145, written by Peter Mell and Timothy Grance and published in September 2011.[^s1] It frames cloud computing as convenient, on-demand network access to a shared pool of configurable resources, such as networks, servers, storage, applications and services, that can be provisioned and released rapidly with minimal management effort or provider interaction.[^s1] NIST states that the model is composed of five essential characteristics, three service models and four deployment models, and that the taxonomy is meant for comparing services rather than prescribing how to build them.[^s1]

## The five essential characteristics

NIST lists five characteristics that every cloud service model shares:[^s1]

- **On-demand self-service**: consumers provision capacity themselves, without a human at the provider.[^s1]
- **Broad network access**: services are reached over standard network mechanisms from phones, tablets, laptops and workstations.[^s1]
- **Resource pooling**: one pool serves many consumers through a multi-tenant model, with resources reassigned dynamically by demand.[^s1]
- **Rapid elasticity**: capacity scales out and in, sometimes automatically, and can look unlimited to the consumer.[^s1]
- **Measured service**: usage is metered (storage, processing, bandwidth, active user accounts) and reported to both sides.[^s1]

Under resource pooling, consumers usually cannot see or control the exact physical location of resources. NIST notes they may still be able to pick a higher-level location such as a country, state or datacenter, which is the hook for data residency choices.[^s1]

## Service and deployment models

The three service models differ in how much of the stack the consumer controls. With Software as a Service the consumer only uses the provider's applications, with Platform as a Service it deploys its own applications on the provider's tools, and with Infrastructure as a Service it runs arbitrary software, including operating systems, on provisioned compute, storage and networks.[^s1] Trailhead's cloud security unit adds that serverless variants such as Backend as a Service and Function as a Service extend this spectrum.[^s3]

The four deployment models describe who the infrastructure is for. A **private cloud** serves a single organization, a **community cloud** serves a group of organizations with shared concerns such as mission or compliance, a **public cloud** is open to the general public on the provider's premises, and a **hybrid cloud** binds two or more of these together with technology that lets data and applications move between them.[^s1] Salesforce's explainer and Trailhead both add **multi-cloud**, using several providers for different needs; Trailhead warns this can reduce visibility across hosts and services.[^s3][^s4]

NIST's companion reference architecture, SP 500-292, names five actors in any cloud arrangement: the cloud consumer, cloud provider, cloud auditor, cloud broker and cloud carrier.[^s2] It is deliberately vendor-neutral and describes what cloud services provide, not how to implement a specific cloud.[^s2]

## Benefits and trade-offs

Salesforce lists convenience, flexibility, lower upfront cost, scalability, reliability and security as the main benefits, while stressing that customers remain responsible for protecting their own data.[^s4] Trailhead frames the risks as downtime when internet services fail, privacy exposure from storing data externally, and a larger attack surface because every component is online.[^s3] Trailhead also traces the model's economics to virtualization, which let one physical server host the workloads of many and so made rented, shared infrastructure viable.[^s3]

## Cloud computing at Salesforce

Salesforce was incorporated on 8 March 1999 and launched in February 2000 under the tagline "The End of Software", selling CRM as a hosted service instead of installed software.[^s5] Its history page says it became the first cloud computing company to pass $1 billion in annual revenue, in fiscal 2009, and that the Force.com platform followed in 2008 so customers could build their own apps on the same architecture.[^s5] Today Salesforce runs its services on Hyperforce, infrastructure built with the major public cloud providers.[^s4]

## Connections

Cloud computing is the parent concept of the three service models, so it **has part** **Software as a Service**, **Platform as a Service** and **Infrastructure as a Service**.[^s1] NIST's resource-pooling characteristic is what **multitenancy** implements on the **Salesforce Platform**, and the location choice that NIST allows is realised by **Hyperforce** regions.[^s1][^s4] The split of control in each service model underlies the **shared responsibility model**, since what the consumer controls is what it must secure.[^s1][^s4] Independent assessment of cloud services is the job SP 500-292 gives the cloud auditor, which links the concept to authorization programmes such as **FedRAMP**.[^s2] Its broader concept is **distributed computing**: shared, networked resources pooled across many machines.[^s1][^s3]

## Sources

[^s1]: NIST, Peter Mell and Timothy Grance, "The NIST Definition of Cloud Computing", SP 800-145 (2011). https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf (accessed 2026-11-11)
[^s2]: NIST, Fang Liu et al., "NIST Cloud Computing Reference Architecture", SP 500-292 (2011). https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication500-292.pdf (accessed 2026-11-11)
[^s3]: Trailhead, "Learn About the Cloud" (Cloud Security Engineering). https://trailhead.salesforce.com/content/learn/modules/cloud-security-engineering/learn-about-the-cloud (accessed 2026-11-11)
[^s4]: Salesforce, "What Is Cloud Computing?". https://www.salesforce.com/ca/cloudcomputing (accessed 2026-11-11)
[^s5]: Salesforce Newsroom, "The History of Salesforce". https://www.salesforce.com/in/news/stories/the-history-of-salesforce/ (accessed 2026-11-11)
