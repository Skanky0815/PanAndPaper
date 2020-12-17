from Engine.Battle.DamgeHandler import DamageHandler
from Engine.Character.Npc import Npc
from Engine.Character.Player import Player
from Engine.Dices import Dice
from Engine.Test import Test


class CharacterAttack:
    def __init__(self, test: Test, player: Player):
        self.__test: Test = test
        self.__player: Player = player
        self.__damage_handler = DamageHandler(test)

    def attack(self, enemy: Npc) -> None:
        if self.__try_to_attack():
            self.__make_damage(enemy)
        else:
            print(f"Es passiert nichts")

    def __try_to_attack(self) -> bool:
        return self.__test.attribute(
            Dice(20),
            self.__player.melee_combat.base_value(),
            self.__player.melee_combat.modifier()
        ).is_success()

    def __make_damage(self, enemy: Npc) -> None:
        damage: int = self.__test.damage(self.__player.weapons[0])
        self.__damage_handler.make_damage(damage, self.__player, enemy)

