---
id: kt:date-and-date-time-fields
type: Feature
title: Date and Date/Time Fields
aliases: [date field, date/time field, datetime field, Date/Time field type, time field, custom time field, temporal field types]
domain: data-model
summary: >-
  The Salesforce field data types for temporal values: Date (year, month, day), Date/Time (a point in time stored in
  GMT and shown in each user's time zone) and Time (a wall-clock time with millisecond precision and no date), with
  matching behavior in formulas, SOQL and Apex.
release: "Winter '27"
status: current
broader: [kt:custom-fields]
related: [kt:formula-fields, kt:number-currency-and-percent-fields, kt:field-type-conversion, kt:scheduled-paths, kt:fiscal-years]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: consumedBy, object: kt:apex}
  - {predicate: consumedBy, object: kt:formula-fields}
sources:
  - id: s1
    title: "Using Date and Date/Time in Formulas (tip sheet)"
    publisher: Salesforce
    url: https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/formula_date_time_tipsheet.pdf
    type: official-docs
    accessed: 2026-11-26
  - id: s2
    title: "Date Formats and Date Literals in WHERE — SOQL and SOSL Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_dateformats.htm
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "Datetime Class — Apex Reference Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_datetime.htm
    type: official-docs
    accessed: 2026-11-26
  - id: s4
    title: "Take Advantage of the New Custom Time Field in Spring '18"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2018/take-advantage-new-custom-time-field-spring-18
    type: official-blog
    accessed: 2026-11-26
created: 2026-11-26
---

# Date and Date/Time Fields

Salesforce has three field data types for temporal values. A **Date** field holds a calendar day made of year, month and day. A **Date/Time** field holds a date plus a time of day to the second, stored in GMT and displayed in the time zone of whoever is viewing it. A **Time** field holds a time of day independent of any date, with millisecond precision.[^s1] The same three types also appear as formula return types, and each maps onto a native type in SOQL and Apex, so the storage rules below follow the value wherever it travels.[^s1][^s3][^s4]

## How it works

The central rule is that Date/Time values are absolute instants. The platform stores them in GMT and converts them to the viewing user's time zone only for display, so two users in different zones see different clock readings for the same record.[^s1] Date values carry no time zone, which is why converting one Date into another is safe.[^s1] The Time type, introduced in Spring '18 as an open beta field type and formula return type, behaves like a reading on a wall clock: it is not adjusted per user, which suits values such as a hotel's standard check-out time that are always meant in local time.[^s4]

Arithmetic follows the type. Subtracting two Dates yields a whole number of days, subtracting two Date/Times yields decimal days (5.52 is about 5 days, 12 hours and 28 minutes), and subtracting two Times yields milliseconds. Adding a number to a Date or Date/Time moves it by that many days, as in `TODAY() + 3`.[^s1] The admin blog's check-out example divides a Time difference by 3,600,000 to get hours.[^s4]

In SOQL, a date literal is written `YYYY-MM-DD` and a dateTime as `YYYY-MM-DDThh:mm:ss` followed by `Z` or a `+hh:mm`/`-hh:mm` offset from UTC, which is how dateTime values are stored.[^s2] Relative date literals such as `TODAY`, `THIS_QUARTER` and `LAST_N_DAYS:n` resolve against the locale and time zone of the user running the query, falling back to the org's when the user has none, and their ranges start at 12:00:00 AM.[^s2] Fiscal literals like `THIS_FISCAL_YEAR` need custom fiscal years defined in Setup, and a range outside a defined fiscal year returns an invalid-date error.[^s2]

In Apex, `Datetime.now()` is based on a GMT calendar, while methods such as `date()`, `hour()` and `format()` report values in the context user's local time zone; `dateGmt()`, `formatGmt()` and `newInstanceGmt()` are the explicit GMT counterparts.[^s3] `format()` falls back to GMT when it cannot determine a time zone, and the overload that takes a time zone expects a Java TimeZone ID, with full names preferred over three-letter abbreviations.[^s3]

## Limits and gotchas

- **Text and Date conversions happen in GMT.** `DATETIMEVALUE(TODAY())` sets midnight GMT, so a San Francisco user in daylight time sees 5:00 p.m. on the previous day.[^s1]
- **`TEXT()` on a Date/Time returns a GMT string ending in `Z`**, not the user's local reading, and it returns a bare `Z` when the field is blank, so wrap it with `ISBLANK`.[^s1]
- **Formulas cannot see the user's time zone.** The tip sheet says daylight saving time is hard to manage in a formula and points to Apex for Date/Time-to-text and Date conversions.[^s1]
- **`LAST_N_DAYS:n` includes today**, so it spans n+1 days, while `NEXT_N_DAYS:n` starts tomorrow; other `LAST_N_` units exclude the current day.[^s2]
- **Query bounds:** SOQL accepts dateTime values from 1700-01-01T00:00:00Z to 4000-12-31T00:00:00Z GMT, shifted by the user's time zone offset.[^s2]
- **Month-end math:** `ADDMONTHS` returns the last day of the target month when the start is a month end, so February 29 becomes February 28 in a non-leap year.[^s1]
- **Apex parsing is locale-sensitive.** `Datetime.parse()` expects the user's locale format and local zone; `valueOf()` expects `yyyy-MM-dd HH:mm:ss` local, and `valueOfGmt()` the same pattern in GMT.[^s3]

## When to use which

Pick **Date** for calendar facts that must read the same everywhere, such as a birthday, contract end or due date. Pick **Date/Time** for events that happened at a real instant, such as a call start or a submission timestamp, and accept that users see it in their own zone.[^s1] Pick **Time** for recurring local times with no date, such as opening hours or check-in windows.[^s4] When a requirement mixes zones, for example showing a time in a branch's zone rather than the viewer's, use Apex, which can format a Datetime in any named Java time zone.[^s3]

## Connections

These are core data types under **custom fields**, siblings of the numeric types in **number, currency, and percent fields**, and their conversion rules matter in **field type conversion**.[^s1] **Formula fields** consume them through `TODAY()`, `NOW()`, `TIMENOW()`, `DATEVALUE()` and `TIMEVALUE()`, and the Time type is also a formula return type.[^s1][^s4] They are filtered with **SOQL** date formats and literals, including the fiscal literals that depend on **fiscal years**, and handled in **Apex** through the Date, Datetime and Time classes.[^s2][^s3] Date and Date/Time fields are also what time-based automation such as **scheduled paths** is anchored to.

## Sources
[^s1]: Salesforce, "Using Date and Date/Time in Formulas" tip sheet. https://resources.docs.salesforce.com/latest/latest/en-us/sfdc/pdf/formula_date_time_tipsheet.pdf (accessed 2026-11-26)
[^s2]: Salesforce Developers, "Date Formats and Date Literals in WHERE — SOQL and SOSL Reference". https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_dateformats.htm (accessed 2026-11-26)
[^s3]: Salesforce Developers, "Datetime Class — Apex Reference Guide". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_datetime.htm (accessed 2026-11-26)
[^s4]: Salesforce Admins Blog, "Take Advantage of the New Custom Time Field in Spring '18". https://admin.salesforce.com/blog/2018/take-advantage-new-custom-time-field-spring-18 (accessed 2026-11-26)
