from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import JOURNAL


class Journal(BaseHandler):
    def __init__(self, game):
        super().__init__(game, JOURNAL)
        self.reply_keyboard.row('⬅ Atrás')

    def show(self, message):
        self.game.bot.send_message(message.chat.id, f'📒 *Tareas*\n'
                                                    f'_ Todavía no tienes ninguna asignación_ (lo cual no es sorprendente, su '
                                                    f'todavía no se puede recibir)', parse_mode='Markdown',
                                   reply_markup=self.reply_keyboard)

    def handle(self, message):
        if message.text == '⬅ Atrás':
            self.game.main_menu.start(message)
        else:
            self.show_input_error(message)
