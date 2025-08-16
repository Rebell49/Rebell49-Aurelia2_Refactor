
from __future__ import annotations
import os
from dataclasses import dataclass
from pathlib import Path

APP_NAME = "aurelia2"

def _app_data_dir() -> Path:
    if os.name == "nt":
        base = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
    elif os.name == "posix":
        if "darwin" in os.sys.platform:
            base = Path.home() / "Library" / "Application Support"
        else:
            base = Path.home() / ".local" / "share"
    else:
        base = Path.home()
    return base / APP_NAME

@dataclass
class Settings:
    data_dir: Path = _app_data_dir()
    log_file: Path = _app_data_dir() / "aurelia.log"
    thoughts_file: Path = _app_data_dir() / "thoughts.ndjson"

SETTINGS = Settings()
SETTINGS.data_dir.mkdir(parents=True, exist_ok=True)
