from Engine.Character.Character import Player
from Engine.Character.Npc import Npc
from Engine.Command.AtrributeTest import AttributeTest
from Engine.Command.BaseCommand import BaseCommand
from Engine.Command.Fight import Fight
from Engine.Command.NpcStatus import NpcStatus
from Engine.Test import Test


class Factory:

    def __init__(self, player: Player, test: Test):
        self.__player: Player = player
        self.__test: Test = test

    def create(self, command_data, npc: Npc = None) -> BaseCommand:
        return {
            "attribute_test": lambda: self.__attribute_test_command(command_data),
            "go": lambda: self.__go_command(command_data),
            "fight": lambda: self.__fight_command(npc),
            "npc_status": lambda: self.__npc_status(npc)
        }.get(command_data["command"])()

    def __attribute_test_command(self, command_data) -> BaseCommand:
        return AttributeTest(
            test=self.__test,
            modifier=command_data["modifier"],
            attribute_value=getattr(self.__player, command_data["attribute"]),
            text=command_data["text"].format(self.__player.name),
            do_text=command_data["do_text"].format(self.__player.name)
        )

    def __go_command(self, command_data) -> BaseCommand:
        return BaseCommand(
            text=command_data["text"].format(self.__player.name),
            do_text=command_data["do_text"].format(self.__player.name)
        )

    def __fight_command(self, npc: Npc) -> BaseCommand:
        return Fight(
            character=self.__player,
            test=self.__test,
            npc=npc
        )

    def __npc_status(self, npc: Npc) -> BaseCommand:
        return NpcStatus(npc=npc)
