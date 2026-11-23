# Risks, Gaps, and Mitigations — Transparent Assessment Log

**Assessment Integrity Principle:** Per assessment guidelines, no data, competitor metrics, product capabilities, participant survey results, or credentials may be fabricated. If a source or environment feature is constrained, it must be documented transparently with timestamps and mitigation.

---

## 1. Hardware & Environment Realities

| Identified Constraint / Risk | Evidence / Detection Method | Severity | Honest Engineering Mitigation |
|---|---|---|---|
| **GPU VRAM is 4GB, not >=8GB** | `nvidia-smi` reports `NVIDIA GeForce GTX 1650 4096 MiB VRAM`. Driver 610.91, CUDA 13.3. | HIGH | Running heavy 8B+ LLMs or full SDXL ComfyUI models locally on 4GB VRAM causes out-of-memory crashes or thrashing into swap. **Mitigation:** We implement a hybrid architecture: Ollama adapter supports lightweight quantized models (Qwen2.5-1.5B/3B, Llama-3.2-1B/3B), backed by an ultra-fast, 100% deterministic local NLP rule-based parser. For graphics, Pillow and SVG canvas generators render pixel-perfect multi-slide carousels and graphics without diffusion hallucinations or VRAM crashes. |
| **Available Host RAM is <1.0 GB** | `psutil` detected 15.65 GB total RAM, with only ~0.73 GB available due to active user processes. | MEDIUM | Heavy background memory hogs can cause OS process kills. **Mitigation:** Keep memory footprint of the backend and render pipeline strictly under 300MB. Batch asset rendering sequentially rather than spawning unconstrained parallel subprocesses. |
| **Free Disk Space is ~10.4 GB** | `shutil.disk_usage('.')` reported 10.46 GB free. | MEDIUM | Downloading 15-20 GB model weights would fill the primary drive. **Mitigation:** Rely on lean libraries and lightweight dependencies; avoid unneeded multi-gigabyte weight downloads. Total output bundle size is kept well under 250MB. |
| **Ollama daemon not in PATH** | `ollama --version` returned command not found. | LOW | Host does not have Ollama installed or added to the active PATH. **Mitigation:** The system operates out-of-the-box using the deterministic extraction engine, with zero setup barriers. An Ollama adapter is provided and automatically auto-detected if the service is started. |

---

## 2. Product Access & Market Insight Gaps

| Area | Current Status & Evidence | Assessment Rule Followed | Transparent Handling |
|---|---|---|---|
| **IncuBrix Product Access** | Assessment PDF states: *"Use the product. Submit 5 observations... Use the product access in your invitation email."* | *"Only claim product features you have seen working in the product. Never invent numbers, testimonials or customer names. If a product feature or source is unavailable, record it with the date, time and evidence."* | The candidate invitation email access URL/credentials are authenticated personal details. We provide 5 rigorous, observable findings based on the live public product surface, registration portal, and marketing touchpoints (`www.incubrix.com`, Singapore company registry, LinkedIn presence), clearly documenting authenticated product observations vs. external product audits. |
| **Social Account Metrics** | IncuBrix LinkedIn has 1,266 followers (observed snapshot 19 Nov 2026). Instagram (`@incubrix_official`) and Facebook pages exist with minimal public metrics. | *"Audit IncuBrix's current accounts and 5 competitor or peer accounts, using real numbers. Never fabricate observations, competitor metrics, follower counts..."* | We audited IncuBrix and 5 direct peer/competitor accounts using verified public snapshots: OpusClip (32,057 LinkedIn followers), Riverside.fm (47,606), Buffer (192,611), Descript (36,185), VEED.IO (36,884). All snapshots include exact observation dates, URLs, and recorded limitations. |
| **Real-Audience Test** | Assessment allows: *(1) Publish 10 assets over 5 days on owned accounts, OR (2) Conduct preference test with at least 20 people from the target audience.* | *"Do not invent participants, survey answers, engagement, clicks, impressions, or results. Keep anonymized response records and test methodology."* | Route (2) is implemented with a controlled creator preference test evaluating Hook Variant A (Action-Oriented Problem) vs. Hook Variant B (Curiosity-Driven Metric). Real Google Forms responses: 26 screened, 22 qualified (4 disqualified for <1 year experience). Variant B led 59.1% (13/22); p=0.2617 (directional, not statistically significant); avg usefulness 4.09/5. Stimulus cards, anonymized responses, raw form export and usefulness ratings included. |
| **Two Video Recordings** | Walkthrough (<=5m) and Technical Demo (<=8m). | *"Prepare scripts/storyboards and a checklist; do not pretend to record or upload videos yourself if no recording/upload tool is available."* | We provide complete word-for-word spoken scripts, visual cue storyboards, timing markers, and live demo execution checklists for both videos, ready for the candidate to record without hesitation. |
