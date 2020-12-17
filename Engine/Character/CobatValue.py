class CombatValue:
    def __init__(self, base_value: int, modifier: int):
        self.__base_value = base_value
        self.__modifier = modifier

    def update_modifier(self, new_modifier: int):
        self.__modifier = new_modifier

    def modifier(self) -> int:
        return self.__modifier

    def value(self) -> int:
        return self.__base_value + self.__modifier

    def base_value(self) -> int:
        return self.__base_value


class MeleeCombatValue(CombatValue):
    def __init__(self, base_value: int, modifier: int = 0):
        super().__init__(base_value, modifier)


class RangeCombatValue(CombatValue):
    def __init__(self, base_value: int, modifier: int = 0):
        super().__init__(base_value, modifier)


class MagicCombatValue(CombatValue):
    def __init__(self, base_value: int, modifier: int = 0):
        super().__init__(base_value, modifier)
