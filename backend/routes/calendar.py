import csv
import io
from fastapi import APIRouter, Depends
from fastapi.responses import Response
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from backend.database import get_db
from backend.models import Asset

router = APIRouter(prefix="/api/calendar", tags=["Calendar"])

WORKBOOK_COLUMNS = [
    "asset_id", "platform", "format", "content_pillar", "hook", "caption",
    "cta", "utm_link", "final_file_url", "source_file_url", "source_input",
    "tools_used", "rights_checked", "ai_label_needed", "scheduled_date",
    "test_published_url", "impressions_or_views", "engagement_rate",
    "clicks", "status", "notes", "duplicate_check", "completeness_check"
]

@router.get("/slots")
def get_calendar_slots(db: Session = Depends(get_db)) -> List[Dict[str, Any]]:
    assets = db.query(Asset).order_by(Asset.scheduled_date).all()
    slots = []
    for a in assets:
        slots.append({
            "asset_id": a.asset_id,
            "scheduled_date": a.scheduled_date,
            "platform": a.platform,
            "format": a.format,
            "pillar": a.content_pillar,
            "hook": a.hook,
            "status": a.status
        })
    return slots

@router.get("/export.csv")
def export_calendar_csv(db: Session = Depends(get_db)):
    assets = db.query(Asset).order_by(Asset.asset_id).all()
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write exact 23-column header
    writer.writerow(WORKBOOK_COLUMNS)
    
    for a in assets:
        # Check completeness formula logic locally for CSV export
        is_complete = bool(a.platform and a.format and a.content_pillar and a.hook and a.caption and a.cta and a.utm_link and a.final_file_url and a.source_file_url and a.rights_checked and a.scheduled_date and a.status)
        completeness = "COMPLETE" if is_complete else "MISSING FIELDS"
        
        writer.writerow([
            a.asset_id,
            a.platform,
            a.format,
            a.content_pillar,
            a.hook,
            a.caption,
            a.cta,
            a.utm_link,
            a.final_file_url,
            a.source_file_url,
            a.source_input,
            a.tools_used,
            a.rights_checked,
            a.ai_label_needed,
            a.scheduled_date,
            a.test_published_url or "",
            a.impressions_or_views or "",
            a.engagement_rate or "",
            a.clicks or "",
            a.status,
            a.notes or "",
            "UNIQUE",
            completeness
        ])
        
    csv_bytes = output.getvalue().encode("utf-8")
    return Response(
        content=csv_bytes,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=calendar.csv"}
    )
