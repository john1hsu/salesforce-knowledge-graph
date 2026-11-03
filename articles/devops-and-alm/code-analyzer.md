---
id: kt:code-analyzer
type: Tool
title: Salesforce Code Analyzer
aliases: [Code Analyzer, Code Analyzer v5, sf code-analyzer, Salesforce Code Scanner, plugin-code-analyzer]
domain: devops-and-alm
summary: >-
  Salesforce's unified static-analysis tool that runs PMD, ESLint, RetireJS, CPD, Regex, Flow Scanner and other
  engines over Apex, Visualforce, Lightning components and Flows from the `sf code-analyzer` CLI commands, VS Code
  and CI, flagging quality, security and performance issues before deployment.
release: "Winter '27"
status: current
broader: [kt:application-lifecycle-management, kt:salesforce-dx]
related: [kt:technical-debt-in-salesforce, kt:second-generation-managed-packages, kt:apex, kt:lightning-web-components, kt:flow-builder]
relations:
  - {predicate: partOf, object: kt:salesforce-cli}
  - {predicate: enables, object: kt:appexchange-security-review}
  - {predicate: mitigates, object: kt:soql-injection}
sources:
  - id: s1
    title: "Salesforce Code Analyzer"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/code-analyzer.html
    type: official-docs
    accessed: 2026-11-03
  - id: s2
    title: "Engines"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/engines.html
    type: official-docs
    accessed: 2026-11-03
  - id: s3
    title: "Elevate Your Team's Code Quality with Salesforce Code Analyzer v5"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/07/elevate-your-teams-code-quality-with-salesforce-code-analyzer-v5
    type: official-blog
    accessed: 2026-11-03
  - id: s4
    title: "Salesforce CLI Command Reference: code-analyzer run"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_code-analyzer_run.html
    type: official-docs
    accessed: 2026-11-03
  - id: s5
    title: "Produce Code Analyzer Reports for AppExchange Security Review"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/appexchange.html
    type: official-docs
    accessed: 2026-11-03
created: 2026-11-03
---

# Salesforce Code Analyzer

Salesforce Code Analyzer is Salesforce's static-analysis tool for platform code. It scans Apex, Visualforce, Flows and Lightning components for quality, security and performance problems so they surface before deployment rather than in production.[^s1] Version 5 is current: Salesforce announced v5 as generally available in July 2025, and v4 was retired in August 2025 and is no longer supported.[^s3][^s1]

## How it works

Code Analyzer is a single front end over several analysis **engines**, each owning a set of rules. PMD covers Apex, Visualforce and other languages and also carries the AppExchange rules; ESLint handles JavaScript and TypeScript; RetireJS checks third-party JavaScript libraries for known vulnerabilities; and CPD finds duplicated code blocks.[^s2] Version 5 added two engines: **Regex**, which runs pattern rules you define in configuration, and **Flow Scanner**, which audits Flows for security issues.[^s2][^s1] Salesforce Graph Engine (data-flow analysis of Apex) is listed as a developer preview, and ApexGuru scans code in a connected org.[^s2] Altogether the tool ships more than 500 built-in rules, each with default tags and a severity you can override.[^s1]

Developers reach it three ways. The `@salesforce/plugin-code-analyzer` plugin adds a `code-analyzer` topic to the Salesforce CLI. A VS Code extension gives in-editor feedback and offers Agentforce for Developers quick fixes. A GitHub Action runs scans in pipelines, uploads results as an artifact and writes a job summary.[^s1] The main commands are `sf code-analyzer run` to scan, `rules` to list rules, and `config` to generate a baseline configuration file.[^s3]

## Configuration and selecting rules

Behaviour is controlled by a YAML file, usually `code-analyzer.yml`. It can add custom rules, change severities, tune engines and exclude paths. The defaults work without one.[^s1] If `code-analyzer.yml` or `code-analyzer.yaml` sits in the current folder, `run` applies it automatically; `--config-file` is only needed for another name or location.[^s4] Salesforce recommends listing only the rules you override, because this file takes precedence over other sources such as PMD XML rulesets.[^s3]

`--rule-selector` defaults to `Recommended`. It can select by engine, severity, rule name or tag: a colon means AND, a comma means OR, and repeated flags are ORed together.[^s4] So `pmd:Performance` narrows to one engine's category, while `AppExchange` selects the security-review rules that v4 kept in a separate engine.[^s3][^s1]

## Limits and gotchas

- **Severity scale.** Severity 1 is Critical, 2 High, 3 Moderate.[^s3] `--severity-threshold` sets the lowest severity that makes the command exit non-zero. That non-zero exit is what lets a pipeline fail the build.[^s4]
- **Output.** Results go to the terminal unless you pass `--output-file`. Supported formats are CSV, HTML, JSON, SARIF and XML. The target folder must already exist, and existing files are overwritten without a prompt.[^s4]
- **Scope.** `--workspace` defaults to the current folder, and `--target` must lie inside the workspace. Without `--target`, every file in the workspace is scanned.[^s4]
- **Static analysis isn't proof.** A clean scan doesn't certify that code is secure, and some findings are false positives. That's why AppExchange reviewers accept reports with justified, unresolved violations.[^s5]

## When to use it

Use Code Analyzer as the pull-request gate in any source-driven pipeline. A common pattern fails the build on any severity 1–2 finding or once total violations pass an agreed budget.[^s3] For AppExchange partners it is the expected pre-submission scan. Run `--rule-selector AppExchange --rule-selector Recommended:Security` with an HTML output file, fix what you can, re-run, and attach the reports in the Security Review Wizard. The scans do not have to pass 100%.[^s5] It complements unit tests rather than replacing them: tests prove behaviour, and the analyzer finds risky patterns such as CRUD violations or SOQL injection.[^s3]

## Connections

Code Analyzer is a tool within **application lifecycle management** and the **Salesforce DX** source-driven model. It is **part of** the **Salesforce CLI** as a plugin.[^s1] It **enables** the **AppExchange security review** by producing the reports partners submit, so partners building **second-generation managed packages** can run it in CI before creating versions.[^s5][^s1] Its rules **mitigate** **SOQL injection** among other security risks.[^s3] It analyzes **Apex** (PMD, Graph Engine), **Lightning Web Components** (ESLint, RetireJS) and **Flow Builder** flows (Flow Scanner).[^s2] Because it flags quality and performance issues as code changes, it is a practical way to keep **technical debt** visible.[^s1]

## Sources
[^s1]: Salesforce Developers, "Salesforce Code Analyzer". https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/code-analyzer.html (accessed 2026-11-03)
[^s2]: Salesforce Developers, "Engines". https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/engines.html (accessed 2026-11-03)
[^s3]: Salesforce Developers Blog, "Elevate Your Team's Code Quality with Salesforce Code Analyzer v5". https://developer.salesforce.com/blogs/2025/07/elevate-your-teams-code-quality-with-salesforce-code-analyzer-v5 (accessed 2026-11-03)
[^s4]: Salesforce Developers, "Salesforce CLI Command Reference: code-analyzer run". https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_code-analyzer_run.html (accessed 2026-11-03)
[^s5]: Salesforce Developers, "Produce Code Analyzer Reports for AppExchange Security Review". https://developer.salesforce.com/docs/platform/salesforce-code-analyzer/guide/appexchange.html (accessed 2026-11-03)
