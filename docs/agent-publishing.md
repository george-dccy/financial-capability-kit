# Agent Publishing Guide

This guide explains how to publish the capability formed by this repository as a personal financial work agent.

## 1. Publishing Goal

Publish Fincap as a capability base, not as a fixed persona.

The agent should behave like:

- a banking and financial work copilot
- a repository-first professional knowledge user
- a private-first experience curator
- a practical executor that can produce briefs, scripts, checklists, and follow-up plans

It should not behave like:

- a bank customer service bot
- a model that invents internal rules
- a personality clone
- a generic web-search assistant

## 2. Minimum Agent Package

When a platform supports custom agents, upload or connect:

- `INSTALL_FOR_AGENTS.md`
- `README.md`
- `registry/*.json`
- `prompts/entrypoints/agent/general.md`
- selected `skills/*` and `knowledge/*`

If file count is limited, keep the registry files and the entrypoint prompt first.

## 3. Platform Recipe

For platforms that can clone repositories, give the agent:

```text
Read https://gitee.com/georgedccy/financial-capability-kit.git and follow INSTALL_FOR_AGENTS.md. Use the repository as my banking and financial capability base. If you cannot read repository files, say so directly.
```

For platforms that only support document upload:

1. Upload `INSTALL_FOR_AGENTS.md`
2. Upload `registry/*.json`
3. Upload the target skill or knowledge folders needed for the agent
4. Add `prompts/entrypoints/agent/general.md` as the system or developer instruction

For chat-only tools, use:

```text
Read INSTALL_FOR_CHAT_MODELS.md first. If you cannot access repository content, do not answer as if you had read it.
```

## 4. Kimi, MiniMax, OpenClaw, Hermes And Similar Platforms

Model and platform features change quickly.
Use platform-specific agent features only when they can actually read files, retain instructions, or call tools.

Recommended packaging:

- MiniMax: use a mode that can clone or read repository content
- Kimi Agent or similar agent platforms: upload the install file, registry files, and selected skills as a capability pack
- OpenClaw or Hermes-style agents: clone the repo and bind the resolver files into the agent startup flow
- CLI agents: set the repository as working directory and read `INSTALL_FOR_AGENTS.md`

The repository should remain model-neutral.
Do not hard-code one vendor's workflow as the only supported path.

## 5. Multi-Agent Collaboration

For multi-agent systems, split roles by task boundary:

- Signal Interpreter: uses `skill.action.interpret-financial-signal`
- Product Mapper: expands public product knowledge with official sources
- Skill Curator: converts repeated tasks into reference or action skills
- Decision Brief Writer: turns complex items into leadership-ready briefs
- Reviewer: checks sources, boundaries, registry consistency, and risk terms

Agents should communicate through explicit artifacts:

- input material
- selected assets
- output draft
- source list
- unresolved questions
- suggested repository update

Avoid vague chat-only handoff.

## 6. Private Layer

Personal cases, preferences, failed attempts, customer notes, and work memories must not be published by default.

Use private-first storage:

- `workspace/private/skills`
- `workspace/private/memories`
- `workspace/private/case-notes`
- `workspace/private/knowledge`

Only promote to public after removing sensitive content and adding public sources.
