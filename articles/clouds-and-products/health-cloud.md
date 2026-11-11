---
id: kt:health-cloud
type: Product
title: Health Cloud
aliases: [Salesforce Health Cloud]
domain: clouds-and-products
summary: >-
  Salesforce's industry cloud for healthcare providers, payers and related organizations, which adds a FHIR R4-aligned
  clinical data model, care management, utilization management and provider network features on top of the
  Salesforce Platform to give a 360-degree view of patients and members.
release: "Winter '27"
status: current
broader: [kt:salesforce-industries]
related: [kt:hipaa, kt:service-cloud, kt:experience-cloud]
relations:
  - {predicate: implements, object: kt:fhir}
  - {predicate: dependsOn, object: kt:person-accounts}
  - {predicate: hasPart, object: kt:utilization-management}
  - {predicate: integratesWith, object: kt:data-cloud}
sources:
  - id: s1
    title: "Health Cloud — Product Overview and FAQ"
    publisher: Salesforce
    url: https://salesforce.com/products/health-cloud/overview/
    type: news
    accessed: 2026-11-11
  - id: s2
    title: "Meet Health Cloud for Providers (Health Cloud for Providers)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/health-cloud-for-providers/meet-health-cloud-for-providers
    type: official-learning
    accessed: 2026-11-11
  - id: s3
    title: "Examine the Clinical Data Model (Health Cloud Data Models)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/fr/content/learn/modules/health-cloud-data-models/examine-the-clinical-data-model
    type: official-learning
    accessed: 2026-11-11
  - id: s4
    title: "Clinical Data Model Mapping to FHIR R4 (Salesforce Health Cloud Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.260.0.health_cloud_object_reference.meta/health_cloud_object_reference/map_fhir_overview.htm
    type: official-docs
    accessed: 2026-11-11
  - id: s5
    title: "Assign Health Cloud Permission Sets and Permission Set Licenses (Health Cloud Administration)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.health_cloud.meta/healthcare_admin.htm/admin_permissionset_licenses_assign.htm
    type: official-docs
    accessed: 2026-11-11
created: 2026-11-11
---

# Health Cloud

Health Cloud is Salesforce's industry cloud for healthcare and life sciences organizations. It runs on the Salesforce Platform and brings clinical and nonclinical data together so that care teams, contact centers and administrators work from one record of each patient or member, a 360-degree view that Salesforce positions as a single source of truth.[^s2] Rather than replacing an electronic health record (EHR), Salesforce describes Health Cloud as an engagement and collaboration layer that sits on top of the EHR and connects clinical with operational data.[^s1] It serves both providers (hospitals, clinics, home health) and payers (health plans), and it is part of the Salesforce Industries family of vertical clouds.[^s1][^s2]

## What it does

Trailhead groups the provider-facing capabilities into a few areas:[^s2]

- **Patient and member services.** A console shows each patient with caregivers, clinic, languages, conditions and prescriptions; patients can self-schedule through a portal.[^s2]
- **Care orchestration.** Care management and coordination aimed at intervening at the right moment and reducing hospital readmissions.[^s2]
- **Provider network and relationship management.** Recruiting and onboarding providers, with records for licenses, education, work history and liability coverage.[^s2]
- **Utilization management.** Prior authorization and service request reviews against evidence-based guidelines, plus handling of care denials.[^s2]

The current product page adds integrated care management with care plans and assessments, intelligent appointment management, home health, group insurance, intelligent document automation, and a "Data 360 for Health" unified profile. It also lists FHIR APIs and prebuilt integrations for bidirectional interoperability.[^s1] Assistive AI is sold separately as Agentforce for Healthcare, described as purpose-built for Health Cloud.[^s1] Salesforce lists four editions: Sales & Service Core, Sales & Service Advanced, Service Max and Sales Max. Higher tiers add more AI, automation, security and backup tooling, and list prices are published per user per month.[^s1]

## Data model

