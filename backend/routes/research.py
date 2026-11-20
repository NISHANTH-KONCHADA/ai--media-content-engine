from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.database import get_db
from backend.models import ResearchObservation, ResearchOpportunity, CompetitorAudit
from backend.schemas import ResearchObservationSchema, ResearchOpportunitySchema, CompetitorAuditSchema

router = APIRouter(prefix="/api/research", tags=["Product & Market Research"])

@router.get("/observations", response_model=List[ResearchObservationSchema])
def get_observations(db: Session = Depends(get_db)):
    return db.query(ResearchObservation).order_by(ResearchObservation.number).all()

@router.get("/opportunities", response_model=List[ResearchOpportunitySchema])
def get_opportunities(db: Session = Depends(get_db)):
    return db.query(ResearchOpportunity).order_by(ResearchOpportunity.rank).all()

@router.get("/competitors", response_model=List[CompetitorAuditSchema])
def get_competitors(db: Session = Depends(get_db)):
    return db.query(CompetitorAudit).all()
