---
id: kt:read-only-mode
type: Feature
title: Read-Only Mode
aliases: [Salesforce read-only mode, read-only access during maintenance, maintenance read-only mode, ApplicationReadWriteMode]
domain: platform-architecture
summary: >-
  The degraded-availability state Salesforce puts a production org into during certain maintenance events, in
  which users and read API calls can still view and report on data but every database write fails until the
  maintenance ends.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform, kt:planned-maintenance-windows]
related: [kt:instance-refresh-and-org-migration, kt:disaster-recovery-and-site-switching, kt:trust-and-status-site, kt:apex-callouts, kt:hyperforce, kt:scheduled-apex]
relations:
  - {predicate: consumedBy, object: kt:heroku-connect}
  - {predicate: dependsOn, object: kt:pod-and-instance-architecture}
  - {predicate: contrastsWith, object: kt:screen-flow}
sources:
  - id: s1
    title: "Salesforce Read-Only Mode Overview"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?amp=&id=Read-Only-Mode-Overview&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-27
  - id: s2
    title: "How is my org impacted during Salesforce maintenance?"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=000335669&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-27
  - id: s3
    title: "Instance Refreshes and Consolidations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?amp=&id=Instance-Refresh-Maintenance-FAQ&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-27
  - id: s4
    title: "Site Switching and Apex Callouts"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2017/10/site-switching-apex-callouts
    type: official-blog
    accessed: 2026-11-27
  - id: s5
    title: "What do I need to do about my upcoming Salesforce site switch?"
    publisher: Heroku Help
    url: https://help.heroku.com/GXAW850T/what-do-i-need-to-do-about-my-upcoming-salesforce-site-switch
    type: official-docs
    accessed: 2026-11-27
  - id: s6
    title: "Salesforce Upgrades and Maintenance"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=xcloud.getstart_upgrades.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-27
created: 2026-11-27
---

# Read-Only Mode

Read-only mode is how Salesforce keeps an org partly usable while its underlying infrastructure is being moved or switched. Instead of taking the org fully offline, the platform lets people keep looking at their data while refusing anything that would write to the database.[^s1] Salesforce applies it during splits, instance migrations, instance switches, pre-scripts and some other maintenance events.[^s6] For a planned window, the Trust status wording says whether the instance will be read-only, fully unavailable, or generally available, so read-only is one of three possible availability levels.[^s2]

## What still works and what doesn't

In read-only mode users can view their data and run reports on it, but they cannot add, edit or delete records.[^s2] The Help overview lists further losses: no file downloads, password resets, activity reminders or Recent Items updates, no saving or editing reports, no dashboard refreshes, no Chatter posts, and no Live Agent.[^s1] More broadly, any feature that writes to the database is off for the duration.[^s1]

How users find out depends on the client. Salesforce Classic and mobile-browser users see a banner, Lightning Experience shows no banner and surfaces an error only when someone tries to save, and the Salesforce mobile app shows a read-only page at login.[^s1] Experience Cloud sites, portals and Salesforce Sites display a maintenance-in-progress message.[^s1] Screen flows and login flows running in Lightning runtime fail with an error telling the user to try again after maintenance, which matters if a login flow gates access to the org.[^s1] Login history is still captured but only shows up a few minutes after the org leaves read-only mode.[^s1]

## Behavior for integrations and code

Read API calls succeed, while API writes fail with the error code `INSERT_UPDATE_DELETE_NOT_ALLOWED_DURING_MAINTENANCE`; Apex DML fails with `InvalidReadOnlyUserDmlException`.[^s1] Inbound Email-to-X and Web-to-X submissions are queued and processed once maintenance finishes.[^s1][^s2] Batch, scheduled, long-running and Bulk API jobs need no action beforehand: Salesforce queues them and runs them after the window, while weekly exports and physical delete are suspended and resume later.[^s2]

The trap for developers is that outbound Apex callouts keep running in read-only mode.[^s4] Code that calls an external system and then tries to record the result in Salesforce can leave the two systems out of sync, because the callout succeeds and the follow-up DML fails.[^s4][^s3] Salesforce recommends stopping callouts while the org is read-only.[^s3] Apex can check the state with `System.getApplicationReadWriteMode()`, which returns `System.ApplicationReadWriteMode.READ_ONLY` when the org or its instance is read-only, so callout logic can skip or defer work.[^s4]

Middleware has to cope too. Heroku Connect detects read-only mode and retries pending writes for read-write mappings, and Heroku suggests pausing the connection just before a site switch for full control; read-only mappings need no action.[^s5]

## Typical duration and triggers

For a first-party instance refresh, the production org is placed in read-only mode during maintenance lasting up to 4 hours, while a sandbox on the same refresh simply has downtime.[^s3] An instance consolidation, by contrast, is a site switch with up to 2 hours of downtime rather than read-only access.[^s3] Planned refreshes and site switches use part of the customer's preferred maintenance window for their read-only period.[^s4]

## Testing and preparation

Salesforce can enable a read-only testing option in a sandbox on request, so teams can watch how custom code, flows and integrations behave before a real window.[^s1] Useful preparation is to guard callouts with the read-write mode check, make integrations retry on the maintenance error code rather than fail permanently, and check that login flows don't block access.[^s1][^s4] Because platform events and Change Data Capture lose their replay continuity across an instance refresh, subscribers should be ready to resynchronize afterward.[^s3]

## Connections

Read-only mode is a behavior of the `kt:salesforce-platform` that shows up inside `kt:planned-maintenance-windows`, which is why that node is listed as broader.[^s2][^s4] It's the state most often triggered by `kt:instance-refresh-and-org-migration` and by `kt:disaster-recovery-and-site-switching`, both run at the level of the instances described in `kt:pod-and-instance-architecture`, and windows are announced on `kt:trust-and-status-site`.[^s3][^s4][^s6] Migrations to `kt:hyperforce` are documented separately from first-party instance refreshes, so check the guidance for the specific event.[^s3] It creates the callout-consistency risk covered in `kt:apex-callouts`, it shapes how `kt:heroku-connect` retries writes, and it affects queued `kt:scheduled-apex` jobs.[^s4][^s5][^s2] It contrasts with `kt:screen-flow`, since screen flows in Lightning runtime fail outright rather than degrading.[^s1]

## Sources
[^s1]: Salesforce Help, "Salesforce Read-Only Mode Overview". https://help.salesforce.com/s/articleView?amp=&id=Read-Only-Mode-Overview&language=en_US&type=1 (accessed 2026-11-27)
[^s2]: Salesforce Help, "How is my org impacted during Salesforce maintenance?". https://help.salesforce.com/s/articleView?id=000335669&language=en_US&type=1 (accessed 2026-11-27)
[^s3]: Salesforce Help, "Instance Refreshes and Consolidations". https://help.salesforce.com/s/articleView?amp=&id=Instance-Refresh-Maintenance-FAQ&language=en_US&type=1 (accessed 2026-11-27)
[^s4]: Salesforce Developers Blog, "Site Switching and Apex Callouts" (Chris Peterson and Aaron Slettehaugh, 2017). https://developer.salesforce.com/blogs/2017/10/site-switching-apex-callouts (accessed 2026-11-27)
[^s5]: Heroku Help, "What do I need to do about my upcoming Salesforce site switch?". https://help.heroku.com/GXAW850T/what-do-i-need-to-do-about-my-upcoming-salesforce-site-switch (accessed 2026-11-27)
[^s6]: Salesforce Help, "Salesforce Upgrades and Maintenance". https://help.salesforce.com/s/articleView?id=xcloud.getstart_upgrades.htm&language=en_US&type=5 (accessed 2026-11-27)
