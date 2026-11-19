---
id: kt:release-updates
type: Feature
title: Release Updates
aliases: [Release Updates node, Release Updates page, Critical Updates, Critical Updates console, Enable Test Run]
domain: devops-and-alm
summary: >-
  The Setup page where Salesforce lists platform behaviour changes that it will enforce on every org in a future
  release, with recommended steps, a due date and, for many updates, a test run toggle so admins can try the new
  behaviour before enforcement. It replaced the older Critical Updates console.
release: "Winter '27"
status: current
broader: [kt:release-management]
related: [kt:salesforce-seasonal-releases, kt:sandbox-types, kt:testing-strategy, kt:org-check]
relations:
  - {predicate: partOf, object: kt:application-lifecycle-management}
  - {predicate: dependsOn, object: kt:environment-strategy}
sources:
  - id: s1
    title: "Release Updates (Salesforce Help)"
    publisher: Salesforce
    url: https://help.salesforce.com/s/articleView?language=en_US&id=sf.release_updates.htm&type=5
    type: official-docs
    accessed: 2026-11-19
  - id: s2
    title: "Learn MOAR with Summer '20 Release Updates Setup Page"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2020/learn-moar-with-summer-20-release-updates-setup-page
    type: official-blog
    accessed: 2026-11-19
  - id: s3
    title: "Master the Release Readiness Process (Advanced Salesforce Release Readiness Strategies)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/content/learn/modules/advanced-salesforce-release-readiness-strategies/master-the-release-readiness-process
    type: official-learning
    accessed: 2026-11-19
  - id: s4
    title: "Ultimate Guide to Salesforce Release Updates"
    publisher: Salesforce Ben
    url: https://www.salesforceben.com/ultimate-guide-to-salesforce-release-updates/
    type: partner
    accessed: 2026-11-19
created: 2026-11-19
---

# Release Updates

Release Updates is the node in Setup where Salesforce publishes changes to platform behaviour that will eventually be switched on for every org. Each entry explains what is changing, who is affected and what to do, and carries a deadline for completing the recommended steps. The page is available in all editions, in both Lightning Experience and Salesforce Classic, and it replaced the older Critical Updates console with more detailed information; Security Alerts were also folded into it.[^s1] Salesforce introduced the page as a beta in Summer '20, describing it as the first place to learn about updates arriving in major releases, patch releases and urgent fixes.[^s2]

## How it works

The home page groups updates by status so admins can see what needs attention. Salesforce Help names four: Needs Action, Due Soon (the Complete Steps By date is approaching), Overdue (the date has passed and steps are still open) and Archived (the update is complete). Tabs filter the list by category.[^s1] Each entry offers View Details for a quick summary and Get Started for the full workflow, where admins work through the steps, start or stop a test run and see the history of step changes.[^s1] The original beta also colour-coded entries and gave each a category tag showing the product area it touches.[^s2]

Many updates support a test run. Enabling it turns the new behaviour on in that org immediately, so admins can see its impact before Salesforce enforces it. The button is a toggle that can be switched on and off until the Complete Steps By date, although test periods in sandboxes can end sooner.[^s1] Updates that might be disruptive were flagged "Test Run Supported" from the start, and Salesforce encouraged trying them in a sandbox or production to surface conflicts.[^s2]

Enforcement is tracked per update. The detail page shows "Enforcement Scheduled" or "Enforced In" with the release that will make the change permanent, and a tooltip gives the upgrade date for that major release; any specific dates shown are guidance.[^s1] Because enforcement dates vary by instance, Salesforce pointed admins to the Trust status site for their instance's exact upgrade date.[^s2] Scheduled updates can still be changed or pushed back, so check the release notes each season rather than relying on a date noted months earlier.[^s4]

## Working practice and gotchas

Treat each release update like a small project in the delivery pipeline. A practitioner process published by Salesforce Ben runs: check whether the affected feature is used (for example by searching metadata), find where it is used, including inside managed packages whose provider may need to act, define the fix, build it in the sandbox furthest from production, test with Enable Test Run, promote it through the pipeline, and then enable and retest in production straight after the deployment.[^s4] The same guide warns that functionality can start failing once the enforcement date passes if the work is skipped.[^s4]

Release readiness training from Trailhead places this work inside the seasonal cycle: read the release notes (important critical updates are often called out under Salesforce Overall), and use the pre-release org, which usually opens three to four weeks before sandbox preview, to explore changes early.[^s3]

## Connections

Release Updates is a tool of **release management**, which it sits under, because each update becomes a change the team must plan, build and ship like its own features.[^s4] It is part of **application lifecycle management** and depends on a sound **environment strategy**: a test run needs sandboxes at the right stage, and the choice among **sandbox types** decides how realistic that test is.[^s1][^s4] Its rhythm follows the three **Salesforce seasonal releases** and the preview window before each.[^s3] It belongs in any **testing strategy** as a regression pass per release, since a test run exists precisely to find conflicts before enforcement.[^s1][^s2] Finding where an affected feature is used, the first step of that process, is the kind of org review that the **Org Check** node covers.[^s4]

## Sources
[^s1]: Salesforce Help, "Release Updates". https://help.salesforce.com/s/articleView?language=en_US&id=sf.release_updates.htm&type=5 (accessed 2026-11-19)
[^s2]: Salesforce Admins Blog, "Learn MOAR with Summer '20 Release Updates Setup Page". https://admin.salesforce.com/blog/2020/learn-moar-with-summer-20-release-updates-setup-page (accessed 2026-11-19)
[^s3]: Trailhead, "Master the Release Readiness Process". https://trailhead.salesforce.com/en/content/learn/modules/advanced-salesforce-release-readiness-strategies/master-the-release-readiness-process (accessed 2026-11-19)
[^s4]: Salesforce Ben, "Ultimate Guide to Salesforce Release Updates". https://www.salesforceben.com/ultimate-guide-to-salesforce-release-updates/ (accessed 2026-11-19)
