---
id: kt:sandboxpostcopy-interface
type: Feature
title: SandboxPostCopy Interface
aliases: [SandboxPostCopy, System.SandboxPostCopy, sandbox post-copy script, post-copy Apex class, runApexClass, SandboxContext]
domain: devops-and-alm
summary: >-
  The Apex interface whose runApexClass(SandboxContext) method Salesforce runs automatically at the end of each
  sandbox create, clone or refresh, so a team can script post-copy setup such as creating users or sanitizing records.
release: "Winter '27"
status: current
broader: [kt:sandbox-types, kt:apex]
related: [kt:sandbox-templates, kt:data-mask-and-seed, kt:apex-testing, kt:test-data-factory]
relations:
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: configuredVia, object: kt:tooling-api}
  - {predicate: alternativeTo, object: kt:data-mask-and-seed}
sources:
  - id: s1
    title: "SandboxPostCopy Interface (Apex Reference Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_interface_System_SandboxPostCopy.htm
    type: official-docs
    accessed: 2026-11-22
  - id: s2
    title: "Create a Sandbox Definition File (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-sandbox-definition.html
    type: official-docs
    accessed: 2026-11-22
  - id: s3
    title: "Create, Clone, or Refresh a Sandbox (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-create-clone-sandboxes.html
    type: official-docs
    accessed: 2026-11-22
  - id: s4
    title: "SandboxInfo (Tooling API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/tooling_api_objects_sandboxinfo.htm
    type: official-docs
    accessed: 2026-11-22
  - id: s5
    title: "org create sandbox (Salesforce CLI Command Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_org_create_sandbox.html
    type: official-docs
    accessed: 2026-11-22
created: 2026-11-22
---

# SandboxPostCopy Interface

`System.SandboxPostCopy` is the Apex interface that lets a team attach a setup script to a sandbox. You write a class that implements it, name that class when you create the sandbox, and Salesforce calls the class once the copy finishes, so every fresh sandbox comes up already prepared for use.[^s1] Typical jobs are creating users, sanitizing copied records and other environment setup that would otherwise be a manual checklist after every refresh.[^s1]

## How it works

The interface has a single method, `runApexClass(System.SandboxContext context)`, which returns nothing.[^s1] The context object tells the script where it is running: `organizationId()`, `sandboxId()` and `sandboxName()` return the new org's ID, the sandbox ID and the sandbox name.[^s1] Branching on the sandbox name is a common way to give a UAT sandbox different setup from a developer sandbox while sharing one class.

The script runs at the end of the sandbox copy under a special Automated Process user that is not visible in the org, with that user's permissions.[^s1] The class is attached per sandbox, and the DX guide describes it as running after each copy of the sandbox, which covers later refreshes as well as the first creation.[^s2]

There are three places to name the class:

- **Setup UI**: choose the Apex class while creating the sandbox, as the interface documentation describes.[^s1]
- **Salesforce CLI**: set `apexClassName` or `apexClassId` in the sandbox definition file; the two are mutually exclusive.[^s2]
- **No CLI flag**: `sf org create sandbox` accepts only name and license type as flags, so an Apex class requires a definition file.[^s5]
- **Tooling API**: the `ApexClassId` field on `SandboxInfo` points to an Apex class extending `SandboxPostCopy` and has been available since API version 36.0.[^s4]

Creating a `SandboxInfo` record queues a new sandbox and updating one refreshes it, and each operation produces a `SandboxProcess` record that can be used to monitor progress.[^s4] On the CLI the matching commands are `sf org create sandbox --definition-file …` and `sf org refresh sandbox`; a refresh can take a definition file to change options at the same time.[^s3]

## Testing

Because the class only runs during a sandbox copy, Salesforce supplies `Test.testSandboxPostCopyScript()` for unit tests. It takes an instance of the implementing class plus the org ID, sandbox ID and sandbox name that would form the context.[^s1] An overload adds a Boolean that makes the test run as the Automated Process user, which is the closest simulation of real execution.[^s1] Testing with that flag set is worth doing, because a script that passes as a system administrator can still fail at copy time.

## Limits and gotchas

- **Restricted running user.** The Automated Process user cannot reach every object and feature, so some setup steps will fail inside the script.[^s1]
- **Failure recovery is manual.** If the script fails, the documented fix is to run it after activation as a user who has the needed permissions.[^s1]
- **Name or ID, not both.** A definition file may set `apexClassName` or `apexClassId`, never both.[^s2]
- **Long copies.** Sandbox creation and cloning are queued and can outlast the CLI wait time; if a command times out, use the returned job ID with `sf org resume sandbox`.[^s3]

Because a failed script may have to be run again by hand after activation, keep it idempotent and small.[^s1] Large data loads are better handled by a seeding tool or a data load job than by a single post-copy transaction.

## When to use it (and when not)

Use `SandboxPostCopy` for deterministic, code-reviewed environment setup: resetting integration endpoints stored in custom settings, creating test users, scrubbing email addresses or inserting a small reference data set. It complements sandbox templates, which decide which objects a Partial Copy or Full sandbox copies; the script then adjusts what arrived.[^s2] For masking large volumes of sensitive data or seeding related records from production, a product such as Data Mask & Seed is the alternative.

## Connections

The interface is part of the **sandbox** lifecycle described in **Sandbox Types**, and it is ordinary **Apex**, so it is subject to Apex rules and is unit-tested through **Apex testing** with `Test.testSandboxPostCopyScript()`.[^s1] It is configured through **Salesforce CLI** sandbox definition files and through the **Tooling API** `SandboxInfo` object.[^s2][^s4] **Sandbox templates** choose the data that is copied before the script runs, and **Data Mask & Seed** is the product alternative for masking and seeding at scale.[^s2] Reusable record builders from a **test data factory** are often shared between tests and post-copy seeding code.

## Sources

[^s1]: Salesforce Developers, "SandboxPostCopy Interface" (Apex Reference Guide). https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_interface_System_SandboxPostCopy.htm (accessed 2026-11-22)
[^s2]: Salesforce Developers, "Create a Sandbox Definition File" (Salesforce DX Developer Guide). https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-sandbox-definition.html (accessed 2026-11-22)
[^s3]: Salesforce Developers, "Create, Clone, or Refresh a Sandbox" (Salesforce DX Developer Guide). https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-create-clone-sandboxes.html (accessed 2026-11-22)
[^s4]: Salesforce Developers, "SandboxInfo" (Tooling API Developer Guide). https://developer.salesforce.com/docs/atlas.en-us.264.0.api_tooling.meta/api_tooling/tooling_api_objects_sandboxinfo.htm (accessed 2026-11-22)
[^s5]: Salesforce Developers, "org create sandbox" (Salesforce CLI Command Reference). https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_org_create_sandbox.html (accessed 2026-11-22)
