---
id: kt:amazon-connect
type: Product
title: Amazon Connect
aliases: [Amazon Connect Customer, Connect Customer, AWS contact center]
domain: integration
summary: >-
  AWS's pay-as-you-go cloud contact center service (now documented as Amazon Connect Customer), which supplies the
  telephony, flows, routing and call analytics behind Salesforce Voice's Amazon Connect variants.
release: "Winter '27"
status: current
broader: [kt:software-as-a-service]
related: [kt:omni-channel, kt:lightning-service-console, kt:aws-lambda]
relations:
  - {predicate: integratesWith, object: kt:salesforce-voice}
  - {predicate: integratesWith, object: kt:telephony-integration-api}
  - {predicate: dependsOn, object: kt:single-sign-on-saml}
sources:
  - id: s1
    title: "What is Connect Customer? (Amazon Connect Administrator Guide)"
    publisher: Amazon Web Services
    url: https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html
    type: partner
    accessed: 2026-11-24
  - id: s2
    title: "Connect Customer feature overview (Amazon Connect Administrator Guide)"
    publisher: Amazon Web Services
    url: https://docs.aws.amazon.com/connect/latest/adminguide/connect-feature-overview.html
    type: partner
    accessed: 2026-11-24
  - id: s3
    title: "Sample Flows for Amazon Connect (Salesforce Voice with Telephony Providers Implementation Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_contact_flows_sample_flows.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s4
    title: "Set Up Call Transcription (Salesforce Voice with Telephony Providers Implementation Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_example_set_up_transcription.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s5
    title: "Contact Record Sync with Amazon Connect (Salesforce Voice with Telephony Providers Implementation Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/service/voice-dev-guide/guide/voice-ctr-sync.html
    type: official-docs
    accessed: 2026-11-24
  - id: s6
    title: "Prepare for a Partner Contact Center (Trailhead: Partner Contact Center Setup: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/service-cloud-voice-setup-quick-look/prepare-for-a-voice-implementation
    type: official-learning
    accessed: 2026-11-24
created: 2026-11-24
---

# Amazon Connect

Amazon Connect is Amazon Web Services' contact-center-as-a-service offering. It lets a business build customer communication experiences, connect customers to agents, route contacts intelligently and watch performance in real time, and it is billed only for what is used.[^s1] AWS now documents the contact-center product as **Amazon Connect Customer** and uses "Amazon Connect" as the umbrella name for a wider set of agentic AI solutions, so Salesforce and AWS pages may use either name for the same service.[^s1] In the Salesforce ecosystem it matters mainly as the telephony engine behind the Amazon Connect variants of Salesforce Voice.[^s4]

## What the service provides

The AWS guide groups capabilities by persona. Customers can reach the business through voice, conversational IVR and chatbots, chat, SMS and messaging, in-app and web calling and video, email, outbound campaigns and voice authentication. Agents get a workspace with knowledge, agent assist and case management. Supervisors get real-time and historical reports, conversational analytics, quality management and workforce forecasting and scheduling. Administrators provision phone numbers, define queues and routing profiles, build flows and integrate other products through a self-service console and APIs.[^s1]

A single drag-and-drop designer builds flows for IVR and bot experiences, agent step-by-step guides and task automation. Flows call AWS Lambda natively, which is the usual route to databases or a third-party CRM.[^s2] Routing profiles send contacts to skilled agents, with priority driven by agent skills, queue priorities, contact attributes and real-time metrics.[^s2] Contact records, conversational analytics and evaluations land in a data lake that can be queried with SQL or BI tools, and Customer Profiles can merge contact history with data from CRMs such as Salesforce.[^s2]

## How it plugs into Salesforce

When a Salesforce Voice contact center is created with Amazon Connect, a set of sample flows named "Sample SCV …" is installed automatically. They cover inbound calls that create a VoiceCall record and hand off to Omni-Channel, direct-to-rep routing, outbound calls with transcription, several transfer types, callbacks, voicemail and case lookup through a REST-calling Lambda.[^s3] Teams customize these flows rather than starting from scratch; the JSON copies on GitHub are kept current with contact center releases.[^s3]

Real-time transcription in the VoiceCall record comes from either Amazon Transcribe or Contact Lens. Transcription through Amazon Transcribe covers only the first 15 minutes of a call because of a Lambda limitation, so Contact Lens is the choice for longer calls.[^s4] After each call, contact record sync (on by default) uses a Lambda function to copy Amazon Connect contact record data into the VoiceCall object; because sync can occasionally fail, Salesforce suggests backing contact records up to S3 and resyncing gaps.[^s5]

## Limits and gotchas

- AWS service quotas, not Salesforce, cap concurrent active calls, transcription jobs and the countries reachable by outbound calls; request increases before go-live.[^s6]
- Porting existing phone numbers to the telephony provider must be requested many weeks ahead, and AWS networking must not block the ports the service needs.[^s6]
- Amazon Transcribe and Contact Lens outbound transcription flows cannot be combined in one setup.[^s3]
- When a second rep joins a call, separate audio channels can cause duplicate transcripts or misattributed speech.[^s4]
- Call usage and minutes monitoring in the Voice analytics applies only to the Amazon Connect options.[^s6]

## When to use it (and when not)

Pick Amazon Connect when you want a cloud contact center whose transcription and analytics feed straight into Salesforce records, and when your team can own AWS-side configuration such as flows, Lambda functions and quotas.[^s6][^s3] If you must keep another telephony vendor, the partner-telephony and bring-your-own options of Salesforce Voice are the alternative, with transcription depending on that provider.[^s6]

## Connections

Amazon Connect is a `kt:software-as-a-service` offering billed on usage.[^s1] It **integrates with** `kt:salesforce-voice`, which offers it as the native telephony choice, and with `kt:telephony-integration-api`, which its Lambda functions call to create and update VoiceCall records.[^s3][^s5] Its flows hand calls to `kt:omni-channel` for routing to reps, who work them in `kt:lightning-service-console`.[^s3] It **depends on** `kt:single-sign-on-saml`, because reps need SSO with cookies enabled to sign in.[^s6] It is **related** to `kt:aws-lambda`, the serverless functions its flows use for every Salesforce call.[^s2][^s5]

## Sources

[^s1]: Amazon Web Services, "What is Connect Customer?". https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html (accessed 2026-11-24)
[^s2]: Amazon Web Services, "Connect Customer feature overview". https://docs.aws.amazon.com/connect/latest/adminguide/connect-feature-overview.html (accessed 2026-11-24)
[^s3]: Salesforce Developers, "Sample Flows for Amazon Connect". https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_contact_flows_sample_flows.htm (accessed 2026-11-24)
[^s4]: Salesforce Developers, "Set Up Call Transcription". https://developer.salesforce.com/docs/atlas.en-us.voice_developer_guide.meta/voice_developer_guide/voice_example_set_up_transcription.htm (accessed 2026-11-24)
[^s5]: Salesforce Developers, "Contact Record Sync with Amazon Connect". https://developer.salesforce.com/docs/service/voice-dev-guide/guide/voice-ctr-sync.html (accessed 2026-11-24)
[^s6]: Trailhead, "Prepare for a Partner Contact Center". https://trailhead.salesforce.com/content/learn/modules/service-cloud-voice-setup-quick-look/prepare-for-a-voice-implementation (accessed 2026-11-24)
