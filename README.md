# Household Budget

A personal finance and shared household budget platform. Track income and expenses, plan monthly budgets, and manage shared finances with a partner, family, or roommates, including split expenses and settlements.

> Status: in active development (Milestone 1 - project foundation)

## Features (planned for MVP)

- Secure authentication (email verification, password reset)
- Private and shared accounts with strict access control
- Income, expense, and transfer transactions
- Categories and monthly budgets with alerts
- Households with roles (Owner, Admin, Member, Viewer)
- Split expenses and settlements ("who owes whom")
- Dashboard with charts

## Tech stack

- **Backend:** Python, FastAPI, SQLAlchemy, Alembic, PostgreSQL, Pydantic
- **Frontend:** React, TypeScript
- **Infrastructure:** Docker, Docker Compose, Redis
- **Testing:** pytest

## Architecture

The backend follows a layered architecture:

API (routes) → Services (business logic) → Repositories (data access) → PostgreSQL

Each layer has a single responsibility, which keeps the code testable and easy to change.

## Getting started

### Prerequisites

- Docker Desktop
- Git

### Run locally

1. Clone the repository.
2. Copy the environment template and fill in real values:

   ```
   cp .env.example .env
   ```

   On Windows (Command Prompt): `copy .env.example .env`

3. Start all services:

   ```
   docker compose up --build
   ```

4. Open in the browser:
   - Health check: http://localhost:8000/health
   - API documentation: http://localhost:8000/docs

## Roadmap

- [ ] Milestone 1 - Project foundation (Docker, PostgreSQL, FastAPI, React)
- [ ] Milestone 2 - Authentication
- [ ] Milestone 3 - Accounts and transactions
- [ ] Milestone 4 - Categories and budgets
- [ ] Milestone 5 - Households, invitations, and roles
- [ ] Milestone 6 - Split expenses and settlements
- [ ] Milestone 7 - Dashboard
- [ ] Milestone 8 - Tests, CI, and deployment

## License

Proprietary. All rights reserved. See [LICENSE](LICENSE).
