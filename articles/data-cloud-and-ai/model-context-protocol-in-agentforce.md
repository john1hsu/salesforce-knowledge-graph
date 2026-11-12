---
id: kt:model-context-protocol-in-agentforce
type: Feature
title: MCP for Agentforce
aliases: [Model Context Protocol in Agentforce, Agentforce MCP client, Agentforce MCP Support, native MCP client in Agentforce]
domain: data-cloud-and-ai
summary: >-
  Agentforce's native Model Context Protocol (MCP) client, which lets admins register external or Salesforce-hosted
  MCP servers in Agentforce Registry or API Catalog and turn allowlisted server tools into agent actions governed
  by Agentforce Gateway policies.
release: "Winter '27"
status: current
broader: [kt:agentforce]
related: [kt:agent-actions, kt:salesforce-hosted-mcp-servers, kt:agentexchange, kt:mulesoft-anypoint-platform]
relations:
  - {predicate: implements, object: kt:model-context-protocol}
  - {predicate: dependsOn, object: kt:named-credentials}
  - {predicate: dependsOn, object: kt:einstein-trust-layer}
  - {predicate: enables, object: kt:agent-actions}
  - {predicate: integratesWith, object: kt:salesforce-hosted-mcp-servers}
sources:
  - id: s1
    title: "Discover MCP for Agentforce (MCP for Agentforce: Quick Look)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/mcp-for-agentforce-quick-look/discover-mcp-for-agentforce
    type: official-learning
    accessed: 2026-11-12
  - id: s2
    title: "Summer '26 Release Architect Highlights: Sharing, Security, and Agentic Integration"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/summer-26-release-architect-highlights/
    type: official-blog
    accessed: 2026-11-12
  - id: s3
    title: "MCP for Agentforce Metadata in Managed Packages"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/pkg2-dev/guide/dev2gp-package-mcp-agentforce.html
    type: official-docs
    accessed: 2026-11-12
  - id: s4
    title: "MCP Solutions for Developers"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/mcp.html
    type: official-docs
    accessed: 2026-11-12
  - id: s5
    title: "Introducing MCP Support Across Salesforce"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/06/introducing-mcp-support-across-salesforce
    type: official-blog
    accessed: 2026-11-12
  - id: s6
    title: "Model Context Protocol Specification (2025-11-25): Architecture"
    publisher: Model Context Protocol
    url: https://modelcontextprotocol.io/specification/2025-11-25/architecture
    type: standards-body
    accessed: 2026-11-12
created: 2026-11-12
---

# MCP for Agentforce

MCP for Agentforce is the native Model Context Protocol client built into Agentforce. It connects an agent to one or more MCP servers so the agent can call the tools those servers expose against external systems, and it gives admins one place to register and manage those servers.[^s1] Salesforce first announced the client as a pilot for the July 2025 release, alongside a central registry with security, rate-limiting and access policies.[^s5] By the Summer '26 release it was described as generally available.[^s2]

## How MCP works

MCP is an open protocol built on JSON-RPC with a client-host-server design. A host application creates one client per server, and each client keeps an isolated, stateful session with its server. Servers expose tools, resources and prompts, and the two sides declare the capabilities they support when the session starts.[^s6] The specification keeps the full conversation with the host and does not let a server see into other servers. That is why the host is where security policy and consent are enforced.[^s6] In Agentforce's case, Agentforce is the host, so MCP traffic sits inside the same security and compliance boundary as the rest of the platform.[^s1]

## How it works in Agentforce

1. **Register the server.** External and third-party servers go in Agentforce Registry. MuleSoft servers and Salesforce standard or custom servers go through API Catalog.[^s1] Admins can also add servers listed on AgentExchange to the registry.[^s2]
2. **Choose authentication.** The registration supports OAuth 2.0, external (named) credentials, or no authentication.[^s1]
3. **Allowlist tools.** Admins pick which of the server's tools to enable. The allowlisted tools become agent actions, and admins then write reasoning instructions that tell each agent when to use them.[^s1][^s2]
4. **Govern usage.** Agentforce Gateway policies set which agents may use which tools and can cap how often an agent calls a tool within a set period.[^s1][^s2]

