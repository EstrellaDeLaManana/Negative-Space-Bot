from RPG.consts.game_states import ESTRAD_SECURITY_SOLDIER
from RPG.consts.quest_items import FEDERATION_PASS
from RPG.bot_classes.base_dialog import BaseDialog


class EstradSecuritySoldier(BaseDialog):
    def __init__(self, game, player):
        super().__init__(game, ESTRAD_SECURITY_SOLDIER, 'Soldado De La República Intergaláctica',
                         'Te saludo en el planeta Estrada, en la Colonia República Intergaláctica. Presentais, '
                         'por favor, su pase.', '👮🏻‍♂️')
        self.player = player
        self.reply_keyboard.row(
            f'[🗣Carisma {self.player.charisma}/4] La alta dirección me envió para enviar un mensaje urgente. '
            'a sus superiores.')
        self.reply_keyboard.row('[💵250] ¿Hay algo que podamos hacer?')
        if FEDERATION_PASS in self.player.quest_items:
            self.reply_keyboard.row('Aquí está mi pase')
        self.reply_keyboard.row('Tengo que irme.')

    def handle(self, message):
        if (message.text ==
                f'[🗣Carisma {self.player.charisma}/4] La alta dirección me envió para enviar un mensaje urgente. '
                f'a sus superiores.'):
            if self.game.player.charisma >= 4:
                self.say(message, 'Muy bien, pasa.')
                self.game.estrad.colony.start(message)
            else:
                self.say(message, '¿A quién estás tratando de engañar? Me habrían advertido si'
                                  ' los jefes esperarían a alguien.')
        elif message.text == '[💵250] ¿Hay algo que podamos hacer?':
            if self.game.player.money >= 250:
                self.game.player.money -= 250
                self.say(message, 'Muy bien, pasa.')
                self.game.estrad.colony.start(message)
            else:
                self.say(message, 'No tienes dinero.')
        elif message.text == 'Aquí está mi pase':
            if FEDERATION_PASS in self.game.player.quest_items:
                self.say(message, 'Bien, ven')
                self.game.estrad.colony.start(message)
            else:
                self.say(message, 'Sí, no lo tienes, listo.')
        elif message.text == 'Tengo que irme.':
            self.say(message, 'Nos vemos..')
            self.game.estrad.start(message)
        else:
            self.show_input_error(message)
