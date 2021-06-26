from RPG.consts.game_states import ESTRAD_PORT
from RPG.bot_classes.locations.base_location import BaseLocation


class EstradPort(BaseLocation):
    def __init__(self, game):
        super().__init__(game, ESTRAD_PORT, 'Puerto Estrada', 'Estás aterrizando en un planeta cubierto de selva, '
                                                            'aquí está muy húmedo, y la densa niebla limita el tuyo '
                                                            'campo de visión por un par de metros. A juzgar por el simbolismo,'
                                                            ' de embarque '
                                                            'la plataforma en la que aterrizaste pertenece '
                                                            'es una Colonia de la República Intergaláctica.')
        self.reply_keyboard.row('🏘A la Colonia', '🚀Volver a la nave')
        self.reply_keyboard.row('📟Menú principal')

    def handle(self, message):
        if message.text == '🚀Volver a la nave':
            self.game.spaceship.cabin.start(message)
        elif message.text == '🏘A la Colonia':
            self.game.estrad.security_soldier.start(message)
        elif message.text == '📟Menú principal':
            self.game.main_menu.start(message)
        else:
            self.show_input_error(message)
