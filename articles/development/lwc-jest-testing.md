---
id: kt:lwc-jest-testing
type: Tool
title: LWC Jest Testing
aliases: [sfdx-lwc-jest, Jest tests for Lightning web components, LWC unit tests, "@salesforce/sfdx-lwc-jest"]
domain: development
summary: >-
  Unit testing of Lightning Web Components with the Jest framework through Salesforce's @salesforce/sfdx-lwc-jest
  package, which runs component tests locally in jsdom, without a browser or org, and supplies stubs and mock wire
  adapters for Salesforce modules.
release: "Winter '27"
status: current
broader: [kt:lightning-web-components, kt:testing-strategy]
related: [kt:wire-service, kt:lightning-data-service, kt:javascript-developer-certification]
relations:
  - {predicate: dependsOn, object: kt:salesforce-cli}
  - {predicate: contrastsWith, object: kt:apex-testing}
  - {predicate: integratesWith, object: kt:salesforce-extensions-for-vs-code}
sources:
  - id: s1
    title: "Lightning Web Components Developer Guide: Write Jest Tests"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/unit-testing-using-jest-create-tests.html
    type: official-docs
    accessed: 2026-11-23
  - id: s2
    title: "Lightning Web Components Developer Guide: Write Jest Tests for Wire Service"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/unit-testing-using-wire-utility.html
    type: official-docs
    accessed: 2026-11-23
  - id: s3
    title: "Lightning Web Components Developer Guide: Test Lightning Web Components"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/testing.htm
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "Unit Test Lightning Web Components: Set Up Jest Testing Framework"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/test-lightning-web-components/set-up-jest-testing-framework
    type: official-learning
    accessed: 2026-11-23
  - id: s5
    title: "Unit Test Lightning Web Components: Write a Jest Test for Wire Service"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/test-lightning-web-components/write-a-jest-test-for-wire-service
    type: official-learning
    accessed: 2026-11-23
  - id: s6
    title: "@salesforce/sfdx-lwc-jest package README"
    publisher: npm
    url: https://www.npmjs.com/package/@salesforce/sfdx-lwc-jest
    type: community
    accessed: 2026-11-23
created: 2026-11-23
---

# LWC Jest Testing

Lightning Web Components are unit tested with Jest, a JavaScript testing framework, wrapped by Salesforce's `@salesforce/sfdx-lwc-jest` package. Tests run locally on Node.js without a browser or a Salesforce org, so developers get fast feedback while coding, and watch mode re-runs tests as files change.[^s3] Jest covers Lightning web components only; it does not work with Aura components.[^s3] Typical targets are a component in isolation: its public API (`@api` properties, methods and events), user interactions such as clicks, DOM output and dispatched events.[^s3]

## How it works

Setup needs Node.js and the Salesforce CLI. Running `sf force lightning lwc test setup` in a Salesforce DX project installs `@salesforce/sfdx-lwc-jest` and adds npm scripts for running, watching, debugging and measuring coverage (`test:unit`, `test:unit:watch`, `test:unit:debug`, `test:unit:coverage`).[^s4] Watch mode relies on Git, so the project must be a Git repository.[^s4] The package can also be installed by hand with npm as a dev dependency.[^s4]

Tests live in a `__tests__` folder at the top of each component bundle and must end in `.js`; Salesforce recommends the `.test.js` suffix.[^s1] The folder should be committed to version control but excluded from deployment via `.forceignore`, which the setup command handles by adding a `__tests__` pattern.[^s1] A test imports `createElement` from `lwc`, creates the component, appends it to `document.body`, and asserts against its shadow DOM. Because jsdom state is shared across the tests in a file, an `afterEach` hook should remove the component from the document.[^s1] Rendering is asynchronous: after changing a property on an attached component, the test must wait on a resolved promise before checking the DOM.[^s1]

## Mocking Salesforce modules

The package ships stubs for `lightning` base components and a default `lightning/navigation` stub; other namespaces, or custom mocks, are wired in through `moduleNameMapper` in a `jest.config.js` that extends the package's `jestConfig`.[^s1][^s6] Imperative Apex never executes in Jest, so `@salesforce/apex` imports are mapped to mock modules exposing `jest.fn()` functions whose resolved values the test controls.[^s1]

