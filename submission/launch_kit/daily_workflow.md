# Daily and Weekly Operating Workflows — IncuBrix Content Engine

---

## 1. Daily Operating Workflow (Time Budget: 45 Minutes/Day)

| Time Slot | Phase | Core Action Items | Assigned Owner | Tool / Output |
|---|---|---|---|---|
| **08:30 - 08:45** | **Pre-Publish Verification** | Inspect scheduled asset folder (`submission/content/assets/A0xx`). Check final video / slide image rendering on mobile preview. Confirm UTM destination link resolves cleanly. | Growth Engineer | Local Asset Folder / Mobile Web |
| **08:45 - 09:00** | **Publish & Pin** | Upload asset to designated platform (LinkedIn / Instagram / YouTube Shorts). Paste platform-tailored caption, hashtags, and CTA. Immediately post pinned comment with clean tracking URL. | Growth Engineer | Native Platform Studio |
| **09:00 - 09:30** | **Golden Hour Engagement** | Monitor initial algorithmic engagement. Reply thoughtfully to every comment within the first 30 minutes to signal high conversational velocity to the algorithm. Engage with 5 peer creator posts. | Growth Engineer | Platform Feeds |
| **17:00 - 17:15** | **Telemetry Logging** | Record 8-hour view count, engagement rate, and inbound clicks in `metrics-tracking.csv`. Flag high-performing hooks for future campaign iterations. | Growth Engineer | Tracking Spreadsheet |

---

## 2. Weekly Operating Cadence (Every Friday Afternoon, 2 Hours)

1. **Campaign Performance Review (45 min):**
   - Aggregate impressions, engagement rates, and UTM clicks across all 3 platforms.
   - Calculate Week-over-Week (WoW) growth.
   - Identify the top-performing format (e.g. Shorts vs Carousels).
2. **Input Ingestion & Batch Engine Execution (30 min):**
   - Take 1 new podcast episode or workshop transcript.
   - Run `python engine/run.py` to extract topics and plan the upcoming week.
   - Review creative briefs in the approval queue; approve or reject assets.
3. **Quality & Rights Gate Verification (20 min):**
   - Run automated quality check: verify zero copyright issues, correct aspect ratios, and valid UTM links.
4. **Schedule Staging (25 min):**
   - Export `calendar.csv` and stage next week's assets in drafts.
