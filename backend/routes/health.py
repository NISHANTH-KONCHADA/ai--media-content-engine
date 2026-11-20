import shutil
import psutil
from fastapi import APIRouter
import subprocess
from backend.config import settings

router = APIRouter(prefix="/api/health", tags=["Health"])

@router.get("")
def get_health():
    ram = psutil.virtual_memory()
    disk = shutil.disk_usage(settings.SUBMISSION_DIR)
    
    # Check GPU
    gpu_info = "Not Detected"
    try:
        smi = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total,memory.free", "--format=csv,noheader"], capture_output=True, text=True, check=True)
        gpu_info = smi.stdout.strip()
    except Exception:
        pass

    # Check FFmpeg
    ffmpeg_ok = False
    try:
        f_ver = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
        ffmpeg_ok = f_ver.returncode == 0
    except Exception:
        pass

    return {
        "status": "HEALTHY",
        "timestamp": psutil.boot_time(),
        "gpu": gpu_info,
        "ram_total_gb": round(ram.total / (1024**3), 2),
        "ram_available_gb": round(ram.available / (1024**3), 2),
        "disk_free_gb": round(disk.free / (1024**3), 2),
        "ffmpeg_available": ffmpeg_ok,
        "deterministic_engine": True,
        "direct_cost": "₹0.00"
    }
