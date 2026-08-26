# Xyool Continuity / Build State

## Purpose
Xyool is an adaptive AI-controlled software system. The human is the final authority. The AI is the active controller/reasoning layer; software capabilities are the passive/executable layer. The system observes, prioritizes attention, reasons, creates capabilities, tests them, simulates them, evaluates results, learns, and evolves without silently promoting risky changes.

## Current architecture

```text
Human Authority
      ↓
Cognitive Runtime / Loop
      ↓
Attention → Memory → AI Reasoning → Objective → Hypothesis
      ↓                                      ↓
Capability Registry ← Candidate Software ← Capability Builder
      ↓                                      ↓
Action / Simulation ← Sandbox ← Evaluation
      ↓
Event Log → Learning → Persistent Memory → Evolution
      ↓
Promotion Gate → Explicit Authorization → Real-world execution
```

## Core principles
- Human remains authority.
- AI is active controller; software is executable/passive capability layer.
- Plans may not reference capabilities that do not exist in the registry.
- Missing capabilities can be proposed/built as candidates, but never silently become production capabilities.
- Sandbox first; real-world execution later.
- Promotion requires measurable improvement and safety gates.
- Real-world side effects require explicit authorization according to policy.
- Attention is event-driven to control AI/API cost: do not wake expensive reasoning for every event.
- Prefer probability/ranking and measured evidence over excessive uncertainty language.
- Build for value first; infrastructure spending should follow demonstrated value.

## Current repo
Repository: `Xyooll/xyool`
Primary development path: `operation-dna/`

## Implemented components
- Event/attention architecture
- Executive/controller loop
- Event logging
- Sandbox simulation
- Evaluation layer
- Learning records
- Benchmark runner
- Synthetic trading market
- Synthetic business opportunity market
- Strategy search
- Hypothesis engine
- AI-to-software candidate/capability builder
- Capability registry
- Production-readiness controls
- Persistent runtime state
- Resource budgets
- Kill switch
- Version store and rollback
- End-to-end readiness tests
- GitHub Actions test workflow
- Backend-neutral storage router
- End-to-end cognitive loop (`software/runtime/loop.py`)
- Local/remote AI model router
- Runnable dependency-light smoke test (`run_smoke_test.py`)

## Synthetic environments
### Trading
- Long/flat only at present.
- Reproducible seeded market.
- Return and max drawdown measured.
- Baseline momentum strategy.
- Candidate strategies can be benchmarked.

### Business
- Synthetic opportunities have value, difficulty, fit, competition.
- Revenue, cost, profit and accepted opportunities measured.
- Baseline fit strategy.

## Current production-readiness controls
- Persistent state stored by runtime component.
- Resource budgets for cost/actions/experiments.
- Kill switch.
- Version promotion and rollback.
- Candidate must pass tests and sandbox before becoming eligible for promotion.
- Promotion still requires an explicit authorization callback.

## Available ChatGPT integrations
- 12andus Astrology
- Airtable
- Alpaca
- Binance
- Blockscout Blockchain Data
- CoinGecko
- Dropbox
- Dropbox Dash
- Financial Datasets
- GitHub
- LONA Trading Assistant
- Make
- Notion
- Plugin Management
- Questforge
- Steer Astro
- Supabase
- Todoist: To Do List & Calendar
- TradingCursor

## Intended integration roles
### GitHub
Source code, tests, versions, CI/CD, AI-generated code changes.

### Supabase
Primary structured operational state: events, objectives, capabilities, experiments, metrics, permissions, strategy versions, relationships.

### Dropbox / Dropbox Dash
Files, datasets, reports, artifacts, backups and connected knowledge retrieval where appropriate.

### Notion
Human-readable research, documentation, decisions, strategy explanations and knowledge capture.

### Airtable
Optional operational/business tables and workflows where its interface is useful.

### Todoist
Human-facing tasks, scheduled work and approvals/reminders where appropriate.

