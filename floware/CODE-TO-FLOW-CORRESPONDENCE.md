# Code → Flow Correspondence

Status: **CANONICAL RESEARCH ARCHITECTURE / HYPOTHESIS UNDER TEST**

## Core hypothesis

Programming languages may be treated as different surface grammars over recurring computational structures.

Floware can attempt to map those structures into AI-native Flow concepts.

> **Do not translate syntax first. Translate purpose, state, relationship, constraint, and transition first.**

This does not assume every programming language can be converted losslessly.

Low-level semantics such as:
- memory layout;
- pointer aliasing;
- race conditions;
- real-time timing;
- undefined behavior;
- hardware registers;
- binary interfaces;
- resource lifetime

may require deterministic software representation or explicit hard-limit annotations.

## Translation layers

```text
SOURCE CODE
   ↓
SURFACE SYNTAX
   ↓
LANGUAGE SEMANTICS
   ↓
STRUCTURAL RELATIONSHIPS
   ↓
FLOW CORRESPONDENCE
   ↓
FLOWARE REPRESENTATION
   ↓
SOFTWARE HARD LIMITS WHERE REQUIRED
```

The important step is:

```text
LANGUAGE SEMANTICS
→ STRUCTURAL RELATIONSHIP
```

not:

```text
keyword
→ renamed keyword
```

## Initial correspondence map

| Programming concept | Structural meaning | Floware correspondence |
|---|---|---|
| variable | named changing state | state field / state slot |
| constant | invariant value | frozen constraint / fixed state |
| function | reusable transformation/action | Flow / Subflow |
| argument | supplied input | Flow input state |
| return value | produced result | output state |
| if / else | conditional route | gate / adaptive branch |
| switch / match | route among cases | router / state-dependent branch |
| loop | repeated evaluation/action | recurrence / re-evaluation cycle |
| break | stop current recurrence | local stop condition |
| continue | skip to next recurrence | recurrence advance |
| class | capability + state contract | Flow/state contract |
| object | instantiated state/capability | live instance |
| interface / protocol | required behavior contract | Flow contract / boundary contract |
| inheritance | structure reused from parent | inherited Flow contract / specialization |
| composition | capability built from parts | composed Flows |
| wrapper | encapsulation/adaptation around capability | adapter Flow / boundary Flow |
| decorator | behavior layered around another function | pre/post Flow layer |
| pointer | indirect reference to another location/object | reference edge / state pointer / correspondence link |
| reference | alias/access path | reference edge |
| import | bring external capability into scope | Flow dependency |
| module/package | grouped reusable capability | Flow package / library |
| namespace | naming boundary | domain / scope |
| exception | abnormal control transfer | fail-closed / recovery route |
| try/catch | guarded operation + recovery | protected Flow + recovery branch |
| event | occurrence that triggers logic | Flow trigger |
| callback | action invoked after another event | downstream Flow hook |
| promise/future | value not yet resolved | pending state / unresolved future state |
| queue | ordered pending work | pending Flow state |
| thread | concurrent execution path | concurrent Flow |
| process | isolated execution context | bounded Flow context |
| lock/mutex | exclusive access constraint | mutual-exclusion gate |
| transaction | all-or-nothing state change | atomic Flow boundary |
| database | persistent structured state | durable state/evidence store |
| cache | temporary reusable state | freshness-bounded state cache |
| API | external capability contract | external Flow boundary |
| compiler | translates one formal representation to another | Flow translator |
| interpreter | executes representation directly | Flow executor |
| runtime | environment enforcing execution semantics | execution substrate / hard-limit layer |
| type | allowable form/contract of data | state contract |
| generic/template | parameterized structure | reusable Flow pattern |
| recursion | capability invokes itself on reduced/new state | recursive Flow |
| state machine | explicit states/transitions | native Flow state graph |
| graph edge | relation between entities/states | correspondence/dependency edge |

## Wrappers

A wrapper does not necessarily change the underlying capability.

It changes:
- how it is entered;
- what is checked;
- what is added before/after;
- how outputs are exposed.

Floware correspondence:

```text
UNDERLYING FLOW
      ↑
ADAPTER / WRAPPER FLOW
      ↑
CALLER
```

This is similar to:
- legal procedural framing;
- interface layers;
- translation boundaries;
- domain adapters.

## Pointers and references

A pointer/reference is structurally:

> **A way to reach something without embedding the thing itself.**

Floware may represent this as:
- state reference;
- evidence reference;
- Flow dependency;
- domain-object link;
- correspondence edge;
- provenance pointer.

Important distinction:

A low-level memory pointer has physical/runtime semantics beyond ordinary conceptual reference.

Therefore:

```text
POINTER AS RELATION
→ Floware correspondence

POINTER AS MEMORY ADDRESS / ALIASING / LIFETIME
→ software semantics may remain necessary
```

## Legal-language correspondence

Legal documents often use:
- defined terms;
- cross-references;
- incorporation by reference;
- conditions;
- exceptions;
- hierarchy;
- scope;
- precedence;
- remedies;
- termination clauses.

These correspond structurally to programming constructs such as:
- symbols;
- references;
- imports;
- gates;
- exception handling;
- authority;
- scope;
- control flow;
- stop conditions.

This does not mean law and programming are the same domain.

It means both use formal structures to coordinate meaning and consequence.

## Coding → Flowing

Proposed vocabulary:

```text
CODING
writing deterministic machine instructions

FLOWING
designing goal-directed adaptive capability in Floware
```

A person who builds a Flow may be:
- flowing;
- designing a Flow;
- composing Flows;
- refining a Flow.

These terms are provisional until usage proves which language is useful.

## Conversion strategy

For any language:

```text
1. identify language primitives
2. identify semantic purpose of each primitive
3. abstract structural relationship
4. map to Flow attribute
5. identify semantics Floware cannot safely absorb
6. preserve those as software/hard-limit boundaries
7. test examples
8. record failed mappings
9. refine glossary
```

## Success condition

A language mapping is useful when Floware can preserve enough of the original program's:
- goal;
- state;
- dependencies;
- constraints;
- branches;
- recurrence;
- error handling;
- inputs/outputs;
- authority;
- observable behavior

to reproduce the intended capability without hiding essential semantics.

## Failure condition

Do not claim successful conversion when a mapping loses essential:
- memory safety;
- timing guarantees;
- concurrency behavior;
- precision;
- security properties;
- physical constraints;
- protocol compatibility.

## Core principle

> **Programming constructs may be local expressions of more general Flow relationships.**

That proposition should be tested language by language.

> **Translate semantics into Flow before translating syntax into words.**
