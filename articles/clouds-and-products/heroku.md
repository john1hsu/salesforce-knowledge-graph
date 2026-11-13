---
id: kt:heroku
type: Product
title: Heroku
aliases: [Heroku Platform, Heroku PaaS]
domain: clouds-and-products
summary: >-
  Salesforce's container-based platform as a service for running custom applications in languages such as Node.js,
  Python, Java and Ruby on managed dynos, with add-ons such as Heroku Postgres and Salesforce-specific bridges
  (Heroku Connect, Heroku External Objects, Heroku AppLink); since February 2026 it runs on a sustaining-engineering model.
release: "Winter '27"
status: current
broader: [kt:platform-as-a-service]
related: [kt:salesforce-platform]
relations:
  - {predicate: hasPart, object: kt:heroku-connect}
  - {predicate: hasPart, object: kt:heroku-applink}
  - {predicate: integratesWith, object: kt:salesforce-connect}
  - {predicate: integratesWith, object: kt:agentforce}
  - {predicate: mitigates, object: kt:api-request-limits}
sources:
  - id: s1
    title: "How Heroku Works"
    publisher: Heroku Dev Center (Salesforce)
    url: https://devcenter.heroku.com/articles/how-heroku-works
    type: official-docs
    accessed: 2026-11-13
  - id: s2
    title: "Heroku Connect"
    publisher: Heroku Dev Center (Salesforce)
    url: https://devcenter.heroku.com/articles/herokuconnect
    type: official-docs
    accessed: 2026-11-13
  - id: s3
    title: "Heroku External Objects"
    publisher: Heroku Dev Center (Salesforce)
    url: https://devcenter.heroku.com/articles/heroku-external-objects
    type: official-docs
    accessed: 2026-11-13
  - id: s4
    title: "Heroku AppLink"
    publisher: Heroku Dev Center (Salesforce)
    url: https://devcenter.heroku.com/articles/heroku-applink
    type: official-docs
    accessed: 2026-11-13
  - id: s5
    title: "AppLink Architecture Overview (Heroku AppLink Integrations)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/zh-CN/content/learn/modules/heroku-applink-integrations/applink-architecture-overview
    type: official-learning
    accessed: 2026-11-13
  - id: s6
    title: "An Update on Heroku"
    publisher: Heroku Blog (Salesforce)
    url: https://heroku.com/blog/an-update-on-heroku
    type: official-blog
    accessed: 2026-11-13
created: 2026-11-13
---

# Heroku

Heroku is Salesforce's general-purpose platform as a service. Developers push source code plus a dependency manifest, and Heroku builds and runs it in isolated, virtualized Unix containers called **dynos**, supporting Ruby, Node.js, Java, Python, Clojure, Scala, Go, PHP and .NET.[^s1] Where the core Salesforce Platform runs metadata-driven Apex inside a multitenant org, Heroku runs ordinary application processes that the customer writes and scales, and add-ons connect them back to Salesforce data.[^s1][^s5]

## How it works

An app is source code, a dependency file (such as `package.json` or `requirements.txt`) and, optionally, a **Procfile** that declares named process types such as `web` and `worker`, each scaled on its own.[^s1] **Buildpacks** turn the source into a build artifact: classic buildpacks produce a *slug* (the Cedar generation), while Cloud Native Buildpacks produce an OCI image (the Fir generation).[^s1] Deployment is usually a `git push`, though GitHub integration and the Heroku API also work.[^s1]

A **release** combines the build artifact, **config vars** (environment variables for credentials and service URLs) and attached **add-ons**. Releases form an append-only ledger, so any change creates a new release that can be rolled back.[^s1] The dyno manager restarts failed dynos and cycles every dyno at least daily. HTTP routers spread traffic randomly across `web` dynos, and Logplex merges log streams into one real-time feed.[^s1] Add-ons such as Heroku Postgres or Key-Value Store are the usual way for dynos to share state.[^s1]

## Salesforce integration

- **Heroku Connect** syncs chosen Salesforce objects with Heroku Postgres tables, read-only or read-write per object, writing Postgres changes back to Salesforce.[^s2]
- **Heroku External Objects** wraps a Heroku Connect database in OData, so `kt:salesforce-connect` can show Postgres rows in Salesforce as external objects without copying them.[^s3]
- **Heroku AppLink** (formerly Heroku Integration) publishes Heroku APIs as External Services, callable from Apex, Flow, Data Cloud and Agentforce.[^s4]

