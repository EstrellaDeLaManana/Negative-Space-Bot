from RPG.bot_classes.locations.base_location import BaseLocation
from RPG.consts.game_states import ESTRAD_FOREST_LAKE


class ForestLake(BaseLocation):
    def __init__(self, game):
        super().__init__(game, ESTRAD_FOREST_LAKE, 'Lago', 'Giras a la izquierda y pasas mucho tiempo. '
                                                            'a través de las densas ramas de la flora exótica local, '
                                                            'pero de repente, dando otro paso adelante, '
                                                            ' te caes hasta las rodillas en el agua. Te das cuenta de que '
                                                            'aquí hay un enorme ozro, oculto por la niebla. Tal vez, '
                                                            'no vale la pena comprobar quién puede habitar en sus aguas...')

        self.reply_keyboard.row('⬅️ Atrás')

    def handle(self, message):
        if message.text == '⬅️ Atrás':
            self.game.estrad.forest.entry.start(message)
        else:
            self.show_input_error(message)
