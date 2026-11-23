---
id: kt:salesforce-voice
type: Product
title: Salesforce Voice
aliases: [Service Cloud Voice, SCV, Salesforce Voice with Telephony Providers, Partner Contact Center, Salesforce Voice with Amazon Connect]
domain: clouds-and-products
summary: >-
  Salesforce's add-on that brings phone calls into the Salesforce console: calls are created as VoiceCall records,
  routed by Omni-Channel and optionally transcribed in real time, with telephony from Amazon Connect or a partner provider.
release: "Winter '27"
status: current
broader: [kt:service-cloud]
related: [kt:agentexchange, kt:government-cloud, kt:lightning-service-console]
relations:
  - {predicate: partOf, object: kt:service-cloud}
  - {predicate: dependsOn, object: kt:omni-channel}
  - {predicate: integratesWith, object: kt:amazon-connect}
  - {predicate: configuredVia, object: kt:telephony-integration-api}
sources:
  - id: s1
    title: "Salesforce Voice with Telephony Providers Implementation Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_intro.htm
    type: official-docs
    accessed: 2026-11-23
  - id: s2
    title: "Prepare Your Team for Effective Voice Implementation (Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/service-cloud-voice/service-voice-prepare
    type: official-learning
    accessed: 2026-11-23
  - id: s3
    title: "Salesforce Voice with Partner Telephony Developer Guide: Transfer Calls"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.voice_pt_developer_guide.meta/voice_pt_developer_guide/voice_pt_transfer_calls.htm
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "Salesforce Voice Best Practices for Error Handling"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_limits_scaling_error_handling.htm
    type: official-docs
    accessed: 2026-11-23
  - id: s5
    title: "Salesforce Voice Limits per Salesforce Org"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_limits_scaling_org_limits.htm
    type: official-docs
    accessed: 2026-11-23
  - id: s6
    title: "Integrating Amazon Connect Natively into Salesforce Using Service Cloud Voice"
    publisher: AWS Partner Network (APN) Blog
    url: https://aws.amazon.com/blogs/apn/integrating-amazon-connect-natively-into-salesforce-using-service-cloud-voice
    type: partner
    accessed: 2026-11-23
created: 2026-11-23
---

# Salesforce Voice

Salesforce Voice is the product formerly called **Service Cloud Voice**. It connects a contact-center telephony system to Salesforce so that reps take calls in the same console where they work cases. Salesforce's developer documentation now uses the umbrella name *Salesforce Voice with Telephony Providers*. It names two Amazon variants: *Salesforce Voice with Amazon Connect* and *Salesforce Voice for Partner Telephony with Amazon Connect*.[^s1] Newer Trailhead material describes the same offering under the label **Partner Contact Center**, so expect both names in current docs.[^s2] It is sold as an add-on license for Sales Cloud, Service Cloud and Government Cloud. It runs in Lightning Experience on Performance, Enterprise, Unlimited and Developer Editions.[^s3]

## Telephony options

There are several ways to supply the telephony:

- **With Amazon Connect**: Amazon Connect is natively integrated, billed together with Salesforce, and includes real-time transcription and call recording.[^s2]
- **With telephony from Amazon Connect**: connects an Amazon Connect instance the customer already runs.[^s2]
- **With partner telephony**: choose a supported telephony system and install the partner's prebuilt managed package from AgentExchange.[^s2]
- **Bring your own telephony**: keep a current provider's system and connect it to Voice.[^s2]

Telephony providers build the connector and package for the partner model, using the Partner Telephony developer guide.[^s3] Messaging from a contact-center-as-a-service (CCaaS) vendor is covered by a separate guide, Bring Your Own Channel.[^s3] Real-time transcription depends on the provider, so partner telephony may not offer it.[^s2]

## How it works

