from fastapi import FastAPI

app = FastAPI(title="Social Media Studio API")


@app.get("/health")
def health():
    return {"status": "ok"}
