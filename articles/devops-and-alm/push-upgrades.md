---
id: kt:push-upgrades
type: Feature
title: Push Upgrades
aliases: [push upgrade, package push upgrade, push package upgrade, customized push upgrades, Push Upgrade Exclusion List]
domain: devops-and-alm
summary: >-
  A packaging capability that lets a package owner upgrade installed managed or unlocked packages in chosen subscriber
  orgs to a chosen version at a scheduled time, without the subscriber installing anything; driven from the UI (1GP),
  Salesforce CLI (2GP and unlocked) or SOAP API objects such as PackagePushRequest and PackagePushJob.
release: "Winter '27"
status: current
broader: [kt:release-management, kt:application-lifecycle-management]
related: [kt:second-generation-managed-packages, kt:first-generation-managed-packages, kt:unlocked-packages, kt:package-versioning-and-ancestry, kt:post-install-scripts]
relations:
  - {predicate: dependsOn, object: kt:appexchange-security-review}
  - {predicate: dependsOn, object: kt:dev-hub}
  - {predicate: configuredVia, object: kt:salesforce-cli}
  - {predicate: configuredVia, object: kt:soap-api}
sources:
  - id: s1
    title: "Push a Package Upgrade for Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/push_upgrade_intro_2GP.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s2
    title: "Schedule a Push Upgrade Using CLI"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/push-upgrade-cli.html
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "Schedule a Push Upgrade Using SOAP API for First- and Second-Generation Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/push_upgrade_use_api.htm
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "Enable a Package Subscriber to Restrict Push Upgrades"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/push-upgrade-customized.html
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "Push Package Upgrades to Subscribers (First-Generation Managed Packaging Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/push-upgrade-intro.html
    type: official-docs
    accessed: 2026-11-16
  - id: s6
    title: "Push Upgrades (First-Generation Managed Packaging Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg1-dev/guide/packaging-push-about.html
    type: official-docs
    accessed: 2026-11-16
created: 2026-11-16
---

# Push Upgrades

A **push upgrade** moves a package that is already installed in subscriber orgs to a newer version, initiated by the package owner rather than by each customer. The owner picks the target orgs, the version and the timing, and subscribers take no action. Salesforce positions it as a way to keep most or all customers on one version, which cuts the risk and support cost of running many versions in the field, and as the route for urgent bug fixes.[^s5][^s1]

## Who can use it

Push upgrades apply to first-generation (1GP) and second-generation (2GP) managed packages that have passed the AgentExchange security review, and to unlocked packages.[^s1][^s2] For managed packages the feature is switched on by logging a case with Salesforce Partner Support; for unlocked packages it is enabled by default.[^s2][^s5] The tooling differs by package type: 1GP pushes can be run from the UI or the API, while 2GP and unlocked pushes use Salesforce CLI or the API and have no UI.[^s1] For 2GP and unlocked packages the push runs in the context of the Dev Hub that owns the package, and the user needs the Create and Update Second-Generation Packages permission.[^s2]

## How it works

With the CLI, there are three stages. First, find target orgs by querying the `PackageSubscriber` object with `sf data query`, filtering by subscriber package ID (prefix `033`) or package version ID (prefix `04t`); there is no dedicated command for this step.[^s2] Second, run `sf package push-upgrade schedule --package <04t id>` with either `--org-list` or `--org-file` (a CSV of org IDs, one per line, with the header line removed) and an optional `--start-time` in UTC; without a start time the push begins when resources are available.[^s2] Third, track it with `sf package push-upgrade list` and `sf package push-upgrade report`, and cancel with `sf package push-upgrade abort` while the request is still Created or Pending.[^s2]

The SOAP API path exposes the same model as objects. A `PackagePushRequest` names the `PackageVersionId` and an optional `ScheduledStartTime`; one `PackagePushJob` per subscriber org is attached to it; and setting the request status to Pending schedules the push.[^s3] Subscriber queries return up to 2,000 records per call, so larger lists need `queryMore()`, and a scheduled push can start a few hours after the requested time.[^s3] Error detail for failed orgs lives in `PackagePushError`, which the CLI docs suggest querying directly.[^s2]

During the upgrade, Apex in the package is compiled, the normal manageability rules for version upgrades apply, and the push succeeds even if the version is password-protected.[^s1]

## Controlling who gets pushed

1GP owners can keep orgs out of a push with the **Push Upgrade Exclusion List**, which takes up to 500 comma-separated org IDs.[^s5] Partners can also grant **customized push upgrades** to specific customers. The partner runs `PushUpgradeCustomizationRepository.create()` in Execute Anonymous for each package ID and production org ID, optionally with an expiry in days. The subscriber then clicks Block Push Upgrades on the package in Installed Packages.[^s4] Sandboxes inherit the ability from their production org, blocks cannot apply to patch versions, and the partner cannot shorten the expiry once a customer has blocked.[^s4] If a managed 2GP moves to a new Dev Hub, the blocking records and permissions do not move with it.[^s4]

## Gotchas and best practices

- Subscribers get no notice apart from a higher version number on the package detail page, so tell them in advance.[^s5][^s6]
- New components arrive assigned only to admins; a post-install Apex script can grant access to existing users.[^s1][^s5]
- Use that script for enhancements to existing features, but leave brand-new features unassigned so admins can opt in.[^s6]
- Avoid changing validation rules, formula fields or trigger errors, which can break subscriber integrations.[^s6]
- Keep patches free of visible changes; test against org shapes that mirror customers' editions, packages and permission sets.[^s6]
- Push in customers' off-peak hours and away from Salesforce major release windows; the initiator owns resolving failures.[^s6][^s5]

## Connections

Push upgrades are a **release management** and **application lifecycle management** technique for ISVs and internal package teams.[^s5] They operate on **second-generation managed packages**, **first-generation managed packages** and **unlocked packages**, delivering versions defined through **package versioning and ancestry**.[^s1] Managed packages depend on passing the **AppExchange security review**, and 2GP pushes run from the owning **Dev Hub**.[^s1][^s2] The work is configured through **Salesforce CLI** or the **SOAP API**, and is often paired with **post-install scripts** that adjust access after the upgrade.[^s2][^s3][^s5]

## Sources

[^s1]: Salesforce Developers, "Push a Package Upgrade for Second-Generation Managed Packages". https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/push_upgrade_intro_2GP.htm (accessed 2026-11-16)
[^s2]: Salesforce Developers, "Schedule a Push Upgrade Using CLI". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/push-upgrade-cli.html (accessed 2026-11-16)
[^s3]: Salesforce Developers, "Schedule a Push Upgrade Using SOAP API for First- and Second-Generation Managed Packages". https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/push_upgrade_use_api.htm (accessed 2026-11-16)
[^s4]: Salesforce Developers, "Enable a Package Subscriber to Restrict Push Upgrades". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/push-upgrade-customized.html (accessed 2026-11-16)
[^s5]: Salesforce Developers, "Push Package Upgrades to Subscribers". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/push-upgrade-intro.html (accessed 2026-11-16)
[^s6]: Salesforce Developers, "Push Upgrades". https://developer.salesforce.com/docs/platform/pkg1-dev/guide/packaging-push-about.html (accessed 2026-11-16)
