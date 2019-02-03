import unittest
from unittest.mock import MagicMock

from Engine.Dices import Dice
from Engine.Test import Test, Result


class TestTest(unittest.TestCase):

    def test_damage_two_dices(self):
        test: Test = Test()

        dice_1: Dice = Dice(6)
        dice_1.roll = MagicMock(return_value=4)

        dice_2: Dice = Dice(6)
        dice_2.roll = MagicMock(return_value=5)

        self.assertEqual(10, test.damage([dice_1, dice_2], 1))

    def test_damage_one_dice(self):
        test: Test = Test()

        dice: Dice = Dice(6)
        dice.roll = MagicMock(return_value=3)

        self.assertEqual(5, test.damage([dice], 2))

    def test_damage_one_dice_without_modifier(self):
        test: Test = Test()

        dice: Dice = Dice(6)
        dice.roll = MagicMock(return_value=4)

        self.assertEqual(4, test.damage([dice]))

    def test_attribute(self):
        test: Test = Test()

        dice: Dice = Dice(20)
        dice.roll = MagicMock(return_value=10)

        result: Result = test.attribute(dice, 8, 2)
        self.assertEqual(10, result.dice_result)

    def test_attribute_without_modifier(self):
        test: Test = Test()

        dice: Dice = Dice(20)
        dice.roll = MagicMock(return_value=10)

        result: Result = test.attribute(dice, 8)
        self.assertEqual(10, result.dice_result)
