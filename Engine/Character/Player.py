from typing import List

from Engine.Character.Character import Character
from Engine.Character.CobatValue import MeleeCombatValue, RangeCombatValue, MagicCombatValue
from Engine.Weapon import Weapon


class Player(Character):

    def __init__(
            self,
            name: str,
            race: str,
            attention: int,
            charisma: int,
            agility: int,
            secrecy: int,
            precision: int,
            acumen: int,
            strength: int,
            willpower: int
    ):
        super(Player, self).__init__(health=40, name=name)
        self.race: str = race

        self.melee_combat: MeleeCombatValue = MeleeCombatValue(15)
        self.range_combat: RangeCombatValue = RangeCombatValue(10)
        self.magic_combat: MagicCombatValue = MagicCombatValue(base_value=0)

        self.weapons: List[Weapon] = []

        self.attention: int = attention  # aufmerksamkeit
        self.charisma: int = charisma  # ausstrahlung
        self.agility: int = agility  # gewandheit
        self.secrecy: int = secrecy  # heimlichkeit
        self.precision: int = precision  # präzision
        self.acumen: int = acumen  # scharfsinn
        self.strength: int = strength  # stärke
        self.willpower: int = willpower  # willenskraft

    def __str__(self) -> str:

        weapons: str = ""
        for weapon in self.weapons:
            dices: str = ""
            for dice in weapon.dices:
                dices += f"{dice.name}"
            weapons += f"\tName: {weapon.name}, Schaden {dices} + {weapon.modifier}\n"

        return "\n" \
            f"Name: {self.name}\n" \
            f"Race: {self.race}\n" \
            f"Leben: {self.health}/40\n" \
            "---------------------------------------\n" \
            f"Aufmerksamkeit:\t{self.attention}\tAusstrahlung:\t{self.charisma}\n" \
            f"Gewandheit:\t\t{self.agility}\tHeimlichkeit:\t{self.secrecy}\n" \
            f"Präzision:\t\t{self.precision}\tScharfsinn:\t\t{self.acumen}\n" \
            f"Stärke:\t\t\t{self.strength}\tWillenskraft:\t{self.willpower}\n" \
            "---------------------------------------\n" \
            f"Waffen:\n{weapons}" \
            "---------------------------------------\n"
