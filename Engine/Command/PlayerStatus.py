from Engine.Character.Character import Player
from Engine.Command.BaseCommand import BaseCommand


class PlayerStatus(BaseCommand):

    def __init__(self, player: Player):
        super().__init__(text="Charakterbogen")
        self.__player = player

    def doing(self) -> bool:
        print(self.__player)
        return False
