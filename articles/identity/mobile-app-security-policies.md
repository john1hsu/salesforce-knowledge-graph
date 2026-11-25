---
id: kt:mobile-app-security-policies
type: SecurityControl
title: Mobile App Security Policies
aliases: [Enhanced Mobile App Security, Enhanced Mobile Security, MobileSecurityPolicy, mobile security policies, Mobile Security policies]
domain: identity
summary: >-
  Device- and app-level policies that protect Salesforce data on phones: Enhanced Mobile App Security policies
  (MobileSecurityPolicy) that check conditions such as jailbreak, OS version or device passcode and respond by
  severity, plus the screen-lock, passcode and biometric settings that connected or external client apps apply to
  Mobile SDK apps.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:salesforce-mobile-app, kt:mobile-sdk, kt:connected-apps, kt:external-client-apps, kt:session-settings, kt:transaction-security-policies]
relations:
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: integratesWith, object: kt:event-monitoring}
  - {predicate: mitigates, object: kt:data-breach-risk}
  - {predicate: contrastsWith, object: kt:transaction-security-policies}
sources:
  - id: s1
    title: "MobileSecurityPolicy (Metadata API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_mobilesecuritypolicy.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s2
    title: "MobileEnforcedPolicyEvent (Platform Events Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_mobileenforcedpolicyevent.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s3
    title: "Using Passcodes (Mobile SDK Development Guide, Native Android)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/mobile-sdk/guide/android-passcodes.html
    type: official-docs
    accessed: 2026-11-25
  - id: s4
    title: "About Login and Passcodes (Mobile SDK Development Guide, Native iOS)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/mobile-sdk/guide/ios-native-login-passcodes.html
    type: official-docs
    accessed: 2026-11-25
  - id: s5
    title: "Biometric Authentication (Mobile SDK Development Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/mobile-sdk/guide/biometric-auth.html
    type: official-docs
    accessed: 2026-11-25
  - id: s6
    title: "Explore Security and Authentication (Mobile SDK Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/mobile_sdk_introduction/mobilesdk_intro_security
    type: official-learning
    accessed: 2026-11-25
created: 2026-11-25
---

# Mobile App Security Policies

Mobile app security policies are the controls Salesforce offers for protecting org data once it reaches a phone. They come in two layers. The first is **Enhanced Mobile App Security**, a paid add-on whose policies are stored as `MobileSecurityPolicy` records and evaluated by the Salesforce mobile app on Android and iOS; each policy checks a device or app condition and reacts according to a severity level.[^s1] The second layer is the app-lock behavior that a connected app or external client app imposes on Mobile SDK apps: a passcode or biometric challenge after the app has been in the background, configured by the admin and enforced by the SDK.[^s3][^s6]

## How Enhanced Mobile App Security works

Using these policies requires the Enhanced Mobile App Security add-on subscription, and affected users need the Enforce Enhanced Mobile App Security user permission.[^s1] The `MobileSecurityPolicy` metadata type has been available since API version 53.0, so policies can be retrieved and deployed like other metadata rather than rebuilt by hand in each org.[^s1]

Each policy combines a `type`, a `ruleValue` with its `ruleValueType` (Boolean, Text or TextList), a `mobilePlatform` (Android or iOS), an `isEnabled` flag that defaults to false, an optional `effectiveDate`, and a required `severityLevel`.[^s1] The policy types cover device posture and app behavior, for example jailbroken or rooted devices, a required device passcode, minimum OS, app and security-patch versions, malware detection, an allowed-device list, blocking the camera or screenshots, a maximum offline period, and logging the user out after a restart or a biometric change.[^s1]

Severity decides what happens on a violation. Critical wipes the app's data and logs the user out; Error blocks access until the user fixes the issue without logging them out; Info blocks only the prohibited action, or logs it and tells the user; Warn shows a notice and lets the user carry on.[^s1]

## Monitoring enforcement

