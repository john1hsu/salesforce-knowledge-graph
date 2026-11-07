---
id: kt:transaction-security-policies
type: SecurityControl
title: Transaction Security Policies
aliases: [Transaction Security, Enhanced Transaction Security, TransactionSecurityPolicy, TSP, Transaction Security Policy Accelerator]
domain: security-and-sharing
summary: >-
  Real-time Event Monitoring rules that evaluate events such as logins, API queries, report runs and list view access
  as they happen and respond by blocking the action, requiring MFA or notifying admins. Built with the Condition
  Builder or Apex; requires Salesforce Shield or the Event Monitoring add-on.
release: "Winter '27"
status: current
broader: [kt:event-monitoring, kt:salesforce-shield]
related: [kt:session-security-levels, kt:login-flows, kt:account-takeover, kt:integration-security]
relations:
  - {predicate: requiresLicense, object: kt:salesforce-shield}
  - {predicate: dependsOn, object: kt:event-monitoring}
  - {predicate: mitigates, object: kt:data-breach-risk}
  - {predicate: mitigates, object: kt:account-takeover}
  - {predicate: integratesWith, object: kt:multi-factor-authentication}
  - {predicate: configuredVia, object: kt:apex}
sources:
  - id: s1
    title: "Get Started with Transaction Security"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/enhanced_transaction_security/enhanced_transaction_security_basics
    type: official-learning
    accessed: 2026-11-07
  - id: s2
    title: "Create a Transaction Security Policy"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/enhanced_transaction_security/enhanced_transaction_security_create
    type: official-learning
    accessed: 2026-11-07
  - id: s3
    title: "Deploy Real-Time Security Guardrails"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/event-monitoring-basics/deploy-real-time-security-guardrails
    type: official-learning
    accessed: 2026-11-07
  - id: s4
    title: "TransactionSecurityPolicy (Object Reference, Winter '27)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_transactionsecurity.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s5
    title: "Getting Started with Enhanced Transaction Security Policies"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2020/07/getting-started-with-enhanced-transaction-security-policies
    type: official-blog
    accessed: 2026-11-07
  - id: s6
    title: "Protecting Sensitive Data in Real Time with Transaction Security Policies"
    publisher: Delivery Hero Tech
    url: https://tech.deliveryhero.com/protecting-sensitive-data-in-real-time-with-transaction-security-policies
    type: community
    accessed: 2026-11-07
created: 2026-11-07
---

# Transaction Security Policies

Transaction Security is the enforcement layer of Salesforce's Real-Time Event Monitoring: it watches events as they occur and applies rules you define, so a risky action can be stopped rather than merely logged.[^s1] Each policy combines an event to watch, a condition, one or more actions and optional notifications, and is either enabled or disabled.[^s1][^s5] It requires a Salesforce Shield or Shield Event Monitoring add-on subscription.[^s1]

## How it works

**Events.** Policies evaluate real-time events. The core four covered in Trailhead are API Event (queries through REST, SOAP or Bulk APIs), List View Event (list view access and export), Login Event, and Report Event (report and dashboard views and exports).[^s1][^s5] The Winter '27 object reference lists a wider set of `EventName` values, including `LoginAsEvent`, `AdminSetupEvent`, `PermissionSetEventStore`, `FileEventStore`, `BulkApiResultEventStore` and anomaly-detection stores such as `ApiAnomalyEventStore`, `ReportAnomalyEventStore`, `CredentialStuffingEventStore`, `SessionHijackingEventStore` and `GuestUserAnomalyEventStore`.[^s4]

**Conditions.** The point-and-click Condition Builder covers most needs: choose an event, set condition logic (for example, all conditions met) and add field comparisons such as Rows Processed greater than or equal to a threshold and Operation equal to `ReportExported`.[^s2] Typical operators map to use cases — Greater Than for volume thresholds, Contains for specific objects, Equals or Starts With for browsers and IP ranges, and Equals on session security level to step up authentication.[^s3] When logic needs related data, such as checking whether the user belongs to a "watch list" public group, an Apex class implements `TxnSecurity.EventCondition`; its `evaluate(SObject event)` method returns `true` to fire the action and `false` to let the user proceed.[^s5] The `TxnSecurity` namespace also offers `AsyncCondition` for asynchronous Apex in Real-Time Event Monitoring policies.[^s4]

