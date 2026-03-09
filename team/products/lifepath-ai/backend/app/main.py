from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.auth import router as auth_router
from app.api.advice import router as advice_router
from app.core.privacy import PrivacyInterceptor

app = FastAPI(title="LifePath AI API", version="0.1.0")
privacy = PrivacyInterceptor()


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
