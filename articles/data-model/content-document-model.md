---
id: kt:content-document-model
type: Concept
title: Content Document Model
aliases: [salesforce files data model, contentdocument, contentversion, contentdocumentlink, files object model]
domain: data-model
summary: >-
  The trio of standard objects behind Salesforce Files: ContentDocument (the file's identity), ContentVersion (each
  version's binary data) and ContentDocumentLink (the junction that shares a file with users, groups, records and
  libraries).
release: "Winter '27"
status: current
broader: [kt:standard-objects, kt:data-architecture]
related: [kt:polymorphic-relationships, kt:salesforce-sharing-model, kt:apex-triggers]
relations:
  - {predicate: implements, object: kt:junction-object}
  - {predicate: governedBy, object: kt:data-and-file-storage-allocations}
  - {predicate: queriedWith, object: kt:soql}
  - {predicate: contrastsWith, object: kt:notes-and-attachments}
sources:
  - id: s1
    title: "Object Reference: ContentDocument"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_contentdocument.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s2
    title: "Object Reference: ContentDocumentLink"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_contentdocumentlink.htm
    type: official-docs
    accessed: 2026-11-12
  - id: s3
    title: "Understand File Uploads in Salesforce (Mobile and Offline Developer Guide)"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/platform/mobile-offline/guide/use-images-upload-file-representation.html
    type: official-docs
    accessed: 2026-11-12
  - id: s4
    title: "Lightning Experience Productivity: Work with Notes and Files (unit)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/modules/lightning-experience-productivity/units/work-with-notes-and-files
    type: official-learning
    accessed: 2026-11-12
  - id: s5
    title: "Pro Tip: Simplify File Management with Salesforce Files in Lightning Experience"
    publisher: Salesforce Admins Blog
    url: https://admin.salesforce.com/blog/2017/pro-tip-simplify-file-management-salesforce-files-lightning-experience
    type: official-blog
    accessed: 2026-11-12
created: 2026-11-12
---

# Content Document Model

Salesforce Files is stored in three standard objects that work together. **ContentDocument** is the file's identity and holds no binary data; **ContentVersion** stores the bytes, one record per version; and **ContentDocumentLink** joins the document to every place it is shared.[^s3] The same model backs Salesforce CRM Content and, through ContentDocumentLink, enhanced notes (ContentNote).[^s1][^s2] Knowing these objects is essential for any data migration, integration or trigger that touches files.

## How it works

You never insert a ContentDocument directly: the object supports query, update and delete, but not create. Inserting a ContentVersion without a ContentDocumentId makes Salesforce create the parent document automatically, while inserting one that names an existing ContentDocumentId adds a new version.[^s1] Updating a file therefore means uploading a new version rather than overwriting the old one, and the document's LatestPublishedVersion points at the current version.[^s1][^s3]

Attaching a file to a record, user, group or library creates a ContentDocumentLink, so one file can be linked to any number of records without duplicating its data.[^s3] The link's LinkedEntityId is polymorphic: it can reference a user, a group, a library, or any record that supports Chatter feed tracking.[^s2] Each link carries two access settings:

- **ShareType**: V (Viewer), C (Collaborator, who can also edit), or I (Inferred from the linked record or library permission).[^s2]
- **Visibility**: AllUsers, InternalUsers, or SharedUsers, which applies only with a private user sharing default.[^s2]

In the UI, the Files related list on a record shows these links. Viewers can view, download and reshare, collaborators can also upload new versions and change permissions, and public links give outsiders view-and-download access that the owner can revoke.[^s4]

## Limits and gotchas

The figures below are from the Winter '27 object reference:

- An org can hold at most 30,000,000 published documents, archived ones included.[^s1]
- New versions per 24 hours are capped at 200,000 in Enterprise, Unlimited and similar editions, and 2,500 in Developer and trial orgs.[^s1]
- ContentSize reports sizes under 2 GB; the newer ContentSizeLong field (API 65.0) reports sizes up to 10 GB.[^s1]
- A ContentDocumentLink query must filter on Id, ContentDocumentId or LinkedEntityId, unless the user has Query All Files (API 59.0+).[^s2]
- Deleting a document deletes all its versions. The cascaded link deletions don't fire ContentDocumentLink triggers.[^s1][^s2]
- A Collaborator (C) link can't be created from an Apex trigger, and query() skips archived documents.[^s1][^s2]

Ownership changes also rewrite links: moving a document to a new owner deletes the old owner's ContentDocumentLink and creates one for the new owner.[^s1] In orgs with Digital Experiences, a document can only be shared with users and groups of the Experience Cloud site where it was created.[^s2]

## When to use it (and when not)

Files is the store to use for record documents in Lightning Experience. Legacy Attachments don't appear in Files home or the Files related list, can't be shared in Chatter, and are read-only in Lightning Experience, so new attachments can't be created there.[^s4][^s5] The Salesforce Admins blog describes converting them, either with the free Salesforce Labs conversion app or an API-based tool for Professional Edition. A General Settings option can also save files added to the Attachments related list as Salesforce Files.[^s5] Classic notes likewise stay in Notes & Attachments and don't interoperate with enhanced notes.[^s4] Documents used as email template attachments are the exception that must stay in the classic Documents object.[^s4]

## Connections

The model is a textbook example of the **junction object** pattern: ContentDocumentLink resolves the many-to-many relationship between files and the entities they are shared with, and its LinkedEntityId is one of the platform's **polymorphic relationships**.[^s2] File access is computed from those links, the linked record's access, and library permissions, so it sits alongside the **Salesforce sharing model** rather than inside it.[^s2] File bytes count toward **data and file storage allocations**, and integrations read the objects with **SOQL** under the filter rules above.[^s1][^s2] Developers who write **Apex triggers** on ContentDocumentLink must account for the trigger gaps on cascaded deletes.[^s2] The legacy **Notes & Attachments** model (classic Attachment and Note records) is the contrast case that Files replaces in Lightning Experience.[^s5]

## Sources
[^s1]: Salesforce Developers, "Object Reference: ContentDocument". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_contentdocument.htm (accessed 2026-11-12)
[^s2]: Salesforce Developers, "Object Reference: ContentDocumentLink". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_contentdocumentlink.htm (accessed 2026-11-12)
[^s3]: Salesforce Developers, "Understand File Uploads in Salesforce". https://developer.salesforce.com/docs/platform/mobile-offline/guide/use-images-upload-file-representation.html (accessed 2026-11-12)
[^s4]: Trailhead, "Lightning Experience Productivity: Work with Notes and Files". https://trailhead.salesforce.com/en/modules/lightning-experience-productivity/units/work-with-notes-and-files (accessed 2026-11-12)
[^s5]: Salesforce Admins Blog, "Pro Tip: Simplify File Management with Salesforce Files in Lightning Experience". https://admin.salesforce.com/blog/2017/pro-tip-simplify-file-management-salesforce-files-lightning-experience (accessed 2026-11-12)
