import Engine.Action as Action
from Engine.Character.Npc import Npc


class BaseCommand:

    def __init__(self, text: str = "", do_text: str = ""):
        self.text: str = text
        self.do_text: str = do_text
        self.__success_action: Action = None
        self.__failure_action: Action = None
        self.__success_text: str = ""
        self.__failure_text: str = ""

    def set_success(self, success_action: Action, text: str) -> None:
        self.__success_action = success_action
        self.__success_text = text

    def set_failure(self, failure_action: Action, text: str) -> None:
        self.__failure_action = failure_action
        self.__failure_text = text

    def do(self) -> bool:
        print(self.do_text)
        if self.doing():
            print(self.__success_text)
            if not self.__success_action:
                return True
            self.__success_action.run()
        else:
            print(self.__failure_text)
            if not self.__failure_action:
                return False
            self.__failure_action.run()

    def doing(self) -> bool:
        return True


class NpcCommand(BaseCommand):

    def __init__(self, text: str = "", do_text: str = "", npc: Npc = None):
        super().__init__(text, do_text)
        self.npc: Npc = npc
