from Engine.Dices import Dice
from Engine.TestResult import TestResult
from Engine.Weapon import Weapon


class Test:

    def attribute(self, dice: Dice, value: int, modifier: int = 0) -> TestResult:
        dice_value: int = dice.roll()
        text: str = f"Du hast mit einem {dice.name} eine {dice_value} gewürfelt gegen {value}"

        if 0 < modifier:
            text += f" modifiziert um {modifier}"
        print(text+".")

        return TestResult(dice_value, (value + modifier))

    def damage(self, weapon: Weapon) -> int:
        dice_values: int = 0
        dice_text: str = ""

        idx: int = 1
        for dice in weapon.dices:
            dice_value: int = dice.roll()
            if idx > 1:
                dice_text += " und mit dem "
            dice_text += f"{dice.name} eine {dice_value}"
            dice_values += dice_value
            idx += 1

        modifier_text: str = ""
        if weapon.modifier > 0:
            modifier_text += f" dazu kommten noch + {weapon.modifier}"

        damage: int = dice_values + weapon.modifier
        print(f"Du hast mit dem {dice_text}{modifier_text} erwürfelt. Damit machst du insgesamt {damage} Schaden.")

        return damage
