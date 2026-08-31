## Social Media Studio backend

The backend is a FastAPI service that helps a social media studio manage the full content lifecycle: ingesting source content, creating platform-specific variants, validating them, approving or rejecting them, scheduling publishing, and tracking publish results. The app entry and route registration are in app/main.py, and the actual endpoint definitions live in:
- app/api/routes/posts.py
- app/api/routes/variants.py
- app/api/routes/review.py
- app/api/routes/schedules.py
- app/api/routes/publish_history.py

This backend supports:
- Source ingestion from URL or markdown
- Variant generation per platform
- Constraint validation
- Review flow with approval/rejection
- Scheduling for approved content
- Publish history and status tracking
- Health check for service availability

---

## Full backend API surface

### 1) Health check
- GET /health

### 2) Ingest post
- POST /api/v1/posts/ingest

### 3) Generate variant
- POST /api/v1/variants/generate

### 4) Approve variant
- POST /api/v1/review/approve/{variant_id}

### 5) Reject variant
- POST /api/v1/review/reject/{variant_id}

### 6) Create schedule
- POST /api/v1/schedules/

### 7) Get publish history
- GET /api/v1/history/{variant_id}

---

## Exact command lines to run and test

### Start with Docker
```powershell
cd C:\Flyrank\Capstone\flyrank-capstone-social-studio\social-studio
docker compose down -v
docker compose up --build -d
```

### Check health
```powershell
curl.exe -sS http://127.0.0.1:8000/health
```

### Open Swagger docs
```powershell
Start-Process http://127.0.0.1:8000/docs
```

### Ingest a post
```powershell
curl.exe -sS -X POST "http://127.0.0.1:8000/api/v1/posts/ingest" `
  -H "Content-Type: application/json" `
  -d "{\"source_type\":\"markdown\",\"markdown\":\"This is a sample social post for testing the studio pipeline.\"}"
```

### Save returned post id
```powershell
$POST = curl.exe -sS -X POST "http://127.0.0.1:8000/api/v1/posts/ingest" `
  -H "Content-Type: application/json" `
  -d "{\"source_type\":\"markdown\",\"markdown\":\"This is a sample social post for testing the studio pipeline.\"}" | ConvertFrom-Json

$POST.id
```

### Generate a variant
```powershell
curl.exe -sS -X POST "http://127.0.0.1:8000/api/v1/variants/generate?post_id=$POST.id&platform=linkedin&tone=professional"
```

### Save the variant id
```powershell
$VARIANT = curl.exe -sS -X POST "http://127.0.0.1:8000/api/v1/variants/generate?post_id=$POST.id&platform=linkedin&tone=professional" | ConvertFrom-Json

$VARIANT.id
```

### Approve variant
```powershell
curl.exe -sS -X POST "http://127.0.0.1:8000/api/v1/review/approve/$VARIANT.id"
```

### Reject variant
```powershell
curl.exe -sS -X POST "http://127.0.0.1:8000/api/v1/review/reject/$VARIANT.id?reason=Needs+more+review"
```

### Schedule approved variant
```powershell
curl.exe -sS -X POST "http://127.0.0.1:8000/api/v1/schedules/?variant_id=$VARIANT.id&scheduled_for=2026-09-02T12:00:00"
```

### Get publish history for a variant
```powershell
curl.exe -sS "http://127.0.0.1:8000/api/v1/history/$VARIANT.id"
```

---

## Full one-shot test script

```powershell
cd C:\Flyrank\Capstone\flyrank-capstone-social-studio\social-studio
docker compose up --build -d

$POST = curl.exe -sS -X POST "http://127.0.0.1:8000/api/v1/posts/ingest" `
  -H "Content-Type: application/json" `
  -d "{\"source_type\":\"markdown\",\"markdown\":\"This is a sample social post for testing the studio pipeline.\"}" | ConvertFrom-Json

$VARIANT = curl.exe -sS -X POST "http://127.0.0.1:8000/api/v1/variants/generate?post_id=$($POST.id)&platform=linkedin&tone=professional" | ConvertFrom-Json

curl.exe -sS -X POST "http://127.0.0.1:8000/api/v1/review/approve/$($VARIANT.id)"
curl.exe -sS -X POST "http://127.0.0.1:8000/api/v1/schedules/?variant_id=$($VARIANT.id)&scheduled_for=2026-09-02T12:00:00"
curl.exe -sS "http://127.0.0.1:8000/api/v1/history/$($VARIANT.id)"

$REJECTED = curl.exe -sS -X POST "http://127.0.0.1:8000/api/v1/variants/generate?post_id=$($POST.id)&platform=telegram&tone=professional" | ConvertFrom-Json
curl.exe -sS -X POST "http://127.0.0.1:8000/api/v1/review/reject/$($REJECTED.id)?reason=Needs+more+review"
```

---

## Local venv alternative
```powershell
cd C:\Flyrank\Capstone\flyrank-capstone-social-studio\social-studio
$env:PYTHONPATH = (Get-Location).Path
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

Then use the same curl commands above.
