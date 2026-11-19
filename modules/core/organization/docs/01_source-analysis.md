# Source Analysis for the Organization Ontology

**Status:** Consolidated analysis baseline  
**Version:** 0.1.0  
**As of:** 3 September 2026  
**Research cutoff date:** 27 August 2026  
**Scope:** `core/organization`  
**Subject:** Organizations, legally registered entities, and organization-related self-descriptions

## 1. Purpose and Method

This analysis evaluates existing ontologies, exchange formats, register models, and project requirements as the domain foundation for the implemented Construct-X module `core/organization`. In particular, it addresses:

- which organization types must be distinguished,
- which information constitutes organizational master data,
- which information applies only within a process, role, or business relationship,
- which identifiers must be structured and distinguished by their scheme,
- which statements should be modeled as time-bound evidence or credentials rather than simple properties,
- which existing Construct-X modules should be reused,
- which sources are suitable as conceptual foundations, alignment targets, mapping sources, or merely indicators of requirements.

The sources are not weighted equally. A class or cardinality is not adopted solely because it appears in a particular exchange format or Gaia-X profile.

## 2. Source Hierarchy

| Source Type | Relevance to Construct-X | Examples |
| --- | --- | --- |
| Normative or broadly reusable conceptual model | Foundation for classes, relationships, and conceptual distinctions | W3C Organization Ontology, SEMIC Core Business Vocabulary, existing Construct-X architecture |
| Official register, code, or verification model | Foundation for identification schemes, controlled values, and verification procedures | BRIS/EUID, VIES, GLEIF/LEI, ISO 20275, NACE, BZSt, EORI |
| Industry or exchange format | Source of required fields and mappings, but not automatically of ontology structure | UBL, GS1, eForms |
| Broad web or alignment vocabulary | Source of established concepts and interoperability | Schema.org, FOAF, GoodRelations |
| Specialized model | Analysis source and future alignment target for a relevant use case | FIBO, W3C VC, DID Core |
| Internal project requirements indicator | Provides possible attributes and processes, but has no normative modeling authority | Self-description table, 1Lieferschein format, current Delivery Note ontology |

### 2.1 Binding Treatment of 1Lieferschein

The Delivery Note ontology and its conceptual model currently in the repository are **work in progress and not a source of truth for `core/organization`**. In particular, existing classes such as `Buyer`, `Seller`, `Shipper`, `Carrier`, or `Party` must not be copied into the Organization ontology.

The 1Lieferschein format is evaluated for information purposes only:

- Which actors must be referenced in delivery processes?
- Which organization, location, contact, and identifier data is actually required in data exchange?
- Which contextual identifiers occur between business partners?

Answers to these questions indicate requirements; they do not imply adoption of the current Delivery Note modeling.

## 3. Summary of Findings

Two complementary sources provide the main conceptual foundations:

