# Construct-X Agent Core-Modul

**Status:** Draft, fachlich bestätigt und implementiert  
**Version:** 0.1.0  
**Stand:** 3. September 2026

## 1. Kurzbeschreibung

Das Modul stellt mit `conx-agent:Agent` eine gemeinsame Oberklasse für Personen
und Organisationen bereit.

## 2. Verständliches Beispiel

> Eine Beteiligung kann von einer Person oder Organisation wahrgenommen
> werden. Beide sind Agenten und können daher über dieselbe Beziehung
> referenziert werden.

```text
Participation -> Agent <- Person
                       <- Organization
```

## 3. Modellumfang

Der Core enthält genau eine Klasse und keine eigenen Properties. Konkrete
Stammdaten bleiben in Person, Organization, Contact und Address.

## 4. Dokumentation

Der zentrale Einstieg ist [docs/index.md](docs/index.md). Die gemeinsame Form
aller Core-Dokumentationen beschreibt der
[Dokumentationsstandard](../DOCUMENTATION.md).

## 5. Technische Artefakte

- Ontologie: `ontology/conx-agent.ttl`
- Core Shapes: nicht erforderlich
- Fachliche Spezifikation: `docs/agent-specification.md`
- Tests: repositoryweite Agent-Ontologietests
