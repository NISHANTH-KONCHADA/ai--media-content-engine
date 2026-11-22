"""Audio synthesis for short videos.

Primary path: Edge-TTS (free, no API key, neural voices, requires network).
Fallback: deterministic procedural tone bed synthesized locally via pydub
(works 100% offline, zero cost).
"""
import asyncio
import subprocess
from pathlib import Path
from typing import List, Tuple

EDGE_TTS_VOICE = "en-US-ChristopherNeural"

def probe_duration(path: Path) -> float:
    """Return media duration in seconds via ffprobe."""
    res = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True
    )
    try:
        return float(res.stdout.strip())
    except (ValueError, TypeError):
        return 0.0

async def _edge_tts_render(text: str, out_path: Path) -> bool:
    try:
        import edge_tts
        comm = edge_tts.Communicate(text, EDGE_TTS_VOICE)
        await asyncio.wait_for(comm.save(str(out_path)), timeout=20)
        return out_path.exists() and out_path.stat().st_size > 500
    except Exception:
        return False

def synthesize_scene_voiceovers(
    texts: List[str], work_dir: Path
) -> Tuple[List[Path], List[float], str]:
    """Render one narration clip per scene.

    Returns (clip_paths, durations, method) where method is
    'edge-tts' when at least one real voice clip was synthesized,
    or 'procedural' when fully offline fallback was used.
    """
    work_dir.mkdir(parents=True, exist_ok=True)
    clips: List[Path] = []
    durations: List[float] = []
    any_tts = False

    for i, text in enumerate(texts):
        clip = work_dir / f"voice_{i}.mp3"
        ok = False
        if text.strip():
            try:
                ok = asyncio.run(_edge_tts_render(text, clip))
            except Exception:
                ok = False
        if ok:
            any_tts = True
        else:
            # Deterministic offline fallback: soft two-tone cue, ~2.5s
            clip = _procedural_tone_clip(work_dir / f"tone_{i}.wav", 2.5)
        clips.append(clip)
        durations.append(probe_duration(clip) or 2.5)

    return clips, durations, ("edge-tts" if any_tts else "procedural")

def _procedural_tone_clip(out_path: Path, seconds: float) -> Path:
    """Synthesize a gentle procedural stereo tone bed (CC0, self-generated)."""
    try:
        from pydub.generators import Sine
        base = Sine(196).to_audio_segment(duration=int(seconds * 1000)) - 30
        fifth = Sine(294).to_audio_segment(duration=int(seconds * 1000)) - 34
        bed = base.overlay(fifth).fade_in(250).fade_out(400)
        bed = bed.set_channels(2).set_frame_rate(44100)
        bed.export(str(out_path), format="wav")
        return out_path
    except Exception:
        # Last resort: silence via ffmpeg anullsrc (still a real audio track)
        subprocess.run(
            ["ffmpeg", "-y", "-f", "lavfi", "-t", str(seconds),
             "-i", "anullsrc=r=44100:cl=stereo", str(out_path)],
            capture_output=True
        )
        return out_path

def concat_audio(clips: List[Path], gap_sec: float, out_path: Path) -> float:
    """Concatenate per-scene clips with a short gap into one AAC-ready WAV."""
    from pydub import AudioSegment
    gap = AudioSegment.silent(duration=int(gap_sec * 1000))
    combined = AudioSegment.empty()
    for c in clips:
        ext = c.suffix.lstrip(".")
        seg = AudioSegment.from_file(str(c), format=ext)
        combined += seg + gap
    combined = combined.set_channels(2).set_frame_rate(44100)
    combined.export(str(out_path), format="wav")
    return len(combined) / 1000.0
