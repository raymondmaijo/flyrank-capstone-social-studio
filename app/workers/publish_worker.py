from app.database import SessionLocal
from app.models.publish_history import PublishHistory
from app.models.schedule_slot import ScheduleSlot
from app.models.variant import Variant
from app.services.publish_service import PublishService
from app.workers.celery_app import celery_app


@celery_app.task(bind=True, max_retries=3)
def publish_due_slot(self, slot_id: str):
    db = SessionLocal()
    slot = db.query(ScheduleSlot).filter(ScheduleSlot.id == slot_id).first()
    if not slot:
        return {"status": "skipped", "reason": "slot_missing"}

    variant = db.query(Variant).filter(Variant.id == slot.variant_id).first()
    if not variant:
        return {"status": "skipped", "reason": "variant_missing"}

    result = PublishService().publish_variant(variant, {"chat_id": "demo-chat"})

    history = PublishHistory(
        id=slot.idempotency_key,
        variant_id=variant.id,
        slot_id=slot.id,
        platform=variant.platform.value,
        attempt_number="1",
        result="success",
        external_post_url=result.get("post_url"),
        response_payload=str(result),
    )

    db.add(history)
    slot.state = "published"
    db.commit()
    db.close()
    return {"status": "success", "url": result.get("post_url")}
