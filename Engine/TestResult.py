class TestResult:
    def __init__(self, dice_result: int, value: int):
        self.dice_result: int = dice_result
        self.__value: int = value

    def is_critical_success(self) -> bool:
        return 1 == self.dice_result

    def is_critical_failure(self) -> bool:
        return 20 == self.dice_result

    def is_success(self) -> bool:
        return self.is_critical_success() or (self.dice_result <= self.__value)
