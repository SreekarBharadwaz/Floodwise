from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from pathlib import Path
import json
import os

BASE_DIR = Path(os.getenv("FLOODWISE_DATA_DIR", "data/sample"))
SUBMISSIONS_DIR = BASE_DIR / "submissions"
SUBMISSIONS_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(
    title="FloodWise Backend",
    version="1.0.0",
    description="Emergency-response scenario intake API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "online", "message": "FloodWise backend is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/api/intake")
async def receive_data(data: dict):
    role = str(data.get("role", "unknown")).lower()
    if role not in {"admin", "user"}:
        role = "unknown"

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = SUBMISSIONS_DIR / f"{role}_{timestamp}.json"
    latest_file = BASE_DIR / f"{role}_latest.json"

    with filename.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    with latest_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    responses = data.get("responses", {})
    return {
        "status": "success",
        "message": "FloodWise data received successfully",
        "role": role,
        "timestamp": timestamp,
        "received_fields": len(responses),
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.backend:app", host="0.0.0.0", port=8000, reload=True)
