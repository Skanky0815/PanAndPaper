from typing import List

from Engine import Costs
from Engine.Dices import Dice


class Weapon:

    def __init__(self, name: str, type: str, dices: List[Dice], modifier: int, costs: Costs):
        self.name: str = name
        self.type: str = type
        self.dices: List[Dice] = dices
        self.modifier: int = modifier
        self.costs: Costs = costs
