# LifePath AI (????) - MVP Scaffold

## Stack
- Frontend: React + TypeScript (mobile-first)
- Backend: FastAPI
- Auth: JWT (placeholder)
- Privacy: Interceptor skeleton (PII detect/mask/audit)
- Memory: Mem0 adapter interface (placeholder)

## Structure
- `backend/` FastAPI API service
- `frontend/` React UI shell
- `docs/` development workflow and memory references

## Quick Start (Backend)
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Quick Start (Frontend)
```bash
cd frontend
npm install
npm run dev
```

## API Conventions
- All responses include `x-privacy-proof` header (placeholder)
- Sensitive input goes through privacy interceptor
- Logs must not store raw sensitive user content

## Phase 1 Implemented
- SQLite local persistence (`users`, `journal_entries`, `audit_logs`)
- JWT auth (`/api/auth/register`, `/api/auth/login`)
- Protected advice APIs (`/api/advice/daily`, `/api/advice/journal`)
- Basic onboarding UI (register/login + daily advice + masked journal timeline)
