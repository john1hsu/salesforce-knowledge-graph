---
id: kt:einstein-next-best-action
type: Feature
title: Einstein Next Best Action
aliases: [Next Best Action, NBA, recommendation strategies, recommendation strategy flow, Einstein NBA]
domain: automation
summary: >-
  Salesforce's recommendation engine: Recommendation records, each tied to a flow, are loaded, filtered and ranked
  by a recommendation strategy built in Flow Builder, and the winners are shown to users or customers who accept
  (launching the flow) or reject them.
release: "Winter '27"
status: current
broader: [kt:process-automation]
related: [kt:service-cloud, kt:experience-cloud]
relations:
  - {predicate: configuredVia, object: kt:flow-builder}
  - {predicate: dependsOn, object: kt:screen-flow}
  - {predicate: consumedBy, object: kt:agent-actions}
  - {predicate: integratesWith, object: kt:einstein-prediction-builder}
sources:
  - id: s1
    title: "Einstein Next Best Action: Understand How Einstein Next Best Action Works"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/einstein-next-best-action/understand-how-einstein-next-best-action-works
    type: official-learning
    accessed: 2026-11-13
  - id: s2
    title: "Improve recommendations with Next Best Action and Agentforce"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2024/deliver-improved-recommendations-through-next-best-action-and-agentforce
    type: official-blog
    accessed: 2026-11-13
  - id: s3
    title: "Einstein Next Best Action Entitlements"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=nba_perms_and_entitlements.htm&type=5
    type: official-docs
    accessed: 2026-11-13
  - id: s4
    title: "Einstein Next Best Actions Considerations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=nba_considerations.htm&type=0
    type: official-docs
    accessed: 2026-11-13
  - id: s5
    title: "Einstein Next Best Action Component"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.nba_lab_cmp.htm&type=5
    type: official-docs
    accessed: 2026-11-13
created: 2026-11-13
---

# Einstein Next Best Action

**Einstein Next Best Action** (NBA) puts the right offer or action in front of a user at the right moment. Admins define **recommendations**, write a **strategy** that decides which of them apply to the current record, optionally feed in a predictive score, and display the winners on a record page, site or app.[^s1] When a user accepts a recommendation, its linked flow runs; the classic Trailhead example offers an auto-renewal to a customer at risk of churning and upsell offers to everyone else.[^s1]

## How it works

A **Recommendation** is a record with a name, description, image, and acceptance and rejection labels, plus an action, normally a flow, that runs on acceptance.[^s1] Every recommendation must point to a flow, and strategies load only recommendations whose flow is active, even though the picker also lists inactive flows.[^s4] Saving a recommendation under an existing name creates a second record rather than overwriting the first, which can surface duplicates to users.[^s4]

A **strategy** is the decision logic. Today it is built as a **recommendation strategy flow** in Flow Builder, which gives strategies access to standard invocable actions, external connectors and visual debugging.[^s2] A strategy can load and filter Recommendation records directly, or load records of any object and convert them at the end with the **Recommendation Assignment** element.[^s4] The **Limit Repetitions** element hides a recommendation from everyone once users have responded to it a set number of times within a set number of days, which requires each recommendation to have a unique record ID.[^s4] Recommendations travel through the strategy and are narrowed by filter and sort logic until only the winners remain.[^s1] A score from Einstein Prediction Builder can act as one input, for example routing customers above a churn-likelihood threshold to a retention offer.[^s1]

Recommendations are displayed by the **Einstein Next Best Action** component on Lightning record pages, where the admin picks the strategy, the number shown (at most four), whether a reject button appears, and whether the component hides itself when nothing qualifies.[^s5] Since Winter '25 the component can also be placed on Experience Cloud sites.[^s2] The REST API exposes recommendations to custom web and mobile apps, and those calls count as requests.[^s3]

## Limits and gotchas

- **Request entitlement.** Each org gets 5,000 strategy requests a month at no charge, in Essentials through Unlimited editions; an add-on SKU adds 10,000 a month.[^s3]
- **Unlimited users.** Service Einstein and Lightning Platform Plus give one user unlimited requests through the Unlimited Next Best Action Strategy Executions permission.[^s3]
- **What counts.** Every load or refresh of a page with the component is a request, as are field updates on that record page, strategy tests and REST API calls.[^s3]
- **Rolling window.** Usage is measured over a rolling 30-day period, while Company Information shows calendar-month usage, so the two can differ.[^s3]
- **No subflows.** Recommendation strategy flows can't call subflows, so shared logic has to be duplicated or moved into invocable actions.[^s4]
- **Run-as user.** Flows launched through the REST API run as the authenticated user, so that user's object and field access applies.[^s4]
- **Reporting.** For Flow Builder strategies, build custom report types on Recommendation Strategy Metrics and Recommendation Responses.[^s4]

Busy record pages can burn through the free allocation quickly, because each refresh counts; overages lead Salesforce to contact the customer about contract additions.[^s3]

## Strategy Builder and its successor

NBA originally had its own **Strategy Builder**, a canvas of colour-coded nodes for loading, filtering, branching and selecting recommendations.[^s1] The Salesforce Admins team now calls Strategy Builder legacy: recommendation strategy flows match its capabilities apart from the Einstein Load node, and both Strategy Builder and Einstein Recommendation Builder are slated to be sunset, so new strategies belong in Flow Builder.[^s2]

## When to use it (and when not)

Use NBA when many possible actions compete for limited screen space and the choice depends on rules or a score, such as service upsells, retention offers or guided next steps.[^s1][^s2] For a single, always-relevant step, a quick action or a screen flow placed on the page is simpler, whereas the NBA component spends a request on every page load.[^s3] The same strategy can also back an **Agentforce** agent action, with `recordId` in and `outputRecommendations` out, so agents and the record page share one ranking logic.[^s2]

## Connections

NBA sits under **process automation** and is **configured via Flow Builder**, where recommendation strategy flows replaced Strategy Builder.[^s2] Each recommendation **depends on a screen flow** (or other flow) that runs when a user accepts it.[^s1][^s4] Strategies can be **consumed by agent actions** in Agentforce.[^s2] They **integrate with Einstein Prediction Builder** scores as decision inputs.[^s1] The feature is most associated with **Service Cloud**, whose Einstein licence grants unlimited requests.[^s3] Its component can also run on **Experience Cloud** sites.[^s2]

## Sources

[^s1]: Trailhead, "Einstein Next Best Action: Understand How Einstein Next Best Action Works". https://trailhead.salesforce.com/content/learn/modules/einstein-next-best-action/understand-how-einstein-next-best-action-works (accessed 2026-11-13)
[^s2]: Salesforce Admins Blog, "Improve recommendations with Next Best Action and Agentforce". https://admin.salesforce.com/blog/2024/deliver-improved-recommendations-through-next-best-action-and-agentforce (accessed 2026-11-13)
[^s3]: Salesforce Help, "Einstein Next Best Action Entitlements". https://help.salesforce.com/s/articleView?language=en_US&id=nba_perms_and_entitlements.htm&type=5 (accessed 2026-11-13)
[^s4]: Salesforce Help, "Einstein Next Best Actions Considerations". https://help.salesforce.com/s/articleView?language=en_US&id=nba_considerations.htm&type=0 (accessed 2026-11-13)
[^s5]: Salesforce Help, "Einstein Next Best Action Component". https://help.salesforce.com/s/articleView?language=en_US&id=platform.nba_lab_cmp.htm&type=5 (accessed 2026-11-13)
