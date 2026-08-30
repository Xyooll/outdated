# Xyool Means Architecture

Xyool is the objective controller. Models, APIs, SDKs, plugins, local software, external agents, research systems, and software factories are **means** it can select, combine, evaluate, replace, or create.

## Core rule

Do not assume a task has one correct means. Select means based on the objective and current state. Measure effectiveness. Keep effective means. Repair or replace ineffective means. Create new means when the existing pool cannot accomplish the objective.

## First-class means

- `inspect_environment` — discover available resources.
- `inspect_project` — inspect repository architecture and implementation.
- `web_search` — external research.
- `create_capability` — local staged software generation.
- `codex_engine` — Codex-class repository engineering through the OpenAI Responses API using `gpt-5.3-codex` by default.

## Codex escalation

When a software-building mean reports promotion failure, missing output, write failure, or another concrete implementation blocker, Xyool should diagnose the failure and prefer `codex_engine` when available instead of blindly repeating the failed builder.

Codex can inspect files, create/update files, list repository contents, run non-destructive tests/build commands, and iterate. It must report evidence rather than claiming completion.

## Future means

The same registry can expose other agent SDKs, MCP servers, plugins, APIs, sandboxes, specialized research agents, trading systems, data providers, deployment systems, and human handoffs. These should remain replaceable adapters rather than becoming the identity of Xyool.

## Safety

Live external actions remain subject to Xyool's authority, authorization, and risk gates. The Codex mean is scoped to the local repository and denies common destructive/remote-git commands.
