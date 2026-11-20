import re
from pathlib import Path
from typing import List, Dict, Any

def extract_lessons_from_markdown(file_path: Path) -> List[Dict[str, Any]]:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Split by H2 headers (## Lesson Title)
    sections = re.split(r'\n(?=##\s+)', text)
    lessons = []

    for section in sections:
        section = section.strip()
        if not section.startswith("##"):
            continue
            
        lines = section.split("\n")
        title = lines[0].replace("##", "").strip()
        body_lines = [l.strip() for l in lines[1:] if l.strip()]
        
        # Extract hook, core explanation, and tactical action
        hook = body_lines[0] if len(body_lines) > 0 else title
        core_body = " ".join(body_lines)
        
        # Look for practical tip / takeaway
        tactical_action = ""
        for line in body_lines:
            if line.lower().startswith("try this") or line.lower().startswith("example") or "try this:" in line.lower():
                tactical_action = line
                break
        if not tactical_action and len(body_lines) > 1:
            tactical_action = body_lines[-1]

        lessons.append({
            "title": title,
            "hook": hook,
            "core_body": core_body,
            "tactical_action": tactical_action,
            "raw_text": section
        })

    return lessons
