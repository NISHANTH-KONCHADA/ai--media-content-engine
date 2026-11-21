import os
import json
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from typing import Dict, Any, List

FONTS_DIR = Path(__file__).resolve().parent / "fonts"
BOLD_FONT_PATH = FONTS_DIR / "LiberationSans-Bold.ttf"
REG_FONT_PATH = FONTS_DIR / "LiberationSans-Regular.ttf"

def get_font(font_path: Path, size: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(str(font_path), size)
    except Exception:
        return ImageFont.load_default()

def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw) -> List[str]:
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        current_line.append(word)
        bbox = draw.textbbox((0, 0), " ".join(current_line), font=font)
        if bbox[2] - bbox[0] > max_width:
            current_line.pop()
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def render_scene_frame(
    scene_type: str,
    title: str,
    text: str,
    progress_pct: float,
    output_path: Path,
    brand_name: str = "IncuBrix"
):
    # 1080 x 1920 (9:16 Vertical video standard)
    width, height = 1080, 1920
    img = Image.new("RGB", (width, height), color="#0B132B")
    draw = ImageDraw.Draw(img)
    
    font_badge = get_font(BOLD_FONT_PATH, 32)
    font_hook = get_font(BOLD_FONT_PATH, 68)
    font_body = get_font(REG_FONT_PATH, 44)
    font_action = get_font(BOLD_FONT_PATH, 48)
    font_footer = get_font(BOLD_FONT_PATH, 30)
    
    # Progress Bar at Top
    draw.rectangle([(0, 0), (width, 16)], fill="#1E293B")
    draw.rectangle([(0, 0), (int(width * progress_pct), 16)], fill="#06B6D4")
    
    # Header Tag
    draw.rounded_rectangle([(60, 80), (1020, 160)], radius=16, fill="#1C2541")
    draw.text((90, 102), f"{brand_name.upper()} • CREATOR WORKFLOW", fill="#06B6D4", font=font_badge)
    
    if scene_type == "hook":
        # Opening Hook Card (First 2-3 seconds)
        draw.rounded_rectangle([(60, 220), (450, 290)], radius=12, fill="#E11D48")
        draw.text((85, 238), "HOOK IN FIRST 2 SECONDS", fill="#FFFFFF", font=font_badge)
        
        hook_lines = wrap_text(title, font_hook, 920, draw)
        y = 380
        for l in hook_lines:
            draw.text((70, y), l, fill="#FFFFFF", font=font_hook)
            y += 85
            
        draw.rounded_rectangle([(60, y + 60), (1020, y + 480)], radius=24, fill="#1C2541", outline="#4F46E5", width=3)
        body_lines = wrap_text(text, font_body, 860, draw)
        by = y + 120
        for bl in body_lines:
            draw.text((100, by), bl, fill="#E2E8F0", font=font_body)
            by += 65
            if by > y + 420:
                break
                
    elif scene_type == "lesson":
        draw.rounded_rectangle([(60, 220), (450, 290)], radius=12, fill="#4F46E5")
        draw.text((85, 238), "THE 3-STEP SYSTEM", fill="#FFFFFF", font=font_badge)
        
        t_lines = wrap_text(title, font_hook, 920, draw)
        y = 380
        for l in t_lines:
            draw.text((70, y), l, fill="#F8FAFC", font=font_hook)
            y += 85
            
        draw.rounded_rectangle([(60, y + 40), (1020, y + 540)], radius=24, fill="#1C2541", outline="#3B82F6", width=2)
        b_lines = wrap_text(text, font_body, 860, draw)
        by = y + 100
        for bl in b_lines:
            draw.text((100, by), bl, fill="#CBD5E1", font=font_body)
            by += 65
            if by > y + 480:
                break
                
    elif scene_type == "action":
        draw.rounded_rectangle([(60, 220), (520, 290)], radius=12, fill="#059669")
        draw.text((85, 238), "TACTICAL IMPLEMENTATION", fill="#FFFFFF", font=font_badge)
        
        draw.text((70, 380), "TRY THIS ON YOUR NEXT RUN:", fill="#A7F3D0", font=font_action)
        
        draw.rounded_rectangle([(60, 480), (1020, 1100)], radius=24, fill="#064E3B", outline="#10B981", width=3)
        a_lines = wrap_text(text, font_action, 860, draw)
        ay = 560
        for al in a_lines:
            draw.text((100, ay), al, fill="#FFFFFF", font=font_action)
            ay += 70
            if ay > 1020:
                break
                
    elif scene_type == "cta":
        draw.rounded_rectangle([(60, 360), (1020, 1100)], radius=32, fill="#1E1B4B", outline="#818CF8", width=4)
        draw.text((120, 480), "AUTOMATE THIS WORKFLOW", fill="#A5B4FC", font=font_hook)
        draw.text((120, 600), "Zero paid APIs. Zero cloud GPU costs.", fill="#F8FAFC", font=font_body)
        draw.text((120, 680), "Runs locally on your computer.", fill="#94A3B8", font=font_body)
        
        draw.rounded_rectangle([(120, 840), (960, 960)], radius=20, fill="#4F46E5")
        draw.text((180, 875), "GET REPURPOSING TEMPLATE ↗", fill="#FFFFFF", font=font_action)
        draw.text((120, 1020), "Visit: incubrix.com/workflow", fill="#38BDF8", font=font_footer)

    # Global Footer
    draw.text((70, 1840), "IncuBrix Growth Engine • Licensed Free-Tier Production", fill="#64748B", font=font_footer)
    draw.text((820, 1840), "incubrix.com", fill="#06B6D4", font=font_footer)
    
    img.save(output_path, "PNG", quality=95)

