from core.scanner import MusicScanner
from models.song import Song
from services.recommendation_engine import RecommendationEngine
from pathlib import Path


class MusicLibrary:
    def __init__(self):
        self._scanner = MusicScanner()
        self._recommendation = RecommendationEngine()
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
    def selected_songs(self) -> list[Song]:
        return [song for song in self.songs if song.selected]
    
    def unselected_songs(self) -> list[Song]:
        return [song for song in self.songs if not song.selected]
    
    def total_size(self) -> int:
        return sum(song.size for song in self.songs)

    def selected_size(self) -> int:
        return sum(song.size for song in self.selected_songs())
    
    def search(self, text: str):

        text = text.lower().strip()

        if not text:
            return self.songs

        return [

            song

            for song in self.songs

            if text in song.filename.lower()

        ]
    def load(self, folder: str) -> list[Song]:

        self.songs = self._scanner.scan(folder)

        for song in self.songs:
            song.analysis = self._recommendation.analyze(song)

        return self.songs
    
    def select_recommended(self):

        self.clear_selection()

        for song in self.songs:

         if song.analysis.recommended:
            song.selected = True
    
    def delete_selected(self):

        deleted = 0

        for song in self.selected_songs():

            try:

                Path(song.path).unlink()

                deleted += 1

            except Exception as e:

                print(e)

        return deleted