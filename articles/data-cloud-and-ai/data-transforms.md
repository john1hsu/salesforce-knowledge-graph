---
id: kt:data-transforms
type: Feature
title: Data Transforms
aliases: [data transform, Data 360 data transforms, Data Cloud data transforms, batch data transforms, batch data transform, streaming data transforms, streaming data transform]
domain: data-cloud-and-ai
summary: >-
  Data 360 (formerly Data Cloud) jobs that clean, reshape, join and aggregate data lake objects or data model
  objects into new target objects, either as scheduled, visually built batch transforms or as continuously running,
  SQL-defined streaming transforms.
release: "Winter '27"
status: current
broader: [kt:data-cloud]
related: [kt:data-streams, kt:data-model-objects, kt:calculated-insights, kt:transform-element]
relations:
  - {predicate: dependsOn, object: kt:data-lake-objects}
  - {predicate: enables, object: kt:identity-resolution}
  - {predicate: governedBy, object: kt:data-cloud-limits}
  - {predicate: integratesWith, object: kt:ai-models}
  - {predicate: coveredBy, object: kt:data-cloud-consultant-certification}
sources:
  - id: s1
    title: "Get Started with Batch Data Transforms in Data 360"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/batch-data-transforms-in-data-cloud-quick-look/get-started-with-batch-data-transforms-in-data-360
    type: official-learning
    accessed: 2026-11-15
  - id: s2
    title: "Get Started with Streaming Data Transforms in Data Cloud"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/streaming-data-transforms-quick-look/get-started-with-streaming-data-transforms-in-data-cloud
    type: official-learning
    accessed: 2026-11-15
  - id: s3
    title: "Streaming Data Transforms"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=data.c360_a_streaming_transform_overview.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "Create a Batch Data Transform"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.c360_a_batch_transform_create.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "Batch Data Transforms Limitations"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.c360_a_batch_transform_limitations.htm&language=en_US&type=5
    type: official-docs
    accessed: 2026-11-15
  - id: s6
    title: "Data 360 Limits and Guidelines"
    publisher: Salesforce Help
    url: https://help.salesforce.com/s/articleView?id=sf.c360_a_limits_and_guidelines.htm&type=5&language=en_US
    type: official-docs
    accessed: 2026-11-15
  - id: s7
    title: "Explore Data Ingestion and Modeling (Data Cloud Consultant Certification Prep)"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/cert-prep-data-cloud-consultant/explore-data-ingestion-and-modeling
    type: official-learning
    accessed: 2026-11-15
  - id: s8
    title: "Connect and Transform Data for Enhanced Insights"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/modules/data-cloud-connect-and-unify/connect-and-transform-data
    type: official-learning
    accessed: 2026-11-15
created: 2026-11-15
---

# Data Transforms

**Data transforms** are the Data 360 (formerly Data Cloud) feature for cleaning, enriching and reshaping data after
it has been connected and before or after it is mapped to the data model. They come in two kinds. A **batch data
transform** reads one or more data lake objects (DLOs) or data model objects (DMOs) and writes a new transformed
dataset on a schedule or on demand. A **streaming data transform** runs continuously, applying a SQL statement to
each record as it arrives.[^s1][^s2] Both are created from the **Data Transforms** tab, and Salesforce notes that the
October 2025 rename to Data 360 left the functionality unchanged.[^s2][^s4]

## How batch transforms work

A batch transform is built on a visual canvas of **nodes**. Input nodes supply DLO or DMO data, output nodes write to
a DLO or DMO, and operation nodes in between do the work. The operation nodes are aggregate, join, append, filter,
transform (formulas, string and date functions, bucketing, dropping columns, JSON handling), update, and AI functions
that call models from AI Models to add predictions.[^s1] Trailhead's walkthrough filters opportunities over 30,000,
joins them to accounts on the account key, sums amounts by industry, writes the result to a new DLO with a primary
key, and runs it with **Run Now**.[^s1]

When you create one you choose the source type first. A DMO-based transform belongs to a single data space and its
output applies only there; a DLO-based transform cannot be associated with a data space. Each output node has a write
mode: **Upsert** reloads all input data on every run and merges it into the output, while **Replace** attempts an
incremental run that loads only changes since the previous run. Creating transforms needs the Data Cloud Architect
permission set.[^s4]

## How streaming transforms work

A streaming transform reads records from a source object, reshapes each one, and writes one or more records to a
different target object, usually a DLO that you then map to a DMO. On setup it processes all existing source records
and then keeps picking up new or changed ones.[^s3] The logic is one SQL statement: `WHERE` limits which records are
processed, and `INNER JOIN` or `LEFT JOIN` can combine two streams on a primary key.[^s3] Trailhead's example
normalizes a contact's mobile, home and work numbers into separate contact-point rows with a `UNION`, dropping empty
values, because a direct mapping can carry only one phone per contact. **Refresh History** shows records processed,
failed and removed.[^s2]

