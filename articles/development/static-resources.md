---
id: kt:static-resources
type: Feature
title: Static Resources
aliases: [static resource, StaticResource, $Resource, "@salesforce/resourceUrl", resourceUrl]
domain: development
summary: >-
  Files uploaded to a Salesforce org (archives, images, style sheets, JavaScript and other files) that Visualforce pages,
  Lightning components and Apex reference by name, and the standard way to bring third-party libraries into Lightning.
release: "Winter '27"
status: current
broader: [kt:salesforce-platform]
related: [kt:lightning-web-components, kt:visualforce, kt:aura-components, kt:test-loaddata, kt:cross-site-scripting]
relations:
  - {predicate: consumedBy, object: kt:lightning-web-components}
  - {predicate: consumedBy, object: kt:visualforce}
  - {predicate: dependsOn, object: kt:content-security-policy}
  - {predicate: configuredVia, object: kt:metadata-api}
  - {predicate: integratesWith, object: kt:lightning-web-security}
sources:
  - id: s1
    title: "Visualforce Developer Guide: Creating a Static Resource"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/salesforce-pages-developers-guide/guide/pages-resources-create.html
    type: official-docs
    accessed: 2026-11-21
  - id: s2
    title: "Visualforce Developer Guide: Using Static Resources"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.264.0.pages.meta/pages/pages_resources.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s3
    title: "Lightning Web Components Developer Guide: Static Resources"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/create-resources.html
    type: official-docs
    accessed: 2026-11-21
  - id: s4
    title: "Lightning Component Reference: Platform Resource Loader"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-platform-resource-loader.html
    type: official-docs
    accessed: 2026-11-21
  - id: s5
    title: "Metadata API Developer Guide: StaticResource"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_staticresource.htm
    type: official-docs
    accessed: 2026-11-21
  - id: s6
    title: "Lightning Web Components Developer Guide: Use Third-Party JavaScript Libraries"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/lwc/guide/js-third-party-library
    type: official-docs
    accessed: 2026-11-21
created: 2026-11-21
---

# Static Resources

A **static resource** is a file uploaded to a Salesforce org so that the org's own pages and components can reference it by name. It can be an archive (.zip or .jar), an image, a style sheet, a JavaScript file or another file type, and it is meant for use inside the org rather than as general hosting for other apps or websites.[^s1] Salesforce recommends static resources over files in the Documents tab because a whole directory tree can be packaged into one archive, and pages refer to it by name through the `$Resource` global variable instead of a hard-coded document ID.[^s2] The same mechanism is also preferred over inline markup for JavaScript and CSS.[^s2]

## How it works

Admins and developers create a resource in Setup under **Static Resources** with the Customize Application permission: they give it a unique name, an optional description, upload the file and choose a cache-control setting.[^s1] Names may contain only letters, digits and underscores; they must start with a letter and cannot end with an underscore or contain two consecutive underscores.[^s1]

**Cache control** decides who can fetch the file and how it is cached. *Private* makes the file available to authenticated users and caches it per user for the session; *Public* makes it reachable by all internet traffic, including unauthenticated users, through a shared cache that loads faster.[^s1][^s3] On a Site whose guest users are restricted by IP range or login hours, the setting is treated as private and caching happens only in the browser.[^s1]

As metadata, each resource is a `StaticResource` component stored in the `staticresources` folder with a `.resource` suffix plus a metadata file; its required fields are `cacheControl` (Private or Public) and `contentType` (a MIME type such as `text/plain`), with an optional `description`.[^s5] In a Salesforce DX project the files live in `force-app/main/default/staticresources`, which may not contain subdirectories.[^s3]

## Using static resources in components

In **Lightning Web Components**, a module imports the resource URL with `@salesforce/resourceUrl/<name>`, adding a `namespace__` prefix only when the resource belongs to a managed package.[^s3] For a file inside an archive, the component concatenates the path to the imported URL, and images are exposed as a class field bound to an `img` element in the template.[^s3]

JavaScript libraries and style sheets are loaded at runtime with `loadScript` and `loadStyle` from `lightning/platformResourceLoader`. Each takes `this` and a file URL and returns a promise, so loads can be chained to control order or run in parallel with `Promise.all`.[^s4][^s6] The module cannot be imported dynamically.[^s4] Salesforce's D3 example calls the loaders in `renderedCallback()` behind a flag so the library loads once, and catches errors from the promise.[^s6]

## Limits and gotchas

- A single static resource can be up to 5 MB, and an org can hold up to 250 MB of static resources in total.[^s1][^s3]
- Uploading third-party code as a static resource is a Lightning security requirement; the library is uploaded to the org rather than referenced from elsewhere.[^s4][^s6]
- If an Aura component loads a script with `ltng:require` and an LWC loads it with `loadScript`, the duplicate isn't detected, so the script must guard itself.[^s4]
- Without Lightning Web Security, libraries must meet Lightning Locker rules; with LWS, most libraries work unchanged, though some still need changes.[^s6]
- Libraries that manipulate the DOM need an empty container marked `lwc:dom="manual"`, and Salesforce does not support third-party libraries themselves.[^s6]
- Making a previously open Site restricted can leave public resources in caches for up to 45 days.[^s1]

## When to use it (and when not)

Use static resources for assets that ship with code: component libraries, icons, fonts, CSS and test data files. They deploy with the Metadata API, so they version and package cleanly alongside the components that use them.[^s2][^s5] They are not a store for user-generated or frequently changing content, and anything set to Public is reachable without authentication once cached, so never put confidential data in a public resource.[^s1]

## Connections

Static resources sit on the core **Salesforce platform** and are **consumed by** both **Visualforce**, through `$Resource`, and **Lightning Web Components**, through `@salesforce/resourceUrl`; **Aura components** load them too.[^s2][^s3][^s4] They exist largely because of the Lightning **content security policy**, which forces third-party code to be hosted in the org, and they work alongside **Lightning Web Security** (or Locker) when that code runs.[^s6] That is also why they matter for **cross-site scripting** defence. They are **configured via** the **Metadata API** `StaticResource` type.[^s5] In Apex testing, **Test.loadData** depends on them, reading CSV test records from a static resource.

## Sources

[^s1]: Salesforce Developers, "Visualforce Developer Guide: Creating a Static Resource". https://developer.salesforce.com/docs/platform/salesforce-pages-developers-guide/guide/pages-resources-create.html (accessed 2026-11-21)
[^s2]: Salesforce Developers, "Visualforce Developer Guide: Using Static Resources". https://developer.salesforce.com/docs/atlas.en-us.264.0.pages.meta/pages/pages_resources.htm (accessed 2026-11-21)
[^s3]: Salesforce Developers, "Lightning Web Components Developer Guide: Static Resources". https://developer.salesforce.com/docs/platform/lwc/guide/create-resources.html (accessed 2026-11-21)
[^s4]: Salesforce Developers, "Lightning Component Reference: Platform Resource Loader". https://developer.salesforce.com/docs/platform/lightning-component-reference/guide/lightning-platform-resource-loader.html (accessed 2026-11-21)
[^s5]: Salesforce Developers, "Metadata API Developer Guide: StaticResource". https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_staticresource.htm (accessed 2026-11-21)
[^s6]: Salesforce Developers, "Lightning Web Components Developer Guide: Use Third-Party JavaScript Libraries". https://developer.salesforce.com/docs/platform/lwc/guide/js-third-party-library (accessed 2026-11-21)
