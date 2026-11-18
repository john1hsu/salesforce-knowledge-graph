---
id: kt:state-and-country-territory-picklists
type: Feature
title: State and Country/Territory Picklists
aliases: [state and country picklists, state and country/territory picklist, country picklists, AddressSettings, StateCode and CountryCode, address picklists]
domain: data-model
summary: >-
  An org-wide setting that replaces the free-text state and country fields of standard addresses with standardized
  picklists backed by ISO codes and customizable integration values, configured in Setup or through the AddressSettings
  metadata type.
release: "Winter '27"
status: current
broader: [kt:custom-fields, kt:data-quality]
related: [kt:picklist-value-sets, kt:standard-objects, kt:validation-rules, kt:person-accounts, kt:change-sets, kt:field-history-tracking]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: enables, object: kt:custom-address-fields}
sources:
  - id: s1
    title: "Let Users Select States, Countries, and Territories from Picklists"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.admin_state_country_picklists_overview.htm&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s2
    title: "Enable and Disable State and Country/Territory Picklists"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.admin_state_country_picklist_enable.htm&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s3
    title: "Integration Values for State and Country/Territory Picklists"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.admin_state_country_picklists_integ_values.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s4
    title: "State and Country/Territory Picklist Field-Syncing Logic"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=admin_state_country_picklists_field_syncing.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-18
  - id: s5
    title: "Metadata API Developer Guide: AddressSettings"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_addresssettings.htm
    type: official-docs
    accessed: 2026-11-18
  - id: s6
    title: "Custom Address Fields Developer Guide: Configure State and Country/Territory Picklists"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.caf_dev_guide.meta/caf_dev_guide/caf_dev_configure_picklists.htm
    type: official-docs
    accessed: 2026-11-18
created: 2026-11-18
---

# State and Country/Territory Picklists

State and Country/Territory Picklists let users choose states, provinces, countries and territories from standardized lists instead of typing them, which removes the "USA / U.S. / United States" sprawl that breaks reports and integrations, including for records written through the API.[^s1] The feature covers the billing, shipping, mailing and "other" addresses on accounts, campaign members, contacts, contracts, leads, orders, person accounts, quotes and service contracts, plus user and company addresses in Setup. It is available in Classic and Lightning Experience in every edition except Database.com.[^s1]

## How it works

Out of the box the list holds 235 countries and territories, and nine countries ship with states or provinces: the United States, Canada, Australia, Brazil, China, India, Ireland, Italy and Mexico.[^s1] Each value carries three identities:[^s1][^s3]

- **Name (label)**: what users see; it is looked up from the code and never stored on the record.[^s3]
- **ISO code**: exposed in the `StateCode` and `CountryCode` fields, for example through Data Loader.[^s1]
- **Integration value**: editable text that defaults to the full ISO name and acts like an API name for the value.[^s3]

The integration value is what lands in the record's text-only State/Province and Country fields, and it is what Apex, SOQL, API integrations, validation and assignment rules, email templates and report filters see.[^s3] When a record is saved, Salesforce keeps code and integration value in step: setting a valid code rewrites the integration value, and setting a valid integration value rewrites the code.[^s4] A state that does not belong to the chosen country is rejected, and clearing the country code also clears the state.[^s4]

Rollout is a four-step project: configure the values (including integration values that match what existing integrations send), scan data and customizations such as list views, reports and workflow rules, convert existing text to standard values, then enable the picklists and optionally rescan.[^s1] Configuration can be done in Setup or as code with the **AddressSettings** metadata type (API 27.0+), a single `Address.settings` file whose `Country` and `State` entries carry `active`, `visible`, `integrationValue`, `isoCode`, `label` and `standard` flags, with `orgDefault` on countries.[^s5] A value can be active (usable in the API) but not visible (hidden from users); visible values must also be active.[^s5]

## Limits and gotchas

- **Unsupported channels**: change sets, Salesforce to Salesforce and Connect Offline don't support the picklists.[^s1]
- **Size**: lists above 1,000 states or countries/territories can degrade performance.[^s1]
- **No deletes via API**: Metadata API can create and edit values but can't delete them, and after enablement `active` can't be set back to false.[^s5]
- **Integration value edits aren't retroactive**: records already saved keep the old value, and every hard-coded reference must change.[^s3]
- **Conflicting writes**: new records silently take the code's value, but an update with mismatched code and integration value fails.[^s4]
- **Lag after enabling**: ISO code fields on existing records fill in over time, so users may be prompted to pick a code when editing.[^s2]
- **History tracking moves**: after enablement, field history follows the picklist fields rather than the text fields.[^s2]
- **Reports show labels, not codes**, and filters must use names in the picklist filters but integration values in the text-only ones.[^s1][^s3]
- **Disabling is lossy**: records saved since enablement keep integration values instead of their original text.[^s2]

Disabling also invalidates workflow field updates, email templates and Visualforce pages that reference the picklists, and drops report and list view columns and filters built on them.[^s2] Enabling or disabling requires the Modify All Data permission.[^s2]

## When to use it (and when not)

Turn it on for any org that reports, routes or territories by geography, or that feeds addresses to downstream systems, because codes give integrations a stable key while labels stay translatable and searchable.[^s1][^s3] Set integration values before enabling so legacy integrations that send full names keep working.[^s3][^s5] Plan it as a data project in its own right, because disabling later is not a clean undo.[^s2] For other governed lists that are not addresses, a global **picklist value set** is the general-purpose tool.[^s1]

## Connections

The feature is a specialised, platform-managed relative of **picklist value sets** and a direct lever on **data quality**, applied to the address fields of **standard objects** including **person accounts**.[^s1] It is **configured via** the **Metadata API** (AddressSettings), while **change sets** cannot carry it, so promotion between orgs runs through metadata deployments.[^s1][^s5] **Validation rules** and data loads must reference codes or integration values rather than labels, and **field history tracking** shifts to the picklist fields once enabled.[^s2][^s3] The same values feed **custom address fields**: if the picklists are already enabled, custom address fields reuse them, and configuring them is the documented first step before enabling custom address fields.[^s6]

## Sources
[^s1]: Salesforce Help, "Let Users Select States, Countries, and Territories from Picklists". https://help.salesforce.com/s/articleView?language=en_US&id=sf.admin_state_country_picklists_overview.htm&type=5 (accessed 2026-11-18)
[^s2]: Salesforce Help, "Enable and Disable State and Country/Territory Picklists". https://help.salesforce.com/s/articleView?language=en_US&id=sf.admin_state_country_picklist_enable.htm&type=5 (accessed 2026-11-18)
[^s3]: Salesforce Help, "Integration Values for State and Country/Territory Picklists". https://help.salesforce.com/s/articleView?id=xcloud.admin_state_country_picklists_integ_values.htm&language=en_US&type=5 (accessed 2026-11-18)
[^s4]: Salesforce Help, "State and Country/Territory Picklist Field-Syncing Logic". https://help.salesforce.com/s/articleView?id=admin_state_country_picklists_field_syncing.htm&language=en_US&type=5 (accessed 2026-11-18)
[^s5]: Salesforce Developers, "Metadata API Developer Guide: AddressSettings". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_addresssettings.htm (accessed 2026-11-18)
[^s6]: Salesforce Developers, "Custom Address Fields Developer Guide: Configure State and Country/Territory Picklists". https://developer.salesforce.com/docs/atlas.en-us.caf_dev_guide.meta/caf_dev_guide/caf_dev_configure_picklists.htm (accessed 2026-11-18)
