import unittest

from Engine.Dices import Dice


class TestDice(unittest.TestCase):

    def test_d6(self):
        dice: Dice = Dice(6)
        self.assertGreaterEqual(dice.roll(), 1)
        self.assertLessEqual(dice.roll(), 6)

    def test_d20(self):
        dice: Dice = Dice(20)
        self.assertGreaterEqual(dice.roll(), 1)
        self.assertLessEqual(dice.roll(), 20)
