from Engine.Command.BaseCommand import BaseCommand


class Exit(BaseCommand):

    def __init__(self):
        super().__init__(text="Beenden")

    def doing(self) -> None:
        print("Machs gut Reisender!")
        exit()
