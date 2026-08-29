from typing import Optional

from pydantic import BaseModel


class PostCreate(BaseModel):
    source_type: str
    source_url: Optional[str] = None
    markdown: Optional[str] = None


class PostRead(BaseModel):
    id: str
    source_type: str
    source_url: Optional[str] = None
    markdown: Optional[str] = None
