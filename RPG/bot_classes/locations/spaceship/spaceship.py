from RPG.bot_classes.locations.spaceship.cabin import Cabin
from RPG.bot_classes.locations.spaceship.captain_bridge import CaptainBridge
from RPG.bot_classes.locations.spaceship.cargo_hold import CargoHold
from RPG.bot_classes.locations.spaceship.computer import Computer


class Spaceship:
    def __init__(self, game):
        self.name = 'Vehículo espacial'
        self.hp = 100
        self.cargo = 0

        self.cabin = Cabin(game, self)
        self.captain_bridge = CaptainBridge(game, self)
        self.cargo_hold = CargoHold(game, self)
        self.computer = Computer(game, self)

        self.child_locations = [self.cabin, self.captain_bridge, self.cargo_hold]

    def get_info(self):
        info = f'🚀*{self.name}*\n' \
               f'💙_Resistencia_: {self.hp}/100\n' \
               f'📦_Bodega_:{self.cargo}/100'
        return info
