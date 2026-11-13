---
id: kt:continuous-integration-for-salesforce
type: Pattern
title: Continuous Integration for Salesforce
aliases: [Salesforce continuous integration, Salesforce CI, CI for Salesforce DX, Salesforce CI pipeline]
domain: devops-and-alm
summary: >-
  The practice of automatically validating every Salesforce change merged into source control by having a CI server
  authenticate headlessly with Salesforce CLI, deploy the change to a disposable scratch org or sandbox, and run Apex
  tests and static analysis before the change can merge.
release: "Winter '27"
status: concept
broader: [kt:application-lifecycle-management, kt:salesforce-dx]
related: [kt:branching-strategy, kt:scratch-orgs, kt:deployment-validation-and-quick-deploy, kt:unlocked-packages, kt:testing-strategy]
relations:
  - {predicate: dependsOn, object: kt:salesforce-cli}
  - {predicate: dependsOn, object: kt:jwt-bearer-flow}
  - {predicate: dependsOn, object: kt:apex-testing}
  - {predicate: integratesWith, object: kt:code-analyzer}
  - {predicate: integratesWith, object: kt:devops-center}
sources:
  - id: s1
    title: "Learn How to Test, Build, and Release (Package Development Model)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/sfdx_dev_model/sfdx_dev_model_release
    type: official-learning
    accessed: 2026-11-13
  - id: s2
    title: "Authorize an Org Using the JWT Flow (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-auth-jwt-flow.html
    type: official-docs
    accessed: 2026-11-13
  - id: s3
    title: "project deploy validate (Salesforce CLI Command Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project_deploy_validate.html
    type: official-docs
    accessed: 2026-11-13
  - id: s4
    title: "Run Relevant Apex Tests in a Deployment (Beta) (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-metadata/guide/meta-deploy-run-relevant-tests.html
    type: official-docs
    accessed: 2026-11-13
  - id: s5
    title: "CI/CD Integration with Code Analyzer"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/ci-cd.html
    type: official-docs
    accessed: 2026-11-13
  - id: s6
    title: "Continuous Integration with Salesforce DX"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2019/05/continuous-integration-with-salesforce-dx
    type: official-blog
    accessed: 2026-11-13
created: 2026-11-13
---

# Continuous Integration for Salesforce

Continuous integration (CI) is the practice of running a consistent, automated set of tests against every change merged into an application, so that broken changes are caught before they land in the shared source repository.[^s1] On Salesforce it only becomes practical once source control, not the production org, is the source of truth: Trailhead's package development model puts CI as the second stage, after coding in scratch orgs and before continuous delivery in Developer and Partial Copy sandboxes and release through a Full sandbox to production.[^s1] Salesforce CLI is the engine throughout, because every step a CI job needs (authenticate, create an org, deploy, test) is a scriptable command.[^s1][^s6]

## How a Salesforce CI run works

A CI tool is connected to the version control system with rules for which events trigger a build. On a trigger, it prepares an environment, deploys the change, runs the test suite and publishes a log of which tests passed and where the build broke. Pull request rules then block a merge until the builds pass.[^s6] A typical job has four steps:

1. **Authenticate headlessly.** A CI job cannot open a browser, so it uses the OAuth JWT bearer flow: `sf org login jwt` with the app's consumer key, the private key file and a username.[^s2]
2. **Create a disposable org.** The CLI creates a scratch org from the Dev Hub, so each run tests one change in a clean org loaded with the matching version of the repository.[^s1]
3. **Deploy and test.** Source is deployed with `sf project deploy start`, or a package version is built and installed, and then Apex tests run.[^s1][^s3]
4. **Analyze and report.** Static analysis and test results are published as build artifacts, and failures fail the job.[^s3][^s5]

Salesforce prefers disposable environments such as scratch orgs over shared orgs for this.[^s6] Unlike Developer sandboxes, which refresh at most once a day, scratch orgs can be created throughout the day, deleted quickly, and run in parallel for different purposes.[^s1] The approach fits both models: the package model deploys through scratch orgs and unlocked packages, and the org model deploys to sandboxes with Metadata API commands.[^s6]

## Authentication details and gotchas

