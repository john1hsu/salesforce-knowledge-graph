---
id: kt:agentforce-testing-center
type: Tool
title: Agentforce Testing Center
aliases: [Testing Center, Agentforce Test Suites, Agent Test Suites, New Testing Center]
domain: data-cloud-and-ai
summary: >-
  Salesforce's batch-testing tool for Agentforce agents: test suites of utterances with expected subagents,
  actions and responses, created by CSV upload, AI generation or metadata, run in parallel in a sandbox and
  scored pass/fail per evaluation. The new version (Beta) lives in Agentforce Studio's Tests tab.
release: "Winter '27"
status: beta
broader: [kt:agentforce-studio, kt:testing-strategy]
related: [kt:agent-development-lifecycle, kt:agentforce-dx, kt:agent-actions, kt:sandbox-types, kt:apex-testing]
relations:
  - {predicate: partOf, object: kt:agentforce-studio}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: dependsOn, object: kt:data-cloud}
  - {predicate: integratesWith, object: kt:agentforce-dx}
sources:
  - id: s1
    title: "Trust Your Agents (Agentforce Agent Testing)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-agent-testing/trust-your-agents
    type: official-learning
    accessed: 2026-11-06
  - id: s2
    title: "Set Up Testing Criteria (Agentforce Agent Testing)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agentforce-agent-testing/set-up-testing-criteria
    type: official-learning
    accessed: 2026-11-06
  - id: s3
    title: "View Test Results (Agentforce Agent Testing)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/ko/content/learn/modules/agentforce-agent-testing/view-test-results
    type: official-learning
    accessed: 2026-11-06
  - id: s4
    title: "Auto-Generate Agent Test Cases from Agentforce Data Libraries"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/11/auto-generate-agent-test-cases-from-agentforce-data-libraries
    type: official-blog
    accessed: 2026-11-06
  - id: s5
    title: "Metadata API Reference for Testing API"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/references/testing-api/testing-metadata-reference.html
    type: official-docs
    accessed: 2026-11-06
  - id: s6
    title: "Create an Agent Test from the Spec File"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx-test-create.html
    type: official-docs
    accessed: 2026-11-06
created: 2026-11-06
---

# Agentforce Testing Center

Agentforce Testing Center is Salesforce's no-code tool for testing Agentforce agents at scale, in a repeatable way, before they reach customers. Testing one question at a time in the builder's conversation preview is slow and hard to repeat. Testing Center instead runs batches of user utterances automatically and in parallel, and reports which subagents and actions the agent picked for each one.[^s1] The current version is in Beta and sits in the **Tests** tab of Agentforce Studio as **Test Suites**. An older version lives in Setup.[^s1][^s2]

## How it works

A test suite targets one agent and is a batch of test cases. Each case pairs a single utterance with expectations, and you can reuse and extend a batch over time.[^s1] When you build a suite from a CSV, the template has four columns:[^s2]

- **Utterance**: the user's request. It is always required, along with at least one other column.[^s2]
- **Expected Subagent**: the API name, not the label, of the subagent that should handle the request.[^s2]
- **Expected Actions**: a bracketed list of action API names in single quotes, such as `['IdentifyRecordByName', 'SummarizeRecord']`.[^s2]
- **Expected Response**: a plain-language description of what a correct answer contains.[^s2]

Instead of writing cases by hand, you can have AI generate them. The New Test Suite wizard proposes 20 cases by default from a test objective and the agent's subagents and actions, and you can ask for a mix of positive and negative cases.[^s3] Testing Center can also generate question-and-answer cases from the content in the agent's data libraries, such as FAQs, PDFs and knowledge articles.[^s4]

Each run's results page shows three pass rates: Subagent Evaluation, Action Evaluation and Response Evaluation. For each utterance it shows the expected and actual subagent, actions and response, with pass or fail for each evaluation. Results can be downloaded.[^s3] An agent can choose the right subagent and still fail the action check, for example if it runs only two of three expected actions. To find the cause, rerun the utterance in the builder's conversation preview.[^s3]

