from typing import List
from Individual import Individual
from match.MatchStrategy import MatchStrategy

class Reversed(MatchStrategy):
    def __init__(self, matchmakingStrategy: MatchStrategy) -> None:
        self.matchmakingStrategy: MatchStrategy = matchmakingStrategy
           
    def match(self, candidates: List[Individual], individual: Individual) -> List[Individual]:
        result:List[Individual] = self.matchmakingStrategy.match(candidates, individual)
        return result[::-1]