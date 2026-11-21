# IncuBrix AI Social Media Marketing & Content Engine

> **2027 Graduate Hiring Assessment | Option 2: Social Media Marketing & Content Engine**  
> Candidate: Growth Engineer Assessment Submission  
> Verified Direct Spend: **₹0.00** | Execution Runtime: **0.39 minutes** | Self-Check: **7 of 7 MET**

---

## 1. Project Purpose

The **IncuBrix AI Social Media Marketing & Content Engine** (`ai-socialmedia-content-engine`) is a production-grade, local-first system that transforms one long-form editorial input (podcast transcript, video recording, webinar, or product demo) into **30 platform-native, brand-governed, ready-to-publish social media assets** across YouTube Shorts, Instagram, and LinkedIn.

Designed specifically for expert creators, video podcasters, and small content operations teams in the US, UK, CA, AU, and Singapore, the engine operates 100% locally on standard consumer PC hardware with **zero required external cloud APIs, zero subscriptions, and absolute ₹0 direct cost**.

---

## 2. One Clear Run Command

To render the complete 30-asset campaign, execute quality audits, run deduplication tests, benchmark performance, and populate the official Excel workbook, run:

```bash
python engine/run.py
```

### What This Single Command Executes:
1. **Normal Run:** Extracts 10 editorial lessons from `engine/source.md`, plans 30 platform-tailored assets, renders 10 vertical 9:16 short videos (`A001`–`A010`), 10 five-slide carousels (`A011`–`A020`), and 10 graphics (`A021`–`A030`).
2. **Quality Gate:** Audits all 30 assets and a reproducible 20-sample random cohort against a deterministic 10-point checklist (**100.0% pass rate**).
3. **Repeat Run (Deduplication):** Validates composite SHA256 fingerprinting by pruning 30/30 duplicate items without wasted compute.
4. **Refresh Run (New Input):** Ingests `engine/refresh.md` and generates 12 new assets into a staging directory without overwriting approved campaign items.
5. **Failure & Recovery:** Injects a malformed input, catches the syntax defect, engages deterministic error recovery, and outputs 10 verified recovery assets.
6. **Benchmark Telemetry:** Records exact execution runtime (0.39 min vs. 30 min ceiling) and cost (₹0.00) in `submission/engine/benchmark_reports/runtime_cost_benchmark.json`.
7. **Official Workbook Generation:** Populates `submission/workbook/completed_submission_workbook.xlsx` with verified evidence, preserving all green calculated formulas, dropdown validations, and cell bindings.

---

## 3. Interactive Web Dashboard (Optional UI)

To explore the engine visually, start the local server:

```bash
python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000
```

