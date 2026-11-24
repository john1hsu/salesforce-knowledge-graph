---
id: kt:dynamic-highlights-panel
type: Feature
title: Dynamic Highlights Panel
aliases: [Dynamic Highlights Panel component, record highlights in Lightning App Builder, configurable highlights panel]
domain: platform-architecture
summary: >-
  A Lightning App Builder field-container component, introduced in Winter '25, that lets admins choose and arrange up
  to 12 key fields at the top of a record page, with per-field visibility rules and dynamic actions, instead of
  driving the highlights area from the object's compact layout.
release: "Winter '27"
status: current
broader: [kt:lightning-app-builder]
related: [kt:dynamic-forms, kt:dynamic-actions, kt:salesforce-mobile-app, kt:field-level-security]
relations:
  - {predicate: alternativeTo, object: kt:compact-layouts}
  - {predicate: dependsOn, object: kt:lightning-web-components}
sources:
  - id: s1
    title: "Maintain Your Platform App Builder Certification for Winter '25"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/platform-app-builder-certification-maintenance-winter-25/maintain-your-platform-app-builder-certification-for-winter-25
    type: official-learning
    accessed: 2026-11-24
  - id: s2
    title: "Jen's Top Winter '25 Release Features | Be Release Ready"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2024/jens-top-winter-25-release-features-be-release-ready
    type: official-blog
    accessed: 2026-11-24
  - id: s3
    title: "Jen's Top Winter '27 Release Features For Admins"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2026/jens-top-winter-27-release-features-for-admins
    type: official-blog
    accessed: 2026-11-24
  - id: s4
    title: "The Ultimate Guide to the Salesforce Dynamic Highlights Panel"
    publisher: Salesforce Ben
    url: https://www.salesforceben.com/the-ultimate-guide-to-the-salesforce-dynamic-highlights-panel/
    type: community
    accessed: 2026-11-24
  - id: s5
    title: "Dynamic Highlights Panel: Conditional Field Visibility for Enhanced Focus"
    publisher: Automation Champion
    url: https://automationchampion.com/2024/08/13/dynamic-highlights-panel-conditional-field-visibility-for-enhanced-focus/
    type: community
    accessed: 2026-11-24
created: 2026-11-24
---

# Dynamic Highlights Panel

The Dynamic Highlights Panel is a record-page component in Lightning App Builder that holds the handful of key fields shown at the top of a record. Before it arrived, the fields in a record's highlights area could only be set through the object's compact layout in Setup; with this component, admins pick and order those fields directly on the Lightning page.[^s1][^s2] Salesforce shipped it in the Winter '25 release, describing it as responsive and able to hold up to 12 fields.[^s2][^s4]

It is a different thing from the classic Highlights Panel component. The classic panel takes its fields from the compact layout and can be upgraded to use dynamic actions; the Dynamic Highlights Panel is a separate component that manages both its fields and its actions on the page itself.[^s1][^s4]

## How it works

The component sits on the **Fields** tab of Lightning App Builder rather than the Components tab, and behaves like a Field Section from Dynamic Forms: it is a container that admins fill by dragging fields in.[^s1][^s2] A **Primary Field** is preselected and can be changed; community guidance recommends keeping the record's Name field there.[^s1][^s4] Fields stay readable when the window is resized because the layout is responsive rather than truncating values.[^s1]

Each field in the panel can carry its own visibility rule, so the panel can show, for example, a loss-reason field only when an opportunity is Closed Lost, or different fields at each lead status.[^s4][^s5] The whole component can also be filtered, for instance by the viewing user's profile, which lets one page host several variants of the panel.[^s4] Conditional field formatting, another Winter '25 addition, also works on fields inside the panel.[^s2]

Actions in the panel use dynamic actions by default, so admins choose buttons and set their visibility in App Builder rather than on the page layout.[^s1][^s2] Trailhead states the component is supported for all LWC-enabled objects and applies to Lightning Experience in Group, Professional, Enterprise, Performance, Unlimited and Developer editions.[^s1]

## Mobile

Desktop users see the panel as soon as the page is saved. For the Salesforce mobile app, an admin must turn on **Dynamic Forms and Dynamic Highlights Panel on Mobile** under Salesforce Mobile App in Setup, a single setting shared with Dynamic Forms.[^s1][^s2] Orgs that do not enable that setting still need a standard Highlights Panel on the page, typically filtered to mobile only, or mobile users get no highlights area at all.[^s4]

## Limits and gotchas

- The panel holds at most 12 fields; practitioners advise showing far fewer so the summary stays scannable.[^s1][^s4]
- The primary field cannot have a visibility rule and cannot be a cross-object field; if field-level security hides it, the user sees the record Name instead.[^s4]
- Blank spaces cannot be inserted between fields, and the panel cannot be shown in a collapsed state.[^s4][^s5]
- When it launched, the panel had no Follow or Unfollow button, a gap Salesforce addressed in Winter '27 (below).[^s5][^s3]
- Visibility rules change what the page shows, not what a user can access; data protection still comes from field-level security.[^s4]

## What changed in Winter '27

Winter '27 lets admins show the standard Follow button inside the highlights panel. It is hidden by default and controlled per Lightning page with a **Hide Follow/Unfollow button** checkbox in the panel's properties; Salesforce suggests testing the setting in a sandbox because the checkbox wording reads against the default.[^s3]

## When to use it (and when not)

Use the Dynamic Highlights Panel when different users or record states need different summary fields, or when admins want field and action placement for a record page managed in one place in App Builder alongside Dynamic Forms.[^s1][^s4] Keep the classic panel and compact layout where the compact layout already serves well across pages, or where mobile users would otherwise lose the panel because the mobile setting is not enabled.[^s4][^s2]

## Connections

The component is part of `kt:lightning-app-builder` and an alternative to configuring highlights fields through `kt:compact-layouts`.[^s1][^s2] It shares its container model and mobile setting with `kt:dynamic-forms` and uses `kt:dynamic-actions` for its buttons by default.[^s1][^s2] Support follows LWC-enabled record pages built on `kt:lightning-web-components`, and its mobile behavior is switched on separately for the `kt:salesforce-mobile-app`.[^s1] Field visibility filters complement rather than replace `kt:field-level-security`, which also decides what appears in the primary field.[^s4]

## Sources
[^s1]: Trailhead, "Maintain Your Platform App Builder Certification for Winter '25". https://trailhead.salesforce.com/content/learn/modules/platform-app-builder-certification-maintenance-winter-25/maintain-your-platform-app-builder-certification-for-winter-25 (accessed 2026-11-24)
[^s2]: Salesforce Admins, "Jen's Top Winter '25 Release Features | Be Release Ready". https://admin.salesforce.com/blog/2024/jens-top-winter-25-release-features-be-release-ready (accessed 2026-11-24)
[^s3]: Salesforce Admins, "Jen's Top Winter '27 Release Features For Admins". https://admin.salesforce.com/blog/2026/jens-top-winter-27-release-features-for-admins (accessed 2026-11-24)
[^s4]: Salesforce Ben, "The Ultimate Guide to the Salesforce Dynamic Highlights Panel". https://www.salesforceben.com/the-ultimate-guide-to-the-salesforce-dynamic-highlights-panel/ (accessed 2026-11-24)
[^s5]: Automation Champion, "Dynamic Highlights Panel: Conditional Field Visibility for Enhanced Focus". https://automationchampion.com/2024/08/13/dynamic-highlights-panel-conditional-field-visibility-for-enhanced-focus/ (accessed 2026-11-24)
