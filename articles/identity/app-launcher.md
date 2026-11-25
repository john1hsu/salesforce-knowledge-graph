---
id: kt:app-launcher
type: Feature
title: App Launcher
aliases: [Salesforce App Launcher]
domain: identity
summary: >-
  The Salesforce menu that shows a user tiles for the standard, custom, connected (third-party) and on-premises apps
  they are authorised to use, plus every item they can reach; admins control which apps appear and in what order.
release: "Winter '27"
status: current
broader: [kt:salesforce-identity]
related: [kt:connected-apps, kt:salesforce-as-identity-provider, kt:lightning-service-console, kt:single-sign-on-saml]
relations:
  - {predicate: configuredVia, object: kt:app-manager}
  - {predicate: dependsOn, object: kt:profiles}
  - {predicate: dependsOn, object: kt:permission-sets}
  - {predicate: consumedBy, object: kt:lightning-apps}
sources:
  - id: s1
    title: "Configure and Use the App Launcher (Identity Implementation Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/identity_app_launcher_intro.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s2
    title: "Reorder App Launcher Apps in Lightning Experience"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/reordering_applauncher_lex.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s3
    title: "Set the Default Sort Order for Apps"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/reordering_custom_apps_parent.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s4
    title: "Enable the App Launcher with a Permission Set in Salesforce Classic"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/identity_app_launcher_permset.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s5
    title: "Create and Customize Lightning Apps"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_apps
    type: official-learning
    accessed: 2026-11-25
  - id: s6
    title: "Navigate Around (Lightning Experience for Salesforce Classic Users)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/lightning-experience-for-salesforce-classic-users/navigate-around
    type: official-learning
    accessed: 2026-11-25
created: 2026-11-25
---

# App Launcher

The **App Launcher** is the menu Salesforce users open to switch between apps. It presents a tile for each Salesforce, connected (third-party) and on-premises app the user is allowed to use, and admins decide which apps each user sees, in what order, and whether the App Launcher is the landing page after login.[^s1] Salesforce documents it in the Identity Implementation Guide rather than only as a navigation feature because it doubles as the user-facing portal for single sign-on into connected apps; its contents can also be managed programmatically through the AppMenuItem API.[^s1]

## What users see

In Lightning Experience the App Launcher icon sits at the left of the navigation bar, and seeing it there is itself a sign the user is in Lightning rather than Classic.[^s4] Opening it shows two sections: **All Apps**, a set of tiles that can include connected apps such as Gmail or Google Drive, and **All Items**, which lists every object and item the user has permission to use. A search box filters both, and authorised users get a direct link to AppExchange.[^s6] Lightning console apps, including the preconfigured Sales Console and Service Console, are opened from the App Launcher too; a user who sees no console tile needs an admin to grant access.[^s6]

Each Lightning app bundles objects, tabs and other items into its navigation bar and can carry its own colour and logo, and the App Launcher is how users move between those apps or reach something outside the current one.[^s5] Trailhead suggests leaving low-priority items out of an app's navigation bar, since users can still find them through the App Launcher.[^s5]

## How admins configure it

Visibility follows the user's access: users only see apps that their profile or permission sets authorise.[^s1] In Setup, **App Manager** lists Salesforce and connected apps, and its "Visible in Lightning Experience" column marks the apps the Lightning App Launcher can show; Classic-only apps without that mark do not appear there.[^s5] For a connected app or external service provider to get a tile, the admin specifies its start URL in App Manager.[^s3]

Order and org-wide visibility are set under **Setup > App Menu**. Admins drag apps into the default order, and changes apply immediately; each app can be toggled between "Visible in App Launcher" and "Hidden in App Launcher" for everyone in the org.[^s2] Viewing that page needs the View Setup and Configuration permission and changing it needs Customize Application.[^s2] All standard and custom apps start out visible; hiding all of them by default requires a request to Salesforce Customer Support.[^s2] Users can rearrange their own App Launcher, and their personal order overrides the admin's default.[^s3][^s2]

## Salesforce Classic differences

The App Launcher is available to both Lightning Experience and Classic users, but Classic needs extra setup.[^s1] A Classic user needs the **Use Identity Features** permission and the App Launcher setting on their profile set to Visible.[^s1] Admins on the standard System Administrator profile already have access, while admins on a profile cloned from it do not.[^s1] The usual way to grant it is a permission set (for example, one labelled "Identity Features") with the Use Identity Features system permission, assigned to the user; if the menu still doesn't show, set the profile's App Launcher setting to Visible.[^s4] Classic permission-set enablement is listed for Enterprise, Performance, Unlimited and Developer editions.[^s4]

## Gotchas

- Every installed app is listed in App Menu, but what a user actually sees combines its visibility toggle with their profile and permission sets.[^s2]
- A user's own reordering wins over the admin's order, so later admin changes to the default may not reach users who have customised theirs.[^s3]
- The 50-item cap applies to an app's navigation bar; items left off it stay reachable under All Items.[^s6]

## Connections

The App Launcher is one of the end-user surfaces of **Salesforce Identity** (`kt:salesforce-identity`), which is why it is configured alongside identity features.[^s1] Its third-party tiles come from **connected apps** (`kt:connected-apps`) whose start URL is set in **App Manager** (`kt:app-manager`), and clicking one typically starts an SSO hand-off in which the org acts as identity provider (`kt:salesforce-as-identity-provider`, `kt:single-sign-on-saml`).[^s3][^s1] What each user sees depends on **profiles** and **permission sets** (`kt:profiles`, `kt:permission-sets`).[^s1] It is also the switcher between **Lightning apps** (`kt:lightning-apps`) and the way users open console apps such as the **Lightning Service Console** (`kt:lightning-service-console`).[^s5][^s6]

## Sources
[^s1]: Salesforce Developers, "Configure and Use the App Launcher (Identity Implementation Guide)". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/identity_app_launcher_intro.htm (accessed 2026-11-25)
[^s2]: Salesforce Developers, "Reorder App Launcher Apps in Lightning Experience". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/reordering_applauncher_lex.htm (accessed 2026-11-25)
[^s3]: Salesforce Developers, "Set the Default Sort Order for Apps". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/reordering_custom_apps_parent.htm (accessed 2026-11-25)
[^s4]: Salesforce Developers, "Enable the App Launcher with a Permission Set in Salesforce Classic". https://developer.salesforce.com/docs/atlas.en-us.identityImplGuide.meta/%20identityImplGuide/identity_app_launcher_permset.htm (accessed 2026-11-25)
[^s5]: Trailhead, "Create and Customize Lightning Apps". https://trailhead.salesforce.com/content/learn/modules/lex_customization/lex_customization_apps (accessed 2026-11-25)
[^s6]: Trailhead, "Navigate Around (Lightning Experience for Salesforce Classic Users)". https://trailhead.salesforce.com/content/learn/modules/lightning-experience-for-salesforce-classic-users/navigate-around (accessed 2026-11-25)
