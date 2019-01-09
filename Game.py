from Engine.Action import Factory as ActionFactory
from Engine.Command.Factory import Factory as CommandFactory
from Engine.Command.PlayerStatus import PlayerStatus
from Engine.Controller import Controller
from Engine.Costs import Costs
from Engine.Character.Character import Player
from Engine.Dices import Dice
from Engine.Test import Test
from Engine.Weapon import Weapon


class Game:
    """
    The game class handle the hole game, setup the actions and run the first

    Attributes:
        __player (Player)           The player character
        __test (Test)               The test class for the dice logic
        __controller (Controller)   The controller with handle the user input

    """

    def __init__(self):
        self.__player: Player = None
        self.__test: Test = Test()
        self.__controller: Controller = Controller()

        self.__setup()

    def __setup(self) -> None:
        self.__player = Player(
            "Syrax",
            "Goblin",
            attention=10,
            charisma=7,
            agility=11,
            secrecy=10,
            precision=9,
            acumen=13,
            strength=5,
            willpower=15
        )
        self.__player.weapons.append(Weapon("Parierdolch", [Dice(6)], 0, Costs(taler=5)))

    def run(self) -> None:
        self.__controller.input_action("Willkommen in Symbaroum!\nWie willst du heißen? (Syrax)\n", self.__run)

    def __run(self, name: str) -> None:
        if "" != name:
            self.__player.name = name

        print(f"Du bist der {self.__player.race} {self.__player.name}. Viel Spaß beim spielen.\n\n")

        self.__controller.add_default_command("c", PlayerStatus(self.__player))
        command_factory: CommandFactory = CommandFactory(self.__player, self.__test)
        action_factory: ActionFactory = ActionFactory(self.__player, self.__controller, command_factory)
        action_factory.start()
