from RPG.consts.game_states import CABIN
from RPG.bot_classes.locations.base_location import BaseLocation


class Cabin(BaseLocation):
    def __init__(self, game, spaceship):
        super().__init__(game, CABIN, 'Cabina privada', 'Estás en tu camarote personal, aquí está '
                                                          'una cámara en la que puedes curar tus heridas y '
                                                          'recuperar la fuerza, así como su Caja personal con las cosas. '
                                                          'En un pequeño ojo de buey observas el infinito Dalí '
                                                          'cosmos.')
        self.spaceship = spaceship
        self.reply_keyboard.row('🚀Puente de mando', '📦Bodega')
        self.reply_keyboard.row('👣Salir de la nave', '📟Menú principal')

    def handle(self, message):
        if message.text == '🚀Puente de mando':
            self.game.spaceship.captain_bridge.start(message)
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
