from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import CREATE_SPACESHIP_MENU
from RPG.utilities import check_name_valid, check_spaceship_name_taken


class SpaceshipCreationMenu(BaseHandler):
    def __init__(self, game):
        super().__init__(game, CREATE_SPACESHIP_MENU)

    def show(self, message):
        self.game.bot.send_message(message.chat.id, '¿Cómo se llamará tu nave espacial?')

    def handle(self, message):
        if not check_name_valid(message.text):
            self.game.bot.send_message(message.chat.id,
                                       'El nombre de la nave debe tener más de 2 caracteres y contener solo '
                                       'letras de cualquier alfabeto y números. Prueba otro.')
        elif check_spaceship_name_taken(self.game.games, message.text):
            self.game.bot.send_message(message.chat.id,
                                       f'Por desgracia, el título {message.text} ya está ocupado. Prueba otro.')
        else:
            self.game.spaceship.name = message.text
            self.game.bot.send_message(message.chat.id,
                                       f'Bienvenido al juego, {self.game.player.name}')
            self.game.main_menu.start(message)
