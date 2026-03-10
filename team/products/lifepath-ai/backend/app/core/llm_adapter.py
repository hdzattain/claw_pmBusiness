from __future__ import annotations

import json
from typing import Optional

import httpx

from app.core.config import settings


def _safe_text(value: str, limit: int = 800) -> str:
    return (value or "").strip().replace("\n", " ")[:limit]


def generate_text(prompt: str, system_prompt: Optional[str] = None) -> Optional[str]:
    provider = (settings.model_provider or "heuristic").strip().lower()

    if provider == "ollama":
        return _generate_via_ollama(prompt=prompt, system_prompt=system_prompt)

    if provider == "openai_compat":
        return _generate_via_openai_compat(prompt=prompt, system_prompt=system_prompt)

    return None


def _generate_via_ollama(prompt: str, system_prompt: Optional[str]) -> Optional[str]:
    payload = {
        "model": settings.ollama_model,
        "stream": False,
        "prompt": f"{system_prompt or ''}\n\n{prompt}".strip(),
    }
    try:
        with httpx.Client(timeout=20.0) as client:
            r = client.post(f"{settings.ollama_base_url.rstrip('/')}/api/generate", json=payload)
            r.raise_for_status()
            data = r.json()
            text = _safe_text(data.get("response", ""), 1200)
            return text or None
    except Exception:
        return None


def _generate_via_openai_compat(prompt: str, system_prompt: Optional[str]) -> Optional[str]:
    if not settings.openai_api_key:
        return None

    payload = {
        "model": settings.openai_model,
        "messages": [
            {"role": "system", "content": system_prompt or "你是一个简洁、可执行的行动建议助手。"},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
        "max_tokens": 350,
    }
    headers = {
        "Authorization": f"Bearer {settings.openai_api_key}",
        "Content-Type": "application/json",
    }

    try:
        with httpx.Client(timeout=20.0) as client:
            r = client.post(f"{settings.openai_base_url.rstrip('/')}/chat/completions", headers=headers, json=payload)
            r.raise_for_status()
            data = r.json()
            choices = data.get("choices") or []
            if not choices:
                return None
            content = (((choices[0] or {}).get("message") or {}).get("content") or "").strip()
            return _safe_text(content, 1200) or None
    except Exception:
        return None
