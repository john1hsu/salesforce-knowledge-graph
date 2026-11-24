---
id: kt:apex-json-serialization
type: Feature
title: Apex JSON Serialization
aliases: [System.JSON class, JSON.serialize, JSON.deserialize, JSON.deserializeUntyped, JSONGenerator, JSONParser, Apex JSON support]
domain: development
summary: >-
  Apex's built-in JSON support: the System.JSON class for round-trip serialization and deserialization of Apex objects
  and sObjects, plus JSONGenerator for writing and JSONParser/JSONToken for token-by-token reading of JSON content
  such as callout responses.
release: "Winter '27"
status: current
broader: [kt:apex]
related: [kt:apex-rest-services, kt:apex-defined-types, kt:custom-exceptions, kt:visualforce]
relations:
  - {predicate: implements, object: kt:json}
  - {predicate: consumedBy, object: kt:apex-callouts}
sources:
  - id: s1
    title: "JSON Class (Apex Reference Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_System_Json.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s2
    title: "JSON Support (Apex Developer Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_methods_system_json_overview.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s3
    title: "JSONParser Class (Apex Reference Guide)"
    publisher: Salesforce
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_System_JsonParser.htm
    type: official-docs
    accessed: 2026-11-24
  - id: s4
    title: "RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format"
    publisher: IETF
    url: https://www.rfc-editor.org/rfc/rfc8259
    type: standards-body
    accessed: 2026-11-24
created: 2026-11-24
---

# Apex JSON Serialization

Apex ships native JSON support in the `System` namespace. The Apex Developer Guide groups it into four types: `System.JSON` for round-trip serialization and deserialization, `System.JSONGenerator` for writing standard JSON encoding, `System.JSONParser` for reading JSON-encoded content such as a web service callout response, and the `System.JSONToken` enumeration of parse tokens.[^s2] These methods throw a `JSONException` when they hit a problem during execution.[^s2] The format itself is defined by RFC 8259 (STD 90), which describes four primitive types (string, number, boolean, null) and two structured types (object and array).[^s4]

## How it works

`System.JSON` is a class of static methods.[^s1]

- `serialize(Object)` returns a JSON string; an overload takes `suppressApexObjectNulls` to drop nulls.[^s1]
- `serializePretty(...)` produces the same output indented, with the same null-suppression overload.[^s1]
- `deserialize(String, System.Type)` returns an instance of the given type and ignores unknown attributes.[^s1]
- `deserializeStrict(String, System.Type)` requires every JSON attribute to exist in the target type.[^s1]
- `deserializeUntyped(String)` returns collections of primitive data types instead of a typed object.[^s1]
- `createGenerator(Boolean prettyPrint)` and `createParser(String)` return a new generator or parser.[^s1]

Serializable types include standard and custom sObjects, Apex primitives and collections, Database method results such as `SaveResult` and `DeleteResult`, and Apex class instances.[^s2] Typed deserialization returns an instance of a named `System.Type`, while untyped deserialization returns generic collections the caller must cast and navigate.[^s1]

`JSONParser` is a streaming, token-level reader. `nextToken()` advances and returns the next `JSONToken` (null at end of input), `nextValue()` skips to the next value token, `getCurrentName()` returns the field name for the current value, and typed getters such as `getIntegerValue()` or `getDatetimeValue()` only work on matching token types.[^s3] `readValueAs(System.Type)` and `readValueAsStrict(System.Type)` deserialize the current sub-tree into a type, and `skipChildren()` jumps past an object or array the code does not need.[^s3] This lets code pull a few fields out of a large response without modeling the whole document.[^s3]

## Limits and gotchas

- **Unknown fields**: lenient `deserialize` throws on extra attributes only for sObjects at API 34.0 or earlier.[^s1]
- **Strict mode**: `deserializeStrict` throws on extra attributes for Apex classes in all API versions, but not for sObjects.[^s1]
- **Null suppression**: the `suppressApexObjectNulls` flag does not apply to sObjects retrieved through SOQL.[^s1]
- **Map keys**: a map serializes only if its key type is a primitive such as String, Id, Integer, Date or an Enum.[^s2]
- **Subtypes**: a variable typed as a parent class serializes only the parent's fields, so subtype data is lost.[^s2]
- **Object graphs**: self-referencing objects raise a `JSONException`, and shared references come back as copies.[^s2]
- **Managed packages**: Apex class instances defined in a managed package cannot be serialized from outside it.[^s2]
- **Exceptions**: from API 63.0, serializing custom exceptions and most built-in exceptions is unsupported.[^s2]
- **Datetimes**: from API 53.0, sub-millisecond precision is handled and unsupported datetime formats raise errors.[^s2]
- **Parser state**: `JSONParser` is not serializable, so keep it in a local variable rather than a controller field.[^s2]

On the wire, RFC 8259 says object names SHOULD be unique and that JSON exchanged outside a closed ecosystem MUST be UTF-8, so payloads with duplicate keys behave unpredictably across parsers.[^s4] The RFC also notes that integers interoperate exactly only within the IEEE 754 double range of plus or minus 2^53 - 1, which matters when external systems send large numeric identifiers.[^s4]

## When to use it (and when not)

Use `JSON.serialize` and typed `JSON.deserialize` for most integration payloads and for persisting structured state as text.[^s1] Use `deserializeUntyped` for loosely shaped or exploratory payloads, `JSONGenerator` when output must not mirror an Apex class exactly, and `JSONParser` when only a small slice of a large response matters.[^s2][^s3] Prefer the lenient methods for third-party APIs that add fields over time, and the strict methods when an unexpected field should fail fast.[^s1]

## Connections

JSON serialization is part of `kt:apex` and implements the IETF JSON standard (`kt:json`).[^s4] It is consumed by `kt:apex-callouts`, whose responses `JSONParser` is designed to read, and by `kt:apex-rest-services`, which exchange JSON bodies with clients.[^s2][^s3] `kt:apex-defined-types` model similar nested payloads for Flow. The API 63.0 change ties it to `kt:custom-exceptions`, and the parser's non-serializable state is a known pitfall in `kt:visualforce` controllers.[^s2]

## Sources
[^s1]: Salesforce, "JSON Class (Apex Reference Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_System_Json.htm (accessed 2026-11-24)
[^s2]: Salesforce, "JSON Support (Apex Developer Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apex/apex_methods_system_json_overview.htm (accessed 2026-11-24)
[^s3]: Salesforce, "JSONParser Class (Apex Reference Guide)". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_class_System_JsonParser.htm (accessed 2026-11-24)
[^s4]: IETF, "RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format". https://www.rfc-editor.org/rfc/rfc8259 (accessed 2026-11-24)
