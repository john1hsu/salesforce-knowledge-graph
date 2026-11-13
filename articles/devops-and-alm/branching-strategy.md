---
id: kt:branching-strategy
type: Concept
title: Branching Strategy
aliases: [Git branching strategy, Salesforce branching strategy, branching model, source control branching model]
domain: devops-and-alm
summary: >-
  The team convention for how Git branches are created, named, merged and mapped to Salesforce environments, which
  decides how metadata changes move from development orgs through test sandboxes to production.
release: "Winter '27"
status: concept
broader: [kt:application-lifecycle-management]
related: [kt:environment-strategy, kt:scratch-orgs, kt:source-tracking, kt:change-sets, kt:continuous-integration-for-salesforce]
relations:
  - {predicate: configuredVia, object: kt:devops-center}
  - {predicate: dependsOn, object: kt:sandbox-types}
  - {predicate: integratesWith, object: kt:salesforce-cli}
sources:
  - id: s1
    title: "Build and Activate a Lifecycle Center Release Pipeline (Lifecycle Center Setup)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/devops-center-setup/build-your-release-pipeline
    type: official-learning
    accessed: 2026-11-13
  - id: s2
    title: "Unbundled Promotions: A Deeper Look (DevOps Center Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.devops_center_dev.meta/devops_center_dev/devops_center_dev_promotions_unbundled.htm
    type: official-docs
    accessed: 2026-11-13
  - id: s3
    title: "DevOps Center for Hybrid Teams"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2024/09/devops-center-for-hybrid-teams
    type: official-blog
    accessed: 2026-11-13
  - id: s4
    title: "Work with Teams in GitHub (Git and GitHub Basics)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/git-and-git-hub-basics/work-with-teams-in-git-hub
    type: official-learning
    accessed: 2026-11-13
  - id: s5
    title: "Choosing the right Git branching strategy for your Salesforce team"
    publisher: Gearset
    url: https://gearset.com/blog/choosing-the-right-git-branching-strategy-for-your-team/
    type: partner
    accessed: 2026-11-13
  - id: s6
    title: "How to avoid and resolve merge conflicts in your Salesforce CI/CD pipeline"
    publisher: Gearset
    url: https://gearset.com/blog/how-to-resolve-salesforce-merge-conflicts/
    type: partner
    accessed: 2026-11-13
created: 2026-11-13
---

# Branching Strategy

A **branching strategy** is the set of rules a Salesforce team follows for its Git repository: which branches are long-lived, which are temporary, how they are named, how work is merged and reviewed, and which branch corresponds to which org. On Salesforce the choice matters more than on many platforms because every branch is ultimately deployed into an org, so the branch layout and the environment strategy have to be designed together.[^s1][^s5]

## How it works on Salesforce

Salesforce's own release tool makes the branch-to-org mapping explicit. In a DevOps Center (now Lifecycle Center) pipeline, each stage is one environment paired with one branch, and changes flow left to right toward production.[^s1] The Trailhead reference pipeline maps an Integration stage on a Partial Copy sandbox to an `int` branch, a UAT stage on a Full Copy sandbox to `uat`, and Production to `main`; the stage branches are created right to left, `uat` from `main` and then `int` from `uat`.[^s1] The development stage has no stage branch: the tool opens a temporary feature branch per work item (for example `feature/WI-000001`) when the work item moves to In Progress.[^s1]

Promotion is a merge plus a deployment. Each work item's feature branch is merged into the branch of the target stage, the merge commit is recorded, and after a successful promotion the tool rebases the feature branch.[^s2] Developers who prefer the Salesforce CLI and an IDE can check out the same feature branch and commit to it, and those commits show up on the work item; branches created by hand must match the work item ID for this synchronization to work.[^s3] Pull requests can also be merged directly in GitHub, after which DevOps Center reports that the stage org is out of sync with its branch until the deployment is completed.[^s2][^s3]

