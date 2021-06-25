from telebot.types import ReplyKeyboardMarkup
from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import EQUIPMENT


class Equipment(BaseHandler):
    def __init__(self, game):
        super().__init__(game, EQUIPMENT)

    def show(self, message):
        self.reply_keyboard = ReplyKeyboardMarkup(True, True)
        if self.game.player.weapon is not None:
            self.reply_keyboard.row('🔫 Armas')
        if self.game.player.armor_set is not None:
            self.reply_keyboard.row('🧥 Kit de armadura')
        self.reply_keyboard.row('⬅ Atrás')
        self.game.bot.send_message(message.chat.id, self.game.player.get_equipment(), parse_mode="Markdown",
                                   reply_markup=self.reply_keyboard)

    def handle(self, message):
        if message.text == '⬅ Atrás':
            self.game.main_menu.start(message)
        elif message.text == '🔫 Armas':
            if self.game.player.weapon is not None:
                self.game.equipment_weapon_info.start(message)
            else:
                self.game.bot.send_message(message.chat.id, 'No lo tienes.', reply_markup=self.reply_keyboard)
        elif message.text == '🧥 Kit de armadura':
            if self.game.player.armor_set is not None:
                self.game.equipment_armor_info.start(message)
            else:
                self.game.bot.send_message(message.chat.id, 'No lo tienes.', reply_markup=self.reply_keyboard)
        else:
            self.show_input_error(message)
