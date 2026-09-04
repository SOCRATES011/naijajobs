## Plan: Bill-splitting Django MVP

TL;DR - Single Django project with an `expenses` app. Use server-rendered Django templates + HTMX for a fast MVP, session-based auth, DRF for future API expansion, Decimal money fields, Postgres in production. Deliverables: runnable repo, README, seed data, basic tests, Procfile/Dockerfile, short demo.

**Steps**
1. Project scaffolding: create Django project + `expenses` app, add deps, configure env and static files.  
2. Models & migrations: implement Group, Member, Expense, Share, Settlement (Decimal fields). Run migrations.  
3. Business logic: implement share-splitting and `recalculate_group_balances(group)` utilities.  
4. API & serializers: add DRF, create GroupSerializer, ExpenseSerializer (nested ShareSerializer), viewsets/routers.  
5. Auth & permissions: session auth (Django), login/register, object-level permissions for group/expense.  
6. Frontend MVP: server-rendered templates for group list/detail, expense create/edit (HTMX for inline forms), balances view, settlement form.  
7. Tests & seed: unit tests for model math, API tests for flows, management `seed` command with demo users/groups/expenses.  
8. Deploy prep & docs: Procfile, Dockerfile, requirements.txt, README with quickstart and Render/Railway instructions.

**Relevant files**
- project/settings.py — env, DB, static  
- project/urls.py — app + API routes  
- expenses/models.py — Group, Member, Expense, Share, Settlement  
- expenses/services.py — share calc & balance recalc  
- expenses/serializers.py — DRF serializers  
- expenses/views.py — DRF viewsets + template views  
- expenses/urls.py — app routes & API router  
- expenses/templates/expenses/*.html — MVP UI  
- expenses/tests/*.py — tests  
- expenses/management/commands/seed.py — demo data seeder  
- requirements.txt, Procfile, Dockerfile, README.md

**Verification**
- Local dev: migrate, run `seed`, start server, verify create-group, create-expense, view balances.  
- Tests: run pytest or `manage.py test` (model arithmetic and API flows).  
- Seed sanity: seed creates 3 users, 1 group, and sample expenses demonstrating equal/custom splits.  
- Deploy smoke: deploy to Render/Railway with Postgres and verify UI flows.

**Decisions / Assumptions**
- Server-rendered templates + HTMX chosen for speed. DRF added for future SPA.  
- Single currency per group in MVP; Decimal fields used (no FX).  
- Session auth (Django) to avoid token complexity.  
- Balance can be computed on demand or stored and updated by services.  
- Exclude payments, multi-currency, and realtime notifications from MVP.

**Further considerations**
1. If you want a React/Next SPA instead, I can switch to an API-first scaffold (adds ~1 day).  
2. Add Celery+Redis later if you need scheduled reminders or currency fetches.

Estimated completion: ~2–3 days for a single developer.
