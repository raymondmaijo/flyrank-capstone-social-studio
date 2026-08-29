from fastapi import FastAPI

from app.api.routes.posts import router as posts_router
from app.api.routes.review import router as review_router
from app.api.routes.schedules import router as schedules_router
from app.api.routes.variants import router as variants_router

app = FastAPI(title="Social Media Studio API")

app.include_router(posts_router)
app.include_router(variants_router)
app.include_router(review_router)
app.include_router(schedules_router)


@app.get("/health")
def health():
    return {"status": "ok"}
