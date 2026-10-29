# Glossary of the Address Module

**Status:** Technically approved and implemented  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Scope:** `core/address`

## 1. Purpose

This glossary provides a concise introduction to the concepts defined in the T-Box. The complete definitions are available in `ontology/conx-addr.ttl`.

## 2. Namespace

```
https://www.construct-x.org/ontology/address#
```

The prefix used is `conx-addr`.

## 3. Classes

|Class|Description|
|---|---|
|`Address`|Structured postal address|
|`AddressAssignment`|Assignment of an address to a resource|
|`AddressRole`|Intended purpose of an address assignment|
|`AdministrativeTerritory`|Administrative territory|
|`Country`|Country|
|`AdministrativeArea`|Administrative subdivision within a country|

## 4. Relationships

| Property | Description |
| --- | --- |
| `hasAddressAssignment` | Links a resource to a contextual address assignment |
| `assignedAddress` | Links an assignment to exactly one address |
| `addressRole` | States one or more business purposes of the assignment |
| `hasCountry` | Links an address to its country |
| `hasAdministrativeArea` | Links an address to a relevant administrative area |
| `broaderAdministrativeTerritory` | Links an area to a broader area or country |
| `hasGeographicPosition` | Optionally links an address to an external geographic position |

## 5. Address Attributes

| Property | Description |
| --- | --- |
| `streetName` | Street or thoroughfare name without the house number |
| `additionalStreetName` | Additional street name used for more precise identification |
| `houseNumber` | House, building, or property number |
| `blockName` | Name of a spatial block or comparable unit |
| `buildingName` | Proper or commonly used building name |
| `buildingPart` | Section, wing, tract, hall, or similar building part |
| `floor` | Floor or level within a building |
| `room` | Room, suite, or comparable unit |
| `internalDeliveryPoint` | Internal delivery point within a building or site |
| `postOfficeBoxNumber` | Identifier of a post office box |
| `localityName` | Locality, city, municipality, or settlement name |
| `citySubdivisionName` | City, locality, or municipal subdivision name |
| `postalCode` | Postal code or comparable postal-area identifier |
| `plotIdentifier` | External identifier of a plot or land parcel |
| `departmentName` | Department or organizational unit using the assignment |
| `attentionOf` | Addressee instruction meaning "for the attention of" |
| `careOf` | Addressee instruction meaning "care of" |

## 6. Illustrative Example

```
ex:company conx-addr:hasAddressAssignment ex:deliveryAddress .
ex:deliveryAddress
    conx-addr:assignedAddress ex:addressBochum ;
    conx-addr:addressRole roles:DeliveryAddressRole .
```

In this example, the company has a delivery address assignment that references the actual address in Bochum.

## 7. External Concepts

Identifiers are represented using ADMS and SKOS. Specific address roles and administrative territories are maintained in separately versioned reference datasets.
