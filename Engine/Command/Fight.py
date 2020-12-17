from Engine import Test
from Engine.Battle.CharacterAttack import CharacterAttack
from Engine.Battle.EnemyAttack import EnemyAttack
from Engine.Character.Npc import Npc
from Engine.Character.Player import Player
from Engine.Command.BaseCommand import NpcCommand


class Fight(NpcCommand):

    def __init__(self, player: Player, test: Test, enemy: Npc):
        super().__init__(do_text=f"{player.name} kämpft!", text=f"Den {enemy.name} angreifen.", enemy=enemy)
        self.__player: Player = player
        self.__character_attack: CharacterAttack = CharacterAttack(player=player, test=test)
        self.__enemy_attack = EnemyAttack(enemy=enemy, test=test)

    def doing(self) -> bool:
        print(f"{self.__player.name} versucht {self.enemy.name} anzugreifen")
        self.__character_attack.attack(self.enemy)
        if self.enemy.is_alive():
            self.__enemy_attack.attack(self.__player)
            return False

        return True
