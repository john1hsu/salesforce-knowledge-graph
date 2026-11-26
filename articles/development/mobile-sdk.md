---
id: kt:mobile-sdk
type: Tool
title: Mobile SDK
aliases: [Salesforce Mobile SDK, forceios, forcedroid, forcehybrid, forcereact]
domain: development
summary: >-
  Salesforce's open-source toolkit for building standalone custom iOS and Android apps (native, hybrid or React
  Native) that log in to Salesforce with OAuth, call its APIs, and keep data offline in the encrypted SmartStore
  database synchronised through Mobile Sync.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:salesforce-mobile-app, kt:mobile-app-security-policies, kt:experience-cloud, kt:lightning-web-components, kt:smartstore, kt:mobile-sync]
relations:
  - {predicate: dependsOn, object: kt:external-client-apps}
  - {predicate: dependsOn, object: kt:oauth-2-flows-in-salesforce}
  - {predicate: queriedWith, object: kt:rest-api}
  - {predicate: alternativeTo, object: kt:salesforce-mobile-app}
  - {predicate: integratesWith, object: kt:headless-identity}
sources:
  - id: s1
    title: "About Native, HTML, and Hybrid Development"
    publisher: Salesforce Developers (Mobile SDK Development Guide)
    url: https://developer.salesforce.com/docs/platform/mobile-sdk/guide/intro-choose-scenario.html
    type: official-docs
    accessed: 2026-11-26
  - id: s2
    title: "About Salesforce Mobile Apps"
    publisher: Salesforce Developers (Mobile SDK Development Guide)
    url: https://developer.salesforce.com/docs/platform/mobile-sdk/guide/preface-arch.html
    type: official-docs
    accessed: 2026-11-26
  - id: s3
    title: "What's New in Mobile SDK 13.2"
    publisher: Salesforce Developers (Mobile SDK Development Guide)
    url: https://developer.salesforce.com/docs/platform/mobile-sdk/guide/gs-whatsnew.html
    type: official-docs
    accessed: 2026-11-26
  - id: s4
    title: "Supported Versions of Tools and Components for Mobile SDK 13.1"
    publisher: Salesforce Developers (Mobile SDK Development Guide)
    url: https://developer.salesforce.com/docs/platform/mobile-sdk/guide/reference-current-versions.html
    type: official-docs
    accessed: 2026-11-26
  - id: s5
    title: "What Was New in Recent Releases"
    publisher: Salesforce Developers (Mobile SDK Development Guide)
    url: https://developer.salesforce.com/docs/platform/mobile-sdk/guide/gs-whatswasnew.html
    type: official-docs
    accessed: 2026-11-26
  - id: s6
    title: "React Native Development"
    publisher: Salesforce Developers (Mobile SDK Development Guide)
    url: https://developer.salesforce.com/docs/platform/mobile-sdk/guide/react-native-intro.html
    type: official-docs
    accessed: 2026-11-26
  - id: s7
    title: "Hybrid Development: Get Started with Hybrid Development"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/mobile_sdk_hybrid/mobilesdk_hybrid_getting_started
    type: official-learning
    accessed: 2026-11-26
created: 2026-11-26
---

# Mobile SDK

Salesforce Mobile SDK is the toolkit for teams that need their own branded mobile app rather than the
off-the-shelf Salesforce mobile app. With it, developers build standalone iOS and Android apps for employees,
customers or partners and ship them through the App Store or Google Play, while Salesforce handles identity and
data access underneath.[^s2] The SDK bundles enterprise login and security (Salesforce login, connected-app policies,
SAML and advanced authentication), an AES-256 encrypted offline database called SmartStore, the Mobile Sync API that
keeps that local store in step with the org, and mobile services such as push notifications.[^s2]

## Development options

Mobile SDK supports four styles of app, all available on both iOS and Android.[^s1]

- **Native**: Swift or Objective-C in Xcode, Java or Kotlin in Android Studio; best performance and most control, highest skill bar.[^s1]
- **Hybrid**: HTML, JavaScript and CSS inside a native container built on Apache Cordova, distributed through the app stores.[^s7]
- **React Native**: JavaScript or TypeScript with natively rendered views and SDK bridges for login, REST, SmartStore and Mobile Sync.[^s1]
- **HTML**: a mobile web app that runs in any browser but lacks secure offline storage and has awkward login flows.[^s1]

Hybrid apps come in two flavours: *hybrid local*, where the web app is packaged on the device and uses the force.js
library, and *hybrid remote*, where Visualforce pages are served from Salesforce through the container.[^s7] The
guide notes that only hybrid apps can host Lightning web components.[^s1] React Native support dates from Mobile
SDK 4.0, and TypeScript became an option in 9.0; its appeal is checking code changes without recompiling and using
browser developer tools.[^s6] Projects are generated with the npm command-line tools forceios, forcedroid,
forcehybrid and forcereact.[^s4][^s6]

