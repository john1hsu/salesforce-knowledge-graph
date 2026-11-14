---
id: kt:change-management-and-adoption
type: Concept
title: Change Management and Adoption
aliases: [user adoption, organizational change management, OCM, Salesforce adoption strategy, LEVERS of Change model]
domain: architecture-practice
summary: >-
  The people side of a Salesforce rollout: planning, communicating, training and measuring so that users actually
  change how they work, structured by Salesforce around a Discover, Rollout and Optimize cycle and the LEVERS of
  Change model (Leadership, Ecosystem, Values, Enablement, Rewards, Structure).
release: "Winter '27"
status: concept
broader: [kt:salesforce-governance]
related: [kt:salesforce-center-of-excellence, kt:requirements-gathering, kt:release-management, kt:in-app-guidance, kt:salesforce-optimizer]
relations:
  - {predicate: usedBy, object: kt:salesforce-architect}
  - {predicate: contrastsWith, object: kt:application-lifecycle-management}
sources:
  - id: s1
    title: "Build Your Own LEVERS Model (LEVERS of Change Model)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/levers-of-change-model/build-you-own-leversmodel
    type: official-learning
    accessed: 2026-11-14
  - id: s2
    title: "Manage Organizational Change (Drucker School—Organizational Change Leadership)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/drucker_org_change_leadership/manage-organizational-change
    type: official-learning
    accessed: 2026-11-14
  - id: s3
    title: "Encourage and Support Users (User Training and Enablement)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/user-training-and-motivation/encourage-and-support-users
    type: official-learning
    accessed: 2026-11-14
  - id: s4
    title: "6 Guiding Principles to Maximize Your Salesforce Adoption"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2021/6-guiding-principles-to-maximize-your-salesforce-adoption
    type: official-blog
    accessed: 2026-11-14
  - id: s5
    title: "Manage Change During Your Lightning Experience Transition"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/manage-change-during-your-lightning-experience-transition
    type: official-blog
    accessed: 2026-11-14
  - id: s6
    title: "Create Prompts in Agentforce 360 Platform (User Engagement)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/user-engagement/create-in-app-prompts
    type: official-learning
    accessed: 2026-11-14
created: 2026-11-14
---

# Change Management and Adoption

Change management and adoption is the discipline of getting people to actually work in a new Salesforce solution, rather than only deploying it. Salesforce's own guidance treats the human side as the hard part: products, org charts and processes can be changed quickly, but people need help adjusting, and their reactions shape how well the change lands.[^s2] For a Salesforce program, a technically sound release that users route around (spreadsheets, side tools, a return to the old interface) has not delivered its value, which is why adoption belongs in the architecture and governance conversation and not only in training.[^s4][^s5]

## How it works

Salesforce frames a change initiative in three phases, used both in its Lightning Experience transition guidance and in its LEVERS of Change model.[^s1][^s5]

- **Discover**: gather user feedback, align an executive sponsor and stakeholders, run a change impact assessment and name likely blockers.[^s1][^s5]
- **Rollout**: decide who moves first, then execute communications, training and the change network of champions and influencers.[^s1][^s5]
- **Optimize**: keep going after go-live by collecting feedback, monitoring adoption metrics and adjusting tactics for the next stage.[^s1][^s5]

The LEVERS model groups six levers into three sources of influence: social (Leadership, Ecosystem), individual (Values, Enablement) and structural (Rewards, Structure).[^s1] The team cocreates a playbook of strategies for each lever, plots them on the Discover/Rollout/Optimize timeline, and assigns owners so leader time and thin resources are visible early.[^s1] Trailhead's worked example sets a SMART goal of 90% adoption for a 60-person sales team moving off spreadsheets, with tactics such as managers running sales meetings from Salesforce, an influencer network, "What's in it for me?" messaging per stakeholder group, realistic training scenarios, adoption leaderboards, and updated process documents and policies.[^s1]

