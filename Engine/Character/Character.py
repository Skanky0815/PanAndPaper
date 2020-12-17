class Character:
    def __init__(self, name: str, health: int, dodge: int = 0, armor: int = 0):
        self.name: str = name
        self.health: int = health
        self.armor: int = armor
        self.dodge: int = dodge
        self.max_health: int = health
