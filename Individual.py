from __future__ import annotations
from typing import List
from Coord import Coord

class Individual():
    def __init__(self, id:int, gender:str, age:int, intro:str, habit:List[str], coord:Coord) -> None:
        self.id: int
        self.gender: str
        self.age: int
        self.intro: str
        self.habits: List[str]
        self.coord: Coord
        pass