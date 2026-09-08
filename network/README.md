# Abhaengigkeiten der Core-Ontologien

Dieser Bereich dokumentiert die externen Ontologien und Namespaces, die von den
bereitgestellten Construct-X Core-Modulen verwendet werden.

Die Datei `imports.lock.yaml` haelt die belegbaren Abhaengigkeiten des
Core-only-Repositorys fest. Lokale Beziehungen zwischen Core-Modulen und
Shape-Sets stehen verbindlich in den jeweiligen `module.yaml`-Dateien.

## Grundsaetze

- Externe Begriffe werden ueberwiegend referenziert und nicht vollstaendig
  importiert.
- Die Shape-Graphen von Person, Organization und Document importieren den
  lokalen versionierten Identifier-Shape-Vertrag.
- Referenzvokabulare werden getrennt von den Ontologie-T-Boxen gepflegt.
- Domain-Ontologien, anwendungsspezifische Profile und optionale Alignments
  gehoeren nicht zum Lieferumfang dieses Repositorys.

Eine zusammengefuehrte `construction-x.ttl` wird derzeit nicht erzeugt. Jedes
Core-Modul bleibt eigenstaendig versionierbar und auslieferbar.
