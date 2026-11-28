---
id: kt:einstein-discovery
type: Feature
title: Einstein Discovery
aliases: [Einstein Discovery in CRM Analytics, Einstein Discovery in Tableau CRM, Einstein Discovery stories]
domain: data-cloud-and-ai
summary: >-
  The no-code predictive analytics feature of CRM Analytics: it trains supervised machine-learning models on a
  CRM Analytics dataset to explain and predict a business outcome (regression, binary or multiclass), then deploys
  predictions and recommended improvements to record pages, Flow, formulas, recipes, Tableau and the REST API.
release: "Winter '27"
status: current
broader: [kt:crm-analytics]
related: [kt:experience-cloud, kt:formula-fields]
relations:
  - {predicate: integratesWith, object: kt:flow-builder}
  - {predicate: integratesWith, object: kt:tableau}
  - {predicate: alternativeTo, object: kt:ai-models}
  - {predicate: queriedWith, object: kt:einstein-discovery-rest-api}
sources:
  - id: s1
    title: "Get to Know Einstein Discovery (Einstein Discovery Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/einstein-discovery-basics/get-to-know-einstein-discovery
    type: official-learning
    accessed: 2026-11-28
  - id: s2
    title: "Create a Model (Einstein Discovery Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/einstein-discovery-basics/create-a-model-edb
    type: official-learning
    accessed: 2026-11-28
  - id: s3
    title: "Meet Einstein Discovery (Einstein Discovery Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/einstein-discovery-quick-look/meet-einstein-discovery
    type: official-learning
    accessed: 2026-11-28
  - id: s4
    title: "Build Your CRM Analytics Dataset (Einstein Discovery Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/einstein-discovery-basics/build-your-crm-analytics-dataset
    type: official-learning
    accessed: 2026-11-28
  - id: s5
    title: "Add an Einstein Discovery Story to a CRM Analytics Template (Analytics Templates Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/analytics/bi-dev-guide-wave-templates/guide/bi-templatesdev-add-discovery-story.html
    type: official-docs
    accessed: 2026-11-28
  - id: s6
    title: "Einstein Discovery REST API Overview (Einstein Discovery REST API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/einstein-discovery/guide/bi-rest-sdd-overview
    type: official-docs
    accessed: 2026-11-28
created: 2026-11-28
---

# Einstein Discovery

Einstein Discovery is the predictive side of CRM Analytics. It layers statistical modeling and supervised machine learning onto business intelligence in a no-code, iterate-quickly environment, so an analyst can explain what drives a KPI, predict its value for each record, and suggest what to change to improve it.[^s1] It is licensed separately from basic analytics: an org needs either the CRM Analytics Plus license or the Einstein Predictions license, both sold at extra cost.[^s1][^s3]

## What it predicts

Every model is built around one outcome variable, and the outcome's data type decides the use case:[^s1]

- **Regression** predicts a number, such as a currency amount or a count.[^s1]
- **Binary classification** predicts one of two text outcomes, for example whether an opportunity is won.[^s1]
- **Multiclass classification** predicts one of 3 to 10 text outcomes, such as the next opportunity stage.[^s1]

The workflow is deliberately iterative: pick a KPI that fits one of these shapes, then clean the data, add or drop columns, filter, transform, tune the threshold and retrain until the model is useful.[^s1]

## How it works

Training data comes from a CRM Analytics dataset, which can be loaded from Salesforce objects, external sources or a CSV upload in Analytics Studio.[^s4] Einstein Discovery needs at least 400 rows that have outcome values to build a model, ignores rows with no outcome during training, and can analyze up to 20 million rows.[^s4] In Analytics Studio you choose **Create > Model**, pick the dataset, set the goal (for example maximize IsWon = TRUE) and let automated column configuration train the first version.[^s2]

After training, the model reports **data alerts** such as multicollinearity, potential bias and frequently missing values; each alert offers a suggested fix, like bucketing a numeric field, or can be ignored.[^s2] Every change produces a new model version that you train again, and the model's variables table shows each explanatory variable's importance, which accounts for interactions between variables, alongside correlation, which the module stresses is not causation.[^s2] Variable settings include bias analysis and transformations such as fuzzy matching, sentiment detection, text clustering and missing-value replacement, and the general settings let you change the validation method and algorithm.[^s2] You can compare models, review version history and view the generated R code.[^s2]

