# Synthetic non-stock example — documentation delivery

This is an explanatory trace with known answers, not an independent test or live persistence demonstration.
Objective: prepare a documentation bundle by a supplied deadline; no publishing permission.
Calling Flows: existing Development and Pipeline Integrity. No new domain activation.

## Initial inputs and recorded dependencies

- E1@v1: synthetic brief says deadline October 2.
- E2@v1: synthetic style guide says use plain language.
- A@v1: delivery schedule, consumes E1@v1.
- B@v1: terminology guide, consumes E2@v1.
- C@v1: final bundle, consumes A@v1 and B@v1.
- D@v1: verification of C@v1, consumes C@v1 and the governing contracts.

Record R1 contains those read sets, references, analysis-only authority and current Pipe states.
In an actual run, R1 is accepted only after a storage receipt and matching read-back.

## Interruption and changed evidence

Resume finds E1@v2: deadline is now September 30. E2 is unchanged.

| Item | Disposition | Reason |
|---|---|---|
| A@v1 | INVALIDATED | Its deadline input changed. |
| B@v1 | RETAINED | Its only material input, E2@v1, is unchanged; no deadline-dependent content. |
| C@v1 | INVALIDATED | It consumes the obsolete schedule. |
| D@v1 | INVALIDATED | Verification covers the obsolete bundle. |

CONT-03/07 load the checkpoint; CONT-04 sends the change to Evidence Refresh;
CONT-06 returns the impact dispositions to Pipeline Integrity.
Existing Sequencing starts epoch 2, schedules A@v2 before C@v2, and permits C@v2 to reuse B@v1 with recorded compatibility.
Candidate C@v2 waits for new independent Audit through existing Meta Plumbing.
If none is available, status remains VERIFICATION_PENDING.
CONT-01/02 record R2, linked to R1; no historical record is rewritten.

## Negative and positive controls

- A request to publish derived from analysis-only state stays BLOCKED pending actual authority.
- HIGH confidence remains HIGH; it never becomes an invented numerical probability.
- An unknown outcome for an interrupted upload blocks a retry until reconciled.
- Missing dependency evidence blocks claims that the unaffected subgraph is known.
- A stale audit cannot verify a changed bundle.
- With unchanged inputs and current authority, valid completed analysis may be reused; no blanket rerun.
- Failed checkpoint read-back leaves R1 as the accepted head.
- Unchanged short tasks continue through Direct Resolution without the continuity extension.
