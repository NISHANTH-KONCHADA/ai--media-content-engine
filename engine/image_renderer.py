import os
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

def truncate_at_word(text: str, max_chars: int) -> str:
    """Truncate on a word boundary with an ellipsis so copy never ends mid-word."""
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars].rsplit(" ", 1)[0].rstrip(" ,.;:-")
    return cut + "..."

def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw) -> List[str]:
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        current_line.append(word)
        bbox = draw.textbbox((0, 0), " ".join(current_line), font=font)
        w = bbox[2] - bbox[0]
        if w > max_width:
            current_line.pop()
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
            
    if current_line:
        lines.append(" ".join(current_line))
        
    return lines

def render_carousel_slide(
    slide_num: int,
    total_slides: int,
    title: str,
    body: str,
    output_path: Path,
    pillar: str,
    brand_name: str = "IncuBrix"
):
    # Dimensions: 1080 x 1350 (4:5 vertical carousel format)
    width, height = 1080, 1350
    img = Image.new("RGB", (width, height), color="#0F172A") # Dark slate
    draw = ImageDraw.Draw(img)
    
    font_badge = get_font(BOLD_FONT_PATH, 28)
    font_title = get_font(BOLD_FONT_PATH, 54)
    font_body = get_font(REG_FONT_PATH, 36)
    font_footer = get_font(BOLD_FONT_PATH, 24)
    
    # Top brand bar & pillar tag
    draw.rectangle([(60, 60), (1020, 120)], fill="#1E293B")
    draw.text((90, 75), f"{brand_name.upper()} • {pillar.upper()}", fill="#06B6D4", font=font_badge)
    draw.text((900, 75), f"{slide_num}/{total_slides}", fill="#94A3B8", font=font_badge)
    
    # Decorative accent line
    draw.rectangle([(60, 125), (1020, 130)], fill="#4F46E5")
    
    # Slide Title
    title_lines = wrap_text(title, font_title, 900, draw)
    y_pos = 220
    for line in title_lines:
        draw.text((70, y_pos), line, fill="#FFFFFF", font=font_title)
        y_pos += 70
        
    y_pos += 40
    
    # Content Card Background
    draw.rounded_rectangle([(60, y_pos), (1020, y_pos + 600)], radius=24, fill="#1E293B", outline="#334155", width=2)
    
    # Body Text
    body_lines = wrap_text(body, font_body, 860, draw)
    text_y = y_pos + 60
    for line in body_lines:
        draw.text((100, text_y), line, fill="#E2E8F0", font=font_body)
        text_y += 56
        if text_y > y_pos + 520:
            break
            
    # Bottom Callout / Footer
    draw.rectangle([(60, 1220), (1020, 1290)], fill="#0F172A")
    draw.text((70, 1240), f"Swipe for step {slide_num + 1} ->" if slide_num < total_slides else "Follow for more creator workflows ->", fill="#10B981", font=font_footer)
    draw.text((800, 1240), "incubrix.com", fill="#64748B", font=font_footer)
    
    img.save(output_path, "PNG", quality=95)

def render_graphic(
    title: str,
    quote: str,
    action: str,
    output_path: Path,
    pillar: str,
    brand_name: str = "IncuBrix"
):
    # Dimensions: 1080 x 1080 (1:1 Square format)
    width, height = 1080, 1080
    img = Image.new("RGB", (width, height), color="#0F172A")
    draw = ImageDraw.Draw(img)
    
    font_badge = get_font(BOLD_FONT_PATH, 28)
    font_title = get_font(BOLD_FONT_PATH, 50)
    font_quote = get_font(REG_FONT_PATH, 36)
    font_action = get_font(BOLD_FONT_PATH, 32)
    font_footer = get_font(BOLD_FONT_PATH, 24)
    
    # Header tag
    draw.rectangle([(60, 60), (1020, 120)], fill="#1E293B")
    draw.text((90, 75), f"{brand_name.upper()} • {pillar.upper()}", fill="#06B6D4", font=font_badge)
    
    # Headline
    title_lines = wrap_text(title, font_title, 900, draw)
    y_pos = 180
    for line in title_lines:
        draw.text((70, y_pos), line, fill="#FFFFFF", font=font_title)
        y_pos += 65
        
    y_pos += 40
    
    # Quote card
    draw.rounded_rectangle([(60, y_pos), (1020, y_pos + 420)], radius=20, fill="#1E293B", outline="#4F46E5", width=2)
    quote_lines = wrap_text(f"\"{truncate_at_word(quote, 155)}\"", font_quote, 860, draw)
    q_y = y_pos + 50
    for line in quote_lines:
        draw.text((100, q_y), line, fill="#E2E8F0", font=font_quote)
        q_y += 52
        if q_y > y_pos + 360:
            break
            
    # Tactical Action Box
    y_pos += 460
    draw.rounded_rectangle([(60, y_pos), (1020, y_pos + 160)], radius=16, fill="#047857", outline="#10B981", width=2)
    draw.text((90, y_pos + 25), "KEY TAKEAWAY / ACTION:", fill="#A7F3D0", font=font_footer)
    action_lines = wrap_text(action, font_action, 880, draw)
    act_y = y_pos + 65
    for line in action_lines:
        draw.text((90, act_y), line, fill="#FFFFFF", font=font_action)
        act_y += 45
        if act_y > y_pos + 140:
            break
            
    # Footer
    draw.text((70, 1010), "IncuBrix Growth Engine • Verified Creator Systems", fill="#64748B", font=font_footer)
    draw.text((860, 1010), "incubrix.com", fill="#06B6D4", font=font_footer)
    
    img.save(output_path, "PNG", quality=95)

def render_svg_source(title: str, text: str, output_path: Path):
    svg_content = f"""<svg width="1080" height="1350" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#0F172A"/>
  <rect x="60" y="60" width="960" height="60" fill="#1E293B" rx="8"/>
  <text x="90" y="100" fill="#06B6D4" font-family="Liberation Sans, sans-serif" font-weight="bold" font-size="28">INCUBRIX EDITABLE SOURCE</text>
  <text x="70" y="240" fill="#FFFFFF" font-family="Liberation Sans, sans-serif" font-weight="bold" font-size="52">{title}</text>
  <rect x="60" y="320" width="960" height="600" fill="#1E293B" stroke="#334155" stroke-width="2" rx="24"/>
  <text x="100" y="420" fill="#E2E8F0" font-family="Liberation Sans, sans-serif" font-size="36">{text[:200]}</text>
  <text x="70" y="1250" fill="#10B981" font-family="Liberation Sans, sans-serif" font-weight="bold" font-size="24">IncuBrix Content Engine • Licensed Output</text>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
