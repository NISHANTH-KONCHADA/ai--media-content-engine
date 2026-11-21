from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.database import get_db
from backend.models import RunLog
from backend.schemas import RunLogSchema

router = APIRouter(prefix="/api/runs", tags=["Run History"])

@router.get("", response_model=List[RunLogSchema])
def get_run_history(db: Session = Depends(get_db)):
    return db.query(RunLog).order_by(RunLog.created_at.desc()).all()
