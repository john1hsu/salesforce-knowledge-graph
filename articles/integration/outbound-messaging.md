---
id: kt:outbound-messaging
type: Feature
title: Outbound Messaging
aliases: [outbound message, outbound messages, workflow outbound message, outbound message action]
domain: integration
summary: >-
  Declarative Salesforce action that sends a SOAP/XML notification containing selected fields of a record to an
  external endpoint when a flow, workflow rule or approval process fires it, with queued, retried, at-least-once
  delivery for up to 24 hours.
release: "Winter '27"
status: current
broader: [kt:event-driven-architecture]
related: [kt:record-triggered-flow, kt:approval-processes, kt:workflow-rules]
relations:
  - {predicate: alternativeTo, object: kt:platform-events}
  - {predicate: alternativeTo, object: kt:change-data-capture}
  - {predicate: alternativeTo, object: kt:apex-callouts}
sources:
  - id: s1
    title: "Understanding Notifications (Outbound Messaging)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/object_ref/sforce_api_om_outboundmessaging_notifications.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s2
    title: "Setting Up Outbound Messaging"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/object_ref/sforce_api_om_outboundmessaging_setting_up.htm
    type: official-docs
    accessed: 2026-11-03
  - id: s3
    title: "Understanding the Outbound Messaging WSDL"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api/guide/sforce-api-om-outboundmessaging-wsdl.html
    type: official-docs
    accessed: 2026-11-03
  - id: s4
    title: "Event-Driven Architecture Decision Guide"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/decision-guides/guide/event-driven
    type: official-docs
    accessed: 2026-11-03
  - id: s5
    title: "Use Apex Callouts and Outbound Messages with Heroku"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/salesforce_heroku_integration/callouts_workflow_with_heroku
    type: official-learning
    accessed: 2026-11-03
created: 2026-11-03
---

# Outbound Messaging

Outbound messaging is a point-and-click way to push record data out of Salesforce. An admin defines an outbound message on one object, chooses which fields to include and an endpoint URL, and then fires it from automation. When it fires, Salesforce sends a SOAP message with the selected field values to the listener, so the external system reacts to the change instead of polling for it.[^s1][^s2] Salesforce's event-driven decision guide describes it as a low-code action that sends XML messages to external endpoints, and publishes it from Flow and workflow rules.[^s4]

## How it works

Setup lives under Setup > Outbound Messages (a Workflow Action). Each definition names the object, endpoint URL, the fields to send, and a **User to send as**, whose permissions decide what data the recipient can see. An optional **Send Session ID** setting adds a session for that user (not the user who made the change), so the listener can call back into Salesforce. The saved definition gets an API version and a downloadable WSDL.[^s2] The setup guide names workflow rules and approval process actions as triggers.[^s2] Trailhead shows the modern route: an Action element in a record-triggered flow, on create, update or delete, with entry conditions to narrow which records send.[^s5]

The WSDL defines a `notifications()` call that carries up to 100 notifications. Each one holds the record Id and an sObject with only the chosen fields, plus the org Id, the triggering action Id, the optional session Id, and enterprise and partner API URLs for callbacks. The listener must answer with a single boolean `Ack`, which covers every notification in that message.[^s3]

Delivery is asynchronous. Notifications go onto a local queue and a background process sends them, sometimes batching separate events into one SOAP message. If the record changes again before sending, only the latest data goes out, not each intermediate state.[^s1]

## Limits and gotchas

- **Retry window:** if the endpoint is down, Salesforce retries with exponentially growing gaps, capped at two hours between attempts. Messages older than 24 hours are dropped and never delivered.[^s1]
- **No ordering, possible duplicates:** messages can arrive out of order and occasionally more than once, so listeners should de-duplicate on notification Id.[^s1][^s3] Salesforce warns that it is not suitable for an audit trail.[^s1]
- **Endpoints:** port 80 must be HTTP, port 443 must be HTTPS, and ports from 1024 up allow either. Two-way TLS is possible by installing Salesforce's API client certificate on the listener.[^s2]
- **Loops:** if the listener writes back to Salesforce, it can trigger the same message again. The setup guide suggests a dedicated integration user whose profile has **Send Outbound Messages** turned off.[^s2]
- **Monitoring:** **View Message Delivery Status** lists queued messages and attempt counts, with buttons to retry now or delete.[^s2]
- **Security:** Trailhead notes that without the session Id the listener has no built-in way to check that a request is genuine.[^s5]

## When to use it (and when not)

Outbound messaging is still supported, but Salesforce has said it will make no further investments in it.[^s4] Compared side by side in the decision guide, it has a 24-hour replay period against three days for platform events and Change Data Capture, a WSDL-defined XML payload, and a limit of 100 notifications per message. The guide prefers platform events and CDC for publishing record changes, and Pub/Sub API for new publish/subscribe work.[^s4] It remains a quick fit for simple, low-volume notifications to SOAP-capable listeners when no code is wanted. When the target expects REST and JSON, or needs custom logic, Trailhead contrasts it with Apex HTTP callouts, which send JSON from code.[^s5]

## Connections

Outbound messaging is an early, push-style piece of `kt:event-driven-architecture` on the platform.[^s1][^s4] It is **an alternative to** `kt:platform-events` and `kt:change-data-capture`, the event-bus options Salesforce now prefers for record change notifications.[^s4] It is also **an alternative to** `kt:apex-callouts` when a team chooses between declarative SOAP and coded REST integration.[^s5] It is **related to** the automation that fires it: `kt:record-triggered-flow` actions, and the `kt:workflow-rules` and `kt:approval-processes` actions named in the setup guide.[^s2][^s5]

## Sources

[^s1]: Salesforce Developers, "Understanding Notifications (Outbound Messaging)". https://developer.salesforce.com/docs/atlas.en-us.api.meta/object_ref/sforce_api_om_outboundmessaging_notifications.htm (accessed 2026-11-03)
[^s2]: Salesforce Developers, "Setting Up Outbound Messaging". https://developer.salesforce.com/docs/atlas.en-us.api.meta/object_ref/sforce_api_om_outboundmessaging_setting_up.htm (accessed 2026-11-03)
[^s3]: Salesforce Developers, "Understanding the Outbound Messaging WSDL". https://developer.salesforce.com/docs/platform/api/guide/sforce-api-om-outboundmessaging-wsdl.html (accessed 2026-11-03)
[^s4]: Salesforce Architects, "Event-Driven Architecture Decision Guide". https://architect.salesforce.com/docs/architect/decision-guides/guide/event-driven (accessed 2026-11-03)
[^s5]: Trailhead, "Use Apex Callouts and Outbound Messages with Heroku". https://trailhead.salesforce.com/content/learn/modules/salesforce_heroku_integration/callouts_workflow_with_heroku (accessed 2026-11-03)
