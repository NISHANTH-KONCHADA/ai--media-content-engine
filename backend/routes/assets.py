from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any
from backend.database import get_db
from backend.models import Asset
from backend.schemas import AssetSchema
from backend.config import settings
from engine.quality_gate import run_campaign_audit, audit_asset

router = APIRouter(prefix="/api/assets", tags=["Asset Library & Quality"])

@router.get("", response_model=List[AssetSchema])
def list_assets(
    platform: Optional[str] = Query(None),
    format: Optional[str] = Query(None),
    pillar: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Asset)
    if platform:
        query = query.filter(Asset.platform == platform)
    if format:
        query = query.filter(Asset.format == format)
    if pillar:
        query = query.filter(Asset.content_pillar == pillar)
    if status:
        query = query.filter(Asset.status == status)
    return query.order_by(Asset.asset_id).all()

@router.get("/{asset_id}")
def get_asset(asset_id: str, db: Session = Depends(get_db)):
    asset = db.query(Asset).filter(Asset.asset_id == asset_id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    
    asset_dict = {c.name: getattr(asset, c.name) for c in asset.__table__.columns}
    audit = audit_asset(asset_dict, settings.SUBMISSION_DIR)
    
    return {
        "asset": asset_dict,
        "audit": audit
    }

@router.put("/{asset_id}", response_model=AssetSchema)
def update_asset(asset_id: str, data: Dict[str, Any], db: Session = Depends(get_db)):
    asset = db.query(Asset).filter(Asset.asset_id == asset_id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
        
    for k, v in data.items():
        if hasattr(asset, k) and k != "id" and k != "asset_id":
            setattr(asset, k, v)
            
    db.commit()
    db.refresh(asset)
    return asset

@router.get("/audit/summary")
def get_audit_summary(db: Session = Depends(get_db)) -> Dict[str, Any]:
    assets = db.query(Asset).order_by(Asset.asset_id).all()
    asset_dicts = [{c.name: getattr(a, c.name) for c in a.__table__.columns} for a in assets]
    return run_campaign_audit(asset_dicts, settings.SUBMISSION_DIR, sample_size=20)