For `@wire`, sfdx-lwc-jest offers three test adapter flavours: a generic one that emits data on demand, a Lightning Data Service one that mimics LDS shape, and an Apex one that also models error responses.[^s2] Tests call `emit()` with JSON fixtures kept in `__tests__/data`, and Salesforce recommends capturing LDS fixtures from a real UI API response rather than writing them by hand.[^s2] An Apex wire is mocked with `jest.mock` and `createApexTestWireAdapter`, and the error path is exercised by calling `error()` on the adapter; `jest.clearAllMocks()` in `afterEach` stops data leaking between tests.[^s5] Registering wire adapters explicitly is an older pattern from Spring '21 and earlier that still works but is no longer recommended.[^s2]

## Limits and gotchas

- The runner checks that its LWC version matches `sourceApiVersion` in `sfdx-project.json`; `--skipApiVersionCheck` bypasses this at the risk of testing against a stale framework.[^s6]
- Release-named dist-tags exist (for example `winter22`), but `latest` follows the repository, not a Salesforce release.[^s6]
- Jest proves component logic against mocks only; real data access, sharing and cross-component behaviour need org-based or end-to-end tests.[^s1][^s3]
- Watch mode fails outside a Git repository, since it uses Git to find changed files.[^s4]

## When to use it (and when not)

Use Jest for every non-trivial component: it is the fastest feedback loop for rendering logic, event contracts and error states, and it needs no browser or org to run.[^s3] Trailhead even teaches it test-first, writing the failing test before the component.[^s4] It is not a substitute for UI automation in a real org, and it cannot test Aura.[^s3]

## Connections

- **broader → `kt:lightning-web-components`**: the framework is the component model these tests exercise.[^s3]
- **broader → `kt:testing-strategy`**: Jest supplies the fast, isolated unit layer of a broader testing strategy.[^s3]
- **related → `kt:wire-service`** and **`kt:lightning-data-service`**: wire adapters, including LDS ones, are what the test adapters mock.[^s2]
- **dependsOn → `kt:salesforce-cli`**: the CLI scaffolds the setup and generates test files.[^s1][^s4]
- **contrastsWith → `kt:apex-testing`**: Apex tests run in an org and gate deployment; Jest tests run locally and mock Apex.[^s1]
- **integratesWith → `kt:salesforce-extensions-for-vs-code`**: the Extension Pack can run and debug Jest tests from the editor.[^s1]
- **related → `kt:javascript-developer-certification`**: JS credential.

## Sources
[^s1]: Salesforce Developers, "Lightning Web Components Developer Guide: Write Jest Tests". https://developer.salesforce.com/docs/platform/lwc/guide/unit-testing-using-jest-create-tests.html (accessed 2026-11-23)
[^s2]: Salesforce Developers, "Lightning Web Components Developer Guide: Write Jest Tests for Wire Service". https://developer.salesforce.com/docs/platform/lwc/guide/unit-testing-using-wire-utility.html (accessed 2026-11-23)
[^s3]: Salesforce Developers, "Lightning Web Components Developer Guide: Test Lightning Web Components". https://developer.salesforce.com/docs/platform/lwc/guide/testing.htm (accessed 2026-11-23)
[^s4]: Trailhead, "Unit Test Lightning Web Components: Set Up Jest Testing Framework". https://trailhead.salesforce.com/en/content/learn/modules/test-lightning-web-components/set-up-jest-testing-framework (accessed 2026-11-23)
[^s5]: Trailhead, "Unit Test Lightning Web Components: Write a Jest Test for Wire Service". https://trailhead.salesforce.com/content/learn/modules/test-lightning-web-components/write-a-jest-test-for-wire-service (accessed 2026-11-23)
[^s6]: npm, "@salesforce/sfdx-lwc-jest package README". https://www.npmjs.com/package/@salesforce/sfdx-lwc-jest (accessed 2026-11-23)