When the app enforces a policy it records a `MobileEnforcedPolicyEvent`. Events are created on first launch and whenever the user rechecks, then batched and published when the app goes to the background; the event has been available since API version 47.0.[^s2] Reading it needs both the Enhanced Mobile App Security and Event Monitoring add-ons plus the same user permission, and it can be subscribed to from Apex triggers, flows, Pub/Sub API or Streaming API on the `/event/MobileEnforcedPolicyEvent` channel.[^s2] Fields include the device model and identifier, OS name and version, app version, the enforced action and JSON policy results, which makes the event a feed for security alerting or reporting on non-compliant devices.[^s2]

## App lock in Mobile SDK apps

For custom apps built on the Mobile SDK, the developer enables a screen lock when creating the external client app, and the admin can then tune the timeout; the app locks after sitting in the background for that period and unlocks through the operating system's biometric or passcode challenge.[^s6] Since Mobile SDK 9.2 the SDK relies on the device's system passcode, so org-level settings such as PIN length and the app's biometric settings are ignored.[^s3][^s4] The Lock App After timeout was ignored in 9.2 and is honored again from 10.1.1, with the lock applied when the app is reactivated.[^s3][^s4] On iOS, Touch ID and Face ID verify the passcode by default, and the app must declare the Face ID usage description key.[^s4]

Mobile SDK 11.0 added biometric authentication as a separate option: when the background timeout passes, the app shows its login screen and the user can return with a password or, if they opted in, device biometrics.[^s5] It is enabled with the `ENABLE_BIOMETRIC_AUTHENTICATION` custom attribute on the connected app, and `BIOMETRIC_AUTHENTICATION_TIMEOUT` sets the minutes before the lock, defaulting to 15 when omitted.[^s5]

## Limits and gotchas

- Enhanced Mobile App Security policies apply to the Salesforce mobile app and need a paid add-on; monitoring events need Event Monitoring on top.[^s1][^s2]
- The Critical severity wipes app data, so test a policy as Warn first and use `effectiveDate` to give users time to comply.[^s1]
- Biometric lock does not refresh the access token while locked; Salesforce advises matching the session timeout and Lock App After values.[^s5]
- Older admin guidance about PIN length no longer applies to Mobile SDK 9.2+ apps, which defer to the device passcode.[^s3]

## When to use it

Use Enhanced Mobile App Security when users carry regulated data on personal or unmanaged devices and the org needs device-posture checks without a full mobile device management rollout.[^s1] For custom Mobile SDK apps, the screen-lock and biometric settings are the built-in baseline and cost nothing extra.[^s5][^s6]

## Connections

These policies sit under **Salesforce Identity** as a device-side complement to session and login controls in **session settings**.[^s5] They protect the **Salesforce mobile app**, while the app-lock settings live on **connected apps** and **external client apps** used by **Mobile SDK** apps.[^s3][^s6] Policies are deployable through **Metadata API** and their enforcement is visible through **Event Monitoring**, mitigating **data breach risk** from lost or compromised devices.[^s1][^s2] They contrast with **transaction security policies**, which react to user activity events in the org rather than to the state of the device.[^s2]

## Sources
[^s1]: Salesforce Developers, "MobileSecurityPolicy" (Metadata API Developer Guide). https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_mobilesecuritypolicy.htm (accessed 2026-11-25)
[^s2]: Salesforce Developers, "MobileEnforcedPolicyEvent" (Platform Events Developer Guide). https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_mobileenforcedpolicyevent.htm (accessed 2026-11-25)
[^s3]: Salesforce Developers, "Using Passcodes" (Mobile SDK Development Guide). https://developer.salesforce.com/docs/platform/mobile-sdk/guide/android-passcodes.html (accessed 2026-11-25)
[^s4]: Salesforce Developers, "About Login and Passcodes" (Mobile SDK Development Guide). https://developer.salesforce.com/docs/platform/mobile-sdk/guide/ios-native-login-passcodes.html (accessed 2026-11-25)
[^s5]: Salesforce Developers, "Biometric Authentication" (Mobile SDK Development Guide). https://developer.salesforce.com/docs/platform/mobile-sdk/guide/biometric-auth.html (accessed 2026-11-25)
[^s6]: Trailhead, "Explore Security and Authentication" (Mobile SDK Basics). https://trailhead.salesforce.com/mobile_sdk_introduction/mobilesdk_intro_security (accessed 2026-11-25)
