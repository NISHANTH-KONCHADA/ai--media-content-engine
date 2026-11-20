# Technical Stack & Hardware Specification

**Assessment Project:** AI Social Media Marketing and Content Engine  
**Hardware Environment:** Windows 11 (AMD64), NVIDIA GeForce GTX 1650 (4GB VRAM)  
**Cost Constraint:** Absolute ₹0 direct cost (no paid APIs, no subscriptions, no cloud GPUs)

---

## 1. Actual Detected Hardware & Environment Audit

Before designing or selecting models, a hardware detection probe was executed directly on the host machine:

| Component | Detected Specification | Constraint Analysis & Adaptation |
|---|---|---|
| **GPU Model** | NVIDIA GeForce GTX 1650 | 4096 MiB (4.0 GB) VRAM. *Critical finding:* While assessment prompt specified "NVIDIA GPU with at least 8GB VRAM", the actual physical GPU is 4GB VRAM. Large 8B+ LLMs or heavy SDXL/Flux diffusion pipelines cannot run without Out-Of-Memory (OOM) failures or crippling memory paging. |
| **CUDA / Driver** | CUDA 13.3 / Driver 610.91 | Compute Capability 7.5. Compatible with local FP16/INT4 inference, PyTorch CUDA builds, and FFmpeg NVENC acceleration. |
| **System RAM** | 15.65 GB Total (0.73 GB Available at audit) | High memory contention. Models must be lightweight (e.g., quantized 1.5B–3B models or CPU-efficient deterministic extraction) to prevent host memory thrashing. |
| **Disk Storage** | 378.11 GB Total (10.46 GB Free) | Limited free storage. Massive multi-gigabyte model weight downloads would risk filling the system drive. High efficiency and modular storage are mandatory. |
| **Python** | Python 3.14.5 (64-bit) | Modern Python runtime with native asynchronous I/O and broad library support. |
| **Node.js / npm** | Node v24.15.0 / npm 11.x | Enterprise-grade modern JavaScript runtime for React + Vite dashboard. |
| **Video Processing** | FFmpeg 9.0.2 (Gyan full build) | Installed on system PATH with complete codec support (x264, aac, filter_complex, drawtext, ass, nvenc). |
| **Container Engine** | Docker Desktop 29.9.3 | Installed; however, non-Docker native Windows workflow is provided as primary for zero-friction evaluation. |

---

## 2. Zero-Cost Technology Selection

| Tier / Function | Selected Tool / Library | Version | License | Cost | Justification & Role |
|---|---|---|---|---|---|
| **Backend API** | FastAPI + Uvicorn | 0.147.0 / 0.54.0 | MIT | ₹0 | Asynchronous, high-throughput REST API powering all 16 application modules with auto-generated OpenAPI documentation. |
| **Data Persistence** | SQLite + SQLAlchemy 2.0 | 2.0.49 | MIT / Public Domain | ₹0 | Zero-configuration, zero-overhead relational database. Complete schema portability without requiring a separate server daemon. |
| **Data Validation** | Pydantic v2 | 2.13.4 | MIT | ₹0 | Strict type enforcement, schema validation, and bidirectional serialization matching workbook headers. |
| **Frontend UI** | React 18 + TypeScript + Vite + Tailwind CSS | React 18.3, Vite 6 | MIT | ₹0 | Ultra-fast responsive single-page web dashboard providing interactive control over all 16 modules. |
| **Text Processing & NLP** | Hybrid NLP Engine (Local Ollama Adapter + Fast Deterministic Rule-Based Extractor) | Custom Python 3.14 | MIT | ₹0 | Zero-failure architecture: supports local Ollama models (Qwen2.5-1.5B/3B, Llama-3.2-1B/3B) when running, with an instant, deterministic NLP regex/structural fallback that works 100% offline with zero dependencies and 0s latency. |
| **Static Creative Engine** | Pillow (PIL) + SVG Vector Templating | 13.0.0 | HPND | ₹0 | Generates pixel-perfect 1080x1350 carousels and 1080x1080 graphics with typography, multi-slide narrative cards, and brand logos. Diffusion models notoriously hallucinate spelling and text layout; Pillow ensures 100% accurate copy and claims. |
| **Video Production Engine** | FFmpeg (Native CLI & Python Wrapper) | 9.0.2 | GPL v3 | ₹0 | Motion-graphics video assembler rendering 9:16 vertical MP4s (1080x1920) with animated text hooks, kinetic captions, progress bars, audio synthesis, and visible end-cards. |
| **Audio Synthesis** | Edge-TTS / Local Synthesis Fallback | 7.3.1 | MIT | ₹0 | Natural creator voiceover audio generation with zero paid API keys, plus deterministic tone/beat audio fallbacks. |
| **Workbook Integration** | OpenPyXL | 3.1.5 | MIT | ₹0 | Reads and writes `.xlsx` files while strictly preserving XML schemas, workbook formulas, dropdown validation rules, and formatting. |
| **Testing Suite** | Pytest + Pytest-Asyncio | 9.1.1 / 1.5.0 | MIT | ₹0 | Comprehensive automated test coverage spanning unit tests, API tests, deduplication tests, refresh tests, and formula checks. |

---

## 3. License Compliance & Rights Safety

All assets, fonts, and dependencies strictly adhere to open-source and commercial-friendly licensing:
1. **Fonts:** Liberation Sans / DejaVu Sans (OFL - Open Font License / Free Redistribution).
2. **Icons & Graphics:** Custom SVG geometric brand elements and algorithmic layouts (Public Domain / MIT).
3. **Audio:** Pure procedural harmonic tone mixing and CC0/Open speech synthesis with zero copyrighted musical compositions.
4. **Third-Party Services:** No paid stock video, paid music, or paid APIs utilized. Direct expenditure is verified at exactly **₹0.00**.
