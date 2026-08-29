from pydantic import BaseModel


class ReviewDecision(BaseModel):
    variant_id: str
    decision: str
    reason: str | None = None
