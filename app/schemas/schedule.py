from datetime import datetime

from pydantic import BaseModel


class ScheduleCreate(BaseModel):
    variant_id: str
    scheduled_for: datetime


class ScheduleRead(BaseModel):
    id: str
    variant_id: str
    scheduled_for: datetime
    state: str
