from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.database import get_db
from backend.models import ContentPillar, Persona
from backend.schemas import ContentPillarSchema, PersonaSchema

router = APIRouter(prefix="/api/strategy", tags=["Strategy Builder"])

@router.get("/pillars", response_model=List[ContentPillarSchema])
def get_pillars(db: Session = Depends(get_db)):
    return db.query(ContentPillar).all()

@router.get("/personas", response_model=List[PersonaSchema])
def get_personas(db: Session = Depends(get_db)):
    return db.query(Persona).all()
