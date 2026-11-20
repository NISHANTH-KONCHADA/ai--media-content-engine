import os
from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = f"sqlite:///{BASE_DIR}/engine.db"
    SUBMISSION_DIR: Path = BASE_DIR / "submission"
    LOGS_DIR: Path = BASE_DIR / "submission" / "engine" / "run_logs"
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen2.5:1.5b"
    ENABLE_DETERMINISTIC_FALLBACK: bool = True
    ENABLE_GROQ_ADAPTER: bool = False
    GROQ_API_KEY: str = ""

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()

# Ensure critical directories exist
settings.SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)
settings.LOGS_DIR.mkdir(parents=True, exist_ok=True)
