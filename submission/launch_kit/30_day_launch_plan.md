# 30-Day Turnkey Launch Plan — IncuBrix Social Growth Engine

**Document Purpose:** Complete, step-by-step operational roadmap IncuBrix can execute starting next Monday with zero rework.  
**Operating Budget:** Direct Software/API Spend = **₹0.00 / month**  
**Assigned Owner:** Growth Engineer / Content Operations Lead

---

## 1. Launch Architecture Overview

```mermaid
flowchart LR
    W1["Week 1: Baseline Activation"] --> W2["Week 2: Engagement Amplification"]
    W2 --> W3["Week 3: Conversion Optimization"]
    W3 --> W4["Week 4: Scale & Retrospective"]
```

---

## 2. Week-by-Week Operational Execution

### Week 1: Baseline Activation & Platform Calibration
- **Goal:** Establish consistent publishing presence across LinkedIn, Instagram, and YouTube Shorts; seed top 7 assets.
- **Publishing Schedule:**
  - *Monday (09:00 UTC):* A001 (YouTube Shorts) — "Stop doing this with your recording"
  - *Tuesday (14:00 UTC):* A011 (LinkedIn Carousel) — "The 5-Step Framework to Turn 1 Podcast into a Week of Content"
  - *Wednesday (16:00 UTC):* A002 (Instagram Reel) — "Finding your best clip start point"
  - *Thursday (14:00 UTC):* A021 (LinkedIn Graphic) — "The biggest mistake in creator workflows"
  - *Friday (10:00 UTC):* A003 (YouTube Shorts) — "Keep speaker context clean"
- **Operational Tasks:**
  - Verify all 23-column UTM links in Google Analytics / server logs.
  - Pin the template link comment within 5 minutes of each video publish.
  - Spend 30 minutes following publish engaging in relevant creator comment sections (#VideoEditing, #Podcasting).

### Week 2: Engagement Amplification & Audience Dialogue
- **Goal:** Accelerate comment velocity, bookmark saves, and inbound creator feedback.
- **Publishing Schedule:** 7 assets deployed across all 3 platforms (A004 to A010, A012, A022).
- **Operational Tasks:**
  - Respond to 100% of comments within the first 60 minutes of posting.
  - Direct interested commenters to the open-source GitHub repository and waitlist.
  - Run weekly telemetry report on 3-second hook retention drop-offs.

### Week 3: Conversion Optimization & Retargeting Hooks
- **Goal:** Drive creator traffic to product trial sign-ups and workflow template downloads.
- **Publishing Schedule:** 8 assets deployed (A013 to A016 carousels, A023 to A026 graphics).
- **Operational Tasks:**
  - Analyze top 3 performing hooks from Weeks 1-2.
  - Deploy refreshed assets from `engine/refresh.md` to test second-order lessons.
  - Monitor click-through rate (CTR) on UTM campaign parameters.

### Week 4: Retrospective, Review & Engine Ingestion
- **Goal:** Audit 30-day performance against targets; ingest next batch of creator recordings.
- **Publishing Schedule:** Final 8 assets deployed (A017 to A020, A027 to A030).
- **Operational Tasks:**
  - Compile 30-day analytics report (Impressions, Engagement Rate, Clicks, Sign-ups).
  - Ingest new creator workshop or podcast recording into `engine/run.py` to auto-generate Month 2 calendar.
  - Present growth review to IncuBrix leadership.
