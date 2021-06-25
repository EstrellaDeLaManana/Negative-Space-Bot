from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.consts.game_states import ESTRAD_BAR


class EstradBar(BaseLocation):
    def __init__(self, game):
        super().__init__(game, ESTRAD_BAR, 'Bar " Harz brahmin"', 'Vas al Bar. Detrás de la barra se sientan '
                                                                     'varios soldados de la Federación. Ahora aquí '
                                                                     'no pasa nada interesante...')
        self.reply_keyboard.row('⬅️ Atrás')

    def handle(self, message):
        if message.text == '⬅️ Atrás':
            self.game.estrad.colony.start(message)
        else:
            self.show_input_error(message)
