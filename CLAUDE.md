# CLAUDE.md

Context for AI assistants working on this repository. Keep it short; update it whenever a new architectural decision is made.

## Project

Household Budget: personal finance + shared household budget web app. Goals: a strong CV portfolio project, later a sellable product. Full long-term vision: [docs/PROJECT_SPEC.md](docs/PROJECT_SPEC.md) (we build a reduced MVP, see below).

## Working with the owner

- First project of this kind; learning while building. Reply in **Bulgarian**.
- Windows, **Command Prompt** (give CMD commands, e.g. `copy`, not `cp`).
- One step at a time. Say what you will change before changing it. Verify it works before moving on.
- Briefly explain each architectural decision: what and why it is production-ready.
- After each step: a short summary the owner can retell in a job interview.
- One commit per step. Never commit `.env`.

## MVP scope

1. Foundation (Docker, PostgreSQL, FastAPI, React) - in progress
2. Authentication
3. Accounts and transactions
4. Categories and budgets
5. Households, invitations, roles
6. Split expenses and settlements
7. Dashboard
8. Tests, CI, deploy

## Architecture decisions

- Monorepo: `backend/` and `frontend/`.
- Backend layers: `api` (endpoints) → `services` (business logic) → `repositories` (DB queries) → `models` (tables). Plus `schemas/` (Pydantic) and `core/` (settings, security).
- Synchronous SQLAlchemy 2.0 with psycopg 3 (simpler to learn, enough for this scale).
- Money is never float: `Decimal` in Python, `NUMERIC(12,2)` in PostgreSQL.
- UUID primary keys everywhere.
- Every account belongs to either a user (personal) or a household (shared), never both. Personal data is invisible to other members, enforced on the backend.
- Tests live in `backend/tests` and `frontend/`, not a shared `/tests`.
- Code, comments, and docs in English.
- Proprietary license ("All rights reserved").
- `.gitattributes` enforces LF (Linux containers); CRLF only for `*.bat`/`*.ps1`.
- `/docs` and `/openapi.json` are disabled in production. Errors never expose stack traces to users; full details go to logs.

## Data model

Full ERD and reasoning: [docs/DATABASE.md](docs/DATABASE.md). Key rules:

- Ownership via two nullable FKs (`owner_user_id`, `household_id`) + `CHECK num_nonnulls(...) = 1` on accounts, categories, budgets.
- Visibility rule lives in the repository layer: account visible if owned or in my household; transaction visible if its account is visible or its `household_id` is my household. Someone else's resource → 404, not 403.
- Sharing a personal expense with a household is per transaction (`transactions.household_id`); account details are never exposed.
- `amount > 0` always; direction from `type` (income, expense, transfer_in, transfer_out). A transfer is two rows linked by `transfer_group_id`.
- Balance is calculated (`opening_balance` + transactions), not stored. Payer of a shared expense = owner of the personal account.
- `settlements` is its own table. `occurred_on` is `DATE`; event times are `TIMESTAMPTZ`.
- Enums are `VARCHAR` + `CHECK`, not native PG enums. Invitation tokens stored as hashes. Audit logs: no FK on `entity_id`, `details` JSONB.
- Default categories are copied per user/household. MVP: no currency conversion.

## Local environment notes

- `docker compose up --build` starts postgres + backend. Health: http://localhost:8000/health
- Docker Desktop on this machine has crashed on stale, undeletable `.sock` files (`%LOCALAPPDATA%\Docker\run`, `%LOCALAPPDATA%\docker-secrets-engine`). Fix: quit Docker, `wsl --shutdown`, rename the folder, restart. Do not run Docker Desktop as admin.
