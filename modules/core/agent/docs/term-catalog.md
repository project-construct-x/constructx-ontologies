# Begriffskatalog des Agent-Moduls

**Status:** Implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026  
**Geltungsbereich:** `core/agent`

## 1. Zweck

Der Katalog dokumentiert den bewusst minimalen öffentlichen Begriffsumfang.

## 2. Namensraum

`https://www.construct-x.org/ontology/agent#` mit dem Präfix `conx-agent`.

## 3. Klassen

| Klasse | Definition |
| --- | --- |
| `conx-agent:Agent` | Entität, die handeln, Verantwortung tragen oder als Beteiligter referenziert werden kann |

## 4. Properties

Das Modul definiert keine eigenen Properties.

## 5. Kontrollierte Werte

Das Modul besitzt kein Referenzvokabular.

## 6. Verständliches Beispiel

```turtle
ex:anna a conx-person:Person .
```

Da `Person` eine Unterklasse von `Agent` ist, kann `ex:anna` überall verwendet
werden, wo ein Agent erwartet wird.

## 7. Ausschlüsse

Spezialisierte Agententypen werden nur bei einem bestätigten fachlichen Bedarf
in ihren zuständigen Modulen ergänzt.
