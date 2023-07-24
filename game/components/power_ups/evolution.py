from game.components.power_ups.power_up import PowerUp

from game.utils.constants import IMPROVE_SHOT, EVOLUTION_TYPE

class Evolution(PowerUp):
    def __init__(self):
        super().__init__(IMPROVE_SHOT, EVOLUTION_TYPE)