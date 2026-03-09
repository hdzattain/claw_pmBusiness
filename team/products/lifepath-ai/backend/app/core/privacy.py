import hashlib
import re
from dataclasses import dataclass


@dataclass
class PrivacyResult:
    status: str
    masked_data: str
    proof: str


class PrivacyInterceptor:
    """PII detect/mask skeleton + pseudo proof token"""

    EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
    PHONE_PATTERN = re.compile(r"\b1\d{10}\b")

    def detect_pii(self, text: str) -> bool:
        return bool(self.EMAIL_PATTERN.search(text) or self.PHONE_PATTERN.search(text))

    def mask_sensitive(self, text: str) -> str:
        text = self.EMAIL_PATTERN.sub("[masked-email]", text)
        text = self.PHONE_PATTERN.sub("[masked-phone]", text)
        return text

    def hash_text(self, value: str) -> str:
        return hashlib.sha256(value.encode("utf-8")).hexdigest()

    def generate_zkp_proof(self, masked: str) -> str:
        # Placeholder proof: hash-based token
        digest = self.hash_text(masked)[:24]
        return f"proof_{digest}"

    def intercept_sensitive(self, user_input: str) -> dict:
        if self.detect_pii(user_input):
            cleaned = self.mask_sensitive(user_input)
            proof = self.generate_zkp_proof(cleaned)
            return {
                "status": "approved",
                "proof": proof,
                "masked_data": cleaned,
                "pii_detected": True,
            }

        return {
            "status": "approved",
            "proof": self.generate_zkp_proof(user_input),
            "masked_data": user_input,
            "pii_detected": False,
        }
