from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import CREATE_PLAYER_MENU
from RPG.utilities import check_name_valid, check_player_name_taken


class PlayerCreationMenu(BaseHandler):
    def __init__(self, game):
        super().__init__(game, CREATE_PLAYER_MENU)

    def show(self, message):
        self.game.bot.send_message(message.chat.id, '¿Cómo te llamarán?')

    def handle(self, message):
        if not check_name_valid(message.text):
            self.game.bot.send_message(message.chat.id, 'El nombre debe tener más de 2 caracteres y solo debe contener '
                                                        'letras de cualquier alfabeto y números. Prueba otro.')
        elif check_player_name_taken(self.game.games, message.text):
            self.game.bot.send_message(message.chat.id, f'Por desgracia, el nombre {message.text} ya está ocupado. Prueba otro.')
        else:
            self.game.player.name = message.text
            self.game.spaceship_creation_menu.start(message)