## How an app connects to Salesforce

Every Mobile SDK app needs a Salesforce external client app; developers copy its callback URL and consumer key into
the app's boot configuration, and the app never uses a consumer secret.[^s7] Since Mobile SDK 11.0 the default login
is the OAuth web server flow rather than the user-agent flow, and 11.0 also added biometric login.[^s5] Mobile SDK
12.0 introduced native login for Experience Cloud sites, including passwordless login, and 12.1 added native user
registration and password reset.[^s5] Version 13.2 added dynamic scope retrieval, runtime consumer-key selection and
refresh-token migration, including moving users from a connected app to an external client app; its 13.2.1 patch added
passkey and identity-verification support.[^s3]

## Versions, limits and gotchas

The guide current at this release documents Mobile SDK 13.2, and announces that 14.0, planned for 2026, will raise
the minimum Kotlin version from 1.6 to 2.0.[^s3] The supported-versions page for 13.1 lists these requirements:[^s4]

- **iOS**: Xcode 16, deployment target iOS 17, base SDK iOS 18; CocoaPods 1.8 or later.[^s4]
- **Android**: JDK 17, Gradle 8.14.3, Android Gradle Plugin 8.12.0, minimum API 28 (Android 9), target API 35 (Android 15).[^s4]
- **Cross-platform**: React Native 0.81.5 with React 19.1.0; Cordova command line 13.0.0; Node.js 20 to latest LTS.[^s3][^s4]

Major releases regularly break existing apps. Mobile SDK 10.0 deprecated SmartStore external storage and the SoupSpec class for
removal in 11.0; 12.2 changed the Android login activity launch mode, which affects apps that override
LoginActivity; and 13.0 deprecated completion-based REST methods on iOS in favour of async requests.[^s5] Since 9.2
the SDK no longer enforces app-specific passcode length or timeout from the connected app, though it still honours the
org's passcode requirement.[^s5] Trailhead hybrid material still shows old Cordova version strings, so check the
supported-versions page before copying commands.[^s7][^s4]

## When to use it (and when not)

The Salesforce mobile app is the fastest way to give employees mobile access, using point-and-click configuration and
Lightning web development; Mobile SDK is for when you need a custom user experience, your own store listing, or an app
for customers and partners.[^s2] Within the SDK, native gives the best look and speed, React Native comes close with a
JavaScript skill set, hybrid trades speed for web reuse, and plain HTML gives up secure offline storage.[^s1]

## Connections

Mobile SDK sits on the `kt:salesforce-platform` and is the custom-build **alternative** to the
`kt:salesforce-mobile-app`.[^s2] It **depends on** `kt:external-client-apps`, the successor to connected apps for new apps, and the
`kt:oauth-2-flows-in-salesforce` for login, and its device policies are covered in `kt:mobile-app-security-policies`.[^s7][^s5]
Data access runs through the `kt:rest-api` wrappers, offline storage through `kt:smartstore` and `kt:mobile-sync`, and
native Experience Cloud login links it to `kt:experience-cloud` and `kt:headless-identity`.[^s2][^s5] Hybrid apps can
embed `kt:lightning-web-components`.[^s1]

## Sources

[^s1]: Salesforce Developers, "About Native, HTML, and Hybrid Development", Mobile SDK Development Guide. https://developer.salesforce.com/docs/platform/mobile-sdk/guide/intro-choose-scenario.html (accessed 2026-11-26)
[^s2]: Salesforce Developers, "About Salesforce Mobile Apps", Mobile SDK Development Guide. https://developer.salesforce.com/docs/platform/mobile-sdk/guide/preface-arch.html (accessed 2026-11-26)
[^s3]: Salesforce Developers, "What's New in Mobile SDK 13.2", Mobile SDK Development Guide. https://developer.salesforce.com/docs/platform/mobile-sdk/guide/gs-whatsnew.html (accessed 2026-11-26)
[^s4]: Salesforce Developers, "Supported Versions of Tools and Components for Mobile SDK 13.1", Mobile SDK Development Guide. https://developer.salesforce.com/docs/platform/mobile-sdk/guide/reference-current-versions.html (accessed 2026-11-26)
[^s5]: Salesforce Developers, "What Was New in Recent Releases", Mobile SDK Development Guide. https://developer.salesforce.com/docs/platform/mobile-sdk/guide/gs-whatswasnew.html (accessed 2026-11-26)
[^s6]: Salesforce Developers, "React Native Development", Mobile SDK Development Guide. https://developer.salesforce.com/docs/platform/mobile-sdk/guide/react-native-intro.html (accessed 2026-11-26)
[^s7]: Trailhead, "Get Started with Hybrid Development" (Hybrid Development module). https://trailhead.salesforce.com/content/learn/modules/mobile_sdk_hybrid/mobilesdk_hybrid_getting_started (accessed 2026-11-26)
