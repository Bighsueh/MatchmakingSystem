from Individual import Individual
from match.MatchStrategy import MatchStrategy
from Coord import Coord
from typing import List
import math

class DistanceBasedStrategy(MatchStrategy):
    def calDistance(self, p1: Coord, p2:Coord) -> float:
        return math.sqrt((p1.y - p2.y) ** 2 + (p1.x - p2.x) ** 2)
    
    def match(self,candidates: List[Individual], individual: Individual) -> List[Individual]:
        return sorted(candidates, key=lambda i: self.calDistance(individual.coord, i.coord))
    