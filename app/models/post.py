from sqlalchemy import Column, DateTime, Enum, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base
from app.core.enums import PostSourceType


class Post(Base):
    __tablename__ = "posts"

    id = Column(String, primary_key=True, index=True)
    source_type = Column(Enum(PostSourceType), nullable=False)
    source_url = Column(String, nullable=True)
    markdown = Column(Text, nullable=True)
    raw_content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    variants = relationship("Variant", back_populates="post")
