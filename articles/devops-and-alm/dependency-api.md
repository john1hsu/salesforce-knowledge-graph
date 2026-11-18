---
id: kt:dependency-api
type: API
title: Dependency API
aliases: [Metadata Dependency API, Dependencies API, MetadataComponentDependency, Salesforce Dependency API]
domain: devops-and-alm
summary: >-
  A beta Salesforce API, exposed as the MetadataComponentDependency object in Tooling API and Bulk API 2.0,
  that returns which metadata components reference which others in an org, for impact analysis and package decomposition.
release: "Winter '27"
status: beta
broader: [kt:tooling-api, kt:application-lifecycle-management]
related: [kt:unlocked-packages, kt:package-dependencies, kt:custom-fields, kt:technical-debt-in-salesforce]
relations:
  - {predicate: partOf, object: kt:tooling-api}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: queriedWith, object: kt:bulk-api-2}
  - {predicate: queriedWith, object: kt:salesforce-cli}
  - {predicate: contrastsWith, object: kt:metadata-api}
  - {predicate: governedBy, object: kt:api-request-limits}
sources:
  - id: s1
    title: "MetadataComponentDependency (Beta) (Tooling API Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/api-tooling/references/tooling-objects/tooling-metadatacomponentdependency.html
    type: official-docs
    accessed: 2026-11-18
  - id: s2
    title: "Where Is This Field Used? With Vladimir Gerasimov (Salesforce Admins Podcast)"
    publisher: Salesforce Admins
    url: https://admin.salesforce.com/blog/2019/where-is-this-field-used-with-vladimir-gerasimov
    type: official-blog
    accessed: 2026-11-18
  - id: s3
    title: "Learn MOAR with Spring '20 Release Highlights for Developers"
    publisher: Salesforce Developers Blog
    url: https://developer.salesforce.com/blogs/2020/01/learn-moar-with-spring-20-release-highlights-for-developers
    type: official-blog
    accessed: 2026-11-18
  - id: s4
    title: "Extract Dependency Information from Unlocked Packages (Salesforce DX Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_extract_dependency_info.htm
    type: official-docs
    accessed: 2026-11-18
created: 2026-11-18
---

# Dependency API

The Dependency API answers the question "what uses this component, and what does it use?" for an org's metadata. It is exposed as a single read-only object, `MetadataComponentDependency`, in which each record is one edge: a dependent component on one side and the component it references on the other. Salesforce still labels it a beta: the documentation says it is for evaluation, not production use, comes without support, and may be discontinued.[^s1] The object appeared in API version 42.0, became queryable through Tooling API in 43.0, and through Bulk API 2.0 in 49.0; the Winter '27 reference is at API 68.0.[^s1]

## How it works

Every record has eight string fields in two mirrored groups. `MetadataComponentId`, `MetadataComponentName`, `MetadataComponentNamespace` and `MetadataComponentType` describe the dependent component, while the `RefMetadataComponent…` fields describe the component it depends on. All of them are filterable, groupable and sortable in principle, and the only supported calls are `describeSObjects()` and `query()` in SOAP or the REST Query resource.[^s1] A typical impact-analysis query filters on `RefMetadataComponentId` to list everything that references one Apex class or custom field; a decomposition query filters on `MetadataComponentType` to map what a set of components needs.[^s1]

The API grew out of the delete-check logic that stops you removing a referenced field. Salesforce's product manager described it in 2019 as a general "where is this used?" service for any component, not only fields, with the custom-field **Where is this used?** button in Setup as its first consumer, then in beta.[^s2] It reached developers as a beta with Spring '20, alongside an open-source `dependencies-cli` plugin whose `component:report` command writes a JSON report of components and their dependencies.[^s3]

## Limits and gotchas

- **Row caps.** A Tooling API query returns at most 2,000 records, while a Bulk API 2.0 query can return up to 100,000.[^s1]
- **Reports are missing from Tooling API results.** Dependencies that involve reports come back only through Bulk API 2.0.[^s1]
- **Restricted SOQL.** `ORDER BY`, `count()`, `queryMore()` and `OFFSET` are unsupported, so large orgs must be partitioned with filters instead of paged.[^s1]
- **Narrow filters.** No `WHERE` on either name field, no `LIKE` on the type fields, and only `=`, `!=`, `AND` and `OR` as operators.[^s1]
- **StandardEntity.** Filtering `RefMetadataComponentType` to `StandardEntity` is not allowed, which complicates questions about standard objects.[^s1]
- **ID format.** Use 18-character IDs in ID filters; the ID fields can also hold a standard object's name instead of an ID.[^s1]
- **Beta caveats.** Coverage of metadata types is incomplete; reports and some other components were called out early as gaps.[^s2][^s1]

## When to use it (and when not)

Use it before deleting or changing a component, to size the blast radius, and when carving an org into packages, where you need to know which components cluster together and which cross-references would become package dependencies.[^s3][^s1] Because it is beta and incomplete, treat an empty result as "no known dependency", not proof that a component is unused; pair it with tests and code search before removing anything.[^s1][^s2] It is not the tool for installed-package ordering: for that, the Tooling API `SubscriberPackageVersion` object's `Dependencies` field lists the 04t IDs an unlocked package needs, in install order.[^s4]

## Connections

The Dependency API is **part of** the **Tooling API** and is **queried with SOQL**, either through Tooling API or, for larger and report-inclusive result sets, **Bulk API 2.0**; from the command line it is reached via the **Salesforce CLI** and its plugins.[^s1][^s3] It **contrasts with** the **Metadata API**, which deploys and retrieves components but does not report the reference graph between them.[^s1] Its main consumers are **unlocked packages** design and **package dependencies** planning, whereas `SubscriberPackageVersion` covers dependencies between installed packages rather than between components.[^s3][^s4] The Setup button that checks **custom fields** was its first user, and the same reference data supports paying down **technical debt** by revealing unused or tangled metadata.[^s2][^s1] Its calls count against **API request limits**, like other Tooling API traffic.[^s1]

## Sources

[^s1]: Salesforce, "MetadataComponentDependency (Beta)", Tooling API Developer Guide (Winter '27, API 68.0). https://developer.salesforce.com/docs/platform/api-tooling/references/tooling-objects/tooling-metadatacomponentdependency.html (accessed 2026-11-18)
[^s2]: Salesforce Admins, "Where Is This Field Used? With Vladimir Gerasimov" (2019). https://admin.salesforce.com/blog/2019/where-is-this-field-used-with-vladimir-gerasimov (accessed 2026-11-18)
[^s3]: Salesforce Developers Blog, "Learn MOAR with Spring '20 Release Highlights for Developers" (2020). https://developer.salesforce.com/blogs/2020/01/learn-moar-with-spring-20-release-highlights-for-developers (accessed 2026-11-18)
[^s4]: Salesforce, "Extract Dependency Information from Unlocked Packages", Salesforce DX Developer Guide. https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_unlocked_pkg_extract_dependency_info.htm (accessed 2026-11-18)
