# Construct-X Address Roles

This directory contains the controlled address-role vocabulary for the Construct-X Address Ontology. As an A-Box reference dataset, it is separate from the T-Box at `modules/core/address/ontology/conx-addr.ttl`.

<a id="kennung-und-version"></a>

## Identification and Version

```text
Vocabulary IRI: https://www.construct-x.org/vocab/address-role
Version IRI:    https://www.construct-x.org/vocab/address-role/0.3.0
Namespace:      https://www.construct-x.org/vocab/address-role#
Prefix:         roles
Version:        0.3.0
Status:         draft
```

The stable vocabulary IRI identifies the `skos:ConceptScheme`. Each specific role has a permanent IRI in the role namespace and is an instance of both `conx-addr:LocationRole` and `skos:Concept`.

<a id="inhalt"></a>

## Contents

Version `0.3.0` contains eleven roles. German labels are retained alongside their English equivalents:

| German | English |
| --- | --- |
| Lieferadresse | Delivery address |
| Rechnungsadresse | Invoice address |
| Postanschrift | Postal address |
| Registrierungsadresse | Registration address |
| Rücksendeadresse | Return address |
| Wohnadresse | Residence address |
| Baustellenadresse | Construction site address |
| Baustellenzufahrtsadresse | Construction site access address |
| rechtliche Adresse | Legal address |
| Hauptsitzadresse | Headquarters address |
| physische Standortadresse | Physical location address |

The registration address role also has the alternative German label `Meldeadresse`.

Labels, definitions, and stable notations are provided directly in `address-roles.ttl`. New roles are added to this reference vocabulary and do not require changes to the Address T-Box.

<a id="ubl-orientierung"></a>

## UBL Guidance

The English preferred labels for Delivery, Postal, Registration, Residence, and Return follow the corresponding Address elements in OASIS UBL 2.5 CS01. UBL describes `cac:RegistrationAddress` in both company-registration and tax-registration contexts; the Construct-X concept combines these uses into a general registration role.

No direct CAC address term was identified in UBL 2.5 for `InvoiceAddressRole`, `ConstructionSiteAddressRole`, or `ConstructionSiteAccessRole`. These roles are therefore documented as Construct-X-specific terms. The roles `LegalAddressRole`, `HeadquartersAddressRole`, and `PhysicalLocationAddressRole` follow Gaia-X. In particular, no equivalence is asserted with a UBL element merely used in a similar way.

UBL 2.5 also contains `cac:DespatchAddress`, defined as a dispatch or collection address. A corresponding Construct-X role is not part of version `0.1.0` and may be added following a domain decision.

Source: [OASIS UBL 2.5 CS01 Common Aggregate Components](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/xsd/common/UBL-CommonAggregateComponents-2.5.xsd)

<a id="verwendung"></a>

## Usage

```turtle
@prefix conx-addr: <https://www.construct-x.org/ontology/address#> .
@prefix ex: <https://example.org/id/> .
@prefix roles: <https://www.construct-x.org/vocab/address-role#> .

ex:site-access-assignment
    a conx-addr:LocationAssignment ;
    conx-addr:assignedAddress ex:gate-3-address ;
    conx-addr:locationRole roles:ConstructionSiteAccessRole,
                          roles:DeliveryAddressRole .
```

All other details of a `LocationAssignment` apply jointly to every role linked to it. If, for example, the department, delivery instruction, or validity differs by role, separate assignments to the same address are used.

<a id="pflege"></a>

## Maintenance

- Notations and IRIs are not reused for other meanings.
- Removed roles are deprecated rather than silently deleted.
- New roles require German and English preferred labels and definitions.
- Direct UBL references are documented only when a corresponding UBL term actually exists.

