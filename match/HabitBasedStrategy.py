from typing import List
from Individual import Individual
from match.MatchStrategy import MatchStrategy

class HabitBasedStrategy(MatchStrategy):
    def calIntersection(self, list1:List[str], list2:List[str]):
        return set(list1) & set(list2)
        
    def match(self, candidates: List[Individual], individual: Individual) -> List[Individual]:
        return sorted(candidates, key= lambda i : self.calIntersection(i.habits, individual.habits), reverse=True)
    
