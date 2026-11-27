---
id: kt:salesforce-hosted-mcp-servers
type: Feature
title: Salesforce Hosted MCP Servers
aliases: [Hosted MCP Servers, Salesforce MCP Servers, Salesforce-hosted MCP servers]
domain: integration
summary: >-
  Fully managed Model Context Protocol (MCP) server endpoints run by Salesforce that expose org data, Apex, flows,
  APIs, prompt templates and product capabilities as tools to external MCP clients, with every call running as the
  OAuth-authenticated user.
release: "Winter '27"
status: current
broader: [kt:integration-patterns]
related: [kt:model-context-protocol-in-agentforce, kt:tableau-next, kt:data-cloud, kt:prompt-builder, kt:agent-script]
relations:
  - {predicate: implements, object: kt:model-context-protocol}
  - {predicate: dependsOn, object: kt:external-client-apps}
  - {predicate: dependsOn, object: kt:oauth-scopes}
  - {predicate: dependsOn, object: kt:field-level-security}
  - {predicate: dependsOn, object: kt:salesforce-sharing-model}
  - {predicate: integratesWith, object: kt:autolaunched-flow}
sources:
  - id: s1
    title: "Salesforce Hosted MCP Servers: Get Started"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html
    type: official-docs
    accessed: 2026-11-27
  - id: s2
    title: "Salesforce Hosted MCP Servers Are Now Generally Available"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2026/04/salesforce-hosted-mcp-servers-are-now-generally-available
    type: official-blog
    accessed: 2026-11-27
  - id: s3
    title: "Salesforce Hosted MCP Servers Are in Beta Today"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2025/10/salesforce-hosted-mcp-servers-are-in-beta-today
    type: official-blog
    accessed: 2026-11-27
  - id: s4
    title: "Build Custom MCP Servers"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/custom-servers.html
    type: official-docs
    accessed: 2026-11-27
  - id: s5
    title: "Products Supporting MCP"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/products-supporting-mcp.html
    type: official-docs
    accessed: 2026-11-27
  - id: s6
    title: "The Salesforce Developer's Guide to the Winter '27 Release"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2026/10/developers-guide-to-the-winter-27-release
    type: official-blog
    accessed: 2026-11-27
created: 2026-11-27
---

# Salesforce Hosted MCP Servers

Salesforce Hosted MCP Servers are MCP endpoints that Salesforce runs for you. They let any MCP-compatible client, such as Claude, ChatGPT, Cursor or a custom agent, reach an org's data and automation through the open Model Context Protocol. Salesforce describes them as a universal connector: an admin configures a server once in Salesforce, and clients connect with standard OAuth.[^s1] They went into beta in October 2025, after a pilot earlier that year.[^s3] Salesforce announced general availability on April 29, 2026, for Enterprise Edition orgs and above. The beta post had targeted February 2026.[^s2][^s3]

## How it works

Salesforce provisions and runs the servers, so there is no infrastructure to deploy or scale.[^s2] Setup has three steps. First, enable a server in Setup through API Catalog. Second, create an External Client App with the `mcp_api` and `refresh_token` OAuth scopes. Third, point a client at the server URL. Salesforce suggests testing in Postman before connecting Claude or ChatGPT.[^s2] Each user authenticates with OAuth 2.0 and PKCE.[^s1] The `mcp_api` scope grants MCP access only. It does not open the existing REST APIs to the client app.[^s2]

The security model is the platform's own. Every transaction runs as the authenticated user, not as an anonymous service account. CRUD permissions, field-level security and sharing rules all apply, and the audit trail records the user's name.[^s2] Servers are secure by default, which means each one has to be enabled explicitly.[^s2]

## Standard and custom servers

Standard servers are preconfigured by Salesforce. They are disabled by default and can't be edited.[^s4] They cover SObject access, Data 360 SQL, Tableau Next analytics and prompt templates from Prompt Builder. How well a client supports prompts depends on the client.[^s5] The SObject access tools come as four separate servers, so you can grant only the access a use case needs:[^s5]

- `platform/sobject-all`: create, read, update and delete records, plus query and search.[^s5]
- `platform/sobject-reads`: read and query only. Salesforce recommends this server as a first deployment.[^s2][^s5]
- `platform/sobject-mutations`: create and update records, with no delete.[^s5]
- `platform/sobject-deletes`: delete only.[^s5]

