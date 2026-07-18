from core.scanner import MusicScanner
from models.song import Song


class MusicLibrary:
    def __init__(self):
        self._scanner = MusicScanner()
        self.songs: list[Song] = []

    def load(self, folder: str) -> list[Song]:
        self.songs = self._scanner.scan(folder)
        return self.songs

    def count(self) -> int:
        return len(self.songs)

    def selected_count(self) -> int:
        return sum(song.selected for song in self.songs)

    def clear_selection(self):
        for song in self.songs:
            song.selected = False

    def select_all(self):
        for song in self.songs:
            song.selected = True
