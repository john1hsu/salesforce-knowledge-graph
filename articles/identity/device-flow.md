---
id: kt:device-flow
type: Feature
title: OAuth 2.0 Device Flow
aliases: [device flow, device authorization grant, device code flow, OAuth 2.0 Device Flow for IoT Integration, RFC 8628 device grant]
domain: identity
summary: >-
  Salesforce's OAuth flow for input-constrained clients such as smart TVs, appliances, IoT devices and command-line
  tools: the client gets a device code and a short user code, the user approves on a separate browser, and the client
  polls the token endpoint until Salesforce issues an access token.
release: "Winter '27"
status: current
broader: [kt:oauth-2-flows-in-salesforce]
related: [kt:account-takeover, kt:data-loader, kt:api-access-control]
relations:
  - {predicate: implements, object: kt:oauth-2-0}
  - {predicate: configuredVia, object: kt:external-client-apps}
  - {predicate: configuredVia, object: kt:connected-apps}
  - {predicate: consumedBy, object: kt:salesforce-cli}
  - {predicate: alternativeTo, object: kt:web-server-flow}
  - {predicate: alternativeTo, object: kt:jwt-bearer-flow}
sources:
  - id: s1
    title: "RFC 8628: OAuth 2.0 Device Authorization Grant"
    publisher: IETF
    url: https://rfc-editor.org/rfc/rfc8628
    type: standards-body
    accessed: 2026-11-15
  - id: s2
    title: "Configure an OAuth 2.0 Device Flow for External Client Apps"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.meta_configure_device_flow_external_client_apps.htm&type=5
    type: official-docs
    accessed: 2026-11-15
  - id: s3
    title: "Configure a Device Flow"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.configure_device_flow_external_client_apps.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "device Commands (Deprecated) — Salesforce CLI Command Reference"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.248.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_auth_device.htm
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "Get Ready for Changes to Connected App Usage Restrictions"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2025/get-ready-for-changes-to-connected-app-usage-restrictions
    type: official-blog
    accessed: 2026-11-15
  - id: s6
    title: "Salesforce Hardens Connected Apps Security Amid Social Engineering Attacks"
    publisher: Salesforce Ben
    url: https://www.salesforceben.com/salesforce-hardens-connected-apps-security-amid-social-engineering-attacks/
    type: news
    accessed: 2026-11-15
created: 2026-11-15
---

# OAuth 2.0 Device Flow

The **device flow** is the OAuth flow Salesforce offers for clients that have limited input or display capabilities, such as smart TVs, appliances and IoT hardware, and it is also usable by command-line applications.[^s2] Instead of typing credentials into the device, the user reads a short code from it, opens a verification page on a phone or computer, enters the code and approves the connection; meanwhile the device waits and then collects an access token.[^s2] It is one of the OAuth 2.0 flows in Salesforce described in the umbrella article; this node covers the standard, the Salesforce-specific request shape and the security story that has made it a flow to use sparingly.

## The standard underneath

The IETF published the device authorization grant as RFC 8628 in August 2019, aimed at internet-connected devices without a suitable browser or keyboard, with the user authorizing on a second device.[^s1] The client POSTs its `client_id` (and optionally a scope) to a device authorization endpoint and gets back a `device_code`, a `user_code`, a `verification_uri`, an optional `verification_uri_complete` for QR codes, an `expires_in` lifetime and an optional polling `interval` that defaults to 5 seconds.[^s1] The client then polls the token endpoint; `authorization_pending` means keep waiting, `slow_down` means add 5 seconds to the interval, and `access_denied` or `expired_token` mean stop.[^s1]

## How it works in Salesforce

Salesforce runs both legs against the same endpoint, `/services/oauth2/token` on the org URL, and uses its own parameter values rather than the RFC's.[^s2]

1. **Get a device code.** POST with `response_type=device_code`, the `client_id` and a `redirect_uri`; the response carries a verification URL, a user code and a device code.[^s2]
2. **User approves.** The user opens the verification URL on a computer or mobile device and enters the user code.[^s2]
3. **Get the token.** The device POSTs with `grant_type=device`, the `client_id` and `code` set to the device code, and receives a bearer access token once approval is done.[^s2]