The output is more than a score. Einstein Discovery produces descriptive, diagnostic and comparative **insights**, **predictions** that can be run as what-if scenarios, and **improvements** tied to variables a user can actually act on, like shipping method or membership level.[^s3] Bias detection flags disparate impact and proxy variables for fields marked as sensitive.[^s3] Models built outside Salesforce can also be uploaded.[^s3]

## Where predictions show up

Once a model is deployed, its predictions and improvements can appear on Lightning record pages and Experience Cloud pages, in CRM Analytics recipes and dataflows, through the PREDICT function in process automation formulas, in Flow Builder, and in Tableau flows, dashboards and calculated fields.[^s3] Developers can call Einstein Prediction Services and the Insights API from REST or Apex.[^s3] The Einstein Discovery REST API, which follows Connect REST API conventions and uses OAuth, can create and retrieve predictions, models and stories.[^s6]

## Limits and gotchas

- The license gate comes first: without CRM Analytics Plus or Einstein Predictions, none of this is available.[^s1]
- Below 400 rows with known outcomes no model is built, and the Trailhead sample model trained on about 7,000 rows is labeled as not very accurate, a reminder that representative, high-quality data matters more than tooling.[^s4]
- Packaging a story into a CRM Analytics template supports numeric, binary and multiclass predictions but not the count analysis type, allows only one story per dataset, requires 2 to 50 fields, and excludes multivalue fields.[^s5]
- Story metadata in templates is case-sensitive, and the outcome definition must match exactly in both places it appears.[^s5]

## When to use it (and when not)

Use Einstein Discovery when the data already lives in CRM Analytics datasets, the question is a classic tabular prediction (amount, yes/no, one-of-N), and business users need explanations and recommended actions on the record, not just a probability.[^s1][^s3] If the model was trained in another tool, it can still be uploaded and deployed through Einstein Discovery's channels.[^s3] It is the wrong tool for a KPI that fits none of the three outcome shapes, or for a dataset too small to train on.[^s1][^s4] For data harmonized in Data 360, compare the AI Models node, which covers the Data 360 modeling workspace.

## Connections

Einstein Discovery is a part of **CRM Analytics** (its broader node), which supplies the datasets, recipes and Analytics Studio it runs in.[^s4] It **integrates with Flow Builder** and with **Tableau**, both of which can consume deployed predictions, and it is **related** to **Experience Cloud** and **formula fields** because predictions surface on site pages and through the PREDICT formula function.[^s3] It is an **alternative to** the Data 360 **AI Models** workspace for no-code predictive modeling, and it is **queried with** the **Einstein Discovery REST API**.[^s3][^s6]

## Sources

[^s1]: Trailhead, "Get to Know Einstein Discovery (Einstein Discovery Basics)". https://trailhead.salesforce.com/content/learn/modules/einstein-discovery-basics/get-to-know-einstein-discovery (accessed 2026-11-28)
[^s2]: Trailhead, "Create a Model (Einstein Discovery Basics)". https://trailhead.salesforce.com/content/learn/modules/einstein-discovery-basics/create-a-model-edb (accessed 2026-11-28)
[^s3]: Trailhead, "Meet Einstein Discovery (Einstein Discovery Quick Look)". https://trailhead.salesforce.com/content/learn/modules/einstein-discovery-quick-look/meet-einstein-discovery (accessed 2026-11-28)
[^s4]: Trailhead, "Build Your CRM Analytics Dataset (Einstein Discovery Basics)". https://trailhead.salesforce.com/content/learn/modules/einstein-discovery-basics/build-your-crm-analytics-dataset (accessed 2026-11-28)
[^s5]: Salesforce Developers, "Add an Einstein Discovery Story to a CRM Analytics Template (Analytics Templates Developer Guide)". https://developer.salesforce.com/docs/analytics/bi-dev-guide-wave-templates/guide/bi-templatesdev-add-discovery-story.html (accessed 2026-11-28)
[^s6]: Salesforce Developers, "Einstein Discovery REST API Overview (Einstein Discovery REST API Developer Guide)". https://developer.salesforce.com/docs/platform/einstein-discovery/guide/bi-rest-sdd-overview (accessed 2026-11-28)
