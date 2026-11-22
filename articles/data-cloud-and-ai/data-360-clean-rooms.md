---
id: kt:data-360-clean-rooms
type: Feature
title: Data 360 Clean Rooms
aliases: [Data Cloud Clean Rooms, Salesforce Clean Rooms, Data 360 clean room collaboration, data clean rooms in Data 360]
domain: data-cloud-and-ai
summary: >-
  A privacy-safe collaboration feature of Data 360 in which a provider and a consumer org match their audiences
  through a template that fixes the match keys, permitted queries and result recipients, so only aggregated,
  thresholded insights come back and neither side's raw records leave its control.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:zero-copy-data-sharing, kt:zero-copy-data-federation, kt:data-cloud-segmentation, kt:data-cloud-activation, kt:identity-resolution]
relations:
  - {predicate: dependsOn, object: kt:data-model-objects}
  - {predicate: dependsOn, object: kt:data-streams}
  - {predicate: integratesWith, object: kt:aws-clean-rooms}
  - {predicate: implements, object: kt:data-clean-room}
sources:
  - id: s1
    title: "Learn about Data 360 Clean Rooms"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005225176&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-22
  - id: s2
    title: "Understanding Clean Rooms: Security, Roles, and Use Cases (Get Started with Data 360 Clean Rooms)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-360-clean-rooms-quick-look/get-started-with-data-360-clean-rooms
    type: official-learning
    accessed: 2026-11-22
  - id: s3
    title: "Data 360 Clean Room Collaboration Process Overview"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=data.c360_a_crc_how_clean_room_works.htm&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s4
    title: "Prepare Your Data for a Clean Room"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=data.c360_a_crc_prepare_data.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s5
    title: "Collaborate in a Clean Room"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=data.c360_a_crc_collaborate_in_clean_room.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-22
  - id: s6
    title: "The New Era of Data Collaboration: Introducing Salesforce Data 360 Clean Rooms"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/introducing-data360-clean-rooms/
    type: official-blog
    accessed: 2026-11-22
created: 2026-11-22
---

# Data 360 Clean Rooms

Data 360 Clean Rooms is Salesforce's data clean room: a secure, rules-governed environment where two companies compare customer groups without handing each other their customer records. Salesforce describes the data as encrypted and kept inside the clean room, with privacy-enhancing technologies enforcing what each party may learn.[^s1] Trailhead frames it as a neutral space where you get the insight but your raw customer data stays under your control.[^s2] Salesforce announced the product as generally available in February 2026 and positions it as built on Data 360's zero copy capabilities, so partner data is analysed where it lives rather than copied in.[^s6]

## Roles and templates

Every collaboration has two parties. The **provider** (also called the publisher) owns valuable behavioural data, often ad inventory such as a media publisher's audience, and controls access by opting in to or defining a use case template. The **consumer** (also called the advertiser) starts collaborations and queries the datasets the provider has approved.[^s1][^s2] The **collaboration template** is the contract: created by Salesforce or by the provider as a JSON file, it defines the match keys (usually hashed email or phone), the preapproved SQL queries, who contributes data, who runs queries and who sees results, and the required and optional fields.[^s1][^s2] Salesforce-provided use cases include segment overlap analysis, automated reports, multi-key matching (for example email plus device ID) and cross-cloud collaboration with AWS Clean Rooms.[^s1]

## How a collaboration works

The provider builds a clean room package in a Developer Edition packaging org and publishes it on AppExchange; alternatively a consumer can add a trusted provider directly to an allow list using its org ID, domain URL and offcore tenant ID.[^s1][^s3] Both parties then map their attributes to the template's fields, and the collaboration only becomes active once both mappings are complete. The consumer creates the collaboration, which sends the provider an invitation; when the provider accepts, its status becomes Active and either party can run the permitted queries, whose aggregated results are stored in a data model object or delivered as the template defines.[^s3] In the activation variant, Data 360 writes the matched audience list to the provider's Amazon S3 bucket for use in a demand-side platform instead of a DMO.[^s3]

