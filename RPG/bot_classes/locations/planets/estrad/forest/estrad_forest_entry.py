from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.consts.game_states import ESTRAD_FOREST_ENTRY


class ForestEntry(BaseLocation):
    def __init__(self, game):
        super().__init__(game, ESTRAD_FOREST_ENTRY, 'Entrada al bosque',
                         'A través de la niebla húmeda, te acercas a la entrada del denso bosque. Ante '
                         'ves el letrero de advertencia " _ ¡Peligro! Cuidado con las tribus nativas " y dos maneras, '
                         'izquierda y derecha.')
        self.reply_keyboard.row('⬅️A la izquierda', '➡️A la derecha')
        self.reply_keyboard.row('🏘Volver a la Colonia', '📟Menú principal')

    def handle(self, message):
        if message.text == '⬅️A la izquierda':
            self.game.estrad.forest.lake.start(message)
        elif message.text == '➡️A la derecha':
            self.game.bot.send_message(message.chat.id,
                                       'Tú eliges el camino de la izquierda. Mientras profundizas más en las profundidades del bosque, '
                                       'cada vez más empiezas a notar cómo los matorrales que te rodean, de vez en cuando '
                                       'se mueven extrañamente...')
            self.game.estrad.forest.field.start(message)
        elif message.text == '🏘Volver a la Colonia':
            self.game.estrad.colony.start(message)
        elif message.text == '📟Menú principal':
            self.game.main_menu.start(message)
        else:
            self.show_input_error(message)
