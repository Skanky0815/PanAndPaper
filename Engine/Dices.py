import random


class Dice:

    def __init__(self, value: int):
        self.name = "W" + str(value)
        self.__value = value

    def roll(self) -> int:
        return random.randint(1, self.__value)
