---
id: kt:dynamic-actions
type: Feature
title: Dynamic Actions
aliases: [Dynamic Actions in Lightning App Builder, dynamic record page actions, Highlights Panel dynamic actions, page-level dynamic actions]
domain: platform-architecture
summary: >-
  A Lightning App Builder capability that moves a record page's action buttons out of the page layout and into the
  Lightning page itself, so admins choose the actions in the Highlights Panel and show or hide each one with
  visibility rules based on record fields, device or user.
release: "Winter '27"
status: current
broader: [kt:lightning-app-builder]
related: [kt:quick-actions, kt:dynamic-forms, kt:dynamic-highlights-panel, kt:salesforce-mobile-app]
relations:
  - {predicate: alternativeTo, object: kt:page-layouts}
sources:
  - id: s1
    title: "Create Dynamic Actions in Lightning App Builder"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.lightning_app_builder_create_dynamic_action.htm&amp=&type=5
    type: official-docs
    accessed: 2026-11-24
  - id: s2
    title: "Learn MOAR: Try Dynamic Actions in App Builder with the Summer '20 Release"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2020/try-dynamic-actions-in-app-builder-with-the-summer-20-release
    type: official-blog
    accessed: 2026-11-24
  - id: s3
    title: "New Low-Code Innovations For Building the Apps You Need, Fast"
    publisher: Salesforce
    url: https://www.salesforce.com/news/stories/new-low-code-innovations-for-building-the-apps-you-need-fast/
    type: news
    accessed: 2026-11-24
created: 2026-11-24
---

# Dynamic Actions

Dynamic Actions let an admin decide, inside Lightning App Builder, which actions appear on a Lightning record page and under what conditions. Instead of inheriting the fixed button list from the object's page layout, the Highlights Panel draws its actions from the Lightning page definition, and each action can carry its own visibility filter.[^s1][^s2] Salesforce introduced the capability alongside Dynamic Forms as a way to show people only the next steps that are relevant to them at that moment, using rules on field values or user information.[^s3]

## How it works

An admin opens a record page in Lightning App Builder, selects the Highlights Panel component and clicks **Upgrade Now** in its properties. From there they either run the migration assistant, which copies the current page-layout actions into the page, or start from an empty list.[^s1] Actions are then added with **Add Action**, and visibility is set with **Add Filter**, which can test a record field, the device type or other criteria; an eye icon marks any action that has a rule.[^s1] Once upgraded, the Highlights Panel is driven by App Builder metadata rather than the page layout, so the page layout's action section stops controlling that page.[^s2][^s1]

Dynamic Actions are available in Lightning Experience in Group, Essentials, Professional, Enterprise, Performance, Unlimited and Developer editions, and creating actions or saving Lightning pages needs the Customize Application permission.[^s1] They work on standard and custom objects, on desktop and mobile.[^s1]

## History

The feature shipped in beta in Summer '20, limited to Highlights Panel actions on custom objects on desktop; standard objects and mobile were on the roadmap at that point.[^s2][^s3] Today the help documentation describes support for both standard and custom objects and for the Salesforce mobile app.[^s1]

## Limits and gotchas

- The upgrade is per Lightning page: only the record page being edited changes, and its users stop seeing the object's page-layout actions there.[^s1]
- A filter takes one value, so matching several values needs one filter per value rather than a comma-separated list.[^s1]
- If a user cannot access the field a filter checks, that criterion evaluates to true, so the action can still appear.[^s1]
- Custom objects use dynamic actions on mobile by default; standard objects need a setting in the Salesforce Mobile App area of Setup.[^s1]
- Desktop and mobile show the same actions by default. Page-level mobile actions, enabled in the page properties, override every other action source on mobile for that page.[^s1]
- Several Highlights Panels with dynamic actions on one page merge into a single action bar on mobile.[^s1]
- The Group object ignores App Builder dynamic actions; its actions stay on the Group Layouts page.[^s1]
- Custom Lightning page templates that use dynamic actions are not supported in the Salesforce mobile app.[^s1]

Visibility filters shape the page rather than enforce access: because an unreadable filter field counts as a match, a rule based on a hidden field is not a reliable way to keep an action from a user.[^s1]

## When to use it (and when not)

Use Dynamic Actions when different users, record states or devices should see different buttons on the same record page, since filters can test field values, device type and user information.[^s3][^s1] Keep page-layout actions when an org still relies on layouts for objects like Group, or when a custom page template must also serve mobile users.[^s1]

## Connections

Dynamic Actions are a capability of `kt:lightning-app-builder` and an alternative to managing record-page buttons in `kt:page-layouts`.[^s1][^s2] The actions they surface are typically `kt:quick-actions` and standard buttons chosen in the Actions window.[^s1] They launched together with `kt:dynamic-forms`, which applies the same rule-based approach to fields, and they are configured on the Highlights Panel, while the separate `kt:dynamic-highlights-panel` component is another action source that page-level mobile actions override.[^s3][^s1] Mobile behavior is controlled separately for the `kt:salesforce-mobile-app`.[^s1] Because the action list lives in App Builder metadata, it travels with the Lightning page rather than with the page layout.[^s2]

## Sources
[^s1]: Salesforce Help, "Create Dynamic Actions in Lightning App Builder". https://help.salesforce.com/s/articleView?language=en_US&id=platform.lightning_app_builder_create_dynamic_action.htm&amp=&type=5 (accessed 2026-11-24)
[^s2]: Salesforce Admins, "Learn MOAR: Try Dynamic Actions in App Builder with the Summer '20 Release". https://admin.salesforce.com/blog/2020/try-dynamic-actions-in-app-builder-with-the-summer-20-release (accessed 2026-11-24)
[^s3]: Salesforce, "New Low-Code Innovations For Building the Apps You Need, Fast". https://www.salesforce.com/news/stories/new-low-code-innovations-for-building-the-apps-you-need-fast/ (accessed 2026-11-24)
