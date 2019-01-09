from typing import Callable, Dict

from Engine.Command.BaseCommand import BaseCommand
from Engine.Command.Exit import Exit


class Controller:

    def __init__(self):
        self.__default_commands: Dict[str, BaseCommand] = {"x": Exit()}

    def add_default_command(self, key: str, command: BaseCommand) -> None:
        self.__default_commands[key] = command

    def input_action(self, text: str, callback: Callable[[str], None] = None) -> bool:
        text += self.__setup_text()

        value: str = input(text)
        if value in self.__default_commands:
            self.__default_commands[value].do()
            return False

        if callback:
            callback(value)

        return False

    def __setup_text(self) -> str:
        text: str = "---------------------------------------\n"
        for idx, command in sorted(self.__default_commands.items()):
            text += f"[{idx}] {command.text}\t"
        text += "\n"
        return text
