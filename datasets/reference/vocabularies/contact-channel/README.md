# Construct-X Contact Channels

Kontrolliertes Referenzvokabular fuer Kommunikationskanaele von `conx-contact:ContactMethod`.

## Version 0.1.0

Enthaltene Kanaele:

- `contact-channel:email`
- `contact-channel:phone`
- `contact-channel:mobilePhone`
- `contact-channel:fax`
- `contact-channel:website`
- `contact-channel:messenger`
- `contact-channel:socialProfile`
- `contact-channel:postalAddress`

Postalische Kontaktmethoden verweisen nicht direkt auf Adressbestandteile, sondern ueber `conx-contact:usesAddressAssignment` auf eine `conx-addr:AddressAssignment`.
