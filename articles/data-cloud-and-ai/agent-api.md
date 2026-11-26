---
id: kt:agent-api
type: API
title: Agent API
aliases: [Agentforce Agent API, Einstein AI Agent API, ai-agent v1 API]
domain: data-cloud-and-ai
summary: >-
  Salesforce's REST API for talking to activated Agentforce agents from outside the Salesforce UI: a client starts a
  session, exchanges messages synchronously or over a server-sent event stream, sends feedback and ends the session,
  authenticating with a JWT-based token from an external client app.
release: "Winter '27"
status: current
broader: [kt:agentforce, kt:salesforce-apis]
related: [kt:agentforce-studio, kt:agentforce-observability, kt:models-api, kt:agent-to-agent-protocol]
relations:
  - {predicate: configuredVia, object: kt:external-client-apps}
  - {predicate: dependsOn, object: kt:client-credentials-flow}
  - {predicate: dependsOn, object: kt:einstein-trust-layer}
  - {predicate: integratesWith, object: kt:generative-ai-audit-and-feedback-data}
sources:
  - id: s1
    title: "Agent API Developer Guide (Agentforce Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api.html
    type: official-docs
    accessed: 2026-11-26
  - id: s2
    title: "Get Started with the Agent API (Agentforce Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api-get-started.html
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "Agent API Session Lifecycle (Agentforce Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api-lifecycle.html
    type: official-docs
    accessed: 2026-11-26
  - id: s4
    title: "Agent API Examples (Agentforce Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api-examples.html
    type: official-docs
    accessed: 2026-11-26
  - id: s5
    title: "Build Custom AI Agents with Agent API (Agent API: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/agent-api-quick-look/build-custom-ai-agents-with-agent-api
    type: official-learning
    accessed: 2026-11-26
created: 2026-11-26
---

# Agent API

The Agent API is a REST interface for conversing with Agentforce agents programmatically. A client opens a session with
an activated agent, sends user messages into it, receives the agent's replies and closes the session when the
conversation is over.[^s1][^s3] Salesforce positions it for putting an agent on a website, running headless agents with
no Salesforce UI, wiring agents into other platforms and workflows, and letting one agent call another.[^s1] Because the
agent keeps context for the life of a session, a multi-turn conversation behaves the same way it would in the
Salesforce-hosted chat surfaces.[^s3]

## How it works

Before calling the API, Agentforce must be enabled and at least one agent activated; agents of the type
"Agentforce (Default)" cannot be reached through it.[^s2][^s5] Access goes through an external client app with OAuth
enabled. The walkthrough uses the client credentials flow, though any flow that returns a JWT-based access token works.[^s2]
The app needs the `api`, `refresh_token, offline_access`, `chatbot_api` and `sfap_api` scopes, must issue JWT-based tokens
for named users, and its client credentials policy names a "Run As" user that has at least API Only access.[^s2] The
token request goes to the org's My Domain URL (not the Lightning domain), and the response points the client at
`https://api.salesforce.com`, the host for all Agent API calls; Government Cloud orgs use `api.gov.salesforce.com`.[^s2][^s4]

A conversation follows a fixed lifecycle:[^s3][^s4]

- **Start a session**: POST to `/einstein/ai-agent/v1/agents/{agentId}/sessions` with an `externalSessionKey`, the org endpoint and the streaming chunk types; the reply carries a `sessionId`.[^s2][^s4]
- **Send a message**: POST to `/einstein/ai-agent/v1/sessions/{sessionId}/messages`, giving each message a `sequenceId` that increases through the session.[^s4]
- **Stream a reply**: POST the same body to `.../messages/stream` with `Accept: text/event-stream` to receive server-sent events instead of one JSON response.[^s4]
- **Give feedback**: POST a `feedbackId` from a reply plus a rating and text to `.../feedback`; a stored rating returns HTTP 201.[^s4]
- **End the session**: DELETE `/einstein/ai-agent/v1/sessions/{sessionId}` with an `x-session-end-reason` header.[^s4]

