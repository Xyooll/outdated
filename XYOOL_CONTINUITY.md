# Xyool Continuity / Build State

## Purpose
Xyool is being built as an adaptive AI-controlled software system. The human is the final authority. The AI is the active controller/reasoning layer; software capabilities are the passive/executable layer. The system should observe, prioritize attention, reason, create capabilities, test them, simulate them, evaluate results, learn, and evolve without silently promoting risky changes.

## Current architecture

```text
Human Authority
      ↓
Cognitive Runtime
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

The storage layer should eventually be exposed through capabilities such as `store_event`, `store_document`, `store_large_file`, `store_code`, `store_experiment`, and `retrieve_memory`, allowing the controller to choose a backend instead of hard-coding one service everywhere.

## Next build priority
Do NOT keep adding disconnected architecture. The next goal is to assemble and verify the real runtime:

1. Storage abstraction over Supabase/GitHub/Dropbox/Notion.
2. Capability registry populated with real, available capabilities and permission metadata.
3. Cognitive Runtime wired end-to-end.
4. Attention/event triggers so expensive AI is invoked only when defined conditions occur.
5. Persistent memory retrieval and event history.
6. AI provider abstraction with local/remote model routing.
7. Complete integration cycle: event → attention → memory → AI → plan → capability check → sandbox/action → evaluation → learning → log.
8. Run the full repository test suite through GitHub Actions and fix failures.
9. Run large synthetic benchmarks before connecting real-world execution.
10. Add shadow-mode adapters for real services; observe without taking external actions.
11. Add human-approved execution.
12. Only then consider narrowly scoped autonomous execution.

## Attention model
The AI should not continuously reason over everything. Software should watch for explicit trigger conditions and wake the AI when attention is justified.

Example:
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

## Safety / authority boundary
The architecture must not turn external accounts, financial actions, destructive operations, or other consequential actions into unrestricted autonomous behavior. Keep permissions explicit and auditable. Human authority remains the final control layer.

## Current status
Architecture: substantially assembled.
Integration: not yet proven end-to-end in the user's local environment.
Full test suite: configured for GitHub Actions, but a complete successful run must be verified rather than assumed.
Real-world execution: NOT ready; remain in synthetic/shadow mode until integration and regression testing pass.

## Continuation instruction
When starting a new conversation, read this file first and continue from **Next build priority**. Do not redesign the architecture from scratch unless new evidence shows a structural problem. Prefer implementing, testing, measuring and fixing over adding speculative components.
