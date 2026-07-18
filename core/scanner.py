from pathlib import Path

from models.song import Song


class MusicScanner:

    def __init__(self):
        self.songs: list[Song] = []

    def scan(self, folder) -> list[Song]:

        self.songs.clear()

        folder = Path(folder)

        if not folder.exists():
            return []

        for file in folder.rglob("*.mp3"):

            song = Song(
                name=file.name,
                path=file,
                size=file.stat().st_size
            )

            self.songs.append(song)

        self.songs.sort(key=lambda song: song.name.lower())

        return self.songs