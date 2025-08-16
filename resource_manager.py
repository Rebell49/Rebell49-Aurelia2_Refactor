
from __future__ import annotations
import datetime as _dt
import psutil
from pathlib import Path
from .config import SETTINGS

class ResourceManager:
    """Kapselt Logging & Systemmetriken."""
    def __init__(self, log_path: Path | None = None) -> None:
        self.log_path = log_path or SETTINGS.log_file

    def snapshot(self) -> dict:
        vm = psutil.virtual_memory()
        return {
            "ts": _dt.datetime.utcnow().isoformat(),
            "cpu": psutil.cpu_percent(interval=0.1),
            "mem_total": vm.total,
            "mem_used": vm.used,
            "mem_percent": vm.percent,
        }

    def log(self, message: str, level: str = "INFO") -> None:
        rec = {"ts": _dt.datetime.utcnow().isoformat(), "level": level, "msg": message}
        line = f"{rec['ts']} [{level}] {message}\n"
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(line)
