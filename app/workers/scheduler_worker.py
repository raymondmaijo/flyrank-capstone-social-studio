from datetime import datetime, timezone

from app.database import SessionLocal
from app.models.schedule_slot import ScheduleSlot
from app.workers.publish_worker import publish_due_slot


def process_due_slots():
    db = SessionLocal()
    due = db.query(ScheduleSlot).filter(
        ScheduleSlot.state == "queued",
        ScheduleSlot.scheduled_for <= datetime.now(timezone.utc),
    ).all()

    for slot in due:
        publish_due_slot.delay(slot.id)
        slot.state = "dispatching"

    db.commit()
    db.close()
    return {"count": len(due)}
