
from __future__ import annotations
import datetime as _dt
import json, re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Dict, Any
from .config import SETTINGS

_word_re = re.compile(r"\b\w{3,}\b", re.UNICODE)

@dataclass
class Thought:
    ts: str
    text: str
    tokens: list[str]

class ThoughtStream:
    """Append-only NDJSON-Speicher für Gedanken."""
    def __init__(self, path: Path | None = None) -> None:
        self.path = path or SETTINGS.thoughts_file
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _tokenize(self, text: str) -> List[str]:
        return _word_re.findall(text.lower())

    def add(self, text: str) -> Thought:
        t = Thought(ts=_dt.datetime.utcnow().isoformat(), text=text.strip(), tokens=self._tokenize(text))
        line = json.dumps(t.__dict__, ensure_ascii=False)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")
        return t

    def iter(self) -> Iterable[Thought]:
        if not self.path.exists():
            return
        with self.path.open("r", encoding="utf-8") as f:
            for line in f:
                try:
                    obj = json.loads(line)
                    yield Thought(**obj)
                except Exception:
                    continue

    def stats(self) -> Dict[str, Any]:
        count = 0
        token_count = 0
        for th in self.iter() or []:
            count += 1
            token_count += len(th.tokens)
        return {"entries": count, "tokens": token_count, "avg_tokens": (token_count / count) if count else 0.0}
