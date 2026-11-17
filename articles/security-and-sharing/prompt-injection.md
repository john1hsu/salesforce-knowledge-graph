---
id: kt:prompt-injection
type: Concept
title: Prompt Injection
aliases: [prompt injection attack, direct prompt injection, indirect prompt injection, LLM prompt injection, LLM01]
domain: security-and-sharing
summary: >-
  An attack on LLM-based applications in which crafted input, typed by a user or hidden in data the model reads,
  changes the model's behaviour against its instructions. In Salesforce it threatens Agentforce agents and prompt
  templates that merge untrusted record data, and is mitigated in layers rather than prevented outright.
release: "Winter '27"
status: concept
broader: [kt:secure-coding]
related: [kt:einstein-trust-layer, kt:agentforce, kt:prompt-builder, kt:retrieval-augmented-generation-in-salesforce, kt:agentexchange]
relations:
  - {predicate: causes, object: kt:data-breach-risk}
  - {predicate: contrastsWith, object: kt:soql-injection}
sources:
  - id: s1
    title: "Secure Your Agentforce Prompts"
    publisher: Salesforce Developers (ISVforce Guide)
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/secure-agentforce-prompts.html
    type: official-docs
    accessed: 2026-11-17
  - id: s2
    title: "Design Security-Hardened Prompts"
    publisher: Salesforce Developers (ISVforce Guide)
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/secure-agentforce-prompt-injection-harden.html
    type: official-docs
    accessed: 2026-11-17
  - id: s3
    title: "Use Random Sequence Enclosures and Prompt Sandwiching"
    publisher: Salesforce Developers (ISVforce Guide)
    url: https://developer.salesforce.com/docs/platform/isvforce/guide/secure-agentforce-prompt-injection-enclosure.html
    type: official-docs
    accessed: 2026-11-17
  - id: s4
    title: "Inside the Einstein Trust Layer"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2023/10/inside-the-einstein-trust-layer
    type: official-blog
    accessed: 2026-11-17
  - id: s5
    title: "NIST AI 100-2 E2025: Adversarial Machine Learning — A Taxonomy and Terminology of Attacks and Mitigations"
    publisher: NIST
    url: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf
    type: standards-body
    accessed: 2026-11-17
  - id: s6
    title: "LLM01:2025 Prompt Injection"
    publisher: OWASP Gen AI Security Project
    url: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
    type: community
    accessed: 2026-11-17
created: 2026-11-17
---

# Prompt Injection

Prompt injection is a vulnerability in applications built on large language models: input that the model parses changes its behaviour or output in ways the builder never intended, even when that input is invisible to a human reader.[^s6] OWASP ranks it first (LLM01) in its 2025 Top 10 for LLM applications.[^s6] Salesforce's ISV guidance describes the same risk in Agentforce terms: attacker-controlled text inside a prompt can make the LLM leak data, generate unauthorized data or produce harmful content.[^s1]

## Direct and indirect forms

NIST's adversarial machine learning taxonomy separates two forms.[^s5] In **direct** prompt injection, the attacker is the system's own user and appends instructions that try to override higher-trust instructions such as the system prompt.[^s5] In **indirect** prompt injection, the attacker never talks to the application; instead they plant instructions in a resource the system later ingests, such as a document or web page, so a third party mounts the attack and the legitimate user usually bears the harm.[^s5] OWASP treats jailbreaking as a subtype of prompt injection, one aimed at making the model ignore its safety protocols altogether.[^s6]

For a Salesforce org the indirect form is the one practitioners underestimate. Any record field, email, case comment or knowledge article that a prompt template merges in, or that an agent retrieves for grounding, is untrusted data. OWASP notes that research shows retrieval-augmented generation does not by itself remove the risk, since a tampered document in the retrieval store can steer the answer.[^s6]

## Impact

OWASP lists the consequences: disclosure of sensitive data or of the system prompt, biased or incorrect output, unauthorized use of functions the model can reach, arbitrary commands in connected systems, and manipulated decisions.[^s6] For agents the function-access impact matters most, because an injected instruction can trigger actions that read or change CRM records on the running user's behalf.[^s6]

