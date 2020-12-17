import json
import os
import random
from typing import List, Dict

from Engine.Character.Npc import Factory as NpcFactory, Npc
from Engine.Character.Character import Character
from Engine.Character.Player import Player
from Engine.Command.BaseCommand import BaseCommand
from Engine.Command.Factory import Factory as CommandFactory
from Engine.ConColor import *
from Engine.Controller import Controller


class Action:

    def __init__(self, key: str, controller: Controller, text: str, commands: List[BaseCommand] = None, npc: Npc = None):
        self.key = key
        self.__controller: Controller = controller
        self.__text: str = text
        self.__commands: List[BaseCommand] = commands
        self.__npc: Npc = npc

    def run(self) -> None:
        question: str = f"{self.__text}\n"
        if self.__npc:
            question: str = f"{self.__text % self.__npc.name}\n"

        for idx, command in enumerate(self.__commands):
            question += f"[{str(idx)}] {command.text}\n"

        if not self.__controller.input_action(question, self.__callback):
            self.run()

    def __callback(self, selected_command: str) -> None:
        selected_command: int = int(selected_command)
        if selected_command >= len(self.__commands):
            print(f"No option found for number {CRED + str(selected_command) + CEND}")
            self.run()
        else:
            if self.__commands[selected_command].do():
                print("Nächste action")
            else:
                self.run()


class Factory:

    __path: str = "var/data/scenery/"

    def __init__(self, player: Player, controller: Controller, command_factory: CommandFactory):
        self.__command_list: Dict[str, BaseCommand] = {}
        self.__action_list: Dict[str, Action] = {}
        self.__controller: Controller = controller
        self.__action_data_list = {}
        self.__player: Player = player
        self.__command_factory: CommandFactory = command_factory

        self.__setup_actions()

    def start(self) -> None:
        list(self.__action_list.values())[random.randint(0, len(self.__action_list) - 1)].run()

    def __setup_actions(self):
        for file_name in os.listdir(self.__path):
            if not file_name.lower().endswith(".json"):
                continue
            self.__create_action(file_name)

        for action_data in self.__action_data_list.values():
            for command_data in action_data["commands"]:
                if "success" in command_data:
                    self.__command_list[command_data["key"]].set_success(
                        self.__action_list[command_data["success"]["action"]],
                        command_data["success"]["text"].format(self.__player.name)
                    )
                if "failure" in command_data:
                    self.__command_list[command_data["key"]].set_failure(
                        self.__action_list[command_data["failure"]["action"]],
                        command_data["failure"]["text"].format(self.__player.name)
                    )

    def __create_action(self, name: str) -> None:
        file = open(f"{self.__path}{name}", "r")

        data = file.read()
        file.close()

        data = json.loads(data)
        self.__action_data_list[data["key"]] = data.copy()
        commands_data = data["commands"].copy()

        npc: Npc = None
        if data["npc"]:
            npc = NpcFactory.create_character(data["npc"])
            data["npc"] = npc

        data["commands"] = []

        data["text"] = data["text"].format(self.__player.name)
        data["controller"] = self.__controller
        for command_data in commands_data:
            command: BaseCommand = self.__command_factory.create(command_data, npc)
            self.__command_list[command_data["key"]] = command
            data["commands"].append(command)

        self.__action_list[data["key"]] = Action(**data)
