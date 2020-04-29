from RPG.consts.game_states import ESTRAD_PORT
from RPG.bot_classes.locations.base_location import BaseLocation


class EstradPort(BaseLocation):
    def __init__(self, game):
        super().__init__(game, ESTRAD_PORT, 'Порт Эстрада', 'Ты высаживаешься на заросшую джунглями планету, '
                                                            'здесь очень влажно, а плотный туман ограничивает твоё '
                                                            'поле зрения парой метров. Судя по символике,'
                                                            ' посадочная '
                                                            'площадка, на которой ты приземлился, принадлежит '
                                                            'здешней колонии Межгалактической Республики.')
        self.reply_keyboard.row('🏘В колонию', '🚀Назад на корабль')
        self.reply_keyboard.row('📟Главное меню')

    def handle(self, message):
        if message.text == '🚀Назад на корабль':
            self.game.spaceship.cabin.start(message)
        elif message.text == '🏘В колонию':
            self.game.estrad.security_soldier.start(message)
        elif message.text == '📟Главное меню':
            self.game.main_menu.start(message)
        else:
            self.show_input_error(message)