Each call is stored in Salesforce as a **VoiceCall** record.[^s6] In the Amazon Connect model, an inbound call first reaches an Amazon Connect contact flow. The flow greets the caller and looks up the customer by phone number. A Lambda function then calls the Telephony Integration API to create the VoiceCall record, and the call is routed to a rep through Omni-Channel.[^s6] Amazon Connect Contact Lens streams transcript segments to Salesforce during the call. When the call ends, contact trace record data is copied into the VoiceCall record.[^s6] Reps sign in to Amazon Connect through SAML single sign-on, which starts when they set themselves to Available in Omni-Channel.[^s6] The AWS account can be one that Salesforce provisions or one the customer owns ("bring your own Amazon"). A customer-owned account allows extra AWS services.[^s6]

Reps accept calls in the Omni-Channel widget, not in the older Salesforce Call Center softphone. Queue-based and skills-based routing work as they do for other channels. Supervisors monitor live work in Omni Supervisor. Contact-center dashboards report call volume, average handle time, average speed to answer and resolution rate.[^s2] Admins and developers customize an implementation through Amazon Connect flows, Lambda functions, the Telephony Integration REST API, the Connect API and the Voice Toolkit API.[^s1]

## Limits and gotchas

- Voice enforces limits for each org. The developer guide points to the Help article "Salesforce Voice Limits and Limitations" for the actual values, so confirm them for your org rather than assuming.[^s5]
- If the org goes over its transcription limit, new utterances are no longer transcribed. Track this with a custom field on VoiceCall.[^s4]
- If the org goes over its concurrent-call or calls-per-second limit, VoiceCall records cannot be created. Check the output of the InvokeTelephonyIntegrationApi Lambda function to spot this.[^s4]
- Government Cloud supports only the Amazon Connect and partner-telephony variants.[^s3]

## When to use it (and when not)

Choose Voice when phone calls should be first-class work items. That means routing them alongside cases and messaging by capacity and skill, recording and transcribing them, and reporting on them in Salesforce.[^s2] Use Amazon Connect when you want one bill and built-in transcription. Use partner telephony or bring your own telephony when you have to keep an existing provider.[^s2]

## Connections

Salesforce Voice is **part of** `kt:service-cloud`, sold as an add-on to it, and is **related** to `kt:lightning-service-console`, the rep workspace that service teams use for cases and calls alike.[^s3][^s2] It **depends on** `kt:omni-channel` for call routing, rep presence and supervision.[^s2] It **integrates with** `kt:amazon-connect`, its native telephony option.[^s1][^s6] It is **configured via** `kt:telephony-integration-api`, which creates and updates VoiceCall records.[^s1][^s6] It is **related** to `kt:agentexchange`, where partner telephony packages are listed, and to `kt:government-cloud`, where it is available with some restrictions.[^s2][^s3]

## Sources

[^s1]: Salesforce Developers, "Salesforce Voice with Telephony Providers Implementation Guide". https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_intro.htm (accessed 2026-11-23)
[^s2]: Trailhead, "Prepare Your Team for Effective Voice Implementation". https://trailhead.salesforce.com/content/learn/modules/service-cloud-voice/service-voice-prepare (accessed 2026-11-23)
[^s3]: Salesforce Developers, "Salesforce Voice with Partner Telephony Developer Guide: Transfer Calls". https://developer.salesforce.com/docs/atlas.en-us.voice_pt_developer_guide.meta/voice_pt_developer_guide/voice_pt_transfer_calls.htm (accessed 2026-11-23)
[^s4]: Salesforce Developers, "Salesforce Voice Best Practices for Error Handling". https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_limits_scaling_error_handling.htm (accessed 2026-11-23)
[^s5]: Salesforce Developers, "Salesforce Voice Limits per Salesforce Org". https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_limits_scaling_org_limits.htm (accessed 2026-11-23)
[^s6]: AWS Partner Network (APN) Blog, "Integrating Amazon Connect Natively into Salesforce Using Service Cloud Voice". https://aws.amazon.com/blogs/apn/integrating-amazon-connect-natively-into-salesforce-using-service-cloud-voice (accessed 2026-11-23)
