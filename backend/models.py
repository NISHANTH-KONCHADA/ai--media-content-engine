import datetime
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base

class Brand(Base):
    __tablename__ = "brands"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), default="IncuBrix", nullable=False)
    tagline = Column(String(255), default="AI-Assisted Workflow & Content Engine for Modern Creators")
    website = Column(String(255), default="https://www.incubrix.com")
    audience = Column(Text, default="Podcasters, YouTubers, Expert Educators, and Content Operations Teams in US, CA, UK, IE, AU, NZ, SG")
    brand_voice = Column(Text, default="Authoritative, actionable, evidence-driven, empathetic to creator burnout, zero hype, technically precise")
    primary_color = Column(String(20), default="#4F46E5")
    secondary_color = Column(String(20), default="#06B6D4")
    accent_color = Column(String(20), default="#10B981")
    approved_claims = Column(Text, default="Automates multi-platform asset extraction from long-form audio/video transcripts; 100% deterministic zero-failure fallback; zero paid API cost; generates editable SVG and 9:16 vertical motion graphics with subtitles.")
    forbidden_claims = Column(Text, default="Do not claim fully autonomous posting without user review; do not claim magical 100x viral growth guarantees; do not claim verified product features not observed in live software.")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class ResearchObservation(Base):
    __tablename__ = "research_observations"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, nullable=False)
    product_area = Column(String(100), nullable=False)
    what_happened = Column(Text, nullable=False)
    worked_difficult = Column(Text, nullable=False)
    evidence_url = Column(String(255), nullable=False)
    growth_impact = Column(Text, nullable=False)

class ResearchOpportunity(Base):
    __tablename__ = "research_opportunities"
    id = Column(Integer, primary_key=True, index=True)
    rank = Column(Integer, unique=True, nullable=False)
    opportunity = Column(String(255), nullable=False)
    evidence = Column(Text, nullable=False)
    expected_impact = Column(Text, nullable=False)
    how_to_measure = Column(Text, nullable=False)
    target_30d = Column(String(255), nullable=False)

class CompetitorAudit(Base):
    __tablename__ = "competitor_audits"
    id = Column(Integer, primary_key=True, index=True)
    account_name = Column(String(100), nullable=False)
    platform = Column(String(50), nullable=False)
    followers = Column(Integer, nullable=True)
    snapshot_date = Column(String(50), nullable=False)
    url = Column(String(255), nullable=False)
    recent_posting_frequency = Column(String(100), default="3-5 posts/week")
    engagement_rate = Column(String(50), default="~1.2% - 2.8%")
    limitations = Column(Text, nullable=False)

class ContentPillar(Base):
    __tablename__ = "content_pillars"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    code = Column(String(20), nullable=False)
    description = Column(Text, nullable=False)
    target_ratio = Column(Float, default=0.20)

class Persona(Base):
    __tablename__ = "personas"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False)
    geography = Column(String(100), default="US, UK, CA, AU, SG")
    goals = Column(Text, nullable=False)
    pain_points = Column(Text, nullable=False)
    preferred_platforms = Column(String(100), nullable=False)

class InputDocument(Base):
    __tablename__ = "input_documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    input_type = Column(String(50), default="markdown") # transcript, blog, webinar, demo
    content = Column(Text, nullable=False)
    content_hash = Column(String(64), unique=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class CreativeBrief(Base):
    __tablename__ = "creative_briefs"
    id = Column(Integer, primary_key=True, index=True)
    input_id = Column(Integer, ForeignKey("input_documents.id"), nullable=True)
    topic = Column(String(255), nullable=False)
    pillar = Column(String(100), nullable=False)
    platform = Column(String(50), nullable=False)
    format = Column(String(50), nullable=False)
    hook = Column(Text, nullable=False)
    key_takeaway = Column(Text, nullable=False)
    cta = Column(Text, nullable=False)
    status = Column(String(30), default="Approved") # Pending, Approved, Rejected
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Asset(Base):
    __tablename__ = "assets"
    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(String(50), unique=True, index=True, nullable=False)
    platform = Column(String(50), nullable=False)
    format = Column(String(50), nullable=False)
    content_pillar = Column(String(100), nullable=False)
    hook = Column(Text, nullable=False)
    caption = Column(Text, nullable=False)
    cta = Column(Text, nullable=False)
    utm_link = Column(String(500), nullable=False)
    final_file_url = Column(String(500), nullable=False)
    source_file_url = Column(String(500), nullable=False)
    source_input = Column(String(255), nullable=False)
    tools_used = Column(String(255), nullable=False)
    rights_checked = Column(String(10), default="Yes")
    ai_label_needed = Column(String(10), default="No")
    scheduled_date = Column(String(50), nullable=False)
    test_published_url = Column(String(500), default="")
    impressions_or_views = Column(String(50), default="")
    engagement_rate = Column(String(50), default="")
    clicks = Column(String(50), default="")
    status = Column(String(30), default="Ready") # Ready, Draft, Rejected
    notes = Column(Text, default="")
    fingerprint = Column(String(64), index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class RunLog(Base):
    __tablename__ = "run_logs"
    id = Column(Integer, primary_key=True, index=True)
    run_type = Column(String(50), nullable=False) # normal, repeat, refresh, recovery
    input_size = Column(String(50), nullable=False)
    items_produced = Column(Integer, default=0)
    items_rejected = Column(Integer, default=0)
    duplicates_removed = Column(Integer, default=0)
    runtime_sec = Column(Float, default=0.0)
    direct_cost = Column(String(50), default="₹0.00")
    log_file = Column(String(255), nullable=False)
    status = Column(String(50), default="SUCCESS")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class AudienceTestResponse(Base):
    __tablename__ = "audience_test_responses"
    id = Column(Integer, primary_key=True, index=True)
    participant_id = Column(String(50), unique=True, nullable=False)
    creator_type = Column(String(100), nullable=False)
    experience_years = Column(String(50), nullable=False)
    preferred_variant = Column(String(10), nullable=False) # A or B
    reason = Column(Text, nullable=False)
    submitted_at = Column(String(50), nullable=False)
