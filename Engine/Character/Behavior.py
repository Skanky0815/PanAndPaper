from typing import Dict

from Engine.Damage import Damage


class Behavior:
    def __init__(self, min: int, max: int, text: str, damage_dice: Dict = None):
        self.__min: int = min
        self.__max: int = max
        self.text: str = text
        self.damage: Damage = Damage(**damage_dice) if damage_dice else None

    def in_range(self, worth_comparing: int) -> bool:
        return self.__min <= worth_comparing & worth_comparing <= self.__max

    def __str__(self) -> str:
        return f"{self.__min}-{self.__max}: \t{self.text}"