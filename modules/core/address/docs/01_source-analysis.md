# Source Analysis: Address Models in vCard, Schema.org, and UBL 2.5

**Status:** Consolidated analysis baseline\
**Version:** 0.2.0\
**As of:** 19 November 2026\
**Research cutoff date:** 13 August 2026\
**Scope:** `core/address`

## 1. Purpose and Scope

This report compares the address concepts from three source models. It documents the original basis for the decisions underlying the Construct-X Address Ontology, which has since been implemented. The authoritative specifications are provided in the current conceptual model and the T-Box.

The analysis distinguishes between:

- address components themselves,
- inherited or associated contact and geographic information,
- the role of an address in a transaction or process, such as a delivery or registration address,
- formal model characteristics such as cardinalities, ordering, and multilingual support.

## 2. Sources Examined

1. [W3C vCard Ontology](https://www.w3.org/TR/vcard-rdf/), W3C Interest Group Note dated 22 May 2014, namespace `http://www.w3.org/2006/vcard/ns#`.
2. [Schema.org PostalAddress](https://schema.org/PostalAddress) and [Schema.org Data Model](https://schema.org/docs/datamodel.html), development version V30.0 dated 19 March 2026, accessed on 13 August 2026.
3. Local file `D:\Sciebo\Construction-X Privat\200_Arbeitspakete\300_Arbeitspaket_3\400_AP3.4\2026-07-07_Lieferschein_Ontologie\UBL-CommonAggregateComponents-2.5.xsd`, UBL 2.5 Committee Specification 01 dated 15 April 2026. SHA-256: `CE667698A58840658811CD3A2C763DCA18985FEA454D379D0DA11B891B347478`. Comparable official sources are the [UBL 2.5 specification](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/UBL-2.5.html) and the [official Common Aggregate Components XSD](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/xsd/common/UBL-CommonAggregateComponents-2.5.xsd).

## 3. Summary of Findings

| Source     | Primary Purpose                                                      | Granularity         | Main Strength                                                                                                  | Key Limitation                                                                                                                         |
| ---------- | -------------------------------------------------------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| vCard RDF  | Contact information for people, organizations, groups, and locations | Compact             | Established RDF/OWL model and straightforward linking of an address to an object                               | Only five current direct address components; post office box and extended address are deprecated                                       |
| Schema.org | Broadly applicable web markup                                        | Compact to moderate | Widespread practical adoption, straightforward JSON-LD use, and support for countries and regions as resources | Deliberately flexible model without mandatory fields or address-specific cardinalities; inherits contact fields unrelated to addresses |
| UBL 2.5    | Structured exchange of business and logistics data                   | Very detailed       | 28 address components, roles within business processes, codes, free-text lines, and geographic coordinates     | Oriented towards XML and exchange formats; some terms overlap semantically or are closely tied to postal and business processes        |

No single source fully meets the needs of Construct-X. vCard and Schema.org are well suited to interoperability in RDF and web environments. UBL provides the broadest set of domain-specific fields, but its structure should not be adopted unchanged as an ontology structure.
## 4. Comparison of Concepts

| Semantic Concept | vCard RDF | Schema.org | UBL 2.5 | Assessment for Subsequent Modeling |
| ---------------- | --------- | ---------- | ------- | --------------------------------- |
| Address object | `vcard:Address` | `schema:PostalAddress` | `cac:Address` / `AddressType` | A common core exists; Schema.org and vCard focus on an address suitable for postal delivery, whereas UBL defines general address information. |
| Link to the entity holding the address | `vcard:hasAddress` with range `vcard:Address` | `schema:address`; additionally, specialized relationships such as `billingAddress` and `deliveryAddress` | Various ASBIE elements such as `PostalAddress`, `DeliveryAddress`, and `RegistrationAddress` | The role is more appropriately attached to the relationship between an entity and an address than to the address itself. |
| Address type | Typing of an address object using, among others, `vcard:Home` or `vcard:Work` | No direct field; inherited `contactType` applies to contact points in general | `cbc:AddressTypeCode` | These should not be equated prematurely: private/business use, delivery purpose, and domain-specific address type are different dimensions. |
| Identity | RDF IRI of the address object; no dedicated current address ID field | RDF/JSON-LD `@id` or inherited `schema:identifier` | `cbc:ID` with an identification scheme | An address-specific identifier and global IRI identity should remain separate. |
| Address format | No field | No field | `cbc:AddressFormatCode` | UBL-specific addition, potentially useful for rendering or exchange profiles. |
| Street address as combined text | `vcard:street-address` | `schema:streetAddress` | `cac:AddressLine/cbc:Line` as an unstructured line | The two RDF sources do not separate street name and building number. A direct mapping to UBL `StreetName` would therefore be lossy. |
| Street name | Only within the combined text | Only within the combined text | `cbc:StreetName` | UBL provides the most granular structured representation. |
| Additional street name | No current field | At most, represented nonspecifically through `extendedAddress` | `cbc:AdditionalStreetName` | Relevant for international addresses and locally used alternative names. |
| Building number | Only within the combined text | Only within the combined text | `cbc:BuildingNumber` | Likely to be an important separate component for construction and logistics use cases. |
| Building/block name | No field | At most, `extendedAddress` | `cbc:BuildingName`, `cbc:BlockName` | UBL distinguishes physical location components more clearly. |
| Subunit within a building | No current field; `extended-address` is deprecated | `extendedAddress` for an apartment, c/o, or alternative name | `cbc:Floor`, `cbc:Room`, `cbc:InhouseMail` | A single extension field supports interoperability, while separate components provide greater precision. Both representations may be needed in parallel. |
| Post office box | `post-office-box` is deprecated | `postOfficeBoxNumber` | `cbc:Postbox` | Schema.org and UBL continue to represent post office boxes explicitly. |
| Free-text address lines | No current `label`; `label` is deprecated | Through `streetAddress` or `extendedAddress`, but without an ordered line structure | `cac:AddressLine` 0..n; each existing AddressLine contains `cbc:Line` 1..n | An ordered free-text representation should be considered for lossless import and country-specific printed formats. |
| Internal delivery / recipient instruction | Not an address component | Partly represented nonspecifically in `extendedAddress` | `cbc:Department`, `cbc:MarkAttention`, `cbc:MarkCare`, `cbc:InhouseMail` | UBL does not fully separate addresses from postal delivery instructions. For Construct-X, it needs to be clarified whether these details belong to the address or to the addressing of a shipment. |
| Locality / municipality | `vcard:locality` | `schema:addressLocality` | `cbc:CityName` | Close semantic correspondence. The concept should not be restricted to legally designated cities. |
| City subdivision | No dedicated field | No dedicated field | `cbc:CitySubdivisionName` | Potentially relevant for large construction sites, neighborhoods, and international addresses. |
| District | Only loosely represented through `region` | Only loosely represented through `addressRegion` | `cbc:District` | UBL provides an additional administrative level. |
| State / province / administrative unit | `vcard:region` as text, with state or province as examples | `schema:addressRegion` as `AdministrativeArea` or text | `cbc:CountrySubentity` as text and `cbc:CountrySubentityCode` as a code | This is the closest domain-level correspondence. UBL `Region` is not automatically equivalent to vCard/Schema.org `region`. |
| Larger geographic or economic region | No separate field | No separate direct field | `cbc:Region` | In UBL, a recognized geographic or economic region or group of countries, not necessarily an administrative level. |
| Postal code | `vcard:postal-code` | `schema:postalCode` | `cbc:PostalZone` | Direct correspondence; model as text to preserve leading zeros and letters. |
| Country | `vcard:country-name` as text | `schema:addressCountry` as `schema:Country` or text; alpha-2 is recommended | `cac:Country` with `cbc:IdentificationCode` and `cbc:Name` | Construct-X should support both a referenceable country resource and code/text representations. |
| Plot / land parcel | No field | No direct field | `cbc:PlotIdentification` | Particularly relevant to Construction-X, but semantically it may be better represented as a relationship to a land parcel object than as a simple address literal. |
| Geographic coordinates | `vcard:hasGeo` or a GEO parameter outside the five direct Address components; legacy latitude/longitude data fields are deprecated | Not directly in `PostalAddress`; usually represented through `Place` and `GeoCoordinates` | `cac:LocationCoordinate` 0..n with coordinate system, degrees/minutes, direction, and altitude | Address and geographic position should be linked, but not equated. The coordinate model should reuse a modern geospatial model that supports coordinate reference systems (CRSs). |
| Time zone | `vcard:tz` on the described entity or as a parameter | No direct address field | `cbc:TimezoneOffset` | A current UTC offset is less stable than a named time zone; UBL explicitly defines the offset at the time of exchange. |
| Description | Generally available through other vocabularies; no dedicated Address field | Inherited `schema:description` | `cbc:Description` 0..n | A generic description should not be conflated with a formatted address line. |
| Multilingual support | vCard parameter mechanism using `language`; additionally, direct and n-ary properties | General RDF language-tagged literals are possible, but there is no address-specific mechanism | Repetition of selected fields is explicitly intended only for the same content in multiple natural languages | Language variants require clear semantics and must not be mistaken for multiple substantively different values. |
| Contact information | Email, telephone, and address are separate vCard properties | As a subclass of `ContactPoint`, `PostalAddress` inherits, among others, email, telephone, fax, and opening hours | `ElectronicAddress` is a separate UBL concept; the postal address contains no telephone or email fields | For Construct-X, physical addresses and communication channels should remain separate concepts. |

## 5. Model Analysis by Source

### vCard RDF

`vcard:Address` describes the components of a delivery address. Its current direct core consists of:

- `vcard:street-address`
- `vcard:locality`
- `vcard:region`
- `vcard:postal-code`
- `vcard:country-name`

All five properties have `xsd:string` as their range. `vcard:hasAddress` is an object property with `vcard:Address` as its range. Additional n-ary `has...` properties exist for the five components, allowing vCard parameters such as language or sorting information to be represented.

The ontology's examples additionally type addresses as `vcard:Home` or `vcard:Work`. This classifies the use of the address but does not extend its components. Earlier fields for post office boxes, extended addresses, and formatted labels are explicitly marked as deprecated in the current ontology. The earlier direct fields for latitude and longitude have also been replaced by `vcard:hasGeo`.

The OWL class definition contains disjunctive existential and maximum-cardinality restrictions on the five core fields. This does not constitute a closed-world validation rule: under open-world semantics, vCard validates neither a complete postal address nor a particular national address format.

### Schema.org PostalAddress

`schema:PostalAddress` is a subclass of `schema:ContactPoint`, which in turn inherits from `schema:StructuredValue`. Seven properties are declared directly for `PostalAddress`:

- `schema:addressCountry`: `schema:Country` or text
- `schema:addressLocality`: text
- `schema:addressRegion`: `schema:AdministrativeArea` or text
- `schema:extendedAddress`: text
- `schema:postOfficeBoxNumber`: text
- `schema:postalCode`: text
- `schema:streetAddress`: text

Inheritance additionally makes general contact and `Thing` properties available, including `telephone`, `email`, `faxNumber`, `contactType`, `identifier`, `name`, and `description`. These are technically applicable to `PostalAddress`, but they do not automatically constitute components of a physical address.

By default, Schema.org specifies no mandatory fields and allows multiple values for every property. According to its own data model, the stated domains and ranges are usage recommendations rather than strict rules. This makes the model robust for web data, but insufficient on its own for binding Construct-X validation.

### UBL 2.5 AddressType

UBL models `AddressType` as an Aggregate Business Information Entity in an XML Schema. The order of the following elements is defined by `xsd:sequence`. At the `AddressType` level, all elements are optional.

| UBL Element | Cardinality | Meaning |
| ----------- | ----------- | ------- |
| `cbc:ID` | 0..1 | Address identifier within an agreed identification scheme |
| `cbc:AddressTypeCode` | 0..1 | Agreed code for the address type |
| `cbc:AddressFormatCode` | 0..1 | Agreed code for the address format |
| `cbc:Postbox` | 0..1 | Post office box number |
| `cbc:Floor` | 0..1 | Floor |
| `cbc:Room` | 0..1 | Room, suite, or apartment |
| `cbc:StreetName` | 0..n | Street name; repetition only for language variants |
| `cbc:AdditionalStreetName` | 0..n | Additional street name; repetition only for language variants |
| `cbc:BlockName` | 0..1 | Name of a block bounded by streets |
| `cbc:BuildingName` | 0..1 | Building name |
| `cbc:BuildingNumber` | 0..1 | Building number within the street |
| `cbc:Description` | 0..n | Explanatory description |
| `cbc:InhouseMail` | 0..1 | Internal delivery point within a building |
| `cbc:Department` | 0..1 | Recipient's department |
| `cbc:MarkAttention` | 0..1 | Recipient instruction meaning “for the attention of” |
| `cbc:MarkCare` | 0..1 | Recipient instruction meaning “c/o” |
| `cbc:PlotIdentification` | 0..1 | Identifier of the associated plot, such as a parcel number |
| `cbc:CitySubdivisionName` | 0..1 | City or locality subdivision |
| `cbc:CityName` | 0..n | City, town, or village; repetition only for language variants |
| `cbc:PostalZone` | 0..n | Postal identifier, such as a postal code |
| `cbc:CountrySubentity` | 0..n | Political or administrative subdivision as text |
| `cbc:CountrySubentityCode` | 0..1 | Political or administrative subdivision as a code |
| `cbc:Region` | 0..1 | Recognized geographic or economic region or group of countries |
| `cbc:District` | 0..1 | District or geographic subdivision |
| `cbc:TimezoneOffset` | 0..1 | UTC offset at the time of exchange |
| `cac:AddressLine` | 0..n | Unstructured address line; an existing AddressLine contains `cbc:Line` 1..n |
| `cac:Country` | 0..1 | Country with an optional identification code and name |
| `cac:LocationCoordinate` | 0..n | Geographic coordinates |

`LocationCoordinateType` supports a coordinate system code, latitude and longitude each expressed as degrees, minutes, and direction, and an altitude value. This format is detailed, but it is not identical to a modern point geometry from a geospatial vocabulary.

UBL 2.5 uses the same `AddressType` through twelve differently named global elements: `Address`, `ApplicableAddress`, `ApplicableTerritoryAddress`, `DeliveryAddress`, `DespatchAddress`, `JurisdictionRegionAddress`, `LocationAddress`, `OriginAddress`, `PostalAddress`, `RegistrationAddress`, `ResidenceAddress`, and `ReturnAddress`. The domain-specific role therefore arises from the context of use, rather than from twelve different subclasses of AddressType.

The UBL 2.5 change history highlights that the cardinalities of `StreetName`, `AdditionalStreetName`, and `CityName` were expanded from 0..1 in UBL 2.4 to 0..n. According to the field definitions, these repetitions represent the same content in multiple natural languages.

## 6. Critical Mapping Issues

1. `region` is not an unambiguous shared field. vCard and Schema.org typically refer to a state, province, or comparable administrative level. UBL primarily represents this through `CountrySubentity`; UBL `Region`, by contrast, can also refer to an economic region or group of countries.
2. `streetAddress` and `street-address` usually contain the street name and building number together. UBL `StreetName` contains only the street name. An unchecked `owl:equivalentProperty` assertion would therefore be incorrect.
3. vCard `Home`/`Work`, Schema.org `billingAddress`/`deliveryAddress`, and the UBL role elements model different types of context. A single “address type” field would conflate these meanings.
4. Schema.org's inherited telephone, email, and opening-hours fields are properties of a contact point, rather than spatial components of an address. They should not be included in the core of an address ontology solely because of inheritance.
5. UBL combines physical location components with delivery instructions such as department, “for the attention of,” and “c/o.” In the Construct-X ontology, these details could be modeled as separate addressing or delivery information.
6. An address can lead to a location, but it is neither identical to a location nor to coordinates. This is particularly relevant to post office boxes, construction site access points, land parcels, and temporary delivery points.
7. The three sources provide no shared, reliable rule for mandatory national address components. Such rules are more appropriately expressed in application-specific SHACL profiles than in the open core ontology.

## 7. Outcomes of the Domain Review

Based on the comparison, the following modeling directions were agreed:

1. The structured address is the authoritative representation. Unstructured or ordered address lines are not intended to serve as parallel primary data.
2. Building number, building, building part, floor, room, and internal delivery point should be representable individually.
3. Countries and administrative units are modeled exclusively as referenceable resources. Future A-Box graphs can provide these areas, their codes, names, and hierarchies.
4. The use of an address is modeled through a `LocationAssignment` with a referenceable `LocationRole`. Specific roles are maintained as an extensible A-Box vocabulary rather than as T-Box properties requiring continual additions.
5. Department, “for the attention of,” and “c/o” are included in the core as optional properties of the location assignment. Profiles can define stricter rules later.
6. The location assignment may reference a resource in an external geographic model through `hasGeoReference`. Coordinate and geometry details are deferred.
7. A formatted postal representation is explicitly not a primary data source and is not included as an Address property in the concept for version 0.1.0.
8. Use-case-specific minimum requirements will be addressed through profiles after the basic structure has been established.

The resulting classes, properties, domains, ranges, and examples are provided in the conceptual model.

## 8. Illustrative Mapping Example

> vCard, Schema.org, and UBL use different names for street and locality fields. In the Construct-X model, these source fields are mapped to the same structured address; recipient instructions remain attached to the location assignment.
