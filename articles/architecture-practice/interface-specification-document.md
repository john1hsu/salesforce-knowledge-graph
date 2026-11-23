---
id: kt:interface-specification-document
type: Concept
title: Interface Specification Document
aliases: [ISD, interface specification, integration specification, interface control document, integration interface spec]
domain: architecture-practice
summary: >-
  A per-interface design document in which a Salesforce architect specifies one integration between Salesforce and
  another system: source and target, sync or async type, trigger, volume and frequency, data formats and field mapping,
  transport, security, failover, monitoring and reconciliation. It is linked from the technical specification.
release: "Winter '27"
status: concept
broader: [kt:solution-design-document]
related: [kt:system-landscape-diagrams, kt:integration-security, kt:named-credentials, kt:mulesoft-anypoint-platform, kt:commerce-cloud, kt:integration-patterns-request-reply-fire-and-forget]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: dependsOn, object: kt:integration-patterns}
  - {predicate: partOf, object: kt:solution-design-document}
sources:
  - id: s1
    title: "Get Started with the Technical Project Documentation (Project Documentation for Salesforce B2C Commerce Technical Architects)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/b2c-project-docs-for-technical-architects/b2c-technical-project-docs
    type: official-learning
    accessed: 2026-11-23
  - id: s2
    title: "Document the Architectural Landscape (Project Documentation for Salesforce B2C Commerce Technical Architects)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/b2c-project-docs-for-technical-architects/b2c-doc-architectural-landscape
    type: official-learning
    accessed: 2026-11-23
  - id: s3
    title: "Integration Patterns Overview"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/fundamentals/integration-patterns
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "Integration Patterns and Practices (Version 64.0, Summer '25)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/256/latest/en-us/sfdc/pdf/integration_patterns_and_practices.pdf
    type: official-docs
    accessed: 2026-11-23
created: 2026-11-23
---

# Interface Specification Document

An **Interface Specification Document (ISD)** describes, in build-ready detail, one interface between Salesforce and another system. Trailhead's project-documentation module for B2C Commerce technical architects treats it as a separate deliverable: the technical specification lists every web service in a summary table (service, type, description), and the per-service detail lives in the ISD.[^s1] The technical specification itself carries sections for integration and data feeds and for interface specifications and schedules, and it should link to each ISD rather than repeat it.[^s1][^s2]

## What goes in it

Trailhead's ISD template is organized per provider or interface and asks the architect to fill in these fields:[^s2]

- **Identity and scope**: interface name, description, and whether the interface is new or already exists.[^s2]
- **Direction and style**: source system, target system, and whether the exchange is synchronous or asynchronous.[^s2]
- **Behaviour**: the content exchanged, the trigger that starts it, and its expected volume and frequency.[^s2]
- **Data contract**: source and target data formats plus the field-level mapping between them.[^s2]
- **Operations**: transport, security and administration, failover and monitoring, and data reconciliation.[^s2]
- **Housekeeping**: open issues and any additional information, such as sample requests and responses or vendor details.[^s2]

Alongside the ISDs, the architect keeps a third-party integration summary that records each integration's type (payment, tax, shipping, order management), provider, credentials link, technology, and input and output formats.[^s2] File-based interfaces over SFTP or WebDAV need their own notes on login, home directory and folder structure, because those channels carry asynchronous integrations with outside vendors and systems.[^s1]

## How it fits the design process

The ISD sits downstream of the landscape view. The architecture diagram identifies the system of record for each data item, and the data flow diagram shows how often data moves and every hop it touches, for example PIM to middleware to SFTP to the platform.[^s2] Batch feeds belong in a scheduled-jobs table (name, schedule, from, to, full or delta, resources), and Trailhead advises delta feeds wherever possible because they are smaller, faster and more resilient to network interruptions.[^s2] The ISD then turns each arrow on those diagrams into a contract that a developer can build and a tester can verify.[^s1]

Salesforce's integration patterns supply the vocabulary for the ISD's type and timing fields. Patterns are classified by type (process, data or virtual integration) and by timing (synchronous blocking calls versus asynchronous queued or message-based ones).[^s3][^s4] Each pattern also prompts questions an ISD should answer, such as whether Salesforce must wait for the reply, what volume is expected, and who handles errors: in request and reply, the caller manages error handling.[^s4]

## Gotchas

- **Idempotency**: Salesforce cannot guarantee a single call, so the spec should say how the receiver de-duplicates repeated messages.[^s4]
- **Volume fit**: request and reply is meant for small-volume, real-time work; bulk data belongs in a batch synchronization interface.[^s4]
- **Middleware boundaries**: Salesforce has no native protocol conversion, so the ISD should state where transformation and orchestration run.[^s3][^s4]
- **Quotas**: the technical specification should flag API quota risks, such as too many outbound HTTP calls during order submission.[^s1]
- **Ownership**: the merchant handles business, legal and financial coordination with providers; the ISD records technical facts only.[^s2]

## Connections

The ISD is **part of** the solution design document, its **broader** node, which links to it for integration detail, and it is written by the Salesforce architect.[^s1][^s2] Its source, target and system-of-record entries come from system landscape diagrams, and it **depends on** the choice among Salesforce integration patterns such as request and reply or fire and forget.[^s2][^s3] The security and transport fields are where decisions about integration security and Named Credentials get recorded, and the transformation notes often name middleware such as MuleSoft Anypoint Platform.[^s2][^s4] The Trailhead template comes from Commerce Cloud projects but applies to any Salesforce integration.[^s1]

## Sources
[^s1]: Salesforce Trailhead, "Get Started with the Technical Project Documentation". https://trailhead.salesforce.com/content/learn/modules/b2c-project-docs-for-technical-architects/b2c-technical-project-docs (accessed 2026-11-23)
[^s2]: Salesforce Trailhead, "Document the Architectural Landscape". https://trailhead.salesforce.com/content/learn/modules/b2c-project-docs-for-technical-architects/b2c-doc-architectural-landscape (accessed 2026-11-23)
[^s3]: Salesforce Architects, "Integration Patterns Overview". https://architect.salesforce.com/fundamentals/integration-patterns (accessed 2026-11-23)
[^s4]: Salesforce, "Integration Patterns and Practices" (Version 64.0, Summer '25). https://resources.docs.salesforce.com/256/latest/en-us/sfdc/pdf/integration_patterns_and_practices.pdf (accessed 2026-11-23)
