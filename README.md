# Aurelia² – Autonomes Verständnisnetz (Refactor)

Eine saubere, modularisierte Neuinterpretation des ursprünglichen Projekts **Aurelia**.
Ziele:
- klare Modulgrenzen, 
- Typhinweise & Docstrings,
- robuste Fehlerbehandlung und Logging,
- CLI **und** optionale Kivy-UI (falls installiert),
- Export/Archiv-Funktionen,
- einfache Tests.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
# CLI starten
python -m aurelia2 --help
python -m aurelia2 think "Neugier ist ein leiser Motor."
python -m aurelia2 status
python -m aurelia2 export out.zip
# (Optional) Kivy-UI
python -m aurelia2 ui
```

## Module

- `aurelia2/resource_manager.py` – System- und Pfadverwaltung, Logging.
- `aurelia2/thought_stream.py` – Persistenter Gedankenstrom, einfache NLP-Spielereien.
- `aurelia2/archive_manager.py` – Export/Import von Sitzungen als ZIP.
- `aurelia2/ui.py` – Kivy-UI (minimal, optional).
- `aurelia2/__main__.py` – CLI/Dispatcher.
- `aurelia2/config.py` – Konfiguration (pfad- und betriebssystemfreundlich).
- `tests/` – Minimaltests.

## Hinweise

- Kivy ist **optional**; ohne Kivy bleibt die CLI voll funktionsfähig.
- Daten werden unter `~/.local/share/aurelia2` (Linux), `~/Library/Application Support/aurelia2` (macOS) bzw. `%APPDATA%\aurelia2` (Windows) gespeichert.
