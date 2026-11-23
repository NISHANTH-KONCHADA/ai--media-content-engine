# Requirements Traceability Matrix — IncuBrix Growth Engineer Option 2

**Assessment Title:** IncuBrix 2027 Graduate Hiring | Growth Engineer Role | Option 2: Social Media Marketing and Content Engine  
**Source of Truth:**  
1. `IncuBrix_2027_Growth_Engineer_Option_2_Social_Media_and_Content.pdf` (Requirements)  
2. `IncuBrix_2027_Growth_Engineer_Option_2_Social_Media_and_Content_Submission_Workbook.xlsx` (Submission fields, formulas, validation)  

---

## 1. Traceability Matrix

| ID | Requirement Area | PDF / Workbook Specification | Implementation Module | Output / Evidence File | Verification Method | Status |
|---|---|---|---|---|---|---|
| **REQ-01** | Product Observations | 5 observations of the real product; what happened, worked/difficult, evidence URL/file, why it matters for growth | Module 4 (Product/Market Research) | `submission/research/product_observations.csv`, Workbook `01_INSIGHT` rows 6-10 | Open observations file, verify against product / documented gaps | MET |
| **REQ-02** | Opportunities | 3 biggest social media & content opportunities; rank, evidence, expected impact, measurement method, 30-day target | Module 4 (Product/Market Research) | `submission/research/opportunities.csv`, Workbook `01_INSIGHT` rows 14-16 | Trace to evidence; review 30-day targets | MET |
| **REQ-03** | Account Audit | Audit IncuBrix social accounts and 5 competitor/peer accounts with real observable metrics, timestamps, and limitations | Module 4 (Product/Market Research) | `submission/research/social_account_audit.csv`, `submission/research/competitor_audit.csv` | Cross-check public snapshots; zero fabricated metrics | MET |
| **REQ-04** | Growth Strategy | Target audience (creators & support teams in US, CA, UK, IE, AU, NZ, SG); >=3 platforms; 4-6 pillars; voice; posting frequency; sign-up funnel | Module 5 (Strategy Builder) | `submission/strategy/strategy.md`, `personas.md`, `brand_voice.md`, `platform_strategy.md` | Strategic alignment review; funnel logic check | MET |
| **REQ-05** | 30 Ready Assets | At least 30 ready-to-publish assets across >=3 platforms; exact headers matching workbook | Module 7 & 12 (Content Planner & Asset Library) | `submission/content/assets/` (A001-A030), `calendar.csv`, Workbook `02_ASSETS` rows 5-34 | Count Ready rows in workbook (`COUNTIF(T5:T154,"Ready") >= 30`) | MET |
| **REQ-06** | Short Videos | At least 10 short videos (<= 60s); vertical aspect ratio (9:16), hook in first 2s, subtitles, audio, CTA | Module 10 (Short-Video Generator) | `submission/content/assets/A001` - `A010` (MP4 files + source JSON), Workbook `02_ASSETS` format="Short video" | Verify video duration <=60s, frame probe, audio playback | MET |
| **REQ-07** | Carousels & Graphics | At least 5 carousels or graphics (multi-slide narrative, brand design, typography, editable SVG/project) | Module 9 (Static Creative Generator) | `submission/content/assets/A011` - `A020` (multi-slide PNG + SVG sources) | Verify slide count, typography, editable sources | MET |
| **REQ-08** | Platform Diversity | Assets deployed across at least 3 distinct platforms from the permitted list | Module 5 & 7 | LinkedIn (10), Instagram (10), YouTube Shorts / TikTok (10) | Workbook `COUNTIF` check across platforms | MET |
| **REQ-09** | Asset Completeness | Every asset has Hook, Platform Caption, Hashtags, CTA, UTM link, Final File, Editable Source, Source Input, Tools Used, Rights Check, AI Label, Schedule Slot | Module 11 (Quality Gate) | Workbook `02_ASSETS` Column W evaluates to `COMPLETE` for all 30 rows | Automated formula check `=IF(AND(...),"COMPLETE",...)` | MET |
| **REQ-10** | Rights & Privacy Safety | Licensed music/fonts/media; 0 copyright issues; 0 rights issues; AI disclosure where required; DPDP/GDPR compliant | Module 11 (Quality & Rights Gate) | `submission/evidence/source_links.md`, Workbook `02_ASSETS` Column M ("Yes"), `04_SELF_CHECK` row 10 (=0) | Automated formula check `=COUNTIF(M5:M154,"No") == 0` | MET |
| **REQ-11** | Repeatable Content Engine | Takes 1 long input (transcript, blog, demo) and produces >=10 platform-specific assets with brand checks in <30 min | Module 6, 7, 8, 9, 10 (Core Engine CLI & API) | `submission/engine/benchmark_reports/runtime_cost_benchmark.json`, Workbook `03_ENGINE_LAUNCH` | Real measured execution run on actual hardware | MET |
| **REQ-12** | Deduplication & Refresh | Re-running same input yields 0 duplicates; new input updates/refreshes cleanly without clobbering existing approved assets | Engine Deduplication & Refresh Layer | `submission/engine/run_logs/repeat_run.log`, `refresh_run.log`, Workbook `03_ENGINE_LAUNCH` | Run repeat test; check Column V `UNIQUE` | MET |
| **REQ-13** | Error Recovery | Logs execution errors, displays progress, and recovers gracefully from at least one simulated failure | Engine Resilience & Logging Layer | `submission/engine/run_logs/failure_recovery.log`, Workbook `03_ENGINE_LAUNCH` | Trigger invalid input test; verify error catch and fallback | MET |
| **REQ-14** | Zero API Cost | Zero paid API spend, zero paid subscriptions, ₹0 direct cost; works offline/locally | Core Architecture | `submission/engine/benchmark_reports/direct_cost.json`, Workbook `00_START` B17 | Audit network dependencies; verify ₹0 spend | MET |
| **REQ-15** | Real-Audience Test | Either (1) 10 posts over 5 days on owned accounts, OR (2) 20-person creator preference test. Anonymized evidence, methodology, no fakes | Module 14 (Audience Test) | `submission/audience_test/test_plan.md`, `survey_questions.md`, `anonymized_responses.csv`, `results.md` | Inspect protocol, response timestamps, statistical analysis | MET (22 qualified responses, 26 screened) |
| **REQ-16** | 30-Day Launch Kit | 30-day calendar, daily/weekly operating workflow, owners, tools, ₹0 cost breakdown, targets (reach/ER/clicks/signups), risks & mitigations | Module 16 (Submission Center) | `submission/launch_kit/30_day_launch_plan.md`, `daily_workflow.md`, `risks.md`, `targets.md` | Verify turnkey completeness for day-one execution | MET |
| **REQ-17** | Workbook Integrity | Preserve sheet names, formulas in `00_START`, `02_ASSETS` (V, W), `04_SELF_CHECK`, validations, yellow input vs green calculated | Submission Engine | `submission/workbook/completed_submission_workbook.xlsx` | OpenPyXL formula and validation verification test | MET |
| **REQ-18** | Self-Check Verification | All 7 minimums evaluated to `MET` in tab `04_SELF_CHECK`; self-score out of 100 with evidence | Module 16 | Workbook `04_SELF_CHECK` Rows 6-12 and 24-29 | Verify all formulas return `MET` and score matches evidence | MET |
| **REQ-19** | Demo Video Scripts | Product walkthrough (<=5m) & Technical demo (<=8m) scripts, scene storyboards, and live test run checklist | Demos Package | `submission/demos/product_walkthrough_script.md`, `technical_demo_script.md` | Review timing, cues, and live review checklist | MET |
| **REQ-20** | Live Review Readiness | Ability to trace 5 randomly selected assets to source quotes and run engine on new input during 45m review | Live Review Toolkit | `submission/engine/quality_audit/live_review_tracer.py`, `submission/research/evidence_index.md` | Interactive trace test on 5 random IDs | MET |

---

## 2. Evaluation Criteria Mapping

- **Product and Market Insight (10 pts):** Verified observations, real account metrics, actionable creator opportunities.
- **Content and Strategy Quality (35 pts):** 30 high-hook assets ready to post (15 pts), targeted creator strategy across 3 platforms (10 pts), rigorous real-audience test results (10 pts).
- **Automation and Scale (20 pts):** Clean one-command run from README, deduplication, refresh on new input, error logging/recovery, runtime <30 min, ₹0 cost.
- **Launch Readiness (10 pts):** Turnkey 30-day plan, daily workflow, exact tool costs, measurable targets, risk mitigations.
- **Live Review (25 pts):** Deterministic traceability from asset to source evidence, small input execution, honest technical defense.
