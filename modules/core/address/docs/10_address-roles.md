# Controlled Address Role Vocabulary

The Construct-X Address Ontology defines only the type of an address role through `conx-addr:AddressRole`. Specific roles are maintained separately as a versioned SKOS reference vocabulary:

```text
Vocabulary IRI: https://www.construct-x.org/vocab/address-role
Version IRI:    https://www.construct-x.org/vocab/address-role/0.2.0
Namespace:      https://www.construct-x.org/vocab/address-role#
Prefix:         roles
Version:        0.2.0
```

Source file: `datasets/reference/vocabularies/address-roles/address-roles.ttl`

## Roles in Version 0.2.0

| Role resource                       | German                                         | English                          | Notation                   | Source                       |
| ----------------------------------- | ---------------------------------------------- | -------------------------------- | -------------------------- | ---------------------------- |
| `roles:DeliveryAddressRole`         | Lieferadresse                                  | Delivery address                 | `delivery`                 | `cac:DeliveryAddress`        |
| `roles:InvoiceAddressRole`          | Rechnungsadresse                               | Invoice address                  | `invoice`                  | ---                          |
| `roles:PostalAddressRole`           | Postanschrift                                  | Postal address                   | `postal`                   | `cac:PostalAddress`          |
| `roles:RegistrationAddressRole`     | Registrierungsadresse; alternativ Meldeadresse | Registration address             | `registration`             | `cac:RegistrationAddress`    |
| `roles:ReturnAddressRole`           | Rücksendeadresse                               | Return address                   | `return`                   | `cac:ReturnAddress`          |
| `roles:ResidenceAddressRole`        | Wohnadresse                                    | Residence address                | `residence`                | `cac:ResidenceAddress`       |
| `roles:ConstructionSiteAddressRole` | Baustellenadresse                              | Construction site address        | `construction-site`        | ---                          |
| `roles:ConstructionSiteAccessRole`  | Baustellenzufahrtsadresse                      | Construction site access address | `construction-site-access` | ---                          |
| `roles:LegalAddressRole`            | Rechtliche Adresse                             | Legal address                    | `legal`                    | Gaia-X `legalAddress`        |
| `roles:HeadquartersAddressRole`     | Hauptsitzadresse                               | Headquarters address             | `headquarters`             | Gaia-X `headquartersAddress` |
| `roles:PhysicalLocationAddressRole` | Physische Standortadresse                      | Physical location address        | `physical-location`        | Gaia-X `location`            |

## Distinction from UBL

The English labels of the five directly corresponding roles follow the terminology of OASIS UBL 2.5 CS01. This reference provides terminological and domain-specific guidance, rather than a formal equivalence assertion between a SKOS concept and an XML Schema element.

UBL uses `cac:RegistrationAddress` for both the registered address of a legal entity and the tax-registered address of a party. `roles:RegistrationAddressRole` combines these contexts into a general registration role. The German alternative label “Meldeadresse” facilitates its use for addresses recorded by public authorities without equating residential and registered addresses.

UBL has no standalone `cac:InvoiceAddress` element. In the UBL model, invoicing parties and their addresses are represented through their respective contexts. Therefore, `roles:InvoiceAddressRole` remains a Construct-X-specific term. The same applies to the two construction-specific roles.

UBL 2.5 also includes `cac:DespatchAddress` as the address of despatch or collection. This role was not added to the approved initial set without an explicit request and remains a documented candidate for extension.

## Gaia-X Guidance

The three roles added in version `0.2.0` represent the address uses defined in Gaia-X. `LegalAddressRole` is deliberately kept separate from `RegistrationAddressRole` because a legally authoritative address is not identical to a registered address in every legal and application context. The optional Gaia-X alignment maps the roles to the Gaia-X predicates in a machine-readable form.

## Modeling Rules

Each role is both a `conx-addr:AddressRole` and a `skos:Concept`. An `AddressAssignment` may have multiple roles if all other details of the assignment apply jointly to those roles. If the department, recipient instruction, or validity differs, multiple assignments are created for the same address.

The open core model also permits roles from other controlled vocabularies. A strict SHACL profile may later require the roles used to belong to the Construct-X concept scheme `https://www.construct-x.org/vocab/address-role`.
