---
id: kt:multiple-currencies
type: Feature
title: Multiple Currencies
aliases: [multi-currency, multicurrency, multi-currency and advanced currency management, advanced currency management, ACM, dated exchange rates, corporate currency]
domain: data-model
summary: >-
  The org-level setting that lets a Salesforce org store each record's amounts in its own ISO currency, convert them
  through admin-maintained rates against a single corporate currency, and, with Advanced Currency Management, apply
  dated exchange rates to opportunities by close date.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:roll-up-summary-field, kt:standard-objects, kt:visualforce, kt:sales-cloud]
relations:
  - {predicate: consumedBy, object: kt:collaborative-forecasts}
  - {predicate: consumedBy, object: kt:price-books}
  - {predicate: dependsOn, object: kt:currency-type-object}
sources:
  - id: s1
    title: "Company-Wide Org Settings: Configure Multiple Currencies"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/company_wide_org_settings/org_settings_currency
    type: official-learning
    accessed: 2026-11-17
  - id: s2
    title: "Considerations for Enabling Multiple Currencies"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.admin_enable_multicurrency_implications.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-17
  - id: s3
    title: "International Organizations: Using Multiple Currencies"
    publisher: Salesforce
    url: https://login.salesforce.com/help/doc/en/salesforce_using_multiple_currencies.pdf
    type: official-docs
    accessed: 2026-11-17
  - id: s4
    title: "Object Reference: CurrencyType"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_currencytype.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s5
    title: "Prepare Your Salesforce Org for Users: Update the Exchange Rate with ACM"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/prepare-your-salesforce-org-for-users/update-the-exchange-rate
    type: official-learning
    accessed: 2026-11-17
  - id: s6
    title: "Roll-up summary field not calculating with Advanced Currency Management enabled"
    publisher: Salesforce Help (Knowledge Article 000041377)
    url: https://help.salesforce.com/HTViewSolution?id=000041377
    type: official-docs
    accessed: 2026-11-17
created: 2026-11-17
---

# Multiple Currencies

**Multiple currencies** (often written *multi-currency* or *multicurrency*) is the org setting that lets one Salesforce org hold monetary amounts in more than one currency. Orgs start out single-currency; once an admin activates multiple currencies, every record carries its own currency, amounts are converted through rates maintained against one **corporate currency**, and each user sees converted values in a **personal currency**.[^s1][^s3] The optional **Advanced Currency Management (ACM)** layer adds dated exchange rates so that opportunities keep the rate that applied when they closed.[^s1][^s2]

## How it works

Activation is done from Company Information (the *Activate Multiple Currencies* checkbox), after which admins add currencies under Manage Currencies, choosing an ISO code, a conversion rate and the number of decimal places for each.[^s1] The setting is available in Group, Professional, Enterprise, Performance, Unlimited, Developer and other editions, in both Lightning Experience and Classic.[^s2]

Three currencies matter for any amount. The **corporate currency** is the headquarters' reporting currency and the base of every conversion rate; it can be changed to any active currency but never deactivated.[^s1][^s3] The **record currency** is set on each record, and the amount is shown in it first.[^s3] The **personal currency** is each user's default for quotas, forecasts, opportunities, quotes and reports, and a converted value in that currency can appear in parentheses next to the record amount when parenthetical conversion is on.[^s1][^s3] Conversion runs in two hops, from record currency to corporate currency and then to the user's currency, so stale rates can compound the variance.[^s2]

Under the hood each currency is a `CurrencyType` record with an ISO 4217 `IsoCode`, a `ConversionRate` against the corporate currency, `DecimalPlaces`, `IsActive` and `IsCorporate`. The object exists only in multicurrency orgs, needs the Customize Application permission to edit, and its records can't be deleted through the API.[^s4] An update must supply every field, because an omitted `IsActive` defaults to false and can silently deactivate a live currency.[^s4]

## Static rates vs. Advanced Currency Management

