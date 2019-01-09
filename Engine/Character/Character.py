import math
from typing import List

from Engine.Costs import Costs
from Engine.Weapon import Weapon


class BaseCharacter:

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
        self.name: str = name
        self.race: str = race

        self.attention: int = attention  # aufmerksamkeit
        self.charisma: int = charisma  # ausstrahlung
        self.agility: int = agility  # gewandheit
        self.secrecy: int = secrecy  # heimlichkeit
        self.precision: int = precision  # präzision
        self.acumen: int = acumen  # scharfsinn
        self.strength: int = strength  # stärke
        self.willpower: int = willpower  # willenskraft

        self.corruption: int = 0
        self.perma_corruption: int = 0

        self.money: Costs = Costs()

        self.toughness = 0
        self.perma_toughness = strength if strength > 10 else 10  # Zähigkeit
        self.pain_barrier = math.ceil(strength / 2)  # Schmerzgrenze
        self.defense = agility  # Verteidigung
        self.corruption_threshold = math.ceil(willpower / 2)  # Korruptionsschwelle


class Player(BaseCharacter):

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
        super().__init__(name, race, attention, charisma, agility, secrecy, precision, acumen, strength, willpower)
        self.profession: str = ''
        self.weapons: List[Weapon] = []

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
            f"Zähigkeit: {self.toughness}/{self.perma_toughness}\tSchmerzgrenze: {self.pain_barrier}\n" \
            "---------------------------------------\n" \
            f"Aufmerksamkeit:\t{self.attention}\tAusstrahlung:\t{self.charisma}\n" \
            f"Gewandheit:\t\t{self.agility}\tHeimlichkeit:\t{self.secrecy}\n" \
            f"Präzision:\t\t{self.precision}\tScharfsinn:\t\t{self.acumen}\n" \
            f"Stärke:\t\t\t{self.strength}\tWillenskraft:\t{self.willpower}\n" \
            "---------------------------------------\n" \
            f"Waffen:\n{weapons}" \
            "---------------------------------------\n"
