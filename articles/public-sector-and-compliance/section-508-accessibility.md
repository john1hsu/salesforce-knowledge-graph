---
id: kt:section-508-accessibility
type: ExternalConcept
title: Section 508 Accessibility
aliases: [Section 508, Revised 508 Standards, Section 508 compliance, ICT accessibility standards]
domain: public-sector-and-compliance
summary: >-
  The US federal accessibility requirement (Section 508 of the Rehabilitation Act) that ICT agencies buy, build
  or use be accessible to people with disabilities; its Revised Standards adopt WCAG 2.0 Level A and AA, and
  Salesforce evidences conformance through per-product Accessibility Conformance Reports (VPATs).
release: "Winter '27"
status: concept
broader: [kt:digital-accessibility]
related: [kt:public-sector-solutions, kt:government-cloud-plus, kt:fedramp, kt:lightning-web-components, kt:experience-cloud]
relations:
  - {predicate: dependsOn, object: kt:wcag}
sources:
  - id: s1
    title: "About the ICT Accessibility 508 Standards and 255 Guidelines"
    publisher: U.S. Access Board
    url: https://www.access-board.gov/ict/
    type: government
    accessed: 2026-11-03
  - id: s2
    title: "FAR Update Adds Revised 508 Standards"
    publisher: Section508.gov (GSA)
    url: https://section508.gov/blog/far-update-adds-revised-508-standards
    type: government
    accessed: 2026-11-03
  - id: s3
    title: "Product Accessibility Status (508 Accessibility)"
    publisher: Salesforce
    url: https://salesforce.com/company/legal/508_accessibility
    type: official-docs
    accessed: 2026-11-03
  - id: s4
    title: "Component Accessibility (Lightning Web Components Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/lwc/guide/create-components-accessibility.html
    type: official-docs
    accessed: 2026-11-03
  - id: s5
    title: "Base Components Accessibility (Lightning Web Components Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/lwc/guide/base-components-accessibility.html
    type: official-docs
    accessed: 2026-11-03
  - id: s6
    title: "Accessible Salesforce Customizations: Restructure Page Layouts"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/accessible-salesforce-customizations/restructure-page-layouts
    type: official-learning
    accessed: 2026-11-03
created: 2026-11-03
---

# Section 508 Accessibility

Section 508 of the US Rehabilitation Act requires that information and communication technology (ICT) which federal agencies develop, procure, maintain or use be accessible to people with disabilities. The technical rules are the Revised 508 Standards, issued by the U.S. Access Board as a final rule on January 18, 2017 (with a correction in January 2018).[^s1] For Salesforce practitioners, Section 508 is the accessibility counterpart to FedRAMP: a federal buyer evaluating a Salesforce org will ask about both security authorization and accessibility conformance.

## What the standard requires

Rather than writing its own web rules, the Revised 508 Standards incorporate WCAG 2.0 by reference, specifically its Level A and Level AA success criteria and conformance requirements.[^s1] Public-facing electronic content must meet WCAG 2.0 A/AA, and so must certain non-public content that carries official agency business, such as notices, forms, surveys, training materials and intranet pages.[^s1] Software user interfaces and platform content must likewise meet WCAG 2.0 A/AA and must interoperate with assistive technology such as screen readers.[^s1]

The rule includes escape valves that matter in procurement. If no fully conforming product is commercially available, an agency must buy the one that best meets the standards and document why; an agency may also claim undue burden or fundamental alteration, but must document it and provide an alternative means of access.[^s1] Unaltered legacy ICT that complied with the original 2000 standards does not need retrofitting.[^s1] The Federal Acquisition Regulation was amended to adopt the Revised Standards in a final rule effective September 10, 2021; it requires documentation for every exception and removed the earlier micro-purchase exception.[^s2]

## How Salesforce evidences conformance

Salesforce publishes Accessibility Conformance Reports (ACRs) built on the International edition of the Voluntary Product Accessibility Template (VPAT), so one report addresses WCAG, the Revised 508 Standards and the European EN 301 549 standard together.[^s3] Reports are listed per product or component with a release label or date, spanning clouds, mobile apps, Tableau, MuleSoft and Lightning components, and are produced both internally and by third-party assessors.[^s3] Salesforce states that it aims for WCAG 2.2 AA conformance, a newer bar than the WCAG 2.0 the 508 rule cites.[^s3]

Two gotchas come up in federal deals. Posted ACRs are not contractual unless the contract explicitly includes them or an equivalent, so agencies wanting a commitment must negotiate it.[^s3] And Salesforce says accessibility features of Salesforce Classic are no longer maintained or enhanced, steering customers to Lightning Experience.[^s3]

## Shared responsibility: what the customer builds

Salesforce's ACRs are published per product and component, so accessibility of an org's own customizations rests with the team that builds them. On the developer side, Salesforce recommends Lightning base components wherever they fit, because they ship with Lightning Design System markup and built-in accessibility; otherwise build from an SLDS blueprint, add accessibility attributes, manage focus and follow WCAG.[^s4] Base components update ARIA state as users interact (for example adding `aria-describedby` to an input that shows a validation error), and icons and avatars rely on the developer supplying `alternative-text`.[^s5] Custom colors should use SLDS styling hooks so they stay within the system's accessible contrast guidance.[^s5]

Admins matter as much as developers. Trailhead's accessible-customizations guidance shows that page template choice changes tab order: a left-sidebar template forces keyboard users through the sidebar before the main content, while a right-sidebar template shortens the path.[^s6] Reducing clutter, making the Details tab first and default, and testing layouts with actual assistive-technology users are recommended practices.[^s6]

## Connections

Section 508 sits under broader digital accessibility (`kt:digital-accessibility`) and `dependsOn` WCAG (`kt:wcag`), which supplies its actual success criteria.[^s1] It travels with FedRAMP (`kt:fedramp`) and Government Cloud Plus (`kt:government-cloud-plus`) in federal procurement and is a recurring requirement for Public Sector Solutions (`kt:public-sector-solutions`) implementations serving citizens.[^s2] Its practical enforcement in an org lands on Lightning Web Components (`kt:lightning-web-components`) built by developers and on public-facing Experience Cloud (`kt:experience-cloud`) sites, where the "public-facing content" provisions apply most directly.[^s4]

## Sources
[^s1]: U.S. Access Board, "About the ICT Accessibility 508 Standards and 255 Guidelines". https://www.access-board.gov/ict/ (accessed 2026-11-03)
[^s2]: Section508.gov (GSA), "FAR Update Adds Revised 508 Standards". https://section508.gov/blog/far-update-adds-revised-508-standards (accessed 2026-11-03)
[^s3]: Salesforce, "Product Accessibility Status (508 Accessibility)". https://salesforce.com/company/legal/508_accessibility (accessed 2026-11-03)
[^s4]: Salesforce, "Component Accessibility", Lightning Web Components Developer Guide. https://developer.salesforce.com/docs/platform/lwc/guide/create-components-accessibility.html (accessed 2026-11-03)
[^s5]: Salesforce, "Base Components Accessibility", Lightning Web Components Developer Guide. https://developer.salesforce.com/docs/platform/lwc/guide/base-components-accessibility.html (accessed 2026-11-03)
[^s6]: Salesforce Trailhead, "Accessible Salesforce Customizations: Restructure Page Layouts". https://trailhead.salesforce.com/content/learn/modules/accessible-salesforce-customizations/restructure-page-layouts (accessed 2026-11-03)
