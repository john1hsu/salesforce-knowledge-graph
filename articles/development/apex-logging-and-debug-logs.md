---
id: kt:apex-logging-and-debug-logs
type: Feature
title: Apex Logging and Debug Logs
aliases: [debug logs, Apex debug log, System.debug, trace flags, debug levels, LoggingLevel]
domain: development
summary: >-
  Salesforce debug logs record a transaction's database operations, system processes, Apex messages and errors;
  they are switched on by time-boxed trace flags, filtered by per-category debug levels, and written to from Apex
  with System.debug and a LoggingLevel.
release: "Winter '27"
status: current
broader: [kt:apex]
related: [kt:custom-exceptions, kt:flow-debugging, kt:apex-testing, kt:limits-class]
relations:
  - {predicate: configuredVia, object: kt:tooling-api}
  - {predicate: configuredVia, object: kt:developer-console}
  - {predicate: integratesWith, object: kt:salesforce-cli}
  - {predicate: contrastsWith, object: kt:event-monitoring}
sources:
  - id: s1
    title: "Apex Developer Guide: Debug Log"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/apex-debugging-debug-log.html
    type: official-docs
    accessed: 2026-11-19
  - id: s2
    title: "Debug Logs"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=platform.code_debug_log.htm&type=5
    type: official-docs
    accessed: 2026-11-19
  - id: s3
    title: "Debug Log Levels"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=code_setting_debug_log_levels.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-19
  - id: s4
    title: "Tooling API: TraceFlag"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_traceflag.htm
    type: official-docs
    accessed: 2026-11-19
  - id: s5
    title: "Apex Reference Guide: System Class"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/apex-ref/references/apex-ref/apex-methods-system-system.html
    type: official-docs
    accessed: 2026-11-19
  - id: s6
    title: "The Salesforce Developer's Guide to the Winter '27 Release"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2026/10/developers-guide-to-the-winter-27-release
    type: official-blog
    accessed: 2026-11-19
created: 2026-11-19
---

# Apex Logging and Debug Logs

A debug log is Salesforce's record of what happened inside one transaction or unit test run: database operations, system processes, HTTP callouts, Apex errors, resource usage, and automation such as workflow rules, assignment rules, approval processes and validation rules.[^s1][^s2] Logs leave out actions fired by time-based workflow and transactions started by lead conversion, so those need other diagnostics.[^s2] Because Apex runs on shared multitenant servers, there is no pause-and-step debugger in production; instead, developers turn logging on for a short window, reproduce the problem and read the resulting log.[^s1]

## How it works

Logging is driven by three pieces. A **trace flag** says what to trace and for how long; a **debug level** says how much detail to keep per category; and Apex code adds its own lines with `System.debug`.[^s3][^s4]

- `USER_DEBUG` trace flags capture one user's activity and `DEVELOPER_LOG` captures activity in the Developer Console.[^s3][^s4]
- `CLASS_TRACING` flags on an Apex class or trigger override levels for that code but never create a log on their own.[^s3][^s4]
- Only one trace flag per traced entity can be active, and its expiration must be under 24 hours after its start.[^s4]

A debug level assigns a level to each category: Database, Workflow, NBA, Validation, Callout, Apex Code, Apex Profiling, Visualforce and System.[^s3] Levels run from `NONE` through `ERROR`, `WARN`, `INFO`, `DEBUG`, `FINE` and `FINER` to `FINEST`, and they are cumulative, so `FINE` also keeps `DEBUG`, `INFO`, `WARN` and `ERROR` events.[^s3] One debug level can be shared by many trace flags; deleting it deletes those flags too.[^s4]

In code, `System.debug(msg)` writes at the default `DEBUG` level, and `System.debug(logLevel, msg)` writes at a chosen `LoggingLevel`.[^s5] Non-string arguments go through `String.valueOf`, which uses a class's overridden `toString` if there is one.[^s5] A message appears only when the Apex Code category is set at or above its level.[^s3][^s5]

