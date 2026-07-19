from models.song import Song
from models.recommendation_result import RecommendationResult


class RecommendationEngine:

    RULES = {
        "official video": 25,
        "video oficial": 25,
        "remix": 10,
        "visualizer": -10,
        "audio": -15,
        "villancico": -30,
    }

    def analyze(self, song: Song) -> RecommendationResult:

        score = 100
        reasons = []

        filename = song.filename.lower()

        for keyword, points in self.RULES.items():

            if keyword in filename:

                score += points

                sign = "+" if points > 0 else ""

                reasons.append(f"{sign}{points}  {keyword}")

        return RecommendationResult(
            score=score,
            recommended=score >= 100,
            reasons=reasons
        )

    def recommend(self, songs):

        return [
            song
            for song in songs
            if self.analyze(song).recommended
        ]