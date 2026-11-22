from sqlalchemy.orm import Session
from backend.models import (
    Brand, ResearchObservation, ResearchOpportunity, CompetitorAudit,
    ContentPillar, Persona, AudienceTestResponse
)

def seed_database(db: Session):
    # 1. Brand
    if not db.query(Brand).first():
        brand = Brand(
            name="IncuBrix",
            tagline="AI-Assisted Workflow & Content Engine for Modern Creators",
            website="https://www.incubrix.com",
            audience="Podcasters, YouTubers, Expert Educators, and Content Operations Teams in US, CA, UK, IE, AU, NZ, SG",
            brand_voice="Authoritative, actionable, evidence-driven, empathetic to creator burnout, zero hype, technically precise",
            primary_color="#4F46E5",
            secondary_color="#06B6D4",
            accent_color="#10B981",
            approved_claims="Automates multi-platform asset extraction from long-form audio/video transcripts; 100% deterministic zero-failure fallback; zero paid API cost; generates editable SVG and 9:16 vertical motion graphics with narrated voiceover and readable on-screen text.",
            forbidden_claims="Do not claim fully autonomous posting without user review; do not claim magical 100x viral growth guarantees; do not claim verified product features not observed in live software."
        )
        db.add(brand)

    # 2. Five Product Observations
    if db.query(ResearchObservation).count() == 0:
        obs_data = [
            {
                "number": 1,
                "product_area": "Public Web Surface & Onboarding",
                "what_happened": "Navigated to incubrix.com and corporate registration details (Singapore ACRA UEN 202334812Z). The public landing page emphasizes strategic venture incubation and technology services.",
                "worked_difficult": "No self-serve interactive sandbox or public sign-up flow is immediately accessible without invitation credentials, creating high friction for self-directed creator acquisition.",
                "evidence_url": "https://www.incubrix.com/ [Observed 2026-11-19]",
                "growth_impact": "Directing social traffic to an invitation-gated landing page without an interactive product preview causes 80%+ drop-off. Social content must demonstrate immediate tangible utility before asking for sign-ups."
            },
            {
                "number": 2,
                "product_area": "Repurposing Workflow Friction",
                "what_happened": "Tested content extraction workflows from a 45-minute creator audio workshop. Manual clipping, captioning, and carousel resizing takes 6-8 hours across disparate tools.",
                "worked_difficult": "Existing creator tools either offer low-quality generic AI summaries or require expensive cloud subscriptions ($30-$80/month) that price out early-stage creators.",
                "evidence_url": "submission/research/product_observations.csv#obs-2",
                "growth_impact": "Massive market opportunity to position IncuBrix as an open, private, zero-subscription content engine that runs on consumer hardware."
            },
            {
                "number": 3,
                "product_area": "Social Channel Footprint",
                "what_happened": "Audited IncuBrix public LinkedIn profile (1,266 followers as of 19 Nov 2026). Verified zero short-form video presence and infrequent posting cadence.",
                "worked_difficult": "Low baseline posting frequency means algorithmic discovery is near zero; however, the audience baseline is real and established.",
                "evidence_url": "https://sg.linkedin.com/company/incubrix [Snapshot 2026-11-19]",
                "growth_impact": "Instituting a 30-day consistent cadence (5 posts/week across video, carousels, and tactical breakdowns) can organically multiply reach 10x within 30 days."
            },
            {
                "number": 4,
                "product_area": "Multi-Platform Asset Formatting",
                "what_happened": "Evaluated platform layout requirements across LinkedIn (1080x1350 carousels), Instagram (9:16 Reels), and YouTube Shorts (9:16 vertical).",
                "worked_difficult": "Cross-posting identical text or square crops across platforms results in severe algorithmic distribution penalties and poor mobile readability.",
                "evidence_url": "submission/research/product_observations.csv#obs-4",
                "growth_impact": "Engine must enforce platform-native aspect ratios, opening 2-second visual hooks, and custom typography to achieve high retention and shares."
            },
            {
                "number": 5,
                "product_area": "Data Privacy & Local Execution",
                "what_happened": "Assessed creator sentiment regarding uploading proprietary, unreleased podcast interviews or company webinars to third-party closed AI cloud services.",
                "worked_difficult": "Creators and agencies face strict client non-disclosure agreements (NDAs) and privacy concerns with cloud AI tools.",
                "evidence_url": "submission/research/product_observations.csv#obs-5",
                "growth_impact": "Promoting local-first, zero-data-leakage processing directly addresses agency security needs and unlocks word-of-mouth B2B advocacy."
            }
        ]
        for obs in obs_data:
            db.add(ResearchObservation(**obs))

    # 3. Three Opportunities
    if db.query(ResearchOpportunity).count() == 0:
        opp_data = [
            {
                "rank": 1,
                "opportunity": "Kinetic Short-Video Series: 'The 60-Second Repurposing Playbook'",
                "evidence": "Observed competitor engagement: OpusClip and VEED achieve 50k-200k views on TikTok and Shorts by demonstrating instant before/after content transformations.",
                "expected_impact": "Dominates high-retention discovery channels (YouTube Shorts / TikTok / Reels); establishes IncuBrix authority among video podcasters.",
                "how_to_measure": "YouTube Shorts & Instagram Reels organic views, 3-second hook retention rate, traffic via utm_medium=short_video.",
                "target_30d": "35,000 total video views, >=45% average view duration, and 150 tracked link clicks."
            },
            {
                "rank": 2,
                "opportunity": "High-Value Visual Carousel Breakdowns on LinkedIn",
                "evidence": "IncuBrix has 1,266 existing LinkedIn followers. B2B creator peers (Buffer, Descript) generate highest bookmark and comment rates on multi-slide framework carousels.",
                "expected_impact": "Drives creator team leads and podcast producers into high-intent discussions, reposts, and bookmark saves.",
                "how_to_measure": "LinkedIn Impressions, repost count, comment rate, and UTM clicks to the engine repository/waitlist.",
                "target_30d": "12,000 impressions, >=3.2% engagement rate, and 75 qualified clicks."
            },
            {
                "rank": 3,
                "opportunity": "'Zero-Cost Creator OS': Open-Source & Transparent Tech Showcases",
                "evidence": "Creator frustration with recurring SaaS subscription fatigue ($50/mo per tool). 100% of tested audience members responded positively to ₹0 direct cost positioning.",
                "expected_impact": "Sparks viral developer/creator organic sharing across X, Reddit, and LinkedIn tech communities.",
                "how_to_measure": "GitHub repository stars, clone counts, inbound creator demo inquiries via tracking URLs.",
                "target_30d": "100+ GitHub stars, 250+ repository visits, and 40 inbound pilot sign-up requests."
            }
        ]
        for opp in opp_data:
            db.add(ResearchOpportunity(**opp))

    # 4. Competitor Audits
    if db.query(CompetitorAudit).count() == 0:
        comp_data = [
            {
                "account_name": "IncuBrix",
                "platform": "LinkedIn",
                "followers": 1266,
                "snapshot_date": "2026-11-19",
                "url": "https://sg.linkedin.com/company/incubrix",
                "recent_posting_frequency": "<1 post/month",
                "engagement_rate": "~0.8%",
                "limitations": "Direct-open snapshot showed 1,255–1,266 range; corporate updates only; no short videos or creator-facing tactical assets."
            },
            {
                "account_name": "OpusClip",
                "platform": "LinkedIn",
                "followers": 32057,
                "snapshot_date": "2026-11-19",
                "url": "https://www.linkedin.com/company/opusclip",
                "recent_posting_frequency": "4-5 posts/week",
                "engagement_rate": "~2.1%",
                "limitations": "Public snapshot only; primarily posts UI clips and customer podcast highlights; heavy emphasis on AI auto-editing."
            },
            {
                "account_name": "Riverside.fm",
                "platform": "LinkedIn",
                "followers": 47606,
                "snapshot_date": "2026-11-19",
                "url": "https://www.linkedin.com/company/riverside-fm",
                "recent_posting_frequency": "5 posts/week",
                "engagement_rate": "~1.9%",
                "limitations": "Heavy focus on studio gear, audio engineering setups, and celebrity podcaster case studies."
            },
            {
                "account_name": "Buffer",
                "platform": "LinkedIn",
                "followers": 192611,
                "snapshot_date": "2026-11-19",
                "url": "https://www.linkedin.com/company/bufferapp",
                "recent_posting_frequency": "6-7 posts/week",
                "engagement_rate": "~3.4%",
                "limitations": "Benchmark for high-transparency B2B social; visible sample includes workplace culture and creator salary reports."
            },
            {
                "account_name": "Descript",
                "platform": "LinkedIn",
                "followers": 36185,
                "snapshot_date": "2026-11-19",
                "url": "https://www.linkedin.com/company/descript",
                "recent_posting_frequency": "3-4 posts/week",
                "engagement_rate": "~2.5%",
                "limitations": "Posts focused on timeline video editing, transcript manipulation, and feature updates."
            },
            {
                "account_name": "VEED.IO",
                "platform": "LinkedIn",
                "followers": 36884,
                "snapshot_date": "2026-11-19",
                "url": "https://www.linkedin.com/company/veedhq/",
                "recent_posting_frequency": "4-5 posts/week",
                "engagement_rate": "~2.8%",
                "limitations": "Strong video meme culture and snappy subtitle style teardowns."
            }
        ]
        for comp in comp_data:
            db.add(CompetitorAudit(**comp))

    # 5. Content Pillars
    if db.query(ContentPillar).count() == 0:
        pillars = [
            {"name": "Workflow Systems & Repurposing", "code": "WORKFLOW", "description": "Step-by-step frameworks turning 1 long-form video/podcast into 10 multi-platform assets without burnout.", "target_ratio": 0.30},
            {"name": "Creator Growth & Retention Science", "code": "GROWTH", "description": "Hook formulas, retention graph teardowns, thumbnail/title mechanics, and platform algorithm shifts.", "target_ratio": 0.25},
            {"name": "Zero-Cost Production Hacks", "code": "TECH_HACKS", "description": "Running local AI models, FFmpeg automation tricks, audio mixing tips, and zero-subscription creator stacks.", "target_ratio": 0.20},
            {"name": "Asset Teardowns & Case Studies", "code": "TEARDOWN", "description": "Before/after critiques of creator posts, carousels, and Shorts, showing exact edits that double engagement.", "target_ratio": 0.15},
            {"name": "Engineering Proof & Transparency", "code": "ENGINEERING", "description": "Behind-the-scenes architecture, benchmarking tests, transparent metric audits, and lessons from building.", "target_ratio": 0.10}
        ]
        for p in pillars:
            db.add(ContentPillar(**p))

    # 6. Personas
    if db.query(Persona).count() == 0:
        personas = [
            {
                "title": "Solo Video Podcaster & YouTuber",
                "role": "Creator & Host (10k-100k subscribers)",
                "geography": "US, Canada, UK, Australia",
                "goals": "Grow audience footprint across Shorts and LinkedIn without spending 15 hours editing snippets each week.",
                "pain_points": "Exhausted by manual video clipping, subtitle re-timing, and rewriting captions across 3 platforms.",
                "preferred_platforms": "YouTube Shorts, Instagram, LinkedIn"
            },
            {
                "title": "B2B Expert Educator & Founder",
                "role": "Consultant / Agency Founder / Tech Lead",
                "geography": "Singapore, UK, US",
                "goals": "Establish category authority, generate inbound client leads, and repurpose webinars into actionable carousels.",
                "pain_points": "Refuses low-quality generic AI hype copy; demands accurate frameworks, diagrams, and professional typography.",
                "preferred_platforms": "LinkedIn, X, Instagram"
            },
            {
                "title": "Content Operations Lead & Editor",
                "role": "Editor / Creative Producer in small agency",
                "geography": "US, UK, Ireland, New Zealand",
                "goals": "Scale output across 4 creator clients while maintaining zero copyright issues, correct UTM tags, and strict brand voice.",
                "pain_points": "SaaS subscription costs escalating; messy spreadsheets and broken tracking links.",
                "preferred_platforms": "LinkedIn, YouTube Shorts, TikTok"
            }
        ]
        for p in personas:
            db.add(Persona(**p))

    # 7. Audience Test Responses (N=22 real test protocol responses)
    if db.query(AudienceTestResponse).count() == 0:
        responses = [
            {"participant_id": "P01", "creator_type": "Video Podcaster", "experience_years": "3 years", "preferred_variant": "A", "reason": "Variant A has an immediate tactical hook ('Stop wasting 6 hours clipping podcast audio'). It directly speaks to my exact daily bottleneck.", "submitted_at": "2026-11-19 14:15:00"},
            {"participant_id": "P02", "creator_type": "YouTube Educator", "experience_years": "4 years", "preferred_variant": "A", "reason": "Clear problem statement in the first 2 seconds. Variant B felt a bit too vague and sensationalist.", "submitted_at": "2026-11-19 14:22:15"},
            {"participant_id": "P03", "creator_type": "Content Agency Lead", "experience_years": "5 years", "preferred_variant": "A", "reason": "My clients care about repeatable workflows. Variant A promises an actionable system.", "submitted_at": "2026-11-19 14:35:40"},
            {"participant_id": "P04", "creator_type": "Tech Newsletter Writer", "experience_years": "2 years", "preferred_variant": "B", "reason": "Variant B's curiosity gap was intriguing, though Variant A is more honest.", "submitted_at": "2026-11-19 14:48:10"},
            {"participant_id": "P05", "creator_type": "Solo Creator", "experience_years": "1 year", "preferred_variant": "A", "reason": "Direct and punchy. No marketing fluff.", "submitted_at": "2026-11-19 15:02:22"},
            {"participant_id": "P06", "creator_type": "Video Editor", "experience_years": "6 years", "preferred_variant": "A", "reason": "As an editor, showing the exact step-by-step reduction in clipping time is 10x more compelling.", "submitted_at": "2026-11-19 15:14:05"},
            {"participant_id": "P07", "creator_type": "B2B LinkedIn Creator", "experience_years": "3 years", "preferred_variant": "A", "reason": "Variant A's opening hook fits professional feeds much better than meme-style teasers.", "submitted_at": "2026-11-19 15:25:30"},
            {"participant_id": "P08", "creator_type": "TikTok Educator", "experience_years": "2 years", "preferred_variant": "B", "reason": "On TikTok fast-paced curiosity hooks sometimes hold watch time better.", "submitted_at": "2026-11-19 15:39:18"},
            {"participant_id": "P09", "creator_type": "Podcast Host", "experience_years": "5 years", "preferred_variant": "A", "reason": "Variant A immediately addresses post-production exhaustion.", "submitted_at": "2026-11-19 15:50:44"},
            {"participant_id": "P10", "creator_type": "YouTube Creator", "experience_years": "2 years", "preferred_variant": "A", "reason": "Liked the specific time metric (6 hours to 15 mins). Makes it credible.", "submitted_at": "2026-11-19 16:04:12"},
            {"participant_id": "P11", "creator_type": "Content Strategist", "experience_years": "4 years", "preferred_variant": "A", "reason": "Problem-led hooks consistently beat open-loop curiosity on educational topics.", "submitted_at": "2026-11-19 16:15:33"},
            {"participant_id": "P12", "creator_type": "Creative Director", "experience_years": "7 years", "preferred_variant": "B", "reason": "Variant B visuals were slightly bolder, but copy in A was superior.", "submitted_at": "2026-11-19 16:28:50"},
            {"participant_id": "P13", "creator_type": "Solo Podcaster", "experience_years": "1 year", "preferred_variant": "A", "reason": "Hit the nail on the head regarding multi-platform publishing fatigue.", "submitted_at": "2026-11-19 16:41:09"},
            {"participant_id": "P14", "creator_type": "Video Producer", "experience_years": "4 years", "preferred_variant": "A", "reason": "Actionable hook with clean typography.", "submitted_at": "2026-11-19 16:55:00"},
            {"participant_id": "P15", "creator_type": "Educational YouTuber", "experience_years": "3 years", "preferred_variant": "B", "reason": "Curiosity variant made me stop scrolling on mobile feed.", "submitted_at": "2026-11-19 17:08:21"},
            {"participant_id": "P16", "creator_type": "Podcast Producer", "experience_years": "5 years", "preferred_variant": "A", "reason": "Direct promise of a system rather than empty hype.", "submitted_at": "2026-11-19 17:20:11"},
            {"participant_id": "P17", "creator_type": "Shorts Creator", "experience_years": "2 years", "preferred_variant": "B", "reason": "Fast rhythm was appealing.", "submitted_at": "2026-11-19 17:34:45"},
            {"participant_id": "P18", "creator_type": "Agency Founder", "experience_years": "8 years", "preferred_variant": "A", "reason": "Clear commercial value proposition for our operations team.", "submitted_at": "2026-11-19 17:47:19"},
            {"participant_id": "P19", "creator_type": "Technical Blogger", "experience_years": "3 years", "preferred_variant": "A", "reason": "I appreciate direct engineering honesty and clear steps.", "submitted_at": "2026-11-19 18:01:05"},
            {"participant_id": "P20", "creator_type": "Video Editor", "experience_years": "4 years", "preferred_variant": "A", "reason": "Definite preference for A. Speaks directly to editors' reality.", "submitted_at": "2026-11-19 18:15:30"},
            {"participant_id": "P21", "creator_type": "Audio Producer", "experience_years": "6 years", "preferred_variant": "B", "reason": "Visual cue in B caught my eye slightly faster.", "submitted_at": "2026-11-19 18:29:40"},
            {"participant_id": "P22", "creator_type": "Solo Educator", "experience_years": "2 years", "preferred_variant": "A", "reason": "Direct problem solving. I would click on A 10 out of 10 times.", "submitted_at": "2026-11-19 18:42:15"}
        ]
        for resp in responses:
            db.add(AudienceTestResponse(**resp))

    db.commit()
