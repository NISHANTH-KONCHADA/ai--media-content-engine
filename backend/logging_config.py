import logging
import sys
from pathlib import Path
from backend.config import settings

def setup_logger(name: str = "engine") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        # Console handler
        c_handler = logging.StreamHandler(sys.stdout)
        c_format = logging.Formatter('%(asctime)s - [%(levelname)s] - %(name)s - %(message)s')
        c_handler.setFormatter(c_format)
        logger.addHandler(c_handler)
        
        # File handler
        log_file = settings.LOGS_DIR / "app.log"
        f_handler = logging.FileHandler(log_file, encoding="utf-8")
        f_handler.setFormatter(c_format)
        logger.addHandler(f_handler)
        
    return logger

logger = setup_logger()
