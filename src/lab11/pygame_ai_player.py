import random
from lab11.turn_combat import CombatPlayer


""" Create PyGameAIPlayer class here"""


class PyGameAIPlayer:
    def selectAction(self, state):
        return ord(str(random.randint(0, 9)))


""" Create PyGameAICombatPlayer class here"""


class PyGameAICombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        self.weapon = random.randint(0, 2)
        return self.weapon
