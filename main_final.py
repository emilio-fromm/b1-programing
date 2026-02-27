# Copyright by Emilio

from fastapi import FastAPI
from routes import users

app = FastAPI(
    title="User Management API",
    description="FastAPI backend for user management - by Emilio",
    version="1.0.0"
)

app.include_router(users.router, prefix="/users", tags=["Users"])


@app.get("/")
def health_check():
    return {"status": "running", "message": "API is active"}


@app.get("/health")
def health_details():
    return {
        "status": "ok",
        "version": "1.0.0",
        "description": "User Management API running smoothly"
    }
