from app.adapters.factory import build_publisher


class PublishService:
    def publish_variant(self, variant, metadata: dict) -> dict:
        publisher = build_publisher(variant.platform.value)
        return publisher.publish(
            variant_id=variant.id,
            content=variant.content,
            metadata=metadata,
        )
