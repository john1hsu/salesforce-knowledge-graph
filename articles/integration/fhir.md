---
id: kt:fhir
type: ExternalConcept
title: FHIR (Fast Healthcare Interoperability Resources)
aliases: [FHIR, HL7 FHIR, Fast Healthcare Interoperability Resources, FHIR R4, FHIR R5]
domain: integration
summary: >-
  HL7's standard for exchanging healthcare data as modular "resources" (Patient, Encounter, Observation and others)
  over a RESTful HTTP API in JSON, XML or RDF; Salesforce Health Cloud's Clinical data model is aligned with FHIR R4,
  with documented deviations that integration middleware must bridge.
release: "Winter '27"
status: concept
broader: [kt:integration-patterns]
related: [kt:rest-api, kt:hipaa, kt:person-accounts, kt:hl7-v2]
relations:
  - {predicate: consumedBy, object: kt:health-cloud}
sources:
  - id: s1
    title: "FHIR Overview - Architects (FHIR R4, v4.0.1)"
    publisher: HL7 International
    url: https://www.hl7.org/fhir/r4/overview-arch.html
    type: standards-body
    accessed: 2026-11-28
  - id: s2
    title: "RESTful API (FHIR R4, v4.0.1)"
    publisher: HL7 International
    url: https://www.hl7.org/fhir/R4/http.html
    type: standards-body
    accessed: 2026-11-28
  - id: s3
    title: "FHIR Overview - Architects (FHIR R5, v5.0.0)"
    publisher: HL7 International
    url: https://hl7.org/fhir/overview-arch.html
    type: standards-body
    accessed: 2026-11-28
  - id: s4
    title: "Mapping FHIR v4.0 to Salesforce Standard Objects (Health Cloud Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.health_cloud_object_reference.meta/health_cloud_object_reference/map_fhir_overview.htm
    type: official-docs
    accessed: 2026-11-28
  - id: s5
    title: "Considerations for Integration (Health Cloud Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/industries/health-cloud-dev-guide/guide/map-fhir-considerations.html
    type: official-docs
    accessed: 2026-11-28
  - id: s6
    title: "On the Road to Cures Update: Certified API Technology"
    publisher: Office of the National Coordinator for Health IT (ONC)
    url: https://healthit.gov/blog/health-information-exchange-2/on-the-road-to-cures-update-certified-api-technology/
    type: government
    accessed: 2026-11-28
created: 2026-11-28
---

# FHIR (Fast Healthcare Interoperability Resources)

FHIR is HL7 International's specification for exchanging healthcare information between systems. It has two main parts: **resources**, information models for healthcare "business objects" such as a patient, procedure, observation or order, and **APIs**, the interfaces systems use to exchange them. The APIs are designed for RESTful implementation, although REST is not strictly required.[^s1] FHIR R4 (v4.0.1) mixes normative and trial-use content. R5 (v5.0.0, Standard for Trial Use) is the current published version.[^s1][^s3] In Salesforce work, FHIR matters mainly as the external model that Health Cloud's clinical objects follow.[^s4]

## How it works

The R4 architecture overview arranges the specification in layers: foundation, base, clinical, financial and specialized resources, with a contextualization layer of profiles and graphs on top. The design deliberately prefers fewer, mutually exclusive resources. Resources reference each other to build larger records, and **profiles** extend, constrain or contextualize them for a particular use.[^s1] The overview also stresses stateless REST for scalability and strongly typed, terminology-bound data for fidelity.[^s1]

The RESTful API addresses resources as `[base]/[type]/[id]` and defines interactions at three levels. At the instance level these are read, vread (one version), update, patch, delete and history. At the type level they are create, search and history. At the whole-system level they are capabilities, batch/transaction, history and search.[^s2] The JSON, XML and RDF Turtle formats use the MIME types `application/fhir+json`, `application/fhir+xml` and `application/fhir+turtle`.[^s2] Each resource's version id is exposed as a weak ETag, so clients can do optimistic locking with `If-Match`. A version mismatch returns HTTP 412.[^s2] Servers must publish a CapabilityStatement that declares which resources and interactions they support. The core specification targets REST maturity level 2, and level 3 is possible through extensions.[^s2]