## Common models

Partner guidance groups Salesforce teams' options into a few recurring models:[^s5]

- **Branch per org as backup**: each org's metadata is pushed to its own branch. Git records history but does not drive releases.[^s5]
- **Feature branching**: only `main` lives long; short-lived feature branches are cut from it and merged back. Simple and fast, with few gates.[^s5]
- **Protected main**: one long-lived integration branch sits in front of `main`, so only UAT-tested work reaches production; partial promotion is harder.[^s5]
- **Expanded branching**: long-lived branches for each test environment, promoting items one stage at a time. This is the shape DevOps Center pipelines use.[^s1][^s5]
- **Gitflow**: a `develop` branch feeds test orgs, release branches are cut for production, and hotfix branches come off `main`. It suits a fixed release cadence.[^s5]

Trailhead's Git module leans toward simplicity: branches should be short-lived, single-purpose and deleted after merging, and long-running branches tend to cause stale code and needless conflicts.[^s4]

## Limits and gotchas

- **Metadata conflicts.** Salesforce metadata is XML, element order can shift between retrievals, and large shared files such as profiles collect unrelated edits on adjacent lines, so conflicts are more frequent than in ordinary code.[^s6]
- **Drift.** Hotfixes made directly in production and abandoned work make orgs and branches diverge; partners advise back-promoting fixes to lower environments.[^s6]
- **Branch lifetime.** The longer a branch stays open, the more likely others have changed the same files; merge small and often and keep one feature per pull request.[^s6][^s4]
- **Not a backup.** Version control does not replace a data and metadata backup solution.[^s5]

## When to use which

Small teams that value speed usually start with feature branching, ideally with scratch orgs built from the repository so each branch gets a disposable org.[^s5] Teams that need several test gates, or that are moving from change sets and already think in terms of promoting between environments, fit the expanded model, which is what DevOps Center provides out of the box.[^s1][^s5] Gitflow pays off only when releases are batched on a predictable schedule.[^s5]

## Connections

The strategy is part of application lifecycle management and is configured in practice through DevOps Center, whose pipeline stages are branch-and-org pairs.[^s1] It depends on the sandbox types chosen for each stage and mirrors the environment strategy.[^s1] Developers work on the same branches through the Salesforce CLI, while source tracking in scratch orgs and sandboxes identifies what to commit.[^s3] It is the foundation for continuous integration, since automated validation runs on merges into stage branches.[^s3][^s5]

## Sources
[^s1]: Trailhead, "Build and Activate a Lifecycle Center Release Pipeline (Lifecycle Center Setup)". https://trailhead.salesforce.com/content/learn/modules/devops-center-setup/build-your-release-pipeline (accessed 2026-11-13)
[^s2]: Salesforce Developers, "Unbundled Promotions: A Deeper Look (DevOps Center Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.devops_center_dev.meta/devops_center_dev/devops_center_dev_promotions_unbundled.htm (accessed 2026-11-13)
[^s3]: Salesforce Developers Blog, "DevOps Center for Hybrid Teams" (2024-09-05). https://developer.salesforce.com/blogs/2024/09/devops-center-for-hybrid-teams (accessed 2026-11-13)
[^s4]: Trailhead, "Work with Teams in GitHub (Git and GitHub Basics)". https://trailhead.salesforce.com/content/learn/modules/git-and-git-hub-basics/work-with-teams-in-git-hub (accessed 2026-11-13)
[^s5]: Gearset, "Choosing the right Git branching strategy for your Salesforce team" (2024-07-26). https://gearset.com/blog/choosing-the-right-git-branching-strategy-for-your-team/ (accessed 2026-11-13)
[^s6]: Gearset, "How to avoid and resolve merge conflicts in your Salesforce CI/CD pipeline" (2024-06-28). https://gearset.com/blog/how-to-resolve-salesforce-merge-conflicts/ (accessed 2026-11-13)
