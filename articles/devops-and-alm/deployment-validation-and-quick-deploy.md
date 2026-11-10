---
id: kt:deployment-validation-and-quick-deploy
type: Feature
title: Deployment Validation and Quick Deploy
aliases: [quick deploy, validated deployment, check-only deployment, checkOnly deployment, deployRecentValidation, sf project deploy quick]
domain: devops-and-alm
summary: >-
  A two-step production release technique: a check-only Metadata API deployment runs the Apex tests and returns a
  job ID without committing anything, and a later quick deploy of that ID within 10 days commits the same components
  without re-running tests.
release: "Winter '27"
status: current
broader: [kt:metadata-api, kt:application-lifecycle-management]
related: [kt:change-sets, kt:release-management, kt:environment-strategy]
relations:
  - {predicate: dependsOn, object: kt:apex-testing}
  - {predicate: configuredVia, object: kt:salesforce-cli}
sources:
  - id: s1
    title: "Deploy a Recently Validated Component Set Without Tests"
    publisher: Salesforce Developers (Metadata API Developer Guide)
    url: https://developer.salesforce.com/docs/platform/api-metadata/guide/meta-rest-deploy-recentvalidation.html
    type: official-docs
    accessed: 2026-11-10
  - id: s2
    title: "project deploy validate"
    publisher: Salesforce Developers (Salesforce CLI Command Reference)
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project_deploy_validate.html
    type: official-docs
    accessed: 2026-11-10
  - id: s3
    title: "project deploy quick"
    publisher: Salesforce Developers (Salesforce CLI Command Reference)
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project_deploy_quick.html
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "Org Development Model: Test and Deploy Changes"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/org-development-model/test-and-deploy-changes
    type: official-learning
    accessed: 2026-11-10
  - id: s5
    title: "Take a Deep Dive into Metadata API Deployments"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/09/take-a-deep-dive-into-metadata-api-deployments
    type: official-blog
    accessed: 2026-11-10
created: 2026-11-10
---

# Deployment Validation and Quick Deploy

**Deployment validation** is a check-only Metadata API deployment: the platform compiles the components, runs the chosen Apex tests and checks coverage, then discards the result instead of committing it. **Quick deploy** takes the ID of a successful validation and deploys the same component set to the same org without running the tests again.[^s1][^s2] The pair lets a team pay the cost of a long production test run ahead of time, during business hours, and then release in a short maintenance window.[^s4]

## How it works

1. **Validate.** Send a deployment with `checkOnly` set to true in the deploy options (REST or SOAP), or run `sf project deploy validate` from a Salesforce DX project. The CLI command requires Apex tests, defaults to `RunLocalTests`, and returns a job ID instead of deploying.[^s1][^s2]
2. **Quick deploy.** Pass that ID to `sf project deploy quick --job-id`, or POST it as `validatedDeployRequestId` to the Metadata REST `deployRequest` resource. A 201 response means a matching validated package was found and a new deployment is running; a 404 means no package meets the requirements.[^s1][^s3]
3. **Confirm.** The validation must have been for the same target org. The Trailhead release walkthrough validates against production by day, quick deploys that evening, then checks the org and runs any manual post-deployment steps.[^s1][^s4]

Under the hood a deployment moves through queuing, component upserts and deletes, Apex testing, a commit phase, and post-commit work. Only one deployment is processed per org at a time, which is one reason a pre-validated deploy shortens the window in which other releases are blocked.[^s5]

## Eligibility rules

A validation qualifies for quick deploy only if it ran within the last 10 days and its Apex tests passed in the target org.[^s1] Coverage rules depend on the test level:

- **All tests or all local tests:** overall org coverage of at least 75%, and every trigger has some coverage.[^s1]
- **`RunSpecifiedTests`:** each class and trigger in the deployment needs at least 75% coverage on its own.[^s1][^s2]

The CLI also offers `RunAllTestsInOrg` and a beta `RunRelevantTests` level, which lets Salesforce choose tests from the payload and its dependencies.[^s2]

## Limits and gotchas

- The job ID is valid for 10 days from when validation started. The `--use-most-recent` flag only finds validations from the past 3 days, so older ones need the explicit `--job-id`.[^s2][^s3]
- Trailhead cautions that the 10-day window holds only if no other deployment or major org change happens in between.[^s4]
- Quick deploy does not support source tracking: it overwrites the matching metadata in the org instead of merging.[^s3]
- Both commands default to waiting 33 minutes; use `--async`, then `sf project deploy report` or `resume`, for long jobs.[^s2][^s3]
- The validate and quick commands target production. For sandboxes the CLI suggests `sf project deploy start --dry-run` with a test level instead.[^s2][^s3]

## When to use it (and when not)

Use it for production releases whose Apex test runs take long enough to threaten a maintenance window, or when a failed deploy mid-window would be costly. Validating early also surfaces missing dependent components and invalid metadata before release night.[^s2][^s4] It is not meant for sandbox deploys, and it is a poor fit when other teams deploy to the same org often, since an intervening deployment or major org change can cost you the validated window.[^s3][^s4]

## Connections

Validation and quick deploy are capabilities of the **Metadata API** (`kt:metadata-api`) and a standard step of **application lifecycle management** (`kt:application-lifecycle-management`), sitting at the production end of an **environment strategy** that stages work through sandboxes first.[^s4] They **depend on Apex testing** (`kt:apex-testing`), because the stored test results and coverage are what make a validation reusable.[^s1] The **Salesforce CLI** (`kt:salesforce-cli`) is the usual way to run both steps.[^s2][^s3] Admins who deploy with Setup-based **change sets** (`kt:change-sets`) reach the equivalent quick deployment from the Deployment Status page, and the technique is a building block of a wider **release management** process (`kt:release-management`).[^s1][^s4]

## Sources
[^s1]: Salesforce Developers, "Deploy a Recently Validated Component Set Without Tests". https://developer.salesforce.com/docs/platform/api-metadata/guide/meta-rest-deploy-recentvalidation.html (accessed 2026-11-10)
[^s2]: Salesforce Developers, "project deploy validate". https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project_deploy_validate.html (accessed 2026-11-10)
[^s3]: Salesforce Developers, "project deploy quick". https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project_deploy_quick.html (accessed 2026-11-10)
[^s4]: Trailhead, "Org Development Model: Test and Deploy Changes". https://trailhead.salesforce.com/content/learn/modules/org-development-model/test-and-deploy-changes (accessed 2026-11-10)
[^s5]: Salesforce Developers Blog, "Take a Deep Dive into Metadata API Deployments" (Neha Ahlawat, 2025-09-23). https://developer.salesforce.com/blogs/2025/09/take-a-deep-dive-into-metadata-api-deployments (accessed 2026-11-10)