The `bypassUser` flag on session start decides whose identity the agent uses: `true` runs as the user assigned to the
agent, `false` as the user behind the access token.[^s2] Synchronous replies return a `messages` array of `Inform`
objects that include the text, a `feedbackId`, a `planId`, an `isContentSafe` flag and any `citedReferences`, which can
carry inline citation metadata pointing to source records or links.[^s4]

The streaming endpoint emits typed events. `ProgressIndicator` signals that work such as an action is under way,
`TextChunk` delivers incremental text, `Inform` carries the complete message with citations, and `EndOfTurn` marks the
end of the reply.[^s4] A `ValidationFailureChunk` means the response failed validation: the client should throw away the
chunks it already rendered and display only what streams next.[^s4] Salesforce recommends synchronous calls for simple
request-response cases and streaming for live chat, where text should appear as it is generated.[^s3]

## Limits and gotchas

- A call that runs longer than the API's 120-second timeout fails with HTTP 500, so long-running actions need design attention.[^s5]
- Agent API traffic counts toward generative AI consumption, so high-volume headless use has a credit cost.[^s5]
- Use the My Domain URL for the token request; the Lightning domain does not work for it.[^s2]
- Sessions should be closed explicitly when a conversation finishes rather than left to lapse.[^s5]
- Clients that stream must handle `ValidationFailureChunk`, or users may see text the agent later withdrew.[^s4]
- Setting `bypassUser` to `false` makes record access follow the token's user, which matters for what the agent can read.[^s2]

## When to use it (and when not)

Choose the Agent API when an agent has to live outside Salesforce's own channels: a custom web or mobile front end, a
back-end process with no UI, or another system or agent that needs to delegate a task.[^s1] When the job is a single
model call with no agent reasoning, topics or actions, the lower-level Models API is the simpler fit; when the agent
runs in Salesforce-hosted surfaces, its builder and channel configuration already cover the conversation and no custom
client is needed.[^s1][^s5]

## Connections

The Agent API is an access path to `kt:agentforce` and one of the `kt:salesforce-apis`; the agents it calls are built
and activated in `kt:agentforce-studio`.[^s1][^s2] It is **configured via** `kt:external-client-apps` and **depends on**
an OAuth grant such as `kt:client-credentials-flow` that yields a JWT-based token.[^s2] Replies flow through the
`kt:einstein-trust-layer`, as the per-message content-safety flag shows, and feedback posted through the API is stored in
Data 360, linking it to `kt:generative-ai-audit-and-feedback-data`.[^s4] The `externalSessionKey` lets teams trace a
session in event logs, which ties it to `kt:agentforce-observability`.[^s2] It is related to `kt:models-api`, its
lower-level sibling for direct model calls, and to `kt:agent-to-agent-protocol`, since agent-to-agent invocation is one
of its stated use cases.[^s1]

## Sources
[^s1]: Salesforce, "Agent API Developer Guide (Agentforce Developer Guide)". https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api.html (accessed 2026-11-26)
[^s2]: Salesforce, "Get Started with the Agent API (Agentforce Developer Guide)". https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api-get-started.html (accessed 2026-11-26)
[^s3]: Salesforce, "Agent API Session Lifecycle (Agentforce Developer Guide)". https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api-lifecycle.html (accessed 2026-11-26)
[^s4]: Salesforce, "Agent API Examples (Agentforce Developer Guide)". https://developer.salesforce.com/docs/ai/agentforce/guide/agent-api-examples.html (accessed 2026-11-26)
[^s5]: Trailhead, "Build Custom AI Agents with Agent API (Agent API: Quick Look)". https://trailhead.salesforce.com/content/learn/modules/agent-api-quick-look/build-custom-ai-agents-with-agent-api (accessed 2026-11-26)
