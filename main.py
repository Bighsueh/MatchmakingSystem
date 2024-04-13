from match import MatchStrategy
from match import DistanceBasedStrategy
from match import HabitBasedStrategy
from match import Reversed
from Individual import Individual
from Coord import Coord
from typing import List

candidates: List[Individual] = []

coord: Coord = Coord(x = 0, y = 0)
individual: Individual = Individual(
    id = 1,
    male = 'MALE',
    age = 18,
    intro = 'self introduction',
    habits = ['singing'],
    coord = coord,
)

strategy = Reversed(DistanceBasedStrategy())
resultList: List[Individual] = strategy.match(candidates= candidates, individual = individual)

bestMatch:Individual = resultList[0]