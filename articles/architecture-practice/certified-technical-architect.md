---
id: kt:certified-technical-architect
type: Certification
title: Certified Technical Architect
aliases: [Salesforce Certified Technical Architect, CTA, CTA credential, Technical Architect credential]
domain: architecture-practice
summary: >-
  The top Salesforce architect credential, held by architects who design secure, high-performance, integrated
  solutions across every platform domain; it requires both Application Architect and System Architect and is awarded
  only after passing the two-step CTA Review Board.
release: "Winter '27"
status: current
broader: [kt:salesforce-architect]
related: [kt:well-architected-framework, kt:solution-design-tradeoffs, kt:salesforce-architecture-center, kt:platform-developer-certification]
relations:
  - {predicate: hasPart, object: kt:cta-review-board}
  - {predicate: dependsOn, object: kt:application-architect-certification}
  - {predicate: dependsOn, object: kt:system-architect-certification}
  - {predicate: usedBy, object: kt:salesforce-architect}
sources:
  - id: s1
    title: "Certification - Salesforce Certified Technical Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/credentials/technicalarchitect
    type: official-learning
    accessed: 2026-11-05
  - id: s2
    title: "Certified Technical Architect Credential"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/architectreviewboard
    type: official-learning
    accessed: 2026-11-05
  - id: s3
    title: "Certification - Salesforce Certified Application Architect"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/credentials/applicationarchitect
    type: official-learning
    accessed: 2026-11-05
  - id: s4
    title: "Certified Technical Architects"
    publisher: Salesforce
    url: https://www.salesforce.com/blog/certified-technical-architects/
    type: official-blog
    accessed: 2026-11-05
  - id: s5
    title: "Is the Salesforce CTA Becoming a Luxury Credential?"
    publisher: Salesforce Ben
    url: https://salesforceben.com/is-the-salesforce-cta-becoming-a-luxury-credential
    type: news
    accessed: 2026-11-05
created: 2026-11-05
---

# Certified Technical Architect

The Salesforce Certified Technical Architect (CTA) is the credential at the top of the Salesforce architect ladder. Trailhead describes holders as architects experienced in designing and implementing secure, high-performance, integrated technical solutions on the platform, fitted into a client's wider architectural landscape.[^s1] Salesforce's own blog calls it the pinnacle credential for its architects, recognising the ability to design across all domains rather than in one specialism.[^s4]

## What the credential represents

Every architect credential below the CTA validates a slice of the job: data, sharing, identity, integration or release management. The CTA is the one that asks a candidate to combine them into a single coherent design for a whole enterprise scenario.[^s1][^s2] That breadth is visible in the prerequisites: the credential page lists Application Architect, which covers native features plus modelling role hierarchies, data and sharing, and System Architect, which covers off-platform systems, integration and secure access between systems.[^s1]

## How it is earned

The path has three layers.[^s1][^s2][^s3]

1. **Domain certifications.** Application Architect is granted automatically after Platform App Builder, Platform Data Architect, Platform Developer and Platform Sharing and Visibility Architect.[^s3] System Architect rolls up a separate set of identity, integration and lifecycle exams.[^s1]
2. **Both roll-up credentials.** Trailhead states that candidates need both System Architect and Application Architect to initially qualify for the CTA.[^s2]
3. **The review board.** The CTA itself is awarded only after two judged steps, the Architect Review Board Evaluation and then the Technical Architect Review Board Exam. Registration goes through Webassessor, after which Salesforce checks prerequisites and assigns a CTA to run the evaluation.[^s2]

The format, timings and fees of those steps belong to the board itself and are covered in the review board node.[^s2]

## History

The credential launched in 2011, and the first ten CTAs were certified that September.[^s4] Official preparation material followed with the Architect Academy in February 2016, and at Dreamforce '17 Salesforce introduced the domain architect certifications as stepping stones toward the CTA, the structure the prerequisite ladder still follows.[^s4]

## Preparation

Trailhead recommends hands-on experience, training courses, Trails and Trailmixes, and self-study of each domain focus area in the separate CTA exam guide.[^s2] Official aids include the Architect Journey Trailmix, CTA601 (an expert-led virtual workshop from Trailhead Academy for experienced architects) and the Architect Trailblazer Community, which shares sample scenarios.[^s2]

## Gotchas and trade-offs

- **The credential page is thin by design.** It states the prerequisites but no exam format, domain list or maintenance rules; those sit on the review board page, the exam guide and the general maintenance pages.[^s1][^s2]
- **Cost and time are substantial.** A Salesforce Ben survey write-up estimates roughly $6,000 just for the certification process up to the board, before retakes, coaching and study time.[^s5]
- **Few architects hold it.** In that survey 4.7% of respondents were CTAs and 14.5% were working toward it; uncertain career return was the most cited reason for not pursuing it.[^s5]
- **Employer backing matters.** The same analysis argues that sponsorship of fees, coaching and protected study time removes most barriers, and that firms needing CTA-level skills should treat preparation as an investment.[^s5]

## When to pursue it

The CTA suits architects whose work already spans both halves of the ladder, on-platform data and sharing design plus integration, identity and delivery governance, and who need to own end-to-end solutions for large clients.[^s1][^s3] Architects focused on a single domain often get more from the domain credentials and hands-on depth, which survey respondents rated the most effective way to advance.[^s5]

## Connections

- **broader → `kt:salesforce-architect`** and **usedBy → `kt:salesforce-architect`**: the CTA is the most senior validation of the architect role.[^s1][^s4]
- **hasPart → `kt:cta-review-board`**: the two-step board is the assessment that awards the credential.[^s2]
- **dependsOn → `kt:application-architect-certification`, `kt:system-architect-certification`**: both are required to qualify.[^s2] Application Architect in turn includes `kt:platform-developer-certification`, which System Architect also requires.[^s1][^s3]
- **related → `kt:well-architected-framework`, `kt:solution-design-tradeoffs`, `kt:salesforce-architecture-center`**: the board tests the ability to design and justify a full solution, which is exactly what Salesforce's architecture guidance and trade-off reasoning support.[^s2]

## Sources
[^s1]: Trailhead, "Certification - Salesforce Certified Technical Architect". https://trailhead.salesforce.com/en/credentials/technicalarchitect (accessed 2026-11-05)
[^s2]: Trailhead, "Certified Technical Architect Credential". https://trailhead.salesforce.com/credentials/architectreviewboard (accessed 2026-11-05)
[^s3]: Trailhead, "Certification - Salesforce Certified Application Architect". https://trailhead.salesforce.com/credentials/applicationarchitect (accessed 2026-11-05)
[^s4]: Salesforce, "Certified Technical Architects" (Debra Maranta, 2019-02-26). https://www.salesforce.com/blog/certified-technical-architects/ (accessed 2026-11-05)
[^s5]: Thomas Morgan, "Is the Salesforce CTA Becoming a Luxury Credential?", Salesforce Ben. https://salesforceben.com/is-the-salesforce-cta-becoming-a-luxury-credential (accessed 2026-11-05)
