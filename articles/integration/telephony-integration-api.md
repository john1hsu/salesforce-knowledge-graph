---
id: kt:telephony-integration-api
type: API
title: Telephony Integration API
aliases: [Telephony Integration REST API, Salesforce Voice Telephony Integration API, Service Cloud Voice REST API, telephony/v1 API]
domain: integration
summary: >-
  The JWT-authorized REST API that a telephony system (Amazon Connect Lambda functions or a partner's platform) calls
  to create and update VoiceCall records, stream real-time transcripts and drive Omni-Channel routing for Salesforce Voice.
release: "Winter '27"
status: current
broader: [kt:salesforce-apis]
related: [kt:rest-api, kt:lightning-service-console]
relations:
  - {predicate: partOf, object: kt:salesforce-voice}
  - {predicate: dependsOn, object: kt:json-web-token}
  - {predicate: dependsOn, object: kt:certificate-and-key-management}
  - {predicate: consumedBy, object: kt:amazon-connect}
  - {predicate: integratesWith, object: kt:omni-channel}
  - {predicate: contrastsWith, object: kt:jwt-bearer-flow}
sources:
  - id: s1
    title: "Using the Telephony Integration API (Salesforce Voice with Telephony Providers Implementation Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_rest_overview.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s2
    title: "Telephony Integration REST API Authorization"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/service/voice-dev-guide/guide/voice-rest-authorization.html
    type: official-docs
    accessed: 2026-11-24
  - id: s3
    title: "Create a Voice Call Record"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/service/voice-dev-guide/guide/voice-rest-voicecalls-create.html
    type: official-docs
    accessed: 2026-11-24
  - id: s4
    title: "Update a Voice Call Record"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/service/voice-dev-guide/guide/voice-rest-voicecalls-update.html
    type: official-docs
    accessed: 2026-11-24
  - id: s5
    title: "Create a Transcript"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/service/voice-dev-guide/guide/voice-rest-voicecalls-transcript.html
    type: official-docs
    accessed: 2026-11-24
  - id: s6
    title: "Integrate Incoming Voice Call Creation (Salesforce Voice with Partner Telephony Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/service/voice-pt-dev-guide/guide/voice-pt-integrate-incoming-call-creation.html
    type: official-docs
    accessed: 2026-11-24
created: 2026-11-24
---

# Telephony Integration API

The Telephony Integration API (also documented as the Telephony Integration REST API) is the server-to-server interface that a telephony system uses to manage voice calls in Salesforce Voice. The Amazon Connect Lambda functions that Salesforce provides call its endpoints automatically, but the same endpoints can be called directly, outside those functions.[^s1] Partner telephony providers use it for inbound calls: when their system receives a call and gets ready to route it to a rep, it calls the API to create the VoiceCall record.[^s6]

## Resources

All resources sit under `https://{MyDomain}.my.salesforce-scrt.com/telephony/v1`, a host separate from the org's normal `my.salesforce.com` API host.[^s3][^s6] The overview lists these operations:[^s1]

- **Create / update a voice call**: `POST /voiceCalls` creates a VoiceCall with its participants; `PATCH /voiceCalls/{CALL ID}` updates it.[^s3][^s4]
- **Transcripts**: create a single real-time transcript, or create transcripts in bulk.[^s1]
- **Routing**: execute an Omni-Channel flow, route or reroute a call, request a callback, reserve a routable number, and clear routing.[^s1]
- **Conversation events and context**: send a real-time conversation event, store a post-call event, and create voice call context for a hand-off to Agentforce Voice.[^s1]

## How requests are authorized

There is no OAuth token endpoint. The caller signs its own JSON Web Token and sends it as `Authorization: Bearer <token>`.[^s2] Contact center setup generates an RSA key pair: the public key is stored on the Salesforce CallCenter record, and for Amazon Connect the private key is kept in AWS (Parameter Store, moving to Secrets Manager from Winter '26).[^s2] Partners instead upload a certificate and keep the private key on their side.[^s6]

The JWT header uses `RS256`. The claims carry `iss` (the org ID), `sub` (the call center API name), `iat`, an `exp` no more than 24 hours out, and an optional `jti` that Salesforce checks for reuse to block replays.[^s2] Keys can be 2048 or 4096 bits; Salesforce recommends 2048.[^s2]

## Call lifecycle

A create request names the call center, the telephony system's own `vendorCallKey`, `to`, `from`, `startTime` and an `END_USER` participant. `initiationMethod` is `Inbound` or `Transfer`; the page states that outbound calls aren't supported through this endpoint.[^s3] Custom VoiceCall fields can be filled through a `callAttributes` JSON string, which partners use to carry IVR data into the record.[^s3][^s6] The response returns the new `voiceCallId` plus an `errors` array, so a record can be created even when some attributes fail.[^s3]

During the call, each utterance is posted to `/voiceCalls/{vendorCallKey}/messages`. The body carries a unique `messageId`, millisecond timestamps, the text and a `senderType` such as `END_USER`, `HUMAN_AGENT` or `VIRTUAL_AGENT`.[^s5] The transcript reaches the rep's console synchronously and is saved asynchronously.[^s5] When the call ends, a PATCH records hold counts, durations, queue, rep, recording location and a disconnect reason. Setting `isActiveCall` to false closes the conversation.[^s4]

## Limits and gotchas

- Call the create endpoint only in real time, when the call starts. Don't use it to back-fill historical calls.[^s3]
- The update is asynchronous and returns `{"status": "pending"}`; its outcome can't be polled.[^s4]
- Send the update only once. A repeat overwrites hold and interaction durations.[^s4]
- Recording fields are written as a separate VoiceCallRecording update; Apex triggers fire on the second, non-recording update.[^s4]
- Transcripts are kept only if their timestamps fall between the call's start and end. Utterances sent while the rep has paused recording or put the participant on hold are dropped.[^s5]
- After a transfer, transcripts must use the `vendorCallKey` of the first VoiceCall, not a Salesforce record ID.[^s5]

## When to use it (and when not)

Use it when you build or extend the telephony side of Salesforce Voice: custom Amazon Connect Lambdas, a partner connector, or IVR data passed into VoiceCall.[^s1][^s6] For everyday CRM reads and writes on VoiceCall or related records, use the standard platform APIs with OAuth instead; this API is scoped to one contact center through its call-center JWT.[^s2]

## Connections

The API is **part of** `kt:salesforce-voice`, which describes it as a main customization surface, and sits under `kt:salesforce-apis` alongside `kt:rest-api`.[^s1] It **depends on** `kt:json-web-token` and `kt:certificate-and-key-management`, because every call carries an RS256 token signed with the contact center's private key.[^s2] It **contrasts with** `kt:jwt-bearer-flow`: both use signed JWTs, but here the token is sent straight to the API instead of being exchanged for an OAuth access token.[^s2] It is **consumed by** `kt:amazon-connect` through the provided Lambda functions.[^s1] It **integrates with** `kt:omni-channel` through its routing and flow resources, and its transcripts appear in `kt:lightning-service-console` as calls happen.[^s1][^s5]

## Sources

[^s1]: Salesforce Developers, "Using the Telephony Integration API". https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_rest_overview.htm (accessed 2026-11-24)
[^s2]: Salesforce Developers, "Telephony Integration REST API Authorization". https://developer.salesforce.com/docs/service/voice-dev-guide/guide/voice-rest-authorization.html (accessed 2026-11-24)
[^s3]: Salesforce Developers, "Create a Voice Call Record". https://developer.salesforce.com/docs/service/voice-dev-guide/guide/voice-rest-voicecalls-create.html (accessed 2026-11-24)
[^s4]: Salesforce Developers, "Update a Voice Call Record". https://developer.salesforce.com/docs/service/voice-dev-guide/guide/voice-rest-voicecalls-update.html (accessed 2026-11-24)
[^s5]: Salesforce Developers, "Create a Transcript". https://developer.salesforce.com/docs/service/voice-dev-guide/guide/voice-rest-voicecalls-transcript.html (accessed 2026-11-24)
[^s6]: Salesforce Developers, "Integrate Incoming Voice Call Creation". https://developer.salesforce.com/docs/service/voice-pt-dev-guide/guide/voice-pt-integrate-incoming-call-creation.html (accessed 2026-11-24)
