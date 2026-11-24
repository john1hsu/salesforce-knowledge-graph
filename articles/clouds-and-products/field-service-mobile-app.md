---
id: kt:field-service-mobile-app
type: Feature
title: Field Service Mobile App
aliases: [Salesforce Field Service mobile app, Field Service Lightning mobile app, FSL mobile app, Field Service Mobile]
domain: clouds-and-products
summary: >-
  The iOS and Android app that Field Service mobile workers use to see their schedule, open work orders and service appointments,
  navigate to jobs, update inventory and complete work, with offline priming and Offline Briefcase so they keep working without a connection.
release: "Winter '27"
status: current
broader: [kt:field-service]
related: [kt:salesforce-mobile-app, kt:service-appointments, kt:work-orders, kt:dispatcher-console, kt:briefcase-builder]
relations:
  - {predicate: partOf, object: kt:field-service}
  - {predicate: dependsOn, object: kt:my-domain}
  - {predicate: configuredVia, object: kt:connected-apps}
  - {predicate: integratesWith, object: kt:lightning-web-components}
  - {predicate: alternativeTo, object: kt:salesforce-mobile-app}
sources:
  - id: s1
    title: "Work From Anywhere (Field Service Mobile, Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field-service-mobile/work-from-anywhere
    type: official-learning
    accessed: 2026-11-24
  - id: s2
    title: "Set Up a Mobile Worker (Field Service Mobile, Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field-service-mobile/set-up-a-mobile-worker
    type: official-learning
    accessed: 2026-11-24
  - id: s3
    title: "Access Your Office on Your Phone (Field Service Mobile, Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/field-service-mobile/access-your-office-on-your-phone
    type: official-learning
    accessed: 2026-11-24
  - id: s4
    title: "Allow Access to Information Offline (Offline Briefcase for Field Service, Trailhead unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/offline-briefcase/allow-access-to-information-online
    type: official-learning
    accessed: 2026-11-24
  - id: s5
    title: "Configure Offline Mode in the Field Service Mobile App (Field Service Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.field_service_dev.meta/field_service_dev/sfs_gs_lwc_fs_offline.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s6
    title: "Considerations for LWC Offline in the Field Service Mobile App (Field Service Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.field_service_dev.meta/field_service_dev/sfs_gs_lwc_considerations.htm
    type: official-docs
    accessed: 2026-11-24
created: 2026-11-24
---

# Field Service Mobile App

The Field Service mobile app is the native app for iOS and Android that technicians and other mobile workers use to do the on-site half of Field Service. Workers install it from Google Play or the Apple App Store and sign in through their org's custom My Domain; from there they see the day's service appointments, drive to each job, review the work order and asset history, and mark the work complete.[^s1] Trailhead stresses that the app works as soon as it is installed and recommends starting from the default configuration before customizing.[^s3]

## What workers see

The home screen combines a calendar for other days, a map with appointments and driving directions, the list of today's service appointments, a pull-up list of quick and global actions such as New Task or New Note, and a navigation bar for the schedule, inventory, notifications and profile.[^s1] Opening a work order shows four panes: Overview (map, location, contact and the asset's service history), Details (number, territory, owner, status), Related (line items, service appointments, skill requirements, child work orders) and Feed for talking to dispatch.[^s1] A typical job runs: check inventory before leaving, follow the map, review history, take before-and-after photos, then choose Complete Work from Show Actions and step through the prompts.[^s1]

Beyond the schedule, the app gives access to knowledge articles, parts and vehicle inventory tracking, product and service recommendations for upselling in the field, customer signatures and photos, messaging with the dispatcher, and maps that can be downloaded for offline use.[^s3]

## Setting up a mobile worker

Field Service set up through Salesforce Go installs the Field Service connected app package by default; it provides geolocation, so dispatchers see workers' positions in real time, and push notifications, and it unlocks mobile settings.[^s2] Each mobile worker needs an active user with a password, a service resource record, membership in a service territory, and both a scheduling and a mobile license.[^s2] Trailhead lists the permission sets Field Service Resource License, Field Service Resource Permissions and FSL Mobile License, and has the admin share the worker's service resource record with them (Read Only) so the app can load it.[^s2]