The JWT flow needs a certificate and private key (self-signed with OpenSSL is acceptable) and an app that holds the certificate. The guide has you create an external client app for this, but a Dev Hub that will run `org create scratch` or `org create sandbox` still needs a connected app.[^s2] Point `sfdcLoginUrl` in `sfdx-project.json` (or `--instance-url`) at the My Domain URL ending in `my.salesforce.com` rather than a `lightning.force.com` URL, since My Domain URLs survive instance migrations.[^s2] The Dev Hub's consumer key and key file can also authorize its scratch orgs, which is useful when the CI server lacks their access tokens. A "user isn't approved" error usually means the scratch org hasn't replicated yet, so retry. If the org enforces high-assurance (stepped-up) authentication, the identity verification prompt blocks headless JWT logins.[^s2]

## Test levels and quality gates

Against production, `sf project deploy validate` runs the full deployment and its tests without committing anything, then returns a job ID that `sf project deploy quick` can deploy within 10 days without re-running tests. For sandboxes, the CLI reference points to `sf project deploy start --dry-run --test-level RunLocalTests` instead.[^s3] RunLocalTests is the default validation level. RunSpecifiedTests and the beta RunRelevantTests need at least 75% coverage on each class and trigger, counted individually.[^s3] RunRelevantTests lets Salesforce choose tests from the deployment payload and its dependencies, and `@IsTest(critical=true)` or `@IsTest(testFor=...)` can force tests in. Because it skips the rest of the local suite, behavior outside the analyzed scope goes untested.[^s4] For CI reporting, `--junit`, `--coverage-formatters` and `--results-dir` emit machine-readable results, and `--async` or `--wait` (default 33 minutes) keep long runs from stalling the job.[^s3]

Static analysis belongs in the same pipeline. Salesforce Code Analyzer's `code-analyzer run` writes results to a file, and its `--severity-threshold` flag returns a non-zero exit code to fail the build at a chosen severity. The official `run-code-analyzer` GitHub Action should be used at v2, which runs Code Analyzer v5; v1 runs the retired v4.[^s5]

## Choosing a CI tool

Salesforce has published example repositories for AppVeyor, Bamboo, Bitbucket Pipelines, CircleCI, GitLab, Jenkins and Travis CI. It suggests weighing hosted against on-premise (on-premise matters if the build needs a private network), whether your version control system has CI built in, operating system support for the CLI, and pricing.[^s6] Teams wanting less scripting can use DevOps Center, where Code Analyzer can also act as a test provider.[^s5]

## Connections

CI is a core practice of application lifecycle management and is made possible by Salesforce DX and its scriptable Salesforce CLI.[^s1] It runs inside a branching strategy, which decides the merge events that trigger builds, and it relies on disposable scratch orgs and, in the package model, unlocked packages.[^s1][^s6] Headless login depends on the OAuth JWT bearer flow.[^s2] Its gates are Apex testing at a chosen test level, production validation and quick deploy, and static analysis with Code Analyzer, all within a broader testing strategy.[^s3][^s4][^s5] DevOps Center offers a lower-code way to get similar pipeline checks.[^s5]

## Sources
[^s1]: Trailhead, "Learn How to Test, Build, and Release (Package Development Model)". https://trailhead.salesforce.com/content/learn/modules/sfdx_dev_model/sfdx_dev_model_release (accessed 2026-11-13)
[^s2]: Salesforce Developers, "Authorize an Org Using the JWT Flow". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-auth-jwt-flow.html (accessed 2026-11-13)
[^s3]: Salesforce Developers, "project deploy validate". https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project_deploy_validate.html (accessed 2026-11-13)
[^s4]: Salesforce Developers, "Run Relevant Apex Tests in a Deployment (Beta)". https://developer.salesforce.com/docs/platform/api-metadata/guide/meta-deploy-run-relevant-tests.html (accessed 2026-11-13)
[^s5]: Salesforce Developers, "CI/CD Integration with Code Analyzer". https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/ci-cd.html (accessed 2026-11-13)
[^s6]: Salesforce Developers Blog, "Continuous Integration with Salesforce DX" (2019). https://developer.salesforce.com/blogs/2019/05/continuous-integration-with-salesforce-dx (accessed 2026-11-13)
