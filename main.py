from fastapi import FastAPI
from database import engine
from models import Base
from routers import inventory, notifications, posts

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Calsoft Internship Assignment 1 Shriya Sharma",
    description="Solutions for Q1 Inventory API, Q2 Device Notifications, Q3 Posts Pagination",
    version="1.0.0"
)

app.include_router(inventory.router,     tags=["Q1 Inventory Report"])
app.include_router(notifications.router, tags=["Q2 Device Notifications"])
app.include_router(posts.router,         tags=["Q3 Posts Pagination"])


@app.get("/", tags=["Health"])
def root():
    return {
        "message": "Assignment 1 API is running!",
        "docs":    "Visit /docs to test all endpoints"
    }