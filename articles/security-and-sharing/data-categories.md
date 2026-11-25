---
id: kt:data-categories
type: Feature
title: Data Categories
aliases: [data category, data category groups, category groups, data category visibility, default data category visibility]
domain: security-and-sharing
summary: >-
  Hierarchical classification labels, organized into category groups, that tag Knowledge articles and questions and
  control which users can see them through All, None or Custom visibility granted by role, permission set,
  permission set group or profile.
release: "Winter '27"
status: current
broader: [kt:knowledge-base]
related: [kt:role-hierarchy, kt:permission-sets, kt:profiles, kt:experience-cloud, kt:high-volume-experience-cloud-users]
relations:
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: contrastsWith, object: kt:salesforce-sharing-model}
  - {predicate: dependsOn, object: kt:role-hierarchy}
sources:
  - id: s1
    title: "Create and Customize Data Categories (Set Up Salesforce Knowledge project)"
    publisher: Salesforce Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/set-up-salesforce-knowledge/create-and-customize-data-categories
    type: official-learning
    accessed: 2026-11-25
  - id: s2
    title: "DataCategoryGroup (Metadata API Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_datacategorygroup.htm
    type: official-docs
    accessed: 2026-11-25
  - id: s3
    title: "Data Category Groups (REST API Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/api-rest/guide/resources-knowledge-support-dcgroups.html
    type: official-docs
    accessed: 2026-11-25
  - id: s4
    title: "Salesforce Knowledge Guide (Classic)"
    publisher: Salesforce
    url: https://login.salesforce.com/help/doc/en/salesforce_knowledge_implementation_guide.pdf
    type: official-docs
    accessed: 2026-11-25
  - id: s5
    title: "WITH DATA CATEGORY (SOQL and SOSL Reference)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-with-datacategory.html
    type: official-docs
    accessed: 2026-11-25
  - id: s6
    title: "dataCategorySelection (SOQL and SOSL Reference)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-with-datacategory-catselection.html
    type: official-docs
    accessed: 2026-11-25
created: 2026-11-25
---

# Data Categories

Data categories are a classification tree that Salesforce Knowledge uses both to organize content and to decide who may read it. Categories live inside a **category group**; each group starts with an automatically created top-level category named "All", under which admins add child categories in Setup > Data Category Setup.[^s1][^s4] Beyond articles and their translations, the Classic Knowledge guide lists Ideas, Answers and Chatter Answers as consumers, while the Metadata API exposes `KnowledgeArticleVersion` and `Question` as the supported object usages.[^s4][^s2] Data categories are available in every edition with Knowledge except Professional Edition.[^s4]

## How visibility works

Category visibility is a second access gate on categorized content, layered on top of object permissions. It is granted through roles, permission sets, permission set groups or profiles, and each grant is one of three settings per group: All Categories, None, or Custom (a chosen subset).[^s4] When a user gets visibility from several sources, the grants combine with OR; child roles inherit the parent role's visibility and can only narrow it.[^s4] Making a category visible also exposes its ancestors and descendants in the tree.[^s4]

The enforcement rule is per group: a categorized article is visible only if the user can see at least one of its categories in each category group applied to it, and a group set to None leaves the user with uncategorized articles only.[^s4] If no visibility has been configured anywhere, all users see all categories; once any role, permission set or profile visibility exists, users without a grant fall back to **Default Data Category Visibility**, which Trailhead's setup project configures per group.[^s4][^s1] Customer and partner portal users inherit their account manager's role visibility, but high-volume users have no role and need permission set or profile grants instead.[^s4]

## Configuration and limits

Creating or editing categories requires the Manage Data Categories permission, and new groups are inactive and hidden from users until activated, so the guide advises defining categories and visibility first.[^s4][^s1] The Winter '27 Metadata API reference allows up to 100 categories in a group and up to 5 hierarchy levels, and a `Question` object can be associated with at most one category group.[^s2] The Classic Knowledge guide adds defaults of 5 category groups with 3 active at a time and 8 categories from one group per article, and notes that Support can raise these limits.[^s4]

Deploying `DataCategoryGroup` through the Metadata API is risky: categories missing from the XML are deleted and their records re-associated with the parent, and moving a category can strip visibility from users who cannot see its new parent. Salesforce recommends creating categories in Setup rather than deploying them from a sandbox.[^s2]

## Querying by category

SOQL's optional `WITH DATA CATEGORY` clause filters articles and questions; the `FROM` object must be `KnowledgeArticleVersion`, an article type such as `Offer__kav`, or `Question`, and article queries also need a `PublishStatus` or `Id` filter in `WHERE`.[^s5] The clause accepts at most three category conditions joined only by AND, with no bind variables.[^s5] Selectors are `AT`, `ABOVE`, `BELOW` and `ABOVE_OR_BELOW`; several categories in one group go in a parenthesized list, a group may appear only once per query, and the running user must have visibility on the named category.[^s6] The REST `support/dataCategoryGroups` resource returns only active groups, and only top categories, that the current user can see.[^s3]

## When to use it (and when not)

Use data categories when article audiences map to a few stable dimensions such as product, region or audience type, and when you want the same tree to drive both navigation filters and read access.[^s4] Keep the number of groups small, because each group adds a mandatory visibility check. Since Summer '20, Lightning Knowledge can also use standard record sharing, and switching to it changes how categories participate in access, so choose one model deliberately.[^s4]

## Connections

Data categories are a sub-feature of **Salesforce Knowledge** and depend on the **role hierarchy** for inherited visibility, with **permission sets** and **profiles** as the other grant paths.[^s4] They contrast with the record-level **Salesforce sharing model**: they filter by classification, not ownership or share rows.[^s4] Filtering is exposed in **SOQL** through `WITH DATA CATEGORY`.[^s5] For **Experience Cloud** sites, role-less **high-volume Experience Cloud users** must receive visibility through permission sets or profiles.[^s4]

## Sources
[^s1]: Salesforce Trailhead, "Create and Customize Data Categories". https://trailhead.salesforce.com/content/learn/projects/set-up-salesforce-knowledge/create-and-customize-data-categories (accessed 2026-11-25)
[^s2]: Salesforce, "DataCategoryGroup", Metadata API Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_datacategorygroup.htm (accessed 2026-11-25)
[^s3]: Salesforce, "Data Category Groups", REST API Developer Guide. https://developer.salesforce.com/docs/platform/api-rest/guide/resources-knowledge-support-dcgroups.html (accessed 2026-11-25)
[^s4]: Salesforce, "Salesforce Knowledge Guide (Classic)". https://login.salesforce.com/help/doc/en/salesforce_knowledge_implementation_guide.pdf (accessed 2026-11-25)
[^s5]: Salesforce, "WITH DATA CATEGORY", SOQL and SOSL Reference. https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-with-datacategory.html (accessed 2026-11-25)
[^s6]: Salesforce, "dataCategorySelection", SOQL and SOSL Reference. https://developer.salesforce.com/docs/platform/salesforce-soql-sosl/guide/sforce-api-calls-soql-select-with-datacategory-catselection.html (accessed 2026-11-25)
