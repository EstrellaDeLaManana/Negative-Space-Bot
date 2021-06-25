from RPG.bot_classes.locations.planets.estrad.colony.estrad_bar import EstradBar
from RPG.consts.game_states import ESTRAD_COLONY
from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.bot_classes.locations.planets.estrad.colony.estrad_trader import EstradTrader
from RPG.consts.quest_items import FEDERATION_PASS


class EstradColony(BaseLocation):
    def __init__(self, game):
        super().__init__(game, ESTRAD_COLONY, 'Colonia', 'Entras en un pequeño campamento militar. Al parecer, '
                                                         'los colonizadores llegaron aquí recientemente, instalación temporal '
                                                         'los módulos residenciales aún no están terminados, y los soldados están corriendo por todas partes '
                                                         'República, representantes de diferentes razas. Ves antes '
                                                         'un Bar local, punto de entrega de equipos'
                                                         ', la sede de los jefes y el camino a un bosque denso y brumoso.')
        self.reply_keyboard.row('🍻Bar', '🏪Punto de entrega de equipo')
        self.reply_keyboard.row('🏕Jefatura superior', '🌲Bosque')
        self.reply_keyboard.row('🚀Volver a la nave', '📟Menú principal')

        self.trader = EstradTrader(game)
        self.bar = EstradBar(game)

        self.child_locations = [self.bar]

    def handle(self, message):
        if message.text == '🍻Bar':
            self.bar.start(message)
        elif message.text == '🏪Punto de entrega de equipo':
            self.trader.start(message)
        elif message.text == '🏕Jefatura superior':
            if FEDERATION_PASS in self.game.player.quest_items:
                self.game.bot.send_message(message.chat.id, 'Ya tienes el pase, no tienes por qué ir allí.')
                self.start(message)
            else:
                self.game.player.quest_items.append(FEDERATION_PASS)
                self.game.bot.send_message(message.chat.id, 'Los jefes de la Colonia te han asignado a las filas de los colonizadores '
                                                            'planetas. Ahora tienes un pase de soldado '
                                                            'federación.')
                self.start(message)
        elif message.text == '🌲Bosque':
            self.game.estrad.forest.entry.start(message)
        elif message.text == '🚀Volver a la nave':
            self.game.spaceship.cabin.start(message)
        elif message.text == '📟Menú principal':
            self.game.main_menu.start(message)
        else:
            self.show_input_error(message)
