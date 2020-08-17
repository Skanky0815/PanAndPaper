from Engine.Command.BaseCommand import BaseCommand
from Engine.Dices import Dice
from Engine.Test import Test, Result


class AttributeTest(BaseCommand):

    def __init__(self, test: Test, modifier: int, attribute_value: int, text: str, do_text: str):
        super().__init__(text=text, do_text=do_text)
        self.__test: Test = test
        self.__modifier: int = modifier
        self.__attribute_value: int = attribute_value

    def doing(self) -> bool:
        result: Result = self.__test.attribute(Dice(20), self.__attribute_value, self.__modifier)
        return result.is_success()