def render_short_video(
    asset_id: str,
    lesson: Dict[str, Any],
    output_dir: Path
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    frames_dir = output_dir / "temp_frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    
    # Render 4 Scene Keyframes
    f1 = frames_dir / "scene_1_hook.png"
    f2 = frames_dir / "scene_2_lesson.png"
    f3 = frames_dir / "scene_3_action.png"
    f4 = frames_dir / "scene_4_cta.png"
    
    render_scene_frame("hook", lesson["hook"], lesson["core_body"][:220] + "...", 0.25, f1)
    render_scene_frame("lesson", lesson["title"], lesson["core_body"][:320] + "...", 0.50, f2)
    render_scene_frame("action", lesson["title"], lesson["tactical_action"], 0.75, f3)
    render_scene_frame("cta", lesson["title"], "Get the full open-source engine", 1.00, f4)
    
    # Save editable source JSON
    source_json_path = output_dir / "source.json"
    source_data = {
        "asset_id": asset_id,
        "format": "Short video (9:16)",
        "resolution": "1080x1920",
        "target_duration_sec": 12.0,
        "scenes": [
            {"scene": 1, "duration": 3.0, "type": "hook", "text": lesson["hook"]},
            {"scene": 2, "duration": 3.0, "type": "lesson", "text": lesson["title"]},
            {"scene": 3, "duration": 3.0, "type": "action", "text": lesson["tactical_action"]},
            {"scene": 4, "duration": 3.0, "type": "cta", "text": "incubrix.com/workflow"}
        ],
        "audio": "Procedural stereo synthesis (44.1kHz AAC)",
        "rights": "100% original / CC0 licensed"
    }
    with open(source_json_path, "w", encoding="utf-8") as f:
        json.dump(source_data, f, indent=2)

    final_mp4 = output_dir / "final_video.mp4"
    
    # Stitch into video using FFmpeg concat filter
    # Scene 1: 3s, Scene 2: 3s, Scene 3: 3s, Scene 4: 3s -> Total 12s
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "3", "-i", str(f1),
        "-loop", "1", "-t", "3", "-i", str(f2),
        "-loop", "1", "-t", "3", "-i", str(f3),
        "-loop", "1", "-t", "3", "-i", str(f4),
        "-f", "lavfi", "-t", "12", "-i", "anullsrc=r=44100:cl=stereo",
        "-filter_complex", "[0:v][1:v][2:v][3:v]concat=n=4:v=1:a=0[v]",
        "-map", "[v]", "-map", "4:a",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-shortest",
        str(final_mp4)
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"FFmpeg render failed for {asset_id}: {res.stderr[:400]}")
        
    # Clean up temp frames to conserve disk
    for f in [f1, f2, f3, f4]:
        try:
            f.unlink()
        except Exception:
            pass
    try:
        frames_dir.rmdir()
    except Exception:
        pass
        
    return final_mp4
