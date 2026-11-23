---
id: kt:javascript-developer-certification
type: Certification
title: JavaScript Developer Certification
aliases: [Salesforce Certified JavaScript Developer, JavaScript Developer I, Salesforce Certified JavaScript Developer I, JS Dev I, JS-Dev-101]
domain: development
summary: >-
  Salesforce's credential for general-purpose JavaScript skills, earned through a proctored 60-question exam on
  language fundamentals, browser and event handling, asynchronous programming, server-side JavaScript, debugging and
  testing; it has no prerequisite and is kept current with an annual Summer-cycle maintenance badge.
release: "Winter '27"
status: current
broader: [kt:salesforce-certification-program]
related: [kt:lightning-web-components, kt:platform-developer-certification, kt:platform-developer-ii-certification, kt:lightning-web-security, kt:lwc-jest-testing]
relations:
  - {predicate: alternativeTo, object: kt:platform-developer-certification}
sources:
  - id: s1
    title: "Javascript Certification - Salesforce Certified JavaScript Developer"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/javascriptdeveloper
    type: official-learning
    accessed: 2026-11-23
  - id: s2
    title: "Salesforce Certified JavaScript Developer Exam Guide"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298945&language=en_US&type=1
    type: official-learning
    accessed: 2026-11-23
  - id: s3
    title: "Salesforce Certification Maintenance Schedule"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=005298922&language=en_US&type=1
    type: official-docs
    accessed: 2026-11-23
  - id: s4
    title: "Get Started with Salesforce JavaScript Developer I Certification Prep"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/javascript-dev-i-cert-prep-variables-collections-functions-classes/get-started-with-salesforce-javascript-developer-i-certification-prep
    type: official-learning
    accessed: 2026-11-23
  - id: s5
    title: "JavaScript Developer Certification Maintenance (Summer '25)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/javascript-developer-certification-maintenance-summer-25
    type: official-learning
    accessed: 2026-11-23
  - id: s6
    title: "JavaScript Developer I Certification: Unlock new career opportunities"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/salesforce-javascript-developer-certification/
    type: official-blog
    accessed: 2026-11-23
created: 2026-11-23
---

# JavaScript Developer Certification

The Salesforce Certified JavaScript Developer credential validates general JavaScript skill rather than knowledge of Apex or platform configuration. Trailhead describes holders as people who build front-end and/or back-end JavaScript applications for the web stack and work with related technologies such as Lightning Web Components.[^s1] Unlike most Salesforce exams, the content is largely vendor-neutral: the outline covers the language itself, the browser, Node.js and testing, and the guide notes only that these skills can also be applied to building Lightning web components.[^s2]

The credential was launched as **JavaScript Developer I**, and some Trailhead study content still uses that name, while the exam guide, credential page and maintenance schedule now say simply "JavaScript Developer".[^s1][^s2][^s3][^s4] When it launched, Salesforce described a two-step journey: the proctored exam plus the Lightning Web Components Specialist superbadge.[^s6] The current exam guide lists no prerequisite and does not mention a superbadge, so check the credential page before relying on the older two-step description.[^s2][^s6]

## Who it is for

The exam guide targets candidates with one to two years of experience building front-end and/or back-end JavaScript applications for the web stack.[^s2] Trailhead's prep module lists typical roles such as JavaScript programmer, front-end developer and Salesforce developer.[^s4] It suits web developers moving onto the platform, and Salesforce developers who write a lot of component code.[^s1][^s4]

## Exam format

As stated in the exam guide checked for this article:[^s2]

- **Questions:** 60 scored multiple-choice/multiple-select questions, plus up to five unscored questions.[^s2]
- **Time:** 105 minutes.[^s2]
- **Passing score:** 65%.[^s2]
- **Fees:** US$200 to register and US$100 to retake, plus applicable taxes.[^s2]
- **Delivery:** proctored, at a testing centre or online; no hard-copy or online material may be consulted.[^s2]
- **Prerequisite:** none.[^s2]
- **Release alignment:** the guide says questions align to Summer '22, but the content is mostly standard JavaScript rather than release features.[^s2]

## Exam outline

The guide weights seven sections:[^s2][^s4]