Health Cloud's Clinical data model is aligned with HL7 FHIR and supports many HL7 message types; EHR data typically arrives through integration middleware.[^s3] Patients are modeled as **Person Accounts**, and objects such as Clinical Encounter, Health Condition, Medication Statement, Medication Request and Diagnostic Summary hang off that record. Encounter junction objects link an encounter to facilities, providers, reasons, diagnoses and service requests.[^s3] The developer guide maps FHIR R4 resources, including Patient, Practitioner, Encounter, Condition, Observation, MedicationRequest, CarePlan and Goal, onto fields of Salesforce standard objects. It warns that Salesforce's implementation of FHIR R4 is not identical to the HL7 definition, so integrations should check each resource's mapping page rather than assume a one-to-one match.[^s4]

## Licensing and setup gotchas

Health Cloud is a mix of a managed package and features built directly into core Salesforce, and its licensing reflects that split.[^s5] Two permission set licenses are both required for the product to work:[^s5]

- **Health Cloud** grants the standard and custom objects behind features in the managed package.[^s5]
- **Health Cloud Platform** grants Health Cloud standard objects for features built into core, outside the package.[^s5]
- **Health Cloud for Experience Cloud Site** covers site users; it is not available to Partner Community users.[^s5]

On top of the licenses, admins assign the required **Health Cloud Standard** permission set and a permission set confusingly named **Health Cloud Permission Set License**, which is a permission set, not a license. Optional sets cover member services, utilization management, social determinants, provider network management and CRM Analytics.[^s5] The product requires Enterprise or Unlimited Edition in Lightning Experience. When revoking access, remove the license-dependent permission set before the license; removing only the permission set hides the UI but leaves the custom objects reachable.[^s5]

## When to use it

Choose Health Cloud when an organization needs a healthcare-specific data model, care coordination and payer workflows such as prior authorization, rather than building them from generic Service Cloud objects.[^s1][^s2] Salesforce states that Health Cloud is HIPAA compliant and supports standards including HL7 FHIR and HITRUST. Shield or Government Cloud can be added for stronger data protection; compliance still depends on how the customer configures and contracts for the services it uses.[^s1]

## Connections

Health Cloud has the **broader** node `kt:salesforce-industries`, the family of vertical clouds it belongs to.[^s1] It **implements** `kt:fhir`, since its Clinical data model and APIs follow FHIR R4 with documented deviations.[^s4] It **depends on** `kt:person-accounts`, the way patients are represented.[^s3] It **has part** `kt:utilization-management`, its prior authorization and review capability.[^s2] It **integrates with** `kt:data-cloud` through the Data 360 for Health unified profile.[^s1] It is **related** to `kt:hipaa`, the US health-privacy law most deployments must satisfy, to `kt:service-cloud`, whose contact-center patterns it extends, and to `kt:experience-cloud`, which hosts patient and member portals under a dedicated site license.[^s1][^s5]

## Sources
[^s1]: Salesforce, "Health Cloud — Product Overview and FAQ". https://salesforce.com/products/health-cloud/overview/ (accessed 2026-11-11)
[^s2]: Trailhead, "Meet Health Cloud for Providers". https://trailhead.salesforce.com/content/learn/modules/health-cloud-for-providers/meet-health-cloud-for-providers (accessed 2026-11-11)
[^s3]: Trailhead, "Examine the Clinical Data Model". https://trailhead.salesforce.com/fr/content/learn/modules/health-cloud-data-models/examine-the-clinical-data-model (accessed 2026-11-11)
[^s4]: Salesforce, "Clinical Data Model Mapping to FHIR R4", Salesforce Health Cloud Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.260.0.health_cloud_object_reference.meta/health_cloud_object_reference/map_fhir_overview.htm (accessed 2026-11-11)
[^s5]: Salesforce, "Assign Health Cloud Permission Sets and Permission Set Licenses", Health Cloud Administration. https://developer.salesforce.com/docs/atlas.en-us.health_cloud.meta/healthcare_admin.htm/admin_permissionset_licenses_assign.htm (accessed 2026-11-11)
