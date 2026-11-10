---
id: kt:platform-as-a-service
type: ExternalConcept
title: Platform as a Service
aliases: [PaaS, platform-as-a-service, PaaS cloud service model]
domain: platform-architecture
summary: >-
  The cloud service model, defined by NIST SP 800-145, in which a provider runs the network, servers, operating systems
  and storage while the customer deploys and controls its own applications using the provider's languages, libraries,
  services and tools; the Salesforce Platform and Heroku are Salesforce's two PaaS offerings.
release: "Winter '27"
status: concept
broader: [kt:cloud-computing]
related: [kt:salesforce-platform, kt:heroku, kt:multitenancy, kt:shared-responsibility-model]
relations:
  - {predicate: contrastsWith, object: kt:infrastructure-as-a-service}
  - {predicate: contrastsWith, object: kt:software-as-a-service}
sources:
  - id: s1
    title: "The NIST Definition of Cloud Computing (NIST SP 800-145)"
    publisher: National Institute of Standards and Technology
    url: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf
    type: standards-body
    accessed: 2026-11-10
  - id: s2
    title: "SP 800-145, The NIST Definition of Cloud Computing (publication page)"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/pubs/sp/800/145/final
    type: standards-body
    accessed: 2026-11-10
  - id: s3
    title: "What Is PaaS (Platform as a Service)?"
    publisher: Salesforce
    url: https://www.salesforce.com/in/paas/
    type: official-blog
    accessed: 2026-11-10
  - id: s4
    title: "Salesforce Developers Blog post on Platform as a Service (Summer '07 release)"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2007/07/whats-paasd-is
    type: official-blog
    accessed: 2026-11-10
  - id: s5
    title: "How Heroku Works"
    publisher: Heroku Dev Center
    url: https://devcenter.heroku.com/articles/how-heroku-works
    type: official-docs
    accessed: 2026-11-10
  - id: s6
    title: "Peek Under the Hood of Heroku (Heroku Enterprise Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/heroku_enterprise_baiscs/under_the_hood
    type: official-learning
    accessed: 2026-11-10
created: 2026-11-10
---

# Platform as a Service

Platform as a Service (PaaS) is one of the three cloud service models in NIST Special Publication 800-145, *The NIST Definition of Cloud Computing*, written by Peter Mell and Tim Grance and published as final in September 2011.[^s1][^s2] That definition describes cloud computing through five essential characteristics, three service models and four deployment models.[^s2] Under PaaS, the consumer deploys applications it created or acquired onto the provider's cloud infrastructure, built with the programming languages, libraries, services and tools that the provider supports.[^s1] The consumer controls those deployed applications and perhaps some settings of the hosting environment. It does not manage or control the underlying network, servers, operating systems or storage.[^s1]

## How it differs from IaaS and SaaS

NIST places PaaS between the other two service models.[^s1] Under Infrastructure as a Service (IaaS), the consumer provisions processing, storage and networks and can run arbitrary software, including its own operating systems.[^s1] Under Software as a Service (SaaS), the consumer simply uses the provider's applications through a browser or program interface, with at most limited user-specific configuration.[^s1] Salesforce's own explainer draws the same line as a split of responsibilities. With IaaS the customer still manages the operating system, middleware, runtime and applications. With PaaS the customer manages only its applications and data. With SaaS the provider runs the whole stack.[^s3]

The service model is separate from the deployment model. A PaaS can run on a private, community, public or hybrid cloud.[^s1] NIST's essential characteristics apply to every model: on-demand self-service, broad network access, resource pooling, rapid elasticity and measured service. NIST explicitly describes resource pooling as serving multiple consumers through a multi-tenant model.[^s1]

## PaaS at Salesforce

Salesforce has used the PaaS label for its developer platform since at least its Summer '07 release. A Salesforce developer blog post from that time presented Apex Code for programmers and Intelligent Workflow for non-programmers as PaaS graduating from preview to product.[^s4] The same post argued that a real platform lets independent developers build applications that compete with the vendor's own products. Hosted macros or scripts that only customize one application do not meet that bar.[^s4] Today Salesforce markets the Salesforce Platform as an enterprise PaaS that covers both low-code automation and scalable custom development.[^s3] Its explainer also lists sub-types such as low-code/no-code PaaS, integration PaaS (iPaaS) and database PaaS.[^s3]

Heroku is Salesforce's general-purpose PaaS for code written in many languages. Developers push source code, buildpacks compile it into a build artifact, and the artifact is combined with config vars and add-ons into a numbered release that runs on dynos, which are isolated Unix containers.[^s5] The developer controls the code, the Procfile, dyno counts and types, config vars, add-ons and rollbacks. Heroku manages the operating system, the build execution, dyno lifecycle and recovery, request routing and log collection.[^s5] Trailhead describes dynos the same way, as managed runtime containers that run on Linux, and notes that Heroku fully manages the infrastructure under add-ons such as Heroku Postgres.[^s6]

## Gotchas and when it fits

- **You give up control of the stack.** NIST's definition means you cannot tune the operating system or storage. You get the provider's languages and tools, along with its limits.[^s1]
- **Platform conventions shape your design.** Heroku dynos have an ephemeral filesystem, so local file changes disappear on restart and shared state belongs in a database or other add-on.[^s5]
- **The two Salesforce PaaS offerings fit different workloads.** Use the Salesforce Platform when an app needs Salesforce data and declarative tools. Use Heroku when you need arbitrary language runtimes on containers that you scale yourself.[^s3][^s5]

PaaS suits teams that want to ship applications without operating infrastructure. Salesforce cites faster delivery, less maintenance and built-in security among the benefits.[^s3] Choose IaaS when you need operating-system-level control. Choose SaaS when an existing application already meets the need.[^s1][^s3]

## Connections

PaaS is a service model of **cloud computing**, its broader concept, and it **contrasts with** **IaaS** and **SaaS**.[^s1] The **Salesforce Platform** is Salesforce's flagship PaaS, and **Heroku** is its container-based PaaS.[^s3][^s5] The **multitenancy** of the Salesforce Platform is one implementation of NIST's resource-pooling characteristic.[^s1] The provider/consumer control split that NIST defines for each service model underlies the **shared responsibility model** used in cloud security and compliance.[^s1]

## Sources

[^s1]: NIST, Peter Mell and Timothy Grance, "The NIST Definition of Cloud Computing", SP 800-145. https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf (accessed 2026-11-10)
[^s2]: NIST CSRC, "SP 800-145, The NIST Definition of Cloud Computing". https://csrc.nist.gov/pubs/sp/800/145/final (accessed 2026-11-10)
[^s3]: Salesforce, "What Is PaaS (Platform as a Service)?". https://www.salesforce.com/in/paas/ (accessed 2026-11-10)
[^s4]: Salesforce Developers Blog, post on Platform as a Service for the Summer '07 release (2007). https://developer.salesforce.com/blogs/2007/07/whats-paasd-is (accessed 2026-11-10)
[^s5]: Heroku Dev Center, "How Heroku Works". https://devcenter.heroku.com/articles/how-heroku-works (accessed 2026-11-10)
[^s6]: Trailhead, "Peek Under the Hood of Heroku" (Heroku Enterprise Basics). https://trailhead.salesforce.com/heroku_enterprise_baiscs/under_the_hood (accessed 2026-11-10)
