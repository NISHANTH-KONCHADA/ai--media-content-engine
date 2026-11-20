from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from backend.database import get_db
from backend.models import CreativeBrief, InputDocument
from backend.schemas import CreativeBriefSchema

router = APIRouter(prefix="/api/planner", tags=["Content Planner & Brief Approval"])

@router.get("/briefs", response_model=List[CreativeBriefSchema])
def list_briefs(status: str = None, db: Session = Depends(get_db)):
    q = db.query(CreativeBrief)
    if status:
        q = q.filter(CreativeBrief.status == status)
    return q.order_by(CreativeBrief.id).all()

@router.put("/briefs/{brief_id}/status")
def update_brief_status(brief_id: int, status: str = Body(..., embed=True), db: Session = Depends(get_db)):
    brief = db.query(CreativeBrief).filter(CreativeBrief.id == brief_id).first()
    if not brief:
        raise HTTPException(status_code=404, detail="Brief not found")
    brief.status = status
    db.commit()
    db.refresh(brief)
    return {"status": "SUCCESS", "brief_id": brief.id, "new_status": brief.status}
