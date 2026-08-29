from sqlalchemy import Column, DateTime, ForeignKey, String, UniqueConstraint
from sqlalchemy.sql import func

from app.database import Base


class ScheduleSlot(Base):
    __tablename__ = "schedule_slots"

    id = Column(String, primary_key=True, index=True)
    variant_id = Column(String, ForeignKey("variants.id"), nullable=False)
    scheduled_for = Column(DateTime(timezone=True), nullable=False)
    state = Column(String, default="queued", nullable=False)
    idempotency_key = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        UniqueConstraint("variant_id", "scheduled_for", name="uq_variant_slot"),
    )
