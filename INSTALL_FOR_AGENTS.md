# Install Fincap For Agents

Read this file first, then use this repository as the user's banking and financial capability base.

## One-Line Install

Ask the agent to run:

```text
请读取并遵循 Financial Capability Kit 安装说明：https://gitee.com/georgedccy/financial-capability-kit/raw/main/INSTALL_FOR_AGENTS.md
```

If Gitee raw access is unavailable, use the GitHub mirror:

```text
请读取并遵循 Financial Capability Kit 安装说明：https://raw.githubusercontent.com/george-dccy/financial-capability-kit/main/INSTALL_FOR_AGENTS.md
```

This is inspired by agent-first install documents such as [gbrain](https://github.com/garrytan/gbrain/blob/master/INSTALL_FOR_AGENTS.md), but Fincap is not a personal memory database. It is a repo-first banking and financial capability kit.

## Step 1: Clone Or Read

Preferred canonical repository:

```powershell
git clone https://gitee.com/georgedccy/financial-capability-kit.git fincap
cd fincap
```

Mirror:

```powershell
git clone https://github.com/george-dccy/financial-capability-kit.git fincap
cd fincap
```

If the platform cannot clone repositories, it must at least read:

- `README.md`
- `registry/skills.json`
- `registry/knowledge.json`
- `registry/prompts.json`
- `prompts/entrypoints/agent/general.md`

## Step 2: Load The Resolver

Treat the three registry files as the resolver:

- `registry/skills.json` decides which reference skill or action skill to read
- `registry/knowledge.json` decides which public knowledge package to read
- `registry/prompts.json` decides which entrypoint or lightweight prompt can be reused

Do not answer from generic financial common sense if the repository has a relevant skill or knowledge file.

## Step 3: Load The Default Agent Prompt

Read:

```text
prompts/entrypoints/agent/general.md
```

Then follow it for the whole conversation, not just the first turn.

## Step 4: Self-Check Repository Access

Before answering the user's first real question, verify:

- You can read all three `registry/*.json` files
- You can list at least one relevant `skills/*/SKILL.md` or `knowledge/*/README.md`
- You can state which file will be used without exposing a long technical trace in the final answer

If this fails, say:

```text
当前无法访问仓库，不能保证按 Financial Capability Kit 回答。
```

## Step 5: Working Rules

- For professional perspective, use `skills/reference/*`
- For task execution, use `skills/action/*`
- For public product facts, FAQ, and sources, use `knowledge/*`
- For new policies, news, products, competitors, client changes, or other new information, use `skills/action/interpret-financial-signal`
- For user experience, preference, case notes, and private methods, use a private workspace if the platform supports it

## Step 6: Boundaries

Do not invent:

- internal bank rules
- approval conclusions
- credit limits
- pricing
- processing time promises
- real customer information

If the repository does not cover the user's question, write:

```text
当前仓库未覆盖
```

Then explain what source or decision is missing.

## Step 7: Update

If this repository is cloned locally:

```powershell
git pull origin main
```

Public updates must not overwrite a user's private workspace.
