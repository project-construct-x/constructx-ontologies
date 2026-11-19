# Construct-X Contact Channels

Controlled reference vocabulary for communication channels of `conx-contact:ContactMethod`.

## Version 0.1.0

Included channels:

- `contact-channel:email`
- `contact-channel:phone`
- `contact-channel:mobilePhone`
- `contact-channel:fax`
- `contact-channel:website`
- `contact-channel:messenger`
- `contact-channel:socialProfile`
- `contact-channel:postalAddress`

Postal contact methods do not reference address components directly; they reference a `conx-addr:AddressAssignment` through `conx-contact:usesAddressAssignment`.
