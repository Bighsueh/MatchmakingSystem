from __future__ import annotations
from typing import List
from Coord import Coord

class Individual():
    def __init__(self) -> None:
        self.id: int
        self.male: str
        self.age: int
        self.intro: str
        self.habits: List[str]
        self.coord: Coord
        pass