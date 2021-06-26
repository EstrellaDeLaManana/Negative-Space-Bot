from telebot.types import ReplyKeyboardMarkup
from RPG.bot_classes.base_handler import BaseHandler
from RPG.consts.game_states import FIGHT_SYSTEM_PLAYER_TURN


class FightSystemPlayerTurn(BaseHandler):
    def __init__(self, game):
        super().__init__(game, FIGHT_SYSTEM_PLAYER_TURN)

    def show(self, message): # Muestra el teclado y las ODAS restantes para el turno del jugador
        self.game.state = FIGHT_SYSTEM_PLAYER_TURN
        self.reply_keyboard = ReplyKeyboardMarkup(True, True)
        if self.game.player.weapon:
            self.reply_keyboard.row(str(self.game.player.weapon), '📟 Abrir inventario - 3 OD')
        else:
            self.reply_keyboard.row('📟 Abrir inventario - 3 OD')
        self.reply_keyboard.row('✔ Закончить terminar el movimiento')
        self.game.fight_system.show_action_points(message, self.reply_keyboard)

    def handle(self, message):  # Manejador de movimientos del jugador
        if message.text == str(self.game.player.weapon):
            self.game.fight_system.weapon_use_menu.start(message)
        elif message.text == '📟 Abrir inventario - 3 OD':
            if self.game.fight_system.action_points >= 3:
                self.game.fight_system.action_points -= 3
                self.game.inventory.start(message)
            else:
                self.game.fight_system.show_action_points_error(message, self.reply_keyboard)
        elif message.text == '✔ Закончить terminar el movimiento':
            self.game.fight_system.max_action_points += 1
            self.game.fight_system.action_points = self.game.fight_system.max_action_points
            self.game.fight_system.start_enemy_turn(message)
        else:
            self.show_input_error(message)
