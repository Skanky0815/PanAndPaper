import math

from Engine.Character.Character import Character
from Engine.Dices import Dice
from Engine.Test import Test


class DamageHandler:
    def __init__(self, test: Test):
        self.__test: Test = test

    def make_damage(self, damage: int, attacker: Character, defender: Character):
        if self.__enemy_dodge(defender.dodge):
            damage = math.ceil(damage / 2)
        self.__handle_damage(attacker, defender, damage)

    def __enemy_dodge(self, dodge: int) -> bool:
        return self.__test.attribute(Dice(20), dodge).is_success()

    def __handle_damage(self, attacker: Character, enemy: Character, damage: int) -> bool:
        wounds: int = damage - enemy.armor
        wounds: int = wounds if wounds > 0 else 0

        enemy.health -= wounds

        print(f"{attacker.name} verursacht bei {enemy.name} {wounds} Schaden.")
        return enemy.health <= 0