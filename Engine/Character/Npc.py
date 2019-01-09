import json
from typing import List

from Engine.Character.Character import BaseCharacter
from Engine.Weapon import NpcWeapon


class Npc(BaseCharacter):

    def __init__(
            self,
            name: str,
            race: str,
            attention: int,
            attention_modifier: int,
            charisma: int,
            charisma_modifier: int,
            agility: int,
            agility_modifier: int,
            secrecy: int,
            secrecy_modifier: int,
            precision: int,
            precision_modifier: int,
            acumen: int,
            acumen_modifier: int,
            strength: int,
            strength_modifier: int,
            willpower: int,
            willpower_modifier: int,
            corruption: int,
            defense: int,
            armor: int,
            weapons: List[any]
    ):
        super().__init__(name, race, attention, charisma, agility, secrecy, precision, acumen, strength, willpower)
        self.corruption: int = corruption
        self.attention_modifier: int = attention_modifier
        self.charisma_modifier: int = charisma_modifier
        self.agility_modifier: int = agility_modifier
        self.secrecy_modifier: int = secrecy_modifier
        self.precision_modifier: int = precision_modifier
        self.acumen_modifier: int = acumen_modifier
        self.strength_modifier: int = strength_modifier
        self.willpower_modifier: int = willpower_modifier
        self.defense: int = defense
        self.armor: int = armor
        self.weapons: List[NpcWeapon] = []

        for weapon in weapons:
            self.weapons.append(NpcWeapon(**weapon))

    def __str__(self) -> str:
        weapons: str = ""
        for weapon in self.weapons:
            weapons += f"\tName: {weapon.name}, Schaden {weapon.damage}\n"

        return "\n" \
            f"Name: {self.name}\n" \
            f"Race: {self.race}\n" \
            f"Zähigkeit: {self.toughness}/{self.perma_toughness}\tSchmerzgrenze: {self.pain_barrier}\n" \
            "---------------------------------------\n" \
            f"Aufmerksamkeit:\t{self.attention} ({self.attention_modifier})\tAusstrahlung:\t{self.charisma} ({self.charisma_modifier})\n" \
            f"Gewandheit:\t\t{self.agility} ({self.agility_modifier})\tHeimlichkeit:\t{self.secrecy} ({self.secrecy_modifier})\n" \
            f"Präzision:\t\t{self.precision} ({self.precision_modifier})\tScharfsinn:\t\t{self.acumen} ({self.acumen_modifier})\n" \
            f"Stärke:\t\t\t{self.strength} ({self.strength_modifier})\tWillenskraft:\t{self.willpower} ({self.willpower_modifier})\n" \
            "---------------------------------------\n" \
            f"Waffen:\n{weapons}" \
            "---------------------------------------\n"


class Factory:

    @staticmethod
    def create_character(name) -> Npc:
        file = open(f"var/data/npcs/{name}.json", "r")

        data = file.read()
        file.close()

        return Npc(**json.loads(data))


