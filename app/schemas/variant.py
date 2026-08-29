from typing import Optional

from pydantic import BaseModel


class VariantCreate(BaseModel):
    post_id: str
    platform: str
    tone: str = "professional"


class VariantRead(BaseModel):
    id: str
    post_id: str
    platform: str
    content: str
    status: str
    validation_errors: Optional[str] = None
