from Engine.Character.Behavior import Behavior
from Engine.Character.Npc import Npc
from Engine.Character.Player import Player
from Engine.Dices import Dice
from Engine.Test import Test


class EnemyAttack:
    def __init__(self, test: Test, enemy: Npc):
        self.__test: Test = test
        self.__enemy: Npc = enemy

    def attack(self, player: Player) -> None:
        for actions in range(1, self.__enemy.actions):
            behavior: Behavior = self.__determine_behavior()
            print(behavior.text)
            # TODO: hier gehts weiter mit dem herausfinden, was die action macht :D

    def __determine_behavior(self) -> Behavior:
        behavior_value: int = Dice(20).roll()
        return self.__enemy.get_behavior(behavior_value)
