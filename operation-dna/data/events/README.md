# Events

One file per material event. Suggested fields:

```yaml
id: event-YYYYMMDD-xxxx
type: contract|filing|earnings|regulatory|product|market|macro
occurred_at: ISO-8601
entities: [entity-id]
summary: concise factual description
impact: -1.0 to 1.0
novelty: 0.0-1.0
relevance: 0.0-1.0
confidence: 0.0-1.0
sources: [source-id]
```

Events are immutable evidence records. Corrections should create a new revision rather than silently rewriting history.
