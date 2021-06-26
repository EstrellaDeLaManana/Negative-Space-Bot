from RPG.consts.game_states import CAPTAIN_BRIDGE
from RPG.bot_classes.locations.base_location import BaseLocation


class CaptainBridge(BaseLocation):
    def __init__(self, game, spaceship):
        super().__init__(game, CAPTAIN_BRIDGE, 'Puente de mando', 'Vas al puente del capitán., '
                                                                         'en todas partes se ven varios elementos '
                                                                         'control de la nave. En gran panorámica '
                                                                         'el ojo de buey abre una vista de la galaxia. A '
                                                                         'el panel de control principal que ves '
                                                                         'interfaz de control del ordenador de a bordo')
        self.spaceship = spaceship
        self.reply_keyboard.row('📟Ordenador de a bordo', '🛏Cabina personal')
        self.reply_keyboard.row('📦Bodega', '👣Salir de la nave')
        self.reply_keyboard.row('📟Menú principal')

    def handle(self, message):
        if message.text == '📟Ordenador de a bordo':
            self.spaceship.computer.start(message)
        elif message.text == '🛏Cabina personal':
            self.spaceship.cabin.start(message)
        elif message.text == '📦Bodega':
            self.spaceship.cargo_hold.start(message)
        elif message.text == '👣Salir de la nave':
            if not self.game.current_planet:
                self.game.bot.send_message(message.chat.id, '¿Un paseo espacial?0_o No es la mejor idea.',
                                               reply_markup=self.reply_keyboard)
            else:
                self.game.current_planet.start(message)
        elif message.text == '📟Menú principal':
            self.game.main_menu.start(message)
        else:
            self.show_input_error(message)
