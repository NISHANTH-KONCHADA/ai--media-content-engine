import os
from pathlib import Path
from typing import Dict, Any, List
import random

def audit_asset(asset: Dict[str, Any], submission_root: Path) -> Dict[str, Any]:
    checks = {}
    
    # 1. Product Claims Check
    forbidden = ["100x viral guarantee", "fully autonomous without review", "unverified feature"]
    text_corpus = (asset.get("hook", "") + " " + asset.get("caption", "")).lower()
    has_forbidden = any(f in text_corpus for f in forbidden)
    checks["verified_claims"] = not has_forbidden

    # 2. Platform Format & Length Check
    fmt = asset.get("format", "")
    plat = asset.get("platform", "")
    valid_format = fmt in ["Short video", "Carousel", "Graphic", "Text post", "Thread", "Long video"]
    valid_platform = plat in ["LinkedIn", "Instagram", "YouTube Shorts", "TikTok", "X", "Threads", "Facebook", "Reddit"]
    checks["platform_format_valid"] = valid_format and valid_platform

    # 3. Hook Quality Check
    hook = asset.get("hook", "").strip()
    checks["strong_hook"] = len(hook) >= 15 and not hook.lower().startswith("in this post")

    # 4. Caption & CTA Check
    caption = asset.get("caption", "").strip()
    cta = asset.get("cta", "").strip()
    checks["caption_and_cta"] = len(caption) >= 40 and len(cta) >= 5

    # 5. Tracking Link (UTM) Check
    utm = asset.get("utm_link", "").strip()
    checks["utm_link_valid"] = utm.startswith("http") and "utm_source=" in utm and "utm_campaign=" in utm

    # 6. Final File Existence & Integrity Check
    final_url = asset.get("final_file_url", "").strip()
    final_path = submission_root / final_url.lstrip("/")
    checks["final_file_exists"] = final_path.exists() and final_path.stat().st_size > 500

    # 7. Editable Source File Existence Check
    source_url = asset.get("source_file_url", "").strip()
    source_path = submission_root / source_url.lstrip("/")
    checks["source_file_exists"] = source_path.exists() and source_path.stat().st_size > 50

    # 8. Rights & Consent Safety Check
    rights = asset.get("rights_checked", "")
    checks["rights_safe"] = rights == "Yes"

    # 9. Schedule Date Present
    sched = asset.get("scheduled_date", "").strip()
    checks["scheduled_date_present"] = len(sched) >= 10

    # 10. AI Label Requirement Assessed
    ai_label = asset.get("ai_label_needed", "")
    checks["ai_label_assessed"] = ai_label in ["Yes", "No"]

    # All pass check
    passed_all = all(checks.values())
    
    return {
        "asset_id": asset.get("asset_id"),
        "checks": checks,
        "passed_count": sum(1 for v in checks.values() if v),
        "total_count": len(checks),
        "passed_all": passed_all,
        "verdict": "PASS" if passed_all else "FAIL"
    }

def run_campaign_audit(assets: List[Dict[str, Any]], submission_root: Path, sample_size: int = 20) -> Dict[str, Any]:
    full_results = [audit_asset(a, submission_root) for a in assets]
    total_assets = len(full_results)
    total_passed = sum(1 for r in full_results if r["passed_all"])
    full_pass_rate = round((total_passed / total_assets * 100), 1) if total_assets > 0 else 0.0

    # Deterministic reproducible pseudo-random sample of 20
    # Seed fixed to 2027 (matching hiring year) for reproducibility
    rng = random.Random(2027)
    sample_indices = rng.sample(range(total_assets), min(sample_size, total_assets))
    sample_results = [full_results[i] for i in sorted(sample_indices)]
    sample_passed = sum(1 for r in sample_results if r["passed_all"])
    sample_pass_rate = round((sample_passed / len(sample_results) * 100), 1) if sample_results else 0.0

    return {
        "total_campaign_assets": total_assets,
        "campaign_passed_all": total_passed,
        "campaign_pass_rate_pct": full_pass_rate,
        "sample_size": len(sample_results),
        "sample_passed_all": sample_passed,
        "sample_pass_rate_pct": sample_pass_rate,
        "sample_threshold_met": sample_pass_rate >= 85.0, # Assessment threshold is >=85%
        "zero_rights_issues": all(r["checks"]["rights_safe"] for r in full_results),
        "sample_audits": sample_results,
        "full_audits": full_results
    }
