from dataclasses import dataclass
from pathlib import Path


@dataclass
class Song:

    name: str
    filename: str
    path: str
    folder: str
    extension: str
    size: int

    selected: bool = False

    # Metadatos (para futuras versiones)
    artist: str = ""
    album: str = ""
    duration: float = 0.0

    @property
    def size_mb(self):
        return self.size / 1024 / 1024

    @property
    def display_size(self):
        return f"{self.size_mb:.2f} MB"

    @property
    def stem(self):
        return Path(self.filename).stem