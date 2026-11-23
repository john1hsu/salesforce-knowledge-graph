---
id: kt:rich-text-area-fields
type: Feature
title: Rich Text Area Fields
aliases: [rich text area field, Text Area (Rich), RTA field, rich text field]
domain: data-model
summary: >-
  A custom field type, labeled Text Area (Rich) in Setup, that stores formatted text, hyperlinks and inline images as
  HTML of up to 131,072 characters including markup, edited in Lightning with a toolbar-based rich text editor.
release: "Winter '27"
status: current
broader: [kt:custom-fields]
related: [kt:external-objects, kt:field-type-conversion]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: consumedBy, object: kt:lightning-web-components}
sources:
  - id: s1
    title: "Custom Field Types"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_types.htm&type=5
    type: official-docs
    accessed: 2026-11-23
  - id: s2
    title: "Salesforce Error 'Body Data Value too large' After Limit is Raised on the Length of Rich and Long Text Areas"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000383031&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-23
  - id: s3
    title: "WHERE — SOQL and SOSL Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_conditionexpression.htm
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "Input Rich Text — Lightning Component Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-input-rich-text.html
    type: official-docs
    accessed: 2026-11-23
  - id: s5
    title: "Formatted Rich Text — Lightning Component Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-formatted-rich-text.html
    type: official-docs
    accessed: 2026-11-23
created: 2026-11-23
---

# Rich Text Area Fields

A rich text area field is the custom field type that Setup lists as **Text Area (Rich)**. It lets users format text, add hyperlinks and insert images through an editor toolbar, and the platform stores the result as HTML.[^s1] The field can hold up to 131,072 characters, and that ceiling counts every formatting character and HTML tag, not just the visible words.[^s1][^s2] It is the formatted sibling of the long text area field, which shares the same 131,072-character maximum but stores plain text.[^s1][^s2]

## How it works

When you create the field you choose a length. The help article on rich and long text areas gives 256 characters as the minimum and 131,072 (128 KB) as the maximum, with 32,768 as the long text area default.[^s2] Users edit the value in a toolbar editor that supports text styles, lists, indenting, alignment, links and images. Lightning Experience and the Salesforce mobile app render the editor differently from Salesforce Classic, so formatting can look slightly different across interfaces.[^s1] Uploaded images are limited to 1 MB each and must be GIF, JPEG or PNG files.[^s1]

Developers who build custom forms usually pair two base Lightning components. `lightning-input-rich-text` is a WYSIWYG editor with a configurable toolbar. Its categories cover font, text styles, body formatting such as lists and indents, alignment, inserting images and links, and removing formatting.[^s4] It accepts png, jpg, jpeg and gif images up to 1 MB, rejects larger files with an `imageuploaderror` event, and cannot resize images.[^s4] `lightning-formatted-rich-text` displays stored rich text read-only. It keeps only an allow-list of tags and attributes, strips the rest while keeping their text, and turns URLs and email addresses into links unless `disable-linkify` is set.[^s5] Both components sanitize HTML passed to their `value` attribute to prevent cross-site scripting.[^s4][^s5]

## Limits and gotchas

- **Markup counts:** the 131,072-character cap includes HTML tags and formatting, so heavily styled content fills the field sooner than its visible text suggests.[^s1][^s2]
- **Per-object budget:** each object can hold 1,638,400 characters in total across its long text area and rich text area fields.[^s2]
- **Raising the length:** after an org-level length increase, each existing custom field must still be edited one by one, or saves fail with "Body Data Value too large."[^s2]
- **Filtering in SOQL:** the SOQL `WHERE` reference excludes long text area fields from filter expressions. Plan to filter on a separate short field rather than on long, formatted content.[^s3]
- **Reports:** reports show only a truncated prefix of long and rich text values. The "Details Only" export includes the full content.[^s1]
- **External objects:** the Text Area (Rich) type isn't available for external objects.[^s1]
- **Editor behavior:** `lightning-input-rich-text` doesn't validate required input on its own, and pasted formatting is kept only when it matches an enabled toolbar format.[^s4]
- **Image visibility:** by default, images uploaded through `lightning-input-rich-text` are accessible to all users in the org. Use `share-with-entity-id` to narrow access to a record, group or user.[^s4]

## When to use it (and when not)

Use a rich text area field when people need structured, readable content on a record, such as formatted instructions, a summary with bullet points, or an inline diagram.[^s1] Choose a long text area field when the content is plain text, such as notes or integration payloads, because markup won't consume the character budget there.[^s1][^s2] Neither type works well as a filter or grouping key, so keep a short text or picklist field beside it when users must search, report on or route by the content.[^s1][^s3] In custom Lightning Web Components, display stored values with `lightning-formatted-rich-text` rather than inserting raw HTML, so the platform's sanitization applies.[^s5]

## Connections

Rich text area fields are one of the **custom field** types and share the long text area length model and per-object character budget.[^s1][^s2] They are queried with **SOQL**, but long text content can't serve as a `WHERE` filter.[^s3] **Lightning Web Components** consume them through `lightning-input-rich-text` for editing and `lightning-formatted-rich-text` for safe display.[^s4][^s5] Because the type isn't supported on **external objects**, data virtualized from outside systems needs a different field type.[^s1] Changing a field's definition after it holds data, as when raising a rich text field's length, connects to the wider topic of **field type conversion**: each change is applied per field, not in bulk.[^s2]

## Sources
[^s1]: Salesforce Help, "Custom Field Types". https://help.salesforce.com/s/articleView?language=en_US&id=platform.custom_field_types.htm&type=5 (accessed 2026-11-23)
[^s2]: Salesforce Help, "Salesforce Error 'Body Data Value too large' After Limit is Raised on the Length of Rich and Long Text Areas". https://help.salesforce.com/s/articleView?id=000383031&language=en_US&type=1 (accessed 2026-11-23)
[^s3]: Salesforce Developers, "WHERE — SOQL and SOSL Reference". https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_conditionexpression.htm (accessed 2026-11-23)
[^s4]: Salesforce Developers, "Input Rich Text — Lightning Component Reference". https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-input-rich-text.html (accessed 2026-11-23)
[^s5]: Salesforce Developers, "Formatted Rich Text — Lightning Component Reference". https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-formatted-rich-text.html (accessed 2026-11-23)