For the leadership side, Trailhead's Drucker School module walks through Kotter's eight steps, from creating urgency and building a coalition to anchoring the change in daily operations, and stresses that communication must be repeated through varied channels and aimed at specific groups.[^s2] It also warns that resistance is normal: some people disagree with the change, and others support it in principle but fear its personal consequences.[^s2]

## Practices that drive adoption

- **Champions and super users** who understand the business process act as first-line help and an extension of the admin team.[^s3]
- **Visible leadership**: leaders run meetings and pipeline reviews in Salesforce and report adoption metrics in organizational updates.[^s4]
- **Simplicity**: avoid excess required fields, prefer out-of-the-box features, and use tools such as Salesforce Optimizer to remove clutter.[^s4]
- **Ongoing, varied training**, including short on-demand recordings, hands-on sandbox practice and sessions built from recurring support questions.[^s3][^s4]
- **A documented support path** that tells users whom to contact for each kind of issue, plus closing the loop on their suggestions.[^s3]
- **Adoption dashboards** to spot active and inactive users, recognize active ones, and find holdouts whose objections can improve the design.[^s3][^s4]

In-app guidance supports the Rollout and Optimize phases directly: admins build floating, docked or targeted prompts and multi-step walkthroughs in the In-App Guidance Builder, schedule how often and how long they show, and read engagement metrics on completion.[^s6]

## Limits and gotchas

Adoption work cannot fix a solution that is cluttered or irrelevant to users; Salesforce's guidance puts simplicity and meaningful, consolidated workflows ahead of more training.[^s4] Treating go-live as the finish line is the common failure: both the Lightning transition guidance and the LEVERS model keep measuring and adjusting after launch.[^s1][^s5] In-app prompts on Experience Cloud sites carry extra prerequisites, including purchased Enablement and PRM and an Aura-template site.[^s6]

## Connections

Change management sits under **Salesforce governance**: Salesforce's adoption guidance pairs the change plan with an operating model, a governance model and a communication cadence, the kind of standing structure a **Center of Excellence** provides.[^s4] It starts in **requirements gathering**, where interviewing and observing users and co-designing with them builds buy-in before anything is built.[^s4] It complements, and contrasts with, **application lifecycle management** and **release management**: those move metadata safely to production, while this moves people.[^s1][^s5] **In-App Guidance** and **Salesforce Optimizer** are platform tools that serve it.[^s4][^s6] For **Salesforce architects**, it is a reminder that a design's value depends on whether users take it up, which is why simplicity is a design choice as much as a training goal.[^s4]

## Sources
[^s1]: Salesforce Trailhead, "Build Your Own LEVERS Model (LEVERS of Change Model)". https://trailhead.salesforce.com/content/learn/modules/levers-of-change-model/build-you-own-leversmodel (accessed 2026-11-14)
[^s2]: Salesforce Trailhead, "Manage Organizational Change (Drucker School—Organizational Change Leadership)". https://trailhead.salesforce.com/content/learn/modules/drucker_org_change_leadership/manage-organizational-change (accessed 2026-11-14)
[^s3]: Salesforce Trailhead, "Encourage and Support Users (User Training and Enablement)". https://trailhead.salesforce.com/content/learn/modules/user-training-and-motivation/encourage-and-support-users (accessed 2026-11-14)
[^s4]: Salesforce Admins Blog, "6 Guiding Principles to Maximize Your Salesforce Adoption". https://admin.salesforce.com/blog/2021/6-guiding-principles-to-maximize-your-salesforce-adoption (accessed 2026-11-14)
[^s5]: Salesforce Admins Blog, "Manage Change During Your Lightning Experience Transition". https://admin.salesforce.com/manage-change-during-your-lightning-experience-transition (accessed 2026-11-14)
[^s6]: Salesforce Trailhead, "Create Prompts in Agentforce 360 Platform (User Engagement)". https://trailhead.salesforce.com/content/learn/modules/user-engagement/create-in-app-prompts (accessed 2026-11-14)