Under the hood, a registration is ordinary metadata. An ExternalServiceRegistration with the schema type ModelContextProtocol holds the server definition. A NamedCredential holds the endpoint, an ExternalCredential holds the authentication principal, and a PermissionSet grants access to that principal.[^s3]

## Limits and gotchas

- **Tool drift:** if a server's tool descriptions change significantly, the registry blocks the affected action and alerts the admin.[^s2] Agentforce also detects other server-side changes and asks you to update the registration.[^s1]
- **Packaging:** ISVs can ship the four registration metadata types in managed 2GP packages, at API version 66.0 or later. MCP tool actions and Gateway policies can't be packaged yet, so subscribers have to create them after install.[^s3]
- **Naming:** a packaged MCP server name may contain only alphanumeric characters, and it must match across file names and file contents.[^s3]
- **Trust:** prompts and responses go through the Einstein Trust Layer and its zero data retention policy. You still decide which server tools agents can reach, and Salesforce data stays in Salesforce.[^s1]
- **Scope:** the sources opened for this article give no numeric caps on servers or tools per agent, so check current documentation before you design around a limit.[^s3]

## When to use it (and when not)

Use an MCP server when a capability already exists behind one. Examples include a vendor's server, a MuleSoft API converted to MCP, or a Heroku-hosted custom server.[^s5] This avoids building a separate custom action for every external operation, because one registration can expose many tools.[^s1] For logic that lives inside the org, standard and custom agent actions (flows, Apex, prompt templates) remain the direct route. MCP adds a protocol hop and a separate governance layer that internal logic doesn't need.[^s1][^s3]

## Connections

MCP for Agentforce implements the open `kt:model-context-protocol` inside `kt:agentforce`. Its main output is new `kt:agent-actions`, since allowlisted tools become actions.[^s2] Authentication relies on `kt:named-credentials` and external credentials, and runtime trust comes from the `kt:einstein-trust-layer`.[^s3][^s1] Servers come from `kt:agentexchange`, `kt:mulesoft-anypoint-platform` and Heroku, among other sources.[^s5][^s2] It is the inbound counterpart to `kt:salesforce-hosted-mcp-servers`, which expose Salesforce data and automation to MCP clients outside Salesforce. Salesforce lists both in its catalog of MCP solutions.[^s4]

## Sources
[^s1]: Trailhead, "Discover MCP for Agentforce (MCP for Agentforce: Quick Look)". https://trailhead.salesforce.com/content/learn/modules/mcp-for-agentforce-quick-look/discover-mcp-for-agentforce (accessed 2026-11-12)
[^s2]: Salesforce, "Summer '26 Release Architect Highlights: Sharing, Security, and Agentic Integration". https://www.salesforce.com/blog/summer-26-release-architect-highlights/ (accessed 2026-11-12)
[^s3]: Salesforce Developers, "MCP for Agentforce Metadata in Managed Packages". https://developer.salesforce.com/docs/platform/pkg2-dev/guide/dev2gp-package-mcp-agentforce.html (accessed 2026-11-12)
[^s4]: Salesforce Developers, "MCP Solutions for Developers". https://developer.salesforce.com/docs/ai/agentforce/guide/mcp.html (accessed 2026-11-12)
[^s5]: Salesforce Developers Blog, "Introducing MCP Support Across Salesforce". https://developer.salesforce.com/blogs/2025/06/introducing-mcp-support-across-salesforce (accessed 2026-11-12)
[^s6]: Model Context Protocol, "Specification (2025-11-25): Architecture". https://modelcontextprotocol.io/specification/2025-11-25/architecture (accessed 2026-11-12)
