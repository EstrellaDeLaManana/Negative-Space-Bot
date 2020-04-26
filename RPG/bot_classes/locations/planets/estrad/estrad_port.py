from telebot.types import ReplyKeyboardMarkup
from RPG.game_states import ESTRAD_PORT
from RPG.bot_classes.locations.base_location import BaseLocation


class EstradPort(BaseLocation):
    def __init__(self, bot_game, estrad):
        super().__init__(bot_game, ESTRAD_PORT, 'Порт Эстрада', 'Ты высаживаешься на заросшую джунглями планету, '
                                                                'здесь очень влажно, а плотный туман ограничивает твоё '
                                                                'поле зрения парой метров. Судя по символике,'
                                                                ' посадочная '
                                                                'площадка, на которой ты приземлился, принадлежит '
                                                                'здешней колонии Межгалактической Республики.')
        self.reply_keyboard = ReplyKeyboardMarkup(True, True)
        self.reply_keyboard.row('🏘В колонию', '🚀Назад на корабль')

    def handle(self, message):
        if message.text == '🚀Назад на корабль':
            self.bot_game.spaceship[message.chat.id].cabin.start(message)
        else:
            self.bot_game.bot.send_message(message.chat.id, 'Да нельзя туда пока', reply_markup=self.reply_keyboard)