Standard conversion rates are static: an edit takes effect immediately and previous rates are not kept, so every amount, including closed opportunities, is reconverted at the new rate and currency gains or losses can't be tracked.[^s1][^s3] ACM, enabled from Manage Currencies, maps rates to date ranges. Opportunity and opportunity product amounts then convert according to the rate in force on the Close Date, and moving a Close Date into another period changes the converted amount.[^s1][^s2][^s5] When ACM is first turned on, the existing rates become the first dated set and stay valid until a later set is added.[^s1] New dated rates are created through Manage Dated Exchange Rates, each with a start date.[^s5]

Dated rates have a narrow reach: they are not used in forecasting, other currency fields or other report types.[^s2]

## Limits and gotchas

- **One-way switch.** Multiple currencies can't be turned off once enabled, and enablement makes permanent changes to the org.[^s1][^s2]
- **Existing data.** Existing records are stamped with the default currency named at enablement; data in mixed currencies should be converted first.[^s2]
- **No deleting currencies.** A currency can be deactivated but never deleted; existing amounts keep it, while new amounts can't use it.[^s2][^s3]
- **Decimal places.** Custom currency fields' own decimal settings are ignored; decimals come from each currency's setup instead.[^s2]
- **Reports.** Field-to-field report filters don't support currency fields such as Amount.[^s2]
- **Roll-ups under ACM.** With ACM on, roll-up summaries of Opportunity currency fields stop calculating; the remedy the article gives is disabling ACM.[^s6]
- **Visualforce.** With ACM enabled, `apex:inputField` and `apex:outputField` can't display currency fields.[^s1]
- **Imports.** Leads need active currency codes, existing accounts and contacts can't have their currency changed by import, and inactive codes convert to the corporate currency.[^s3]
- **Packaging.** Package build orgs are configured with USD only, so tests using another currency code fail.[^s2]

## When to use it (and when not)

Enable multiple currencies when the org genuinely transacts in more than one currency and leaders need consolidated reporting in one corporate currency.[^s3] Because the change is permanent, trial it in a sandbox first and convert mixed-currency data beforehand.[^s2][^s3] Add ACM only when historical opportunity values must hold their closing rate; it costs Opportunity currency roll-ups and Visualforce field display, and it does not reach forecasts or other objects.[^s1][^s2][^s6]

## Connections

Multiple currencies is an org-wide capability of the **Salesforce platform** that touches the currency fields of **standard objects** such as Account, Lead, Case, Opportunity and Opportunity Product.[^s2] **Collaborative forecasts** consume it through the forecast currency, which is either the corporate currency or each owner's personal currency.[^s3] **Price books** in **Sales Cloud** feed Opportunity Product line items, one of the objects whose amounts carry a record currency.[^s2] Its rate store is the `CurrencyType` object.[^s4] Turning on ACM constrains **roll-up summary fields** and **Visualforce** currency display.[^s1][^s6]

## Sources

[^s1]: Trailhead, "Company-Wide Org Settings: Configure Multiple Currencies". https://trailhead.salesforce.com/content/learn/modules/company_wide_org_settings/org_settings_currency (accessed 2026-11-17)
[^s2]: Salesforce Help, "Considerations for Enabling Multiple Currencies". https://help.salesforce.com/s/articleView?id=sf.admin_enable_multicurrency_implications.htm&language=en_US&type=5 (accessed 2026-11-17)
[^s3]: Salesforce, "International Organizations: Using Multiple Currencies" (PDF). https://login.salesforce.com/help/doc/en/salesforce_using_multiple_currencies.pdf (accessed 2026-11-17)
[^s4]: Salesforce Developers, "Object Reference: CurrencyType". https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_currencytype.htm (accessed 2026-11-17)
[^s5]: Trailhead, "Prepare Your Salesforce Org for Users: Update the Exchange Rate with ACM". https://trailhead.salesforce.com/content/learn/projects/prepare-your-salesforce-org-for-users/update-the-exchange-rate (accessed 2026-11-17)
[^s6]: Salesforce Help, Knowledge Article 000041377 on roll-up summaries with Advanced Currency Management. https://help.salesforce.com/HTViewSolution?id=000041377 (accessed 2026-11-17)