## Limits and gotchas

Checked against Winter '27 on the Data 360 limits page and the batch limitations page:[^s5][^s6]

- **Streaming transforms:** 25 per org (adjustable through your Account Executive), and each SQL statement can be up to 20,000 characters.[^s6]
- **Batch transforms:** up to 1,000 per org, at most 50 running concurrently, and a job running longer than 24 hours is canceled by the system.[^s6]
- **Batch definitions:** one batch transform can combine up to five transform definitions.[^s5]
- **Inputs and outputs:** the same object can't be both an input and an output node, and multiple transforms can't write to the same object, although definitions inside one transform can.[^s5]
- **Streaming source and target** must be different objects; Salesforce recommends rebuilding the target object to keep its data consistent.[^s3]

Pick the write mode deliberately for large sources: Upsert reprocesses all input on every run, whereas Replace
can run incrementally.[^s4]

## When to use which

Use a **batch transform** for complex, multi-step logic that can refresh periodically: dashboard KPIs such as win
rate, standardizing inconsistent values such as company-name spellings, or combining CRM, usage and payroll data
ahead of identity resolution and calculated insights.[^s1] Use a **streaming transform** when records must be
cleaned as they land, such as normalizing transactions from many processors for near-real-time fraud signals, or
when the default model needs rows reshaped.[^s2] For simple per-row cleanup on ingestion, formula fields on the data
stream may be enough, since they can standardize formats, build join keys and flag
records.[^s8] The official exam prep lists telling these transformation capabilities apart as an objective
of the Data Cloud Consultant exam.[^s7]

## Connections

Data transforms are a feature of `kt:data-cloud`. They **depend on** `kt:data-lake-objects`, which hold the data that
`kt:data-streams` ingest and are the usual target of a transform, and they can also read and write
`kt:data-model-objects`.[^s1][^s3] Transforms run after data is connected and before it is mapped and unified.[^s8] Their cleaned and joined output **enables** `kt:identity-resolution` and feeds
`kt:calculated-insights` and segmentation.[^s1][^s2] They **integrate with** `kt:ai-models` through the AI functions
node, and are **governed by** `kt:data-cloud-limits`.[^s1][^s6] The Flow `kt:transform-element` is a related but
separate CRM-side tool for mapping data inside a flow. The topic is **covered by** the
`kt:data-cloud-consultant-certification`.[^s7]

## Sources
[^s1]: Trailhead, "Get Started with Batch Data Transforms in Data 360". https://trailhead.salesforce.com/content/learn/modules/batch-data-transforms-in-data-cloud-quick-look/get-started-with-batch-data-transforms-in-data-360 (accessed 2026-11-15)
[^s2]: Trailhead, "Get Started with Streaming Data Transforms in Data Cloud". https://trailhead.salesforce.com/content/learn/modules/streaming-data-transforms-quick-look/get-started-with-streaming-data-transforms-in-data-cloud (accessed 2026-11-15)
[^s3]: Salesforce Help, "Streaming Data Transforms". https://help.salesforce.com/s/articleView?id=data.c360_a_streaming_transform_overview.htm&language=en_US&type=5 (accessed 2026-11-15)
[^s4]: Salesforce Help, "Create a Batch Data Transform". https://help.salesforce.com/s/articleView?id=sf.c360_a_batch_transform_create.htm&language=en_US&type=5 (accessed 2026-11-15)
[^s5]: Salesforce Help, "Batch Data Transforms Limitations". https://help.salesforce.com/s/articleView?id=sf.c360_a_batch_transform_limitations.htm&language=en_US&type=5 (accessed 2026-11-15)
[^s6]: Salesforce Help, "Data 360 Limits and Guidelines". https://help.salesforce.com/s/articleView?id=sf.c360_a_limits_and_guidelines.htm&type=5&language=en_US (accessed 2026-11-15)
[^s7]: Trailhead, "Explore Data Ingestion and Modeling (Data Cloud Consultant Certification Prep)". https://trailhead.salesforce.com/content/learn/modules/cert-prep-data-cloud-consultant/explore-data-ingestion-and-modeling (accessed 2026-11-15)
[^s8]: Trailhead, "Connect and Transform Data for Enhanced Insights". https://trailhead.salesforce.com/content/learn/modules/data-cloud-connect-and-unify/connect-and-transform-data (accessed 2026-11-15)