Each log line is pipe-delimited: a timestamp in the user's time zone, an event identifier such as `CODE_UNIT_STARTED` or `USER_DEBUG`, and details like line numbers. `[EXTERNAL]` marks code with no visible line number, such as managed packages.[^s1] `EXECUTION_STARTED`/`EXECUTION_FINISHED` bracket a transaction, and `CODE_UNIT_STARTED`/`CODE_UNIT_FINISHED` bracket triggers, validation rules and `@future` methods.[^s1]

## Limits and gotchas

- Each log is capped at 20 MB; at that size Salesforce drops 200 KB, usually the oldest lines, so early events can vanish.[^s1][^s2]
- System debug logs are kept 24 hours and monitoring debug logs seven days, so logs are not an audit trail.[^s1][^s2]
- Over 1,000 MB of logs in 15 minutes disables trace flags; their last editors get an email and can re-enable them after 15 minutes.[^s1][^s2]
- Once an org stores more than 1,000 MB of logs, nobody can add or edit trace flags until logs are deleted.[^s1][^s2]
- Tracing busy classes or active users can cause request failures, regardless of window or log size.[^s1]
- Apex Code at `FINEST` logs every variable assignment, which can expose sensitive data and slow deployments noticeably.[^s1][^s3]
- `System.debug` calls do not count toward Apex code coverage, and session IDs are replaced with `SESSION_ID_REMOVED`.[^s1][^s5]

## When to use it (and when not)

Debug logs are the right tool for reproducing a specific bug, checking how close a path runs to governor limits via the Apex Profiling category, or tracing which automation fired in what order.[^s1][^s3] Keep trace flags narrow and short-lived, and avoid tracing frequently run classes or very active users, since that can make requests fail.[^s1] Winter '27 lets developers set per-category levels when running anonymous Apex from Salesforce CLI, and the browser-based Web Console can create trace flags and fetch logs.[^s6]

They are a poor fit for persistent, org-wide observability: retention is a day or a week and volume caps switch tracing off, so long-lived application logging needs a custom framework that stores its own records.[^s1][^s2] For org-wide activity, Event Monitoring's `EventLogFile` records are the closer fit; Winter '27 added Composite API event types there to pinpoint failing subrequests.[^s6]

## Connections

**Apex** is the parent: `System.debug` and `LoggingLevel` are part of the language's `System` namespace.[^s5] Trace flags and debug levels are records `configuredVia` the **Tooling API** (`TraceFlag`, `DebugLevel`) and the **Developer Console**, and the log feature `integratesWith` **Salesforce CLI**, which can set log levels for anonymous Apex.[^s4][^s6] **Flow debugging** relies on the Workflow category of these logs for flows that fail outside Flow Builder.[^s3] **Custom exceptions** and the **Limits class** surface their state in logs, and **Apex testing** writes logs for test runs.[^s1] The node `contrastsWith` **Event Monitoring**, whose `EventLogFile` records are built for org-wide monitoring rather than per-transaction debugging.[^s6]

## Sources
[^s1]: Salesforce Developers, "Apex Developer Guide: Debug Log". https://developer.salesforce.com/docs/platform/apex-dev/references/apex-dev/apex-debugging-debug-log.html (accessed 2026-11-19)
[^s2]: Salesforce Help, "Debug Logs". https://help.salesforce.com/s/articleView?language=en_US&id=platform.code_debug_log.htm&type=5 (accessed 2026-11-19)
[^s3]: Salesforce Help, "Debug Log Levels". https://help.salesforce.com/s/articleView?id=code_setting_debug_log_levels.htm&language=en_US&type=5 (accessed 2026-11-19)
[^s4]: Salesforce Developers, "Tooling API: TraceFlag". https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_traceflag.htm (accessed 2026-11-19)
[^s5]: Salesforce Developers, "Apex Reference Guide: System Class". https://developer.salesforce.com/docs/platform/apex-ref/references/apex-ref/apex-methods-system-system.html (accessed 2026-11-19)
[^s6]: Salesforce Developers Blog, "The Salesforce Developer's Guide to the Winter '27 Release". https://developer.salesforce.com/blogs/2026/10/developers-guide-to-the-winter-27-release (accessed 2026-11-19)
