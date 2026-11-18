---
id: kt:geolocation-fields
type: Feature
title: Geolocation Fields
aliases: [geolocation field, Location field type, geolocation compound field, latitude and longitude fields]
domain: data-model
summary: >-
  A custom field type (API type Location) that stores a latitude/longitude pair as a read-only compound field with
  editable __latitude__s and __longitude__s subfields, used for distance formulas and location-based SOQL queries.
release: "Winter '27"
status: current
broader: [kt:custom-fields]
related: [kt:formula-fields, kt:custom-address-fields, kt:lookup-filters, kt:validation-rules, kt:field-service, kt:salesforce-maps]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: consumedBy, object: kt:lightning-web-components}
sources:
  - id: s1
    title: "Geolocation Compound Field — Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/compound_fields_geolocation.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s2
    title: "Location-Based SOQL Queries — SOQL and SOSL Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_geolocate.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s3
    title: "Compound Field Considerations and Limitations — Object Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/compound_fields_limitations.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s4
    title: "CustomField — Metadata API Developer Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/customfield.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s5
    title: "lightning-input-location — Lightning Component Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-input-location.html
    type: official-docs
    accessed: 2026-11-18
  - id: s6
    title: "Configure for Location Accuracy — Configure Your Salesforce Maps Environment"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/configuring-your-salesforce-maps-environment/configure-for-location-accuracy
    type: official-learning
    accessed: 2026-11-18
created: 2026-11-18
---

# Geolocation Fields

A geolocation field stores a point on Earth as a latitude and a longitude. Since API version 26.0 it is a compound field of type Location made of two subfields, and admins can add it as a custom field to standard or custom objects.[^s1] Many standard objects, such as Account, Contact, Quote and User, also carry a geolocation component inside their standard address fields.[^s1] Values are decimal degrees: latitude must fall between -90 and 90 and longitude between -180 and 180, which is the range the `lightning-input-location` component enforces on entry.[^s5]

## How it works

For a field named `Location__c`, the platform exposes the subfields `Location__latitude__s` and `Location__longitude__s`.[^s1] The compound field itself is read-only; you write data by setting the two subfields, which are editable.[^s1] In SOQL you can select the subfields individually anywhere, while selecting the whole compound field returns structured latitude and longitude data only through SOAP and REST API queries.[^s2] SOAP calls on API versions earlier than 30.0 return the compound value as a string, so older integrations must parse it before doing math.[^s1]

In the Metadata API, a custom location field's `displayLocationInDecimal` attribute controls display. When true, the UI shows decimal notation; when false, it shows degrees, minutes and seconds.[^s4]

Location-based SOQL uses two functions. `DISTANCE(location1, location2, 'unit')` returns the distance in `'mi'` or `'km'`, and `GEOLOCATION(lat, lon)` builds a point from literal coordinates and must be used inside `DISTANCE`.[^s2] Both work in `WHERE` and `ORDER BY`, and `DISTANCE` also works in `SELECT`, which supports "nearest N within a radius" queries.[^s2] The same `DISTANCE` logic is available in validation rules, field updates, approval and workflow entry criteria, and in lookup filters set through the Metadata API.[^s3]

## Populating coordinates

A geolocation field is only useful once it is filled in. For Account, Contact, Lead and WorkOrder addresses, an admin can activate the geo data integration rules in supported editions so the standard geocode fields update automatically. On other objects and editions, coordinates must be set through the API, the CLI or an outside geocoding service.[^s3] In Salesforce Maps, data integration rules keep standard geocode fields current when an address changes. Without them, the old coordinates stay until they are cleared and the record is geocoded again.[^s6]

## Limits and gotchas

- **Field allocation:** one custom geolocation field counts as three custom fields: latitude, longitude, and one for internal use.[^s1]
- **Operators:** `DISTANCE` supports only `<` and `>`, not equality. `GROUP BY` isn't supported, and Apex bind variables can't supply the unit.[^s2]
- **Argument order:** when you mix a field with `GEOLOCATION()`, the field must come first, or the query fails as malformed.[^s2]
- **Nulls:** a value counts as null only when both coordinates are null. A record with only one coordinate set is treated as unset when you filter or sort by distance.[^s2]
- **Precision:** `DISTANCE` uses a haversine approximation that assumes a spherical Earth. Error can approach 0.55% near the equator, so compare distances against a tolerance.[^s2]
- **Formula blanks:** in distance formulas, choose "Treat blank fields as blanks." Treating blanks as zeros measures from 0°, 0°.[^s2]
- **Unsupported surfaces:** custom settings, dashboards, Schema Builder, Salesforce to Salesforce and filter-based workflow updates all exclude geolocation fields.[^s3]
- **Compound access:** compound fields can't be used in Visualforce, and Data Loader exports of them fail. Export the latitude and longitude components instead.[^s3]
- **Formula functions:** only `ISBLANK`, `ISCHANGED` and `ISNULL` accept a compound field directly. Other functions and comparison operators need the subfields.[^s3]
- **External objects:** Location is one of the custom field types that external objects don't support.[^s4]

## When to use it (and when not)

Use a custom geolocation field when a record needs a point that isn't a standard address. Examples include a job site, an asset or a store pin you query by radius. If the location is a postal address on a supported standard object, use the address's built-in geocode with data integration rules instead of a parallel custom field.[^s1][^s3] For route planning, territory visualization or batch geocoding at scale, Salesforce Maps writes coordinates to latitude and longitude fields. Those can be standard geocode fields or custom fields you define.[^s6] Because `DISTANCE` is approximate, do your own calculation when precision matters.[^s2]

## Connections

Geolocation fields are a kind of **custom field** and spend three slots of the object's field allocation.[^s1] They are queried with **SOQL** through `DISTANCE` and `GEOLOCATION`, can drive **formula fields**, **validation rules** and distance-range **lookup filters**, and are defined in source as `CustomField` metadata through the **Metadata API**.[^s2][^s3][^s4] **Lightning Web Components** collect them with `lightning-input-location`.[^s5] They sit beside **custom address fields**, which carry their own latitude and longitude subfields, and they feed location-centric products such as **Salesforce Maps** and **Field Service**.[^s3][^s6]

## Sources
[^s1]: Salesforce Developers, "Geolocation Compound Field — Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/compound_fields_geolocation.htm (accessed 2026-11-18)
[^s2]: Salesforce Developers, "Location-Based SOQL Queries — SOQL and SOSL Reference". https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_geolocate.htm (accessed 2026-11-18)
[^s3]: Salesforce Developers, "Compound Field Considerations and Limitations — Object Reference". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/compound_fields_limitations.htm (accessed 2026-11-18)
[^s4]: Salesforce Developers, "CustomField — Metadata API Developer Guide". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/customfield.htm (accessed 2026-11-18)
[^s5]: Salesforce Developers, "lightning-input-location — Lightning Component Reference". https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-input-location.html (accessed 2026-11-18)
[^s6]: Trailhead, "Configure for Location Accuracy — Configure Your Salesforce Maps Environment". https://trailhead.salesforce.com/content/learn/modules/configuring-your-salesforce-maps-environment/configure-for-location-accuracy (accessed 2026-11-18)
