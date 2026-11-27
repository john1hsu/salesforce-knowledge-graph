---
id: kt:model-context-protocol
type: ExternalConcept
title: Model Context Protocol (MCP)
aliases: [MCP, Model Context Protocol, MCP specification, MCP standard]
domain: integration
summary: >-
  An open, JSON-RPC 2.0 based protocol, governed under the Linux Foundation's Agentic AI Foundation, through which
  AI applications (clients) call tools, read resources and use prompts exposed by servers; Salesforce both consumes
  it (Agentforce as an MCP client) and provides it (Salesforce Hosted MCP Servers, DX MCP Server).
release: "Winter '27"
status: concept
broader: [kt:integration-patterns, kt:generative-ai]
related: [kt:model-context-protocol-in-agentforce, kt:salesforce-hosted-mcp-servers, kt:agentforce-vibes-ide, kt:salesforce-dx-mcp-server]
relations:
  - {predicate: contrastsWith, object: kt:agent-to-agent-protocol}
  - {predicate: dependsOn, object: kt:oauth-2-0}
  - {predicate: consumedBy, object: kt:mulesoft-anypoint-platform}
  - {predicate: consumedBy, object: kt:heroku}
  - {predicate: enables, object: kt:agent-actions}
sources:
  - id: s1
    title: "Model Context Protocol Specification: Overview (Base Protocol)"
    publisher: Model Context Protocol
    url: https://modelcontextprotocol.io/specification/latest/basic/index
    type: standards-body
    accessed: 2026-11-27
  - id: s2
    title: "Model Context Protocol Specification: Key Changes (Changelog)"
    publisher: Model Context Protocol
    url: https://modelcontextprotocol.io/specification/latest/changelog
    type: standards-body
    accessed: 2026-11-27
  - id: s3
    title: "MCP joins the Agentic AI Foundation"
    publisher: Model Context Protocol Blog
    url: https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/?from=bd_signal
    type: standards-body
    accessed: 2026-11-27
  - id: s4
    title: "Salesforce Hosted MCP Servers: Get Started"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html
    type: official-docs
    accessed: 2026-11-27
  - id: s5
    title: "MCP Solutions for Developers"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/ai/agentforce/guide/mcp.html
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

# Model Context Protocol (MCP)

The Model Context Protocol is an open standard that defines how an AI application talks to external capability providers. The application acts as the client, and each provider runs an MCP server that offers tools to call, resources to read and prompts to reuse.[^s1] Because the wire format is shared, one server can serve any compliant client, and one client can use any compliant server. That is why Salesforce treats MCP as an integration standard rather than a product feature.[^s5]

## How the protocol works

Every MCP message is a JSON-RPC 2.0 request, response or notification. A request carries an id that is never null, a response echoes that id with either a result or an error, and a notification has no id and gets no reply.[^s1] The specification separates a mandatory core from optional parts. All implementations must support the base protocol, versioning rules and the message patterns. Authorization, the server features (resources, prompts and tools), client features such as elicitation, and utilities such as completion and pagination are optional.[^s1]

MCP runs over two families of transport: local STDIO, where the client launches the server as a subprocess, and HTTP. Authorization rules apply to the HTTP transports, which should follow the OAuth-based Authorization specification. STDIO servers should instead read credentials from their environment.[^s1]

## Versioning and recent changes

Revisions are named by date. The current revision, 2026-07-28, followed 2025-11-25 and changed the protocol a lot.[^s2] It removed the initialize handshake and protocol-level sessions. Every request now carries its protocol version and client capabilities, and servers must answer a new `server/discover` call that advertises their versions and identity.[^s1][^s2] Cross-call state is now passed as explicit handles in tool arguments instead of an `Mcp-Session-Id` header. A multi round-trip pattern, where a server returns an input-required result and the client retries with the answers, replaces server-initiated sampling, roots and elicitation requests.[^s2] The same revision deprecated roots, sampling, logging and the older HTTP+SSE transport. It also deprecated OAuth Dynamic Client Registration in favour of Client ID Metadata Documents.[^s2] In practice, check which revision a client and server both support before you assume a feature exists.[^s1]

## Governance

Anthropic introduced MCP and, on December 9, 2025, contributed it as a founding project of the Agentic AI Foundation, a fund under the Linux Foundation. The foundation's board handles budget and membership, while MCP's maintainers keep technical control. Changes still go through the specification enhancement proposal (SEP) process.[^s3] The project reported more than 10,000 active servers and over 97 million monthly SDK downloads at that time.[^s3]

## MCP in the Salesforce ecosystem

Salesforce uses MCP in both directions. Salesforce Hosted MCP Servers are managed endpoints that let external clients, including Claude, ChatGPT, Cursor and custom agents, work with org data and automation. Users sign in with per-user OAuth 2.0 and PKCE, and the tools respect field-level security and sharing rules.[^s4] Salesforce's catalogue of MCP solutions also lists the Salesforce DX MCP Server (beta), the MuleSoft MCP Server and Anypoint Connector for MCP, the Heroku MCP Server, and an MCP client in the Agentforce Vibes extension.[^s5] The Winter '27 release made this two-way. Agentforce agents can call MCP tools, and agents built with Agent Script Builder can be exposed as tools on a custom MCP server.[^s6]

## When to use it (and when not)

Choose MCP when an AI client needs governed, reusable access to a system and you would otherwise write one-off adapters for each assistant. One MCP server can be shared across many clients.[^s5] For an Agentforce agent calling logic that already lives in the org, a native agent action avoids the protocol hop. For agents delegating work to other agents, the A2A protocol fits better. MCP connects an agent to tools and data, not to a peer agent.[^s6][^s1]

## Connections

MCP sits under `kt:integration-patterns` and `kt:generative-ai`. `kt:model-context-protocol-in-agentforce` implements the client side inside Agentforce, and `kt:salesforce-hosted-mcp-servers` and `kt:salesforce-dx-mcp-server` implement the server side.[^s5][^s4] HTTP deployments depend on `kt:oauth-2-0`.[^s1][^s4] `kt:mulesoft-anypoint-platform` and `kt:heroku` both ship MCP servers or connectors.[^s5] It contrasts with `kt:agent-to-agent-protocol`, and MCP tools surface to agents as `kt:agent-actions`.[^s6]

## Sources
[^s1]: Model Context Protocol, "Specification: Overview (Base Protocol)". https://modelcontextprotocol.io/specification/latest/basic/index (accessed 2026-11-27)
[^s2]: Model Context Protocol, "Specification: Key Changes (Changelog)". https://modelcontextprotocol.io/specification/latest/changelog (accessed 2026-11-27)
[^s3]: Model Context Protocol Blog, "MCP joins the Agentic AI Foundation". https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/?from=bd_signal (accessed 2026-11-27)
[^s4]: Salesforce Developers, "Salesforce Hosted MCP Servers: Get Started". https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html (accessed 2026-11-27)
[^s5]: Salesforce Developers, "MCP Solutions for Developers". https://developer.salesforce.com/docs/ai/agentforce/guide/mcp.html (accessed 2026-11-27)
[^s6]: Salesforce Developers Blog, "The Salesforce Developer's Guide to the Winter '27 Release". https://developer.salesforce.com/blogs/2026/10/developers-guide-to-the-winter-27-release (accessed 2026-11-27)
