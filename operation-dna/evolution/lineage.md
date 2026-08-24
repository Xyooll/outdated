# Evolutionary Lineage

Stable and experimental versions are treated as separate lineages.

```text
STABLE
  ├── experiment-A
  ├── experiment-B
  └── experiment-C
          ↓
      evaluation
          ↓
   promote / reject
          ↓
       STABLE
```

Every promotion records parent version, candidate version, evaluation evidence, performance deltas, risk assessment, and rollback target.

The stable lineage is never replaced without a recoverable prior version.