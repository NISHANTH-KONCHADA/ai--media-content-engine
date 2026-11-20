from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import os

from backend.config import settings
from backend.database import engine, Base, SessionLocal
from backend.seeder import seed_database
from backend.logging_config import logger

from backend.routes import (
    health,
    brand,
    research,
    strategy,
    audience,
    assets,
    calendar,
    runs,
    ingestion,
    planner
)

# Initialize Database Schema
Base.metadata.create_all(bind=engine)

# Seed database with initial verified assessment data
with SessionLocal() as db:
    seed_database(db)

app = FastAPI(
    title="IncuBrix AI Social Media Marketing & Content Engine",
    description="Zero-cost, local-first content engine powering creator social marketing workflows",
    version="1.0.0"
)

# Configure CORS for local development & dashboard
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(health.router)
app.include_router(brand.router)
app.include_router(research.router)
app.include_router(strategy.router)
app.include_router(audience.router)
app.include_router(assets.router)
app.include_router(calendar.router)
app.include_router(runs.router)
app.include_router(ingestion.router)
app.include_router(planner.router)

# Mount static file directory for rendered assets
assets_dir = settings.SUBMISSION_DIR / "content" / "assets"
assets_dir.mkdir(parents=True, exist_ok=True)
app.mount("/static/assets", StaticFiles(directory=str(assets_dir)), name="assets")

@app.get("/dashboard", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
def get_dashboard():
    dashboard_path = Path(__file__).resolve().parent / "static" / "dashboard.html"
    if dashboard_path.exists():
        with open(dashboard_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h1>IncuBrix Engine Online</h1><p><a href='/docs'>API Documentation</a></p>")
