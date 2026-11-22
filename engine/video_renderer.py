import os
import json
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from typing import Dict, Any, List, Optional, Tuple

from engine.audio import synthesize_scene_voiceovers, concat_audio

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

def _truncate_at_word(text: str, max_chars: int) -> str:
    """Truncate on a word boundary with an ellipsis so copy never ends mid-word."""
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars].rsplit(" ", 1)[0].rstrip(" ,.;:-")
    return cut + "..."

def _draw_badge(draw: ImageDraw.ImageDraw, xy: Tuple[int, int], label: str,
                font: ImageFont.FreeTypeFont, fill: str, pad_x: int = 25, pad_y: int = 14):
    """Draw a label badge sized to its text (no overflow)."""
    x, y = xy
    bbox = draw.textbbox((0, 0), label, font=font)
    w = bbox[2] - bbox[0] + 2 * pad_x
    h = bbox[3] - bbox[1] + 2 * pad_y
    draw.rounded_rectangle([(x, y), (x + w, y + h)], radius=12, fill=fill)
    draw.text((x + pad_x, y + pad_y - 4), label, fill="#FFFFFF", font=font)
    return w, h

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
    draw.text((90, 102), f"{brand_name.upper()} - CREATOR WORKFLOW", fill="#06B6D4", font=font_badge)

    if scene_type == "hook":
        # Opening Hook Card (First 2-3 seconds)
        _draw_badge(draw, (60, 220), "HOOK IN FIRST 2 SECONDS", font_badge, "#E11D48")

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
        _draw_badge(draw, (60, 220), "THE 3-STEP SYSTEM", font_badge, "#4F46E5")

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
        _draw_badge(draw, (60, 220), "TACTICAL IMPLEMENTATION", font_badge, "#059669")

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
        draw.text((180, 875), "GET REPURPOSING TEMPLATE ->", fill="#FFFFFF", font=font_action)
        draw.text((120, 1020), "Visit: incubrix.com/workflow", fill="#38BDF8", font=font_footer)

    # Global Footer (left/right zones kept separate to avoid overlap)
    draw.text((70, 1840), "IncuBrix Growth Engine", fill="#64748B", font=font_footer)
    draw.text((880, 1840), "incubrix.com", fill="#06B6D4", font=font_footer)

    img.save(output_path, "PNG", quality=95)

def render_short_video(
    asset_id: str,
    lesson: Dict[str, Any],
    output_dir: Path,
    hook_text: Optional[str] = None,
    cta_text: str = "Get the full zero-cost repurposing workflow at incubrix.com/workflow"
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    frames_dir = output_dir / "temp_frames"
    frames_dir.mkdir(parents=True, exist_ok=True)

    display_hook = hook_text or lesson["hook"]

    # Narration script per scene (what the voiceover actually says)
    narration = [
        display_hook,
        f"{lesson['title']}. {_truncate_at_word(lesson['core_body'], 160)}",
        _truncate_at_word(lesson["tactical_action"], 180),
        "Get the full zero cost repurposing workflow at incubrix dot com."
    ]

    # Synthesize per-scene voiceover clips (Edge-TTS, procedural fallback)
    audio_dir = output_dir / "temp_audio"
    clips, clip_durations, audio_method = synthesize_scene_voiceovers(narration, audio_dir)

    # Scene duration = narration length + breathing room, min 3s
    scene_durations = [max(3.0, d + 0.6) for d in clip_durations]

    # Render 4 Scene Keyframes
    f1 = frames_dir / "scene_1_hook.png"
    f2 = frames_dir / "scene_2_lesson.png"
    f3 = frames_dir / "scene_3_action.png"
    f4 = frames_dir / "scene_4_cta.png"

    render_scene_frame("hook", display_hook, _truncate_at_word(lesson["core_body"], 220), 0.25, f1)
    render_scene_frame("lesson", lesson["title"], _truncate_at_word(lesson["core_body"], 320), 0.50, f2)
    render_scene_frame("action", lesson["title"], lesson["tactical_action"], 0.75, f3)
    render_scene_frame("cta", lesson["title"], "Get the full open-source engine", 1.00, f4)

    # Concatenate narration into one audio track with a short gap between scenes
    audio_track = output_dir / "temp_audio" / "track.wav"
    total_audio = concat_audio(clips, 0.35, audio_track)
    total_video = sum(scene_durations)
    duration = max(total_audio, total_video)

    # Save editable source JSON (records the true, measured values)
    source_json_path = output_dir / "source.json"
    source_data = {
        "asset_id": asset_id,
        "format": "Short video (9:16)",
        "resolution": "1080x1920",
        "target_duration_sec": round(duration, 2),
        "scenes": [
            {"scene": 1, "duration": round(scene_durations[0], 2), "type": "hook", "text": display_hook},
            {"scene": 2, "duration": round(scene_durations[1], 2), "type": "lesson", "text": lesson["title"]},
            {"scene": 3, "duration": round(scene_durations[2], 2), "type": "action", "text": lesson["tactical_action"]},
            {"scene": 4, "duration": round(scene_durations[3], 2), "type": "cta", "text": "incubrix.com/workflow"}
        ],
        "audio": f"Narrated voiceover via {audio_method} (44.1kHz AAC); procedural fallback when offline",
        "audio_method": audio_method,
        "rights": "100% original / CC0 licensed"
    }
    with open(source_json_path, "w", encoding="utf-8") as f:
        json.dump(source_data, f, indent=2)

    final_mp4 = output_dir / "final_video.mp4"

    # Stitch scenes with per-scene durations; mux narration track
    cmd = ["ffmpeg", "-y"]
    for frame, dur in zip([f1, f2, f3, f4], scene_durations):
        cmd += ["-loop", "1", "-t", f"{dur:.2f}", "-i", str(frame)]
    cmd += ["-i", str(audio_track),
            "-filter_complex", "[0:v][1:v][2:v][3:v]concat=n=4:v=1:a=0[v]",
            "-map", "[v]", "-map", "4:a",
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-shortest",
            str(final_mp4)]

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"FFmpeg render failed for {asset_id}: {res.stderr[:400]}")

    # Clean up temp artifacts to conserve disk
    for f in [f1, f2, f3, f4]:
        try:
            f.unlink()
        except Exception:
            pass
    for f in audio_dir.glob("*"):
        try:
            f.unlink()
        except Exception:
            pass
    for d in (frames_dir, audio_dir):
        try:
            d.rmdir()
        except Exception:
            pass

    return final_mp4
