---
id: kt:custom-address-fields
type: Feature
title: Custom Address Fields
aliases: [custom address field, Address field type, Address data type, CustomAddressFieldSettings, enableCustomAddressField]
domain: data-model
summary: >-
  An org-level, irreversible setting that adds an Address data type for custom fields, so standard and custom objects can
  store structured compound addresses (street, city, state code, country code, postal code and geocode) that mirror
  standard address fields, at a cost of nine custom field allocations each.
release: "Winter '27"
status: current
broader: [kt:custom-fields]
related: [kt:geolocation-fields, kt:standard-objects, kt:field-sets, kt:sosl, kt:data-loader]
relations:
  - {predicate: dependsOn, object: kt:state-and-country-territory-picklists}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: consumedBy, object: kt:apex}
  - {predicate: integratesWith, object: kt:bulk-api-2}
sources:
  - id: s1
    title: "Custom Address Fields — Custom Address Fields Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.caf_dev_guide.meta/caf_dev_guide/caf_dev_guide.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s2
    title: "Custom Address Fields Requirements and Limitations"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.caf_dev_guide.meta/caf_dev_guide/caf_dev_limitations.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s3
    title: "Enable Custom Address Fields"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.caf_dev_guide.meta/caf_dev_guide/caf_dev_manage.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s4
    title: "Apex Examples — Custom Address Fields Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.caf_dev_guide.meta/caf_dev_guide/caf_dev_examples_apex.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s5
    title: "Address Compound Fields — Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/compound_fields_address.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s6
    title: "Add a Geocode to a Custom Address Field"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.caf_dev_guide.meta/caf_dev_guide/caf_dev_add_geocode.htm
    type: official-docs
    accessed: 2026-11-19
created: 2026-11-19
---

# Custom Address Fields

Custom Address Fields is a feature that adds an **Address** data type to custom fields. Each field stores a postal address as one structured compound value, which can also be read and written through its individual components.[^s1] The fields work on standard and custom objects. Users can enter and edit addresses on records and see them in list views and reports, and the feature is available in all editions.[^s1] The aim is to give admins and developers address fields that behave like the standard ones, such as Account billing or Contact mailing addresses, instead of five or six loose text fields, though with a list of gaps covered below.[^s1][^s5]

## How it works

An admin with the Customize Application permission turns the feature on under Setup → User Interface by selecting **Use custom address fields**. The same switch exists in the Metadata API as `enableCustomAddressField` on the `CustomAddressFieldSettings` type.[^s3] The address picklists must be configured first, because the State and Country components of a custom address are picklists rather than free text.[^s2][^s3] Once the feature is on, Address appears as a data type when you add a field in Object Manager.[^s3][^s5] **The setting can't be disabled**, so turning it on is a one-way, org-wide decision.[^s3]

Each field is a compound of street, city, postal code, country code, state code, latitude, longitude and geocode accuracy, plus one hidden component for internal use.[^s1][^s2] In Apex and the APIs the components follow the pattern `Field__Component__s`. A field `Mailing_Address__c` exposes `Mailing_Address__Street__s`, `__City__s`, `__StateCode__s`, `__CountryCode__s`, `__PostalCode__s`, `__Latitude__s`, `__Longitude__s` and `__GeocodeAccuracy__s`.[^s4] You write an address by setting those components and calling `insert` or `update`, and you clear one by setting every component to null and updating the record.[^s4] The compound value surfaces as the API's `Address` type, which extends `Location`. On standard addresses `CountryCode` exists only when the picklists are enabled, but on a custom address field it is always available.[^s5]

Custom address fields aren't geocoded for you. Salesforce's documented approach is Apex that calls an external map service and writes the latitude and longitude components, optionally run from a trigger. Every call then hits the provider and can incur charges.[^s6] Data integration rules can't map a custom address's State and Country components.[^s2]

## Limits and gotchas

- **Field allocation:** each custom address field consumes nine custom field allocations on its object.[^s1][^s2]
- **Package installs:** a package containing a custom address field installs only in an org that has the feature enabled already.[^s2]
- **Not supported:** approvals, workflow, merge fields, field sets, Lightning Web Components, Visualforce, Composite API, field encryption, lead conversion and the Data Import Wizard.[^s2]
- **Also not supported:** the address Flow screen input component, fuzzy matching, and converting another field type into an address field.[^s2]
- **Search:** global, lookup and SOSL search are listed as unsupported, and only the Street component is searchable.[^s2]
- **Distance:** the `DISTANCE` function doesn't work with custom address fields, unlike standard addresses and geolocation fields.[^s2][^s5]
- **Import and export:** load data with the REST API or Bulk API 2.0 and export with the API or SOQL. Bulk API can't export custom compound fields and reports a misleading "not enabled" error.[^s2]
- **Not validated:** Data Loader, Bulk API 1.0, Schema Builder, Web-to-Case, Email-to-Case and web-to-lead aren't validated with these fields.[^s2]
- **Reports and layout:** reports need the individual components, not the compound field. A field can't be marked required, and component labels can't be renamed.[^s2]
- **Classic search filters:** using a custom address in a Classic search filter layout makes package installs and Metadata `deploy()` fail.[^s2]

## When to use it (and when not)

Use a custom address field when an object needs a second, structured address with ISO-coded states and countries. Examples include a shipping site on Opportunity or a location on a custom Warehouse object, where code and integrations benefit from a single compound value.[^s1][^s4] Prefer the standard address where one exists, because standard addresses support `DISTANCE` and automatic geocoding on supported objects.[^s5] If the record needs only a coordinate, a geolocation field is cheaper in allocations. If the address must drive approvals, LWC forms, field sets or full-text search, the unsupported list may push you back to separate text and picklist fields.[^s2]

## Connections

Custom address fields are a kind of **custom field** and depend on **state and country/territory picklists** for their code components.[^s2][^s3] They are switched on through Setup or `CustomAddressFieldSettings` in the **Metadata API**, written in **Apex** through `__s` components, and exported with **SOQL**.[^s2][^s3][^s4] They pair with **geolocation fields** through their latitude and longitude components, and they mirror the compound addresses on **standard objects**.[^s5][^s6] Their gaps define their relationship with **field sets**, **SOSL**, **Data Loader** and **Bulk API 2.0**, which is the supported bulk load path.[^s2]

## Sources
[^s1]: Salesforce Developers, "Custom Address Fields — Custom Address Fields Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.caf_dev_guide.meta/caf_dev_guide/caf_dev_guide.htm (accessed 2026-11-19)
[^s2]: Salesforce Developers, "Custom Address Fields Requirements and Limitations". https://developer.salesforce.com/docs/atlas.en-us.caf_dev_guide.meta/caf_dev_guide/caf_dev_limitations.htm (accessed 2026-11-19)
[^s3]: Salesforce Developers, "Enable Custom Address Fields". https://developer.salesforce.com/docs/atlas.en-us.caf_dev_guide.meta/caf_dev_guide/caf_dev_manage.htm (accessed 2026-11-19)
[^s4]: Salesforce Developers, "Apex Examples — Custom Address Fields Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.264.0.caf_dev_guide.meta/caf_dev_guide/caf_dev_examples_apex.htm (accessed 2026-11-19)
[^s5]: Salesforce Developers, "Address Compound Fields — Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/compound_fields_address.htm (accessed 2026-11-19)
[^s6]: Salesforce Developers, "Add a Geocode to a Custom Address Field". https://developer.salesforce.com/docs/atlas.en-us.caf_dev_guide.meta/caf_dev_guide/caf_dev_add_geocode.htm (accessed 2026-11-19)
