from typing import Optional

from pydantic import BaseModel


class PublishHistoryRead(BaseModel):
    id: str
    variant_id: str
    slot_id: str
    platform: str
    result: str
    external_post_url: Optional[str] = None
