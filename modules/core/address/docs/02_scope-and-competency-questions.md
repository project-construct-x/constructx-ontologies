# Scope and Competency Questions for the Address Module

**Status:** Domain-reviewed and implemented  
**Version:** 0.2.0  
**As of:** 19 November 2026  
**Scope:** `core/address`

## 1. Purpose

The module describes structured addresses and the assignment of an address to a resource. It separates the location from its domain-specific use, for example as a delivery or billing address.
## 2. Confirmed Scope

- structured components of an address,
- location assignments with at least one role,
- countries and administrative areas as referencable resources,
- optional linkage to a geographic position.
    

## 3. Out of Scope

Contact channels, persons, organizations, coordinate models, and formatted postal addresses are not defined within the Address module.
## 4. Competency Questions
1. Which address is assigned to a resource?
2. Which role does this assignment have?
3. In which country and administrative area is the address located?
4. Is a geographic position linked to the assignment?

## 5. Example

> A company uses the same address for both billing and delivery purposes. The  
> street address is stored only once; the two purposes are represented on the  
> location assignment.

```text
Company -> LocationAssignment -> Address in Bochum
              |
              +-> Billing address
              +-> Delivery address
```

## 6. Modeling Decisions

The address itself remains free of recipient-specific and usage-specific data. Roles and  
recipient-specific notes are represented on `LocationAssignment`. The complete  
modeling decisions are documented in the conceptual model.

## 7. Acceptance Criteria

The scope is fulfilled if address, assignment, and role remain separated and  
the core shapes validate the required relationships.