Raw records are not moved. Between two Data 360 orgs the feature uses metadata association and federated querying, and in cross-cloud collaborations the data stays in place with AWS Clean Rooms; each org keeps ownership of its data.[^s1][^s3] Salesforce's blog describes the matching step as a private join on encrypted keys, such as hashed emails, that neither party can see.[^s6]

## Preparing data

Only accelerated data streams can feed a clean room; file federation and live-query federation are not supported. Profile data needs a unique identifier such as email, phone or device ID, and should be SHA256-hashed after normalising to lowercase and stripping whitespace.[^s4] The documented pattern is a batch data transform that builds a match-key DMO from the Contact Point Email and Contact Point Phone DMOs, hashes the values and drops the plaintext column, then relates it N:1 to Individual; identity resolution is optional. The shared unit is a published segment on the Individual or Unified Individual DMO.[^s4]

## Limits and gotchas

- Only segments can be shared; individual records may be shared only in hashed form and only with the party that owns them.[^s2]
- Providers set minimum thresholds on aggregate results to stop small groups being singled out; the help article's example is 1,000 unique records and Trailhead's is 100 matched individuals, so treat the number as a template setting.[^s1][^s2]
- Each scheduled query is tied to a consumer segment's publish schedule, with one scheduled run per consumer segment, or per segment and parameter combination for custom templates.[^s5]
- Queries and data accesses are recorded in the Clean Room Audit Log DMO, and both collaborators must be Data 360 customers.[^s1][^s2]
- Setup needs an Enterprise Edition home org and Data Cloud Architect, Activation Manager or Activation Specialist permission sets.[^s4][^s5]

## When to use it (and when not)

Use a clean room when two organisations need joint answers, such as audience overlap, campaign attribution or lookalike reach, but neither may disclose its customer list. Salesforce's examples include a consumer brand matching ad views to a grocer's sales, a bank consortium detecting fraud, and an airline and hotel matching guest segments.[^s6] When one side should simply read the other's data, a plain zero copy data share is simpler; when you want to push your own segment to an ad platform you control, ordinary activation fits better.

## Connections

The feature is part of Data 360 (`broader`) and reuses its zero copy plumbing: zero copy data sharing and federation are the non-private ways to expose or read data, while a clean room adds template-enforced query and threshold controls on top.[^s1][^s6] It depends on data streams and data model objects for the hashed match keys, on segmentation for the shared audiences, and optionally on identity resolution for unified individuals.[^s4] Its activation template overlaps with Data 360 activation, and it integrates with AWS Clean Rooms for cross-cloud collaboration.[^s1][^s3] It implements the general data clean room pattern used across the advertising industry.[^s2]

## Sources
[^s1]: Salesforce Help, "Learn about Data 360 Clean Rooms" (2026). https://help.salesforce.com/s/articleView?id=005225176&language=en_US&type=1 (accessed 2026-11-22)
[^s2]: Trailhead, "Understanding Clean Rooms: Security, Roles, and Use Cases". https://trailhead.salesforce.com/content/learn/modules/data-360-clean-rooms-quick-look/get-started-with-data-360-clean-rooms (accessed 2026-11-22)
[^s3]: Salesforce Help, "Data 360 Clean Room Collaboration Process Overview". https://help.salesforce.com/s/articleView?language=en_US&id=data.c360_a_crc_how_clean_room_works.htm&type=5 (accessed 2026-11-22)
[^s4]: Salesforce Help, "Prepare Your Data for a Clean Room". https://help.salesforce.com/s/articleView?id=data.c360_a_crc_prepare_data.htm&language=en_US&type=5 (accessed 2026-11-22)
[^s5]: Salesforce Help, "Collaborate in a Clean Room". https://help.salesforce.com/s/articleView?id=data.c360_a_crc_collaborate_in_clean_room.htm&language=en_US&type=5 (accessed 2026-11-22)
[^s6]: Salesforce, "The New Era of Data Collaboration: Introducing Salesforce Data 360 Clean Rooms" (2026-02-09). https://www.salesforce.com/blog/introducing-data360-clean-rooms/ (accessed 2026-11-22)
