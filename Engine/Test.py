from typing import List

from Engine.Dices import Dice


class Test:

    def attribute(self, dice: Dice, value: int, modifier: int = 0):
        dice_value: int = dice.roll()
        text: str = f"Du hast mit einem {dice.name} eine {dice_value} gewürfelt gegen {value}"

        if 0 < modifier:
            text += f" modifiziert um {modifier}"
        print(text+".")

        return Result(dice_value, (value + modifier))

    def damage(self, dices: List[Dice], modifier: int = 0) -> int:
        dice_values: int = 0
        dice_text: str = ""

        idx: str = 1
        for dice in dices:
            dice_value: int = dice.roll()
            if idx > 1:
                dice_text += " und mit dem "
            dice_text += f"{dice.name} eine {dice_value}"
            dice_values += dice_value
            idx += 1

        modifier_text: str = ""
        if modifier > 0:
            modifier_text += f" dazu kommten noch + {modifier}"

        damage: int = dice_values + modifier
        print(f"Du hast mit dem {dice_text}{modifier_text} erwürfelt. Damit machst du insgesamt {damage} Schaden.")

        return damage


class Result:

    def __init__(self, dice_result: int, value: int):
        self.dice_result: int = dice_result
        self.__value: int = value

    def is_critical_success(self) -> bool:
        return 1 == self.dice_result

    def is_critical_failure(self) -> bool:
        return 20 == self.dice_result

    def is_success(self) -> bool:
        return self.is_critical_success() or (self.dice_result <= self.__value)

