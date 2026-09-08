# Konzeptmodell des Identifier-Moduls

**Status:** Fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/identifier`

## 1. Zweck

Das Modell beschreibt die gemeinsame Struktur einer fachlichen Kennung.

## 2. Modell in einfachen Worten

Eine Fachressource verweist auf einen Identifier. Der Identifier trägt genau
einen Kennungswert und kann die verantwortliche Schema-Agentur nennen.

## 3. Begriffe

| Begriff | Bedeutung |
| --- | --- |
| `adms:Identifier` | eigenständige Kennungsressource |
| `adms:identifier` | Beziehung vom Fachobjekt zur Kennung |
| `skos:notation` | eigentlicher Kennungswert |
| `adms:schemaAgency` | optionale herausgebende Stelle |

## 4. Beziehungen

Die Fachmodule definieren, welche Ressourcen `adms:identifier` verwenden. Das
Identifier-Modul prüft anschließend die Struktur des Zielwertes.

## 5. Verständliches Beispiel

```turtle
ex:firma adms:identifier ex:register-id .
ex:register-id
    a adms:Identifier ;
    skos:notation "HRB 1234" ;
    adms:schemaAgency "Amtsgericht Bochum" .
```

## 6. Abgrenzung

Ressourcen-IRI, fachliche Kennung und Identitätsnachweis sind unterschiedliche
Sachverhalte.

## 7. Entscheidungen

Es werden keine lokalen Kennungsbegriffe eingeführt. Der Vertrag bleibt klein
und fachübergreifend.
