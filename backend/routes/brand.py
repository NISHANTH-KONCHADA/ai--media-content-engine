from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import Brand
from backend.schemas import BrandSchema

router = APIRouter(prefix="/api/brand", tags=["Brand Workspace"])

@router.get("", response_model=BrandSchema)
def get_brand(db: Session = Depends(get_db)):
    brand = db.query(Brand).first()
    if not brand:
        raise HTTPException(status_code=404, detail="Brand profile not found")
    return brand

@router.put("", response_model=BrandSchema)
def update_brand(data: BrandSchema, db: Session = Depends(get_db)):
    brand = db.query(Brand).first()
    if not brand:
        brand = Brand()
        db.add(brand)
    
    for key, val in data.dict(exclude={"id"}).items():
        setattr(brand, key, val)
        
    db.commit()
    db.refresh(brand)
    return brand
