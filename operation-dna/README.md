# Xyool

Xyool is a general-purpose autonomous AI application built around the OpenAI Agents SDK.

## Target architecture

```text
                    ┌──────────────────┐
                    │      USER        │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   YOUR APP/API   │
                    └────────┬─────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │     OPENAI AGENT        │
                │                         │
                │  Instructions           │
                │  Reasoning              │
                │  Context / memory       │
                │  Tool selection         │
                └───────────┬─────────────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
         ┌─────────┐   ┌──────────┐  ┌──────────┐
         │ Database│   │ Your APIs│  │ Web/File │
         │         │   │          │  │  tools   │
         └─────────┘   └──────────┘  └──────────┘
```

The model is the intelligence and orchestrator. Xyool is the application layer that supplies instructions, persistent context, skills, tools, data, and optional MCP connections.

## Three primitives

### Instructions

`agent_behavior.md` contains Xyool's stable behavioral DNA: understand objectives, reason, inspect, act, observe, evaluate, learn, adapt, preserve evidence, and continue until the objective is verified complete.

### Skills

`skills/` contains reusable instructions. Skills are not separate agents or hard-coded workflows. The agent decides when a skill is useful and loads it through the generic skill tool.

### Tools

Tools are the means by which the agent interacts with reality. Xyool currently exposes project inspection, persistent memory, testing, web search, optional OpenAI file search, and optional MCP servers. More tools can be added without creating a new intelligence or router.

## OpenAI Agents SDK

The runtime uses the OpenAI Agents SDK rather than a custom reasoning/orchestration loop. The SDK manages agent turns, tool calls, and sessions. Xyool uses a persistent SQLite session for conversation continuity.

The runtime also supports MCP servers through the SDK. Configure them with `XYOOL_MCP_SERVERS` as a JSON array. Supported transports are `streamable_http` and `stdio`.

Example:

```json
[
  {
    "name": "example",
    "transport": "streamable_http",
    "url": "https://example.com/mcp"
  }
]
```

Credentials should be supplied through environment variables or another secret mechanism, not committed to the repository.

## Memory

The Agents SDK session provides persistent conversation memory. Xyool's existing evidence-oriented memory library remains available as a tool for durable knowledge, experiences, provenance, indexing, and aggregation.

This separation keeps conversation continuity simple while preserving a library for information that should survive beyond a single conversation.

## Direction

The previous custom orchestrator, resource router, custom model protocol, custom web client, and software-agent loop are being retired from the primary runtime. Existing modules remain in the repository temporarily so they can be migrated, tested, and removed safely rather than becoming hidden dependencies.

The goal is a much smaller system:

```text
Xyool
 ├── Instructions
 ├── Skills
 ├── Tools
 ├── Memory / data
 └── OpenAI Agent
```

The architecture should remain domain-independent. Research, software development, finance, trading, document analysis, and other activities are things the same agent can perform using appropriate skills and tools—not separate agents.