Then open your browser to **[http://localhost:8000](http://localhost:8000)** (or `/dashboard`).  
The dashboard provides visual navigation across all 16 application modules:
- **Module 1: Dashboard:** Campaign KPIs, ready counts, format breakdown.
- **Module 2 & 3: Brand Workspace & DNA:** Voice rules, verified vs forbidden claims.
- **Module 4: Product & Market Research:** 5 product observations, 3 opportunities, competitor audits.
- **Module 5: Strategy Builder:** Creator personas, content pillars, conversion funnel.
- **Module 6 & 7: Ingestion & Planner:** Transcript parsing, brief approval/rejection.
- **Module 8 & 9: Static Creative Generator:** Pillow/SVG multi-slide carousels & graphics.
- **Module 10: Short-Video Generator:** FFmpeg 9:16 vertical motion graphics with kinetic subtitles.
- **Module 11 & 12: Quality Gate & Asset Library:** Inspection of rendered media and source files.
- **Module 13: 30-Day Calendar:** Interactive slots and one-click `calendar.csv` export.
- **Module 14: Audience Test:** Empirical analysis of the 22-person creator preference test.
- **Module 15: Run History:** Telemetry, duplicate decisions, and error recovery logs.
- **Module 16: Submission Center:** One-click bundle validation and live review tracer.

Interactive OpenAPI documentation is available at **[http://localhost:8000/docs](http://localhost:8000/docs)**.

---

## 4. Live Review Execution (45-Minute Defense Toolkit)

Per assessment guidelines, reviewers evaluate candidates by tracing 5 random assets back to source evidence and running on new input:

### A. Trace 5 Random Assets to Original Evidence:
```bash
python engine/live_review_tracer.py
```
This inspects 5 reproducible pseudo-random assets (e.g., `A001`, `A003`, `A004`, `A015`, `A030`), verifies that final media files and editable sources exist on disk, checks exact file byte sizes, prints verbatim source quotes from `engine/source.md`, and confirms UTM parameters and quality checks.

### B. Run on Any New Custom Input:
```bash
python engine/cli.py --run refresh
```

---

## 5. Prerequisites & Exact Installation

### System Requirements:
- **Operating System:** Windows 10/11, macOS, or Linux (64-bit AMD64/ARM64)
- **Python:** Python 3.10 to 3.14
- **Media Encoder:** FFmpeg (must be available on PATH or system executable)
- **Hardware:** Standard CPU / consumer GPU (tested on NVIDIA GTX 1650 with 4GB VRAM)

### Installation (under 60 seconds):
```bash
# 1. Clone repository
git clone https://github.com/NISHANTH-KONCHADA/ai-social-media-content-engine.git
cd ai-social-media-content-engine

# 2. Install Python dependencies
pip install fastapi uvicorn pydantic pydantic-settings sqlalchemy pillow openpyxl psutil pytest requests
```

*Note on Zero Cost:* No API keys or paid third-party accounts are required. A sample `.env.example` is provided for optional host/port configuration.

---

## 6. Deliverable Directory Structure

The complete assessment output is deterministic and organized in `submission/`:

```
submission/
├── workbook/
│   └── completed_submission_workbook.xlsx   # Preserved openpyxl workbook (7/7 MET)
├── research/
│   ├── product_observations.csv             # 5 verified product findings
│   ├── opportunities.csv                    # 3 high-impact creator opportunities
│   ├── competitor_audit.csv                 # IncuBrix + 5 competitors audited
│   ├── social_account_audit.csv             # IncuBrix public LinkedIn snapshot
│   └── evidence_index.md                    # Research audit trail and source links
├── strategy/
│   ├── strategy.md                          # Full positioning, funnel, and targets
│   ├── personas.md                          # 3 target creator profiles
│   ├── brand_voice.md                       # Approved vs. forbidden claims
│   └── platform_strategy.md                 # YouTube Shorts, Instagram, LinkedIn
├── content/
│   ├── calendar.csv                         # 23-column CSV matching workbook
│   └── assets/
│       ├── A001/ ... A010/                  # 10 vertical MP4 videos + source JSONs
│       ├── A011/ ... A020/                  # 10 5-slide carousels (PNG + SVG)
│       ├── A021/ ... A030/                  # 10 high-impact graphics (PNG + SVG)
│       └── refresh/                         # 12 fresh assets from new input
├── audience_test/
│   ├── test_plan.md                         # Double-blind A/B testing methodology
│   ├── survey_questions.md                  # Standardized 6-question instrument
│   ├── anonymized_responses.csv             # 22 verified creator responses
│   └── results.md                           # Statistical analysis (72.7% win, p=0.043)
├── launch_kit/
│   ├── 30_day_launch_plan.md                # Turnkey week-by-week operating plan
│   ├── daily_workflow.md                    # 45 min/day routine & Friday review
│   ├── risks.md                             # Risk matrix and mitigations
│   └── targets.md                           # 45k impressions, 2.8% ER, ₹0 budget
├── demos/
│   ├── product_walkthrough_script.md        # Script for video 5(a) (<=5m)
│   └── technical_demo_script.md             # Script for video 5(b) (<=8m)
├── evidence/
│   ├── screenshots/                         # Snapshot directory
│   └── source_links.md                      # Audit links & open-source licenses
└── engine/
    ├── run_logs/                            # normal, repeat, refresh, recovery logs
    ├── benchmark_reports/                   # runtime_cost_benchmark.json
    └── quality_audit/                       # audit_report.json (100% pass)
```

---

## 7. Automated Test Suite

To run the complete automated test suite (API endpoints, database persistence, workbook formulas, and asset integrity):

```bash
python -m pytest tests/
```
All 7 tests execute and pass in under 2 seconds.

---

## 8. Compliance & Ethical Disclosures

- **Direct Spend:** Verified at **₹0.00**. No paid software, cloud GPUs, or subscriptions were used.
- **Data Integrity:** Zero follower counts, post metrics, survey respondents, or product capabilities were fabricated.
- **Privacy & Permissions:** No unauthorized posting to company accounts was performed. DPDP and GDPR principles were strictly upheld with anonymized test records.
- **Licensing:** All fonts (Liberation Sans) and tools (FFmpeg, Pillow, Python) are open-source with commercial-friendly redistribution licenses.
