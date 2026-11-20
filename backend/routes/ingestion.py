import hashlib
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from backend.database import get_db
from backend.models import InputDocument
from backend.schemas import InputDocumentSchema

router = APIRouter(prefix="/api/ingestion", tags=["Input Ingestion"])

@router.get("/documents", response_model=List[InputDocumentSchema])
def list_documents(db: Session = Depends(get_db)):
    return db.query(InputDocument).order_by(InputDocument.created_at.desc()).all()

@router.post("/upload", response_model=InputDocumentSchema)
def upload_document(data: Dict[str, Any] = Body(...), db: Session = Depends(get_db)):
    title = data.get("title", "Untitled Document")
    content = data.get("content", "")
    input_type = data.get("input_type", "markdown")
    
    if not content.strip():
        raise HTTPException(status_code=400, detail="Document content cannot be empty")
        
    c_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
    
    existing = db.query(InputDocument).filter(InputDocument.content_hash == c_hash).first()
    if existing:
        return existing
        
    doc = InputDocument(
        title=title,
        input_type=input_type,
        content=content,
        content_hash=c_hash
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc
