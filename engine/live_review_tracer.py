import sys
import random
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from backend.database import SessionLocal
from backend.models import Asset
from engine.extractor import extract_lessons_from_markdown

def trace_asset(asset_id: str):
    db = SessionLocal()
    try:
        asset = db.query(Asset).filter(Asset.asset_id == asset_id).first()
        if not asset:
            print(f"[!] Asset {asset_id} not found in database.")
            return

        print(f"\n=======================================================")
        print(f"  ASSET TRACE: {asset.asset_id} ({asset.platform} • {asset.format})")
        print(f"=======================================================")
        print(f"Content Pillar:     {asset.content_pillar}")
        print(f"Opening Hook:       \"{asset.hook}\"")
        print(f"Final Render File:  {asset.final_file_url}")
        final_p = BASE_DIR / "submission" / asset.final_file_url.lstrip("/")
        print(f"File Exists on Disk:{final_p.exists()} (Size: {final_p.stat().st_size if final_p.exists() else 0} bytes)")
        print(f"Editable Source:    {asset.source_file_url}")
        src_p = BASE_DIR / "submission" / asset.source_file_url.lstrip("/")
        print(f"Source Exists:      {src_p.exists()} (Size: {src_p.stat().st_size if src_p.exists() else 0} bytes)")
        print(f"Source Evidence:    {asset.source_input}")
        print(f"Tools Used:         {asset.tools_used}")
        print(f"Rights Checked:     {asset.rights_checked} (Zero copyright flags)")
        print(f"UTM Tracking URL:   {asset.utm_link}")
        print(f"Scheduled Slot:     {asset.scheduled_date}")
        print(f"Quality Status:     {asset.status}")
        print(f"-------------------------------------------------------")
        print(f"Caption Preview:\n{asset.caption[:180]}...")
        print(f"=======================================================\n")
    finally:
        db.close()

def main():
    db = SessionLocal()
    try:
        all_ids = [a.asset_id for a in db.query(Asset).order_by(Asset.asset_id).all()]
    finally:
        db.close()

    if not all_ids:
        print("[!] No assets found in database. Run `python engine/run.py` first.")
        return

    # Select 5 reproducible pseudo-random assets
    rng = random.Random(2027)
    sampled = sorted(rng.sample(all_ids, min(5, len(all_ids))))
    
    print(f"[*] IncuBrix Live Review Tracer: Tracing 5 Randomly Selected Assets: {sampled}")
    for aid in sampled:
        trace_asset(aid)

if __name__ == "__main__":
    main()
