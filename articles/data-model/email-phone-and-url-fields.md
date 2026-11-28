---
id: kt:email-phone-and-url-fields
type: Feature
title: Email, Phone, and URL Fields
aliases: [email field, phone field, url field, contact-point field types, email custom field, phone custom field, url custom field]
domain: data-model
summary: >-
  Three text-based custom field data types on the Salesforce platform for contact points: Email (up to 80 characters,
  pattern-validated), Phone (up to 40 characters, formatted on display) and URL (up to 255 characters, rendered as a
  link), each exposed to the API as its own string-like type that client applications must format correctly.
release: "Winter '27"
status: current
broader: [kt:custom-fields]
related: [kt:external-id-fields, kt:validation-rules, kt:duplicate-management, kt:field-type-conversion, kt:shield-platform-encryption]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: consumedBy, object: kt:lightning-web-components}
  - {predicate: consumedBy, object: kt:soap-api}
sources:
  - id: s1
    title: "Custom Field Types"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_types.htm&type=5
    type: official-docs
    accessed: 2026-11-28
  - id: s2
    title: "Field Types — Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/field_types.htm
    type: official-docs
    accessed: 2026-11-28
  - id: s3
    title: "Custom Fields — Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/custom_fields.htm
    type: official-docs
    accessed: 2026-11-28
  - id: s4
    title: "Input Field — Lightning Component Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-input-field.html
    type: official-docs
    accessed: 2026-11-28
  - id: s5
    title: "Formatted Email — Lightning Component Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-formatted-email.html
    type: official-docs
    accessed: 2026-11-28
  - id: s6
    title: "Formatted Phone — Lightning Component Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-formatted-phone.html
    type: official-docs
    accessed: 2026-11-28
  - id: s7
    title: "Formatted URL — Lightning Component Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-formatted-url
    type: official-docs
    accessed: 2026-11-28
created: 2026-11-28
---

# Email, Phone, and URL Fields

Email, Phone and URL are the three custom field data types Salesforce provides for contact points. Each stores a short
string but adds behavior on top of plain Text: an Email field holds up to 80 characters and checks the address
pattern, a Phone field holds up to 40 characters and is formatted as a phone number, and a URL field holds up to 255
characters and is shown as a clickable link.[^s1][^s4] In the API each is a distinct field type (`email`, `phone` and
`url`) rather than generic `string`, which lets clients and UI components treat them specially.[^s2]

## How it works

**Email.** When a user edits the field through the Lightning input component, the email pattern is validated
automatically and UTF-8 is supported, so international addresses can be entered.[^s4] On read, Lightning renders the
value as a `mailto:` hyperlink that opens the device's default mail application.[^s5] On Contacts and Leads, users can
start an email from the field, but Salesforce Help notes that custom email fields are not used for mass or list email.[^s1]

**Phone.** The input accepts up to 40 characters, and the platform formats the value as a phone number on display.[^s1][^s4]
The display component links the number with the `tel:` scheme, so a click opens a VoIP app on desktop or dials on a
mobile device.[^s6] With an English (United States) or English (Canada) locale, a 10-digit number, or an 11-digit
number starting with 1, appears as (999) 999-9999; prefixing the value with + keeps it in international form.[^s6]
Click-to-dial from the record itself relies on a call-center integration.[^s1]

**URL.** The input checks that a protocol such as `http://` or `ftp://` is present.[^s4] The display component renders
the value as a link; a value without a protocol gets one added, and the component does not handle email addresses or
phone numbers, which have their own components.[^s7] In Lightning Experience, Help describes internal links opening in
the same window and external links in a new one.[^s1]

## Limits and gotchas

- **The API does not format for you.** Client applications must send valid email and URL values and format phone numbers themselves.[^s2]
- **Phone values are free text.** The API notes that phone values can include alphabetic characters, so do not assume digits only.[^s2]
- **Oversized values fail.** Since API version 15.0, a value longer than the field causes a `STRING_TOO_LONG` error instead of truncation, unless `AllowFieldTruncationHeader` is set.[^s2]
- **Only Email can be an External ID.** The object reference limits external IDs to text, number or email fields, so Phone and URL cannot drive an upsert.[^s3]
- **Uniqueness is optional and configurable.** A unique custom field may be case sensitive or insensitive, and duplicates return `DUPLICATE_VALUE`.[^s3]
- **Display formatting is locale-driven.** The (999) 999-9999 pattern applies only to US and Canadian English locales; other locales show values differently.[^s6]

## When to use it (and when not)

Choose these types over Text whenever the value is a real contact point, because users get validation on entry and
clickable `mailto:`, `tel:` and web links on read with no extra code.[^s4][^s5][^s6][^s7] Use Email when the address
must match incoming records during integration, since it is the only one of the three that can be an External ID.[^s3]
Prefer Text for identifiers that merely look like phone numbers or links but are not meant to be clicked, and add
validation rules where the built-in checks are too loose, for example to enforce a country-specific phone pattern,
because the API leaves phone formatting to the client.[^s2] Formula default values are permitted for all three
types, which helps pre-fill a corporate domain or a standard switchboard number.[^s3]

## Connections

These types are a subset of **custom fields** and are queried with **SOQL** like any other string-based field.[^s3]
Email's eligibility makes it a common **external ID field** for **upsert**-style integrations, and its uniqueness
setting complements **duplicate management**.[^s3] Values enter through the **SOAP API** and other APIs that leave
formatting to the caller, so **validation rules** and **data quality** practices fill the gap.[^s2] On the UI side,
**Lightning web components** consume them through base input and formatted-output components.[^s4][^s5][^s6][^s7]
Help lists all three as supporting **Shield Platform Encryption**, and changing them to another type falls under
**field type conversion** rules.[^s1]

## Sources
[^s1]: Salesforce Help, "Custom Field Types". https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_types.htm&type=5 (accessed 2026-11-28)
[^s2]: Salesforce Developers, "Field Types — Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/field_types.htm (accessed 2026-11-28)
[^s3]: Salesforce Developers, "Custom Fields — Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/custom_fields.htm (accessed 2026-11-28)
[^s4]: Salesforce Developers, "Input Field — Lightning Component Reference". https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-input-field.html (accessed 2026-11-28)
[^s5]: Salesforce Developers, "Formatted Email — Lightning Component Reference". https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-formatted-email.html (accessed 2026-11-28)
[^s6]: Salesforce Developers, "Formatted Phone — Lightning Component Reference". https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-formatted-phone.html (accessed 2026-11-28)
[^s7]: Salesforce Developers, "Formatted URL — Lightning Component Reference". https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-formatted-url (accessed 2026-11-28)
