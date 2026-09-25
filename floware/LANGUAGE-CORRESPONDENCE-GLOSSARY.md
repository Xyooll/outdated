# Floware Language Correspondence Glossary

Status: **LIVING GLOSSARY**

Purpose:

> Build a shared semantic vocabulary that lets Xyool understand how programming-language concepts correspond to Flow attributes without confusing syntax with structure.

This glossary is expected to grow by language.

## Universal semantic families

### State
Examples:
- variable
- field
- property
- register
- binding

Floware:
- state
- state field
- persistent state
- temporary state

### Transformation
Examples:
- function
- method
- procedure
- lambda

Floware:
- Flow
- Subflow
- transformation step

### Routing
Examples:
- if
- else
- switch
- match
- pattern match

Floware:
- gate
- conditional route
- router

### Repetition
Examples:
- for
- while
- recursion
- event loop

Floware:
- recurrence
- recursive Flow
- re-evaluation cycle

### Reference / indirection
Examples:
- pointer
- reference
- handle
- identifier
- foreign key
- link

Floware:
- reference edge
- dependency edge
- provenance link
- correspondence link

### Encapsulation / adaptation
Examples:
- wrapper
- decorator
- adapter
- facade
- proxy

Floware:
- wrapper Flow
- adapter Flow
- boundary Flow
- translation Flow

### Contract
Examples:
- type
- interface
- protocol
- schema
- trait

Floware:
- Flow contract
- state contract
- evidence contract
- boundary contract

### Failure / recovery
Examples:
- exception
- error
- retry
- catch
- finally

Floware:
- fail-closed state
- recovery route
- retry condition
- cleanup/closure state

### Concurrency
Examples:
- thread
- process
- async task
- actor
- coroutine

Floware:
- concurrent Flow
- isolated Flow context
- asynchronous Flow
- message-linked Flow

### Persistence
Examples:
- file
- database
- object store
- cache

Floware:
- durable state
- evidence store
- bounded cache

### External boundary
Examples:
- API
- socket
- FFI
- driver

Floware:
- external Flow boundary
- software interface boundary
- hardware boundary

## Language-specific expansion template

For each language:

```text
LANGUAGE:
PARADIGMS:
CORE PRIMITIVES:
STATE MODEL:
CONTROL MODEL:
REFERENCE MODEL:
ERROR MODEL:
CONCURRENCY MODEL:
RESOURCE-LIFETIME MODEL:
TYPE MODEL:
EXTERNAL-INTERFACE MODEL:

FLOW CORRESPONDENCES:
SOFTWARE-ONLY SEMANTICS:
FAILED / AMBIGUOUS MAPPINGS:
EXAMPLES:
```

## Planned language families

Start with structurally different languages rather than many similar ones:

1. Python — dynamic / object-oriented / functional elements
2. C — procedural / pointers / manual memory
3. Rust — ownership / borrowing / explicit safety
4. JavaScript — event loop / async / dynamic objects
5. SQL — declarative data transformation
6. Bash — shell/process composition
7. Lisp — symbolic/recursive/functional
8. Haskell — pure functional / types / effects
9. Prolog — logic/declarative inference
10. Solidity — contract/state-machine + transactional execution

This order is a research plan, not a ranking.

## Correspondence discipline

A programming term is not universal merely because multiple languages use similar words.

Map:
- semantic role;
- causal function;
- state relationship;
- execution consequence.

Then test whether the same Flow correspondence survives across languages.
