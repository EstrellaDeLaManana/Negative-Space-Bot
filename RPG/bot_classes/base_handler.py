from telebot.types import ReplyKeyboardMarkup


class BaseHandler:  # Controlador base, todas las clases de bot_classes se heredan de él
    def __init__(self, game, game_state):
        self.game = game
        self.game_state = game_state
        self.reply_keyboard = ReplyKeyboardMarkup(True, True)

    def start(self, message):
        self.game.state = self.game_state
        self.show(message)

    def show(self, message):
        pass

    def handle(self, message):
        pass

    def show_input_error(self, message):
        self.game.bot.send_message(message.chat.id, 'Comando no válido introducido, inténtelo de nuevo.',
                                   reply_markup=self.reply_keyboard)
