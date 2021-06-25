from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import MAIN_MENU


class MainMenu(BaseHandler):
    def __init__(self, game):
        super().__init__(game, MAIN_MENU)
        self.reply_keyboard.row('🎒Inventario', '⛑Equipamiento')
        self.reply_keyboard.row('📒Registro', '📟Perfil')
        self.reply_keyboard.row('👀Mirar alrededor')

    def show(self, message):
        self.game.bot.send_message(message.chat.id, 'Menú principal', reply_markup=self.reply_keyboard)

    def handle(self, message):
        if message.text == '🎒Inventario':
            self.game.inventory.start(message)
        elif message.text == '⛑Equipamiento':
            self.game.equipment.start(message)
        elif message.text == '📒Registro':
            self.game.journal.start(message)
        elif message.text == '📟Perfil':
            self.game.player_profile.start(message)
        elif message.text == '👀Mirar alrededor':
            self.game.current_location.start(message)
        else:
            self.game.bot.send_message(message.chat.id, 'Se ha introducido un valor incorrecto')
