import hashlib


def build_idempotency_key(variant_id: str, scheduled_for: str, platform: str) -> str:
    raw = f"{variant_id}:{scheduled_for}:{platform}"
    return hashlib.sha256(raw.encode()).hexdigest()