## Pro-code path

Behind the UI, an agent test is stored as the **AiEvaluationDefinition** Metadata API type, which requires API version 63.0 or later. Its `subjectType` must be `AGENT`, and `subjectName` holds the agent's API name. If `subjectVersion` is left out, the test runs against the latest active version.[^s5] Each test case has inputs (an utterance, plus optional context variables and conversation history) and named expectations. Built-in expectations include `topic_sequence_match`, `action_sequence_match`, `bot_response_rating`, `coherence`, `completeness`, `conciseness` and `output_latency_milliseconds`. Custom `string_comparison` and `numeric_comparison` checks can read values with JSONPath.[^s5] Because tests are metadata, they can be deployed from org to org and run through the Testing API's Connect REST resources.[^s5] Agentforce DX's `sf agent test create` turns a YAML test spec into an AiEvaluationDefinition and deploys it to the org. The test then appears in Testing Center. Salesforce notes that this documented flow targets the legacy Testing Center, and docs for the new Studio version were still to come.[^s6]

## Limits and gotchas

- **Sandbox only.** Tests can change CRM data, so Salesforce says to run them only in a sandbox. Sandboxes now have access to Data 360 and Agentforce for this testing.[^s1][^s2]
- **Capacity.** You can run up to 10 test jobs at once within a 10-hour window, with up to 1,000 test cases per test.[^s1]
- **Cost.** Test runs consume requests and credits just like production use, sandboxes included.[^s1]
- **Permissions.** The new Testing Center requires Manage Agentforce Grids and Manage Agentforce Testing. The legacy Setup version requires Manage AI Agents or Customize Application on a System Administrator profile.[^s2]
- **Empty expectations fail.** An empty expected value counts as a failure, so leave out columns you don't want to check rather than leaving them blank.[^s2]

## When to use it

Use the conversation preview for quick, one-off checks while you build. Use Testing Center for regression baselines, wide utterance coverage and checks before you activate a new agent version. Use the metadata and CLI path when tests need to live in source control and run in CI.[^s1][^s6]

## Connections

Testing Center is **part of** `kt:agentforce-studio`, whose Tests tab hosts it,[^s3] and it applies `kt:testing-strategy` to non-deterministic AI agents. It covers the test stage of the `kt:agent-development-lifecycle`. It checks whether agents pick the right `kt:agent-actions`.[^s2] It is **configured via** `kt:metadata-api` through AiEvaluationDefinition,[^s5] it **integrates with** `kt:agentforce-dx` through `sf agent test`,[^s6] and it runs in sandboxes (`kt:sandbox-types`) that need Data 360 (`kt:data-cloud`).[^s1] It plays a role for agents similar to the one `kt:apex-testing` plays for code, but it judges probabilistic behavior, not fixed assertions.

## Sources
[^s1]: Trailhead, "Trust Your Agents". https://trailhead.salesforce.com/content/learn/modules/agentforce-agent-testing/trust-your-agents (accessed 2026-11-06)
[^s2]: Trailhead, "Set Up Testing Criteria". https://trailhead.salesforce.com/content/learn/modules/agentforce-agent-testing/set-up-testing-criteria (accessed 2026-11-06)
[^s3]: Trailhead, "View Test Results". https://trailhead.salesforce.com/ko/content/learn/modules/agentforce-agent-testing/view-test-results (accessed 2026-11-06)
[^s4]: Salesforce Developers Blog, "Auto-Generate Agent Test Cases from Agentforce Data Libraries". https://developer.salesforce.com/blogs/2025/11/auto-generate-agent-test-cases-from-agentforce-data-libraries (accessed 2026-11-06)
[^s5]: Salesforce Developers, "Metadata API Reference for Testing API". https://developer.salesforce.com/docs/ai/agentforce/references/testing-api/testing-metadata-reference.html (accessed 2026-11-06)
[^s6]: Salesforce Developers, "Create an Agent Test from the Spec File". https://developer.salesforce.com/docs/ai/agentforce/guide/agent-dx-test-create.html (accessed 2026-11-06)
