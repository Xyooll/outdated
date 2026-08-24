# Homeostasis and Invariants

The system must preserve defined operating boundaries while adapting.

## Protected invariants
- credential and secret isolation
- permission boundaries
- audit logging
- data integrity and provenance
- maximum resource and financial exposure
- mandatory validation gates
- backup and recovery requirements
- rollback capability
- approved execution destinations

AI may propose changes to protected policies, but cannot silently change or disable them. Changes require explicit authorization through the appropriate control path.

## Principle
Adaptation changes behavior inside the safety envelope; it does not redefine the envelope without authorization.