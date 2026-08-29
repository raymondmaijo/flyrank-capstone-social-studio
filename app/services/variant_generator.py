from uuid import uuid4

from app.core.enums import Platform, VariantStatus
from app.database import SessionLocal
from app.models.post import Post
from app.models.variant import Variant


class VariantGenerator:
    def generate_for_post(self, post_id: str, platform: str, tone: str = "professional"):
        db = SessionLocal()
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            raise ValueError("Post not found")

        content = f"{post.raw_content[:180]}\n\n#socialgrowth #contentmarketing"
        variant = Variant(
            id=str(uuid4()),
            post_id=post.id,
            platform=Platform(platform),
            content=content,
            tone=tone,
            hashtags_count=2,
            status=VariantStatus.DRAFT,
        )

        db.add(variant)
        db.commit()
        db.refresh(variant)
        db.close()
        return variant
