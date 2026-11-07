---
id: kt:integration-security
type: Concept
title: Integration Security
aliases: [API security, securing Salesforce integrations, integration user security, system-to-system integration security]
domain: integration
summary: >-
  The set of practices and platform controls that protect system-to-system connections into and out of Salesforce:
  dedicated least-privilege API-only integration users, OAuth flows instead of stored passwords, allowlisted API
  clients, secrets held in named credentials, and monitoring of integration traffic.
release: "Winter '27"
status: concept
broader: [kt:integration-patterns]
related: [kt:oauth-2-flows-in-salesforce, kt:connected-apps, kt:external-client-apps, kt:event-monitoring, kt:transaction-security-policies]
relations:
  - {predicate: hasPart, object: kt:named-credentials}
  - {predicate: implements, object: kt:principle-of-least-privilege}
  - {predicate: dependsOn, object: kt:permission-sets}
  - {predicate: mitigates, object: kt:data-breach-risk}
  - {predicate: contrastsWith, object: kt:account-takeover}
  - {predicate: coveredBy, object: kt:integration-architect-certification}
sources:
  - id: s1
    title: "Identity and Access Management - Patterns (Salesforce Well-Architected)"
    publisher: Salesforce Architects
    url: https://architect.salesforce.com/docs/architect/well-architected/guide/trust-identity-access-patterns.html
    type: official-docs
    accessed: 2026-11-07
  - id: s2
    title: "Salesforce Integration User Licenses"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=platform.integration_user.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-07
  - id: s3
    title: "API Access Control"
    publisher: Salesforce Help
    url: https://help.salesforce.com/apex/HTViewHelpDoc?id=xcloud.security_api_access_control_about.htm
    type: official-docs
    accessed: 2026-11-07
  - id: s4
    title: "Best Practices for Configuring Your Integration User"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2023/best-practices-for-configuring-your-integration-user
    type: official-blog
    accessed: 2026-11-07
created: 2026-11-07
---

# Integration Security

Integration security is the discipline of protecting the non-human connections between Salesforce and other systems: middleware, data warehouses, vendor apps and custom services that call Salesforce APIs, and the callouts Salesforce makes outward. These accounts run unattended and often hold broad data access, so Salesforce's Well-Architected guidance treats integration and automation users as critical-impact accounts that belong in a tracked asset inventory and deserve strict least privilege.[^s1] The concern is not a single feature but a combination of identity, authorization, secrets management, network restriction and monitoring controls.

## How it works

**A dedicated integration user per integration.** The Well-Architected patterns call for one unique, API-only user for each integration, holding only the permissions it needs; a single shared API user with Modify All Data serving several integrations is listed as an anti-pattern.[^s1] Salesforce supplies a purpose-built *Salesforce Integration* user license for this. It provisions the *Minimum Access – API Only Integrations* profile and the *Salesforce API Integration* permission set license; users on it cannot reach the user interface, and the API-only setting cannot be turned off. The license is available in Enterprise, Unlimited, Performance and Developer editions, and it replaces the deprecated *Salesforce API Only System Integrations* profile.[^s2] Actual object and field access is then granted with permission sets or permission set groups.[^s2]

**Shaping that user's access.** A Salesforce Admins post recommends stripping the API-only profile down to defaults, login hours and IP ranges, cloning it per external application so each can carry its own login IP ranges and app access, and using muting in permission set groups to drop permissions an integration does not need.[^s4] It suggests setting Login IP Ranges to the provider's published egress ranges, so that stolen tokens are less useful from elsewhere, and building the permission set up from zero in a sandbox before production.[^s4] The same post noted that Enterprise, Unlimited and Performance orgs received five integration licenses at no cost and Developer Edition one; the current Help page says only that orgs get "a limited number" by default, so confirm the count in your org.[^s4][^s2]

**OAuth, not passwords.** Integrations should authenticate with OAuth flows rather than username-password. Well-Architected names the JWT bearer flow as the preferred choice for trusted server-to-server production integrations, the web server flow where user context is needed, and the device flow only for headless devices.[^s1] For REST access the Help page directs integration users to an external client app with an OAuth 2.0 flow; SOAP and Bulk API still use the `login()` call.[^s2] OAuth scopes broader than the integration needs are flagged as an anti-pattern.[^s1]

**Allowlisting API clients.** API Access Control, which an org requests from Salesforce Customer Support, blocks API access except through connected apps an admin has approved; profiles and permission sets then decide which users may use each approved app. It can apply to all users or only to customers and partners, and it is available in Professional, Enterprise, Performance, Unlimited and Developer editions.[^s3] Leaving it disabled is listed as a Well-Architected anti-pattern.[^s1]

**Secrets for outbound calls.** For callouts, named and external credentials centralize authentication so secrets never live in Apex, Aura, LWC, configuration files or version control, and they can be rotated on a schedule without code changes.[^s1]

## Limits and gotchas

- Integration users still pass through the data layer: Apex serving them should enforce CRUD and FLS with `WITH USER_MODE` or `Security.stripInaccessible()`; the older `WITH SECURITY_ENFORCED` clause is treated as deprecated.[^s1]
- API Access Control is not self-service and can block any existing integration whose connected app is not allowlisted, so inventory clients before requesting it.[^s3]
- Service-account passwords that never change, and accounts with no IP or login-hour limits, are explicit anti-patterns.[^s1]
- Granting View All Data or Modify All Data to an integration needs documented business justification.[^s1]

## When to use it

Apply these controls to every integration, but weight them by blast radius: a vendor app with read access to a few objects needs a narrow permission set and an IP range, while a middleware account that writes across the org also warrants Event Monitoring of its API usage and Transaction Security policies that detect bulk exports or logins from unexpected places.[^s1] When migrating an existing integration off an administrator account, the Admins post advises running the new user alongside the old one for one to two months before retiring the old access.[^s4]

## Connections

Integration security sits under **integration patterns**: every pattern (request-reply, fire-and-forget, batch sync) needs an authenticated, authorized channel.[^s1] **Named credentials** is its outbound secrets component, while **OAuth 2.0 flows**, **connected apps** and **external client apps** define how inbound clients obtain tokens.[^s1][^s2] Access is granted through **permission sets**, applying the **principle of least privilege**.[^s2][^s4] **Event Monitoring** and **Transaction Security policies** supply detection.[^s1] It contrasts with **account takeover**, which targets human logins, and its controls reduce **data breach risk**. The topic is examined in the **Integration Architect certification**.

## Sources
[^s1]: Salesforce Architects, "Identity and Access Management - Patterns (Salesforce Well-Architected)". https://architect.salesforce.com/docs/architect/well-architected/guide/trust-identity-access-patterns.html (accessed 2026-11-07)
[^s2]: Salesforce Help, "Salesforce Integration User Licenses". https://help.salesforce.com/s/articleView?id=platform.integration_user.htm&language=en_US&type=5 (accessed 2026-11-07)
[^s3]: Salesforce Help, "API Access Control". https://help.salesforce.com/apex/HTViewHelpDoc?id=xcloud.security_api_access_control_about.htm (accessed 2026-11-07)
[^s4]: Salesforce Admins, "Best Practices for Configuring Your Integration User". https://admin.salesforce.com/blog/2023/best-practices-for-configuring-your-integration-user (accessed 2026-11-07)
