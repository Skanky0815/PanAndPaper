from Engine.Character.Npc import Npc
from Engine.Command.BaseCommand import NpcCommand


class NpcStatus(NpcCommand):

    def __init__(self, npc: Npc):
        super().__init__(text=f"Den Status von {npc.name} abfragen.", npc=npc)

    def doing(self) -> bool:
        print(self.npc)
        return False

