from pydantic import BaseModel, Field
from typing import Optional, List
import datetime

class BrandSchema(BaseModel):
    id: Optional[int] = None
    name: str = "IncuBrix"
    tagline: str
    website: str
    audience: str
    brand_voice: str
    primary_color: str
    secondary_color: str
    accent_color: str
    approved_claims: str
    forbidden_claims: str

    class Config:
        from_attributes = True

class ResearchObservationSchema(BaseModel):
    id: Optional[int] = None
    number: int
    product_area: str
    what_happened: str
    worked_difficult: str
    evidence_url: str
    growth_impact: str

    class Config:
        from_attributes = True

class ResearchOpportunitySchema(BaseModel):
    id: Optional[int] = None
    rank: int
    opportunity: str
    evidence: str
    expected_impact: str
    how_to_measure: str
    target_30d: str

    class Config:
        from_attributes = True

class CompetitorAuditSchema(BaseModel):
    id: Optional[int] = None
    account_name: str
    platform: str
    followers: Optional[int] = None
    snapshot_date: str
    url: str
    recent_posting_frequency: str
    engagement_rate: str
    limitations: str

    class Config:
        from_attributes = True

class ContentPillarSchema(BaseModel):
    id: Optional[int] = None
    name: str
    code: str
    description: str
    target_ratio: float

    class Config:
        from_attributes = True

class PersonaSchema(BaseModel):
    id: Optional[int] = None
    title: str
    role: str
    geography: str
    goals: str
    pain_points: str
    preferred_platforms: str

    class Config:
        from_attributes = True

class InputDocumentSchema(BaseModel):
    id: Optional[int] = None
    title: str
    input_type: str
    content: str
    content_hash: Optional[str] = None
    created_at: Optional[datetime.datetime] = None

    class Config:
        from_attributes = True

class CreativeBriefSchema(BaseModel):
    id: Optional[int] = None
    input_id: Optional[int] = None
    topic: str
    pillar: str
    platform: str
    format: str
    hook: str
    key_takeaway: str
    cta: str
    status: str = "Approved"

    class Config:
        from_attributes = True

class AssetSchema(BaseModel):
    id: Optional[int] = None
    asset_id: str
    platform: str
    format: str
    content_pillar: str
    hook: str
    caption: str
    cta: str
    utm_link: str
    final_file_url: str
    source_file_url: str
    source_input: str
    tools_used: str
    rights_checked: str = "Yes"
    ai_label_needed: str = "No"
    scheduled_date: str
    test_published_url: Optional[str] = ""
    impressions_or_views: Optional[str] = ""
    engagement_rate: Optional[str] = ""
    clicks: Optional[str] = ""
    status: str = "Ready"
    notes: Optional[str] = ""
    fingerprint: Optional[str] = None

    class Config:
        from_attributes = True

class RunLogSchema(BaseModel):
    id: Optional[int] = None
    run_type: str
    input_size: str
    items_produced: int
    items_rejected: int
    duplicates_removed: int
    runtime_sec: float
    direct_cost: str
    log_file: str
    status: str
    created_at: Optional[datetime.datetime] = None

    class Config:
        from_attributes = True

class AudienceTestResponseSchema(BaseModel):
    id: Optional[int] = None
    participant_id: str
    creator_type: str
    experience_years: str
    preferred_variant: str
    reason: str
    submitted_at: str

    class Config:
        from_attributes = True