AppLink's Node.js and Python SDKs can run in user mode, which applies the calling user's permissions, field-level security and sharing. They can also run as a designated named user, for system-level work such as batch jobs.[^s5][^s4] On publish, AppLink adds the app's APIs to the API Catalog and generates Agentforce agent actions. A service-mesh buildpack then rejects requests that don't come from connected orgs.[^s4]

## Limits and gotchas

- **Ephemeral filesystem.** Each dyno's local disk is scratch space that other dynos can't see, and it is wiped on restart, daily cycling or deploy. Durable state belongs in a database or queue.[^s1]
- **Eco dynos sleep.** After 30 minutes of inactivity they sleep, so the next request waits a few seconds.[^s1]
- **Heroku Connect plans.** The `demo` plan caps sync at 10,000 rows across all mappings, with a 10-minute minimum polling interval. The `enterprise` and `shield` plans set row allocations by contract.[^s2]
- **Integration users.** Give each Connect add-on its own integration user with API Enabled. Salesforce allows 10 concurrent queries per user and 5 OAuth tokens per integration user by default.[^s2]
- **External Objects throttling.** Paid plans allow 20,000 OData requests per hour and `demo` allows 1,000. Queries must finish within 20 seconds, and results page 50 records at a time.[^s3]
- **External Objects gaps.** The data isn't available in standard reports. Batch Apex and External Change Data Capture aren't supported.[^s3]
- **AppLink region.** AppLink currently runs only in the `virginia` region, which adds latency for apps hosted far from it.[^s4]

## Product direction

On 6 February 2026 Heroku said it is moving to a **sustaining-engineering model**, prioritizing stability, security, reliability and support over new features.[^s6] New customers can no longer sign Enterprise Account contracts. Existing Enterprise subscriptions are honored and can renew, and credit-card customers see no pricing change.[^s6] The announcement said Heroku remains an actively supported, production-ready platform, and that apps, pipelines, teams and add-ons are unaffected.[^s6] Architects choosing Heroku for new work should weigh this roadmap signal alongside its fit.

## When to use it (and when not)

Heroku suits work that doesn't fit inside an org: high-volume consumer-facing apps, long-running or compute-heavy processing, and code in languages other than Apex.[^s5] Heroku Connect can serve such apps from Postgres, which Trailhead says reduces the impact of API limits on core Salesforce operations.[^s5] Logic that is mostly declarative, record-centric and well within platform limits usually belongs on the core platform instead.

## Connections

Heroku is an instance of `kt:platform-as-a-service` and the companion to the multitenant `kt:salesforce-platform`.[^s1] It **has parts** `kt:heroku-connect` and `kt:heroku-applink`, the add-ons that bridge it to orgs.[^s2][^s4] It **integrates with** `kt:salesforce-connect` through Heroku External Objects.[^s3] It also integrates with `kt:agentforce`, because AppLink generates agent actions from Heroku APIs.[^s4] It **mitigates** `kt:api-request-limits` when Heroku Connect lets high-volume apps read synced data from Postgres instead of calling Salesforce APIs.[^s5]

## Sources
[^s1]: Heroku Dev Center, "How Heroku Works". https://devcenter.heroku.com/articles/how-heroku-works (accessed 2026-11-13)
[^s2]: Heroku Dev Center, "Heroku Connect". https://devcenter.heroku.com/articles/herokuconnect (accessed 2026-11-13)
[^s3]: Heroku Dev Center, "Heroku External Objects". https://devcenter.heroku.com/articles/heroku-external-objects (accessed 2026-11-13)
[^s4]: Heroku Dev Center, "Heroku AppLink". https://devcenter.heroku.com/articles/heroku-applink (accessed 2026-11-13)
[^s5]: Trailhead, "AppLink Architecture Overview". https://trailhead.salesforce.com/zh-CN/content/learn/modules/heroku-applink-integrations/applink-architecture-overview (accessed 2026-11-13)
[^s6]: Heroku Blog, "An Update on Heroku". https://heroku.com/blog/an-update-on-heroku (accessed 2026-11-13)
