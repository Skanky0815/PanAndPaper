from typing import List

from Engine import Test
from Engine.Character import Character
from Engine.Character.Npc import Npc
from Engine.Command.BaseCommand import NpcCommand
from Engine.Dices import Dice
from Engine.Test import Result


class Fight(NpcCommand):

    def __init__(self, character: Character, test: Test, npc: Npc = None):
        super().__init__(do_text=f"{character.name} kämpft!")
        self.character: Character = character
        self.test: Test = test
        if npc:
            self.set_npc(npc)

    def set_npc(self, npc: Npc) -> None:
        self.text = f"Den {npc.name} angreifen."
        self.npc = npc

    def doing(self) -> bool:
        print(f"{self.character.name} versucht {self.npc.name} anzugreifen")
        test_result: Result = self.test.attribute(Dice(20), self.character.precision, self.npc.defense)
        if test_result.is_success():
            return self.__handle_success(test_result)
        else:
            return self.__handle_failure(test_result)

    def __handle_success(self, test_result: Result) -> bool:
        if test_result.is_critical_success():
            print(f"Das ist ein kritischer Erfolg! {self.character.name} greift mit seinem {self.character.weapons[0].name} + 1D6 an.")
            dices: List[Dice] = self.character.weapons[0].dices.copy()
            dices.append(Dice(6))
            return self.__handle_damage(self.test.damage(dices))
        else:
            print(f"Erfolg! {self.character.name} greift mit seinem {self.character.weapons[0].name} an.")
            return self.__handle_damage(self.test.damage(self.character.weapons[0].dices))

    def __handle_failure(self, test_result: Result) -> bool:
        if test_result.is_critical_failure():
            print(f"Kritischer Misserfolg! Es passiert nichts.")
        else:
            print(f"Es passiert nichts")
        return False

    def __handle_damage(self, damage: int) -> bool:
        wounds: int = damage - self.npc.armor
        wounds: int = wounds if wounds > 0 else 0

        self.npc.toughness += wounds

        print(f"{self.character.name} verursacht bei {self.npc.name} {wounds} Schaden.")
        return self.npc.toughness >= self.npc.perma_toughness
