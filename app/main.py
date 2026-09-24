from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="CloudSentinel API",
    description="Self-Healing DevSecOps Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "application": "CloudSentinel",
        "status": "running",
        "version": "1.0.0",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "cloudsentinel-api"
    }


@app.get("/version")
def version():
    return {
        "application": "CloudSentinel",
        "version": "1.0.0"
    }