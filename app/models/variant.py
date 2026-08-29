from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base
from app.core.enums import Platform, VariantStatus


class Variant(Base):
    __tablename__ = "variants"

    id = Column(String, primary_key=True, index=True)
    post_id = Column(String, ForeignKey("posts.id"), nullable=False)
    platform = Column(Enum(Platform), nullable=False)
    content = Column(Text, nullable=False)
    status = Column(Enum(VariantStatus), default=VariantStatus.DRAFT, nullable=False)
    tone = Column(String, nullable=False)
    hashtags_count = Column(Integer, default=0)
    validation_errors = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    post = relationship("Post", back_populates="variants")