## FHIR in Salesforce

Salesforce Health Cloud's **Clinical data model** is built to align with FHIR R4. Salesforce notes that, because of how its platform works, its implementation does not exactly match HL7's definition. The developer guide therefore publishes a mapping page for each supported resource, including Patient, Practitioner, Encounter, Condition, Observation, MedicationRequest, CarePlan, Goal and Immunization.[^s4] The integration considerations require Enterprise or Unlimited Edition and a middleware layer to convert HL7 and FHIR messages into Salesforce objects and fields.[^s5]

## Gotchas

The integration considerations list where Salesforce flattens FHIR structures. Mappings should be designed around these differences:[^s5]

- A FHIR CodeableConcept can carry many codings, but Salesforce lacks zero-to-many references, so it becomes up to 15 code-set lookups.[^s5]
- Periods, quantities, ranges and ratios are split into separate start/end, value/unit, lower/upper and numerator/denominator fields.[^s5]
- Simple code value sets become picklists, while other code and URI types are stored as strings.[^s5]
- HumanName maps to the PersonName object, which is linked to the Account or Contact of a Person Account.[^s5]

## Why it matters in the US

ONC's 21st Century Cures Act rule required certified health IT developers to deliver FHIR-based standardized APIs, under criterion §170.315(g)(10), to their customers by December 31, 2022. Its standards update process added the HL7 FHIR US Core implementation guides 4.0.0 and 5.0.1.[^s6] Medicare and MIPS Promoting Interoperability participants had to use the updated certified technology for performance periods starting in 2023.[^s6] As a result, a Health Cloud implementation usually exchanges data with EHRs that expose FHIR APIs.[^s6]

## When to use it (and when not)

Use FHIR resources and the RESTful API as the integration contract when exchanging clinical data with EHRs, payers or patient apps. Map them to Health Cloud objects in middleware rather than inventing a custom schema.[^s4][^s5] For older feeds, Salesforce also documents storing HL7 v2.3 messages in standard objects, a separate path from FHIR.[^s4] Do not assume a one-to-one mapping: check each resource's mapping page and the flattening rules first.[^s4][^s5]

## Connections

FHIR sits under **integration patterns** as an external, standards-based contract exchanged over REST.[^s2] It is **consumed by** **Health Cloud**, whose Clinical data model maps FHIR R4 resources onto standard objects.[^s4] It relates to the Salesforce **REST API**, which is a different API: middleware typically reads FHIR from an EHR and writes the mapped records into Salesforce.[^s5] It relates to **Person Accounts**, the anchor for mapped patient names, and to **HL7 v2**, the older messaging standard Health Cloud also supports.[^s4][^s5] It relates to **HIPAA** because the data exchanged is protected health information, and US API requirements under the Cures Act rule shape which FHIR guides counterpart systems implement.[^s6]

## Sources

[^s1]: HL7 International, "FHIR Overview - Architects" (FHIR R4, v4.0.1). https://www.hl7.org/fhir/r4/overview-arch.html (accessed 2026-11-28)
[^s2]: HL7 International, "RESTful API" (FHIR R4, v4.0.1). https://www.hl7.org/fhir/R4/http.html (accessed 2026-11-28)
[^s3]: HL7 International, "FHIR Overview - Architects" (FHIR R5, v5.0.0). https://hl7.org/fhir/overview-arch.html (accessed 2026-11-28)
[^s4]: Salesforce Developers, "Mapping FHIR v4.0 to Salesforce Standard Objects", Health Cloud Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.health_cloud_object_reference.meta/health_cloud_object_reference/map_fhir_overview.htm (accessed 2026-11-28)
[^s5]: Salesforce Developers, "Considerations for Integration", Health Cloud Developer Guide. https://developer.salesforce.com/docs/industries/health-cloud-dev-guide/guide/map-fhir-considerations.html (accessed 2026-11-28)
[^s6]: ONC, "On the Road to Cures Update: Certified API Technology" (2022). https://healthit.gov/blog/health-information-exchange-2/on-the-road-to-cures-update-certified-api-technology/ (accessed 2026-11-28)
