import telebot
from RPG.bot_classes.bot_base_handler import BotBaseHandler
from RPG.game_states import MAIN_MENU


class BotMainMenu(BotBaseHandler):
    def __init__(self, bot_game):
        super().__init__(bot_game, MAIN_MENU)

    def show(self, message):
        main_menu_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        main_menu_keyboard.row('🎒Инвентарь', '⛑Снаряжение')
        main_menu_keyboard.row('📒Журнал', '📟Профиль')
        self.bot_game.bot.send_message(message.chat.id, 'Главное меню', reply_markup=main_menu_keyboard)

    def handle(self, message):
        if message.text == '🎒Инвентарь':
            self.bot_game.inventory.start(message)
        elif message.text == '⛑Снаряжение':
            pass
        elif message.text == '📒Журнал':
            pass
        elif message.text == '📟Профиль':
            self.bot_game.player_profile.start(message)
        else:
            self.bot_game.bot.send_message(message.chat.id, 'Введено неверное значение')
