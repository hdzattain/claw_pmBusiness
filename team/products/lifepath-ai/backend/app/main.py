from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.api.auth import router as auth_router
from app.api.advice import router as advice_router
from app.core.db import init_db

app = FastAPI(title="LifePath AI API", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    init_db()


@app.middleware("http")
async def privacy_proof_header(request: Request, call_next):
    response = await call_next(request)
    # Placeholder proof token
    response.headers["x-privacy-proof"] = "zkp-placeholder-v0"
    return response


@app.get("/health")
def health():
    return {"ok": True, "service": "lifepath-backend"}


app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(advice_router, prefix="/api/advice", tags=["advice"])
