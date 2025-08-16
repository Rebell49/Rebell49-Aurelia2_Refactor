
from __future__ import annotations
import zipfile
from pathlib import Path
from .config import SETTINGS

class ArchiveManager:
    """Exportiert/Importiert Benutzerdaten als ZIP."""
    def __init__(self, data_dir: Path | None = None) -> None:
        self.data_dir = data_dir or SETTINGS.data_dir

    def export_zip(self, zip_path: Path) -> Path:
        zip_path = Path(zip_path)
        zip_path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
            for p in self.data_dir.rglob('*'):
                if p.is_file():
                    zf.write(p, arcname=p.relative_to(self.data_dir))
        return zip_path

    def import_zip(self, zip_path: Path) -> None:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(self.data_dir)
