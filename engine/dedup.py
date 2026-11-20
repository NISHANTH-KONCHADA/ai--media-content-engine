import hashlib
import re
from typing import Set, Dict, Any

def normalize_text(text: str) -> str:
    # Lowercase, strip punctuation and extra whitespace
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return " ".join(text.split())

def compute_asset_fingerprint(platform: str, format_type: str, pillar: str, hook: str) -> str:
    norm_platform = normalize_text(platform)
    norm_format = normalize_text(format_type)
    norm_pillar = normalize_text(pillar)
    norm_hook = normalize_text(hook)
    
    raw = f"{norm_platform}:{norm_format}:{norm_pillar}:{norm_hook}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

class DeduplicationRegistry:
    def __init__(self):
        self.seen_fingerprints: Set[str] = set()

    def is_duplicate(self, fingerprint: str) -> bool:
        return fingerprint in self.seen_fingerprints

    def register(self, fingerprint: str) -> bool:
        if fingerprint in self.seen_fingerprints:
            return False
        self.seen_fingerprints.add(fingerprint)
        return True

    def count(self) -> int:
        return len(self.seen_fingerprints)
