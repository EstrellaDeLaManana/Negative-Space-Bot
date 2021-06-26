from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.bot_classes.locations.planets.base_planet import BasePlanet
from RPG.bot_classes.locations.planets.estrad.estrad_port import EstradPort
from RPG.bot_classes.locations.planets.estrad.estrad_security_soldier import EstradSecuritySoldier
from RPG.bot_classes.locations.planets.estrad.colony.estrad_colony import EstradColony
from RPG.bot_classes.locations.planets.estrad.forest.estrad_forest import EstradForest


class Estrad(BaseLocation):
    def __init__(self, game, player):
        super().__init__(game, None, 'Tablados',
                         'Es un pequeño planeta en el borde de la galaxia que posee un clima tropical. En este instante '
                         'el planeta está colonizado por la Federación Intergaláctica. Población mundial representada '
                         'los aborígenes locales, miembros de la raza Estradina, y los colonizadores Intergalácticos'
                         'Federación.')
        self.port = EstradPort(game)
        self.security_soldier = EstradSecuritySoldier(game, self.game.player)
        self.colony = EstradColony(game)
        self.forest = EstradForest(game)
        self.child_locations = [self.port, self.colony, self.forest]

    def get_info(self):
        return f'*{self.name}*\n' \
               f'{self.description}'

    def start(self, message):
        if self not in self.game.opened_planets:
            self.game.opened_planets.append(self)
        self.port.start(message)
