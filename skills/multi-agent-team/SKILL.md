---
name: multi-agent-team
description: Set up and run a specialized multi-agent team in OpenClaw for solo founder or operator workflows. Use when creating role-based agents, routing tasks to different specialists, sharing team memory files, scheduling recurring team tasks, and coordinating agents via sessions_spawn/sessions_send.
---

# Multi-Agent Team

Create and operate a role-based AI team (strategy/business/marketing/dev) inside OpenClaw.

## Define team structure

1. Create one lead agent role and 1+ specialist roles.
2. For each role, define:
   - mission and scope
   - tone/personality
   - preferred model
   - recurring responsibilities
3. Keep role boundaries explicit to reduce context switching and overlap.

## Set up shared + private memory

Use a shared folder for team-level truth and private folders for role notes.

Recommended layout:

```text
team/
├── GOALS.md
├── DECISIONS.md
├── PROJECT_STATUS.md
└── agents/
    ├── lead/
    ├── business/
    ├── marketing/
    └── dev/
```

Rules:
- Update `DECISIONS.md` only for durable decisions.
- Update `PROJECT_STATUS.md` for current execution state.
- Specialists write deep notes in their private folder; summarize only key points into shared docs.

## Run role-specific execution

Use OpenClaw multi-session primitives:

- Spawn or keep persistent role sessions with `sessions_spawn`.
- Send role-targeted work with `sessions_send`.
- Use on-demand status checks (avoid tight polling loops).

Coordination pattern:
1. Lead decomposes work into parallel tracks.
2. Dispatch tracks to specialists.
3. Specialists return concise findings + recommendations.
4. Lead synthesizes final plan and next actions.

## Routing design

When you wire a chat control surface (e.g., DingTalk/Telegram/Discord), define mention/tag routing:

- `@lead` → lead session
- `@biz` → business session
- `@mkt` → marketing session
- `@dev` → dev session
- `@all` → broadcast
- no tag → lead default

## Scheduled task design

Use heartbeat/cron for proactive tasks:

- Morning: lead standup summary
- Daily metrics: business
- Daily trend scan: marketing
- CI/quality checks: dev
- End-of-day summary: lead

Keep schedules light initially; add more only after signal quality is good.

## Operating heuristics

- Start with 2 agents (lead + one specialist), then expand.
- Match model cost/performance to task complexity.
- Prefer short specialist outputs with explicit recommendations.
- Store durable knowledge in files, not only chat history.

## Reference

For the original use-case writeup, read:
- `references/source-usecase.md`
