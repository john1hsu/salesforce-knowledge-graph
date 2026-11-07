---
id: kt:principle-of-least-privilege
type: Concept
title: Principle of Least Privilege
aliases: [least privilege, PoLP, PLP, least-privilege access, minimum necessary access]
domain: security-and-sharing
summary: >-
  The security principle that every user, integration, agent and process receives only the access
  its task requires; in Salesforce it is realised by a minimal baseline profile plus additive
  permission sets and permission set groups.
release: "Winter '27"
status: concept
broader: [kt:salesforce-sharing-model]
related: [kt:permission-sets, kt:permission-set-groups, kt:profiles, kt:integration-security, kt:field-level-security, kt:nist-sp-800-53]
relations:
  - {predicate: mitigates, object: kt:data-breach-risk}
  - {predicate: partOf, object: kt:zero-trust-architecture}
sources:
  - id: s1
    title: "least privilege (CSRC Glossary)"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/Glossary/term/least_privilege
    type: standards-body
    accessed: 2026-11-07
  - id: s2
    title: "Protecting Data with the Principle of Least Privilege"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/principle-of-least-privilege/
    type: official-blog
    accessed: 2026-11-07
  - id: s3
    title: "Data Security: Control Access to Objects (Trailhead)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/modules/data_security/units/data_security_objects
    type: official-learning
    accessed: 2026-11-07
  - id: s4
    title: "Technical Debt: Close Security Gaps and Enhance Salesforce Security (Trailhead)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/technical-debt/close-security-gaps
    type: official-learning
    accessed: 2026-11-07
  - id: s5
    title: "Secure and Trusted Headless Foundation: Apply Least-Privilege Controls (Trailhead)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/secure-and-trusted-headless-foundation/apply-least-privilege-controls
    type: official-learning
    accessed: 2026-11-07
created: 2026-11-07
---

# Principle of Least Privilege

The principle of least privilege says that a user, or a process acting for a user, should hold only the access needed to complete its assigned work. NIST's glossary records several closely aligned definitions, from CNSSI 4009 and NIST SP 800-53 Rev. 5 among others, all framing it as giving each entity only the resources and authorizations its function requires.[^s1] Salesforce presents it as a core information-security tenet that applies to users, devices, applications and systems alike, and positions it as one building block of a Zero Trust strategy in which holding a credential does not unlock everything.[^s2]

## How it works in Salesforce

Salesforce's recommended implementation is the permission-set-led security model. Admins give users a deliberately thin baseline, then layer on only what each job needs.[^s2] Every user has exactly one profile, which sets defaults such as apps, record types, page layouts, IP ranges and login hours; permission sets bundle the permissions for a specific task, a user can hold several, and permission set groups combine sets to represent a persona such as a sales rep.[^s3] Trailhead recommends the **Minimum Access - Salesforce** profile, or a clone of it, as the baseline because it grants very few platform permissions, with object, field, Apex, tab and Visualforce access granted through permission sets and groups instead.[^s3] Inside a group, a muting permission set can suppress individual permissions, which helps when a reusable set grants slightly more than one persona should have.[^s3]

The same idea governs non-human actors. Trailhead's guidance for agents and headless integrations asks designers to decide whether the caller acts in the end user's context (so two reps can legitimately see different results) or as a dedicated integration user with its own narrowly scoped permission set.[^s5] It recommends starting read-only, returning only the objects, fields and records required, favouring specific actions over broad edit rights, and adding write access only after the read-only design has been tested and approved.[^s5]

## Practical steps

Salesforce's own guidance boils down to three steps: audit existing accounts and permissions to remove privilege creep, assign the minimum-access profile, and then layer permission sets and groups according to each user's required access.[^s2] When granting a permission, it suggests asking whether the user truly needs that level, whether it can be reduced further, whether it can be limited by time or session, and whether the user can still do the job with less.[^s2] For agentic and integration access, Trailhead adds verification: prove in a sandbox that unauthorized requests fail, test with the real end user's identity rather than an admin, and make custom Apex enforce security explicitly.[^s5]

## Gotchas

- **Over-permissive standard profiles.** Standard profiles' object permissions cannot be edited, and some grant more than users need, so review them before assignment or clone and trim them.[^s3]
- **Super-permissions.** View All Data and Modify All Data override all sharing settings; Trailhead advises caution when assigning them outside the System Administrator profile.[^s3]
- **Removal is two-sided.** A permission granted in both a profile and a permission set stays in effect until it is removed from both.[^s3]
- **Custom-profile sprawl.** Trailhead's technical-debt scenario shows executives given excess access through a custom profile, rates the risk High, and recommends reassigning those users and deleting the profile so extra access arrives only through permission sets.[^s4]
- **Inherited orgs.** Over-privileged users are especially common in orgs an admin takes over, so a privilege audit is a sensible first task.[^s2]
- **Permissions stop at the boundary.** Salesforce permissions govern what data leaves the platform, not what an external model or vendor does with it, so send only the minimum data needed.[^s5]

## Connections

Least privilege is the design goal behind much of the **Salesforce sharing model**. **Permission sets** and **permission set groups** are the mechanisms that implement it, while **profiles** are reduced to a minimal baseline; object and **field-level security** permissions are where it becomes concrete.[^s3] Applying it to API and agent access is a central concern of **integration security**.[^s5] Because it limits what a compromised account or careless user can reach, it mitigates **data breach risk**, and it sits inside a wider **Zero Trust architecture** strategy.[^s2] Its formal definitions come from NIST and CNSSI, linking it to the access-control family of **NIST SP 800-53**.[^s1]

## Sources
[^s1]: NIST CSRC, "least privilege (Glossary)". https://csrc.nist.gov/Glossary/term/least_privilege (accessed 2026-11-07)
[^s2]: Salesforce, "Protecting Data with the Principle of Least Privilege". https://www.salesforce.com/blog/principle-of-least-privilege/ (accessed 2026-11-07)
[^s3]: Salesforce Trailhead, "Data Security: Control Access to Objects". https://trailhead.salesforce.com/modules/data_security/units/data_security_objects (accessed 2026-11-07)
[^s4]: Salesforce Trailhead, "Technical Debt: Close Security Gaps and Enhance Salesforce Security". https://trailhead.salesforce.com/content/learn/modules/technical-debt/close-security-gaps (accessed 2026-11-07)
[^s5]: Salesforce Trailhead, "Secure and Trusted Headless Foundation: Apply Least-Privilege Controls". https://trailhead.salesforce.com/content/learn/modules/secure-and-trusted-headless-foundation/apply-least-privilege-controls (accessed 2026-11-07)
