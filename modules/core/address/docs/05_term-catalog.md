# Glossary of the Address Module

**Status:** Technically approved and implemented  
**Version:** 0.3.0  
**As of:** 26 November 2026  
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
|`LocationAssignment`|Assignment of an address, a geolocation, or both to a resource|
|`LocationRole`|Intended purpose of a location assignment|
|`AdministrativeTerritory`|Administrative territory|
|`Country`|Country|
|`AdministrativeArea`|Administrative subdivision within a country|

## 4. Relationships

| Property | Description |
| --- | --- |
| `hasLocationAssignment` | Links a resource to a contextual location assignment |
| `hasAssignedAddress` | Links an assignment to at most one address |
| `hasLocationRole` | States one or more business purposes of the assignment |
| `hasCountry` | Links an address to its country |
| `hasAdministrativeArea` | Links an address to a relevant administrative area |
| `hasBroaderAdministrativeTerritory` | Links an area to a broader area or country |
| `hasGeoReference` | Optionally links an assignment to one geographic reference (IRI or blank node, type open) |

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

## 6. Illustrative Example

```
ex:company conx-addr:hasLocationAssignment ex:deliveryAddress .
ex:deliveryAddress
    conx-addr:hasAssignedAddress ex:addressBochum ;
    conx-addr:hasLocationRole roles:DeliveryAddressRole .
```

In this example, the company has a delivery location assignment that references the actual address in Bochum.

## 7. External Concepts

Identifiers are represented using ADMS and SKOS. Specific address roles and administrative territories are maintained in separately versioned reference datasets.
