---
id: kt:my-domain
type: Feature
title: My Domain
aliases: [My Domain name, org subdomain, enhanced domains, MyDomainName.my.salesforce.com]
domain: identity
summary: >-
  The org-specific subdomain (for example yourname.my.salesforce.com) that Salesforce uses for login and application
  URLs; with enhanced domains it is carried into every org URL, and it is a prerequisite for SSO, social login and a
  branded login page.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:single-sign-on-saml, kt:multi-factor-authentication, kt:experience-cloud, kt:hyperforce, kt:sandbox-types, kt:scratch-orgs]
relations:
  - {predicate: enables, object: kt:single-sign-on-saml}
  - {predicate: enables, object: kt:openid-connect-authentication-providers}
  - {predicate: contrastsWith, object: kt:custom-domains}
  - {predicate: coveredBy, object: kt:identity-and-access-management-architect-certification}
sources:
  - id: s1
    title: "Set Up Your Salesforce My Domain (Identity Basics: Customize Your Login Process)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/identity_login/identity_login_my_domain
    type: official-learning
    accessed: 2026-11-02
  - id: s2
    title: "Enhanced Domains"
    publisher: Salesforce Developers (Identity Implementation Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_enhanced.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s3
    title: "Change Your My Domain Details"
    publisher: Salesforce Developers (Identity Implementation Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_rename.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s4
    title: "What Determines Your URL Formats?"
    publisher: Salesforce Developers (Identity Implementation Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_url_formats_what_determines.htm
    type: official-docs
    accessed: 2026-11-02
  - id: s5
    title: "Brand Your Salesforce Org's Domains"
    publisher: Salesforce Developers (Identity Implementation Guide)
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_brand_your_org.htm
    type: official-docs
    accessed: 2026-11-02
created: 2026-11-02
---

# My Domain

My Domain is the Salesforce Identity feature that gives each org its own subdomain inside the Salesforce domain, so users sign in at a URL such as `yourname.my.salesforce.com` rather than at an instance-specific host like `na30.salesforce.com`. Every org now has one: production orgs created in Winter '21 or later get a My Domain by default, and an org that never chose a name receives one derived from its org ID, which admins can later change.[^s1][^s4] It is configured from Setup by searching for "My Domain".[^s1]

## Why it matters

Trailhead lists four capabilities that depend on a My Domain: working in several orgs in one browser, single sign-on with third-party identity providers, authentication providers for social login such as Google or Facebook, and a login page customised with company branding.[^s1] The branding options include a logo (JPG, GIF or PNG, at most 100 KB and 250 × 125 pixels), a background colour, and a right-hand frame for announcements, which must be served over HTTPS in production.[^s1] Login policies on the same page can force users, and separately SOAP API clients, to authenticate through the My Domain URL; with Event Monitoring an org can also log redirections from previous hostnames to find stale references.[^s1]

## Enhanced domains and URL formats

Enhanced domains are a My Domain configuration that places the My Domain name in every URL the org serves, including Experience Cloud sites, Salesforce Sites, Visualforce pages and content files. Because these URLs carry no instance name, they stay stable when Salesforce moves the org to another instance, and they satisfy current browser requirements; the guide states they have been required since Summer '22.[^s2] With enhanced domains the main formats are:[^s2]

| Surface | Format |
|---|---|
| Login | `MyDomainName.my.salesforce.com` |
| Experience Cloud sites | `MyDomainName.my.site.com` |
| Salesforce Sites | `MyDomainName.my.salesforce-sites.com` |
| Visualforce | `MyDomainName--PackageName.vf.force.com` |
| Sandbox login | `MyDomainName--SandboxName.sandbox.my.salesforce.com` [^s2] |

Sandbox hostnames include the word "sandbox", which makes non-production environments easy to recognise.[^s4] Without enhanced domains, a separate "stabilize URLs" setting decides whether instance names appear in Visualforce, Experience Builder, Site.com and content file URLs.[^s4] The enhanced domains page lists availability in Hyperforce orgs and orgs routed through the Salesforce Edge Network, but notes it is not available in Developer Edition orgs or scratch orgs.[^s2]

## Renaming: process and gotchas

Admins can change the name, the suffix where several are offered, and the enhanced-domains choice. Names must be 3–34 characters in production and sandboxes (3–27 in Developer Edition), using letters, numbers and hyphens, and cannot begin with a hyphen. Editing requires Customize Application, and setting a name also needs Modify All Data.[^s3] A rename is a two-stage change: Salesforce first provisions the new domain, usually in minutes but sometimes up to 24 hours, and nothing changes for users until an admin deploys it.[^s3]

After deployment the old hostname redirects to the new one, but only the most recent previous name is redirected, so successive renames break older links; removing an old domain stops its redirect and frees it for use in another org.[^s3] Deployment briefly interrupts users, so Salesforce advises testing in a sandbox, deploying off-hours and announcing the change. Renaming after Service Cloud Voice is enabled breaks its Amazon Connect SSO setup and disables Voice.[^s3] In practice, hard-coded URLs in integrations, identity-provider metadata and bookmarks also need review, which the redirection log helps with.[^s1]

## My Domain vs. custom domains

My Domain covers login and application URLs and, with enhanced domains, also supplies the subdomain for Sites and Experience Cloud sites. A custom domain is a different mechanism: it serves Sites and Experience Cloud content from a domain the company owns, such as `example.com`, which suits multi-brand companies.[^s5] Without enhanced domains, each site needed its own registered subdomain that could not be changed after saving, which is one reason enhanced domains simplify branding.[^s5]

## Connections

My Domain is a building block of **Salesforce Identity**. It **enables SAML single sign-on** and social sign-on through **OpenID Connect authentication providers**, and login-policy enforcement on it complements **multi-factor authentication**.[^s1] Its enhanced-domain URL formats shape **Experience Cloud** site addresses and **sandbox** hostnames, and instance-free URLs matter when orgs move to **Hyperforce**; enhanced domains are not available in **scratch orgs**.[^s2][^s4] It **contrasts with custom domains**, which brand public site content rather than the org's login host.[^s5] The topic is examined in the **Identity and Access Management Architect** certification.

## Sources

[^s1]: Trailhead, "Set Up Your Salesforce My Domain" (Identity Basics). https://trailhead.salesforce.com/content/learn/modules/identity_login/identity_login_my_domain (accessed 2026-11-02)
[^s2]: Salesforce Developers, "Enhanced Domains". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_enhanced.htm (accessed 2026-11-02)
[^s3]: Salesforce Developers, "Change Your My Domain Details". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_rename.htm (accessed 2026-11-02)
[^s4]: Salesforce Developers, "What Determines Your URL Formats?". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_url_formats_what_determines.htm (accessed 2026-11-02)
[^s5]: Salesforce Developers, "Brand Your Salesforce Org's Domains". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/domain_name_brand_your_org.htm (accessed 2026-11-02)
