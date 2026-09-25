# User Concept — Pipes use Pointers and Wrappers

Date: 2026-09-24
Status: **ACTIVE / CORE FLOWARE ARCHITECTURE**

## USER-STATED

Pipes may be handled using pointers and wrappers.

The intended terms are **Pointers** and **Wrappers**.

## SYSTEM INTERPRETATION

This reuses an architectural pattern already present in Relational Story.

Canonical Pipe representation:

~~~text
PIPE
=
ENDPOINT POINTERS
+
CONNECTION WRAPPER
+
LIVE PIPE STATE
~~~

Pointer:

> Where is the canonical underlying object/state?

Wrapper:

> What does the relationship mean here and what rules govern its use?

Pipe:

> The governed connection formed from the endpoint references, relationship-specific wrapper, and current operational state when needed.

Important distinction:

~~~text
POINTER != PIPE
WRAPPER != PIPE

POINTERS + WRAPPER + LIVE CONNECTION STATE
→ PIPE
~~~

## SYSTEM CONSEQUENCE

Canonical contract:
- `floware/PIPE-CONTRACT.md`

Canonical glossary:
- `floware/GLOSSARY.md`

High-risk Meta Plumbing:
- `floware/meta/PLUMBING.md`

High-risk stock Plumbing:
- `domains/stock-market/PLUMBING.md`

This allows Patching to traverse explicit Pipes, Sequencing to derive readiness/order from Pipe properties, and Audit to inspect Pipe/Plumbing integrity independently.
