from RPG.consts.game_states import ESTRAD_TRADER, ESTRAD_TRADER_TRADE_MENU, ESTRAD_TRADER_BUY, ESTRAD_TRADER_SELL
from RPG.bot_classes.base_dialog import BaseDialog
from RPG.consts.quest_items import FEDERATION_PASS
from RPG.consts.items import LITTLE_MED_PACK, LIGHT_SOLDIER_ARMOR_SET, LIGHT_LASER_RIFFLE, OLD_LASER_PISTOL
from RPG.bot_classes.trader import TradeMenu


class EstradTrader(BaseDialog):
    def __init__(self, game):
        super().__init__(game, ESTRAD_TRADER, 'Soldado De La República Intergaláctica', '¡Salud! Aquí '
                                                                                    'puedes obtener una base '
                                                                                    'kit de soldado de la Federación si u'
                                                                                    ' tienes una identificación, o '
                                                                                    'comprar equipo adicional,'
                                                                                    ' si lo básico no es suficiente para TI.',
                         '👨🏼')
        self.reply_keyboard.row('Muéstrame tus productos')
        self.reply_keyboard.row('Quiero conseguir un kit')
        self.reply_keyboard.row('Tengo que irme.')
        self.kit_given = False
        self.trade_menu = TradeMenu(game, self, ESTRAD_TRADER_TRADE_MENU, ESTRAD_TRADER_BUY, ESTRAD_TRADER_SELL,
                                    'Mira esto., '
                                    'lo que tengo.',
                                    [LITTLE_MED_PACK, OLD_LASER_PISTOL], 1.25)

    def handle(self, message):
        if message.text == 'Muéstrame tus productos':
            self.trade_menu.start(message)
        elif message.text == 'Quiero conseguir un kit':
            if FEDERATION_PASS in self.game.player.quest_items:
                if not self.kit_given:
                    self.game.player.add_item(LIGHT_LASER_RIFFLE)
                    self.game.player.add_item(LITTLE_MED_PACK)
                    self.game.player.add_item(LIGHT_SOLDIER_ARMOR_SET)
                    self.game.player.laser_ammo += 20
                    self.kit_given = True
                    self.say(message, 'Aquí tienes. Bienvenido a las filas de los colonizadores del planeta Estrada!')
                else:
                    self.say(message, "Un juego por mano, ya tienes el tuyo.")
            else:
                self.say(message, 'Lo siento, sin un soldado de la Federación, no puedo darte un kit de combate.')
        elif message.text == 'Tengo que irme.':
            self.say(message, 'Pasa otra vez.')
            self.game.estrad.colony.start(message)
        else:
            self.show_input_error(message)
