---
id: kt:in-app-guidance
type: Feature
title: In-App Guidance
aliases: [in-app prompts, Lightning prompts, In-App Guidance Builder, in-app walkthroughs, Salesforce prompts and walkthroughs]
domain: platform-architecture
summary: >-
  A declarative Lightning Experience feature that lets admins show floating, targeted or docked prompts, and
  multi-step walkthroughs built from them, on specific app and record pages to train, onboard and inform users at
  the point of work, with audience, scheduling and engagement tracking.
release: "Winter '27"
status: current
broader: [kt:lightning-experience]
related: [kt:change-management-and-adoption, kt:lightning-app-builder, kt:experience-cloud, kt:permission-sets]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: dependsOn, object: kt:profiles}
sources:
  - id: s1
    title: "Promote Feature Adoption and Discovery (Improve User Engagement with In-App Prompts)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/user-engagement/promote-feature-adoption-and-discovery
    type: official-learning
    accessed: 2026-11-28
  - id: s2
    title: "Create Prompts in Agentforce 360 Platform (Optimizing Lightning Prompts Creation)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/user-engagement/create-in-app-prompts
    type: official-learning
    accessed: 2026-11-28
  - id: s3
    title: "Prompt | Metadata Types | Metadata API Developer Guide"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-prompt.html
    type: official-docs
    accessed: 2026-11-28
  - id: s4
    title: "Drive User Engagement at the Point of Impact With In-App Guidance"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/in-app-guidance/
    type: official-blog
    accessed: 2026-11-28
created: 2026-11-28
---

# In-App Guidance

**In-App Guidance** is Salesforce's built-in way to put short, contextual help directly on Lightning Experience pages. Admins create prompts declaratively, decide who sees them, where they appear and for how long, and Salesforce tracks how users respond so it can stop showing a prompt once the user has acted on it.[^s4] When it launched as generally available in 2019, Salesforce positioned it for training, onboarding new users, highlighting changes and making announcements, and listed it for Essentials, Group, Professional, Enterprise, Performance, Unlimited and Developer editions.[^s4]

## Prompts and walkthroughs

A **prompt** is a single window of guidance; a **walkthrough** is a series of connected prompts that leads a user step by step across one or more pages.[^s1] There are three prompt types:[^s1]

- **Floating**: a short, unobtrusive message with an optional image and one button that opens a URL, placed in one of nine page positions.[^s1]
- **Targeted**: like floating, but attached to a specific element on the page rather than a fixed position.[^s1]
- **Docked**: stays put as the user moves around, supports richer text and embedded video, and suits instructions users consult while they work.[^s1]

Trailhead recommends floating and targeted prompts for messages of a sentence or two and docked prompts for longer content.[^s1] It also suggests in-app guidance for easy features, requested enhancements, low-adoption reminders and productivity tips, and advises against relying on it for complex workflows or steep learning curves.[^s1]

## How it works

Admins manage prompts in Setup under In-App Guidance and build them in the **In-App Guidance Builder**, which opens on the target Lightning page.[^s2] The builder sets an end date, whether the prompt shows when the page loads, how many times it shows and how many days pass between showings.[^s2] Audiences default to no profile and no permission restrictions and can be narrowed to specific profiles or permissions.[^s2] Using external images requires a trusted URL, which needs the Customize Application and Modify All Data permissions.[^s2]

Under the hood each prompt is **Prompt** metadata (API version 46.0 and later), stored in a `prompts` folder with the `.prompt` suffix, so prompts can be retrieved and deployed with the Metadata API like other configuration.[^s3] Each prompt carries one or more `PromptVersion` entries that hold the content and targeting: display type (`DockedComposer`, `FloatingPanel` or `Targeted`), target page type and keys, optional record type, theme, image or video, schedule fields, and audience rules expressed as permission or profile filters.[^s3]

## Limits and gotchas

Limits as given in the Metadata API reference for Winter '27 (API version 68.0):[^s3]

- Prompt titles and docked headers allow 36 characters, the dismiss button label 15, and the action button label 25.[^s3]
- From API version 60.0 the body allows 4,000 characters for all prompt types (earlier versions capped floating and targeted bodies at 240); docked counts include HTML markup.[^s3]
- A walkthrough can include up to 10 steps, numbered consecutively.[^s3]
- `timesToDisplay`, the maximum number of times a prompt recurs, has a maximum value of 30.[^s3]
- A prompt can use an image or a video link, not both, and an image needs alt text.[^s3]
- Permission-based audience rules are supported only on app, Home and record pages.[^s3]

On Experience Cloud, prompts carry extra prerequisites: Enablement and Partner Relationship Management must be purchased, the site must use an Aura template, and only floating prompts and walkthroughs made of floating prompts are supported.[^s2]

## Measuring engagement

The In-App Guidance Setup page reports **Views** (unique users who saw a prompt) and **Completes** (the share who clicked the action button, the walkthrough link or Finish).[^s2] For deeper analysis, admins can build a custom report type on the Prompt Actions object, which records fields such as step number, last display date and last result per user, or install free Salesforce Labs report packages from AgentExchange.[^s2]

## When to use it (and when not)

Use In-App Guidance when the message belongs on a specific page at a specific moment: pointing to a new button, announcing a policy change to a permission-defined group, or linking to a Trailhead module about the feature in front of the user.[^s4][^s1] It is a poor fit for teaching multi-step business processes or heavily personalized features, where structured training and well-designed pages do more.[^s1] Because prompts are metadata, treat them like other configuration: build them in a sandbox and move them through the release pipeline.[^s3]

## Connections

In-App Guidance is a feature of **Lightning Experience** and targets the app, Home and record pages that admins assemble in **Lightning App Builder**.[^s3][^s2] It is a delivery tool for **change management and adoption**, supporting rollout and the ongoing measure-and-adjust loop with its engagement metrics.[^s2] Its audience filters rely on **profiles** and **permission sets**, and it is **configured via the Metadata API** through the Prompt type.[^s3] On **Experience Cloud** sites it is available only under the licensing and template conditions above.[^s2]

## Sources

[^s1]: Salesforce Trailhead, "Promote Feature Adoption and Discovery". https://trailhead.salesforce.com/content/learn/modules/user-engagement/promote-feature-adoption-and-discovery (accessed 2026-11-28)
[^s2]: Salesforce Trailhead, "Create Prompts in Agentforce 360 Platform". https://trailhead.salesforce.com/content/learn/modules/user-engagement/create-in-app-prompts (accessed 2026-11-28)
[^s3]: Salesforce, "Prompt | Metadata Types | Metadata API Developer Guide". https://developer.salesforce.com/docs/platform/api-metadata/references/meta-types/metadata-prompt.html (accessed 2026-11-28)
[^s4]: Salesforce, "Drive User Engagement at the Point of Impact With In-App Guidance". https://www.salesforce.com/blog/in-app-guidance/ (accessed 2026-11-28)
