from RPG.consts.game_states import CARGO_HOLD
from RPG.bot_classes.locations.base_location import BaseLocation


class CargoHold(BaseLocation):
    def __init__(self, game, spaceship):
        super().__init__(game, CARGO_HOLD, 'Bodega', 'Entras en un amplio compartimento de carga. Hasta aquí '
                                                                 'está vacío. Más tarde, puedes transportar mercancías aquí.')
        self.spaceship = spaceship
        self.reply_keyboard.row('🚀Puente de mando', '🛏Cabina personal')
        self.reply_keyboard.row('👣Salir de la nave', '📟Menú principal')

    def handle(self, message):
        if message.text == '🚀Puente de mando':
            self.spaceship.captain_bridge.start(message)
        elif message.text == '📟Menú principal':
            self.game.main_menu.start(message)
        elif message.text == '👣Salir de la nave':
            if not self.game.current_planet:
                self.game.bot.send_message(message.chat.id, '¿Un paseo espacial?0_o No es la mejor idea.',
                                               reply_markup=self.reply_keyboard)
            else:
                self.game.current_planet.start(message)
        elif message.text == '🛏Cabina personal':
            self.spaceship.cabin.start(message)
        else:
            self.show_input_error(message)
