from Engine.Character.Character import Character
from Engine.Command.BaseCommand import BaseCommand


class PlayerStatus(BaseCommand):

    def __init__(self, character: Character):
        super().__init__(text="Charakterbogen")
        self.__character = character

    def doing(self) -> bool:
        print(self.__character)
        return False
