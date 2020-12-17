from Engine.Character.Npc import Npc
from Engine.Command.BaseCommand import NpcCommand


class NpcStatus(NpcCommand):

    def __init__(self, enemy: Npc):
        super().__init__(text=f"Den Status von {enemy.name} abfragen.", enemy=enemy)

    def doing(self) -> bool:
        print(self.enemy)
        return False