1. The [W3C Organization Ontology](https://www.w3.org/TR/vocab-org/) represents general organizations, formal organizations, organizational units, hierarchies, memberships, roles, posts, and sites.
2. The [SEMIC Core Business Vocabulary 2.3.0](https://semiceu.github.io/Core-Business-Vocabulary/releases/2.3.0/) represents registered legal entities with a legal name, legal form, legal identifier, activity, registration date, and registered address. It is compatible with the ADMS identifier model already established in the project.

The [Gaia-X class `LegalPerson`](https://docs.gaia-x.eu/ontology/development/classes/LegalPerson/), added by the user, is an important alignment and self-description profile. However, it is insufficient as a general organization model: its mandatory information and cardinalities are Gaia-X-specific, even its `name` is optional, and it groups very different identifiers under `registrationNumber`.

The following domain layers therefore emerge for Construct-X:

- `Organization` for an organized collective actor,
- `LegalEntity` for legally registered entities with legal capacity,
- `OrganizationalUnit` for units meaningfully identified only within an organization,
- role or participation assignments for sellers, buyers, carriers, manufacturers, and similar process roles,
- external evidence resources for compliance, qualifications, insurance, and time-dependent status statements once a specific use case exists.

`org:FormalOrganization` remains an external alignment target and is not introduced as a local Construct-X class.

The local term `LegalEntity` is preferable to `LegalPerson`. It avoids confusion with natural persons in `core/person` while still allowing alignment with `legal:LegalEntity` and `gx:LegalPerson`.

## 4. Sources Evaluated

| Source | Version Used | Role | Provisional Use |
| --- | --- | --- | --- |
| [W3C Organization Ontology](https://www.w3.org/TR/vocab-org/) | W3C Recommendation, 2014 | General organizational structure | Primary reference for organization, unit, hierarchy, membership, role, post, and site |
| [SEMIC Core Business Vocabulary](https://semiceu.github.io/Core-Business-Vocabulary/releases/2.3.0/) | 2.3.0, SEMIC Recommendation of 12 May 2026 | Registered legal entities | Primary reference for Legal Entity, legal name, legal form, registration, and ADMS identifiers |
| [Gaia-X LegalPerson](https://docs.gaia-x.eu/ontology/development/classes/LegalPerson/) | Development version, accessed 2026-08-27 | Gaia-X self-description | Alignment and profile source; not adopted unchanged |
| [Schema.org Organization](https://schema.org/Organization) | Development version, accessed 2026-08-27 | Web interoperability | Source for naming, fields, and alignment |
| [OASIS UBL 2.5 CS01](https://docs.oasis-open.org/ubl/cs01-UBL-2.5/) | 2.5 CS01 | Business and document exchange | Field analysis and mapping source for `Party`, `PartyLegalEntity`, registers, and financial accounts |
| [GS1 Web Vocabulary: Organization](https://ref.gs1.org/voc/Organization) | Continuously maintained, accessed 2026-08-27 | Supply chains and GS1 identification | Reference for GLN, organization names, and supply-chain interoperability |
| [GS1 GLN Data Model](https://www.gs1.org/standards/gln-data-model-solution-standard/current-standard) | Current standard | Legal entity, function, and location | Typed use of GLNs; not every GLN is interpreted as a Legal Entity ID |
| [GLEIF LEI Model in RDF](https://www.gleif.org/en/lei-data/semantic-representation-of-the-lei/lei-model-in-rdf-resource-description-framework) | Continuously maintained | Legal entities, LEI, and ownership relationships | Reference and possible alignment for LEI data |
| [GLEIF ISO 20275 ELF Code List](https://www.gleif.org/about-lei/code-lists/iso-20275-entity-legal-forms-code-list) | February 2026 version | Legal forms by jurisdiction | Preferred controlled vocabulary for legal forms |
| [EU eProcurement Ontology](https://docs.ted.europa.eu/EPO/latest/conceptual.html) | 5.2, accessed 2026-08-27 | Procurement roles and actors | Reference for contextual Agent roles |
| [EU eForms Parties](https://docs.ted.europa.eu/eforms/latest/schema/parties.html) | Current version | Organizations and role-specific touchpoints | Supports separation of organization, role, and contact point |
| [FOAF](https://xmlns.com/foaf/spec/) | 0.99 | Minimal Agent model | Alignment through `core/agent`; insufficient as an organization core |
| [GoodRelations](https://www.heppnetz.de/ontologies/goodrelations/v1.html) | 1.0 | E-commerce businesses and identifiers | Historical alignment source, now largely overlapping with Schema.org |
| [FIBO](https://spec.edmcouncil.org/fibo/index.html) | Current published version | Financial, ownership, and control structures | Future specialized reference; too extensive for the MVP |
| [ADMS 2.0](https://semiceu.github.io/ADMS/releases/2.00/) | 2.0 | Structured identifiers | Reuse according to the Construct-X identifier architecture |
| [W3C Verifiable Credentials Data Model](https://www.w3.org/TR/vc-data-model/) | 2.0 Recommendation | Issuer, subject, validity, status, and evidence | Foundation for external evidence, not organizational master data |
| [W3C DID Core](https://www.w3.org/TR/did-core/) | 1.0 Recommendation | Decentralized identifiers and control | DID as a technical identifier, not proof of legal existence |
| [NACE Rev. 2.1](https://ec.europa.eu/eurostat/web/nace) | Used for European statistics since 2025 | Classification of economic activities | Preferred European classification for business activities |
| [VIES](https://europa.eu/youreurope/business/finance-and-tax/vat/check-vat-number-vies/index_en.htm) | Accessed 2026-08-27 | Verification of EU VAT identifiers | External verification procedure with a documented time and result |
| [BRIS Business Search](https://e-justice.europa.eu/topics/registers-business-insolvency-land/business-registers-search-company-eu/general-information-find-company_en) | Accessed 2026-08-27 | Interconnection of national business registers | Verification of register data and EUID within its coverage |
| [EORI](https://taxation-customs.ec.europa.eu/customs/customs-procedures-import-and-export/customs-operations/economic-operators-registration-and-identification-number-eori_en) | Accessed 2026-08-27 | Customs identifier | Conditional identifier for parties involved in customs operations, not a universal organization requirement |
| [BZSt on the Business Identification Number](https://www.bzst.de/SharedDocs/Downloads/DE/Presse/20241104_einfuehrung_widnr.pdf?__blob=publicationFile&v=3) | Introduction and distinction of the W-IdNr. | German tax identifiers | Demonstrates the need to distinguish W-IdNr., USt-IdNr., and tax number |
| [EU SME Definition](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32003H0361) | Recommendation 2003/361/EC | SME criteria | Foundation for a time-dependent classification, not a simple core Boolean |
| [EU Regulation 651/2014](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32014R0651) | Particularly Article 2(18) and Annex I | Undertakings in difficulty and SMEs | Context-dependent legal assessment, not master data |
| [EU Sanctions Resources](https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures/overview-sanctions-and-related-resources_en) | Continuously updated | Sanctions lists and legal acts | Source for dated checks, not a permanent compliance Boolean |

The following internal project sources were also evaluated:

- [Identifier Model](../../../../docs/architecture/identifier-model.md)
- [Agent Specification](../../agent/docs/10_agent-specification.md)
- [Address Roles](../../address/docs/10_address-roles.md)
- [Contact Source Analysis](../../contact/docs/01_source-analysis.md)
- The user-provided table “Ideas for the Self-Description of Organizations.”

## 5. Analysis of Organization Classes

### 5.1 `Organization`

The W3C Organization Ontology describes an organization as a deliberately structured social entity. It can act as an Agent, have members, operate at sites, and be divided into parent or subordinate units. This fits the existing Construct-X class `Agent` and is broader than a legal person.

Examples include companies, public authorities, associations, consortia, and other organized collectives. An organization need not itself be entered in a public register or have separate legal personality.

### 5.2 `FormalOrganization`

`org:FormalOrganization` describes organizations generally recognized in the world that can, for example, enter into contracts, hold accounts, or bear legal responsibility. This class is suitable as an external semantic layer between a general organization and a specifically registered `LegalEntity`.

Construct-X introduces no local class with the same name. The local core uses `Organization` and `LegalEntity` directly; alignment of `LegalEntity` with `org:FormalOrganization` remains the responsibility of an alignment module.

### 5.3 `LegalEntity` Rather than a Local `LegalPerson`

SEMIC describes `legal:LegalEntity` as an entity with legal capacity that is registered with a competent authority and appears in a business register. Gaia-X describes a `LegalPerson` uniquely identified by at least one registration number.

Construct-X uses `LegalEntity` because:

- The term is less likely to be confused with `core/person`.
- It can be mapped directly to SEMIC and aligned with Gaia-X.
- It makes clear that not every `Organization` is a registered legal entity.
- It prevents branches, departments, or temporary consortia from automatically being treated as separate legal persons.

Sole traders and self-employed natural persons remain instances of `core/person:Person` in the MVP. Although the EU SME definition regards an economically active natural person as an enterprise regardless of legal form, this implies neither separate legal personality nor membership of the class `Organization`.

Construct-X therefore introduces no local class `EconomicActor`. The concept was a possible local abstraction, but is not a class directly adopted from the evaluated core ontologies. Economic activity by a person or organization is described through a contextual Agent role in a business process. A dedicated business profile resource is reserved for a future requirement if several separate business activities of the same person must be distinguished.

### 5.4 `OrganizationalUnit`

An organizational unit derives its meaning from a parent organization. Department, division, branch, and plant are not generally synonymous:

- A department is typically an organizational unit.
- A branch may be an organizational unit, a registered business subdivision, or both.
- A plant or depot is often primarily a site with an organizational function.
- A permanent establishment is a location concept shaped by legal and tax considerations, rather than automatically a separate organization.

The implemented model therefore keeps organizational units and locations separate; linking them remains the responsibility of an appropriate location model.

### 5.5 Roles Are Not Organization Subclasses

Seller, buyer, shipper, recipient, carrier, customer, manufacturer, and collecting party are roles within a particular delivery, contract, or product context. EU ePO uses an `AgentInRole` pattern; eForms maintains organization data centrally and references the organization from the respective role context.

This supports the implemented Construct-X pattern:

| Resource | Property | Target |
| --- | --- | --- |
| `AgentRoleAssignment` | `assignedAgent` | Organization or Person |
| `AgentRoleAssignment` | `role` | Controlled role value |
| `AgentRoleAssignment` | `context` | Delivery note, consignment, item, contract, or project |

An organization can therefore be both seller and shipper in the same transaction without being created twice as a master data object or typed as two classes.

## 6. Detailed Source Assessment

### 6.1 W3C Organization Ontology

**Strengths**

- Clear general organization concept,
- `FormalOrganization` and `OrganizationalUnit`,
- parent/suborganization relationships,
- direct and reified memberships,
- roles, posts, and sites,
- established connection to the Agent concept.

**Limitations**

- No detailed register, tax, or LEI data,
- no fully developed legal form model,
- no compliance or credential semantics.

**Assessment:** The strongest structural reference, but insufficient on its own as a complete Legal Entity core.

### 6.2 SEMIC Core Business Vocabulary

SEMIC focuses on formally registered legal entities. Relevant concepts include:

- legal name and alternative name,
- legal identifier and other identifiers,
- legal form,
- registered address,
- registration date,
- business activity,
- contact point,
- legal status and power of attorney.

The distinction between a general identifier and a legal identifier assigned by a competent authority is particularly valuable. Identifiers are structured using ADMS and may carry a notation, scheme, issuer, and issue date.

**Assessment:** The strongest domain source for the `LegalEntity` component. Its scope is narrower than `Organization`, however, because informal organizations and internal units are not its main focus.

### 6.3 Gaia-X `LegalPerson`

Gaia-X currently requires a `LegalPerson` to have:

- at least one `registrationNumber`,
- exactly one `legalAddress`,
- exactly one `headquartersAddress`.

The documentation lists local register identifiers, EUID, EORI, VAT ID, and LEI as permitted registration numbers. Relationships with parent and subordinate legal persons are also provided.

**Useful Contributions**

- Legal identity requires at least one reliable register or authority identifier.
- Legal and headquarters addresses are distinct roles.
- International identification schemes must be distinguished explicitly.
- Group or mandate relationships are relevant to self-descriptions.

**Critical Issues**

- VAT ID, EORI, and LEI are not universal registration numbers for every legal entity.
- `name` is only `0..1` and is not explicitly the registered name; this is too weak for a general Legal Entity profile.
- Exactly one legal and headquarters address is a Gaia-X profile decision, not a general ontological truth. Multiple assignments relevant to different times, languages, or jurisdictions must remain possible in principle.
- In the current development documentation, some descriptions of `parentOrganizationOf` and `subOrganisationOf` appear to run counter to their property names. They must not be adopted without checking.
- The documentation is a development version; IRIs and semantics may change.

**Assessment:** An important alignment target and future Gaia-X SHACL profile, but not a direct template for the Construct-X T-Box.

### 6.4 Schema.org

Schema.org covers a wide range of fields through `legalName`, `legalAddress`, `legalRepresentative`, `companyRegistration`, `leiCode`, `vatID`, `taxID`, `iso6523Code`, `parentOrganization`, `subOrganization`, `department`, `member`, `employee`, `foundingDate`, `contactPoint`, and `location`.

The properties frequently have very broad ranges, and many identifiers are represented directly as strings. This is practical for web markup, but insufficiently structured for verifiable master data. `iso6523Code` is useful as an international identifier reference; Construct-X should nevertheless use the established ADMS pattern and, where appropriate, maintain ISO 6523 ICD as an identification scheme.

**Assessment:** An excellent naming and alignment source, but not a normative basis for cardinalities or quality requirements.

### 6.5 UBL

Within its `Party` aggregate, UBL separates:

- `PartyIdentification`,
- `PartyName` and trading name,
- postal address,
- tax information,
- `PartyLegalEntity`,
- contact,
- financial account.

`PartyLegalEntity` includes registration name, company ID, registration address, registration scheme, and headquarters party. The registration scheme may carry an identifier, name, type, and jurisdiction. `FinancialAccount` represents account identifier, account name, account type, currency, and further banking information as a separate aggregate.

**Assessment:** UBL supports the required fields and the separation of legal entity, address, contact, and account. As an XML exchange schema, however, it is neither an ontology import nor a template for the class hierarchy.

### 6.6 GS1 and GLN

GS1 is particularly relevant to supply chains and therefore to 1Lieferschein. Depending on its type, a GLN may identify a legal entity, function, physical location, or digital location. Consequently:

- GLN is an important identification scheme for Construct-X.
- The mere existence of a GLN does not prove that its subject is a `LegalEntity`.
- The identifier and the type of resource identified must be validated together.
- Location GLNs belong to locations; functional GLNs may belong to organizational units or function resources.

### 6.7 GLEIF, LEI, and Legal Forms

The LEI dataset distinguishes Level 1 data (“who is who”) from Level 2 relationships (“who owns whom”). Level 1 includes legal name, legal and headquarters addresses, register and register identifier, legal form, creation date, and status.

The GLEIF RDF ontologies are valuable for future LEI and corporate group alignments. The February 2026 version of the ISO 20275 ELF list contains more than 3,600 legal forms across more than 200 jurisdictions. It is therefore preferable to an invented local legal-form string.

An LEI must nevertheless not become universally mandatory. It exists only for entities that have applied for one or require one under regulation.

### 6.8 ePO and eForms

ePO and eForms provide two particularly important patterns for Construct-X:

1. Roles such as Buyer or Winner are contextual roles of an organization.
2. Role-specific contact information is maintained through separate touchpoints when it differs from general organizational contacts.

eForms also distinguishes technical document identifiers from official organization identifiers. Multiple identifiers issued by legal authorities are possible. Requirements for name, address, website, and contact vary by role and procedure.

**Assessment:** Strong support for defining mandatory information in SHACL profiles for specific application roles rather than globally in OWL.

### 6.9 FOAF, GoodRelations, and FIBO

- FOAF provides only a very small Agent and Organization concept and is already relevant through `core/agent`.
- GoodRelations contains established e-commerce concepts such as legal name, VAT ID, tax ID, DUNS, and GLN. Many have since been incorporated into Schema.org.
- FIBO provides highly detailed models for legal entities, ownership, control, and financial organizations. Its import and conceptual complexity would be disproportionate for an initial Construct-X organization core.

These sources are suitable as future alignments or detailed references, rather than the primary import foundation of the MVP.

## 7. Evaluation of the Self-Description Table

### 7.1 Names, Legal Form, and Addresses

| Input | Source Findings | Critical Assessment | Provisional Model Assignment |
| --- | --- | --- | --- |
| Mandatory name | SEMIC: `legalName`; Schema.org: `legalName`; UBL: `RegistrationName` | Appropriate for a strict `LegalEntity` self-description profile. A general `Organization` requires at least a designation, but not necessarily a registered name. | `legalName` for Legal Entity; general `name` for Organization |
| Mandatory legal form | SEMIC `legalFormType`; GLEIF/ISO 20275 | Applies only to legal entities where a distinct legal form is applicable. Local free text alone is insufficient for reliable verification. | Reference to a controlled legal-form concept; free text at most as supplementary information |
| Mandatory legal address | Gaia-X, SEMIC, UBL, and GLEIF provide registered/legal addresses | Plausible as a profile requirement. Street and building number are not always available internationally; mandatory components must depend on jurisdiction. | Existing `core/address` with `LegalAddressRole` |
| Headquarters address | Gaia-X and GLEIF distinguish it from the legal address | Not always different and not mandatory in every profile. The same address may have both roles. | `LocationAssignment` with `HeadquartersAddressRole` |

Construct-X must not define new properties for street, building number, postal code, or locality in `core/organization`. These are provided by `core/address`. An Organization profile may require at least one appropriate `LocationAssignment` and require the referenced address to satisfy a jurisdiction-specific address profile.

### 7.2 Authorized Representatives

The table structure `title, given name, family name, date of birth, place` should not be embedded directly in the organization. An authorized representative remains a resource from `core/person`. Representation is a separate, potentially time-bound relationship with at least:

- represented organization,
- representing person or organization,
- representation type or role,
- sole or joint representation where required,
- legal basis or register reference,
- validity period,
- optional evidence.

Date and place of birth are personal data and must not routinely be repeated as public organizational master data. If a register comparison requires them, they belong in an access-controlled verification procedure or credential. BRIS confirms that registers may provide information about legal representatives; actual availability depends on the register and document.

### 7.3 Identification Numbers

| Identifier in the Table | Scope | Mandatory Status | Modeling and Verification |
| --- | --- | --- | --- |
| USt-IdNr. / VAT ID | VAT registration, particularly within the EU internal market | Not universally mandatory | `adms:Identifier` with VAT scheme and jurisdiction; VIES check as a dated verification result |
| “Tax ID” | Too imprecise for organizations | Unusable in this form | In Germany, distinguish W-IdNr., USt-IdNr., and tax number; do not reuse a natural person's personal identification number |
| LEI | Financial market and voluntary LEI registration | Required only where available or mandated by regulation | `adms:Identifier` with LEI scheme; verification against GLEIF |
| EUID | Companies and branches connected through BRIS within its scope | Only for covered register cases | `adms:Identifier` with EUID scheme; verification against BRIS or the source register |
| Commercial register entry | Registered entities under the relevant jurisdiction | Conditionally mandatory | Identifier plus register scheme, register authority, and jurisdiction; do not require a court as a universal model feature |
| EORI | Economic operators involved in customs operations | Only for customs contexts | `adms:Identifier` with EORI scheme; external EORI validation |
| GLN | GS1-identified entity, function, or location | Only when GS1 is used | Check the identification scheme and GLN type against the resource identified |
| DID | Any DID subject and controlled verification methods | Optional | Technical or controlled identifier; legal binding established separately |
| NorthData, Schufa, Creditreform ID | Provider- or platform-specific record | Optional and does not establish trust | Generic external identifier with scheme and provider; no dedicated core property per provider |

The input table simultaneously requires VAT ID, tax ID, LEI, and EUID. This is incorrect as a general rule: the identifiers have different scopes, and not every organization can possess them. A future Self-Description Shape should instead require:

1. at least one legally reliable identifier from an approved scheme,
2. an identification scheme appropriate to the jurisdiction and organization type,
3. additional identifiers only where the relevant use case requires them,
4. separate verification reports for external register queries.

### 7.4 Activity and Classification

`Start of activity`, establishment, and register entry are distinct:

- `foundingDate` typically refers to establishment,
- `registrationDate` refers to registration,
- `activityStartDate` refers to the actual start of economic activity.

Before `start of activity` becomes mandatory, it must be clarified which statement is intended and which register reliably provides it. SEMIC offers `registrationDate`, and Schema.org offers `foundingDate`; a separate activity start date would be an additional Construct-X requirement.

NACE Rev. 2.1 is the natural reference for classifying economic activities in Europe. Classification should be modeled as a controlled concept with a version and, where applicable, primary or secondary activity, rather than an untyped string.

### 7.5 Account Information

IBAN, account holder, and BIC are not intrinsic properties of an organization. UBL represents a financial account as a separate aggregate. Accounts may also:

- be associated with multiple organizations,
- apply only to particular payments, contracts, or currencies,
- be managed by payment service providers,
- be security-sensitive and require access restrictions.

Recommendation: exclude these from the Organization core. A future Payment/Finance module or contract profile should own `FinancialAccount` and the time- or purpose-bound account assignment.

### 7.6 Status and Compliance Statements

| Table Entry | Why Not a Simple Core Boolean? | Recommended Representation |
| --- | --- | --- |
| Undertaking not in difficulty | The EU concept depends on legal form, capital, losses, insolvency, age, and state-aid context. Absence from an insolvency register is insufficient. | Dated assessment or credential with legal basis, assessor, and validity |
| Compliance with Russia sanctions | Sanctions regimes and lists change; ownership, control, goods, and transactions may also be relevant. | Screening result with checked lists/regimes, time, assessor, and subject scope |
| SME status | Depends on employees, turnover/balance sheet, and linked or partner enterprises. | Time-bound classification or credential referencing the EU definition and reporting period |
| Entitlement to deduct input VAT | Depends on tax law, jurisdiction, period, and transaction | Tax evidence or credential; not generally inferred in OWL |
| Creditworthiness | Depends on provider, assessment date, and methodology | External assessment with provider, date, scale, and validity; not derived from a provider ID |

Cryptographic verifiability of a credential establishes only integrity, issuer, and, where applicable, status. The W3C VC Data Model explicitly provides no guarantee that the substantive claim is true or sufficient for the specific decision process. The verifier still requires a trust and verification policy.

### 7.7 Memberships, Insurance, and Qualifications

Memberships are relationships rather than simple organization properties. A membership should keep together at least the organization, receiving organization, membership type, membership number, period, and status. The membership number identifies the membership within the association's context and is not necessarily a global organization identifier.

A statutory accident insurance institution, association, and guild can therefore use the same basic pattern. Evidence may be linked as a separate credential.

Insurance confirmations, authorization to submit building documents, and public appointment are also external evidence whose validity depends on time and scope. At least the following are relevant:

- holder or credential subject,
- issuer,
- evidence type,
- validity start and end,
- status or revocation,
- domain-specific and geographic scope,
- referenced regulations or schema.

These do not belong in the initial Organization core as built-in classes or Booleans.

### 7.8 Website and DID

Schema.org and eForms provide both websites and contact points. Construct-X uses the existing Contact model: an official homepage is a website contact method on a contact point with `contact-usage:official` and `contact-purpose:general`. Role-specific web pages may have separate contact points. No dedicated homepage property is required in the Organization module.

Comparing legal notices, domain holders, and register data is a verification procedure. It cannot be replaced by a simple SHACL regular expression.

A `did:web` technically demonstrates control over the corresponding web path, rather than automatically establishing the identity of the registered entity. Binding the DID to a legal identifier requires trustworthy evidence or a traceable register/credential chain.

### 7.9 Assessment of the Proposed Verification Rules

| Verification Goal | Checkable with OWL/SHACL | External Verification | Result to Store |
| --- | --- | --- | --- |
| Name, legal form, and legal address are complete | Presence, datatypes, controlled legal form, and LocationAssignment | Comparison with the competent source register; BRIS only within its coverage | Register, retrieval time, entity found, fields compared, match result |
| VAT ID is present and formally appropriate | Scheme, notation, and country-specific pattern | VIES or competent national authority; VIES searches national data and does not provide names/addresses in every country | Time, requester, status, confirmed name/address where available; technical errors separated from “invalid” |
| LEI is present and active | LEI scheme and formal format | GLEIF record or API | LEI status, legal name, register reference, checked dataset version |
| EUID or national registration number is present | Scheme, notation, register, and jurisdiction | BRIS or national register | Register, EUID/register ID, status, retrieval date, and field comparison |
| Website belongs to the organization | URI syntax and a profile's HTTPS policy | Legal notice, register comparison, domain check, and possibly DNS/certificate verification | Checked URL, method, time, identity attributes found, and result |
| DID is controlled by the organization | DID syntax and referenceable DID Document | Challenge or signature verification plus separate binding to legal identity | DID, verification method, challenge time, and identity evidence |
| No relevant sanctions match | Only the presence of a structured screening result | Screening against current lists relevant to the jurisdiction and transaction, including ownership and control where applicable | Lists/regimes, version or retrieval date, search parameters, result, assessor, and validity |
| SME status or “not in difficulty” | Completeness of an assessment and its legal basis | Calculation or domain assessment using financial, personnel, ownership, and insolvency data | Reporting period, inputs, ruleset version, result, issuer, and validity |

A timeout or unavailable register must not be stored as “identifier invalid” or “verification passed.” Technical verification outcome, domain-level match, and trust decision are three separate levels.

## 8. Informative Requirements from 1Lieferschein

The following needs can be derived from the current project state without treating the Delivery Note ontology as a reference model.

### 8.1 Required Actor Roles

- Creator or issuer,
- seller,
- shipper,
- buyer,
- recipient,
- carrier,
- customer or originator,
- manufacturer,
- collecting party.

This list demonstrates the need for reusable organizations and contextual roles. It does not demonstrate a need for organization subclasses with the same names.

### 8.2 Required Organizational Information

- Legal name and, where applicable, trading name,
- party and register identifiers,
- addresses and physical locations,
- sites, plants, depots, or branches,
- general and role-specific contacts,
- organizational units,
- business-partner-specific numbers such as customer, supplier, cost center, construction site, location, or tenant numbers.

The final group in particular is **not organizational master data**. For example, a customer account number is assigned by a seller to a customer and applies only within that business relationship. Such identifiers belong to a participation, partner, or contract assignment with an issuing organization and context.

## 9. Provisional Module Boundaries

| Module | Responsible For | Not Responsible For |
| --- | --- | --- |
| `core/agent` | Common superclass `Agent` | Organizational structure and legal data |
| `core/organization` | Organization, Legal Entity, Organizational Unit, general hierarchy, membership, and legal representation | Address components, contact channels, bank accounts, evidence content, delivery roles, and posts in the MVP |
| `core/person` | Natural person and intrinsic core data | Representation relationship with an organization |
| `core/address` | Address and role-based `LocationAssignment` | Organizational hierarchy |
| `core/contact` | Contact point, contact method, purpose, and usage context | Organizational role and membership |
| Existing `core/participation` | Agent role in a delivery note, project, contract, or other context | Organizational master data |
| External evidence systems | Evidence referenced as needed for insurance, qualifications, membership, or compliance | No dedicated Construct-X Credential module has been approved for the MVP |
| Future Payment/Finance module | Bank account and purpose-specific account assignment | General organization |
| Domain modules | Domain-specific roles, profiles, and mandatory information | Duplicates of Person, Organization, Contact, and Address |

Importing `core/address` or `core/contact` into the Organization T-Box is not automatically necessary. The modules can be used together in a data or SHACL profile. This keeps the Organization ontology small and avoids unnecessary import coupling.

## 10. Provisional Core Terms

The following list is an analysis outcome, not yet a binding term catalog.

### 10.1 Likely Classes

- `Organization`
- `LegalEntity`
- `OrganizationalUnit`
- `Membership`
- `LegalRepresentation`

### 10.2 Likely Core Properties

- General name,
- legal name,
- alternative or trading name,
- legal form,
- registration date,
- economic activity or classification,
- parent and subordinate organization,
- organizational unit affiliation,
- ADMS identifiers,
- references to existing LocationAssignments and ContactPoints in profiles.

An official homepage is represented through the existing Contact model as a website contact method with `contact-usage:official` and `contact-purpose:general`. It requires no dedicated property in the Organization module.

### 10.3 Excluded from the Initial Organization Core

- IBAN, BIC, and account holder,
- general compliance Booleans,
- credit ratings and credit scores,
- embedded personal data of authorized representatives,
- delivery roles such as Buyer, Seller, or Carrier,
- customer, supplier, tenant, and cost-center numbers without relationship context,
- insurance, membership, and qualification evidence as flat properties,
- a local class `EconomicActor` or `FormalOrganization`,
- W3C ORG `Post` or a local post in the MVP,
- a dedicated Credential module without a confirmed cross-module requirement,
- a local replacement class for `adms:Identifier`.

## 11. Implications for Profiles and Validation

Mandatory information primarily belongs in SHACL profiles rather than the general OWL T-Box. At least three levels are expected:

1. **Organization Core:** minimal structural consistency for arbitrary organizations.
2. **Legal Entity Core:** legal name, registration date, suitable structured identifier, and the legal-location assignment still to be assessed; legal form remains optional in the MVP.
3. **Future Self-Description Profiles:** stricter use-case- or jurisdiction-specific requirements, including current register verification and required evidence.

Jurisdiction-specific profiles are outside the MVP. Future profiles may cover Gaia-X, delivery processes, procurement, or national register requirements. For example, a Gaia-X profile can require exactly one legal and headquarters address without asserting this cardinality for every organization worldwide.

External checks such as VIES, GLEIF, BRIS, EORI, domain verification, or sanctions screening are not pure SHACL constraints. SHACL can check that a structured verification result with date, status, and verification service is present. The actual live query requires a separate validation service.

## 12. Consolidated Decisions

| Topic | MVP Decision |
| --- | --- |
| Economic actor | No local class `EconomicActor` or `Enterprise`; economic activity is described through contextual Agent roles |
| Sole traders and freelancers | Remain `Person`; no automatic typing as `Organization` or local `LegalEntity` |
| Formal organization | No local class `FormalOrganization`; assess future alignment of `LegalEntity` with W3C ORG |
| Organization part or location | Separate legal personality leads to `LegalEntity`; organizational classification leads to `OrganizationalUnit`; a physical place remains a separate location resource |
| Membership | Included in version 0.1.0 as a separate relationship resource |
| Post / `Post` | Outside the MVP; introduced only upon a confirmed need for permanent positions that may also be vacant |
| Legal representation | Included in `core/organization` as a relationship resource between `LegalEntity` and `Person` |
| Identification schemes | ADMS structure in the MVP; no incorrect universal mandatory list of VAT ID, LEI, EUID, and EORI |
| Jurisdictions | Jurisdiction-specific allowlists and verification profiles addressed after the MVP |
| Homepage | Reuse of `core/contact` as an official general website contact |
| Credentials | No dedicated Credential module in the MVP; external evidence connected only when specifically required |
| Personal data of authorized representatives | Reference to a `Person` only; no duplication of name, date of birth, or place of birth |
| Date concept | `registrationDate` for registration of a `LegalEntity`; no ambiguous `activityStartDate` in the MVP |

The specific alignment IRIs, controlled legal-form and activity vocabularies, and future selection of national register and identification schemes remain open, but do not block the domain specification of the MVP.

## 13. Overall Assessment

The Organization ontology should not be built from the long attribute list of a self-description. Much of the table describes identifiers within particular regimes, relationships, accounts, assessments, or time-bound evidence rather than the organization itself.

A robust core emerges from combining W3C ORG and SEMIC Core Business Vocabulary, supplemented by alignments with Gaia-X, Schema.org, GS1, GLEIF, and ePO. UBL, eForms, and 1Lieferschein provide valuable requirements for mappings and application profiles. Registers and verification services provide evidence, but must not be conflated with ontology semantics.

The most important architectural decision is therefore:

> Organizational identity, process role, relationship, contact, address, and verifiable evidence are separate resources or modules combined in application-specific profiles.

This keeps `core/organization` reusable while allowing it to support the network's strict self-description, Gaia-X, and delivery-process requirements.

## 14. Illustrative Mapping Example

> A commercial register provides the legal name, registration date, and identifier. Organization adopts this master data, but does not model the external register check itself as part of the organization.
