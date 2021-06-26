from telebot.types import ReplyKeyboardMarkup
from RPG.bot_classes.base_handler import BaseHandler


class Container(BaseHandler):  # Clase base Dial todos los contenedores
    def __init__(self, game, state, description, item):
        super().__init__(game, state)
        self.description = description
        self.item = item

    def show(self, message):
        if self.item is not None:
            reply_keyboard = ReplyKeyboardMarkup(True, True)
            reply_keyboard.row('✔Tomar', '✖Dejar')
            self.game.bot.send_message(message.chat.id, self.description, reply_markup=reply_keyboard)
        else:
            reply_keyboard = ReplyKeyboardMarkup(True, True)
            reply_keyboard.row('⬅Atrás')
            self.game.bot.send_message(message.chat.id, 'El cajón está vacío', reply_markup=reply_keyboard)

    def handle(self, message):
        if self.item is not None:
            if message.text == '✔Tomar':
                self.game.player.add_item(self.item)
                self.item = None
                self.game.current_location.start(message)
            elif message.text == '✖Dejar':
                self.game.current_location.start(message)
            else:
                self.game.bot.send_message(message.chat.id, 'Se ha introducido un valor incorrecto')
        else:
            if message.text == '⬅Atrás':
                self.game.current_location.start(message)
            else:
                self.game.bot.send_message(message.chat.id, 'Se ha introducido un valor incorrecto')