Custom servers do two things. They combine tools from several standard servers under one URL, and they expose your own logic as tools, which standard servers can't do because they are immutable.[^s4] A custom tool can be built from an autolaunched flow, an `@InvocableMethod` Apex action, an `@AuraEnabled` Apex method, an `@RestResource` Apex REST class, or an API listed in API Catalog.[^s4] Named Query APIs can also back custom tools.[^s2] Configuring a server takes no code. You can scope a server to one persona, and Metadata API deploys it from sandbox to production. Each custom server has its own URL, so you don't need extra connected apps or orgs.[^s4]

## Limits and gotchas

- **Tool count:** the docs give no numeric cap. They warn that AI clients start choosing tools poorly beyond a few dozen, so keep each server focused.[^s4]
- **Descriptions matter:** the client picks tools by their names and descriptions, so write them for the model.[^s4]
- **API Catalog coverage:** only some product-specific Connect API endpoints are in API Catalog, and customers can't author Connect APIs of their own.[^s4][^s5]
- **Packaging:** managed packages can't include MCP server configurations yet. ISVs ship the underlying flows and Apex, and subscribers configure the server after install.[^s4]
- **Pricing:** the beta post said pricing would be announced later and was subject to change. The pages opened for this article don't state rate limits or prices, so check current terms.[^s3][^s2]

## What changed in Winter '27

Winter '27 makes MCP work in both directions. You can expose an Agentforce agent as a tool on a custom hosted server. Only agents built with Agent Script qualify, and the call runs as the authenticated user.[^s6] The same release lets admins activate hosted servers for Agentforce, not only for external clients, through API Catalog.[^s6]

## When to use it (and when not)

Use hosted servers when a user's own AI assistant or an external agent needs governed, per-user access to Salesforce. Because they inherit the user's permissions, they avoid the over-privileged integration users that custom connectors often need.[^s2] For system-to-system integration with no AI client in the loop, REST, Bulk or event APIs are still the direct route. MuleSoft's AI Gateway can sit in front of the servers when you need centralized MCP governance.[^s2] For developer workflows on a local machine, Salesforce points to the separate Salesforce DX MCP Server.[^s3]

## Connections

Hosted servers implement `kt:model-context-protocol` on the server side. They are the outbound counterpart to `kt:model-context-protocol-in-agentforce`, the client that brings external tools into agents. In Winter '27 that client can also consume hosted servers.[^s6] Authentication depends on `kt:external-client-apps` and the `mcp_api` entry in `kt:oauth-scopes`.[^s2] Data access is subject to `kt:field-level-security` and the `kt:salesforce-sharing-model`.[^s5] Custom tools reuse `kt:autolaunched-flow`, `kt:apex-rest-services` and `kt:prompt-builder` assets.[^s4][^s5] Product servers surface `kt:data-cloud` SQL and `kt:tableau-next` analytics, and `kt:agent-script` agents can be exposed as tools.[^s5][^s6]

## Sources
[^s1]: Salesforce Developers, "Salesforce Hosted MCP Servers: Get Started". https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html (accessed 2026-11-27)
[^s2]: Salesforce Developers Blog, "Salesforce Hosted MCP Servers Are Now Generally Available". https://developer.salesforce.com/blogs/2026/04/salesforce-hosted-mcp-servers-are-now-generally-available (accessed 2026-11-27)
[^s3]: Salesforce Developers Blog, "Salesforce Hosted MCP Servers Are in Beta Today". https://developer.salesforce.com/blogs/2025/10/salesforce-hosted-mcp-servers-are-in-beta-today (accessed 2026-11-27)
[^s4]: Salesforce Developers, "Build Custom MCP Servers". https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/custom-servers.html (accessed 2026-11-27)
[^s5]: Salesforce Developers, "Products Supporting MCP". https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/products-supporting-mcp.html (accessed 2026-11-27)
[^s6]: Salesforce Developers Blog, "The Salesforce Developer's Guide to the Winter '27 Release". https://developer.salesforce.com/blogs/2026/10/developers-guide-to-the-winter-27-release (accessed 2026-11-27)
