---
id: kt:anypoint-runtime-manager
type: Tool
title: Anypoint Runtime Manager
aliases: [Runtime Manager, MuleSoft Runtime Manager, ARM]
domain: integration
summary: >-
  The Anypoint Platform console for deploying, operating and monitoring Mule applications and servers across
  sandbox, staging and production environments, whether they run on CloudHub, CloudHub 2.0, Runtime Fabric or
  customer-hosted (hybrid) Mule runtimes.
release: "Winter '27"
status: current
broader: [kt:mulesoft-anypoint-platform]
related: [kt:mule-runtime-engine, kt:api-led-connectivity, kt:cloudhub-2, kt:runtime-fabric, kt:anypoint-monitoring]
relations:
  - {predicate: partOf, object: kt:mulesoft-anypoint-platform}
  - {predicate: integratesWith, object: kt:mule-runtime-engine}
  - {predicate: dependsOn, object: kt:runtime-manager-agent}
sources:
  - id: s1
    title: "Anypoint Runtime Manager"
    publisher: MuleSoft (Salesforce)
    url: https://docs.mulesoft.com/runtime-manager/
    type: official-docs
    accessed: 2026-11-25
  - id: s2
    title: "Servers"
    publisher: MuleSoft (Salesforce)
    url: https://docs.mulesoft.com/runtime-manager/servers-about
    type: official-docs
    accessed: 2026-11-25
  - id: s3
    title: "Creating and Deploying Mule Apps"
    publisher: MuleSoft (Salesforce)
    url: https://docs.mulesoft.com/control-planes/creating-and-deploying-mule-apps
    type: official-docs
    accessed: 2026-11-25
  - id: s4
    title: "Explore Deployment Models for Mule Applications (Anypoint Platform Deployment and Management of APIs)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/anypoint-platform-deployment-and-management-of-apis/learn-deployment-models-for-mule-applications
    type: official-learning
    accessed: 2026-11-25
created: 2026-11-25
---

# Anypoint Runtime Manager

Anypoint Runtime Manager is the part of MuleSoft Anypoint Platform that gives operations teams one view of their Mule applications, servers and APIs. From it you deploy, manage and monitor applications in sandbox, staging or production environments, whether those applications run in the cloud or on premises.[^s1] Trailhead describes it as the central tool for operating deployed applications: viewing logs, configuring alerts, restarting apps, scaling workers and promoting apps from one environment to the next.[^s4]

## How it works

Runtime Manager is a control-plane tool. It does not run integrations itself. It tells a runtime plane where and how to run Mule applications, and the Mule runtime engine executes them. The documentation describes four deployment scenarios:[^s1]

- **CloudHub**: MuleSoft-hosted runtimes, with Insight for analytics and monitoring.[^s1]
- **Hybrid**: Mule servers you run yourself (on premises or in your own cloud), registered with and managed from the cloud console. Government Cloud customers use their Government Cloud control plane.[^s1]
- **Anypoint Platform Private Cloud Edition**: an on-premises copy of Runtime Manager that can deploy to any target except CloudHub.[^s1]
- **Anypoint Runtime Fabric**: a customer-hosted Runtime Fabric instance managed from the cloud console.[^s1]

CloudHub 2.0 is the container-based successor to CloudHub. Each app runs in its own container, can scale automatically, can run multiple replicas and recovers from failures. The original CloudHub is a fully managed, multitenant iPaaS that is still widely used and supported.[^s4] The control-plane documentation calls Runtime Manager the hub for CloudHub, CloudHub 2.0, Runtime Fabric and Hybrid Standalone.[^s3]

For hybrid deployments, Runtime Manager manages each Mule runtime instance as a **server**. Servers talk to Runtime Manager through the Runtime Manager agent. You can manage servers one at a time or combine them into **server groups** or **clusters** for redundancy, high availability and simpler administration. Every Mule instance you want to manage needs its own server entry.[^s2]

## Control planes and runtime availability

Anypoint organizations live in a single control plane. The documentation lists US, EU, Canada, Japan, India, Australia and United Kingdom clouds. Which runtime targets you can use depends on the control plane:[^s3]

- CloudHub 2.0 is available in every listed commercial cloud. The original CloudHub is available only in the US and EU control planes.[^s3]
- Runtime Fabric is available in every listed cloud, but Canada, Japan, India and Australia need an account manager to enable it.[^s3]
- Hybrid Standalone is available everywhere, as long as the Runtime Manager agent is registered with the control plane that holds the organization.[^s3]

## Limits and gotchas

- **Deployment tooling differs by target.** Anypoint Studio, Anypoint Code Builder, the Mule Maven plugin, Anypoint CLI and REST APIs can all deploy, with restrictions. Studio deploys directly only to CloudHub; CloudHub 2.0, Runtime Fabric and hybrid targets go through Runtime Manager.[^s3]
- **Hybrid servers must register with the right control plane.** An agent registered with a different control plane than the organization's will not be managed.[^s3]
- **Private Cloud Edition cannot target CloudHub**, so a fully on-premises platform also needs an on-premises runtime plane.[^s1]
- **Operations spans several tools.** After deployment, Runtime Manager handles start, stop, update, delete, logs, properties, schedules and alerts. Deeper observability, API policies, secrets and usage reporting are handled by Anypoint Monitoring, API Manager, Secrets Manager and Usage Reports.[^s3]

## When to use it (and when not)

Use Runtime Manager to run Mule applications as a governed estate: promoting builds through environments, scaling workers or replicas, setting alerts and checking logs in one place.[^s4] For new MuleSoft-hosted workloads, CloudHub 2.0 is the default choice for its container isolation and automatic scaling. Teams that must keep runtimes on their own infrastructure choose Runtime Fabric or hybrid servers and still manage them from the same console.[^s1][^s4]

## Connections

Runtime Manager is part of the `kt:mulesoft-anypoint-platform` and acts as the control plane for the `kt:mule-runtime-engine`, which is configured through it.[^s1][^s3] Its deployment targets `kt:cloudhub-2` and `kt:runtime-fabric`, and its hybrid link through the Runtime Manager agent, determine where the System, Process and Experience APIs of `kt:api-led-connectivity` actually run.[^s2][^s4] `kt:anypoint-monitoring` supplements its built-in logs and alerts.[^s3]

## Sources
[^s1]: MuleSoft (Salesforce), "Anypoint Runtime Manager". https://docs.mulesoft.com/runtime-manager/ (accessed 2026-11-25)
[^s2]: MuleSoft (Salesforce), "Servers". https://docs.mulesoft.com/runtime-manager/servers-about (accessed 2026-11-25)
[^s3]: MuleSoft (Salesforce), "Creating and Deploying Mule Apps". https://docs.mulesoft.com/control-planes/creating-and-deploying-mule-apps (accessed 2026-11-25)
[^s4]: Trailhead, "Explore Deployment Models for Mule Applications". https://trailhead.salesforce.com/content/learn/modules/anypoint-platform-deployment-and-management-of-apis/learn-deployment-models-for-mule-applications (accessed 2026-11-25)