### Trading / market data
Alpaca, Binance, Financial Datasets, CoinGecko, Blockscout, LONA Trading Assistant and TradingCursor can provide domain capabilities. Real-money actions remain gated.

### Automation
Make can serve as an external workflow/automation capability.

## Local hardware target
Development/sandbox node is currently the user's Dell Precision 7520:
- Windows 10 Pro
- Intel i7-7820HQ, 4 cores / 8 logical processors
- 32 GB RAM
- NVIDIA Quadro M1200, 4 GB VRAM
- Samsung PM961 512 GB NVMe

The machine is adequate for Xyool runtime, simulations, databases, development and small/local models. Do not require a VPS yet. Cloud AI can handle heavier reasoning. The local GPU should be treated as optional/limited acceleration rather than the primary AI engine.

## Storage strategy
Use the local NVMe primarily for compute/runtime/cache/sandbox. Prefer connected services for durable storage:
- Supabase: structured operational data
- GitHub: source/version history
- Dropbox: large files/artifacts/backups
- Notion: human-readable knowledge

`software/runtime/storage.py` provides a backend-neutral router so logical storage classes can be mapped to different backends without hard-coding vendors into the cognitive layer.

## Attention model
The AI should not continuously reason over everything. Software watches for explicit trigger conditions and wakes the AI when attention is justified.

Examples:
- Trading software detects a defined market condition → wake AI.
- Social system detects meaningful analytics change → wake AI.
- Marketplace adapter detects a high-fit job/request → wake AI.
- Otherwise: collect/log cheaply and remain passive.

Rank attention using expected value relative to reasoning/API cost where measurable.

## Missing capability rule
A plan is invalid if it calls an unregistered capability. Instead:
1. Detect missing capability.
2. Create a capability-build hypothesis.
3. Generate candidate software in isolation.
4. Test it.
5. Sandbox it.
6. Evaluate it.
7. Log the result.
8. Make it eligible for promotion only if gates pass.
9. Require authorization for protected side effects.

## Current runtime
`software/runtime/loop.py` now wires the main event-driven cycle together. It checks the kill switch, evaluates attention, checks the AI cost budget, retrieves relevant memory, invokes the injected reasoner, rejects unknown capabilities, pauses for authorization on protected capabilities, executes permitted capabilities, records results, and writes episodic memory.

`software/runtime/model_router.py` selects a local provider for low-complexity work and can route higher-complexity work to an injected remote provider subject to a cost policy.

`run_smoke_test.py` provides a dependency-light synthetic end-to-end test that should be run from the `operation-dna` directory with Python.

## Build status
Architecture: substantially assembled.
Core orchestration: wired.
Storage abstraction: wired at the contract/router level; vendor-specific production adapters still need credentials/configuration.
Capability registry: implemented; real external capabilities still need adapter registration.
AI routing: implemented at the provider abstraction level; real providers still need runtime configuration.
Integration: ready for local execution testing.
Full test suite: configured for GitHub Actions, but a successful complete run must be verified rather than assumed.
Real-world execution: NOT ready; remain in synthetic/shadow mode until integration and regression testing pass.

## Next execution sequence
1. Clone/pull repository on the user's Precision 7520.
2. Run `python run_smoke_test.py` from `operation-dna`.
3. Run the complete test suite used by CI.
4. Fix integration failures found by actual execution.
5. Connect durable storage adapters, starting with Supabase.
6. Register real read-only capabilities from available integrations.
7. Configure local/remote AI providers.
8. Run large synthetic benchmarks.
9. Add shadow-mode real-service adapters.
10. Add human-approved execution.
11. Only then consider narrowly scoped autonomous execution.

## Continuation instruction
When starting a new conversation, read this file first and continue from **Next execution sequence**. Do not redesign the architecture from scratch unless new evidence shows a structural problem. Prefer implementing, testing, measuring and fixing over adding speculative components.
