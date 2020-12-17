from typing import List

from Engine.Dices import Dice


class Damage:
    def __init__(self, dice_count: int = 1, dice_type: int = 6, modifier: int = 0):
        self.modifier: int = modifier
        self.dices: List[Dice] = []
        for x in range(1, dice_count):
            self.dices.append(Dice(dice_type))