## Mitigations

Neither standards body claims a complete fix. NIST reports that current models remain highly vulnerable to direct injection and that detectors can themselves be attacked, while OWASP says fool-proof prevention may not exist and aims instead at limiting impact.[^s5][^s6] Defences are therefore layered:

- **Harden the prompt.** Salesforce advises giving the model a role, bounding which topics it may answer, defining the expected output, and stating that untrusted data cannot override the instructions.[^s2]
- **Separate data from instructions.** Wrap untrusted input in a random-sequence enclosure, a fresh, securely generated token per inference, rather than quote-style delimiters that attackers can easily close.[^s3]
- **Sandwich the instructions.** Repeat the instructions after the untrusted data as well as before it, so the last thing the model reads is the developer's intent.[^s3]
- **Validate and filter.** Check user-controlled data before merging it, and apply input and output filtering plus deterministic validation of output formats.[^s1][^s6]
- **Limit privilege and add a human.** Keep privileged operations in code under least privilege, and require human approval for high-risk actions.[^s6]
- **Test adversarially.** Red-team the application regularly, treating the model as an untrusted user.[^s5][^s6]

## How Salesforce applies it

At platform level, the **Einstein Trust Layer** applies prompt-defense heuristics, such as instruction defense, after data masking, and appends post-prompting instructions intended to guard against injection; it also scores responses for toxicity and logs prompts and outputs to an audit trail.[^s4] These help but do not replace application-level design, which is why Salesforce makes injection mitigation an explicit requirement for partners. Every Agentforce solution listed on AgentExchange that ships prompts must guard them against injection whenever they include user-controlled or untrusted input, combining techniques as needed, and Salesforce describes the field as still evolving.[^s1] The same guidance bars secrets in packaged prompts and limits where packaged prompts may be stored to prompt templates, protected custom settings and protected custom metadata.[^s1]

## Connections

Prompt injection sits **broader** under **secure coding** as the LLM-era member of the injection family, and it **contrasts with SOQL injection**: both treat untrusted input as instructions, but SOQL injection rewrites a database query while prompt injection rewrites a model's task.[^s6] It **causes data-breach risk** through leaked prompts and data or misused agent actions.[^s6] The **Einstein Trust Layer** mitigates it with prompt defense, and **Agentforce** and **Prompt Builder** templates are the main surfaces that need hardening.[^s1][^s4] **Retrieval-augmented generation** is related because grounding content is a channel for indirect injection.[^s5][^s6] **AgentExchange** is related because its security review enforces the partner prompt requirements.[^s1]

## Sources
[^s1]: Salesforce Developers, "Secure Your Agentforce Prompts", ISVforce Guide. https://developer.salesforce.com/docs/platform/isvforce/guide/secure-agentforce-prompts.html (accessed 2026-11-17)
[^s2]: Salesforce Developers, "Design Security-Hardened Prompts", ISVforce Guide. https://developer.salesforce.com/docs/platform/isvforce/guide/secure-agentforce-prompt-injection-harden.html (accessed 2026-11-17)
[^s3]: Salesforce Developers, "Use Random Sequence Enclosures and Prompt Sandwiching", ISVforce Guide. https://developer.salesforce.com/docs/platform/isvforce/guide/secure-agentforce-prompt-injection-enclosure.html (accessed 2026-11-17)
[^s4]: Stephan Chandler-Garcia, "Inside the Einstein Trust Layer", Salesforce Developers Blog, 2023-10-06. https://developer.salesforce.com/blogs/2023/10/inside-the-einstein-trust-layer (accessed 2026-11-17)
[^s5]: NIST, "AI 100-2 E2025: Adversarial Machine Learning — A Taxonomy and Terminology of Attacks and Mitigations". https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf (accessed 2026-11-17)
[^s6]: OWASP Gen AI Security Project, "LLM01:2025 Prompt Injection". https://genai.owasp.org/llmrisk/llm01-prompt-injection/ (accessed 2026-11-17)
