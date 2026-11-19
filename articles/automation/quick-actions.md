---
id: kt:quick-actions
type: Feature
title: Quick Actions
aliases: [quick action, object-specific actions, global actions, publisher actions, QuickAction metadata]
domain: automation
summary: >-
  One-click actions that let users create or update records, log calls, send case email, or launch a flow,
  Lightning web component, Visualforce page or canvas app, either in the context of one record
  (object-specific) or from anywhere in the app (global).
release: "Winter '27"
status: current
broader: [kt:process-automation]
related: [kt:page-layouts, kt:activity-data-model, kt:formula-fields]
relations:
  - {predicate: integratesWith, object: kt:screen-flow}
  - {predicate: integratesWith, object: kt:lightning-web-components}
  - {predicate: integratesWith, object: kt:visualforce}
  - {predicate: configuredVia, object: kt:metadata-api}
sources:
  - id: s1
    title: "Object-Specific versus Global Actions"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.salesforce1appadmin.meta/salesforce1appadmin/s1_admin_guide_actions_obj_vs_global.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s2
    title: "Lightning Experience Customization: Empower Your Users with Quick Actions"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/modules/lex_customization/units/lex_customization_actions
    type: official-learning
    accessed: 2026-11-19
  - id: s3
    title: "Using Predefined Values in Actions"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.salesforce1appadmin.meta/salesforce1appadmin/s1_admin_guide_actions_predef_values.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s4
    title: "Metadata API Developer Guide: QuickAction"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-quickaction.html
    type: official-docs
    accessed: 2026-11-19
  - id: s5
    title: "Lightning Web Components Developer Guide: Quick Actions"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-quick-actions
    type: official-docs
    accessed: 2026-11-19
  - id: s6
    title: "Lightning Web Components Developer Guide: Configure a Component for Quick Actions"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/lwc/guide/use-config-for-quick-actions
    type: official-docs
    accessed: 2026-11-19
created: 2026-11-19
---

# Quick Actions

**Quick actions** are declarative, one-click shortcuts that let users finish a common task (create a related record, update a few fields, log a call, or launch custom UI) without leaving the page they are on. Each action has its own small layout of fields, and the action only appears to users after an admin adds it to a page layout or to the global publisher layout.[^s1][^s2]

## Object-specific vs. global actions

Salesforce has two families of quick action, and the difference is about record context.[^s1]

- **Object-specific actions** are built under an object's *Buttons, Links, and Actions* and can go only on that object's layouts.[^s1]
- **Object-specific Create** links the new record to the source record, e.g. a contact made from Acme joins Acme.[^s1][^s2]
- **Other object-specific types** are Update a Record, Log a Call, Custom (component, flow, Visualforce or canvas), and Send Email on cases only.[^s1]
- **Global actions** are built from the Global Actions page in Setup, have no record context, and support Create, Log a Call and Custom.[^s1]
- **Global actions surface** in the global actions menu in the header once added to the global layout's Mobile & Lightning section.[^s2]

One rule forces the choice: an action that creates a detail record in a master-detail relationship has to be object-specific.[^s1] Object pages inherit actions from the global publisher layout until their own page layout's action section is customized.[^s2]

## How it works

Every action has an **action layout**, edited in a drag-and-drop editor much like the page layout editor; required fields are added automatically and flagged, and removing one stops users from completing the action.[^s2] **Predefined field values** fill fields silently, for example setting Stage to Prospecting on a new-opportunity action so the field can be dropped from the layout. A predefined value wins over a field's default value, and on object-specific actions it can reference the source record and its related objects.[^s3] Predefined values can't be set on multi-select picklists or read-only types such as auto-number, formula and roll-up summary fields.[^s3]

In Lightning Experience the page layout's *Salesforce Mobile and Lightning Experience Actions* section drives what users see, and it is separate from the Classic publisher section. Actions show in the highlights panel's action menu in layout order, while Email, Log a Call, New Event and New Task render in the Activity tab instead.[^s2]

In metadata, actions are the `QuickAction` type (suffix `.quickAction`, folder `quickActions`), introduced in API version 28.0. Its `type` enum spans Create, Update, LogACall, SendEmail, Flow, LightningComponent, LightningWebComponent, VisualforcePage and Canvas, among others, and `fieldOverrides` stores predefined values.[^s4] The guide advises keeping an action layout to eight fields or fewer.[^s4]

## Limits and gotchas

- **LWC actions are record-only:** they work only on Lightning Experience record pages, not as global actions, and not in the Salesforce mobile app.[^s5][^s6]
- **LWC action type is fixed:** `actionType` is `ScreenAction` (modal, the default) or `Action` (headless `invoke()`), and can't be changed later.[^s6]
- **Aura sites unsupported:** LWC quick actions aren't supported in Aura-based Experience Builder sites.[^s5]
- **Customer Chatter groups:** groups that include customers support only the standard Chatter actions such as Post, File, Link and Poll.[^s1]
- **Layout overrides hide buttons:** once you override the Mobile & Lightning action defaults, standard and custom buttons must be added there as actions.[^s2]
- **Flexipage-based actions** appear in the metadata as Beta from API version 68.0, so treat them as preview functionality.[^s4]

## When to use it (and when not)

Use a Create or Update action when a user needs a short, focused form with sensible predefined values, which is especially valuable on mobile.[^s3] When the task needs branching, multiple screens or logic, point a Custom action at a screen flow or a Lightning web component instead.[^s1][^s5] For work that should happen without a user clicking anything, use record-triggered automation rather than an action.

## Connections

Quick actions are a user-initiated entry point into **process automation**, which is why that node is broader. They are placed through **page layouts** and the global publisher layout.[^s1] Their Log a Call and activity actions feed the **activity data model** shown in the Activity tab.[^s2] Custom actions integrate with **screen flows**, **Lightning web components** and **Visualforce**, where a Visualforce page must use the object's standard controller.[^s1][^s6] Predefined values can use **formula** expressions in metadata (`fieldOverrides.formula`), and actions are deployed through the **Metadata API** as `QuickAction` components.[^s4]

## Sources

[^s1]: Salesforce, "Object-Specific versus Global Actions". https://developer.salesforce.com/docs/atlas.en-us.salesforce1appadmin.meta/salesforce1appadmin/s1_admin_guide_actions_obj_vs_global.htm (accessed 2026-11-19)
[^s2]: Trailhead, "Lightning Experience Customization: Empower Your Users with Quick Actions". https://trailhead.salesforce.com/modules/lex_customization/units/lex_customization_actions (accessed 2026-11-19)
[^s3]: Salesforce, "Using Predefined Values in Actions". https://developer.salesforce.com/docs/atlas.en-us.salesforce1appadmin.meta/salesforce1appadmin/s1_admin_guide_actions_predef_values.htm (accessed 2026-11-19)
[^s4]: Salesforce, "Metadata API Developer Guide: QuickAction". https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-quickaction.html (accessed 2026-11-19)
[^s5]: Salesforce, "Lightning Web Components Developer Guide: Quick Actions". https://developer.salesforce.com/docs/platform/lwc/guide/use-quick-actions (accessed 2026-11-19)
[^s6]: Salesforce, "Lightning Web Components Developer Guide: Configure a Component for Quick Actions". https://developer.salesforce.com/docs/platform/lwc/guide/use-config-for-quick-actions (accessed 2026-11-19)
