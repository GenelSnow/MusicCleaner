from dataclasses import dataclass, field


@dataclass
class RecommendationResult:

    score: int
    recommended: bool
    reasons: list[str] = field(default_factory=list)