## Working offline

The app downloads the data a worker is likely to need while connected, a process Salesforce calls **offline priming**, so the worker keeps working without signal and changes sync back once the connection returns.[^s3] By default it primes service appointments from 45 days before to 45 days after today; admins can shorten that window in Field Service Mobile Settings, and Trailhead notes a smaller window makes the app launch faster.[^s2]

For finer control, **Offline Briefcase** lets an admin pick exactly which objects and records go to the device, assigned to one worker or a group and filtered by location, record type or other fields; briefcase records can feed flows and extensions that run fully offline.[^s4] **Performance Priming** builds on briefcases to fetch the records and metadata each worker's profile needs, and Trailhead says it syncs the most critical changes every five minutes.[^s4][^s2]

With Automatic Offline Mode, the app decides it is offline by repeatedly checking the Salesforce API rather than just looking for Wi-Fi or cellular signal, so it can go offline even with a weak connection. Admins tune this with custom attributes on the iOS or Android connected app; workers must log out and back in to pick up changes.[^s5] The defaults are:[^s5]

- A connection check every 15 seconds while online, and 1 second after a failed check.[^s5]
- Offline after 3 failed checks; back online after 3 successful ones; a check times out after 5 seconds.[^s5]

## Limits and gotchas

- Aggressive check settings can make the app flip between modes, and a flow in progress can be interrupted when it switches.[^s5]
- Online status reflects connection checks, not data calls, so data refresh can still be slow where coverage is poor.[^s5]
- Task records placed in a briefcase are not primed and trigger a priming error, though other objects still prime.[^s6]
- Global quick actions do not receive the current record's ID, even when launched from a record page.[^s6]
- On iOS, changes to Lightning web components appear only after a cold start of the app.[^s6]

## When to use it (and when not)

Use the Field Service app when users are scheduled resources working through service appointments and work orders, often with poor coverage; it is built around that data model and its offline priming.[^s1][^s2] Its screens, navigation and priming are organized around the worker's appointments, so users who work general CRM records without Field Service scheduling fit the general Salesforce mobile app better. Customize before replacing: branding, notifications, object-specific quick actions, global actions, flows and app extensions that pass data to other apps are all supported.[^s1][^s3]

## Connections

The app is **part of** `kt:field-service` and is where workers act on `kt:service-appointments` and `kt:work-orders` that dispatchers schedule in the `kt:dispatcher-console`.[^s1][^s2] Login **depends on** `kt:my-domain`, and its behavior is **configured via** the Field Service `kt:connected-apps` for iOS and Android.[^s1][^s5] Custom screens are built with `kt:lightning-web-components` running offline (LWC Offline).[^s6] Offline data selection uses briefcases, linking it to `kt:briefcase-builder`, and it is an **alternative to** the general `kt:salesforce-mobile-app` for field workers.[^s4][^s3]

## Sources
[^s1]: Trailhead, "Work From Anywhere". https://trailhead.salesforce.com/content/learn/modules/field-service-mobile/work-from-anywhere (accessed 2026-11-24)
[^s2]: Trailhead, "Set Up a Mobile Worker". https://trailhead.salesforce.com/content/learn/modules/field-service-mobile/set-up-a-mobile-worker (accessed 2026-11-24)
[^s3]: Trailhead, "Access Your Office on Your Phone". https://trailhead.salesforce.com/content/learn/modules/field-service-mobile/access-your-office-on-your-phone (accessed 2026-11-24)
[^s4]: Trailhead, "Allow Access to Information Offline". https://trailhead.salesforce.com/content/learn/modules/offline-briefcase/allow-access-to-information-online (accessed 2026-11-24)
[^s5]: Salesforce, "Configure Offline Mode in the Field Service Mobile App". https://developer.salesforce.com/docs/atlas.en-us.field_service_dev.meta/field_service_dev/sfs_gs_lwc_fs_offline.htm (accessed 2026-11-24)
[^s6]: Salesforce, "Considerations for LWC Offline in the Field Service Mobile App". https://developer.salesforce.com/docs/atlas.en-us.field_service_dev.meta/field_service_dev/sfs_gs_lwc_considerations.htm (accessed 2026-11-24)
