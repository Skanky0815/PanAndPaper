import json
from typing import List, Dict

from Engine.Character.Behavior import Behavior
from Engine.Character.Character import Character


class Npc(Character):

    def __init__(
            self,
            name: str,
            race: str,
            health: int,
            dodge: int,
            armor: int,
            actions: int,
            behaviors: Dict
    ):
        super(Npc, self).__init__(name=name, health=health, armor=armor)
        self.actions: int = actions
        self.race: str = race
        self.dodge: int = dodge
        self.behaviors: List[Behavior] = []

        for behavior in behaviors:
            print(behavior)
            self.behaviors.append(Behavior(**behavior))

    def __str__(self) -> str:
        behaviors: str = ""
        for behavior in self.behaviors:
            behaviors += f"\t{behavior}\n"

        return "\n" \
            f"Name: {self.name}\n" \
            f"Race: {self.race}\n" \
            f"Leben: {self.health}/{self.max_health}\n" \
            "---------------------------------------\n" \
            f"Verhalten:\n{behaviors}" \
            "---------------------------------------\n"

    def is_alive(self):
        return self.health > 0

    def get_behavior(self, worth_comparing: int) -> Behavior:
        return next(behavior for behavior in self.behaviors if behavior.in_range(worth_comparing))


class Factory:

    @staticmethod
    def create_character(name) -> Npc:
        file = open(f"var/data/npcs/{name}.json", "r")

        data = file.read()
        file.close()

        return Npc(**json.loads(data))