**Actions.** A policy can block the operation (with a default or custom block message), require higher assurance through MFA, or take no action, and can notify chosen users by email, in-app notification or both.[^s1][^s2] Notification alone doesn't stop anything; it only creates awareness.[^s3]

**Setup.** Enable the feature from Setup → Transaction Security Policies; authors need the Modify Transaction Security Policies permission. New policies are created disabled and are switched on with the Status toggle on the Actions tab.[^s2] Policies are stored as `TransactionSecurityPolicy` records, whose `ActionConfig` holds actions and recipients and whose `ApexPolicyId` points to the Apex condition class.[^s4] Salesforce Labs' free Policy Accelerator package deploys prebuilt policies for data protection, access control and API monitoring.[^s3]

## Limits and gotchas

Verified against Winter '27:

- **Legacy is gone.** Legacy Transaction Security, with fields like `EventType`, `ResourceName` and `ExecutionUserId`, is retired in all orgs as of Summer '20; only the enhanced, real-time model remains.[^s4]
- **Message sizes.** A custom block message is limited to 1,000 characters and custom email content to 1,333 characters.[^s4]
- **MFA in Lightning.** The MFA action isn't supported in Lightning Experience for List View and Report Event policies; it's upgraded to Block there.[^s4]
- **Lockout risk.** A Login Event policy whose action is Block can lock everyone, including admins, out of the org — prototype in a scratch or playground org.[^s1][^s2]
- **Over-blocking.** Exclude integration and service users by user ID or user type, prefer MFA over Block for login policies, and target thresholds or specific reports rather than blocking all exports.[^s3]
- **Operational upkeep.** Practitioners report that Apex policies driven by "sensitive field" lists or per-object bypass permissions need ongoing maintenance as the data model changes, and that clear block messages reduce user confusion.[^s6]

## When to use it (and when not)

Use transaction security when you must *prevent* an action in the moment: large report or list view exports, API queries on sensitive objects from outside the corporate network, or logins from untrusted locations or browsers.[^s1][^s3] Event log files and dashboards are detective controls that show what already happened; a customer case study pairs them with real-time policies for exactly that reason.[^s6] For coarse access rules that don't depend on event context, sharing settings, permissions and session security levels are cheaper and don't need a Shield licence.

## Connections

Transaction security policies are **part of Event Monitoring** and **Salesforce Shield**, and **require** a Shield or Event Monitoring add-on licence.[^s1] They **depend on** real-time events from Event Monitoring and are **configured via** the Condition Builder or **Apex** classes implementing `TxnSecurity` interfaces.[^s4][^s5] The MFA action demands higher assurance, and conditions can test a session's security level, linking them to **multi-factor authentication** and **session security levels**.[^s1][^s3] By stopping mass exports and suspicious API queries, they **mitigate data breach risk** and **account takeover**, and they complement **integration security** by monitoring API activity.[^s3][^s5]

## Sources

[^s1]: Trailhead, "Get Started with Transaction Security". https://trailhead.salesforce.com/content/learn/modules/enhanced_transaction_security/enhanced_transaction_security_basics (accessed 2026-11-07)
[^s2]: Trailhead, "Create a Transaction Security Policy". https://trailhead.salesforce.com/content/learn/modules/enhanced_transaction_security/enhanced_transaction_security_create (accessed 2026-11-07)
[^s3]: Trailhead, "Deploy Real-Time Security Guardrails". https://trailhead.salesforce.com/content/learn/modules/event-monitoring-basics/deploy-real-time-security-guardrails (accessed 2026-11-07)
[^s4]: Salesforce Developers, "TransactionSecurityPolicy (Object Reference, Winter '27)". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/api/sforce_api_objects_transactionsecurity.htm (accessed 2026-11-07)
[^s5]: Salesforce Developers Blog, "Getting Started with Enhanced Transaction Security Policies". https://developer.salesforce.com/blogs/2020/07/getting-started-with-enhanced-transaction-security-policies (accessed 2026-11-07)
[^s6]: Delivery Hero Tech, "Protecting Sensitive Data in Real Time with Transaction Security Policies". https://tech.deliveryhero.com/protecting-sensitive-data-in-real-time-with-transaction-security-policies (accessed 2026-11-07)
