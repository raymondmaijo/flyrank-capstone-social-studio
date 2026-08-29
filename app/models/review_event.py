from sqlalchemy import Column, DateTime, ForeignKey, String, Text
from sqlalchemy.sql import func

from app.database import Base


class ReviewEvent(Base):
    __tablename__ = "review_events"

    id = Column(String, primary_key=True, index=True)
    variant_id = Column(String, ForeignKey("variants.id"), nullable=False)
    actor = Column(String, default="system", nullable=False)
    action = Column(String, nullable=False)
    reason = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