Note that Salesforce's grant type is the short value `device`, not the RFC's `urn:ietf:params:oauth:grant-type:device_code` URN, so generic RFC 8628 libraries may need adjusting.[^s1][^s2]

Setup is a single switch on the client app. For an external client app, an admin opens the External Client App Manager, edits the app's settings, enables OAuth with its basic settings and selects **Enable Device Flow**; doing so needs the permission to view all external client apps and edit their policies.[^s3] In source-driven setups the same switch is the `isDeviceFlowEnabled` field set to `true` in the app's global OAuth settings file.[^s2]

## Security and the 2025 restrictions

The flow's convenience is also its weakness. RFC 8628 warns of remote phishing, where an attacker gets a victim to enter a code that actually authorizes the attacker's device, and advises servers to show device details and ask for confirmation; it also calls for rate limiting because short user codes have low entropy.[^s1] In 2025 attackers used voice-phishing calls to talk Salesforce users into installing a malicious replica of Data Loader, and press coverage noted the device flow can be started with only a client ID, which makes such lures easier.[^s6]

Salesforce responded with connected app usage restrictions that began in early September 2025: previously authorized users keep using uninstalled apps only when those apps do not rely on the device flow.[^s5] Uninstalled apps that use the device flow were therefore blocked at once, even for users who had authorized them earlier, while installed apps kept working.[^s6] Authorizing uninstalled apps now requires the **Approve Uninstalled Connected Apps** or the broader **Use Any API Client** permission, which Salesforce says to grant sparingly.[^s5]

## Use in the Salesforce CLI

The CLI exposes the flow as `sf org login device`, which replaced the older `sfdx auth:device:login`; you open the verification URL, enter the code, log in if needed and allow the device to connect to the org.[^s4] Flag names changed in the move, for example `--clientid` to `--client-id` and `--instanceurl` to `--instance-url`.[^s4] Given the restrictions above, teams relying on device login should confirm the client app behind it is installed in the org or move to a browser-based or JWT-based login.[^s5][^s4]

## When to use it (and when not)

Use the device flow only when the client truly cannot host a browser login, such as a kiosk, a TV app or a headless terminal, and make sure its client app is installed and governed in the org.[^s2][^s5] Clients that can run a browser fall outside the grant's intended audience, so they should use an ordinary browser-based authorization-code login, and unattended automation is better served by a flow with no human approval step, such as the JWT bearer flow.[^s1]

## Connections

The device flow is one of the **OAuth 2.0 flows in Salesforce** and **implements** the **OAuth 2.0** device authorization grant from RFC 8628.[^s1][^s2] It is **configured via** an **external client app** or a **connected app**, and it is **consumed by** the **Salesforce CLI** through its device login command.[^s3][^s4] It is an **alternative to** the **web server flow** for user-present logins and to the **JWT bearer flow** for automation.[^s2] Its phishing exposure ties it to **account takeover**, to the **Data Loader** impersonation campaign, and to the usage restrictions that **API Access Control** tightens further.[^s1][^s6][^s5]

## Sources

[^s1]: IETF, "RFC 8628: OAuth 2.0 Device Authorization Grant". https://rfc-editor.org/rfc/rfc8628 (accessed 2026-11-15)
[^s2]: Salesforce Help, "Configure an OAuth 2.0 Device Flow for External Client Apps". https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.meta_configure_device_flow_external_client_apps.htm&type=5 (accessed 2026-11-15)
[^s3]: Salesforce Help, "Configure a Device Flow". https://help.salesforce.com/s/articleView?id=xcloud.configure_device_flow_external_client_apps.htm&language=en_US&type=5 (accessed 2026-11-15)
[^s4]: Salesforce Developers, "device Commands (Deprecated)". https://developer.salesforce.com/docs/atlas.en-us.248.0.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_auth_device.htm (accessed 2026-11-15)
[^s5]: Salesforce Admins Blog, "Get Ready for Changes to Connected App Usage Restrictions". https://admin.salesforce.com/blog/2025/get-ready-for-changes-to-connected-app-usage-restrictions (accessed 2026-11-15)
[^s6]: Salesforce Ben, "Salesforce Hardens Connected Apps Security Amid Social Engineering Attacks". https://www.salesforceben.com/salesforce-hardens-connected-apps-security-amid-social-engineering-attacks/ (accessed 2026-11-15)
