# Technical Demo Video Script (Duration: ~6 Minutes 45 Seconds)

**Assessment Requirement:** Item 5(b) — Technical Demo, unedited, up to 8 minutes: one normal run, a refresh on new input, and recovery from one simple failure.  
**Video Objective:** Demonstrate the technical architecture, execution speed, error resilience, and deduplication capabilities of the code.

---

## Live Demonstration Checklist & Step-by-Step Script

### 00:00 - 01:15 | Segment 1: Environment & Architecture Overview
- **Visual:** Terminal window open at project root (`c:\Users\konch\OneDrive\Desktop\2`).
- **Terminal Command:**
  ```bash
  python -c "import torch, psutil; print('RAM:', psutil.virtual_memory().total / (1024**3))"
  nvidia-smi
  ffmpeg -version | Select-Object -First 1
  ```
- **Spoken Audio:**
  > "Welcome to the technical demonstration of the IncuBrix Content Engine.
  >
  > First, let's verify our environment. We are running on Windows 11 with an NVIDIA GeForce GTX 1650 with 4 gigabytes of VRAM. Because consumer GPUs cannot load massive 8B+ parameter models without crashing or paging into system RAM, we engineered a high-throughput hybrid architecture: an optional Ollama adapter for lightweight quantized models, backed by an instant deterministic NLP extraction engine, Pillow typography compositing, and native FFmpeg 9.0 video assembly.
  >
  > The entire engine operates 100% locally with zero paid API keys, zero cloud subscriptions, and absolute ₹0 direct cost."

### 01:15 - 03:00 | Segment 2: One Normal Run from README
- **Visual:** Terminal executing the main run command.
- **Terminal Command:**
  ```bash
  python engine/run.py
  ```
- **Spoken Audio:**
  > "Now, we execute the single primary run command from our README: `python engine/run.py`.
  >
  > Watch the output:
  > In less than one second, it extracts 10 core editorial lessons from our source workshop markdown.
  > It synthesizes platform-native hooks, captions, and UTM links for 30 distinct assets across YouTube Shorts, Instagram, and LinkedIn.
  >
  > Next, the media renderers fire:
  > FFmpeg renders 10 vertical 9:16 short videos with 2-second visual hooks, scene progression, subtitles, and clean audio tracks.
  > Pillow renders 10 five-slide carousels—that's 50 individual high-contrast slides—along with vector SVG editable sources.
  > And Pillow renders 10 high-impact graphics.
  >
  > It exports `calendar.csv` with the exact 23 workbook columns, runs our deterministic 10-point Quality Gate with a 100% pass rate, and populates the official submission workbook while strictly preserving all Excel formulas.
  >
  > Total execution time: just 0.39 minutes—well under the 30-minute assessment threshold!"

### 03:00 - 04:30 | Segment 3: Repeat Run (Deduplication Check)
- **Visual:** Terminal executing repeat run.
- **Terminal Command:**
  ```bash
  python engine/cli.py --run repeat
  ```
- **Spoken Audio:**
  > "Now, let's test deduplication resilience. If a user accidentally re-runs the engine on the same input, what happens?
  >
  > We execute `python engine/cli.py --run repeat`.
  >
  > Notice the result:
  > The engine computes SHA256 composite content fingerprints across platform, format, pillar, and normalized hook.
  > It immediately identifies all 30 candidate assets as duplicates and prunes them from generation.
  > Zero duplicate assets are written to disk, preserving the database and preventing wasted compute. Execution finishes in less than 0.05 seconds."

### 04:30 - 05:30 | Segment 4: Refresh on New Input
- **Visual:** Terminal executing refresh run.
- **Terminal Command:**
  ```bash
  python engine/cli.py --run refresh
  ```
- **Spoken Audio:**
  > "Next, we demonstrate refresh capability when new input arrives.
  >
  > We run `python engine/cli.py --run refresh` against `engine/refresh.md`, our second original workshop.
  >
  > The engine parses the new input, extracts four fresh lessons, and renders 12 new platform-tailored assets into a designated refresh staging directory.
  >
  > Crucially, it does this without overwriting or clobbering any previously approved assets or existing schedule dates in the main campaign."

### 05:30 - 06:15 | Segment 5: Recovery from Simple Failure
- **Visual:** Terminal executing failure recovery run.
- **Terminal Command:**
  ```bash
  python engine/cli.py --run failure_recovery
  ```
- **Spoken Audio:**
  > "Now, we demonstrate error handling and graceful recovery.
  >
  > We run `python engine/cli.py --run failure_recovery` with a simulated corrupted, malformed input header lacking lesson content.
  >
  > Watch the engine catch the defect: it logs the structural validation failure, rejects the corrupt input, and automatically triggers the deterministic fallback engine to generate 10 verified recovery assets safely.
  >
  > No unhandled exceptions, no crash dumps, and clean execution logs saved to `run_logs/failure_recovery.log`."

### 06:15 - 06:45 | Segment 6: Conclusion & Live Review Readiness
- **Visual:** Display `submission/engine/benchmark_reports/runtime_cost_benchmark.json` and `submission/engine/quality_audit/audit_report.json`.
- **Spoken Audio:**
  > "In summary: the engine meets every single technical requirement:
  > Zero API cost, sub-1-minute execution time, 100% rights compliance, and full live review traceability from asset to source evidence. Thank you."
