from dataclasses import dataclass
from pathlib import Path


@dataclass
class Song:
    name: str
    path: Path
    size: int

    selected: bool = False

    artist: str = "Desconocido"
    album: str = "Desconocido"
    duration: float = 0.0

    @property
    def size_mb(self):
        return round(self.size / (1024 * 1024), 2)