| Section | Weight |
|---|---|
| Variables, Types, and Collections | 23%[^s2] |
| Objects, Functions, and Classes | 25% |
| Browser and Events | 17% |
| Debugging and Error Handling | 7% |
| Asynchronous Programming | 13% |
| Server Side JavaScript | 8% |
| Testing | 7%[^s2] |

The two largest sections cover declaring and initialising variables, strings, numbers and dates, type coercion and truthy/falsy evaluation, arrays and JSON, then functions, objects, classes, modules, variable scope and execution flow.[^s2] Browser objectives span events and propagation, DOM manipulation, browser developer tools and browser APIs.[^s2] Asynchronous programming centres on async concepts and the event loop. The server-side section asks candidates to pick Node.js implementations, CLI commands, core modules and package-management approaches. The testing section asks whether a given unit test is ineffective and how to fix it.[^s2]

For preparation the guide points to an official trailmix, the Study for the Salesforce JavaScript Developer Exam trail, and general references such as MDN and the Node.js API documentation.[^s2] Trailhead's prep module restates the same seven sections and weights.[^s4]

## Maintenance and gotchas

- **Summer maintenance cycle.** The credential has its own JavaScript Developer maintenance badge on the Summer cycle; the Summer '26 badge is listed as due in August 2027.[^s3]
- **Maintenance covers LWC topics.** Maintenance modules review platform updates, such as TypeScript and HTML class binding in Lightning web components in Summer '25, not just core JavaScript.[^s5]
- **Missed deadlines expire the credential.** A recently expired certification may be reinstated through a support case at Salesforce's discretion; one that lapsed more than a cycle ago must be earned again by exam.[^s3]
- **Not a substitute for Apex knowledge.** The outline has no Apex, SOQL or data-model objectives, so it does not show back-end platform skills.[^s2]

## When to pursue it

It fits developers whose daily work is component and browser code, or web developers who want a Salesforce credential that builds on what they already know.[^s1][^s2] Developers who write triggers, Apex services and integrations get more from Platform Developer and then Platform Developer II, which test platform-specific logic.[^s1][^s2]

## Connections

- **broader → `kt:salesforce-certification-program`**: one of Salesforce's developer credentials, with exam and maintenance rules from that programme.[^s1][^s3]
- **alternativeTo → `kt:platform-developer-certification`**: Trailhead shows Platform Developer as a related credential; one tests JavaScript, the other Apex and platform logic.[^s1]
- **related → `kt:platform-developer-ii-certification`**: the advanced Apex-focused path for developers who also need back-end depth.[^s1]
- **related → `kt:lightning-web-components`, `kt:lightning-web-security`**: the guide presents the skills as the basis for writing Lightning web components, which run in a sandbox with restricted DOM access.[^s2]
- **related → `kt:lwc-jest-testing`**: the Testing section asks candidates to judge and improve unit tests, the skill used when testing components with Jest.[^s2]

## Sources
[^s1]: Trailhead, "Javascript Certification - Salesforce Certified JavaScript Developer". https://trailhead.salesforce.com/credentials/javascriptdeveloper (accessed 2026-11-23)
[^s2]: Salesforce Help, "Salesforce Certified JavaScript Developer Exam Guide". https://help.salesforce.com/s/articleView?id=005298945&language=en_US&type=1 (accessed 2026-11-23)
[^s3]: Salesforce Help, "Salesforce Certification Maintenance Schedule". https://help.salesforce.com/s/articleView?id=005298922&language=en_US&type=1 (accessed 2026-11-23)
[^s4]: Trailhead, "Get Started with Salesforce JavaScript Developer I Certification Prep". https://trailhead.salesforce.com/content/learn/modules/javascript-dev-i-cert-prep-variables-collections-functions-classes/get-started-with-salesforce-javascript-developer-i-certification-prep (accessed 2026-11-23)
[^s5]: Trailhead, "JavaScript Developer Certification Maintenance (Summer '25)". https://trailhead.salesforce.com/content/learn/modules/javascript-developer-certification-maintenance-summer-25 (accessed 2026-11-23)
[^s6]: Salesforce, "JavaScript Developer I Certification: Unlock new career opportunities". https://www.salesforce.com/blog/salesforce-javascript-developer-certification/ (accessed 2026-11-23)
