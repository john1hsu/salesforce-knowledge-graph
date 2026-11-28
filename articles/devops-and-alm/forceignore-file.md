---
id: kt:forceignore-file
type: Feature
title: .forceignore File
aliases: [forceignore, .forceignore, force ignore file, Salesforce DX ignore file]
domain: devops-and-alm
summary: >-
  A gitignore-style text file in a Salesforce DX project that lists source files and directories Salesforce CLI
  project commands must skip when deploying, retrieving, converting or deleting source.
release: "Winter '27"
status: current
broader: [kt:salesforce-dx]
related: [kt:source-tracking, kt:sfdx-project-structure, kt:package-xml-manifest, kt:lwc-jest-testing]
relations:
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: partOf, object: kt:salesforce-dx}
  - {predicate: dependsOn, object: kt:source-tracking}
sources:
  - id: s1
    title: "How to Exclude Source When Syncing (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-exclude-source.html
    type: official-docs
    accessed: 2026-11-28
  - id: s2
    title: "project list ignored (Salesforce CLI Command Reference)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project_list_ignored.html
    type: official-docs
    accessed: 2026-11-28
  - id: s3
    title: "Salesforce DX Project Configuration (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-ws-config.html
    type: official-docs
    accessed: 2026-11-28
  - id: s4
    title: "gitignore Documentation (Git Reference Manual)"
    publisher: Git project
    url: https://git-scm.com/docs/gitignore
    type: textbook
    accessed: 2026-11-28
created: 2026-11-28
---

# .forceignore File

`.forceignore` is a plain-text file in a Salesforce DX project that tells Salesforce CLI which source files, or which whole directories, to leave out when it syncs metadata between the local project and an org, or when it converts source into DX source format.[^s1] Most `sf project` commands honour it, including `project deploy start`, `project retrieve start`, `project convert source` and `project delete source`.[^s1] It is the main way to keep files such as test folders, local tooling config or org-specific components in version control without ever deploying them.

## How it works

For commands that use source tracking, the file sits in the project root, next to `sfdx-project.json`; for `project convert mdapi` it goes in the retrieved metadata directory that holds `package.xml`.[^s1] Every path in the file is relative to the directory that contains it.[^s1] The package directories the file applies to are the ones declared under `packageDirectories` in `sfdx-project.json`, which tells the CLI where source lives in the project.[^s3]

Salesforce describes the syntax as mimicking `.gitignore` and says the project commands apply the same rules and patterns.[^s1] Paths always use a forward slash, even on Windows; `*` matches anything except a slash; `**` has position-dependent meaning; and blank lines can separate groups of entries.[^s1] In Git's rules, a leading `**/` matches in any directory, a trailing `/**` matches everything inside a directory, and a trailing slash restricts a pattern to directories.[^s4] Git also lets a `!` prefix re-include a file, but not one whose parent directory is already excluded, and the last matching pattern wins.[^s4]

Some files are ignored even with no entry: any file or directory whose name starts with a dot (such as `.DS_Store` or `.sf`), files ending in `.dup`, and the `package2-descriptor.json` and `package2-manifest.json` files.[^s1]

A project can hold more than one `.forceignore`. For each source file, the CLI walks up the directory tree and uses the first `.forceignore` it finds, so a second package directory can carry its own rules that apply only to its files.[^s1]

## Patterns and gotchas

Metadata types with content, such as Apex classes and email templates, are stored as two files, for example `HelloWorld.cls` and `HelloWorld.cls-meta.xml`. To exclude the component, list both files or end the content file's path with an asterisk so it also matches the `-meta.xml` file.[^s1] A whole Lightning web component bundle can be excluded by its folder (`**/lwc/myLwcComponent`), and every Apex class by `**/classes`.[^s1]

To stop a change made directly in an org from being pulled into the project, add the file name that retrieving it would create, such as a permission set's `-meta.xml` file.[^s1] Component names with special characters are URL-encoded on disk (a colon becomes `%3A`), and `.forceignore` must use the encoded file name.[^s1] The exact paths to ignore can be read from the package directory, or from the Path column of `sf project deploy preview` or `sf project retrieve preview` when source tracking is on.[^s1]

To check the rules, `sf project list ignored` lists every forceignored file across the project's package directories.[^s2] Its `--source-dir` (`-p`) flag narrows the check to one directory or tests whether a single file is ignored, and `--json` returns machine-readable output; its older alias is `force:source:ignored:list`.[^s2]

## When to use it (and when not)

Use `.forceignore` for files that belong in the repository but should never reach an org, such as tooling config inside component bundles (the guide's sample output lists an Aura bundle's `.eslintrc.json` as ignored) or components that changed only in one org.[^s1] Lightning web component Jest setup also adds a `__tests__` pattern to it so test folders stay out of deployments. It is not a replacement for `.gitignore`, which decides what Git tracks; the two files usually sit side by side, share a pattern language and list different things.[^s4] When one deployment should include only a chosen set of components, a `package.xml` manifest or the `--metadata` flag of `project deploy start` targets them directly, while `.forceignore` holds standing exclusions applied to every project command.[^s1]

## Connections

`.forceignore` is part of **Salesforce DX** project setup and is read by the **Salesforce CLI** `project` commands.[^s1] It works alongside **source tracking**, whose deploy and retrieve previews show the paths to put in the file.[^s1] It complements the project layout declared in `sfdx-project.json` (**SFDX project structure**), whose package directories it filters, and the explicit component lists of a **package.xml manifest**.[^s3] **LWC Jest testing** depends on it to keep test folders in source control but out of orgs.

## Sources

[^s1]: Salesforce Developers, "How to Exclude Source When Syncing (Salesforce DX Developer Guide)". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-exclude-source.html (accessed 2026-11-28)
[^s2]: Salesforce Developers, "project list ignored (Salesforce CLI Command Reference)". https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project_list_ignored.html (accessed 2026-11-28)
[^s3]: Salesforce Developers, "Salesforce DX Project Configuration (Salesforce DX Developer Guide)". https://developer.salesforce.com/docs/platform/sfdx-dev/guide/sfdx-dev-ws-config.html (accessed 2026-11-28)
[^s4]: Git project, "gitignore Documentation (Git Reference Manual)". https://git-scm.com/docs/gitignore (accessed 2026-11-28)
