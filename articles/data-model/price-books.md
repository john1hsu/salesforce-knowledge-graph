---
id: kt:price-books
type: StandardObject
title: Price Books
aliases: [price book, Pricebook2, PricebookEntry, price book entry, standard price book, custom price book]
domain: data-model
summary: >-
  The Salesforce standard objects that hold what a company charges for its products: Pricebook2 is a list of
  products, and each PricebookEntry sets one product's price in one price book and currency, with every product
  priced first in the standard price book before custom price books can override it.
release: "Winter '27"
status: current
broader: [kt:standard-objects, kt:sales-cloud]
related: [kt:junction-object, kt:apex-testing, kt:revenue-cloud]
relations:
  - {predicate: consumedBy, object: kt:salesforce-cpq}
  - {predicate: consumedBy, object: kt:salesforce-pricing}
  - {predicate: enables, object: kt:opportunity-products}
  - {predicate: dependsOn, object: kt:multiple-currencies}
sources:
  - id: s1
    title: "PricebookEntry | Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_pricebookentry.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s2
    title: "OpportunityLineItem | Object Reference for the Salesforce Platform"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunitylineitem.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s3
    title: "Test Class | Apex Reference Guide"
    publisher: Salesforce Developers
    url: https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_test.htm
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "Create Price Books to Track Your Products"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/en/sales_admin_products_quotes_contracts/sales_admin_products_quotes_contracts_unit_1
    type: official-learning
    accessed: 2026-11-10
  - id: s5
    title: "Manage Products, Prices, Quotes, and Orders: Create Custom Price Books"
    publisher: Trailhead
    url: https://trailhead.salesforce.com/content/learn/projects/manage-products-prices-quotes-orders/create-custom-price-books
    type: official-learning
    accessed: 2026-11-10
created: 2026-11-10
---

# Price Books

A **price book** is the Salesforce record that lists the products a company sells and what it charges for them. Under the hood it is two standard objects: `Pricebook2`, the price book itself, and `PricebookEntry`, which links one `Product2` to one `Pricebook2` and holds a price for one currency.[^s1] Every org that uses products has a **standard price book**, the master list of all products, and admins add **custom price books** when the same product needs different prices for different markets, segments or regions.[^s4]

## How it works

When a product is created it gets a standard price and appears in the standard price book; a custom price book can then give the same product its own list price.[^s4] In the Trailhead example, a regional custom price book carries a lower list price than the product's standard price to offset a tax incentive that customers in that region don't get.[^s4] Custom price books must be marked Active before reps can use them, and admins add products to them through the Price Book Entries related list, picking the currency and entering a list price for each entry.[^s5] Price Book is customizable like other objects, so a field such as a Region picklist can be added to categorize books.[^s5]

The data rules sit on `PricebookEntry`:[^s1]

- The standard price for a product must exist before any custom price for it can be loaded.[^s1]
- Create one entry for each standard or custom price and currency combination of a product in a book.[^s1]
- `UnitPrice` (label List Price) is required and can only be set when `UseStandardPrice` is false.[^s1]
- With `UseStandardPrice` true, the entry's price is read-only and tracks the standard price for that product and currency.[^s1]
- `Product2Id` and `Pricebook2Id` are required on create and can't be changed afterwards.[^s1]

## Price books on opportunities

An opportunity can have product line items only if it has a `Pricebook2`, and each `OpportunityLineItem` must point to a product listed in that opportunity's price book, so in practice one opportunity draws from one price book.[^s2] When reps add products they choose the price book and each product comes in at that book's price.[^s4] If the opportunity has no price book yet, adding a line item whose entry sits in an active price book of the matching currency makes the API set that price book on the opportunity automatically.[^s2] The line item's `ListPrice` mirrors the entry's `UnitPrice`, while its own `UnitPrice` (Sales Price) is the negotiated price, which lets reports compare the two.[^s2]

## Limits and gotchas

- Once line items exist, you can't change the opportunity's price book or its `CurrencyIsoCode`.[^s2]
- Price book entries can never be deleted; deactivate an entry (set `IsActive` to false) to retire it.[^s1]
- Under multicurrency, line items always carry the parent opportunity's currency, so the book needs an entry in that currency.[^s2]
- In Lightning, `ListPrice` on a line item isn't populated before insert; read it in an after-insert trigger instead.[^s2]
- `PricebookEntry` exists only when the org has the products feature enabled, and its `Name` and `ProductCode` come read-only from the product.[^s1]
- Apex tests can't see org data by default, so they call `Test.getStandardPricebookId()` to get the standard price book's ID before inserting standard-price entries.[^s3]

## When to use it (and when not)

Use a single standard price book when everyone pays the same price, and add custom price books only for prices that genuinely differ by market or customer type, as in the Trailhead project that splits nonprofit and enterprise pricing.[^s5] An entry holds a single list price per product, book and currency, and the negotiated figure lives on each line item's Sales Price.[^s1][^s2] Tiered discounts, bundles and rule-driven pricing therefore belong to the pricing products described under Connections, not to extra price books.

## Connections

Price books are **standard objects** (`kt:standard-objects`) at the heart of the **Sales Cloud** (`kt:sales-cloud`) quote-to-cash data model.[^s4] `PricebookEntry` links one product to one price book, much like a `kt:junction-object` resolves a many-to-many relationship.[^s1] Price books **enable** `kt:opportunity-products`, since line items can exist only on an opportunity with a price book, and they **depend on** `kt:multiple-currencies` when an org prices in more than one currency.[^s2] They are **consumed by** `kt:salesforce-cpq` and `kt:salesforce-pricing` in `kt:revenue-cloud`, which build discounting and pricing logic on top of list prices. Test code that touches products relies on the `kt:apex-testing` helper for the standard price book ID.[^s3]

## Sources

[^s1]: Salesforce Developers, "PricebookEntry | Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_pricebookentry.htm (accessed 2026-11-10)
[^s2]: Salesforce Developers, "OpportunityLineItem | Object Reference for the Salesforce Platform". https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunitylineitem.htm (accessed 2026-11-10)
[^s3]: Salesforce Developers, "Test Class | Apex Reference Guide". https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_test.htm (accessed 2026-11-10)
[^s4]: Trailhead, "Create Price Books to Track Your Products". https://trailhead.salesforce.com/en/sales_admin_products_quotes_contracts/sales_admin_products_quotes_contracts_unit_1 (accessed 2026-11-10)
[^s5]: Trailhead, "Manage Products, Prices, Quotes, and Orders: Create Custom Price Books". https://trailhead.salesforce.com/content/learn/projects/manage-products-prices-quotes-orders/create-custom-price-books (accessed 2026-11-10)
