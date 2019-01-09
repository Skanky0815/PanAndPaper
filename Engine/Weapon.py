from typing import List

from Engine import Costs
from Engine.Dices import Dice


class Weapon:

    def __init__(self, name: str, dices: List[Dice], modifier: int, costs: Costs):
        self.name: str = name
        self.dices: List[Dice] = dices
        self.modifier: int = modifier
        self.costs: Costs = costs


class NpcWeapon:

    def __init__(self, name: str, damage: int):
        self.name: str = name
        self.damage: int = damage
