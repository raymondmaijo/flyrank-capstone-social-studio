from sqlalchemy import Column, DateTime, ForeignKey, String, Text, UniqueConstraint
from sqlalchemy.sql import func

from app.database import Base


class PublishHistory(Base):
    __tablename__ = "publish_history"

    id = Column(String, primary_key=True, index=True)
    variant_id = Column(String, ForeignKey("variants.id"), nullable=False)
    slot_id = Column(String, ForeignKey("schedule_slots.id"), nullable=False)
    platform = Column(String, nullable=False)
    attempt_number = Column(String, default="1")
    result = Column(String, nullable=False)
    external_post_url = Column(String, nullable=True)
    response_payload = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        UniqueConstraint("slot_id", "attempt_number", name="uq_slot_attempt"),
    )
